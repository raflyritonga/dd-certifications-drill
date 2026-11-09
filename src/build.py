"""Validate each track's questions, deal them into mock tests, and build the single-page app (index.html).

A track is any dd-*/ folder with a track.json. It holds only content:
  track.json        title, storage key, pools, focused drills, official and private sets
  questions/        pool_*.json and official.json
  cheatsheet.html   the track's cheat sheet (HTML fragment)
  materials/        exam guide, practice questions, study notes (not needed to build)

Usage (from the repo root): python3 src/build.py [--artifact OUT_FRAGMENT]
"""
import json, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # the repo root
PER_PACKAGE = 25
SEED = 2026
KEEP = ("id", "topic", "subtopic", "difficulty", "q", "options", "answer", "explanation", "notes", "ref", "verified")


def check(qs, problems):
    for q in qs:
        opts = q.get("options", [])
        if len(opts) != 3:  # the real exams use 3 options per question
            problems.append(f"{q['id']}: {len(opts)} options, expected 3")
        if not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(opts)):
            problems.append(f"{q['id']}: bad answer index")
        if len(set(o.strip() for o in opts)) != len(opts):
            problems.append(f"{q['id']}: duplicate options")
        if q.get("notes") and len(q["notes"]) != len(opts):
            problems.append(f"{q['id']}: {len(q['notes'])} notes for {len(opts)} options")
        for k in ("q", "topic", "explanation"):
            if not q.get(k):
                problems.append(f"{q['id']}: missing {k}")


def load_pools(track, cfg):
    qs, problems = [], []
    for name in cfg["pools"]:
        path = track / "questions" / f"{name}.json"
        if not path.exists():
            problems.append(f"missing {path.relative_to(ROOT)}")
            continue
        qs += json.loads(path.read_text())
    check(qs, problems)
    ids = Counter(q["id"] for q in qs)
    problems += [f"duplicate id {i}" for i, c in ids.items() if c > 1]
    stems = Counter(re.sub(r"\W+", " ", q["q"].lower()).strip() for q in qs)
    problems += [f"duplicate stem: {s[:70]}" for s, c in stems.items() if c > 1]
    return qs, problems


def interleave_by_subtopic(items, rng):
    groups = defaultdict(list)
    for q in items:
        groups[q.get("subtopic", "")].append(q)
    for g in groups.values():
        rng.shuffle(g)
    order = sorted(groups.values(), key=len, reverse=True)
    out = []
    while any(order):
        for g in order:
            if g:
                out.append(g.pop())
    return out


def deal(qs, n_packages):
    rng = random.Random(SEED)
    target = n_packages * PER_PACKAGE
    topics = list(dict.fromkeys(q["topic"] for q in qs))
    by_topic = {t: [q for q in qs if q["topic"] == t] for t in topics}
    # the bank can hold more than the mock tests need; give each topic a share of the slots
    # proportional to its size (largest remainder), so topic weighting stays the same.
    # Questions left out of the mock tests stay in the bank for drills and the full simulation.
    if len(qs) > target:
        exact = {t: target * len(v) / len(qs) for t, v in by_topic.items()}
        quota = {t: int(x) for t, x in exact.items()}
        for t in sorted(exact, key=lambda t: exact[t] - quota[t], reverse=True)[:target - sum(quota.values())]:
            quota[t] += 1
        # every topic appears in every mock test when it has enough questions
        for t in topics:
            while quota[t] < min(len(by_topic[t]), n_packages):
                quota[t] += 1
                quota[max(quota, key=quota.get)] -= 1
        for t in topics:
            rng.shuffle(by_topic[t])
            by_topic[t] = by_topic[t][:quota[t]]
    packages, c = [[] for _ in range(n_packages)], 0
    for t in topics:
        for q in interleave_by_subtopic(by_topic[t], rng):
            packages[c % n_packages].append(q["id"])
            c += 1
    for pk in packages:
        rng.shuffle(pk)
    return packages


