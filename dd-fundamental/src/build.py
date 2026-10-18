"""Validate the question pools, deal them into 20 balanced packages of 25, and build index.html.

Usage (from the app folder): python3 src/build.py [--artifact OUT_FRAGMENT]
"""
import json, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # the app folder
SOURCES = ROOT / "materials"  # exam guide, practice exam file, study notes
POOLS = ["pool_fund", "pool_net", "pool_allot", "pool_agent", "pool_data", "pool_viz"]
N_PACKAGES, PER_PACKAGE = 20, 25
SEED = 2026


def load_pools():
    qs, problems = [], []
    for name in POOLS:
        items = json.loads((ROOT / "questions" / f"{name}.json").read_text())
        for q in items:
            q["pool"] = name
            opts = q.get("options", [])
            if len(opts) != 3:  # the real exam uses 3 options per question
                problems.append(f"{q['id']}: {len(opts)} options, expected 3")
            if not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(opts)):
                problems.append(f"{q['id']}: bad answer index")
            if len(set(o.strip() for o in opts)) != len(opts):
                problems.append(f"{q['id']}: duplicate options")
            for k in ("q", "topic", "explanation"):
                if not q.get(k):
                    problems.append(f"{q['id']}: missing {k}")
        qs += items
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


def deal(qs):
    rng = random.Random(SEED)
    target = N_PACKAGES * PER_PACKAGE
    topics = list(dict.fromkeys(q["topic"] for q in qs))
    by_pool = {t: [q for q in qs if q["topic"] == t] for t in topics}
    # trim any surplus from the largest pools so the total is exactly 500
    while sum(map(len, by_pool.values())) > target:
        biggest = max(by_pool, key=lambda p: len(by_pool[p]))
        by_pool[biggest].pop(rng.randrange(len(by_pool[biggest])))
    packages, c = [[] for _ in range(N_PACKAGES)], 0
    for t in topics:
        for q in interleave_by_subtopic(by_pool[t], rng):
            packages[c % N_PACKAGES].append(q["id"])
            c += 1
    for pk in packages:
        rng.shuffle(pk)
    used = {i for pk in packages for i in pk}
    return packages, [q for q in qs if q["id"] in used]


def parse_official():
    text = (SOURCES / "datadog-fundamentals-certification-practice-exam-questions.md").read_text()
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
        m = re.match(r"(\d+)\.\s*(.*)", lines[0])
        num, stem = int(m.group(1)), m.group(2)
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
        out.append({
            "id": f"official-{num:02d}", "topic": "Official practice set", "subtopic": "", "difficulty": "",
            "q": stem, "options": opts, "answer": ans,
            "explanation": "Answer from the official Datadog practice exam.",
            "ref": "https://learn.datadoghq.com/courses/datadog-fundamentals-practice-exam",
        })
    assert all(q["answer"] is not None for q in out), "official question without answer"
    return out


def main():
    qs, problems = load_pools()
    print(f"{len(qs)} questions loaded")
    for p in problems:
        print("  PROBLEM", p)
    packages, used = deal(qs)
    off_path = ROOT / "questions" / "official.json"
    official = json.loads(off_path.read_text()) if off_path.exists() else parse_official()
    keep = ("id", "topic", "subtopic", "difficulty", "q", "options", "answer", "explanation", "notes", "ref", "verified")
    data = {
        "questions": [{k: q.get(k, "") for k in keep} for q in used],
        "packages": packages,
        "checked": "October 2026",
        "official": [{k: q.get(k, "") for k in keep} for q in official],
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = (ROOT / "src" / "template.html").read_text().replace("/*__DATA__*/null", blob)
    page = page.replace("<!--__SHEET__-->", (ROOT / "src" / "cheatsheet.html").read_text())
    (ROOT / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + page + "\n</body>\n</html>\n")
    if "--artifact" in sys.argv:
        Path(sys.argv[sys.argv.index("--artifact") + 1]).write_text(page)
    print(f"packages: {[len(p) for p in packages]}")
    for i, pk in enumerate(packages[:3]):
        print(f"  P{i+1} topics:", dict(Counter(next(q['topic'] for q in used if q['id'] == x) for x in pk)))
    print("answer-position spread:", dict(Counter(q["answer"] for q in used)))
    print("difficulty:", dict(Counter(q.get("difficulty") for q in used)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
