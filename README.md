# Datadog Certifications Drill

One practice app for Datadog certification exams, with a separate space for each certification.

> **Unofficial.** This is a personal study project. It is not made, endorsed, or reviewed by Datadog, and its questions are not real exam questions. For the official certifications, exam details, and free prep material, go to Datadog:
>
> - [Datadog Certification](https://www.datadoghq.com/certification/): the official program, registration, and policies
> - Datadog Fundamentals: [exam guide](https://www.datadoghq.com/pdf/datadog-fundamentals-exam-guide-aug-2026.pdf), [learning path](https://learn.datadoghq.com/bundles/datadog-fundamentals-certification-learning-path), [practice exam](https://learn.datadoghq.com/courses/datadog-fundamentals-practice-exam)
> - Log Management Fundamentals: [learning path](https://learn.datadoghq.com/bundles/log-management-fundamentals-certification-learning-path), [practice exam](https://learn.datadoghq.com/courses/log-management-fundamentals-practice-exam)
> - APM & Distributed Tracing Fundamentals: [learning path](https://learn.datadoghq.com/bundles/apm-distributed-tracing-fundamentals-certification-learning-path), [practice exam](https://learn.datadoghq.com/courses/apm-distributed-tracing-fundamentals-practice-exam)

| Space | Exam | Questions |
|---|---|---|
| Fundamentals | Datadog Fundamentals | 520 + Datadog's 25 practice questions |
| Log Management | Datadog Log Management Fundamentals | 525 + Datadog's 25 practice questions |
| APM | Datadog APM & Distributed Tracing Fundamentals | 530 + Datadog's 23 practice questions |

## Use it

Open `index.html` in the repo root in a browser. It works offline. Switch certifications with the selector at the top; each one keeps its own scores in that browser, and **Reset progress** only clears the certification you are in.

Each space has:

- **Full exam simulation**: 90 questions in 2 hours, the same length and time limit as the real exams
- **20 mock tests** of 25 questions, each covering every exam topic. After a test, **Last result** reopens your latest attempt in each mode
- **Focused drills** on the areas the exam leans on, a random 25, and retrying your mistakes
- **The official practice set**: Datadog's 25 practice questions, with explanations added
- **Practice by topic**, starting with questions you missed or haven't seen
- **Cheat sheet** covering the whole exam guide, with links to the source docs under each section

| | Study mode | Exam mode |
|---|---|---|
| Feedback | Right after each answer, with every option explained | None until you submit, then a full review |
| Timer | None | 80 seconds per question, the real exam's pace |
| Topic labels | Shown | Hidden, like the real exam |
| Changing answers | Locked once you answer | Change answers and flag questions until you submit |

Keys: `1`–`3` or `A`–`C` to answer, `Enter` to continue, `Esc` to leave. A session in progress survives a page reload.

## About the questions

- **3 options per question**, one correct, matching the official practice exams.
- **Every option is explained**: why the right answer is right and why each wrong one is wrong, with a link to the docs page behind it.
- **Checked against the live Datadog docs**: Fundamentals in October 2026, Log Management and APM in November 2026. Each Log Management and APM question was written from the current docs and then fact-checked by a second, independent pass.
- **Official practice sets**: Datadog's answer key is kept as-is. Where the product has changed since, the explanation adds a "Current docs:" note. Three APM practice questions come without a marked answer; their key comes from the current docs, and the explanation says so.
- The questions are original. Nothing was copied from exam-dump sites.

### Fundamentals: 520 questions in ten topics

| Topic | Questions |
|---|---|
| Data Collection & Integrations | 80 |
| Networking & Datadog Ports | 75 |
| Allotments, Billing & Custom Metrics | 75 |
| Computing Fundamentals | 60 |
| Troubleshooting the Agent | 49 |
| Tagging & Search | 45 |
| Agent Installation & Keys | 41 |
| Monitors & Alerts | 40 |
| Dashboards & Host Map | 35 |
| APM & Tracing (ddtrace) | 20 |

### Log Management: 525 questions across the exam guide's outline

| Domain | Subdomains (questions) |
|---|---|
| Logging Fundamentals | Logging Systems – Rationale & Justification (20), Logging Formats (25), Log Emission (25) |
| Log Collection | Enabling Log Collection (50), Log Filtering & Obfuscation (30), Processors & Pipelines (50), Standard Attributes (25) |
| Log Searching & Filtering | Live vs. Explorer (20), Search Syntax (45), Explorer Functionality (35) |
| Log Analysis | Filtering and Excluding (30), Aggregations (25), Visualizing (30) |
| Log Utilization | Monitors & Alerting (30), Metric Generation (25), Exporting (25) |
| Log Troubleshooting | Ingestion Issues (35) |

Detailed study notes for the whole guide are in [`dd-log-management/materials/study-notes.md`](dd-log-management/materials/study-notes.md).

### APM & Distributed Tracing: 530 questions across the exam guide's outline

| Domain | Subdomains (questions) |
|---|---|
| APM Fundamentals | APM Rationale (20), Datadog Approach to APM (20), Tracing Architectures (25), Language Level Differences — Automatic Instrumentation (25), OOTB Tracer vs Community Tracer (15), Tagging (30), Retention Periods for APM Data (25) |
| Application Instrumentation | Datadog Tracing Libraries (25), Instrumentation Types (25), Datadog Agent Architecture (25), Sampling vs Retention (30), APM Data Security (20), Profile Collection (25) |
| Insight Discovery | Software Catalog (20), Search Syntax (25), Trace Live vs Retained Search (20), Profilers (20), Deployment Tracking (20), Error Tracking (20), Span Summary (15), Service Performance Dashboards (25) |
| Troubleshooting Application using APM | Using Trace Search (during incident) (25), Monitors & Alerting (30) |

The exam guide in [`dd-apm/materials/`](dd-apm/materials/) is the 2025 edition; the questions follow the current docs, and [`dd-apm/materials/study-notes.md`](dd-apm/materials/study-notes.md) lists what changed in the product since.

## Project layout

The app code lives at the root. Each `dd-*` folder holds only one certification's content.

| Path | What it is |
|---|---|
| `index.html` | The built app. Generated by the build script; don't edit it by hand |
| `src/template.html` | App UI (HTML, CSS, JavaScript) |
| `src/build.py` | Finds every track, checks its questions, deals the mock tests, and writes `index.html` |
| `dd-*/track.json` | The track's title, saved-progress key, question files, focused drills, and official set |
| `dd-*/questions/` | `pool_*.json` question banks and `official.json`, the official practice set with explanations |
| `dd-*/cheatsheet.html` | The track's cheat sheet and its source links |
| `dd-*/materials/` | Exam guide, official practice questions, and study notes. Not needed to build |
| `dd-fundamental/index.html` | Forwards the old address to the new app and carries saved progress along |

To add another certification, create a `dd-<name>/` folder with `track.json`, `questions/` and `cheatsheet.html`, then rebuild. It appears in the selector automatically.

## Edit and rebuild

Edit the files in a track folder or in `src/`, then rebuild from the repo root:

```bash
python3 src/build.py
```

Each question looks like this:

```json
{
  "id": "net-002",
  "topic": "Networking & Datadog Ports",
  "subtopic": "Datadog Ports",
  "difficulty": "easy",
  "q": "What is the default port and protocol of the DogStatsD server bundled with the Agent?",
  "options": ["8126/TCP", "8125/TCP", "8125/UDP"],
  "answer": 2,
  "explanation": "DogStatsD listens on UDP 8125 by default. 8126/TCP is the APM trace receiver.",
  "notes": [
    "8126/TCP is the APM trace receiver.",
    "DogStatsD uses UDP, not TCP, on 8125.",
    "DogStatsD listens on 8125/UDP by default (enabled by default since Agent 6)."
  ],
  "ref": "https://docs.datadoghq.com/developers/dogstatsd/",
  "verified": "2026-10"
}
```

- `answer` is the 0-based index of the correct option. Options are shuffled every time a question is shown.
- `notes` has one entry per option, in the same order.
- Use `\n` in `q` to show a config or code snippet. Wrap inline code in backticks.

The build prints a `PROBLEM` line and exits with an error code if a question doesn't have exactly 3 options, has an out-of-range `answer`, repeats an option, has the wrong number of notes, is missing its text or explanation, or reuses an `id` or question text within a track. It still writes `index.html`, so fix any problems and rebuild.