def parse_official(path, ref, prefix):
    """Fallback when questions/official.json is missing: read the practice-exam Markdown as-is."""
    out = []
    for block in re.split(r"\n\s*\n", path.read_text().strip()):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
        m = re.match(r"(\d+)\.\s*(.*)", lines[0])
        num, stem = int(m.group(1)), re.sub(r"\s*\(Choose only ONE best answer\)\s*$", "", m.group(2))
        opts, ans = [], None
        for l in lines[1:]:
            om = re.match(r"([A-D])\.\s*(.*)", l)
            if not om:
                stem += "\n" + l
                continue
            body = om.group(2).strip()
            if re.search(r"\(correct\)\s*$", body, re.I):
                ans = len(opts)
                body = re.sub(r"\s*\(correct\)\s*$", "", body, flags=re.I)
            opts.append(body)
        out.append({"id": f"{prefix}official-{num:02d}", "topic": "Official practice set", "subtopic": "", "difficulty": "",
                    "q": stem, "options": opts, "answer": ans,
                    "explanation": "Answer from the official Datadog practice exam.", "ref": ref})
    # a practice file can leave a question unmarked; skip it here (official.json supplies a key from the docs)
    return [q for q in out if q["answer"] is not None]


def slim(qs):
    return [{k: q.get(k, "") for k in KEEP} for q in qs]


def build_track(track, cfg):
    qs, problems = load_pools(track, cfg)
    if not qs:
        return None, problems
    n_packages = max(1, min(cfg.get("packages", 20), len(qs) // PER_PACKAGE))
    packages = deal(qs, n_packages)
    off = cfg.get("official")
    official = []
    if off:
        path = track / off["file"]
        if path.exists():
            official = json.loads(path.read_text())
        elif (track / off["source"]).exists():
            official = parse_official(track / off["source"], off["ref"], off.get("prefix", ""))
        check(official, problems)
    data = {
        "key": cfg["key"], "title": cfg["title"], "short": cfg["short"], "storage": cfg["storage"],
        "checked": cfg["checked"], "focus": cfg.get("focus", []), "private": bool(cfg.get("private")),
        "questions": slim(qs), "packages": packages, "official": slim(official),
    }
    write_private(track, cfg)
    print(f"[{cfg['key']}] {len(qs)} questions, {len(official)} official, "
          f"{n_packages} mock tests ({sum(map(len, packages))} questions in them)")
    print(f"  answer-position spread: {dict(sorted(Counter(q['answer'] for q in qs).items()))}"
          f", difficulty: {dict(Counter(q.get('difficulty') for q in qs))}")
    return data, problems


def write_private(track, cfg):
    """Private sets live in the track's materials/ and are kept out of Git. They go into a separate
    script that index.html loads if it exists, so the shared app never contains them."""
    p = cfg.get("private")
    if not p:
        return
    src, js = track / p["file"], track / "materials" / "extra-sets.js"
    if src.exists():
        sets = [{"key": p["key"], "title": p["title"], "desc": p["desc"], "questions": slim(json.loads(src.read_text()))}]
        js.write_text(f"(window.DD_EXTRA = window.DD_EXTRA || {{}})[{json.dumps(cfg['key'])}] = "
                      + json.dumps(sets, ensure_ascii=False) + ";\n")
        print(f"  private set: {js.relative_to(ROOT)} (+{len(sets[0]['questions'])} questions)")
    else:
        js.unlink(missing_ok=True)


def main():
    tracks, sheets, tags, problems = [], [], [], []
    for cfg_path in sorted(ROOT.glob("dd-*/track.json")):
        track, cfg = cfg_path.parent, json.loads(cfg_path.read_text())
        data, probs = build_track(track, cfg)
        problems += [f"[{cfg['key']}] {p}" for p in probs]
        if not data:
            print(f"[{cfg['key']}] skipped: no questions yet")
            continue
        tracks.append((cfg.get("order", 99), data))
        sheet = track / "cheatsheet.html"
        body = sheet.read_text() if sheet.exists() else '<div class="sheet"><p class="muted">No cheat sheet yet.</p></div>'
        sheets.append(f'<template id="sheet-{cfg["key"]}">{body}</template>')
        if cfg.get("private"):
            tags.append(f'<script src="{track.name}/materials/extra-sets.js"></script>')
    for p in problems:
        print("  PROBLEM", p)
    tracks = [d for _, d in sorted(tracks, key=lambda x: x[0])]
    blob = json.dumps({"tracks": tracks}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = (ROOT / "src" / "template.html").read_text().replace("/*__DATA__*/null", blob).replace("<!--__SHEETS__-->", "\n".join(sheets))
    # the shipped page tries to load each track's materials/extra-sets.js; the artifact never does
    (ROOT / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + page.replace("<!--__EXTRA__-->", "\n".join(tags)) + "\n</body>\n</html>\n")
    if "--artifact" in sys.argv:
        Path(sys.argv[sys.argv.index("--artifact") + 1]).write_text(page.replace("<!--__EXTRA__-->", ""))
    print(f"index.html: {', '.join(t['short'] for t in tracks)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
