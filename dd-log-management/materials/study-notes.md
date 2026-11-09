# Datadog Log Management Fundamentals — Study Notes

Built from the Log Management Fundamentals exam guide (v2, August 2026), the 25 official practice questions, and the Datadog docs pages behind each subdomain. Every fact was re-checked against the live docs in November 2026. Each section ends with a Sources line listing the pages it came from.

# The exam guide

## What the exam covers
- The Log Management Fundamentals exam is for people who can show an overall knowledge of Datadog Log Management, **independent of a specific job role**.
- Topics it tests (from the guide's introduction):
  - Understand logging: systems, formats, emission
  - Understand log collection in Datadog
  - Understand and use log parsing and associated rules
  - Understand how to search and filter logs
  - Understand how to use logs for analysis in troubleshooting
- The guide calls it a **pilot exam** with a **maximum seat time of 2 hours**.

## Intended candidates
- Ideal candidates have **at least 6 months of experience** with Datadog Log Management and its associated features, and understand how Log Management works and how it is best used in production.
- Roles named in the guide: Site Reliability Engineer, DevOps Engineer, Cloud/Infrastructure Engineer, Application Support Engineer, Security engineer, Software engineer, Engineering manager, Platform/Observability engineers, Compliance/Audit teams. The certification is open to candidates from any background.
- Recommended Datadog knowledge ("substantial knowledge" of): Logging Fundamentals, Log Collection, Log Parsing, Log Searching & Filtering, Log Analysis, Log Utilization, Log Troubleshooting.

## Exam format and scoring
| Item | Value |
|---|---|
| Total questions | **90** multiple-choice |
| Scored questions | **75** (count toward the final score) |
| Pre-test questions | **15**, unscored, not identified to the candidate |
| Seat time | 2 hours maximum |
| Unanswered questions | Scored as incorrect, so answer everything |

- **Pre-test items**: Datadog collects candidate performance on the 15 pre-test questions to evaluate them for future exam forms. They do not affect your score and look like any other question.
- The guide does not publish a passing score.

## Question type
- Only one type: **multiple choice** with **one correct response** and **two or more incorrect responses (distractors)**.
- Pick the response that **most accurately** answers the question. Distractors are written to look plausible in the context of the question. The official practice questions have three options each and say "Choose only ONE best answer".

## Out of scope (non-exhaustive list from the guide)
- Programming
- Systems Architecture
- Testing
- Cross-product Applications of Logs (for example Cloud SIEM, APM correlation: know the concept only)
- Observability Pipelines (on-premises processing, scrubbing and forwarding)

## Content outline
The guide lists domains and subdomains without weights. The outline table repeats the **Log Collection** header at the top of page 3, so Processors & Pipelines and Standard Attributes sit under Log Collection; the guide's introduction and recommended knowledge call this area **Log Parsing**.

| Domain | Subdomain | What it covers |
|---|---|---|
| Logging Fundamentals | Logging Systems – Rationale & Justification | Why organisations log (troubleshooting, audit, security), logs vs metrics vs traces, severity levels, Logging without Limits, indexes, Flex Logs, archives, Linux log locations |
| Logging Fundamentals | Logging Formats | Structured (JSON) vs unstructured logs, reserved attributes, JSON preprocessing, timestamps, multi-line logs, size limits |
| Logging Fundamentals | Log Emission | How apps and systems produce logs: files, stdout/stderr, syslog, journald, Windows Event Log, logging libraries, browser SDK, HTTP intake API |
| Log Collection | Enabling Log Collection | `logs_enabled`, Agent config files, `conf.d` log sources, tags and unified service tagging, permissions, Docker, Kubernetes, transport, cloud forwarders |
| Log Collection | Log Filtering & Obfuscation | Agent processing rules (`exclude_at_match`, `include_at_match`, `mask_sequences`, `multi_line`), auto multi-line, Sensitive Data Scanner, deleting sensitive logs |
| Log Collection (Log Parsing) | Processors & Pipelines | Pipeline filters and order, integration pipelines, Grok parser, remappers, enrichment processors, Pipeline Scanner, Auto-Processing |
| Log Collection (Log Parsing) | Standard Attributes | Naming convention, default standard attributes, aliasing, Attribute Remapper, facets on standard attributes |
| Log Searching & Filtering | Live vs. Explorer | Live Tail (all ingested logs, real time) vs Log Explorer (indexed logs, retention), time ranges, Flex and archives |
| Log Searching & Filtering | Search Syntax | Boolean operators, free text vs full text, attributes and tags, escaping, wildcards, ranges, CIDR, arrays |
| Log Searching & Filtering | Explorer Functionality | Search bar, facets and measures, list view and columns, side panel, saved views, calculated fields, Watchdog Insights |
| Log Analysis | Filtering and Excluding | Facet-panel filtering, negation, indexes and index filters, exclusion filters and sampling, daily quotas, retention |
| Log Analysis | Aggregations | Group into Fields / Patterns / Transactions, unique counts and measures, top N nesting, formulas, functions, rollups |
| Log Analysis | Visualizing | List, Timeseries, Top List, Table, Pie, Tree Map, dashboard widgets, template variables, notebooks |
| Log Utilization | Monitors & Alerting | Log monitors (indexed logs, 2-day window), group by, thresholds, no data, notification variables, log samples, Watchdog |
| Log Utilization | Metric Generation | Log-based metrics from the ingest stream, count vs distribution, group by, 15-month retention, custom metric billing |
| Log Utilization | Exporting | Export menu, CSV limits, archives, rehydration, Archive Search, forwarding to custom destinations, Logs API |
| Log Troubleshooting | Ingestion Issues | Where a log stops: Agent config, commands, permissions, network, intake limits, indexing, timestamps, status, parsing |

## Recommended learning resources
- **Log Management Fundamentals Certification Learning Path**: 16 courses covering key exam topics (completing it does not guarantee a pass). https://learn.datadoghq.com/bundles/log-management-fundamentals-certification-learning-path
- **Practice exam**: 25 questions, free, take it any time at your own pace. https://learn.datadoghq.com/courses/log-management-fundamentals-practice-exam
- **Documentation** the guide says candidates might otherwise overlook:
  - Log Management: https://docs.datadoghq.com/logs/
  - Host Agent Log Collection: https://docs.datadoghq.com/agent/logs/?tab=tailfiles
  - Agent Configuration Files: https://docs.datadoghq.com/agent/configuration/agent-configuration-files/
  - Getting Started with Tags: https://docs.datadoghq.com/getting_started/tagging/
- **Datadog Foundational Enablement technical training** (instructor-led, 60-minute sessions with demos):
  - Foundation Enablement: Log Management: https://www.datadoghq.com/technical-enablement/sessions/log-management/
  - Foundation Enablement: Intermediate Log Management: https://www.datadoghq.com/technical-enablement/sessions/log-management-intermediate/
  - Foundation Enablement: Introduction to Monitors: https://www.datadoghq.com/technical-enablement/sessions/monitors/
  - Foundation Enablement: Tagging: https://www.datadoghq.com/technical-enablement/sessions/tagging/

## What the official practice questions lean on
The 25 official practice questions spread across every domain. The topics they hit most:
- **Search syntax**: `status:error and info` (status attribute plus a free-text word in the message), and two values on one reserved attribute, where the answer key gives `source:nginx AND source:redis`. Know the key's answer, but in the product a log has one `source`, so an AND of two values matches nothing; `source:(nginx OR redis)` returns logs from either. Operators are case-sensitive in the product: write `AND`/`OR` in uppercase (no operator = implicit AND).
- **Agent filtering and scrubbing**: `exclude_at_match` to drop logs by value, `mask_sequences` to hide sensitive data.
- **Log Explorer handling**: drag columns by the 6-dot handle, add sortable columns from Options or the facet panel, Group into Fields to count by facet, Timeseries/Table split by up to 3 facets.
- **Export menu**: Generate New Metric for long-term KPIs (15-month retention), Export to Monitor to notify stakeholders.
- **Collection basics**: JSON is parsed automatically, `/var/log/` holds Linux logs, the Agent tails files on disk, `dd-agent` owns `/var/log/datadog/`, `configcheck` prints loaded configs, JavaScript apps use the SDK, browser logs are not stored by default.
- **Pipelines**: a custom pipeline filtered on the tagged `source` parses JSON from a source with no integration.
- **Concepts**: logs explain why things failed and serve audit/compliance; Logging without Limits lets you archive all logs; Cloud SIEM detects security signals from logs; template variables build dynamic dashboard links in alerts; standard attributes make logs easy to search.

Sources: https://learn.datadoghq.com/bundles/log-management-fundamentals-certification-learning-path, https://learn.datadoghq.com/courses/log-management-fundamentals-practice-exam

# Domain 1: Logging Fundamentals

## Logging Systems – Rationale & Justification

### Why organisations log
- Logs are written, timestamped records of discrete events. They answer **why** something happened: the specific error message, stack trace, user, request or config change behind a failure.
- Main reasons to log:
  - **Troubleshooting / root cause**: Logging without Limits gives "a streamlined troubleshooting experience in the Log Explorer" so teams can "quickly assess and fix" infrastructure issues.
  - **Audit and compliance**: archives "support your security and IT teams during audits and assessments"; archives keep logs "for longer periods of time and meet compliance requirements while also keeping auditability for ad-hoc investigations".
  - **Security investigation**: Flex Logs and archives are positioned for "security investigations" and "compliance audit"; Cloud SIEM detects threats from ingested logs *without requiring you to index them* (cross-product detail, only know the concept).
- Modern infrastructure "can generate thousands of log events per minute" (cloud apps: "millions per minute"). With conventional logging you must pick which logs to send and which to archive; filtering before sending "may lead to gaps in coverage or the accidental removal of valuable data". This is the problem Logging without Limits solves.
- "Tail" (glossary): from the Unix `tail` command; print the last lines of a file to see the most recent events. The Agent can be set up to tail a log file (`type: file`).
Sources: https://docs.datadoghq.com/logs/, https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/glossary/

### Logs vs metrics vs traces
- **Metrics** (glossary): "numerical values that can track anything about your environment over time, from latency to error rates to user signups". Stored as `[value, timestamp]` data points in a timeseries. They "provide an overall picture of your system" and let you "assess the health of your environment at a glance". **"Once you identify a problem, you can use logs and tracing to further troubleshoot."**
  - Good at: long-term trends, cheap aggregation, alerting, capacity/scaling. Bad at: explaining the individual event or its context.
- **Traces** (glossary): "A trace tracks the time spent processing a request, and the status of this request. Each trace consists of one or more spans." Good at: where latency is spent across services for one request.
- **Logs**: high-detail, event-level, often semi-structured text. Good at: root cause, exact error, audit trail, security forensics. Bad at: cheap long-term trending at high volume (that is why Datadog offers log-based metrics) and high cost if you index everything.
- Pitfall: "break down slow requests by time in code, CPU, GC, lock contention, I/O" describes the profiler / traces, not logs. "Identify trends over long periods" is metrics (or log-based metrics), not raw logs.
- Correlate logs and metrics: log side panel > **Metrics** tab; on a dashboard or Metrics Explorer graph click a point > **View related logs**.
Sources: https://docs.datadoghq.com/metrics/, https://docs.datadoghq.com/glossary/, https://docs.datadoghq.com/logs/guide/correlate-logs-with-metrics/

### Log severity levels and Datadog status
- Syslog / RFC 5424 severities (integers 0-7, lower = more severe): 0 emerg (emergency), 1 alert, 2 critical, 3 error, 4 warning, 5 notice, 6 info (informational), 7 debug.
- Datadog official log `status` values: emerg, alert, critical, error, warning, notice, info, debug, plus **ok**.
- By default the intake assigns status `INFO` to every log. JSON preprocessing reads these attributes as the official status by default: `status`, `severity`, `level`, `syslog.severity`. Any other name (for example `log_level`) needs a **Log Status Remapper** processor, or for JSON logs can be added to the status attribute list in **Preprocessing for JSON logs** (put it first, the list is read in order). Pipeline changes only affect new logs.
- Status remapper mapping (case-insensitive):
  - integers 0-7 -> syslog severity
  - starts with `emerg` or `f` -> emerg (0) (so `FATAL` -> emerg)
  - starts with `a` -> alert (1)
  - starts with `c` -> critical (2)
  - starts with `err` -> error (3)
  - starts with `w` -> warning (4)
  - starts with `n` -> notice (5)
  - starts with `i` -> info (6)
  - starts with `d`, `t`, `v`, `trace`, `verbose` -> debug (7)
  - starts with `o` or `s`, or equals `OK`/`Success` -> **OK** (pitfall: Java `SEVERE` -> OK)
  - anything else -> info (6)
- Only the first status remapper in pipeline order applies (across all matching pipelines).
- Custom severities: use a **Category Processor** to map custom values to a new attribute, then a status remapper. Datadog integrations map HTTP codes: 2xx OK, 3xx notice, 4xx warning, 5xx error. Bunyan levels = syslog-like x10: 10 TRACE, 20 DEBUG, 30 INFO, 40 WARN, 50 ERROR, 60 FATAL.
- API payload: `{"type": "status-remapper", "sources": ["<ATTR>"], "is_enabled": true}` (`is_enabled` default false).
Sources: https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/, https://docs.datadoghq.com/logs/guide/remap-custom-severity-to-official-log-status/, https://docs.datadoghq.com/logs/log_configuration/pipelines/#preprocessing, https://docs.datadoghq.com/logs/guide/logs-show-info-status-for-warnings-or-errors/

### Datadog Log Management value proposition and Logging without Limits
- Datadog Log Management **decouples log ingestion from indexing** = Logging without Limits* (trademark). You can "cost-effectively collect, process, archive, explore, and monitor all of your logs without limitations".
- Mantra: ingest everything, process/enrich everything (pipelines), **index what you need** (indexes + exclusion filters), **archive everything** (archives get all ingested logs, indexed or not), **generate metrics from all ingested logs**.
- Lifecycle: ingest -> pipelines/processors (after collection, before indexing) -> Live Tail (all ingested logs after processing, before indexing/archiving) -> indexes (exclusion filters, daily quota, retention) / archives / log-based metrics.
- Excluded logs: discarded from the index but **still** in Live Tail, still archived, still usable to generate metrics. Indexed logs power faceted search, patterns, analytics and log monitors.
- LwL guide workflow: (1) find most logged service/status (graph view, Top List, group by `service` then `status`), (2) Patterns view to find noisy patterns, (3) pattern side panel > **Add Exclusion Filter** (disabled if less than half the pattern's logs fall in a single index; opens Log Index Configuration pre-filled), (4) Generate Metrics > **New Metric** to keep KPIs on the excluded logs, then an **Anomaly** monitor on that metric.
- Configuration lives at **Logs > Pipelines** (Log Configuration page): pipelines, indexes, archives, generate metrics, Flex Logs Controls.
Sources: https://docs.datadoghq.com/logs/, https://docs.datadoghq.com/logs/guide/getting-started-lwl/, https://docs.datadoghq.com/logs/log_configuration/, https://docs.datadoghq.com/logs/live_tail/, https://docs.datadoghq.com/glossary/

### Indexes, exclusion filters, daily quotas, retention
- Indexes segment logs "into value groups for differing retention, quotas, usage monitoring, and billing". A new account has a single index for all logs; use multiple indexes for multiple retention periods or multiple daily quotas (max **100 indexes** per account by default).
- A log enters the **first** index whose filter it matches. **Exclusion filters** (none by default; defaults: query `*`, **Exclude 100%**, active) drop logs from the index; the **daily quota** caps indexed logs per day (default reset **2:00pm UTC**); **retention** is set per index. Excluded and over-quota logs are still in Live Tail, still archived and still usable for log-based metrics. Full rules and examples: **Domain 4 > Filtering and Excluding**.
- Log-based metrics: 10s granularity kept **15 months**, billed as **custom metrics**; avoid grouping by high-cardinality attributes. Details: **Domain 5 > Metric Generation**. Free usage metrics (`datadog.estimated_usage.logs.*`) and the OOTB dashboard "Log Management - Estimated Usage" (estimates, may differ from billing): **Metric Generation > Logs usage metrics**.
- Find rarely queried indexes: Audit Trail query `@evt.name:"Log Management" @action:queried`, group by `@asset.new_value.query.indexes`.
- RBAC: three default roles Admin, Standard, Read-only; custom roles can restrict who changes index retention (avoid cost spikes).
Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/, https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/, https://docs.datadoghq.com/account_management/org_settings/

### Flex Logs
- Decouples **storage from compute** for cost-effective long-term retention. Use cases: long-term auditing, compliance/legal, security investigations, high-cardinality reporting over long periods.
- Tier guidance: **Standard Indexing** = queried frequently, short retention (application logs). **Flex Logs** = long retention, sometimes queried urgently (security, transaction, network logs; high volume, infrequent access). **Archives** = infrequently queried, long-term (audit and configuration logs).
- Good candidates to send straight to Flex: CDN, DNS, load balancers, VPC flow logs, CI/CD, identity, audit logs (CloudTrail, K8s audit).
- Not supported in Flex: **monitors**, **Watchdog**. Dashboards supported (count them when sizing compute). In Log Explorer toggle **Include Flex Logs** (next to the time picker).
- Compute sizes: Starter, XS, XS+, S, M, L (each about 2x the previous). US3, US5, AP1, AP2, US1-FED, US2-FED: only Starter, XS, XS+, S. Sizing by stored events: Starter < 10B; XS 10-50B; XS+ 50-100B; S 100-200B; M 200-500B; L 500B-1T; 1T+ contact CSM. Scalable tiers flat rate; Starter bundled storage+compute.
- Retention: Starter 3, 6, 12 or 15 months; scalable 30-450 days. Upgrade any time; downgrade once per 15 days. One compute size per org; Starter and scalable cannot be mixed in one org.
- Enable at **Flex Logs Controls** page (permission `flex_logs_config_write`), then in an index select Flex Tier under Configure Storage Tier and Retention. Both tiers: logs stay Standard for its retention, then Flex for the remainder (Standard 3 d + Flex 90 d = 3 d Standard then 87 d Flex). Removing Standard tier: logs no longer queryable in monitors or Watchdog Insights.
- Compute limit: concurrent queries and max logs scanned per query; when reached, queries slow/retry and may fail ("compute capacity is constrained").
Sources: https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/logs/guide/flex_compute/

### Archives, Archive Search and Rehydration
- Archives forward **all ingested logs, indexed or not**, to your own bucket (Amazon S3, Azure Storage, Google Cloud Storage) as compressed JSON (**zstd** by default). Logs enter the **first** archive whose filter matches.
- **Archive Search** (recommended way to access archives) streams results without re-indexing: up to **100,000 logs kept 24 hours**, charged only for the scan.
- **Rehydration** (historical views) loads archived logs back into the Log Explorer: up to **1 billion** events per view, index exclusion filters do not apply, default retention **15 days**, S3 must use role delegation.
- Setup steps, permissions, path format, partition/lookup attributes and limits: **Domain 5 > Exporting**.
Sources: https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/explorer/archive_search/, https://docs.datadoghq.com/logs/log_configuration/rehydrating/

### Standard Linux log locations and journald
- System and application logs on Linux live under **`/var/log`** (for example `/var/log/apache/access.log`, `/var/log/mysql/mysql_error.log`). Those files are typically readable only by root (or a group such as `mysql`).
- Agent runs as user/group **`dd-agent`**, so it cannot read root-only files in `/var/log` by default. Fixes:
  - ACLs: `setfacl -R -m u:dd-agent:rx /var/log/apache` (existing files) and `setfacl -R -d -m u:dd-agent:rx /var/log/apache` (default ACL for new/rotated files). Check with `getfacl`. If needed add a logrotate `postrotate` rule in `/etc/logrotate.d/`.
  - Without ACLs: group-based access, e.g. logrotate `create 644 mysql adm`.
  - Or `chmod 755 <folder>` / `chmod 644 <file>`; or an open source shipper with root access (rsyslog, syslog-ng, NXLog, Fluentd, Logstash).
  - Giving the Agent root access is **strongly not recommended** (stated on the heightened-read-permissions guide).
- Agent's own log files (`/var/log/datadog/` on Linux, rotation, debug mode, flares): see **Domain 6 > Agent's own logs, debug mode and flares**.
- **journald** (systemd-journald collects and stores structured, indexed journals). Agent min 7.29.0 for the integration. Journal files are owned/readable by the `systemd-journal` group: `usermod -a -G systemd-journal dd-agent`. Default journal locations: `/var/log/journal` and `/run/log/journal` (set `path` otherwise). Config in `journald.d/conf.yaml`:
  ```yaml
  logs:
    - type: journald
      path: /var/log/journal/
      include_units:
        - sshd.service
  ```
  Filters: `include_units`/`exclude_units`, `include_user_units`/`exclude_user_units` (7.37+, `*` works only in exclude), `include_matches`/`exclude_matches` (7.39+, `key=value`), `config_id` to tail the same journal twice (7.41+). `source`/`service` come from `SYSLOG_IDENTIFIER`, `_SYSTEMD_UNIT`, `_COMM` (first non-empty). Validate with `agent status` (journald under Logs Agent).
- Log collection is **off by default**: `logs_enabled: true` in `datadog.yaml` (or `DD_LOGS_ENABLED=true`), needs Agent v6+. Log lines must end with `\n` or `\r\n`.
Sources: https://docs.datadoghq.com/logs/guide/setting-file-permissions-for-rotating-logs/, https://docs.datadoghq.com/logs/guide/custom-log-file-with-heightened-read-permissions/, https://docs.datadoghq.com/agent/configuration/agent-log-files/, https://docs.datadoghq.com/integrations/journald/, https://docs.datadoghq.com/agent/logs/

### Common pitfalls
- Exclusion filters and daily quotas only stop **indexing**, never ingestion, archiving or metric generation.
- Logs reached through Live Tail are not searchable later unless indexed (Live Tail is real time, sampled when too many logs match).
- Archives are not searchable in Log Explorer until rehydrated; Archive Search results stay on their own page for 24 h.
- Monitors and Watchdog do not work on Flex-only logs.
- Strings starting with `s` (e.g. `SEVERE`) map to status OK, not error; strings starting with `f` (`FATAL`) map to emerg.
- Log-based metrics are custom metrics: high-cardinality group-bys raise the bill.
Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/, https://docs.datadoghq.com/logs/live_tail/, https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/

## Logging Formats

### Structured vs unstructured logs
- **Structured** logs (JSON) carry key/value attributes. Datadog **automatically parses JSON-formatted logs**: every JSON key becomes a log attribute with no pipeline needed.
- **Unstructured / semi-structured** text (plain lines, syslog text, Apache/NGINX access lines, key=value) arrives with everything in the `message`. To get attributes you parse it in a **pipeline** with a **Grok Parser** (ingest-time) processor.
- Pipelines "take logs from a wide variety of formats and translate them into a common format in Datadog". No server-side or logger change is required: everything is configured on the Pipelines page.
- Processing order: JSON **preprocessing** runs first, then pipelines (each log is tested against every pipeline filter; matching pipeline applies its processors sequentially, then the next pipeline).
- Parsed logs are needed for queries, monitors, aggregations, facets, Sensitive Data Scanner, and so on.
- **Find unparsed logs**: open a log and check the **Event Attributes** panel (it says no attributes were extracted), or query `datadog.pipelines:false` in the Log Explorer (indexed logs without custom attributes after pipeline processing). Use **Patterns** on that query to kick-start pipelines; create a log-based metric (for example `logs.unparsed`) with that query so non-indexed logs are covered too, grouped by `service`/`team`, then a metric monitor as a quota.
- **Auto-Processing** (new): parses custom application logs that match **no** integration or custom pipeline filter; extracts core attributes (timestamp, status, trace ID, span ID). Entries are per **source + service** pair, created about 15 minutes after first logs, need at least 1,000 indexed logs in the past 24 hours, max 100 entries per org. On by default for orgs created on or after Nov 4, 2026; off by default for older orgs. Not available on US5. A pipeline whose filter matches every log (for example `*`) stops Auto-Processing for the whole org. Toggle: Processing page > **Auto-Processing** tab; **View Transformations**; **Switch to manual pipeline**.
Sources: https://docs.datadoghq.com/logs/log_configuration/parsing/, https://docs.datadoghq.com/logs/log_configuration/pipelines/, https://docs.datadoghq.com/logs/guide/detect-unparsed-logs/

### Why JSON (or key=value) is recommended
- Java docs: stack traces from typical Java logs split into multiple lines (one exception = 4 events). Logging to **JSON**: stack trace properly wrapped into one log event; all attributes (severity, logger name, thread name) extracted; access to **MDC** attributes; **no custom parsing rules** needed.
- Python docs: tracebacks split logs into multiple lines; Datadog "strongly recommends" a **JSON formatter** so each stack trace is wrapped into the correct log and attributes are extracted.
- key=value / logfmt is easy to parse with one Grok filter (`keyvalue`) instead of a full pattern; the Log Parsing Best Practices guide points to the key-value filter that "can automatically extract all your attributes".
- Recommended pattern for apps: log to a file in JSON, tail it with the Agent (`type: file`).
Sources: https://docs.datadoghq.com/logs/log_collection/java/, https://docs.datadoghq.com/logs/log_collection/python/, https://docs.datadoghq.com/logs/guide/log-parsing-best-practice/

### Reserved attributes
| Attribute | Meaning |
|---|---|
| `host` | Originating host as defined in metrics; Datadog applies matching host tags. Agent sets it automatically. |
| `source` | Integration/technology name (`nginx`, `postgresql`). If it matches an integration name, Datadog **auto-installs the integration pipeline (parsers) and facets**. |
| `status` | Level/severity; used for patterns, dedicated UI layout. |
| `service` | App/service name; used to pivot Logs <-> APM, keep same value as APM (unified service tagging `env`, `service`, `version`). |
| `trace_id` | Correlates log with its trace. |
| `message` | Body of the log; highlighted in Live Tail/Explorer and indexed for **full-text search**. |
- In search, reserved attributes need no `@` (`service:web`); other attributes need `@` (`@http.status_code:500`).
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes, https://docs.datadoghq.com/logs/explorer/search_syntax/

### JSON preprocessing (Preprocessing for JSON logs)
- Runs **before** pipelines, only on JSON logs. Default config works for standard forwarders. Edit: **Logs > Pipelines** > hover **Preprocessing for JSON logs** > pencil icon; add/reorder attribute names; Save. Only affects **new** logs.
- **Preprocessing is the only way to define one of your log attributes as `host`** (there is no host remapper processor, and the generic Remapper processor cannot remap reserved attributes such as `host`).
- Default mappings (JSON key -> reserved attribute):
  - **Source**: `ddsource`
  - **Host**: `host`, `hostname`, `syslog.hostname` (Agent or RFC5424 format sets host automatically)
  - **Date**: `@timestamp`, `timestamp`, `_timestamp`, `Timestamp`, `eventTime`, `date`, `published_date`, `syslog.timestamp`
  - **Message**: `message`, `msg`, `log`
  - **Status**: `status`, `severity`, `level`, `syslog.severity`
  - **Service**: `service`, `syslog.appname`, `dd.service` (Agent or RFC5424 sets service automatically)
  - **Trace ID**: `dd.trace_id`, `contextMap.dd.trace_id`, `named_tags.dd.trace_id`, `trace_id`
  - **Span ID**: `dd.span_id`, `contextMap.dd.span_id`, `named_tags.dd.span_id`, `span_id`
- Date list is searched **in order**: to make a custom key (for example `mytimestamp`) win, add it **first** in the list.
- **Kubernetes pitfall**: a JSON log containing `host`, `hostname` or `syslog.hostname` overrides the Agent hostname, so the log loses the correct host-level tags. Datadog recommends clearing those attributes.
- Containerized logs: override default source/service with an environment variable / Autodiscovery labels, not with `ddsource` alone.
- If no date attribute is present, Datadog stamps the log with its **intake (received) time**.
- Pipeline equivalents for non-default keys: Log Date Remapper, Log Status Remapper, Service Remapper, Log Message Remapper, Trace ID Remapper, Span Remapper.
Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#preprocessing, https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/

### Remapper behaviour (status, message, service, date)
- **Log Status Remapper** value mapping: see **Logging Systems > Log severity levels and Datadog status** (`FATAL` -> emerg, `SEVERE` -> OK, anything unknown -> info).
- First-write-wins processors: Status remapper, Service remapper, Message remapper, Trace remapper, Span remapper (first one in pipeline order; across matching pipelines, first encountered).
- **Log Date Remapper**: if several apply, the **last** one in pipeline order wins. Default date attributes listed on its page: `timestamp`, `date`, `_timestamp`, `Timestamp`, `eventTime`, `published_date`.
- Log Message Remapper can take several attributes as fallbacks (first existing one is used); API `sources` default `msg`.
- Processor API types: `date-remapper`, `status-remapper`, `message-remapper`, `service-remapper`; `is_enabled` default `false`.
Sources: https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_message_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/service_remapper/, https://docs.datadoghq.com/logs/log_configuration/pipelines/#attribute-precedence

### Timestamps and date formats
- Recognized official date formats: **ISO8601**, **UNIX (milliseconds EPOCH)**, **RFC3164**. Timestamps that do not exactly match these formats may be dropped, even if similar (the docs' example: epoch in **nanoseconds**). Epoch **seconds** also need converting (troubleshooting guide: Arithmetic Processor x1000).
- Timestamps are stored in **UTC** and displayed in the user's local timezone (check **Preferences > Time zone** first if times look shifted).
- **Ingestion window**: logs with an official date more than **18 hours in the past** are rejected/dropped at intake (track with `datadog.estimated_usage.logs.drop_count`). Date remapper page: up to 18 h in the past and **2 h in the future**. Preview: up to 7 days in the past.
- Epoch timestamps are parsed as **UTC** by default; local-time logs appear shifted (New York EST -5 appears 5 h in the past).
- Grok `date()` matcher: `date("pattern"[, "timezoneId"[, "localeId"]])`, output is **epoch milliseconds**. Example: `%{date("yyyy-MM-dd HH:mm:ss z"):date}`, `%{date("dd/MMM/yyyy:HH:mm:ss Z"):date}`, `%{date("EEE MMM dd HH:mm:ss yyyy","Europe/Paris"):date}`.
- Timezone param formats: `GMT`/`UTC`/`UT`/`Z`; `+hh:mm`, `-hhmm` (range -18:00 to +18:00); `UTC+5`, `GMT-3`; TZ database IDs (`Europe/Paris`).
- **Parsing a date does NOT set the official date**: add a **Log Date Remapper** after the Grok Parser.
- Raw text fix: Pipeline > Add Processor > Grok Parser with `date()` -> Add Processor > **Date remapper** > add attribute in "Set date attribute(s)" > Create.
- JSON with custom key in supported format: add key to Preprocessing date list (first).
- JSON with unsupported format: Grok Parser with **Advanced Settings > Extract from** `mytimestamp`, then Log Date Remapper.
- JSON epoch **seconds**: remove `timestamp` from preprocessing date list, **Arithmetic Processor** `timestamp * 1000` into a new attribute, Log Date Remapper on the new attribute.
- Pipeline changes only affect **new** logs (processing happens at ingestion).
Sources: https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/, https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/log_configuration/parsing/#parsing-dates, https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/

### Common text formats and Grok
- Grok syntax (`%{MATCHER:EXTRACT:FILTER}`, rule must match the **entire** log, first matching rule top-to-bottom wins, best practice max **10 parsing rules per Grok parser** and **20 processors per pipeline**), samples, Tap to Parse, matchers and filters: **Domain 2 > Processors & Pipelines > Grok**. Text-format shortcuts: key=value / logfmt -> `rule %{data::keyvalue}` (`keyvalue(": ")` for `key: value`, `keyvalue("=","/:")` for URL values); JSON after a text prefix -> `%{data::json}`; also `xml`, `csv` (`tab` for TSV), `url`, `querystring`, `useragent`, `array`.
- **Apache/NGINX common & combined log format**: integration pipelines parse them when `source` is `apache` / `nginx` (integration pipeline installed automatically after the first log with that source; read-only, clone to edit; cannot be deleted, only disabled). Example common-format rule produces `network.client.ip`, `http.method`, `http.url`, `http.version`, `http.status_code`, `network.bytes_written`, `date`. The default NGINX format lacks request time; Datadog recommends adding `$request_time` to `log_format`.
- **Syslog**: RFC5424 format automatically sets host and service. Standard attributes `syslog.hostname` (-> host), `syslog.appname` (-> service), `syslog.severity` (-> status), `syslog.timestamp` (-> date), `syslog.env`. Agent TCP/UDP listener accepts **raw string, JSON and Syslog** formatted logs; each line must end with `\n` or `\r\n` or the Agent waits indefinitely.
- Glog (Kubernetes components), XML, CSV examples exist in parsing docs.
Sources: https://docs.datadoghq.com/logs/log_configuration/parsing/, https://docs.datadoghq.com/logs/log_configuration/processors/grok_parser/, https://docs.datadoghq.com/logs/guide/log-parsing-best-practice/, https://docs.datadoghq.com/integrations/nginx/, https://docs.datadoghq.com/standard-attributes/, https://docs.datadoghq.com/agent/logs/

### Multi-line logs (stack traces)
- Without aggregation, the Agent sends one log per line, so a stack trace becomes many logs. Fixes: log in JSON (stack trace stays in one event), or aggregate at the Agent with a manual `multi_line` processing rule (pattern = start of a new log, Golang regexp) or **automatic multi-line detection** (Agent **7.65.0+**, **enabled by default from Agent 7.82.0**; datetime in the first 60 bytes starts a new log; JSON never aggregated; pretty-printed JSON compacted from 7.67; Go stack traces from 7.81). Full rules, examples and options: **Domain 2 > Log Filtering & Obfuscation > Manual multi-line aggregation** and **Automatic multi-line detection and aggregation**.
- In Docker labels / K8s annotations, escape `\d` as `\\d` and use valid JSON (no trailing commas).
- Stack trace attributes with dedicated UI: `error.stack`, `error.message`, `error.kind`, `logger.name`, `logger.thread_name`. Integration pipelines remap logging-library params to these.
Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#manually-aggregate-multi-line-logs, https://docs.datadoghq.com/agent/logs/auto_multiline_detection/, https://docs.datadoghq.com/logs/log_collection/#attributes-for-stack-traces

### Log size and attribute limits
- Per log event (converted to JSON): **< 2048 attributes**; attribute keys **< 50 characters**; nesting **< 20 successive levels**; values **< 1024 characters** if promoted as a facet.
- Tags: max **100 tags** per log, each **<= 256 characters**, max **10 million unique tags per day**.
- Timestamp: up to **18 h in the past** (Preview: 7 days). Attributes with **null** values are not retained (Preview to retain).
- Non-compliant logs may be transformed or truncated, or not indexed if outside the time range.
- Size: HTTPS API accepts logs up to **1 MB**; recommended individual log **<= 25 KB (25,000 bytes)**; the Agent **splits** a log at **900 KB (900,000 bytes)**. Logs above 1 MB are **truncated** (metrics `datadog.estimated_usage.logs.truncated_count`, `..._truncated_bytes`).
- HTTP API per request: payload max **5 MB uncompressed** (else **413**); single log max **1 MB** (larger is accepted, truncated, returns **2xx**); max **1000 entries** per array. Send compressed with `Content-Encoding: gzip` (or `deflate`). Endpoint `POST https://http-intake.logs.<site>/api/v2/logs`, header `DD-API-KEY`; body fields `ddsource`, `ddtags`, `hostname`, `message` (required), `service`. Success = **202**.
- Indexed-only field truncation for grouped queries: `message` 75 KiB, other fields 25 KiB (full text still stored and visible in list).
- Agent option `exclude_truncated` processing rule (Agent 7.69+) drops truncated logs.
Sources: https://docs.datadoghq.com/logs/log_collection/#limitations, https://docs.datadoghq.com/logs/log_collection/#custom-log-forwarding, https://docs.datadoghq.com/api/latest/logs/#send-logs, https://docs.datadoghq.com/logs/troubleshooting/

### Encodings and other Agent format options
- Agent assumes **UTF-8**. `encoding:` (only for `type: file`): `utf-16-le`, `utf-16-be` (Agent 6.23/7.23), `shift-jis` (6.34/7.34). Unsupported value -> read as UTF-8. Changing encoding on an already-tailed file can produce mojibake; rotate/replace the file.
- ASCII control characters are serialized on ingestion; escape the serialized value in Grok.
- Invalid characters in structured logs should be stripped at the Agent with `mask_sequences`.
Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#log-file-encodings, https://docs.datadoghq.com/logs/log_configuration/processors/, https://docs.datadoghq.com/logs/log_configuration/parsing/#ascii-control-characters

### Common pitfalls
- Expecting a Grok-parsed date to change the log time (needs Date Remapper).
- Epoch seconds or nanoseconds in `timestamp` (must be milliseconds) -> wrong or dropped logs.
- Non-UTC local timestamps without `timezone` in `date()` -> shifted logs.
- Custom `source` name instead of the integration name -> no integration pipeline.
- `hostname` key inside app JSON on Kubernetes -> wrong host, missing host tags.
- Multi-line regex that never matches the start of a log -> line loss or one huge log.
- Agent 7.67+ JSON compaction breaks processing-rule regexes that expect spaces after colons.
- Logs without trailing newline are never sent by the Agent.
Sources: https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/agent/logs/auto_multiline_detection/, https://docs.datadoghq.com/agent/logs/

## Log Emission

How applications and systems produce logs and get them to Datadog: files, container stdout/stderr, syslog daemons, journald, Windows Event Log, language logging libraries, the browser logs SDK and the HTTP intake API. Verified against current docs (2026-11).

### Ways a log can reach Datadog (overview)

- **Host / file tailing (default pattern)**: application writes to a local file, the Datadog Agent tails it. Every language page (Python, Java, Node.js, Go, Ruby, PHP, C#) starts with "log to a file and tail that file with the Datadog Agent".
- **Containers**: application writes to `stdout`/`stderr`; the Agent collects container output directly, no logging driver needed. With the Docker check enabled, container and orchestrator metadata are added as tags automatically.
- **Network listener**: Agent listens on a TCP/UDP port (`type: tcp` / `type: udp`) for raw, JSON or Syslog-formatted lines.
- **journald** (`type: journald`) and **Windows Event Log** channels (`type: windows_event`).
- **Existing log shippers**: Rsyslog, Syslog-ng, NXlog, FluentD, Logstash (dedicated docs for each).
- **Agentless**: send directly to the Logs HTTP intake API (custom forwarders, Winston HTTP transport, .NET direct submission, Serilog sink). Datadog still recommends the Agent: it provides native connection management, retries and enrichment, plus Agent-side features such as sensitive data scrubbing.
- **Browser logs SDK** (`@datadog/browser-logs`) for JavaScript web apps; mobile SDKs (Android, iOS, Flutter, React Native, Roku, Kotlin Multiplatform) also exist.
- **Serverless**: Datadog Forwarder (AWS Lambda function) ships cloud logs.
- **Agent checks**: custom integrations can call `send_log` to submit logs.
- Log collection requires Agent v6.0+. It is **disabled by default**: set `logs_enabled: true` in `datadog.yaml` (env var `DD_LOGS_ENABLED=true`).
- The Agent collects only logs written **after** it starts tailing (default `start_position: end`).

Sources: https://docs.datadoghq.com/logs/log_collection/, https://docs.datadoghq.com/agent/logs/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/

### Writing logs to files and having the Agent tail them
- The default pattern on every language page: the application writes to a local file and the Agent tails it (`type: file`). The steps (create `conf.d/<CUSTOM_LOG_SOURCE>.d/conf.yaml` with a `logs:` section, restart, check `status`), the full parameter table (`type`, `port`, `path`, `channel_path`, `service`, `source`, `exclude_paths`, `sourcecategory`, `start_position`, `encoding`, `tags`), wildcards, `open_files_limit`, Windows paths and the TCP/UDP listener are in **Domain 2 > Enabling Log Collection > Custom log collection**.
- Language pages use `sourcecategory: sourcecode` in the file-tail example.
- **A log line must end with a newline (`\n` or `\r\n`)**. Without it the Agent waits indefinitely and never sends the line (applies to files and TCP/UDP).
- The Agent reads only new lines by default (`start_position: end`); `beginning` does not support wildcard paths, a stored offset wins over `beginning`/`end`, `forceBeginning`/`forceEnd` ignore it; containers always start at `beginning`.
Sources: https://docs.datadoghq.com/agent/logs/, https://docs.datadoghq.com/agent/logs/advanced_log_collection/, https://docs.datadoghq.com/logs/guide/increase-number-of-log-files-tailed/

### Application logging libraries per language (log to file in JSON)

Common rules on every language page:
- Configure the logger to write **JSON** to a file. Reasons: multi-line stack traces/tracebacks stay wrapped in one log event; all attributes (timestamp, level, logger, MDC/extra fields) are extracted automatically; no custom parsing rules needed. JSON logs are parsed automatically by Datadog.
- Agent config: create `conf.d/<lang>.d/conf.yaml` with `type: file`, `path`, `service`, `source: <lang>`, `sourcecategory: sourcecode`; restart; check `status`.
- Non-JSON multi-line logs: commented example rule `log_processing_rules: - type: multi_line, name: new_log_start_with_date, pattern: \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])`.
- If the APM SDK injects `service` into the log, it overrides the `service` set in the Agent config.

| Language | Libraries in docs | Agent folder / `source` |
| --- | --- | --- |
| Python | JSON-log-formatter, Python-json-logger, django-datadog-logger (`DJANGO_DATADOG_LOGGER_EXTRA_INCLUDE` regex for `extra`) | `python.d/`, `source: python` |
| Java | Log4j (via `log4j-over-slf4j` + Logback), Log4j 2 (built-in JSON layout, `JsonTemplateLayout` template in `src/main/resources`), Logback (`logstash-logback-encoder` `LogstashEncoder` for files; built-in `ch.qos.logback.classic.encoder.JsonEncoder` shown for console), Tinylog (`writer = json`, `writer.format = LDJSON`) | `java.d/`, `source: java` |
| Node.js | Winston (examples), Bunyan, Pino; Winston 3 `format.json()` + `transports.File` | `nodejs.d/`, `source: nodejs` |
| Go | logrus with `log.SetFormatter(&log.JSONFormatter{})`; `WithFields` for metas | `go.d/`, `source: go` |
| Ruby (Rails) | Lograge (`config.lograge.formatter = Lograge::Formatters::Json.new`, `config.colorize_logging = false`), Grape via `grape_logging` | `ruby.d/`, `source: ruby` |
| C# / .NET | Serilog (`JsonFormatter` / `RenderedCompactJsonFormatter`), NLog (`JsonLayout`), log4net (`log4net.Ext.Json`) | `csharp.d/`, `source: csharp` |
| PHP | Monolog (`JsonFormatter` + `StreamHandler`), Zend-Log, Symfony (Monolog JSON formatter service) | `php.d/`, `source: php` |

Language specifics worth remembering:
- Java: raw stack traces become many events ("4 events generated when only one is expected"). JSON also gives MDC attributes. Streaming directly is only for the exceptional case where the app cannot log to a file; Datadog does **not** support sending logs over TCP directly to the intake, so configure Logback's TCP appender to a local Agent `type: tcp` listener (example port `10518`), which forwards over HTTPS. Log4j 2 can log to a remote host but cannot prefix logs with an API key, hence the Logback bridge.
- Go: best practice levels `DEBUG`, `INFO`, `WARNING`, `FATAL`; Go `FATAL` maps to Datadog severity `Emergency`.
- Ruby: Lograge turns multi-line Rails request logs into one JSON line; log hashes instead of strings so keys (`user`, `button_name`) become attributes.
- C#: three approaches: file-tail with Agent (recommended, Agent enriches metadata); Agentless logging via APM auto-instrumentation; Serilog sink `Serilog.Sinks.Datadog.Logs` (HTTPS port 443). Make sure the Agent user can read the file.
- Node.js troubleshooting: catch Logstash transport errors; do not set `max_connect_retries` to `1`.

Sources: https://docs.datadoghq.com/logs/log_collection/python/, https://docs.datadoghq.com/logs/log_collection/java/, https://docs.datadoghq.com/logs/log_collection/nodejs/, https://docs.datadoghq.com/logs/log_collection/go/, https://docs.datadoghq.com/logs/log_collection/ruby/, https://docs.datadoghq.com/logs/log_collection/csharp/, https://docs.datadoghq.com/logs/log_collection/php/

### Agentless logging to the HTTP intake API

Endpoint (v2, POST): `https://http-intake.logs.<DD_SITE>/api/v2/logs`, e.g. `http-intake.logs.datadoghq.com` (US1), `http-intake.logs.us3.datadoghq.com`, `http-intake.logs.us5.datadoghq.com`, `http-intake.logs.datadoghq.eu`, `http-intake.logs.ap1.datadoghq.com`, `http-intake.logs.ap2.datadoghq.com`, `http-intake.logs.uk1.datadoghq.com`, `http-intake.logs.ddog-gov.com`. Legacy v1: `/v1/input`. Port 443 (HTTPS).

- Auth: header `DD-API-KEY: <API key>` (an **API key**, not an application key or client token). Body JSON with `Content-Type: application/json`; tags can be passed as `ddtags` query parameter with `text/plain` content type.
- Body fields: `message` (required), `ddsource`, `ddtags` (e.g. `env:staging,version:5.1`), `hostname`, `service`. `ddsource` matching an integration name installs that integration's parsers and facets.
- **Limits per request**: payload max **5MB**; single log max **1MB**; array max **1000 entries**. A log over 1MB is accepted and **truncated** to 1MB with a 2xx (single or multi-log request; only oversized logs truncated). For optimal performance, Datadog recommends individual logs of no more than 25K bytes (log collection page). (Agent HTTP batches separately cap a single log at 900kB.)
- Compression recommended: `Content-Encoding: gzip` (v2 enum: `identity`, `gzip`, `deflate`).
- Timestamps up to **18 hours in the past** (7 days with a Preview). Older logs are dropped at intake (Logs Troubleshooting page; check `datadog.estimated_usage.logs.drop_count`).
- v2 status codes: **202** Accepted; 400 Bad request; 401 Unauthorized; 403 Permission issue; 408 Request Timeout (retry); 413 Payload too large; 429 Too Many Requests (retry); 500 (retry); 503 Service Unavailable (retry). v1 returns 200 OK.
- Other per-log limits (tags, attributes, nesting, null values, indexed-field truncation): see **Logging Formats > Log size and attribute limits**.
- TCP log collection to the Datadog intake is **not supported** (no delivery or reliability guarantees); use HTTP. This is about the intake endpoints, not the Agent's own local `type: tcp` listener.
- When to use agentless: the app runs where an Agent cannot be installed or cannot write to files (PaaS, locked-down hosts, custom forwarders). Trade-offs: the app must handle connection issues/retries; no Agent enrichment or Agent-side scrubbing.
- Node.js: Winston `transports.Http` with `host: 'http-intake.logs.<SITE>'`, `path: '/api/v2/logs?dd-api-key=<KEY>&ddsource=nodejs&service=<APP>'`, `ssl: true`.
- .NET Agentless logging (APM auto-instrumentation required, no code changes): `DD_API_KEY`, `DD_SITE` (default `datadoghq.com`), `DD_LOGS_DIRECT_SUBMISSION_INTEGRATIONS` = `Serilog`, `NLog`, `Log4Net`, `ILogger` (semicolon list). Extras: `DD_LOGS_DIRECT_SUBMISSION_MINIMUM_LEVEL` (default `Information`), `..._HOST`, `..._TAGS`, `..._SOURCE` (default `csharp`), `..._MAX_BATCH_SIZE` (default `1000`), `..._MAX_QUEUE_SIZE` (default `100000`), `..._BATCH_PERIOD_SECONDS` (default `1`). log4net/NLog need an appender/logger configured.
- Rsyslog: `imfile` module (inotify mode recommended from 8.1.5) + `omhttp` action to `http-intake.logs.<site>` port 443, `restpath="api/v2/logs"`, header `DD-API-KEY`; `$ModLoad immark` / `$MarkMessagePeriod 20` keeps the connection alive. Syslog-ng: `http()` destination to `/api/v2/logs?ddsource=...` with `DD-API-KEY` header.
- Agent transport (compressed HTTPS on 443 since 6.19/7.19, `force_use_http`, `batch_wait`, `compression_level`, batch limits): see **Domain 2 > Enabling Log Collection > Transport, compression, limits**.

Sources: https://docs.datadoghq.com/api/latest/logs/#send-logs, https://docs.datadoghq.com/logs/log_collection/#logging-endpoints, https://docs.datadoghq.com/logs/log_collection/nodejs/#agentless-logging, https://docs.datadoghq.com/logs/log_collection/csharp/#agentless-logging-with-apm, https://docs.datadoghq.com/integrations/rsyslog/, https://docs.datadoghq.com/integrations/syslog_ng/, https://docs.datadoghq.com/agent/logs/log_transport/

### Browser logs SDK (JavaScript web apps)

- Package `@datadog/browser-logs` (`datadogLogs`), or CDN (`window.DD_LOGS`, e.g. `https://www.datadoghq-browser-agent.com/us1/v7/datadog-logs.js`). Works without the RUM SDK; also works in Worker/Service Worker (no session info there).
- **Client token**, not an API key: API keys would be exposed client-side. Create in **Organization Settings > Client Tokens** (New Client Token). Deleted client tokens cannot be restored (revoked API keys can for 7 days). Tokens stay active if the creator is deactivated.
- Install options: **NPM** (recommended for modern apps, bundled, no page-load impact, may miss errors before init); **CDN async** (performance targets, may miss early errors; wrap early calls in `window.DD_LOGS.onReady()`); **CDN sync** (collects all errors, loads first, may impact page load; guard with `window.DD_LOGS &&`).
- Init: `datadogLogs.init({ clientToken, site, forwardErrorsToLogs: true, sessionSampleRate: 100 })`. Initialize as early as possible.
- API: `logger.debug|info|warn|error(message, messageContext?, error?)`; generic `logger.log(message, context, status)`; statuses `debug`, `info`, `warn`, `error`.
- SDK adds by default: `date`, `view.url`, `view.referrer`, `session_id`. Datadog backend adds `http.useragent`, `network.client.ip` (plus geoip). `origin: "logger"` for custom logs.
- `beforeSend(log, context)`: scrub (e.g. rewrite `view.url`) or return `false` to discard (e.g. 404 network errors). Context: `isAborted`, `handlingStack`. Sensitive auto-collected fields: `view.url`, `view.referrer`, `message`, `error.stack`, `http.url`.
- Multiple loggers: `createLogger(name, {level, handler, context})`, `getLogger(name)`.
- Global context: `setGlobalContext`, `setGlobalContextProperty`, `getGlobalContext`, `removeGlobalContextProperty`, `clearGlobalContext` (renamed in v4.17.0 from `*LoggerGlobalContext`). User: `setUser`, `setUserProperty`, ... Account: `setAccount`, ... Global context overrides user/account context. Contexts live in page memory unless `storeContextsAcrossPages` (v4.49.0, localStorage, 5 MiB per origin, incompatible with `trackSessionAcrossSubdomains`).
- `setLevel('warn')`: only logs at or above that level are sent. `setHandler('http'|'console'|'silent')` or array `['http','console']`.
- Tracking consent: `trackingConsent: 'granted' | 'not-granted'`, change later with `setTrackingConsent`; not synced across tabs.
- `getInternalContext()` returns `session_id`. WASM errors need `@datadog/browser-plugin-wasm`.
- Endpoint: Browser SDK sends JSON over HTTPS to the `logs.` browser intake on 443.

Sources: https://docs.datadoghq.com/logs/log_collection/javascript/, https://docs.datadoghq.com/account_management/api-app-keys/#client-tokens

### Containers: stdout/stderr
- Datadog recommends containerized apps write to `stdout`/`stderr` so collection is automatic and container tags are attached. Logs written to files in containers need a volume shared with the Agent (`type: file` label/annotation); custom file collection from the host gets **no container metadata/tags**.
- **Logs from container `stderr` default to status `Error`**.
- If `source`/`service` are not set, the Agent falls back to the Unified Service Tagging `service` tag (when set), otherwise to the container short image name.
- Short-lived containers: collected (Agent 6.14+) as long as not removed. If a container is removed during a network outage, unsent logs are lost.
- Docker and Kubernetes setup (env vars, mounts, Autodiscovery labels and annotations, `containerCollectAll`, `/var/log/pods`): **Domain 2 > Enabling Log Collection > Docker log collection** and **Kubernetes log collection**.
Sources: https://docs.datadoghq.com/containers/docker/log/, https://docs.datadoghq.com/containers/kubernetes/log/, https://docs.datadoghq.com/logs/guide/mechanisms-ensure-logs-not-lost/

### Syslog daemons and heightened-permission system logs

- System logs (syslog, journald) often need root to read; the Agent does not run as root.
- Three options: give the Agent root (**strongly not recommended**); change permissions (`chmod 755` on directories, `chmod 644` on files - the Agent needs read+execute on directories and read on the file); or use an open-source shipper with root access (Rsyslog, Syslog-ng, NXlog, FluentD, Logstash) to send to Datadog or to a local Agent.
- Default Linux log location `/var/log/`.
- Rsyslog: set `HOSTNAME` to match the Datadog host name so logs link to host metrics; set `ddsource` in the template; add `ddtags`.

Sources: https://docs.datadoghq.com/logs/guide/custom-log-file-with-heightened-read-permissions/, https://docs.datadoghq.com/integrations/rsyslog/, https://docs.datadoghq.com/integrations/syslog_ng/

### journald
- Setup (minimum Agent 7.29.0, `usermod -a -G systemd-journal dd-agent`, `journald.d/conf.yaml` with `type: journald`, default paths `/var/log/journal` and `/run/log/journal`, unit and match filters, `config_id`): **Logging Systems > Standard Linux log locations and journald**.
- If permissions are wrong, journald sends an **empty payload** and no explicit error is raised.
- `include_matches`/`exclude_matches` example: `_TRANSPORT=kernel`. `*` works in exclude lists only.
- `source`/`service` are filled from the first non-empty of `SYSLOG_IDENTIFIER`, `_SYSTEMD_UNIT`, `_COMM`; set `SyslogIdentifier` in the systemd unit to use integration pipelines.
- Containerized Agent: mount the journal and `/etc/machine-id`. Docker can use the journald logging driver instead of json-file.
Sources: https://docs.datadoghq.com/integrations/journald/, https://docs.datadoghq.com/agent/logs/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/#permission-issue-and-journald

### Windows Event Log

- Config file `conf.d/win32_event_log.d/conf.yaml`; list channels with PowerShell `Get-WinEvent -ListLog *` (most active: `| sort RecordCount -Descending`), or Event Viewer > Properties > `Full Name`.
- As logs: under `logs:` use `type: windows_event`, `channel_path: <channel>`, `source`, `service`. The integration page recommends `source: windows.events` to get the integration pipeline (the Agent log page shows source = channel name).
- As Datadog Events (different feature): `instances:` with `path` + `legacy_mode: false` (Event Log API), or deprecated WMI legacy mode with `log_file`.
- Filtering: `query` (XPath/structured XML; faster, less CPU) recommended over `log_processing_rules`.
- Security channel: add the Agent user to the **Event Log Readers** group. Windows Agent user is `ddagentuser`.

Sources: https://docs.datadoghq.com/integrations/win32_event_log/, https://docs.datadoghq.com/agent/logs/

### Log rotation and tailing

- On rotation, the Agent keeps tailing the old file in parallel with the new one, prioritising the newest. **60 seconds** after rotation is detected it closes the rotated file; anything written after is lost. Tune with `logs_config.close_timeout` / `DD_LOGS_CONFIG_CLOSE_TIMEOUT`.
- The Agent stores a pointer (offset) per tailed file/container, so after network issues it resumes where it stopped. TCP/UDP listeners buffer in memory; new logs are dropped when the buffer is full.
- Permissions after rotation: the Agent runs as `dd-agent` (Linux), so rotated files created root-only make it lose access. Fixes:
  - ACLs: `setfacl -R -m u:dd-agent:rx /var/log/apache` (existing files) **and** `setfacl -R -d -m u:dd-agent:rx /var/log/apache` (default ACL: files created later, including by rotation, inherit access). Check with `getfacl`.
  - `copytruncate` keeps the original file so default ACLs do not help: add a `postrotate ... /usr/bin/setfacl -m u:dd-agent:rx <file> ... endscript` to the existing logrotate config (or `/etc/logrotate.d/dd-agent_ACLs` for unmanaged paths). Two configs on the same file give `error: duplicate log entry for <FILE>`.
  - No ACLs: logrotate `create 644 mysql adm` (troubleshooting guide: set `644` in the rotation config).
  - Windows: `icacls "path" /grant "ddagentuser:(OI)(CI)(RX)" /t`; `(OI)(CI)` inheritance covers files created by rotation.
- PostgreSQL note: data directory 0700 (v10-) or 0700/0750 (v11).

Sources: https://docs.datadoghq.com/logs/guide/mechanisms-ensure-logs-not-lost/, https://docs.datadoghq.com/logs/guide/setting-file-permissions-for-rotating-logs/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/

### Injecting trace IDs (logs-traces correlation, light)

- APM SDKs inject `dd.trace_id`, `dd.span_id`, `dd.env`, `dd.service`, `dd.version` into logs. Configure `DD_ENV`, `DD_SERVICE`, `DD_VERSION` (unified service tagging).
- Logs must be JSON or parsed by the language integration pipeline for correlation to work; custom parsing must keep `dd.trace_id`/`dd.span_id` as strings and use the Trace Remapper.
- Java: tracer 0.74.0+ injects automatically into JSON logs; older versions need `-Ddd.logs.injection=true` or `DD_LOGS_INJECTION=true`. Manual: MDC `dd.trace_id`/`dd.span_id` via `CorrelationIdentifier` (needs `dd-trace-api`).
- Python: `ddtrace-run` or `import ddtrace.auto`; include `dd.*` fields in the format string; JSON trace values are extracted at top level or under `extra` / `record.extra`. Older tracers: `DD_LOGS_INJECTION=true`.
- .NET: `DD_LOGS_INJECTION` default `true` from tracer 3.24.0.
- Traces and logs are sampled independently: a trace ID in a log whose trace was not retained is not a config error.

Sources: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/java/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python/, https://docs.datadoghq.com/logs/log_collection/python/

### Reserved attributes and stack-trace attributes to emit
- Emit the reserved attributes (`host`, `source`, `status`, `service`, `trace_id`, `message`) and the unified tags `env`, `service`, `version`: see **Logging Formats > Reserved attributes** and **Domain 2 > Standard Attributes**.
- Stack-trace display attributes (`logger.name`, `logger.thread_name`, `error.stack`, `error.message`, `error.kind`): see **Standard Attributes > Stack trace attributes**.
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes, https://docs.datadoghq.com/logs/log_collection/#attributes-for-stack-traces

### Common pitfalls

- `logs_enabled` left `false` (default); no `conf.d/*.d/conf.yaml` with a `logs:` section; YAML errors; forgot to restart the Agent.
- Expecting old lines to be shipped: the Agent reads only new lines (default `start_position: end`).
- Last line without a trailing newline never ships.
- Agent user lacks read (file) / execute (directory) permission, often lost again after rotation.
- Plain-text multi-line stack traces split into separate events: emit JSON.
- Using an API key in browser code (use a client token); using an application key on the intake (needs API key).
- Sending logs older than 18 hours; single logs > 1MB get truncated; > 1000 logs per array or > 5MB per payload.
- Writing container logs to files inside the container without a shared volume.

Sources: https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/agent/logs/

# Domain 2: Log Collection

## Enabling Log Collection

### Turning on log collection in the Agent
- Log collection requires Agent v6.0+. It is **not enabled by default**.
- Host Agent: in the main config file `datadog.yaml`, change `logs_enabled: false` to `logs_enabled: true`.
- Containerized Agent / env var: `DD_LOGS_ENABLED=true`.
- Example from the docs:
  ```yaml
  logs_enabled: true
  logs_config:
    auto_multi_line_detection: true
    force_use_http: true
  ```
- `logs_enabled: true` only switches the Logs Agent on. **By default the Agent does not collect any logs**: you also need at least one `logs:` section (in a `conf.d/<name>.d/conf.yaml` file, an Autodiscovery annotation/label, or container collect-all).
- Always **restart the Agent** after a config change; changes are not picked up until restart. Linux (systemd): `sudo systemctl restart datadog-agent` (upstart: `sudo restart datadog-agent`). Kubernetes: `kubectl delete pod <AGENT POD>` (rescheduled automatically). Windows: `agent.exe restart-service`.
- Verify with the status subcommand: `sudo datadog-agent status` (Linux), `docker exec -it <CONTAINER> agent status`, `kubectl exec -it <POD> -- agent status`. A custom source appears under the Checks / Logs Agent section; the status output also shows which transport (HTTPS/TCP) is in use.
- Other subcommands: `configcheck` (prints all loaded and resolved configs), `stream-logs` (stream logs being processed by a running Agent), `diagnose` (connectivity), `flare` (send support bundle), `hostname`.
- The Agent only collects logs **written after** it started tailing/listening. When validating a new setup, make sure new lines are written.
- Log-only Agent (no metrics): set `enable_payloads:` `series: false`, `events: false`, `service_checks: false`, `sketches: false` in `datadog.yaml` (Agent 6.4+), or `DD_ENABLE_PAYLOADS_SERIES=false` etc. in containers.
- Common config checks from the troubleshooting guide: `api_key` defined in `datadog.yaml`; `logs_enabled: true`; at least one `.yaml` in `conf.d/` with a `logs` section; no YAML parse errors; check `sudo grep -i error /var/log/datadog/agent.log`.
Sources: https://docs.datadoghq.com/agent/logs/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/agent/configuration/agent-commands/, https://docs.datadoghq.com/agent/supported_platforms/linux/, https://docs.datadoghq.com/logs/guide/how-to-set-up-only-logs/

### Agent configuration files and locations
| Platform | Main config `datadog.yaml` | Checks/integrations dir `conf.d` |
|---|---|---|
| Linux / AIX | `/etc/datadog-agent/datadog.yaml` | `/etc/datadog-agent/conf.d/` |
| macOS | `/opt/datadog-agent/etc/datadog.yaml` | `/opt/datadog-agent/etc/conf.d/` |
| Windows | `%ProgramData%\Datadog\datadog.yaml` | `%ProgramData%\Datadog\conf.d` |
- Each integration/custom source gets a folder `conf.d/<CHECK_NAME>.d/`; an example `conf.yaml.example` is shipped, rename it to `conf.yaml` to enable. The Agent loads **all valid YAML files** in a `<CHECK>.d/` folder (configs can be split, e.g. `backend.yaml`, `frontend.yaml`).
- Zero-length files in `conf.d` are ignored. `*.yaml.default` files define default checks and are ignored if any other config exists for that check. `auto_conf.yaml` holds Autodiscovery templates.
- **Duplicate log sources**: the Agent does not accept multiple YAML files pointing to the same log source (to avoid duplicates). It considers files in **alphabetical order and uses the first**.
- Agent's own log files (`/var/log/datadog/` on Linux/AIX, `/opt/datadog-agent/logs` on macOS 7.28+, `C:\ProgramData\Datadog\logs` on Windows; 10MB rollover, 1 backup): see **Domain 6 > Agent's own logs, debug mode and flares**.
Sources: https://docs.datadoghq.com/agent/configuration/agent-configuration-files/, https://docs.datadoghq.com/agent/configuration/agent-log-files/

### Custom log collection (conf.d/<name>.d/conf.yaml)
Steps: (1) in `conf.d/` create `<CUSTOM_LOG_SOURCE>.d/` readable by the Datadog user; (2) create `conf.yaml`; (3) add a `logs:` group; (4) restart the Agent; (5) run `status` and look for `<CUSTOM_LOG_SOURCE>` under Checks. Fleet Automation can push custom log configs to many Agents.
- Tail a file:
  ```yaml
  logs:
    - type: file
      path: "/var/log/myapp/app.log"
      service: "myapp"
      source: "myapp"
      tags:
        - env:prod
  ```
  Windows path: `C:\\path\\app.log` (escaped backslashes); `ddagentuser` must have read access.
- TCP/UDP listener (Agent listens; app sends to it):
  ```yaml
  logs:
    - type: tcp      # or udp
      port: 10518
      service: "myapp"
      source: "custom"
  ```
  Supports raw string, JSON and Syslog formats; batch logs separated by line breaks. Agent 7.31+: TCP connection stays open indefinitely when idle. To add the sender IP: `logs_config: use_sourcehost_tag: true` in `datadog.yaml` (adds `source_host` tag).
- journald: `conf.d/journald.d/conf.yaml` with `type: journald`, `path: /var/log/journal/`; `include_units` / `exclude_units` filter units. Journal files are readable by the `systemd-journal` group: `usermod -a -G systemd-journal dd-agent`. With wrong permissions journald sends an **empty payload** (no explicit error).
- Windows Event Log: `conf.d/win32_event_log.d/conf.yaml`, `type: windows_event`, `channel_path: "<CHANNEL>"`, set `source` to the same channel name to get the integration pipeline, `sourcecategory: windowsevent`. List channels with PowerShell `Get-WinEvent -ListLog *`.
- **Every log line must end with a newline** (`\n` or `\r\n`); otherwise the Agent waits indefinitely and never sends that line (files and TCP/UDP).
- Parameters:
  | Param | Req | Notes |
  |---|---|---|
  | `type` | yes | `tcp`, `udp`, `file`, `windows_event`, `docker`, `journald` |
  | `port` | yes for tcp/udp | listening port |
  | `path` | yes for file/journald | supports wildcards |
  | `channel_path` | yes for windows_event | channels |
  | `service` | yes | must equal the APM service name if traced (UST) |
  | `source` | yes | integration name; for custom apps match custom metric namespace (e.g. `myapp` for `myapp.request.count`) |
  | `include_units` / `exclude_units` | no | journald only |
  | `exclude_paths` | no | file + wildcard path; Agent >= 6.18 |
  | `sourcecategory` | no | e.g. `source:postgres, sourcecategory:database` |
  | `start_position` | no | file and journald |
  | `encoding` | no | file only |
  | `tags` | no | list added to each log |
- `start_position` (file: Agent 6.19+/7.19+; journald: 6.38+/7.38+): values `beginning`, `end`, `forceBeginning`, `forceEnd`; **default `end`**. `beginning` does **not** support wildcard paths. If a stored offset exists, it **takes precedence** over `beginning`/`end`; `forceBeginning`/`forceEnd` override the stored offset. Containers always start at `beginning`.
- `encoding`: default UTF-8; `utf-16-le`, `utf-16-be` (Agent 6.23/7.23), `shift-jis` (6.34/7.34). Any other value → read as UTF-8. Changing encoding on a file already being tailed can produce mojibake (offset misaligned) → rotate/replace file.
- Wildcards: `path: /var/log/myapp/*.log` matches every `.log` in that dir (not `myapp.conf`, not subdirs). `/var/log/myapp/*/*.log` matches one level down only. `exclude_paths` removes matches. Path matching is **case sensitive**. Recursive `**` globs need Agent 7.76+ and `logs_config.enable_recursive_glob: true` (off by default). The Agent needs **read and execute** on a directory to list its files.
- `logs_config.open_files_limit` caps simultaneously tailed files; when exceeded, default `file_wildcard_selection_mode: by_name` (reverse lexicographic), or `by_modification_time` (Agent 7.40+, more disk I/O).
Sources: https://docs.datadoghq.com/agent/logs/?tab=tailfiles, https://docs.datadoghq.com/agent/logs/advanced_log_collection/#tail-directories-using-wildcards, https://docs.datadoghq.com/agent/logs/advanced_log_collection/#log-file-encodings, https://docs.datadoghq.com/integrations/journald/

### Integration log setup, source and service
- Integrations and log collection are tied: uncomment/add the `logs:` section in the integration's `conf.d/<integration>.d/conf.yaml` (e.g. `nginx.d/conf.yaml` with `type: file`, `path: /var/log/nginx/access.log`, `service: nginx`, `source: nginx`), enable `logs_enabled`, restart.
- `source` = the integration/technology name. When it matches an integration name, Datadog **automatically installs the integration pipeline** (parsers + facets). Installation is triggered when the first log with that source is received. Integration pipelines are read-only (clone to edit), cannot be deleted (only disabled).
- `service` = application producing the logs; used to pivot Logs ↔ APM, so it must match the APM service name.
- Reserved tag keys: `host`, `device`, `source` (span filtering and automated pipeline creation for Log Management), `service`, `env`, `version`, `team`.
- Tags automatically added by the Agent pre-ingestion: `source`, `service`, `env`, `filename` and `dirname` (file sources), `source_host` (TCP/UDP), `event_type`/`event_source` (Windows events), optional `truncated`, `multiline`.
Sources: https://docs.datadoghq.com/logs/log_collection/, https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes, https://docs.datadoghq.com/logs/log_configuration/pipelines/#integration-pipelines, https://docs.datadoghq.com/integrations/nginx/, https://docs.datadoghq.com/agent/logs/agent_tags/

### Tags and unified service tagging
- Tag format `<key>:<value>` (recommended) or `<value>`. Must start with a letter; allowed: letters, numbers, `_`, `-`, `:`, `.`, `/` (and `@` only for logs via HTTP). Others become `_`. Max **200 characters**. Key = text before the **first** colon (`env:staging:east` → key `env`, value `staging:east`). Avoid unbounded values (user IDs, timestamps).
- Log-specific limits: a log event should have **≤100 tags**, each tag ≤256 characters, ≤10 million unique tags/day.
- `DD_TAGS` uses **whitespace** as separator; `DD_TAGS="test:this is a test"` gives 4 tags. Use YAML/annotations for values with spaces. Host tags in `datadog.yaml` (`tags:` list) apply to all metrics, traces and logs of that Agent.
- Tag inheritance: data inherits host-level tags. Tag precedence: the Agent does **not** enforce precedence; it emits every unique value (e.g. `service:payments`, `service:checkout` from different sources). A global `env` plus a different pod `env` → data carries both.
- **Unified service tagging (UST)**: reserved tags `env`, `service`, `version`. Requires Agent 6.19.x/7.19.x+. `version` should change with each deployment.
  - Kubernetes: labels `tags.datadoghq.com/env|service|version` on the workload **and** the pod template; `DD_ENV`/`DD_SERVICE`/`DD_VERSION` env vars (via downward API) only needed for APM. Per-container: `tags.datadoghq.com/<CONTAINER>.service`.
  - Docker: env vars `DD_ENV`, `DD_SERVICE`, `DD_VERSION` + labels `com.datadoghq.tags.env|service|version`. Non-traced third-party containers (Redis, NGINX) can use labels only.
  - ECS Fargate with FireLens/Fluent Bit: UST only for metrics and traces, **not logs**.
  - Non-containerized: `DD_ENV=… DD_SERVICE=… DD_VERSION=… /bin/my-service`; with logs injection the tracer injects env/service/version into logs. Single service per host: `env: <ENV>` and `tags: - service:<SERVICE>` in `datadog.yaml`.
  - The official `service` of a container log defaults to the container short image if no Autodiscovery logs config is present.
  - OpenTelemetry mapping: `deployment.environment.name` → `env`, `service.name` → `service`, `service.version` → `version`.
Sources: https://docs.datadoghq.com/getting_started/tagging/, https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/, https://docs.datadoghq.com/getting_started/tagging/assigning_tags/, https://docs.datadoghq.com/logs/log_collection/#limitations

### File permissions
- The Agent does not run as root. Agent user: `ddagentuser` on Windows; `dd-agent` on Linux. It needs **read** on log files and **read + execute** on every parent directory.
- Error messages in `status`, `namei` diagnosis, `chmod` fixes, ACLs, logrotate `644`, Windows `icacls ... (OI)(CI)(RX)` and the `/var/log/datadog` ownership fix (`chown -R dd-agent:dd-agent`): **Domain 6 > File permissions** and **Agent's own logs, debug mode and flares**.
Sources: https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/#permission-issues-tailing-log-files, https://docs.datadoghq.com/agent/troubleshooting/permissions/

### Docker log collection
- Containerized Agent `docker run` flags: `-e DD_LOGS_ENABLED=true`, `-e DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL=true` (log config for **all** containers), `-e DD_CONTAINER_EXCLUDE="name:datadog-agent"` (don't collect the Agent's own logs/metrics; regex), `-v /var/run/docker.sock:/var/run/docker.sock:ro` (discover containers / stdout via socket), `-v /var/lib/docker/containers:/var/lib/docker/containers:ro` (file-based collection, Agent 6.27/7.27+), `-v /opt/datadog-agent/run:/opt/datadog-agent/run:rw` (stores last line collected per container so logs aren't lost across restarts/network issues).
- Host Agent with Docker: `logs_enabled: true`, `listeners: - name: docker`, `config_providers: - name: docker, polling: true`, `logs_config: container_collect_all: true`. Windows 10: add `ddagentuser` to `docker-users`.
- File-based container collection is default since 6.33/7.33 (better performance than socket). Migration: only new containers use files; `DD_LOGS_CONFIG_DOCKER_CONTAINER_FORCE_USE_FILE=true` forces all (possible duplicates).
- Defaults: `source` and `service` = `short_image` tag (Agent 6.8+). Logs from `stderr` default to status `Error`. Custom (host-file) collection does **not** add container metadata tags.
- Autodiscovery label: `com.datadoghq.ad.logs='[{"source":"nginx","service":"webapp"}]'` (Dockerfile `LABEL`, compose `labels:`, or `docker run -l`). Label with `type: file` + `path` (7.25+): path relative to the Agent container (shared volume); stdout/stderr then **not** collected automatically, add a second `{"type":"docker",...}` entry; `source`/`service` have no default.
- Docker Compose: `DD_CONTAINER_EXCLUDE` value must not be quoted. Agent reads AD labels every 1 second; since 6.14 collects stopped containers' logs if not removed.
Sources: https://docs.datadoghq.com/containers/docker/log/, https://docs.datadoghq.com/containers/guide/container-discovery-management/

### Kubernetes log collection
- Recommended: Agent DaemonSet tails Kubernetes log files under `/var/log/pods` (more efficient than Docker socket, works with any runtime).
- Helm `datadog-values.yaml`: `datadog.logs.enabled: true`, `datadog.logs.containerCollectAll: true`. Operator `DatadogAgent`: `spec.features.logCollection.enabled: true`, `containerCollectAll: true`. DaemonSet env vars: `DD_LOGS_ENABLED`, `DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL`.
- `containerCollectAll` default **false** → nothing collected unless an Autodiscovery log config exists (annotation, `DatadogInstrumentation` CRD, or AD config file). When true, `source`/`service`/`short_image` = container short image (e.g. `gcr.io/owner/example-image:latest` → `example-image`). `tags.datadoghq.com/service` label sets `service`.
- Annotation: `ad.datadoghq.com/<CONTAINER_NAME>.logs: '[{"source":"java","service":"example-app","tags":["foo:bar"]}]'`. Matches the **container name** (`.spec.containers[i].name`), not the image. For Deployments/ReplicaSets put annotations in `.spec.template.metadata`, not on the Deployment's own metadata.
- AD config files (Helm `datadog.confd`, Operator `override.nodeAgent.extraConfd.configDataMap`) match by `ad_identifiers` = container short image.
- Filtering: `DD_CONTAINER_EXCLUDE_LOGS` / `DD_CONTAINER_INCLUDE_LOGS`, annotations `ad.datadoghq.com/logs_exclude` (pod) and `ad.datadoghq.com/<CONTAINER>.logs_exclude`. Exclusion via these wins over explicit AD log configs. Inclusion generally beats exclusion, except `ad.datadoghq.com/exclude` annotations.
- File inside container: annotation with `"type":"file","path":...`; path is relative to the Agent container, mount the dir (e.g. `hostPath`) in both app and Agent; use `%%kube_pod_name%%` in path for replicas; stdout/stderr not collected unless also listed.
- Unprivileged Agent + Docker runtime cannot read `/var/log/pods` symlinks; mount Docker socket; `DD_LOGS_CONFIG_K8S_CONTAINER_USE_FILE=true` forces file mode.
Sources: https://docs.datadoghq.com/containers/kubernetes/log/, https://docs.datadoghq.com/containers/guide/container-discovery-management/

### Transport, compression, limits
- Agent 6.19+/7.19+: default transport is **compressed HTTPS** (port **443**). At startup with logs enabled the Agent runs an HTTPS connectivity test; if it fails it falls back to TCP until next restart. The test runs **only at startup**. Check with `agent status`.
- Force HTTPS: `logs_config: force_use_http: true` (env `DD_LOGS_CONFIG_USE_HTTP=true` per the page; see note). Force TCP: `logs_config: force_use_tcp: true` / `DD_LOGS_CONFIG_FORCE_USE_TCP=true`. Always enforce a specific transport when using a proxy. A **SOCKS5 proxy** (`logs_config.socks5_proxy_address`) **enforces TCP**.
- HTTPS is recommended (200 returned after storage). Batch limits: max batch 1MB, max single log 900kB, max 1,000 logs per batch. Batch wait up to **5 s** by default; `logs_config.batch_wait` / `DD_LOGS_CONFIG_BATCH_WAIT`, integer 1-10 seconds.
- `compression_level` / `DD_LOGS_CONFIG_COMPRESSION_LEVEL`: 0 (none) to 9 (max); **default 6**.
- Legacy TCP: TLS on port 10516 (US1) / 443 (EU); 10514 without TLS (US1). TCP log collection is **not supported** (no delivery or reliability guarantees; data may be lost without notice). TCP endpoints are only listed for US1 and EU; the other sites (US3, US5, AP1, AP2, UK1, US1-FED, US2-FED) have no TCP endpoint.
- TCP proxy: `logs_config.logs_dd_url: "<proxy>:<port>"`, `logs_no_ssl: true`. HTTPS uses the same proxy settings as other data types.
- Intake limits (1MB per log, 25KB recommended, Agent splits at 900KB, timestamps up to 18 h in the past, attribute and tag limits): see **Domain 1 > Logging Formats > Log size and attribute limits**.
Sources: https://docs.datadoghq.com/agent/logs/log_transport/, https://docs.datadoghq.com/agent/logs/proxy/, https://docs.datadoghq.com/logs/log_collection/#custom-log-forwarding

### AWS: Datadog Forwarder (Lambda)
- AWS Lambda function that ships CloudWatch Logs and S3 logs (also SNS, Kinesis events) to Datadog. For Lambda telemetry Datadog now recommends the Lambda Extension instead.
- Install via **CloudFormation** (recommended), Terraform module, or manual. Required params: `DdApiKey` (or `DdApiKeySecretArn` / `DdApiKeySsmParameterName`) and `DdSite`. Function has logical ID `Forwarder`. **Install in every region** you collect from. Adjust settings by updating the CloudFormation stack, not editing the Lambda. v4.1.0+ is ARM64 only; v5.0.0 removed TCP (`DD_USE_TCP`), all HTTPS.
- Triggers: **automatic** (Datadog AWS integration tile > Log Collection tab > add Forwarder ARN > Log Autosubscription toggles; not cross-account/cross-region) or **manual** (Lambda console > Add trigger > CloudWatch Logs; S3 event `Object Created`/`s3:ObjectCreated:*`). Auto filters are named `DD_LOG_SUBSCRIPTION_FILTER_<LOG_GROUP>`.
- Useful params: `DdTags` (comma-delimited, no trailing comma, e.g. `env:prod,stack:classic`), `DdSource` (overrides auto-detected source; adds `source_overridden:true`), `ExcludeAtMatch` / `IncludeAtMatch` (regex on log message; a log matching both is **excluded**), `RedactIp`, `RedactEmail`, `DdScrubbingRule`, `DdCompressionLevel` (default 6), `DdForwardLog`, `DdMultilineLogRegexPattern` (S3 multiline), `AdditionalTargetLambdaArns`, `DdStoreFailedEvents`, `ReservedConcurrency` (recommend ≥10, default 0). Manual install: CloudFormation names → screaming snake case env vars (`DdApiKey` → `DD_API_KEY`).
- S3 files must be newline-delimited; a JSON array is ingested as one event. Each AWS service has its `source` (e.g. `source:cloudtrail`, `source:elb`, `source:vpc`, `source:lambda`).
Sources: https://docs.datadoghq.com/logs/guide/forwarder/, https://docs.datadoghq.com/logs/guide/send-aws-services-logs-with-the-datadog-lambda-function/

### AWS: Amazon Data Firehose destination
- Fully managed by AWS: no infrastructure to maintain. Datadog is a built-in destination. CloudWatch log groups → (optional Kinesis Data Stream, recommended when multiple consumers) → Firehose stream → Datadog.
- Console: Amazon Data Firehose > **Create Firehose stream** > source `Amazon Kinesis Data Streams` or `Direct PUT` > destination `Datadog` > `Datadog logs` HTTP endpoint URL for your site > API key (or Secrets Manager `{"api_key":"..."}`) > optional retry, buffer, **Parameters** (attached as tags) > **S3 backup bucket** for failed events (forward it with the Forwarder) > Create.
- Intake limit **65,536 events per batch**; recommended buffer size **2 MiB**. A single Kinesis payload must not exceed 65,000 log messages.
- IAM role trusted by `logs.amazonaws.com`; actions `firehose:PutRecord`, `firehose:PutRecordBatch`, `kinesis:PutRecord`, `kinesis:PutRecords`. Subscription filter (`aws logs put-subscription-filter` or console **Create Kinesis / Amazon Data Firehose subscription filter**) must be in the same account. **Each CloudWatch log group can only have two subscriptions.**
- Find logs: `@aws.firehose.arn:"<ARN>"`. Source detected from log group name (`/aws/lambda/...` → `source:lambda`), service defaults to source (function name for Lambda), tags `region`, `aws_account`, `sourcecategory:aws`. Override with Firehose **Parameters (Common Attributes)**; `ddsource`/`service`/`ddtags` in log body only if enabled by Support.
Sources: https://docs.datadoghq.com/logs/guide/send-aws-services-logs-with-the-datadog-kinesis-firehose-destination/

### Azure and Google Cloud
- Azure automated log forwarding: Datadog **Integrations > Azure > Configure Log Forwarding** (or ARM template; needs management-group permission). Deploys a control plane (Function apps) that discovers resources and sets **diagnostic settings**, plus log forwarders (Azure Container Apps + storage accounts) deployed in each forwarding subscription that scale with volume. Diagnostic settings can only target storage accounts in the **same region**; Log Analytics Workspace forwarding also only works within the log forwarder's region. Commercial Azure only. Log Analytics Workspace data export rules → `ddlogstorage*` storage account.
- Azure manual: ARM template/Container App or Blob Storage trigger Azure Function with `DD_API_KEY`, `DD_SITE`; diagnostic settings to the storage account.
- Google Cloud (recommended): Cloud Logging **Log Router sink** → **Pub/Sub topic** → **pull** subscription → **Dataflow job using the Datadog (`Pub/Sub to Datadog`) template** → Datadog Logs API URL. Batching + compression = most network-efficient. Setup via GCP integration tile **Configure Log Collection** > Quick Start or Terraform, or manual. Create a dead-letter topic (`outputDeadletterTopic`); store API key in Secret Manager; enable the Dataflow API; custom worker service account for least privilege. **Pub/Sub Push** subscriptions are deprecated (no batching/compression; can't reach external endpoints from VPC). Monitor `gcp.pubsub.subscription.num_undelivered_messages`. Agent can also collect GCE/GKE app logs.
Sources: https://docs.datadoghq.com/logs/guide/azure-automated-log-forwarding/, https://docs.datadoghq.com/logs/guide/azure-manual-log-forwarding/, https://docs.datadoghq.com/logs/guide/google-cloud-log-forwarding/, https://docs.datadoghq.com/logs/guide/collect-google-cloud-logs-with-push/

### Common pitfalls
- `logs_enabled: true` but no `logs:` config → nothing collected.
- Forgot to restart the Agent.
- Last log line without trailing newline never sent.
- Agent user lacks `x` on a parent directory (wildcards fail: "check that all its subdirectories are executable").
- logrotate recreates files with restrictive perms → set 644 / Windows `(OI)(CI)` inheritance.
- `source` misspelled or not an integration name → no integration pipeline.
- `service` differs from APM service → no logs/traces pivot.
- K8s annotation keyed on image instead of container name, or put on Deployment metadata instead of the pod template.
- `start_position: beginning` with wildcard path is unsupported; stored offsets override `beginning`/`end`.
- Only logs with timestamps up to 18h in the past can be submitted; the HTTPS API accepts logs up to 1MB (Agent splits at 900KB).
Sources: https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/agent/logs/

## Log Filtering & Obfuscation

### Where Agent processing rules live

- Agent-side rules run on the host, before logs are sent to Datadog. Two places to define them:
  - **Per log source / integration**: `log_processing_rules` inside a `logs:` entry of an integration config (`conf.d/<INTEGRATION>.d/conf.yaml`), a Docker label `com.datadoghq.ad.logs`, or a Kubernetes pod annotation `ad.datadoghq.com/<CONTAINER_NAME>.logs`.
  - **Global (all logs collected by this Agent)**: `processing_rules` under `logs_config` in the main `datadog.yaml` (Agent v6.10+), or the env var `DD_LOGS_CONFIG_PROCESSING_RULES` (JSON array). Operator: `spec.override.[nodeAgent|clusterAgent|clusterChecksRunner].env`; Helm: `datadog.env`.
- Key naming pitfall: `log_processing_rules` = per-integration; `logs_config.processing_rules` = global in `datadog.yaml`.
- Global rule types: `exclude_at_match`, `include_at_match`, `mask_sequences` (v6.10+) and `exclude_truncated` (v7.69+). `multi_line` is not in the documented list of global rule types; configure it per source in `log_processing_rules`.
- **Integration-specific rules completely override global rules** for that integration (they are not merged). If a source has its own `log_processing_rules`, global rules do not apply to it; copy any global masking rule into the source config if you still need it.
- If the global processing rules have a format issue, **the Agent does not start the log collector**. Troubleshoot with the Agent `status` subcommand.
- Multiple rules are **applied sequentially, each on the result of the previous one** (order in the list matters; e.g. a mask that runs first changes what a later exclude rule sees).
- Patterns use **Golang regexp syntax** (RE2-style).
- Each rule has `type`, `name`, `pattern` (plus `replace_placeholder` for `mask_sequences`; `exclude_truncated` needs only `type`).

```yaml
# datadog.yaml (global)
logs_config:
  processing_rules:
    - type: exclude_at_match
      name: exclude_healthcheck
      pattern: healthcheck
    - type: mask_sequences
      name: mask_user_email
      pattern: \w+@datadoghq.com
      replace_placeholder: "MASKED_EMAIL"
```

```shell
DD_LOGS_CONFIG_PROCESSING_RULES='[{"type": "mask_sequences", "name": "mask_user_email", "replace_placeholder": "MASKED_EMAIL", "pattern" : "\\w+@datadoghq.com"}]'
```

Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#global-processing-rules, https://docs.datadoghq.com/agent/logs/advanced_log_collection/#multi-line-log-aggregation-faq

### Filtering: exclude_at_match, include_at_match, exclude_truncated

- `exclude_at_match`: if the pattern is **contained in the message**, the log is excluded and not sent to Datadog.
- `include_at_match`: only logs whose message includes the pattern are sent. **If several `include_at_match` rules are defined, all patterns must match** (logical AND).
- To include on "pattern A OR pattern B", use **one** rule with an alternation: `pattern: abc|123`. Long alternations can be split over lines in a double-quoted YAML string ending lines with `\`.
- `exclude_truncated` (Agent v7.69+): drops logs the Agent truncated; no pattern needed.

```yaml
logs:
  - type: file
    path: /my/test/file.log
    service: cardpayment
    source: java
    log_processing_rules:
    - type: exclude_at_match
      name: exclude_datadoghq_users
      pattern: \w+@datadoghq.com
    - type: exclude_truncated
```

- Containers: same rules inside the JSON of the Docker label `com.datadoghq.ad.logs` or the pod annotation `ad.datadoghq.com/<CONTAINER_NAME>.logs`.
  - **Escape regex backslashes** in labels/annotations: `\d` becomes `\\d`, `\w` becomes `\\w`.
  - Label/annotation value **must be valid JSON**: no trailing commas, no comments.
- Excluding whole containers (not message content): `DD_CONTAINER_EXCLUDE_LOGS` / `DD_CONTAINER_INCLUDE_LOGS` (Agent v7.20+), space-separated regexes on `name:`, `image:`, `kube_namespace:`. `DD_CONTAINER_EXCLUDE` excludes both logs and metrics. You cannot exclude globally with `DD_CONTAINER_EXCLUDE` then re-include with `DD_CONTAINER_INCLUDE_LOGS`.
- Files: `exclude_paths` (with wildcard `path`, Agent 6.18+) excludes whole files from tailing.

Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#filter-logs, https://docs.datadoghq.com/containers/guide/container-discovery-management/

### Scrubbing at the Agent: mask_sequences

- `mask_sequences` replaces all matched groups with the value of `replace_placeholder`.
- Agent v7.17+: `replace_placeholder` can reference capture groups `$1`, `$2`... Use `${<GROUP_NUMBER>}` when text must follow the group with no space.
  - Example: `pattern: "(User email: )[^@]*@(.*)"`, `replace_placeholder: "$1 masked_user@${2}"` turns `User email: foo.bar@example.com` into `User email: masked_user@example.com`.

```yaml
log_processing_rules:
  - type: mask_sequences
    name: mask_credit_cards
    replace_placeholder: "[masked_credit_card]"
    pattern: (?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})
```

- Agent masking is the option when data **must not leave your environment**. (Sensitive Data Scanner in the cloud redacts only after data reaches the Datadog backend.)
- The Manage Sensitive Logs guide: if sensitive data is prohibited from leaving your environment, add scrubbing rules at source collection (Agent `mask_sequences`, Autodiscovery for container fine-grained control; the Serverless Forwarder has similar scrubbing).

Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#scrub-sensitive-data-from-your-logs, https://docs.datadoghq.com/logs/guide/manage-sensitive-logs-data-access/#stop-sending-sensitive-data-to-datadog

### Commonly used log scrubbing rules

| Goal | Type | Pattern (abridged) | Placeholder |
|---|---|---|---|
| Drop lines containing `sensitive-info` | `exclude_at_match` | `(?:sensitive\-info)` | - |
| Redact value after `my_key=` | `mask_sequences` | `(?:my_key=[A-Za-z0-9\s_]*[A-Za-z0-9][A-Za-z0-9\s_])` | `my_key=[VALUE REDACTED]` |
| US SSN | `mask_sequences` | `(?:\d{3}-?\d{2}-?\d{4})` | `[SSN REDACTED]` |
| Email (RFC 5322) | `mask_sequences` | long RFC 5322 regex | `[EMAIL REDACTED]` |
| Credit cards (Visa, MC, Amex, Diners, Discover, JCB) | `mask_sequences` | card regex | `[CREDIT CARD REDACTED]` |
| US postal codes | `mask_sequences` | `(?:\d{5}-\d{4}|\d{5}|[A-Z]\d[A-Z] \d[A-Z]\d)` | `[POSTAL CODE REDACTED]` |
| Between parentheses / brackets | `mask_sequences` | `(?:ExampleConfig\([^\)]+)` | ... |
| Class A IPs | `mask_sequences` | IPv4 regex | `[IP REDACTED]` |

- Pitfall: the plain credit-card regex can match **trace IDs** and break log/trace correlation. If you connect logs and traces, use the variant wrapped in word boundaries `\b(?:...)\b`.

Sources: https://docs.datadoghq.com/logs/guide/commonly-used-log-processing-rules/

### Manual multi-line aggregation (multi_line)

- For non-JSON logs that span several lines (stack traces). `type: multi_line` aggregates all lines into a single entry **until the given pattern is detected again**, so the pattern must identify the **start of a new log** (typically the timestamp).
- Regex must match at the **beginning** of a log; patterns cannot match mid-line. A never-matching pattern may cause log line losses. Log collection works with precision up to the millisecond; logs with greater precision are not sent even if they match.

```yaml
log_processing_rules:
  - type: multi_line
    name: new_log_start_with_date
    pattern: \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])
```

| Raw string | Pattern |
|---|---|
| `14:20:15` | `\d{2}:\d{2}:\d{2}` |
| `11/10/2014` | `\d{2}\/\d{2}\/\d{4}` |
| `Thu Jun 16 08:29:03 2016` | `\w{3}\s+\w{3}\s+\d{2}\s\d{2}:\d{2}:\d{2}\s\d{4}` |
| `20180228` | `\d{8}` |
| `2020-10-27 05:10:49.657` | `\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}` |
| `{"date": "2018-01-02"` | `\{"date": "\d{4}-\d{2}-\d{2}` |

- FAQ: use manual rules when you know the format (precise control); use automatic detection when there are many sources / unknown formats. If a multi-line pattern matches nothing, non-JSON lines are processed individually; JSON lines are treated as single lines and only the first valid JSON enters intake (rest dropped).

Sources: https://docs.datadoghq.com/agent/logs/advanced_log_collection/#manually-aggregate-multi-line-logs, https://docs.datadoghq.com/agent/logs/advanced_log_collection/#multi-line-log-aggregation-faq

### Automatic multi-line detection and aggregation

- Current implementation: Agent **7.65.0+**. **Enabled by default starting with Agent 7.82.0**; disabled by default on older versions. Legacy (V1) applies to Agent < 7.65 or when forced with `logs_config.force_auto_multi_line_detection_v1: true`.
- Disable: `logs_config.auto_multi_line_detection: false` or `DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION=false`. Per source: `auto_multi_line_detection: false|true` in the `logs:` entry (per-integration settings accept the same `auto_multi_line` options as `datadog.yaml`).
- Default: only lines that **begin with a datetime** start a new log; following lines (exceptions, stack frames) are aggregated into it.
- Default-on features: `enable_datetime_detection` (datetime aggregation) and `enable_json_detection` (JSON logs never aggregated). Env vars `DD_LOGS_CONFIG_AUTO_MULTI_LINE_ENABLE_DATETIME_DETECTION`, `..._ENABLE_JSON_DETECTION`.
- Datetime must appear in the **first 60 bytes** and include **both date and time**: `2021-03-28 13:45:30`, `2023-03-28T14:33:53.743350Z`, `Jun 14 15:16:01`, `2024/05/16 19:46:15` are detected; `12:30:2017`, `12:30:20`, `2024/05/16` are not.
- Customize with `logs_config.auto_multi_line_detection_custom_samples` (env `DD_LOGS_CONFIG_AUTO_MULTI_LINE_DETECTION_CUSTOM_SAMPLES`):
  - `sample:` a sample first line. Tokenizes the first 60 bytes of the log and the sample (words+length, whitespace, numbers+length, special chars, datetime components); if **75%** of the log's tokens match, it is marked for aggregation. Recommended for stable formats; easier than regex.
  - `regex:` works like a `multi_line` rule.
  - Optional `label:` per sample/regex. Legacy `auto_multi_line_extra_patterns` is still supported when migrating from V1.
- Labels: `start_group` (beginning of a multi-line log; flushes buffer; only one buffered at a time), `aggregate` (added to existing multi-line log; default when nothing matches), `no_aggregate` (never part of aggregation; flushes buffer; used for JSON).
- **JSON aggregation** (Agent 7.67+): pretty-printed JSON is compacted to one line. It **runs before `log_processing_rules`**, so a rule regex expecting `"key": "value"` (space after colon) will not match; use `"key":"value"` or disable with `logs_config.auto_multi_line.enable_json_aggregation: false`. Tag with `auto_multi_line.tag_aggregated_json: true` and search `aggregated_json:true`.
- **Stack trace aggregation** (Agent 7.81+): Go stack traces; `auto_multi_line.stack_trace_parsers` default `["go"]`, set `[]` to disable.
- Debugging: `logs_config.tag_multi_line_logs: true` adds tag `multiline` (e.g. `auto_multiline`, `multiline_regex`); `logs_config.tag_truncated_logs: true` adds tag `truncated` (`single_line` if too long before aggregation, `multi_line` if a bad pattern overflowed the aggregation buffer).
- Reference defaults: `timestamp_detector_match_threshold` 0.5; `tokenizer_max_input_bytes` 60.
- Legacy (V1, Agent 7.37+): `auto_multi_line_extra_patterns`, `auto_multi_line_default_match_threshold` (lower = more matches), Helm `datadog.logs.autoMultiLineDetection`.

Sources: https://docs.datadoghq.com/agent/logs/auto_multiline_detection/, https://docs.datadoghq.com/agent/logs/auto_multiline_detection_legacy/

### Sensitive Data Scanner (SDS) for logs

- Stream-based pattern matching to identify, tag, and optionally redact or hash sensitive data. Found in **Organization Settings > Sensitive Data Scanner**. Guided setup when no scanning groups exist.
- **In the cloud**: data leaves your environment first; scanned and redacted in the Datadog backend during processing, **before indexing** and other routing decisions, and before being shown in the UI. (In-environment scanning uses Observability Pipelines, out of scope here.)
- Logs: all structured and unstructured content (message and attribute values). SDS does not scan integer/float/double values (numbers in strings are scanned).
- **Scanning group** = what to scan: query filter + toggles per product (logs, APM, RUM, events) + optional sampling **10-99%**. A new group is **disabled by default**; turn on its toggle. Limits: 20 scanning groups/org (default), 750 scanning rules/org.
- **Scanning rule** = what to match: library rule (Scanning Rule Library, with recommended keywords) or custom regex (PCRE subset: no backreferences/lookarounds, atomic groups, possessive quantifiers, `\K`, `\R`, conditionals, recursion...). Keywords: by default within **30 characters before** the match; max **20 keywords** per rule; case-insensitive.
- Action on Match: scan **Entire Event** (optionally exclude attributes) or **Specific Attributes** (attribute path without `@`).
- Actions: **Redact** (replace with your token, e.g. `[sensitive_data]`), **Partially redact**, **Hash** (FarmHash 64-bit fingerprint), **Mask** (reversible for users with `Data Scanner Unmask`). Redact, partial redact, and hash are irreversible.
- With **sampling enabled** you cannot choose obfuscating actions (redact, partially redact, hash); disable sampling to obfuscate.
- Mask: unmask in Findings page (eye icon) or Log/Trace/RUM Explorer; not for API/Terraform/archives (always obfuscated); not on rehydrated logs; not recommended for credentials.
- Permissions: Datadog Admin by default; `data_scanner_read` / `data_scanner_write` (Compliance) for custom roles; `data_scanner_unmask`.
- Tags: recommended `sensitive_data` and `sensitive_data_category`; use them in RBAC restriction queries, searches, monitors.
- **Rules affect only data arriving after the rule was defined** (no retroactive scan). Rehydrated logs are not re-scanned. SDS does not affect rules defined on the Agent.
- Redact data in **tags**: remap tag to an attribute with a Remapper processor (uncheck **Preserve source attribute**), then scan that attribute with Specific Attributes.
- Suppressions (Match exactly / Start with / End with) ignore risk-accepted matches.
- Excluded namespaces (logs): 30 chars after reserved words like `host`, `service`, `status`, `env`, `trace_id`, `timestamp`, `date` are never redacted.
- Alerts for logs: security notification rule from Findings (no log samples). OOTB dashboard "Sensitive Data Scanner Overview".

Sources: https://docs.datadoghq.com/security/sensitive_data_scanner/, https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data/

### Handling sensitive logs already in Datadog

- Intentional sensitive data: restrict with logs RBAC. Unintentional: (1) determine scope with a **sensitive outline query** (e.g. `version:x.y.z source:python status:debug`), (2) fix upstream, (3) handle data already sent.
- Where data may live (most to least likely): indexes, archives, log-based metrics, log monitor notifications (log samples), Live Tail (no persistence beyond 50 logs cached in browser).
- Fix upstream: SDS for streaming logs; add an index **exclusion filter** on the outline query to stop indexing; Agent scrubbing to stop sending.
- **Make un-queryable until age-out**: Logs > Configuration **Data Access** page: create a **restriction query** (`logs_read_data` permission) from the outline query and apply to roles; can scope by `@timestamp:[start TO end]`. Un-queryable logs don't appear in Log Explorer, Dashboards, or Live Tail. Each role has one restriction query; roles on the Unrestricted Access list see all logs.
- Archives must be patched by you (archive format docs).
- Retention: Datadog deletes logs past the longest retention; shorten via Log Indexes > Edit > **Set Index Retention**. Delete an entire index via its Delete icon.
- **Logs Data Deletion** (Organization Settings > Data Deletion): enable in Organization Settings > Preferences (**Org Admin only**); role needs **Logs Delete Data** permission; select product, time frame, query, Delete, confirm. Starts instantly; recoverable/cancellable for **10 days**, then permanent. Max **5 concurrent** deletions. **Derived data (e.g. metrics generated from logs) is not deleted.** History kept 90 days in Deletion History; also in Audit Trail (`@asset.name:"Data Deletion"`). Stop sending the data first. Non-logs data: contact Support.

Sources: https://docs.datadoghq.com/logs/guide/manage-sensitive-logs-data-access/, https://docs.datadoghq.com/logs/guide/delete_logs_with_sensitive_data/, https://docs.datadoghq.com/account_management/delete_data/, https://docs.datadoghq.com/logs/guide/logs-rbac/

### Agent exclusion vs index exclusion filters

| | Agent `exclude_at_match` / `include_at_match` | Index exclusion filter |
|---|---|---|
| Where | On the host, before sending | In Datadog, after ingestion and processing |
| Logs reach Datadog? | No (never sent/ingested) | Yes, ingested |
| Live Tail / log-based metrics / archives | Not available | Still available |
| Change | Edit Agent config, restart | Toggle in UI or API, sampling 0-100% |

- Exclusion filter defaults: query `*`, sampling `Exclude 100% of logs`, toggle active. Only the **first active matching** exclusion filter applies. Patterns view has an **Add Exclusion Filter** button.

Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters, https://docs.datadoghq.com/logs/guide/getting-started-lwl/

## Processors & Pipelines

### How pipelines process logs
- Datadog automatically parses JSON-formatted logs. Raw (non-JSON) and JSON logs can then go through processing pipelines that translate many formats into one common format and apply an attribute naming convention.
- A pipeline = a filter query + an ordered list of processors (and, for top-level pipelines, nested pipelines).
- Every incoming log is tested against **every** pipeline filter, in pipeline-list order. If it matches a filter, **all processors of that pipeline run sequentially**, then the log moves on to the next pipeline. A log can therefore be modified by several pipelines.
- The pipeline filter is evaluated **before** any of that pipeline's processors. You cannot filter a pipeline on an attribute that the same pipeline extracts.
- All processing happens at ingestion: changes to a pipeline only affect **new** logs, never logs already ingested.
- Pipelines and processors are configured in the UI at Logs > Pipelines (app path `/logs/pipelines`, page also called the Processing page), or through the Logs Pipelines API (`/api/v1/logs/config/pipelines`) and Terraform. No Agent or server-side change is needed.
- Pipeline/processor documentation here is for cloud-side (Datadog SaaS) processing. On-prem processing is Observability Pipelines (out of scope for this exam).
- Recommended limits (best practice): **at most 20 processors per pipeline** and **at most 10 parsing rules per Grok parser**. Datadog may disable underperforming parsing rules, processors or pipelines that impact service performance.
- Pipeline tags and description are optional; pipeline tags do **not** affect logs, they only help filter/search on the Pipelines page.
- Processor API objects all share `type`, `name`, `is_enabled` (default `false` in the API).
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/, https://docs.datadoghq.com/logs/log_configuration/processors/, https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/

### Creating, managing and previewing pipelines
- Create: Pipelines page > **New Pipeline** > pick a log from the live tail preview to build a filter, or write your own filter (dropdown or the `</>` icon) > name it > optional description/tags > **Create**.
- Add content: hover a pipeline, click the arrow to expand, then **Add Processor** or **Add Nested Pipeline**.
- **Custom pipeline for a source with no integration**: create a custom pipeline whose filter targets that source (for example `source:my-app`) and add processors (Grok parser, remappers, ...) to parse it.
- **Clone**: reuse rules and processors without starting over. The docs state "When you clone a pipeline, Datadog automatically disables the pipeline you cloned. Click the toggle to enable."
- **Move to**: reorder pipelines precisely from the sliding option panel with the Move to modal. Pipelines cannot be moved into read-only pipelines.
- **Manage**: each pipeline shows last modification time and user; the list can be filtered by that modification info and facets such as enabled/disabled or read-only.
- **Estimated usage metrics** per pipeline (volume and count of logs ingested/modified) with a link to the out-of-the-box Logs Estimated Usage dashboard.
- **Preview pipeline changes** (pipeline simulation): while editing, preview how changes affect logs using a live tail processed with your proposed changes.
  - Compare against **Your changes** (deployed version vs your edits) or **Entire pipeline** (log entering the pipeline vs after the whole pipeline).
  - Filter by impact: **All logs**, **Impacted logs** (changed by your edits in this session), **Not impacted logs**.
- **Permissions** (Granular Access Control on pipelines, assignable to roles, users, teams; API = Restriction Policies, also Terraform):
  - Unrestricted pipeline: any user with `logs_write_pipelines` can modify it and its processors.
  - Edit scopes: **Editor** (only listed principals edit the pipeline config and processors) and **Processor Editor** (only processors, including nested pipelines, can be edited by listed principals; nobody can change the pipeline's filter or its order in the list).
  - Being on a restriction list does NOT grant `logs_write_pipelines` / `logs_write_processors`; those must be granted separately.
  - `logs_write_pipelines`: create/modify pipelines (name, filter, reorder) and grant Logs Write Processors to other roles. `logs_write_processors`: create, edit or delete processors and nested pipelines; global or restricted to some pipelines. `logs_read_config`: read logs configuration.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/, https://docs.datadoghq.com/account_management/rbac/permissions/

### Nested pipelines
- A nested pipeline is a pipeline inside a pipeline, used to split processing in two steps (e.g. first filter by team, then by integration/service).
- A top-level pipeline can contain nested pipelines **and** processors; a nested pipeline can contain **only processors** (one level of nesting).
- To nest: hover the pipeline > **Move to** icon > choose target pipeline > **Move**.
- A pipeline that already contains nested pipelines can only be moved to another **top-level** position, never into another pipeline.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#nested-pipelines

### Integration pipelines and the Pipeline Library
- Integration pipelines exist for supported sources. They are **read-only**, parse logs appropriately for that technology and add the corresponding facets.
- Install trigger: configure the log `source` to the integration's source name; when Datadog receives the **first log with that source**, the integration pipeline is installed automatically and added to the pipeline list.
- To edit: **clone** it and edit the clone. Integration pipelines **cannot be deleted, only disabled**.
- **Integration Pipeline Library** (Pipelines > Library, `/logs/pipelines/pipeline/library`): browse the full list of integration pipelines to see how Datadog processes each format by default; pipelines can be cloned from the library.
- Integration pipelines support the **default** log format of a technology. Customized formats may not parse: clone and troubleshoot on the clone.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#integration-pipelines, https://docs.datadoghq.com/logs/faq/how-to-investigate-a-log-parsing-issue/

### Preprocessing for JSON logs
- Runs **before** pipeline processing, only on JSON logs, mapping well-known keys to reserved attributes; within each list, the first attribute present wins (order matters). **Preprocessing is the only way to define one of your log attributes as `host`.**
- Default lists, editing steps, the Kubernetes `hostname` pitfall and the date rules (ISO8601, UNIX ms, RFC3164; 18 h in the past, 2 h in the future; epoch seconds -> Arithmetic `* 1000` + date remapper): **Domain 1 > Logging Formats > JSON preprocessing** and **Timestamps and date formats**.
Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#preprocessing, https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/

### Attribute precedence when processors set the same attribute
- **Last write wins**: Grok parser, Category, Arithmetic, String builder, Lookup, URL parser, User-Agent parser, GeoIP parser, Decoder.
- **Depends on `override_on_conflict`** (default `false` = existing target not overwritten): Attribute Remapper, Array Map processor.
- **First write wins**: Log status remapper, Service remapper, Log message remapper, Trace remapper, Span remapper (first in the pipeline; across pipelines the first encountered applies).
- Exception: **Log date remapper uses the last one** in order.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#attribute-precedence

### Grok parser: setup and UI
- Parses the full `message` (default) or a specific attribute. Add: expand pipeline > **Add... > Grok Parser** > name > **Define parsing rules**.
- **Log samples**: review pulled samples or **Add a new sample**: up to **10 samples, 5000 characters each** (UI). Datadog pulls samples from the **five highest-volume log patterns** matching the pipeline filter. (API `samples`: up to 5.)
- **Tap to Parse**: generates parsing rules that match your samples (does not consume AI Credits; not available on GovCloud sites).
- Preview parsing results per sample: **Match** (rule matches and extracts fields), **Match with a warning** (rule matches but extracts no fields), **No Match**.
- **Advanced Settings**: **Extract from** (parse a given text attribute instead of `message`, e.g. `command.line`) and **Helper Rules** (reusable tokens).
- API: `{"type":"grok-parser","source":"message","samples":[...],"grok":{"support_rules":"...","match_rules":"..."}}`; `support_rules` = helper rules, `match_rules` = parsing rules.
- Sources: https://docs.datadoghq.com/logs/log_configuration/processors/grok_parser/, https://docs.datadoghq.com/logs/log_configuration/parsing/#advanced-settings

### Grok syntax and rules
- Rule syntax: `RuleName %{MATCHER:EXTRACT:FILTER}`. Matcher = what to expect (`word`, `notSpace`, `number`...); Extract (optional) = attribute name; Filter (optional) = post-processing of the match. Omitting EXTRACT (e.g. `%{notSpace}`) matches text without storing it.
- Example: `MyParsingRule %{word:user} connected on %{date("MM/dd/yyyy"):date}`.
- Multiple rules in one parser: **only one matches** a given log, the **first match from top to bottom**; a rule can reference rules defined **above** it.
- Rule names: unique within the parser; only alphanumerics, `_` and `.`; must start with an alphanumeric.
- A rule must match the **entire** log entry (beginning to end). Use `\n` and `\s+` for newlines/whitespace. Null/empty properties are not displayed.
- Special characters such as `|`, `[`, `(` must be escaped (`\|`, `\[`).
- Best practices: put the sample log as a comment in the rule; build rules one attribute at a time with the **star trick** (`.*` at the end); prefer simple matchers (`notSpace`, `data`, `word`, `integer` cover most cases); remove the extract part to skip text you don't want as attributes.
- Troubleshooting a rule: compare against samples (timestamp format is a common culprit), then remove attributes one by one from the end with `.*` until it matches to find the culprit (e.g. `notSpace` used on a user agent containing spaces; fix with `regex("[^\"]*")`; `integer` used on a decimal value; fix with `number`).
- Patterns: alternating `(%{integer:user.id}|%{word:user.firstname})` = boolean OR; optional `(%{integer:user.id} )?` (no space after the first word before the optional group); helper rules: rule `MyParsingRule %{user} %{connection} %{server}` with helpers `user %{word:user.name} id:%{integer:user.id}` etc.
- Discard trailing text with `%{data:ignore}` or `.*`.
- Query-time parsing (Log Explorer calculated fields) supports only matchers `data`, `integer`, `notSpace`, `number`, `word` and filters `number`, `integer`. Everything else is ingest-time (Grok processor) only.
- Sources: https://docs.datadoghq.com/logs/log_configuration/parsing/, https://docs.datadoghq.com/logs/guide/log-parsing-best-practice/, https://docs.datadoghq.com/logs/faq/how-to-investigate-a-log-parsing-issue/

### Grok matchers and filters (reference)
- Matchers (both query and ingest time): `word` (`\b\w+\b`, letters/digits/underscore), `notSpace` (until next space), `number` (decimal float -> double), `integer` (-> integer), `data` (anything incl. spaces/newlines, `.*`).
- Ingest-only matchers: `date("pattern"[, "timezoneId"[, "localeId"]])`, `regex("pattern")`, `boolean("truePattern","falsePattern")` (default true/false, case-insensitive), `numberStr`, `numberExt`, `numberExtStr`, `integerStr`, `integerExt`, `integerExtStr` (Ext = scientific notation; Str = keep as string), `doubleQuotedString`, `singleQuotedString`, `quotedString`, `uuid`, `mac`, `ipv4`, `ipv6`, `ip`, `hostname`, `ipOrHost`, `port`.
- Filters (both): `number`, `integer`. Ingest-only filters: `boolean`, `nullIf("value")` (null if equal, e.g. `nullIf("-")`), `json`, `rubyhash`, `useragent([decodeuricomponent:true/false])`, `querystring`, `decodeuricomponent`, `lowercase`, `uppercase`, `keyvalue(...)`, `xml`, `csv(...)`, `scale(factor)`, `array(...)`, `url`.
- `keyvalue([separatorStr[, characterAllowList[, quotingStr[, delimiter]]]])`: separator default `=`; allow list adds non-escaped value chars beyond default `\\w.\\-_@` (e.g. `keyvalue("=","/:")` for URLs); quoting default `<>`, `""`, `''`; pair delimiter default space, `,` and `;` (e.g. `keyvalue("=", "", "", "|")`). Usage `%{data::keyvalue}` or `%{data::keyvalue(": ")}`. Empty (`key=`) and `null` values are not output; unmatched keyvalue on `data` returns `{}`.
- Dates: `date()` produces EPOCH **milliseconds**. Timezone param formats: `GMT`/`UTC`/`UT`/`Z`, `+hh:mm`/`-hhmm` (range -18:00..+18:00), `UTC+5`/`GMT-3` style, or TZ database IDs like `Europe/Paris`. Example `%{date("yyyy-MM-dd'T'HH:mm:ss.SSSZ"):date}`. **Parsing a date does not set the official log date**: add a Log Date Remapper afterwards.
- `json` filter: parse a JSON object after a text prefix, e.g. `... %{data::json}`.
- `xml`: `%{data::xml}`; tag with attribute and text -> `{"title":{"lang":"en","value":"..."}}`; repeated tags -> arrays.
- `csv(headers[, separator[, quotingcharacter]])`: default separator `,`, one char only, `tab` for TSV; default quote `"`; fewer values than headers -> fills the first ones; ints/doubles auto-cast. Example `%{data:user:csv("first_name,name,st_nb")}`.
- `array([[openCloseStr, ] separator][, subRuleOrFilter])`: e.g. `%{data:users:array("[]",",")}`, `array("{}","-", uppercase)`.
- ASCII control characters are serialized at ingestion; escape the serialized value in the rule.
- Sources: https://docs.datadoghq.com/logs/log_configuration/parsing/

### Remappers (reserved attributes)
- **Log date remapper** (`date-remapper`, `sources`): sets the official timestamp. Default date attributes (remapper page): `timestamp`, `date`, `_timestamp`, `Timestamp`, `eventTime`, `published_date`. Recognized formats ISO8601, UNIX ms, RFC3164; otherwise Grok-parse to epoch first. If several date remappers apply, the **last** one wins. Use cases: Akamai `reqTimeMillis`; Ruby timestamp inside message (after Grok).
- **Log status remapper** (`status-remapper`): value mapping in **Domain 1 > Log severity levels and Datadog status** (case-insensitive). **First** status remapper wins (within a pipeline and across all matching pipelines).
- **Service remapper** (`service-remapper`): first one wins. Use case Microsoft 365 `Workload`.
- **Log message remapper** (`message-remapper`, default source `msg`): several sources = fallback order (attribute1, else attribute2...). First one wins. Message shows in the Content column and is used for full-text search. Okta example: `displayMessage`.
- **Trace remapper** (`trace-id-remapper`, default `dd.trace_id`) and **Span remapper** (`span-id-remapper`, default `dd.span_id`): correlate logs with traces/spans when IDs are not auto-injected, typically after Grok parsing the ID from the message. Trace/span IDs are not displayed in log attributes in the UI. Alternative: SDK auto-injection.
- Sources: https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/service_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_message_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/trace_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/span_remapper/

### Attribute (generic) remapper
- Remaps source attributes **or tags** to a target attribute or tag, mainly to normalise to standard attributes. Cannot remap reserved attributes (`host` not at all; `message`, `service`, `status`, `date`, `trace_id`, `span_id` need their dedicated remappers). Casting, defaults (`preserve_source` false = source removed, `override_on_conflict` false = existing target kept, `target_format` auto) and the API payload: **Standard Attributes > Attribute Remapper processor**.
Sources: https://docs.datadoghq.com/logs/log_configuration/processors/remapper/

### Enrichment processors
- **Category processor** (`category-processor`, `categories[{filter:{query}, name}]`, `target`): adds an attribute whose value = name of the first matching category. Queries use Log Explorer search syntax on any attribute or tag (facet or not), wildcards allowed. **Stops at the first matching query**, so order matters. Category names unique. Often followed by a status remapper (e.g. map `http.status_code:5*` to `error`).
- **Arithmetic processor** (`arithmetic-processor`, `expression`, `target`, `is_replace_missing` default `false`): operators `+ - * /` and parentheses; put spaces around `-` (`(end-time - start-time) / 1000`); missing/non-numeric attribute -> calculation skipped unless **Replace missing attribute by 0**; existing target overwritten; results rounded to 9 decimals; use the Grok `scale` filter to scale units.
- **String builder** (`string-builder-processor`, `template`, `target`, `is_replace_missing` default `false`): template `Request %{http.method} %{http.url}`; objects can't be used (`%{http}` fails); arrays of values join with commas (`123,456,789`); `%{array_users.first_name}` -> `John,Jack`; missing attribute -> empty string or whole operation skipped; existing target overwritten; result max **256 characters**.
- **GeoIP parser** (`geo-ip-parser`): default source `network.client.ip`, default target `network.client.geoip`; continent, country, subdivision, city (`name`, `iso_code`/`code`).
- **URL parser** (`url-parser`): default source `http.url`, target `http.url_details` (host, path, port, queryString, scheme).
- **User-Agent parser** (`user-agent-parser`): default source `http.useragent`, target `http.useragent_details` (browser, device, os); `is_encoded` (default `false`) to URL-decode encoded user agents such as IIS logs.
- **Lookup processor** (`lookup-processor`, `source`, `target`, `lookup_table` ["key,value"], `default_lookup`): maps a source value to a human-readable value from a manual mapping table (enter `source_key,target_value` pairs or upload CSV on the Manual Mapping tab) or a **Reference Table** (Reference Table tab). Optional fallback value when not found. Mapping-table size limit **100Kb, shared across all Lookup Processors** on the platform; Reference Tables support larger files.
- **Reference Tables**: CSV with a primary key; manual upload or cloud storage (S3, Azure, GCS) up to **200 MB**; up to 200 columns, 500KiB per row, **100 tables per org**; auto-refresh every **5 minutes** for cloud storage, hourly for integrations, none for manual CSV; replacing via CSV upserts (updates, adds, deletes missing rows); permissions `reference_tables_read` / `reference_tables_write`; deleting a table stops Lookup enrichment (up to 10 min).
- **Threat Intel processor**: matches an IoC key (e.g. IP) against a threat-intel table and enriches matches.
- Sources: https://docs.datadoghq.com/logs/log_configuration/processors/category_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/arithmetic_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/string_builder_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/geoip_parser/, https://docs.datadoghq.com/logs/log_configuration/processors/url_parser/, https://docs.datadoghq.com/logs/log_configuration/processors/user_agent_parser/, https://docs.datadoghq.com/logs/log_configuration/processors/lookup_processor/, https://docs.datadoghq.com/reference_tables/

### Array, decoder, exclude attribute and OCSF processors
- **Array processor** (`array-processor`, `operation.type`): `select` (first element matching `filter`, read `value_to_extract`, e.g. headers `name:Referrer` -> `value`), `length` (element count), `append` (append attribute value to target array; creates array if missing; `preserve_source` default false), `key-value` (flatten `{key,value}` objects into attributes; target optional, root by default; `override_on_conflict` default false).
- **Array Map processor** (`array-map-processor`): applies sub-processors (Attribute Remapper, String Builder, Arithmetic, Category only) to each element of a source array, writing a target array; `$sourceElem` / `$targetElem`; all targets start with `$targetElem`; same source and target = in place; **only first 50 elements** processed; `preserve_source` default `true`.
- **Decoder processor**: decodes `base64` or `base16/hex` string fields; hex output can be string (UTF-8) or integer; handles truncated input by trimming/padding; on failure the log is left unchanged. Not available on app.ddog-gov.com.
- **Exclude Attribute processor** (`exclude-attribute`, `attribute_to_exclude`): removes an attribute during processing before indexes/archives/forwarding. Does **not** reduce ingestion cost (metering happens before processing). Cannot exclude reserved attributes (`host`, `source`, `service`, `status`, `message`, `timestamp`). Removes attributes only, not tags.
- **OCSF processor**: normalizes security logs to the Open Cybersecurity Schema Framework (Cloud SIEM use). Setup: a pipeline per log source, a nested (sub-)pipeline per OCSF target event class, pre-processing processors before the OCSF processor, select schema version/class/profile, map source attributes, configure ENUM attributes (e.g. `severity_id`).
- Sources: https://docs.datadoghq.com/logs/log_configuration/processors/array_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/array_map_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/decoder_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/exclude_attribute_processor/, https://docs.datadoghq.com/logs/log_configuration/processors/ocsf_processor/, https://docs.datadoghq.com/security/cloud_siem/ingest_and_enrich/open_cybersecurity_schema_framework/ocsf_processor/

### Pipeline Scanner
- Traces specific logs in real time to identify which pipelines and processors modified them; use to troubleshoot unparsed logs, missing tags, unexpected structure changes, conflicting or redundant rules, and compliance.
- Open from Log Explorer: open a log > **Pipeline Scanner** icon (hover text "View pipelines for similar logs"), or click an attribute > **Scan pipelines for**. Or Pipelines page > **Pipeline Scanner**.
- Refine the query (cannot be changed after the session starts) > **Launch this session**: for the next **15 minutes** matching logs are tagged with the pipelines/processors that modify them. Clicking a log pauses Live Tail; edit pipelines in the side panel (doesn't affect already processed logs), click Play to see new logs.
- Requires `logs_read_config` and `logs_write_pipelines`. Limits: **3 concurrent sessions**, **12 sessions per 12-hour sliding window**.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipeline_scanner/

### Auto-Processing and unparsed logs
- Auto-Processing (not on US5) parses custom application logs automatically, extracting core attributes (timestamp, status, trace ID, span ID). It only handles logs that **do not match any integration or custom pipeline filter**; a pipeline with filter `*` stops Auto-Processing for the whole org.
- One entry per source+service pair, created ~15 minutes after first logs if the pair has at least 1,000 indexed logs in 24 h; max **100 entries** per org. On by default for orgs created on or after Nov 4, 2026; off for older orgs. Toggle in the Auto-Processing tab of the Processing page; option to auto-enable or review new entries; **Switch to manual pipeline** creates a custom pipeline with the same filter/processors.
- Unparsed logs: Event Attributes panel shows no extracted attributes; query `datadog.pipelines:false` in Log Explorer for indexed logs without custom attributes after processing; create a log-based metric on that query and monitor it.
- Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#auto-processing, https://docs.datadoghq.com/logs/guide/detect-unparsed-logs/

## Standard Attributes

### Why a naming convention matters
- Centralising logs from many technologies produces tens or hundreds of attribute names for the same thing. A client IP may arrive as `clientIP`, `client_ip_address`, `remote_address`, `client.ip`; request execution time as `exec_time`, `request_latency`, `request.time_elapsed`.
- Datadog's answer: **attributes** + **aliasing** to unify the Logs environment.
- Attributes prescribe log **facets** and **tags**, which are what you filter and search on in the Log Explorer.
- Three ideas on the Attributes and Aliasing page:
  - **Reserved attributes**: automatically ingested.
  - **Standard attributes**: "the backbone of the naming convention for your organization". A default set ships with Datadog; the list can be customised (append, edit, delete) to create your team's naming convention.
  - **Aliasing**: used once a naming convention exists, or to build a single standard facet from multiple log sources. Example from docs: follow the clients most hit by latency on a hybrid Apache + Amazon CloudFront setup using the standard `Network Client IP` facet together with the standard `duration`. Aliasing implements a naming convention **without changing a team's technical stack**.
- Benefit summary (exam wording style): standard attributes make logs from different sources easy to search, filter, facet and correlate together (one facet, one dashboard query across teams/sources). Log integrations natively rely on the default standard attributes.
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/, https://docs.datadoghq.com/logs/explorer/facets/#alias-facets

### Reserved attributes
- Automatically ingested with logs. List on the Attributes and Aliasing page (6): `host`, `source`, `status`, `service`, `trace_id`, `message`.
  - `host`: originating host name as defined in metrics. Datadog retrieves the matching host's host tags and applies them to the logs. The Agent sets it automatically.
  - `source`: the integration name / technology the log came from (for example `nginx`, `postgresql`). When it matches an integration name, Datadog **automatically installs the corresponding parsers and facets** (integration pipeline).
  - `status`: level/severity. Used to define **patterns** and has a dedicated layout in the Log UI.
  - `service`: name of the application/service generating the log. Used to switch from Logs to APM, so use the same value in both products (unified service tagging: `env`, `service`, `version`).
  - `trace_id`: Trace ID used for traces; correlates a log with its trace.
  - `message`: by default the value of `message` is the log body; it is highlighted, shown in Live Tail, and **indexed for full-text search**.
- The Default Standard Attributes table also labels these as domain "Reserved" (and adds `device` for RUM only).
- `date` (official timestamp) and `span_id` are treated like reserved fields by the Attribute Remapper page: they cannot be remapped with the generic remapper.
- Search: reserved attributes need **no `@` prefix**: `service:web-app`, `status:error`, `host:i-1234567890abcdef0`. All other attributes need `@` (for example `@http.status_code:500`).
- Recommended: configure unified service tagging if you also collect traces/metrics.
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes, https://docs.datadoghq.com/standard-attributes/?product=log+management, https://docs.datadoghq.com/logs/explorer/search_syntax/#reserved-attributes

### How reserved attributes get their values (JSON preprocessing and dedicated remappers)
- JSON preprocessing runs **before** pipelines and maps well-known keys to reserved attributes (UI: Logs > Pipelines > **Preprocessing for JSON logs**; default lists in **Domain 1 > Logging Formats > JSON preprocessing**). Preprocessing is the **only** way to define a log attribute as `host`. Logs older than 18 h are rejected.
- For other source keys use the dedicated processor: Log Date Remapper, Log Message Remapper, Log Status Remapper, Service Remapper, Trace Remapper, Span Remapper.
- Order rules: status/service/message remapper: only the **first** one in pipeline order counts (status: first across all matching pipelines). Date remapper: the **last** one counts. Status value mapping: **Domain 1 > Log severity levels and Datadog status**.
- Syslog standard attributes are "generally remapped" to reserved ones: `syslog.appname` -> `service`, `syslog.severity` -> `status`, `syslog.timestamp` -> `date`.
Sources: https://docs.datadoghq.com/logs/log_configuration/pipelines/#preprocessing, https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/service_remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/log_message_remapper/

### Default standard attribute list (Log Management)
Functional domains and prefixes:
- **Network/communications** - prefix `network`: `network.client.ip` (IP of the client that initiated the inbound connection), `network.destination.ip`, `network.client.port`, `network.destination.port`, `network.bytes_read` (client -> server bytes), `network.bytes_written` (server -> client bytes).
- **Geolocation** - prefix `network.client.geoip` or `network.destination.geoip`: `.country.name`, `.country.iso_code` (for example `US`, `FR`), `.continent.code` (`EU`, `AS`, `NA`, `AF`, `AN`, `SA`, `OC`), `.continent.name`, `.subdivision.name` / `.subdivision.iso_code` (first subdivision level, for example California), `.city.name`. Produced by the **GeoIP Parser** (example: source `network.client.ip`, target `network.client.geoip`).
- **HTTP requests** - prefix `http`: `http.url`, `http.status_code`, `http.method`, `http.referer`, `http.request_id`, `http.useragent`, `http.version`. Typical integrations: Apache, Rails, AWS CloudFront, web app servers.
  - **URL details** - prefix `http.url_details` (generated by the **URL Parser**): `.host`, `.port`, `.path`, `.queryString` (object of query params), `.scheme`.
  - **User-Agent** - prefix `http.useragent_details` (generated by the **User-Agent Parser**): `.os.family`, `.browser.family`, `.device.family`.
- **Source code** - prefixes `logger` and `error`: `logger.name`, `logger.thread_name`, `logger.method_name`, `logger.version`, `error.kind`, `error.message`, `error.stack`. Typical: Java, Node.js, .NET, Golang, Python.
- **Database** - prefix `db`: `db.instance` (for example `customers` from a JDBC URL), `db.statement`, `db.user`, `db.operation` (for example `SELECT`, `findAndModify`, `HMSET`). Typical: Cassandra, MySQL, RDS, Elasticsearch.
- **Performance**: `duration` - a duration of any kind in **nanoseconds** (HTTP response time, DB query time, latency). Datadog recommends remapping any durations in logs to `duration` because it is displayed and used as a default **measure** for trace search.
- **User related** - prefix `usr` (not `user`): `usr.id`, `usr.name`, `usr.email`.
- **Syslog and log shippers** - prefix `syslog`: `syslog.hostname`, `syslog.appname`, `syslog.severity`, `syslog.timestamp`, `syslog.env`. Integrations: Rsyslog, NxLog, Syslog-ng, Fluentd, Logstash.
- **DNS** - prefix `dns`: `dns.id`, `dns.question.name|type|class|size`, `dns.answer.name|type|class|size`, `dns.flags.rcode`.
- **Events** - prefix `evt`: `evt.name` (shared name across events from the same activity, for example authentication), `evt.outcome` (for example `success`, `failure`).
- Full table: Docs > Default Standard Attributes, filter by product "Log Management". Same table covers RUM and APM attributes (several are shared with APM: `network.client.ip`, `http.url`, `http.status_code`, `db.*`, `error.*`).
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#default-standard-attribute-list, https://docs.datadoghq.com/standard-attributes/?product=log+management, https://docs.datadoghq.com/logs/log_configuration/processors/url_parser/, https://docs.datadoghq.com/logs/log_configuration/processors/user_agent_parser/, https://docs.datadoghq.com/logs/log_configuration/processors/geoip_parser/

### Stack trace attributes (dedicated UI display)
- When logging stack traces, these names get a dedicated display in the log side panel: `logger.name`, `logger.thread_name`, `error.stack` (actual stack trace), `error.message` (message contained in the stack trace), `error.kind` (type/kind of error, for example `Exception`, `OSError`).
- By default **integration pipelines** try to remap default logging-library parameters to these attributes and parse stack traces/tracebacks to extract `error.message` and `error.kind` automatically.
- For custom apps whose keys differ (for example `exception`, `trace`), remap them to these standard names.
Sources: https://docs.datadoghq.com/logs/log_collection/#attributes-for-stack-traces

### Creating and editing standard attributes (configuration page)
- **Admin users** curate the list. UI: Logs > Pipelines > **Standard Attributes** (app path `/logs/pipelines/standard-attributes`) > click **New Standard Attribute**.
- Fields:
  - **Path**: path as it appears in the JSON (for example `network.client.ip`).
  - **Type**: `string`, `integer`, `double`, `boolean` - used to **cast elements of the remapping list**.
  - **Description**: human-readable.
  - **Remapping list** (optional): comma-separated list of non-compliant attributes to remap (alias) to this standard attribute.
- You can append your own, and edit or delete existing (including default) standard attributes.
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#create-a-new-standard-attribute

### Aliasing rules
- Aliasing a source attribute to a destination (standard) attribute means logs carry **both** the source and the destination attributes.
- Users can query either the aliased (source) facet or the standard (destination) facet, but are encouraged to use the standard facet; this steers people to the naming convention and away from building saved views/dashboards on non-standard content.
- Rules (high exam value):
  - Aliasing happens **after** logs are processed by pipelines, so any extracted or processed attribute can be an alias source.
  - Datadog **enforces the type** of an aliased attribute; if the cast is not possible, aliasing is **skipped**.
  - If a log already carries the destination attribute, aliasing **overrides** that value.
  - If several source attributes are aliased to the same standard attribute and one log carries several of them, **only one** is aliased.
  - Updates/additions to standard attributes apply **only to newly ingested logs** (no backfill).
  - Standard attributes **cannot be aliased**.
  - Attributes can only be aliased **to standard attributes**.
  - JSON structure: one standard attribute cannot be the child of another (for example `user` and `user.name` cannot both be standard attributes).
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#aliasing

### Alias facets in the Log Explorer
- **Aliased facets** remain usable for slicing and dicing but are considered **deprecated** by the organisation. The *standard* facet more likely contains content from other teams too, which makes cross-source correlation easier.
- If you see an aliased facet, use the **switch to alias** menu item: it hides the aliased facet and unhides the standard facet. If that changes a saved view, save the saved view so the aliasing applies to everyone using it. Keep the aliased facet only when troubleshooting old content (from before the alias existed).
- **Aliasing facet to facet**: best when multiple teams **already created** multiple facets for similar content. Facet menu > **Alias to...** > pick the destination from the org's standard facets. Users can use either facet; they are nudged to the standard one.
- **Aliasing attribute to facet**: best when **onboarding logs from new sources**. Instead of creating a facet then immediately deprecating it, alias the field directly to an existing facet from the log side panel.
- Good practice: always consider using an existing facet before creating a new one.
Sources: https://docs.datadoghq.com/logs/explorer/facets/#aliased-facets, https://docs.datadoghq.com/logs/explorer/facets/#alias-facets

### Attribute Remapper processor
- Remaps one or more source attributes **or tags** to a target attribute **or tag**. Typical use: remap a custom attribute to a standard attribute (log format normalisation).
- Target name cannot contain `:` or `,` (plus the general attribute/tag naming constraints).
- If target is an attribute, the remapper can try to cast the value (UI: String, Integer, Double; decimal separator for Double must be `.`). If the cast fails, the **original value and type are preserved**.
- Cannot remap Datadog reserved attributes: `host` cannot be remapped at all (use JSON preprocessing); `message`, `service`, `status`, `date`, `trace_id`, `span_id` need their dedicated processors (Log Message Remapper, Service Remapper, Log Status Remapper, Log Date Remapper, Trace Remapper, Span Remapper).
- UI option "keep the source attribute" (API `preserve_source`): by default the source is **removed**.
- API payload (`type: attribute-remapper`):
```json
{
  "type": "attribute-remapper",
  "name": "Remap <SOURCE_ATTRIBUTE> to <TARGET_ATTRIBUTE>",
  "is_enabled": true,
  "source_type": "attribute",
  "sources": ["<SOURCE_ATTRIBUTE>"],
  "target": "<TARGET_ATTRIBUTE>",
  "target_type": "tag",
  "target_format": "integer",
  "preserve_source": false,
  "override_on_conflict": false
}
```
- Defaults: `is_enabled` false; `source_type` `attribute`; `target_type` `attribute`; `target_format` `auto` (no cast; values `auto`, `string`, `integer`); `preserve_source` **false** (source removed); `override_on_conflict` **false** (an already-set target is NOT overwritten). Required: `type`, `sources`, `target`.
- Example in docs: remap `user.firstname` to `user_name`, keeping the source -> log has both.
- Remapper vs aliasing: remapper runs inside a pipeline (order matters, can rename tags, can delete source); aliasing is configured on the standard attribute / facet, runs after all pipelines and keeps both attributes.
Sources: https://docs.datadoghq.com/logs/log_configuration/processors/remapper/, https://docs.datadoghq.com/logs/log_configuration/processors/

### Facets built on standard attributes
- Facets on **reserved attributes and most standard attributes are available by default** (for example `Host`, `Service`), one reason standard attributes make logs easy to search, filter and correlate across sources.
- Qualitative example on a standard attribute: top `network.client.geoip.country.iso_code` by 5xx. Measure example: `duration` in nanoseconds; scale service A (ms) by `*1000000` and service B (microseconds) by `*1000` with the Arithmetic Processor, then query `duration:>20ms` across both.
- Facet types, where facets are not needed, creation, limits (about 1000 facets), hiding and groups: **Domain 3 > Explorer Functionality > Facets** and **Managing facets**.
Sources: https://docs.datadoghq.com/logs/explorer/facets/

### Attributes vs tags
- Tags: `key:value` labels inherited from hosts and integrations; unified service tags `env`, `service`, `version`; searched without `@` (`env:prod`); tags without key searched with `tags:<MY_TAG>`. Tag strings must start with a letter; max 200 chars (general tagging page); metric/span tags are normalised to lowercase.
- Attributes: key/value pairs in the log content (JSON or extracted by parsing); searched with `@` (`@http.url_details.path:"/api/v1/test"`); attribute search is **case-sensitive**; log attributes are **not normalised** (unlike tags).
- Log limits: < 2048 attributes per log (JSON), keys < 50 chars, nesting < 20 levels, values < 1024 chars if promoted as facet; <= 100 tags per log, each tag <= 256 chars; null-valued attributes are not retained.
- Remapper can convert between them (`source_type`/`target_type` = `attribute` or `tag`).
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#attributes-search, https://docs.datadoghq.com/getting_started/tagging/#define-tags, https://docs.datadoghq.com/logs/log_collection/#limitations

### Common pitfalls
- `usr.*`, not `user.*`, is the standard user prefix.
- `duration` is in **nanoseconds**, not milliseconds; rescale with the Arithmetic Processor before/when remapping.
- Generic Attribute Remapper cannot target `host`, `service`, `status`, `message`, `date`, `trace_id`, `span_id`.
- Remapper defaults delete the source and do not overwrite an existing target; aliasing keeps the source but DOES override an existing destination value.
- Standard attribute / alias changes do not rewrite already-ingested logs.
- `user` and `user.name` cannot both be standard attributes.
- Reserved attributes searched without `@`; standard attributes still need `@` (`@network.client.ip`, `@http.status_code`, `@duration`).
Sources: https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/, https://docs.datadoghq.com/logs/log_configuration/processors/remapper/

# Domain 3: Log Searching & Filtering

## Live vs. Explorer

### The core difference
- Logging without Limits decouples ingestion from indexing: every ingested log is processed by pipelines, but only some are indexed (index filters, exclusion filters, daily quotas decide that).
- **Live Tail** = all ingested logs in near real time, from anywhere in your infrastructure. It shows **both indexed and non-indexed logs** (logs dropped by an index exclusion filter, logs that matched no index, logs over an index's daily quota). Logs in Live Tail are already **structured, processed and enriched by Log Pipelines** (not raw payloads).
- **Log Explorer** = search, filter, group (analytics/patterns), visualize and export **indexed logs** within each index's retention period. It can also include Flex Tier logs (toggle) and rehydrated historical views (Index facet).
- Docs summary on the Log Management overview: Live Tail "See your ingested logs in real time across all your environments"; Analytics "over your indexed logs"; Patterns "clustering your indexed logs".
- Live Tail has no stored history: the docs describe "no persistence beyond the 50 logs cached in browsers", and for broad queries the result "can be extremely sampled".

| | Live Tail | Log Explorer |
|---|---|---|
| Which logs | All ingested + processed logs (indexed and non-indexed) | Indexed logs (+ Flex logs if toggled, + historical views) |
| Exclusion filters / daily quota | Do not hide logs | Excluded / over-quota logs are not there |
| Time | Real time only (15-minute window) | Any time range within index retention |
| History / persistence | None (50 logs cached in the browser) | Retention set per index |
| Aggregations (Fields, Patterns, Transactions) | No | Yes, indexed logs only |
| Permission | `logs_live_tail` (global) | `logs_read_data` / legacy `logs_read_index_data` |

Sources: https://docs.datadoghq.com/logs/explorer/live_tail/, https://docs.datadoghq.com/logs/, https://docs.datadoghq.com/logs/guide/manage-sensitive-logs-data-access/

### Opening Live Tail and how it behaves
- UI path: **Logs > Log Explorer**, then choose the **Live Tail** option in the **time range selector** (time picker). Direct URL: `app.datadoghq.com/logs/livetail`.
- Uses the normal Log Search Syntax (`key:value`, `@attribute`, Boolean operators, `CIDR()`).
- **Sampling**: when too many matching logs flow in, the Live Tail output is **sampled for readability**. Sampling is **uniformly random**, so what you see is statistically representative of real throughput. To see **every** log, **scope the query down** with more search filters.
- **Pause / Play**: the Pipeline Scanner's Live Tail pauses when you click a log to inspect it; click **Play** to resume and see new logs (for example, after editing a processor). Edits do not change logs already processed.
- Live Tail window: logs are expected within a **15-minute** period of Live Tail's window. Logs whose timestamps are skewed (for example a host's local time not converted to UTC) can fall outside it and seem missing. Fix with a Date Remapper attribute that reflects UTC, or a Grok date matcher with a timezone.
- Full-text search syntax `*:search_term` **cannot be used in Live Tail** (nor in index filters, archive filters, pipeline filters, rehydration filters, log-based metric filters). Plain free text (`hello`) and `key:value` are fine.
- `CIDR()` works in Log Explorer, **Live Tail**, dashboard log widgets, log monitors and log configurations, e.g. `CIDR(@network.client.ip, 13.0.0.0/8)`.
- **Facets are not required** for Live Tail search (nor for Explorer search, processing, metric generation, archives, rehydration, index/exclusion filters). Autocomplete relies on facets, but any input matching incoming logs works. Hidden facets have no effect on Live Tail.

Sources: https://docs.datadoghq.com/logs/explorer/live_tail/, https://docs.datadoghq.com/logs/log_configuration/pipeline_scanner/, https://docs.datadoghq.com/logs/troubleshooting/live_tail/, https://docs.datadoghq.com/logs/explorer/search_syntax/, https://docs.datadoghq.com/logs/explorer/facets/

### When to use Live Tail
- Check that a process **started correctly** or that a **new deployment went smoothly**.
- Verify **new log collection** (Agent config, integration) without waiting for indexing, and regardless of indexes.
- Verify **pipeline / processor** changes: pipeline **preview** ("Preview pipeline changes") uses a live tail of your logs processed with your proposed changes, with filters **All logs / Impacted logs / Not impacted logs** and compare modes **Your changes / Entire pipeline**. When creating a pipeline you can select a log from the live tail preview to build the filter.
- **Pipeline Scanner**: launch a session (lasts **15 minutes**) and its Live Tail shows which pipelines match each log; limits 3 concurrent sessions, 12 sessions per 12-hour sliding window; needs `logs_read_config` and `logs_write_pipelines`.
- **Archives**: if an archive stays pending, check the archive inclusion filter query is valid and **matches log events in Live Tail**.
- Seeing logs that an exclusion filter removed from the index (they are "only excluded from indexing", still visible in Live Tail, archived, usable for log-based metrics).

Sources: https://docs.datadoghq.com/logs/explorer/live_tail/, https://docs.datadoghq.com/logs/log_configuration/pipelines/, https://docs.datadoghq.com/logs/log_configuration/pipeline_scanner/, https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/guide/getting-started-lwl/

### Index settings that make Live Tail and Explorer differ
- Live Tail shows logs after processing and before index routing, so anything an index decision removes is still in Live Tail but not in the Explorer: a log that matches **no index filter** (`datadog_index:N/A` in estimated usage metrics), a log dropped by an **exclusion filter** (they "still flow through the Livetail"), a log over the index's **daily quota**. Index, exclusion-filter, quota and retention rules: **Domain 4 > Filtering and Excluding**.
- Retention "determines how long logs are stored and searchable in Datadog" (Log Explorer).
- Troubleshooting "**Logs present in Live Tail, but missing from Logs Explorer**" (too-broad exclusion filters, index filter order, free text matching short strings in JSON, usage metrics by `datadog_index` / `datadog_is_excluded`, usage metrics ignore daily quotas): **Domain 6 > Ingestion Issues**.
- Pitfall: aggregations (Group into Fields/Patterns/Transactions) are for **indexed logs only**. For non-indexed logs: temporarily disable the exclusion filter ("switch off, switch on"), generate **log-based metrics**, or **rehydrate** from archives.
Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/, https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/explorer/analytics/

### Access and troubleshooting Live Tail
- Permission **`logs_live_tail`** ("Logs Live Tail"): grants Live Tail; it is **global** and grants access "regardless of Log Read Index Data permission". Listed as one of two **legacy** log permissions (with `logs_read_index_data`) superseded by the finer-grained `logs_read_data`; default role: **Datadog Read Only Role**.
- **Restriction queries still apply**: a user restricted to `service:api` with Live Tail permission only sees `service:api` logs in Live Tail (same for indexes). If a restriction query hides logs, the user sees no logs in Explorer or Live Tail.
- Live Tail page errors / no logs: try Incognito, another browser, ask teammates; check network/VPN/antivirus: allow inbound traffic from **`live.logs.datadoghq.com`** (`traceroute live.logs.datadoghq.com`; IP prefixes from `ip-ranges.datadoghq.com`); clear browser cache and DNS cache (`chrome://net-internals/#dns` > Clear host cache); disable ad blockers/extensions; check timestamps (15-minute window, UTC). Support ticket: browser/OS details, HAR file, console screenshot, recording.

Sources: https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/, https://docs.datadoghq.com/account_management/rbac/permissions/, https://docs.datadoghq.com/logs/troubleshooting/live_tail/

### Log Explorer search and time ranges
- A Log Explorer search = **a time range + a search query** (`key:value` + full-text). Time range selector is at the **top right**. Example: `service:payment status:error rejected` with `Past 15 minutes`. `key:value` search does not need a declared facet. Search bar features (highlighting, validation, autocomplete, raw mode, Natural Language Queries): **Explorer Functionality > Page layout and the search bar**.
- **Custom time frames** (typed in the time picker): queries run in **UTC**, but the time frame is selected in your **browser's time zone**.
  - **Sliding**: start and end move (`5h`, `3 mo`, `N{unit}`; units `m/min`, `h/hr`, `d/day`, `w/week`, `mo/month`).
  - **Growing**: fixed start, end = now (`since Jun 1`, `Jan 1 to now`, `from 5h`, `{date} - now`).
  - **Fixed**: frozen start and end (`Jan 1 - Jan 2`, `6:00 am - 1:00 pm`, Unix seconds or ms `1577883600 - 1578009540`).
  - **Calendar-aligned**: `today`, `yesterday`, `week to date` (from 12AM Monday), `month to date`, `year to date`, `this month`, `last week`/`previous week`, `2 weeks ago`.
  - Arrow keys `[↑]`/`[↓]` increment a highlighted part of the time frame.
- **Saved Views** store the query **with its time range**, but are meant for **live** time ranges (past hour, past week): fixed ranges are converted on save. Details: **Explorer Functionality > Saved views and the default view**.
- **List** sort default: timestamp, most recent first (fastest). Timeseries split by up to 3 facets.
- **View in context** (log lines just before and after a log, even if they don't match the filter) and the **Metrics** tab (30-minute window around the log): **Explorer Functionality > Log side panel**.
Sources: https://docs.datadoghq.com/logs/explorer/search/, https://docs.datadoghq.com/dashboards/guide/custom_time_frames/, https://docs.datadoghq.com/logs/explorer/saved_views/, https://docs.datadoghq.com/logs/explorer/visualize/, https://docs.datadoghq.com/logs/explorer/side_panel/

### Beyond index retention: Flex logs, historical views, Archive Search
- **Index facet**: appears only with multiple indexes and/or active historical views; scope a query to a subset of indexes. Rehydrated **historical indexes** are selected from the Index facet in the index selector.
- **Flex Logs**: configured per index; in the Log Explorer, toggle **Include Flex Logs** (next to the time picker). No monitors, no Watchdog; dashboards ok. Tiers, sizes and retention: **Domain 1 > Flex Logs**.
- **Archive Search** (Logs > Archive Search > New Search): query archives directly **without rehydrating**; up to **100,000 logs retained for 24 hours**; no aggregations. Example use: logs from 3 weeks ago when retention is 15 days. Modes, permissions and limits: **Domain 5 > Exporting > Archive Search**.
- **Rehydration (historical views)**: up to 1 billion events per view; index exclusion filters do not apply; default retention 15 days; scan size depends on time range, not the query. Archive Search is now the recommended way to access archived logs.
Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/logs/explorer/archive_search/, https://docs.datadoghq.com/logs/log_configuration/rehydrating/

### Common pitfalls
- "Logs are in Live Tail but not in the Explorer" almost always means index routing: exclusion filter, index filter order/no matching index, or daily quota reached. It is not a collection problem (Live Tail proves the log was ingested and processed).
- Live Tail is not a historical search tool: you cannot pick a past time range in it, and nothing is stored.
- Broad Live Tail queries are sampled: narrow the query, do not assume missing logs.
- `*:term` full-text search fails in Live Tail; use `key:value` or free text.
- Explorer analytics never include excluded logs; use log-based metrics (computed on all ingested logs) for KPIs on excluded logs.
- Logs older than index retention are not in the Explorer: use Flex (if configured), Archive Search, or rehydration.

Sources: https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/explorer/live_tail/, https://docs.datadoghq.com/logs/explorer/analytics/

## Search Syntax

### Query anatomy: terms and Boolean operators
- A Log Explorer search = a **time range** (selector at the top right, e.g. `Past 15 minutes`) + a **search query** that mixes `key:value` filters and free/full-text terms. Example: `service:payment status:error rejected` over `Past 15 minutes`.
- Two kinds of terms:
  - **Single term**: one word, e.g. `test`, `hello`.
  - **Sequence**: words in straight double quotes, e.g. `"hello world"` (exact phrase). Use straight quotes (`"`); search ignores curly quotes (“ ”) that chat apps/editors insert, so “hello world” matches logs containing `hello` and `world` in any order (not as a sequence).
- Boolean operators are **case-sensitive** (write them uppercase):
  | Operator | Meaning | Example |
  |---|---|---|
  | `AND` | Intersection; **default when no operator is given** (implicit AND) | `authentication AND failure` |
  | `OR` | Union | `authentication OR password` |
  | `-` | Exclusion; applies to each individual raw text search | `authentication AND -password` |
- `NOT` also appears in docs examples (`env:production NOT service:background-worker`, `NOT(CIDR(...))`), but the operator table on the search syntax page lists only `AND`, `OR`, `-`.
- Grouping with parentheses: `(env:prod AND -version:beta)`; value lists on one key: `env:(prod OR test)`, `service:(web-store OR auth-dotnet)`.
- Pitfall: a log has a single value for `service`/`source`, so `service:(checkout AND payments)` returns nothing; use `OR` to get either.
- Event-based syntax (Logs, APM, RUM, Events, Security, CI...) is not interchangeable with metric-based syntax (Metrics, CCM uses `{tag:value}`, `!`, `&&`, `||`).
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/, https://docs.datadoghq.com/logs/explorer/search/, https://docs.datadoghq.com/getting_started/search/, https://docs.datadoghq.com/getting_started/search/product_specific_reference/

### Free-text vs full-text search
- **Free text** (no prefix), e.g. `hello`: searches only `message`, `@title`, `@error.message` and `@error.stack` (the `content` column in Log Explorer).
- **Full text**, syntax `*:search_term`: searches **all log attributes, including the message**.
  | Query | Type | Matches |
  |---|---|---|
  | `*:hello` | Full-text | exact string `hello` in any attribute |
  | `*:hello*` | Full-text | any attribute value starting with `hello` (e.g. `hello_world`) |
  | `*:"hello world"` | Full-text | exact string `hello world` in any attribute |
  | `hello` | Free text | `hello` in message/title/error fields |
  | `hello world` | Free text | both words anywhere in the message (e.g. `hello beautiful world`) |
- Full-text search is **only in Log Management**; works in **monitor, dashboard and notebook** queries. It **cannot** be used in: index filters, archive filters, log pipeline filters, rehydration filters, log-based metric filters, or **Live Tail**.
- Full-text search gives case-insensitive results (the documented workaround for case-sensitive attribute search). Free-text matching is also not case-sensitive: `hello` matches `Hello, world!`.
- The `message` reserved attribute is the log body, displayed in Live Tail and indexed for full-text search.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#full-text-search, https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes

### How free-text search splits words
- Free-text search matches **whole words**. Message and query are split by Unicode word-boundary rules; spaces and most punctuation separate words and are not searchable. `hello` matches `Hello, world!`; `"hello world"` matches `hello-world`. Same rules for `*:` searches.
  | Pattern | Example | Words |
  |---|---|---|
  | letter.letter | `my.friend` | `my.friend` (one word) |
  | period + space | `my. friend` | `my`, `friend` |
  | letter.number | `version.2` | `version`, `2` |
  | number.letter | `5.star` | `5`, `star` |
  | number.number | `192.168.1.1` | one word |
  | number,number | `3,456` | one word |
  | letter:letter | `metric:cpu` | one word |
  | letter:number | `RequestId:5` | `RequestId`, `5` |
  | apostrophe | `don't` | one word |
  | underscore | `hello_world` | one word |
  | hyphen | `hello-world` | `hello`, `world` |
- Pitfall: `friend` does NOT match `my.friend`; use `*friend`.
- Straight `'` and curly apostrophes differ: `don't` (straight) does not match `don’t` (curly); use `don*` to match both.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#how-free-text-search-splits-words

### Attribute search, reserved attributes and tags
- Attributes need the `@` prefix: `@url:www.datadoghq.com`, `@http.url_details.path:"/api/v1/test"`.
- **Reserved attributes** need no `@`: `host`, `source`, `status`, `service`, `trace_id`, `message` (e.g. `service:web-app`, `status:error`, `host:i-1234567890abcdef0`).
- **Tags** (inherited from hosts and integrations) use `key:value` without `@`: `env:prod`, `env:(prod OR test)`. A bare word like `test` is a free-text search for the string, not a tag. Tags not in `key:value` form: search with `tags:<MY_TAG>`.
- **No facet is required** to search on attributes or tags (`key:value` queries don't need a declared facet). Facets help autocomplete and analytics.
- Attribute searches are **case-sensitive**. For case-insensitive results use full-text search, or apply the Grok `lowercase` filter at parse time.
- Existence/absence: `-@http.status_code:*` returns logs that do NOT have the `http.status_code` attribute.
- Calculated fields are referenced with the `#` prefix (e.g. `#request_duration:>1000`); they are query-time, user-scoped, temporary, max 5 at a time.
- `status` values (official log statuses, Syslog severities): `emerg` (0), `alert` (1), `critical` (2), `error` (3), `warning` (4), `notice` (5), `info` (6), `debug` (7), plus `OK`. Status remapper maps strings by prefix (e.g. `f...` -> emerg, `w...` -> warning, `i...` -> info; unknown -> info). Status is color-coded in the search bar (red for `error`, blue for `info`).
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#attributes-search, https://docs.datadoghq.com/logs/explorer/search_syntax/#tags, https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#reserved-attributes, https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/, https://docs.datadoghq.com/logs/explorer/calculated_fields/

### Escaping special characters and spaces
- Special characters that must be escaped with `\`: `-` `!` `&&` `||` `>` `>=` `<` `<=` `(` `)` `{` `}` `[` `]` `"` `*` `?` `:` `\` `#` and spaces.
- `/` is NOT special (no escaping needed). `@` cannot be used in Log Explorer queries except as the attribute prefix.
- Value with special characters: escape or double-quote it. `hello:world` -> `@my_attribute:hello\:world` or `@my_attribute:"hello:world"`.
- `@http.url:/api\-v1/*` = `http.url` starts with `/api-v1/` (hyphen escaped, slash not).
- Special characters inside the log **message** are not searchable: parse them into an attribute with a Grok Parser and search that attribute.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#escape-special-characters-and-spaces

### Wildcards
- Docs framing (current): wildcards work in free-text search, which searches the log message (the `content` column); to search log attributes with wildcards, use full-text search (`*:hello*`) or a keyed value such as `service:*mongo`.
- `*` = any number of characters (including zero). In the message, `*` matches within a **single word**: `web*` (web, webserver), `*web` (myweb), `*web*` (mywebserver).
- A single `*` doesn't cross words: `waiting*time` does NOT match `waiting until next renew time`. To span words:
  - `**` (double wildcard) matches anything including spaces/punctuation: `waiting**time`.
  - Escaped space `\ ` matches consecutive words, each may have wildcards: `waiting\ un*`.
- Wildcards only work outside double quotes; `"*test*"` searches the word `test`.
- Wildcards on tags/attributes (faceted or not): `service:*mongo`. Without a prefix, `*NETWORK*` searches only the message.
- `?` matches a single special character or space in an attribute/tag value: `@my_attribute:hello?world` matches `hello world`.
- Performance: single-word searches without wildcards/quotes are fastest; combine wildcard/quoted searches with selective filters like `service` or `host`.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#wildcards

### Numerical values, ranges and measures
- Numeric search: the docs say to first **add the attribute as a facet** (measure, or integer-type dimension). Then use `<`, `>`, `<=`, `>=`: `@http.response_time:>100`.
- Ranges: `@http.status_code:[400 TO 499]` (all 4xx).
- Dimensions can be string or integer type; **integer type enables range filtering** (`http.status_code:[200 TO 299]`).
- Measures: (long) integer or double; units TIME (nanosecond...week) or BYTES (bit...exbibyte). Unit is a property of the **measure, not the field**: normalize values (e.g. Arithmetic Processor) to the measure's unit, then query with units, e.g. `duration:>20ms`.
- In the facet panel, measures show a min/max slider to scope ranges.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#numerical-values, https://docs.datadoghq.com/logs/explorer/facets/

### CIDR search
- `CIDR(<attribute>, <block>[, <block>...])`: `CIDR(@network.client.ip,13.0.0.0/8)`; multiple blocks and array attributes: `CIDR(@network.ip.list,13.0.0.0/8, 15.0.0.0/8)` (any IP in the array).
- Negate with `NOT(...)`: `source:vpc NOT(CIDR(@network.client.ip, 13.0.0.0/8)) CIDR(@network.destination.ip, 15.0.0.0/8)`.
- Supports IPv4 and IPv6; works in Log Explorer, Live Tail, dashboard log widgets, log monitors and log configurations.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#search-using-cidr-notation

### Arrays
- Facet value `Peter` on `users.names` returns logs where the value is `Peter` or an array containing `Peter`. Works on non-faceted arrays too.
- Arrays of JSON objects can't be faceted but can be searched: `@Event.EventData.Data.Name:ObjectServer`. (To facet, extract with a Grok parser first.)
- Nested array field: `@network.ip.attributes.ip:2a02\:1810*` matches if any item matches.
- `@user_perms:(4 6)` = array contains both 4 and 6; `@user_perms:[2 TO 6]` = at least one value in 2..6.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/#arrays, https://docs.datadoghq.com/logs/explorer/facets/#create-facets

### Search bar features (autocomplete, highlighting, raw mode, NLQ)
- Syntax highlighting, error validation ("Missing closing parenthesis character"), autocomplete (values by **descending log count over the past 15 minutes**, **100 most recent searches**, matching Saved Views), the **raw mode** toggle and Natural Language Queries (**Ask**; disabling needs `org_management`; not on gov sites): **Explorer Functionality > Page layout and the search bar**.
- Hidden facets are removed from autocomplete but remain valid in queries.
Sources: https://docs.datadoghq.com/logs/explorer/search/, https://docs.datadoghq.com/logs/explorer/facets/#hide-facets

### Advanced search (subqueries, Reference Tables)
- **+ Add** > Logs: subquery filter with `IN`/`NOT IN` on a correlating attribute; values matched default `1000`, max `1,000,000` (top or bottom).
- Example: drop orders that later succeeded = main `status:error`, subquery `status:success`, `NOT IN` on order ID.
- **Add** > Join with Reference Table: IN/NOT IN; tables over 1,000,000 rows can't filter.
Sources: https://docs.datadoghq.com/logs/explorer/advanced_search/

## Explorer Functionality

The Log Explorer (Logs > Explorer, `app.datadoghq.com/logs`) is the home base for log troubleshooting. You can arrive from scratch, from a Saved View, or from another context (monitor notification, dashboard widget). In it you **search and filter**, **analyze** (group into Fields, Patterns, Transactions), **visualize** (List, Timeseries, Top List, Table, Pie, Tree Map) and **export** (Saved View, dashboard/notebook widget, monitor, metric, cURL, CSV, Share View).

### Page layout and the search bar

- A search = **time range** (time selector, top right) + **search query** (`key:value` plus full-text). Example: `service:payment status:error rejected` with time range `Past 15 minutes`.
- `key:value` queries do **not** need a facet declared first (Search Logs page; Search Syntax page also says "It is not required to define a facet to search on attributes and tags").
- Indexed logs support both full-text and `key:value` search.
- Search bar features:
  - **Syntax highlighting**: keys, values, free text and control characters (parentheses) are colored differently; `status` values are color-coded (red `error`, blue `info`).
  - **Error validation**: flags missing values in `key:value`, incomplete range queries, unclosed parentheses (e.g. "Missing closing parenthesis character").
  - **Autocomplete**: facets suggested in the order they appear in the facet panel; after `facet:` the values appear in **descending order of log count from the past 15 minutes**. Your **100 most recent searches** are retained and suggested. Matching **Saved Views** are suggested too (same order as the Saved Views panel).
  - **Raw mode**: toggle to the right of the search bar removes syntax highlighting, search-pill styling and autocomplete.
  - Keyboard: `CMD-A`, `CMD-C`, `CMD-X`, `CMD-V` work in the search bar.
- **Natural Language Queries (NLQ)**: click **Ask** in the search field and type plain English ("Top 20 services by errors"). Disabling NLQ needs `org_management` permission: Organization Settings > Preferences > toggle off Natural Language Queries. Not available on the government sites `app.ddog-gov.com` and `us2.ddog-gov.com`.
- Time range: picker top right; custom syntax per Custom Time Frames guide (sliding `5h`, growing `since Jun 1` / `Jan 1 to now`, fixed `Jan 1 - Jan 2`, calendar-aligned `today`, `week to date`, `last month`). Queries run in UTC but the time frame is chosen in the **browser's time zone**. Highlight part of the time frame and use up/down arrow keys to increment.

Sources: https://docs.datadoghq.com/logs/explorer/, https://docs.datadoghq.com/logs/explorer/search/, https://docs.datadoghq.com/logs/explorer/search_syntax/, https://docs.datadoghq.com/dashboards/guide/custom_time_frames/

### Facets: concepts and types

- Facets = user-defined tags and attributes from **indexed** logs, for qualitative or quantitative analysis. Used to search, define log patterns, perform log analytics, and in log monitors, dashboard log widgets and notebooks.
- Facets are **NOT needed** for: log processing, Live Tail search, Log Explorer search, generating metrics from logs, archive forwarding, rehydration, routing logs to pipelines and indexes with filters, or exclusion filters/sampling. Autocomplete in those contexts relies on facets, but any input matching incoming logs works.
- **Qualitative facets = dimensions** ("Facets"). Use them to get relative insights (top values), **count unique values**, and frequently **filter**. Type: **string** or **numerical (integer)**. Integer type adds **range filtering**: `http.status_code:[200 TO 299]`.
- **Quantitative facets = measures**. Use them to **aggregate** values (avg, sum...), **range filter** (`duration:>20ms`), and **sort logs** by value. Type: **(long) integer** or **double**.
- **Measure units**: only two families:
  - BYTES: bit, byte, kibibyte, mebibyte, gibibyte, tebibyte, pebibyte, exbibyte
  - TIME: nanosecond, microsecond, millisecond, second, minute, hour, day, week
- **Unit is a property of the measure, not the field.** If `service:A` logs `duration` in ms and `service:B` in µs while the measure is in ns: scale with the **Arithmetic Processor** (`*1000000` for A, `*1000` for B), then `duration:>20ms` works consistently across both.
- Facet panel display: **facets** show a top list of unique values with log counts (click a value to toggle only-this-value vs all; checkboxes add/remove a single value; you can search within values). **Measures** show a **slider** with min/max; drag it or type bounds.
- Search syntax note: the Search Syntax page states "To search on a numerical attribute, first add it as a facet" before using `<`, `>`, `<=`, `>=`.

Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/explorer/search_syntax/#numerical-values

### Managing facets

- **Out-of-the-box facets**: common ones like `Host` and `Service`; facets on Reserved Attributes and most Standard Attributes exist by default.
- **Index facet**: appears only if the org has **multiple indexes** and/or **active historical views** (rehydrations). Use it to scope a query to a subset of indexes.
- **Creating facets** (permission `logs_write_facets` = "Logs Write Facets": create, edit and delete log facets; global permission; Datadog Standard Role has it. `facets_write` is for non-log products):
  - Good practice: reuse an existing facet before creating a new one.
  - **A new facet is populated only for logs that arrive after it is created** (not retroactive).
  - Recommended maximum: **1000 facets**.
  - **From the log side panel** (easiest, details pre-filled): open a log, click the field (tag or attribute), create facet. **String value -> only "facet" creation offered. Numerical value -> both facet and measure offered.**
  - **From the facet list**: **+ Add** (add facet) button at top of facet panel, when no matching log is at hand. Field name: **tag key name for tags**, **attribute path with `@` prefix for attributes** (e.g. `@http.url_details.path`). Autocomplete helps, but any value can be entered even if no matching logs flow yet.
  - Array of JSON objects: you cannot facet it directly; extract the attribute with a **Grok parser** first, then create the facet.
- **Hide facets**: cog icon next to the facet > **Hide Facet**. Hidden facets:
  - remain visible in the facet search box (unhide from there);
  - are hidden from search-bar autocomplete and from analytics dropdowns (measure, group-by) in the Log Explorer;
  - are still **valid in search queries** (e.g. a pasted link);
  - have **no impact outside the Log Explorer** (Live Tail, monitors, dashboard widgets);
  - are **personal**: do not affect teammates unless you **update a Saved View** (hidden facets are part of a saved view's context).
- **Group facets**: cog > **Edit facet** > expand **Advanced options** > **Group** field > **Update**. Only affects display in the facet list; no impact on search/analytics.
- **Filter facets**: the search box on the facet panel matches **both the display name and the field name**.
- **Alias facets** (facet -> standard facet, or attribute -> facet): cog menu **Alias to...**; pick a standard facet. Aliased facets still work but are considered deprecated; users are nudged to the standard facet. In the facet list, **switch to alias** hides the aliased facet and unhides the standard one; save the saved view so everyone gets it. Keep the aliased facet for content older than the aliasing. Aliasing facets/standard attributes requires `logs_write_pipelines`.
- **Delete a facet**: click **Showing xx of xx** at top of facet panel > search the facet > **pencil icon** > **Delete**. Warning: deleting a facet used in **indexes, monitors, dashboards, restriction queries**, or by other teams can break those configurations.

Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/, https://docs.datadoghq.com/account_management/rbac/permissions/

### List view (log stream) and display options

- Lists are **paginated** results of individual logs or aggregates.
- Columns (list of logs):
  - **Table header row** (first row interactions): preferred way to **sort, rearrange (drag and drop) or remove** columns.
  - **Facet panel** (left) or **log side panel** (right): preferred way to **add** a column for a field. In the side panel JSON, click an attribute > add/remove column.
- **Options** button: controls **Content Height** and **Content Display** per log in the table.
- **Default sort = timestamp, most recent on top** - fastest, recommended. You can also sort by a measure (lowest/highest first) or lexicographically by a facet value.
- Any attribute or tag can be a column, but **sorting is reliable only for declared facets**; non-faceted columns do not sort reliably.
- The **log table configuration is stored in Saved Views**.
- List of aggregates: Patterns sorted by count of matching events (descending by default); Transactions sorted by transaction id lexicographically (ascending by default).
- Calculated fields automatically get a column in List view.

Sources: https://docs.datadoghq.com/logs/explorer/visualize/#lists

### Log side panel

- Click a log to open it. Layout: **upper part = context** (infrastructure/application context from tags: host, container name, file name, serverless function, custom tags like team/env/version added by Agent or forwarder); **lower part = content** (message plus structured attributes extracted/enriched by pipelines).
- Some standard attributes (`error.stack`, `http.method`, `duration`) get enhanced displays; remap your attributes to standard names to benefit.
- **View in context** button: rewrites the search to show log lines **just before and after** the selected log, **even if they don't match the current filter**. Context uses `Hostname`, `Service`, `filename`, `container_id` attributes plus tags.
- **Metrics** tab: underlying infrastructure metrics over a **30-minute window around the log**.
- **Host** section: links to the host dashboard or Network Analytics; **Container** section links to the container page. Serverless logs show a **Serverless** section instead of Host.
- **Trace** tab (needs trace ID injection in logs + Unified Service Tagging): see the log within its full trace; **View Trace Details** opens APM. The trace ID is displayed in the side panel and can be used to filter logs. If the trace was sampled out/not retained, the side panel says the trace is missing; traces and logs are sampled independently, so this is **not a configuration error**. The Service section highlights the part of the trace for that service.
- JSON attribute interactions: add/remove column; append search with include/exclude of the value; build/edit a **facet or measure**; build/edit a **calculated field** ("Create calculated from...").
- **Share** button: **Copy to clipboard** (or `Ctrl+C`/`Cmd+C`) copies the **log JSON**; **Share Event** shares the log plus the underlying view via email, Slack and other notification integrations.
- **Save to notebook** in the side panel: the log is shown in a reader-friendly format in the notebook and stays there even after the log ages out of retention.
- Tap to Parse (Preview): **Tap** button next to the copy button (or highlight text > Tap) generates an extraction rule for a calculated field.

Sources: https://docs.datadoghq.com/logs/explorer/side_panel/, https://docs.datadoghq.com/logs/guide/correlate-logs-with-metrics/, https://docs.datadoghq.com/logs/explorer/export/

### Saved views and the default view

- Access Saved Views in the **upper left** of the Log Explorer (Views panel).
- A saved view keeps: the **search query with its time range** (live ranges like past hour; **fixed ranges are converted to live ranges on save**), the **default visualization** (log stream, patterns or analytics with their properties), and the **selected subset of facets** shown in the facet list. Search Syntax page summary: query, columns, time horizon, facets. Hidden facets and column layout are part of it.
- **Default view** = your existing Log Explorer view. **Only you** see it; updating it does not affect the org. It can be **temporarily overridden** by any UI action or by opening a link that embeds a different configuration. From the default view entry: **reload**, **update** with current parameters, **reset** to Datadog's defaults.
- All other saved views are **shared across the organization**:
  - **Integration saved views**: out of the box with most log integrations, **read-only**, identified by the integration logo.
  - **Custom saved views**: created by users with the **Save** button; editable by any user **except Read Only users**; identified by the creator's avatar.
- Actions on a saved view: load/reload, update with current config, rename, delete, **share through a short-link**, **star** (favorite: appears on top of the list and is accessible from the **navigation menu**). Update/rename/delete are disabled for integration saved views and for Read Only users.
- Permission: `saved_views_write` (Modify Saved Views across all Datadog products, Datadog Standard Role).

Sources: https://docs.datadoghq.com/logs/explorer/saved_views/, https://docs.datadoghq.com/account_management/rbac/permissions/

### Sharing, permalinks and export entry points
- Export/save options (Saved View, Dashboard or Notebook widget, Monitor, Metric, cURL, CSV, Share View), CSV limits (**100,000** logs, **300** patterns, **500** transactions) and CSV sanitizing: **Domain 5 > Exporting > Log Explorer Export menu**. The Logs API returns max 1000 logs per call; use pagination for more.
- Share a single log: side panel **Share** > Copy to clipboard (JSON) or Share Event.
- Share a saved view: short-link from the saved view entry.
- Share a Watchdog outlier: open it, click **Copy Link**; the link **expires with the retention of the underlying data** (e.g. 15-day logs -> link dies after 15 days).
- Time in URLs (Custom Time Frames guide, dashboard example): `from_ts`/`to_ts` are Unix **millisecond** timestamps; `live=true` keeps relative time when saved or shared.
Sources: https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/watchdog/insights/#share-an-outlier, https://docs.datadoghq.com/dashboards/guide/custom_time_frames/#urls

### Calculated fields

- Transform/enrich logs at **query time**; behave like attributes for search, aggregation, visualization and defining other calculated fields.
- Two types: **Formulas** and **Extractions** (Extractions are in Preview).
- Shared properties: **temporary** (do not persist beyond your Log Explorer session), **user-scoped** (visible only to you), good for **retroactive analysis of already indexed logs**, referenced with the **`#` prefix**, **up to five** at a time.
- When to use: short-term investigations; retroactive analysis (pipeline changes only affect logs ingested after the change); no permission/expertise to change pipelines; private experimentation. If it proves valuable long term, move the logic into a **log pipeline**.
- Create: **Add** button next to the search bar > **Calculated field**; or open a log > select a JSON attribute > **Create calculated from...** (best for extractions because you get a real sample).
- After creation: a **header row** under the search bar lists active calculated fields (hover for definition; edit, filter by, group by); **List** view gets a column automatically; the side panel groups them in a dedicated section.
- Formula syntax: tag/reserved attribute with no prefix (escape dashes: `ci\-job\-id`), attribute `@attr`, calculated field `#field`, strings in double quotes, numbers plain. Example: `#latency_gap = @client_latency - @server_latency`.
- Operator precedence: `()` > `!`/`NOT`/`-` > `^`, `%` > `*`, `/` > `+`, `-` > `<`, `<=`, `>`, `>=` > `==`, `!=` > `&&`/`AND` > `||`/`OR`.
- Functions: arithmetic `abs`, `ceil`, `floor`, `max`, `min`, `round(value, precision)`; string `concat`, `lower`, `upper`, `left`, `right`, `substring`, `proper`, `split_before`, `split_after`, `textjoin`; logical `if(cond, a, b)`, `is_null`; regex `regexp_like`, `regexp_replace` (double backslashes in formula strings, e.g. `"\\d"`).
- Extractions: Grok (`%{word:first}`) or regex with **named** capture groups `(?<name>...)` (names letters+digits only, start with a letter). Query-time Grok supports only `data`, `integer`, `notSpace`, `number`, `word` matchers and `number`/`integer` filters. Regex extractions are always strings. Extractions run **before** formulas (a formula can use an extracted field, not vice versa).

Sources: https://docs.datadoghq.com/logs/explorer/calculated_fields/, https://docs.datadoghq.com/logs/explorer/calculated_fields/formulas/, https://docs.datadoghq.com/logs/explorer/calculated_fields/extractions/, https://docs.datadoghq.com/logs/explorer/search_syntax/#calculated-fields

### Watchdog Insights in the Log Explorer

- A **Watchdog Insights banner/carousel** near the top of the Log Explorer shows insights **for the current query**. Expand for an overview; **View all** opens the full side panel. Highest-priority insights (by insight type, state, status, start time, anomaly type) are on the left.
- Insights come from data that includes the `service` tag. Two Log Management insight types:
  - **Log Anomaly Detection**: ingested logs analyzed at intake; Watchdog aggregates on detected **patterns** plus `environment`, `service`, `source`, `status`; flags **emergence** or **sudden increase** of warning/error logs. Shown matching the search context and your role's restrictions. Click an insight for the description and contributing patterns. **Severe** anomalies (contain error logs, last **at least 10 minutes**, significant increase) also appear in the **Watchdog alerts feed** and can be alerted on with a **Watchdog logs monitor**.
  - **Error Outliers**: faceted tags/attributes that are **statistically overrepresented among errors** matching the query (e.g. `env:staging`, `docker_image:acme:3.1`, `http.useragent_details.browser.family:curl`). Banner card: field name + proportion of errors vs overall logs it accounts for. Side panel card: main log pattern. Full side panel: timeseries of error logs with the field, associated tags, list of log patterns.
- General: Anomalies are precalculated Watchdog alerts matching the query; Outliers are calculated dynamically on the query and time frame.
- **Filter on Insight** (inverted triangle icon, hover top right of a card): rescopes the view to the insight; a filtered outlier disappears because it becomes the baseline.

Sources: https://docs.datadoghq.com/logs/explorer/watchdog_insights/, https://docs.datadoghq.com/watchdog/insights/

### Group into Patterns / Transactions entry points
- In the query editor, **Group into**: **Fields**, **Patterns**, **Transactions**. Aggregations work on **indexed logs only**.
- **Patterns**: cluster on `message`, grouped by **Status** and **Service** by default, from **10,000 log samples**; the pattern side panel can kickstart a **Grok parsing rule** and **Add Exclusion Filter** (stop indexing a noisy pattern); the **Pattern Inspector** highlights variable values in yellow.
- **Transactions**: group logs by a common attribute (e.g. `requestId`); Duration and Max Severity are added automatically; results include all logs of related transactions.
- Full details: **Domain 4 > Aggregations > Group into Patterns** and **Group into Transactions**.
Sources: https://docs.datadoghq.com/logs/explorer/analytics/patterns/, https://docs.datadoghq.com/logs/explorer/analytics/transactions/, https://docs.datadoghq.com/logs/explorer/analytics/, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/

### Common pitfalls

- Creating a facet does not backfill: older logs show no value for it. Use a calculated field for retroactive analysis of indexed logs.
- Measures need numeric values; a string field from the side panel only offers "facet".
- Unit belongs to the measure; normalize mixed units with the Arithmetic Processor.
- Hiding a facet is personal and does not hide it from monitors, Live Tail or dashboards; it is still valid in queries.
- Sorting on a non-faceted column is unreliable.
- `key:value` search needs no facet, but numerical operators (`<`, `>`, `<=`, `>=`) on an attribute need it declared as a facet first (Search Syntax page).
- Default view changes are private; to share a configuration, save a custom saved view.
- Calculated fields are private and temporary; use pipelines for team-wide, persistent processing.
- Deleting a facet can break indexes, monitors, dashboards and restriction queries.
- A "trace missing" message in the side panel usually means independent sampling, not misconfiguration.

Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/explorer/calculated_fields/, https://docs.datadoghq.com/logs/explorer/side_panel/

# Domain 4: Log Analysis

## Filtering and Excluding

Two different "filtering" worlds, and the exam mixes them:
- **Query-time filtering** (Log Explorer): narrows what you *see* among already-indexed logs. Costs nothing, changes nothing stored.
- **Ingest-time filtering** (index filters, exclusion filters, daily quotas): decides what gets *indexed* (stored, searchable, billed as indexed). Excluded logs are still ingested, processed by pipelines, visible in Live Tail, usable for log-based metrics, archived, and available to Cloud SIEM.

### Filtering in the Log Explorer: facet panel and side panel
- A Log Explorer search = **time range + search query**. Time range selector is at the top right of the Log Explorer.
- **Facet panel** (left): open a facet to see the top unique values with a log count for the current query scope.
  - **Clicking a value** toggles the search between *only this value* and *all values*.
  - **Clicking a checkbox** adds or removes that one value from the selected list (unchecking one value = exclude it, keep the rest).
  - You can search inside a facet's values.
  - **Measures** show a slider with min and max; drag it or type numbers to filter a range.
- **Log side panel**: click an attribute or tag value in the JSON section to append it to the search as an include or exclude filter, add/remove it as a column, or create a facet/measure from it.
- Facets are **not required** to filter: `key:value` search works on any tag/attribute without a facet. Facets help (autocomplete, top values, counts). Exception: numeric comparisons (`>`, `<`, ranges) need the attribute to be a facet/measure. Integer-typed dimensions and measures allow range filters, for example `@http.status_code:[200 TO 299]`.
- **Index facet** (`index`): appears only when the org has **multiple indexes** and/or active **historical views** (rehydrations). Use it to scope a query to a subset of indexes, for example `index:main`.
- Hiding facets, the facet search box, the 1000-facet guideline, "new facet = new logs only" and where facets are not needed: **Domain 3 > Explorer Functionality > Managing facets**.
Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/explorer/side_panel/, https://docs.datadoghq.com/logs/explorer/search/

### Negation and filter syntax for narrowing
- Operators (`AND`, `OR`, `-`; case-sensitive; no operator = implicit `AND`), grouping, `@` rules, case sensitivity, wildcards, numeric ranges, CIDR and advanced search (`IN`/`NOT IN` subqueries) are covered in **Domain 3 > Search Syntax**. Narrowing examples:
  - `service:payments status:error -host:canary-01` = payments errors not from host canary-01.
  - `-@http.status_code:*` = logs that do **not** have the attribute; `@http.status_code:*` = logs that have it.
  - `source:vpc NOT(CIDR(@network.client.ip, 13.0.0.0/8)) CIDR(@network.destination.ip, 15.0.0.0/8)`.
  - `@http.response_time:>100`, `@http.status_code:[400 TO 499]` (attribute must be a facet).
- **Full-text search** `*:term` works in Log Management (Explorer, monitors, dashboards, notebooks) but **cannot** be used in index filters, archive filters, pipeline filters, rehydration filters, log-based metric filters, or Live Tail.
- Out of scope for questions in this subdomain: Cloud SIEM and APM trace correlation are cross-product uses of logs; mention them only as background.
Sources: https://docs.datadoghq.com/logs/explorer/search_syntax/, https://docs.datadoghq.com/logs/explorer/advanced_search/

### Filtering by time
- Sliding (`5h`), growing (`since Jun 1`, `from 5h`), fixed (`Jan 1 - Jan 2`, Unix seconds or milliseconds) and calendar-aligned (`today`, `week to date`, `last week`) time frames: **Domain 3 > Live vs. Explorer > Log Explorer search and time ranges**. Queries run in UTC; the frame is chosen in the **browser's time zone**.
- Example: `service:payment status:error rejected` + `Past 15 minutes`.
- Live Tail is chosen from the time-range selector in the Log Explorer.
Sources: https://docs.datadoghq.com/dashboards/guide/custom_time_frames/, https://docs.datadoghq.com/logs/explorer/search/

### Saved views
- Saved Views (upper left of the Log Explorer) store the query **and time range** (fixed ranges converted to live ones), the default visualization and the facet subset. The **default view** is private; integration saved views are read-only; custom saved views are shared and editable by anyone except Read Only users. Full details: **Domain 3 > Explorer Functionality > Saved views and the default view**.
Sources: https://docs.datadoghq.com/logs/explorer/saved_views/

### Indexes and index filters

- Indexes live in Logs > Configuration (Pipelines page) > **Indexes** (`/logs/pipelines/indexes`). Index details show logs indexed in the past 3 days and retention.
- Indexed logs are needed for faceted search, patterns, analytics and log monitors.
- New account = **one index** for all logs. Use multiple indexes for **multiple retention periods** and **multiple daily quotas** (finer budget control, usage monitoring, billing).
- Create with **New Index**. Default maximum **100 indexes** per account (support can raise it).
- Index name: must start with a letter; only lowercase letters, numbers and `-`.
- Delete: Delete icon in the index action tray; requires `Logs delete data` (`logs_delete_data`). A deleted index stops accepting logs, its logs become unqueryable, and **you cannot recreate an index with the same name**.
- **Index filter** = a query that routes logs into an index. **Logs enter the FIRST index whose filter they match**; reorder with drag and drop. A last index with no filter (`*`) catches the rest.
  - Example order: `status:notice` > `status:error` > `*`.
- API fields: `name`, `filter.query`, `num_retention_days` (Standard tier days), `num_flex_logs_retention_days` (total Standard + Flex days), `daily_limit`, `daily_limit_reset.reset_time` (`HH:00`) + `reset_utc_offset` (`+02:00`), `daily_limit_warning_threshold_percentage`, `exclusion_filters[]`, `tags`, read-only `is_rate_limited`.
- Permissions: `logs_modify_indexes` (global; create/edit indexes, filters, retention, and grant per-index `logs_read_index_data` and `logs_write_exclusion_filters`). `logs_write_exclusion_filters` can be global or scoped to specific indexes via the UI field "Grant editing Exclusion Filters of this index to" (UI only, not API).

Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/, https://docs.datadoghq.com/api/latest/logs-indexes/, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/

### Exclusion filters and sampling

- Default: an index has **no** exclusion filters, so everything matching the index filter is indexed.
- Add: Log Indexes > expand the index > **Add an Exclusion Filter**.
- An exclusion filter = **query** + **sampling rule** + **active/inactive toggle**:
  - Default query `*` (all logs in the index).
  - Default sampling rule **Exclude 100% of logs** matching the query. Rate 0-100%. API: `sample_rate` 1.0 = exclude all.
  - Default toggle **active**. Inactive = ignored for **new** logs (already-excluded logs do not come back).
- So a filter saved with defaults excludes **everything** in that index.
- Sampling applies either to **individual logs** or to **groups of logs defined by unique values of an attribute** (`sample_attribute`, for example `@user.email`, `@ci.job_id`, Trace ID). When an attribute is set, only logs with that attribute are sampled.
  - Individual-log sampling uses trace IDs when present, so kept logs are more likely to correlate with sampled traces. Choosing Trace ID as the attribute behaves the same.
  - Trace ID sampling needs the **trace ID remapper** upstream in pipelines.
- **Only the first ACTIVE matching exclusion filter applies.** A log that matches a filter (even if it survives the sampling) ignores all later filters. A log is never sampled twice. Reorder with drag and drop.
- Examples from docs:
  - Switch off/on: 100% filter on `status:DEBUG`, toggle in UI or API during incidents.
  - Trends: keep 3xx/4xx/5xx, exclude 95% of `source:nginx AND http.status_code:[200 TO 299]`; build a log-based metric for full KPIs.
  - Entity sampling: `env:production`, exclude 90% of `@user.email` (keeps full logs for about 10% of users).
  - `service:my_python_app`, exclude 50% of Trace ID.
- **Consistent sampling across indexes**: one exclusion rule per index, **same sampling rate and same attribute**, check filters and their order.
- From **Patterns**: select a pattern > **Add Exclusion Filter** (top right of pattern panel). Opens index configuration in a new tab, prefilled for the index holding most of that pattern's logs. **Disabled if less than half of the pattern's logs fall in a single index.**
- Excluded logs: **not** in Log Explorer search, analytics, patterns or log monitors. **Still** in Live Tail, log-based metrics, archives, and Cloud SIEM detection (LwL powers SIEM without indexing).
- Audit Trail records who changed retention or exclusion filters.

Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters, https://docs.datadoghq.com/logs/guide/getting-started-lwl/, https://docs.datadoghq.com/logs/live_tail/, https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/

### Daily quotas, warning thresholds and usage monitoring

- Daily quota = hard limit on logs **stored** in an index per day, set **in millions of logs**. Counted **after** exclusion filters.
- After the quota: logs are not indexed but still go to Live Tail, archives and log-based metrics.
- Default reset **2:00pm UTC**; optional custom reset time (API `reset_time` + `reset_utc_offset`).
- Optional **warning threshold** as a % of the quota, **minimum 50%**.
- Quota and threshold changes take effect **immediately**.
- An **event** is generated when the quota or the warning threshold is reached. Monitor: events query `source:datadog datadog_index:* "daily quota reached"`, count by `datadog_index`, evaluate over current day starting at reset time. Datadog recommends alerting at **80%** of quota over the past 24 hours.
- Usage metrics (free, 15 months): `datadog.estimated_usage.logs.ingested_events`, `datadog.estimated_usage.logs.ingested_bytes`. Tags: `datadog_index`, `datadog_is_excluded`, `service` (+ `status` on ingested_events). Use `datadog_is_excluded:false` to count **indexed** logs. `N/A` = ingested but not routed by any inclusion/exclusion rule.
- Index-scoped log monitor: query including `index:main`.

Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/#set-daily-quota, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/, https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/#logs-usage-metrics

### Retention per index

- Retention is set **per index** = how long logs are stored and searchable. Values allowed by your contract.
- Extra retentions: contact Customer Success (`success@datadoghq.com`), then update indexes.
- **Out-of-contract retention periods**: enabled per org in Organization Settings by a user with **Org Management**; then users with **Modify Index** can pick 3, 7, 15, 30, 45 or 60 days. Incurs on-demand charges. Not inherited by child orgs.
- Use multiple indexes when different logs need different retention (for example 7 vs 30 days).

Sources: https://docs.datadoghq.com/logs/log_configuration/indexes/#update-log-retention, https://docs.datadoghq.com/account_management/org_settings/#out-of-contract-retention-periods-for-log-indexes

### Flex Logs (high level)
- Tier choice (Standard / Flex / Archives), compute sizes, retention options, Standard-then-Flex arithmetic and the compute limit: **Domain 1 > Logging Systems > Flex Logs**.
- Configured **in the index**: Indexes Configuration > edit index > Flex Tier > Configure Storage Tier and Retention. **Index filters also apply to Flex.**
- Search: **Include Flex Logs** toggle next to the time picker in the Log Explorer. **Not supported: monitors, Watchdog.** Dashboards supported.
Sources: https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/logs/guide/flex_compute/

### Common pitfalls

- Thinking excluded logs are dropped entirely: they are still ingested (and billed for ingestion), in Live Tail, metrics, archives, SIEM.
- Putting a catch-all index (`*`) first: it captures everything and later indexes get nothing.
- Expecting two exclusion filters to stack: only the first active matching one applies.
- Saving an exclusion filter with the default `*` query: excludes the whole index.
- Toggling a filter off and expecting past logs to reappear: it affects only new logs.
- Using `*:term` full-text syntax in an index filter: not supported.
- Expecting a Flex-only index to drive a log monitor: monitors are not supported on Flex.
- Thinking a warning threshold can be 25%: minimum is 50%.
- Expecting over-quota logs to be indexed later: after the daily quota is reached, logs are simply not indexed (still in Live Tail, archives, log-based metrics).
- Confusing `1w` (sliding past 7 days), `week to date` (12AM Monday until now) and `last week` (the full previous calendar week).

## Aggregations

### Log Analytics overview: three ways to "Group into"
- In the Log Explorer query editor, the **Group into** selector aggregates the queried logs into one of three types: **Fields**, **Patterns**, or **Transactions**.
- The fields you pick to group, aggregate and measure are **kept** as you switch between visualizations and aggregation types.
- You can add **multiple queries** and apply **formulas and functions** (see below).
- **Aggregations work on indexed logs only.** To aggregate non-indexed logs (dropped by exclusion filters, or sent only to archives), the docs list three options:
  - temporarily disable the index exclusion filters (switch off / switch on),
  - generate **log-based metrics** (computed at ingestion on all ingested logs, before indexing),
  - **rehydrate** the logs from archives.
- Pitfall: "Group into Patterns, group by status and service" is not how you chart log counts by a facet. For counts per facet value, use **Group into Fields** and pick the facet in the group-by (`by`) dropdown.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/, https://docs.datadoghq.com/logs/explorer/

### Group into Fields: what you can compute
- All logs matching the query filter are grouped by the values of the chosen group-by field(s) (facets or tags).
- On each group you can compute:
  - **count of logs** per group (the default),
  - **count of unique values** of a field per group (shown in the UI as `count unique of`). Works on qualitative facets (dimensions), for example a facet on `@user.email` to count distinct users per day,
  - **statistical operations** on numerical values. The Log Analytics page lists `min`, `max`, `avg` and **percentiles**; the Facets page also uses `sum` on measures, and the aggregate API accepts `sum`, `median` and `pc75`/`pc90`/`pc95`/`pc98`/`pc99`. These need a **measure** (a quantitative facet).
- **Multi-valued logs are counted in each group.** A log tagged `team:sre` and `team:marketplace` counts once in the `team:sre` group and once in the `team:marketplace` group. So the sum of group counts can be higher than the total number of logs.
- Logs with a null or empty value for a dimension are not shown as a sub-group in nested tables.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/#group-logs-by-fields, https://docs.datadoghq.com/logs/explorer/visualize/#nested-tables

### Facets vs measures (what each aggregation needs)
- Facet concepts, units, creation, hiding and groups: **Domain 3 > Explorer Functionality > Facets** and **Managing facets**. What matters for aggregations:
  - **Qualitative facets = dimensions** (string or integer): top values, **count unique**, filtering. An integer dimension also allows range filters such as `http.status_code:[200 TO 299]`.
  - **Quantitative facets = measures** ((long) integer or double): **aggregate values** (avg, sum, percentiles), range filter, sort logs by value.
  - From the log side panel, a **string** value only offers facet creation; a **numerical** value offers **both facet and measure**. From the facet list: **+ Add** with the tag key or the `@`-prefixed attribute path.
  - **A new facet only fills in for logs ingested after it is created**; logs already indexed are not backfilled.
  - Measure units belong to the measure (BYTES, TIME): with a `duration` measure in nanoseconds you can query `duration:>20ms`; normalize mixed units first with an Arithmetic processor.
  - **Hidden facets** disappear from autocomplete and from the **measure and group-by dropdowns** in Explorer analytics; they stay valid in queries; no effect on Live Tail, monitors or dashboard widgets.
  - Arrays of JSON objects cannot be faceted directly: extract the attribute with a grok parser first. Aliased facets still work but are deprecated; prefer the standard facet. Best practice: at most **1000 facets**.
Sources: https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/explorer/search_syntax/#numerical-values

### Query-time fields for retroactive aggregation (Calculated Fields)
- Facets and pipeline changes only affect **newly ingested** logs. To aggregate on a value from **already indexed** logs, use a **Calculated Field** (Formula or Extraction). It works at query time and can be used for search, **aggregation**, visualization, and other calculated fields.
- Referenced with the `#` prefix, for example `#latency_gap = @client_latency - @server_latency`. Temporary, user-scoped, up to **five** at a time. If it proves useful long term, move the logic into a log pipeline. Creation, syntax and functions: **Domain 3 > Explorer Functionality > Calculated fields**.
Sources: https://docs.datadoghq.com/logs/explorer/calculated_fields/

### Dimensions, top N and ordering of groups
- **Top List** supports **one** dimension in the Fields aggregation.
- **Timeseries, Table, Tree Map and Pie Chart** support multiple dimensions. The current docs disagree on the exact maximum: the Log Analytics page says "up to four" dimensions for the Fields aggregation, while the Log Visualizations page says Timeseries can split by "up to three" facets and nested tables show top values from "up to three" facets. Because the current docs conflict, do not rely on the exact number; the safe facts are "Top List = one dimension" and "the others = several".
- **With several dimensions, top values are nested**: first the top values of dimension 1, then the top values of dimension 2 *within each* top value of dimension 1, and so on. Example: top 10 availability zones, then top 10 versions inside each zone. Those are not the 10 most common versions overall.
- Each group-by has a top/bottom **limit** (for example top 10, top 50 URL paths).
- **Tables with several measures**: the top or bottom list follows the **first** measure. The other measures are only shown for those rows.
- **Table subtotals can differ** from the real sum of a group because only the top (or bottom) subset is shown. Null or empty values are not shown as a sub-group.
- A Table with one measure and one dimension is the same as a Top List, just displayed differently.
- Log Analytics API (`POST /api/v2/logs/analytics/aggregate`), for reference:
  - `group_by[].limit` has a **default of `10`**,
  - at most **10000** buckets. With several group-bys, the **product of the limits** must not exceed 10000,
  - `sort.type` is `alphabetical` (default) or `measure`, and `order` is `asc` or `desc`,
  - `compute.aggregation` values: `count`, `cardinality` (this is unique count), `pc75`, `pc90`, `pc95`, `pc98`, `pc99`, `sum`, `min`, `max`, `avg`, `median`,
  - `compute.type` is `total` (default, for a table or top list) or `timeseries` (with an `interval`, for example `1m`). The interval defaults to a resolution of 150 points,
  - `group_by[].missing` sets the value used for logs that do not have the facet,
  - `histogram` buckets only work on measures, with at most 100 buckets,
  - paging with `page.cursor` (at most 1000 results) only works if `sort` is `alphabetical` for at least one facet.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/#visualize-log-groups, https://docs.datadoghq.com/logs/explorer/visualize/, https://docs.datadoghq.com/api/latest/logs/#aggregate-events, https://docs.datadoghq.com/logs/guide/build-custom-reports-using-log-analytics-api/

### Multiple queries, formulas and functions
- **Multiple queries** are supported in **Timeseries** and **Table** visualizations. Add one with the **+ Add** button next to the query editor. A new query **copies the last query and its grouping options**, and is selected for display by default.
- Show or hide a query in the chart by clicking its **letter** (A, B, ...) in the query editor.
- **Timeline for** dropdown: chooses which query's timeline is displayed.
- **Use facets with** dropdown: chooses which query is changed when you click values in the facet panel. Only the selected query is updated.
- **Formulas**: add with **+ Add**. Example: `A / B` = ratio of unique `Cart Id` for Enterprise vs Premium merchants. **All queries in a formula must be grouped by the same field** (in the example, both by `Webstore Store Name`).
- **Functions**: supported in **all** visualizations. Click the **Σ** icon next to the measure (or next to a formula). Available families are the same as in the dashboard graph editor: Arithmetic, Interpolation, **Timeshift**, Rate, Smoothing, **Rollup**, **Exclusion**.
  - Exclusion example: `cutoff min` at 100 hides values below 100.
  - Timeshift example: apply "week before" to the error-ratio formula to compare with last week.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/#multiple-queries, https://docs.datadoghq.com/logs/explorer/analytics/#formulas, https://docs.datadoghq.com/logs/explorer/analytics/#functions

### Rollups and time intervals
- Every timeseries is aggregated over time intervals (**rollup**). For log timeseries you choose the **roll-up interval** in the display options, along with bars, lines or areas. Bars are recommended for counts and unique counts. Lines are recommended for statistical aggregations.
- The `rollup` function (Σ > Rollup): `.rollup(<AGGREGATOR>, <INTERVAL>)` or `.rollup(<AGGREGATOR>)`.
  - Aggregator is one of `avg`, `sum`, `min`, `max`, `count`. The default is `avg`.
  - The interval is given **in seconds**. Example: `.rollup(sum,120)` sums the points in 2-minute buckets, and `.rollup(avg,86400)` gives daily averages.
  - A custom interval can only make points coarser than the enforced interval, within the **1,500 points per series** limit.
- Default (enforced) intervals for line graphs: past 1h = 20s, past 4h = 1m, past day = 5m, past week = 1hr. Bar graphs use coarser intervals: past 1h = 1m, past day = 20m, past week = 2hr. The Query Value widget targets 150 points.
- `moving_rollup(<query>, <interval>, <aggregator>)` combines the points from the last X seconds.
- Calendar-aligned rollup: `.rollup(sum, weekly, monday, 'America/New_York')`. Units are `daily`, `weekly` or `monthly`. The default week start is `sunday` and the default timezone is UTC.
- Avoid rollups in monitor queries. Rollup buckets are aligned to UNIX time, so a monitor can evaluate an incomplete bucket.

Sources: https://docs.datadoghq.com/dashboards/functions/rollup/, https://docs.datadoghq.com/logs/explorer/visualize/#timeseries

### Group into Patterns
- **Default behaviour**: patterns cluster logs with similar values of the **`message`** field, and group the results by **Status** and **Service**. You can choose other attributes for clustering or grouping.
- **Pattern detection uses 10,000 log samples.** To see patterns for a smaller subset (a rare error, for example), **refine the search query** first.
- Use case: find and filter out noisy error patterns that could hide other issues.
- Visualization: **List** (list of aggregates) only. Patterns are sorted by the **number of matching logs per pattern, descending**.
- **Pattern side panel** (click a pattern):
  - see a sample of logs from that pattern,
  - **append the search filter** to scope the query to that pattern only,
  - get a **kickstart for a grok parsing rule** to extract structured attributes from logs of that pattern.
- **Pattern Inspector**: the variable (aggregate) values in the message are **highlighted in yellow**. Hover one for a quick distribution preview. Click it to open the side panel's **Pattern Inspector** tab, which shows the distribution of the underlying values, for example how many hosts or which regions are affected.
- Export to CSV: up to **300** patterns (100,000 for individual logs, 500 for transactions).
- The Watchdog Insights error outlier side panel also shows a list of log patterns (https://docs.datadoghq.com/logs/explorer/watchdog_insights/).

Sources: https://docs.datadoghq.com/logs/explorer/analytics/patterns/, https://docs.datadoghq.com/logs/explorer/visualize/#list-aggregates-of-logs, https://docs.datadoghq.com/logs/explorer/export/

### Group into Transactions
- Transactions aggregate indexed logs by **instances of a sequence of events**, such as a user session or a request that crosses several microservices. You group on a shared attribute such as `requestId`, `orderId`, a trace ID or a session ID.
- **Main difference from Fields**: each transaction includes the logs that match the query **and also all other logs that belong to the same transaction**.
- Two measures are **added automatically**:
  - **Duration**: the time between the **first and last log** of the transaction (last timestamp minus first timestamp),
  - **Maximum Severity**: the highest status found among the transaction's logs.
- **Find Key Items**: for any **string facet**, use `count unique`, `latest`, `earliest`, or `most frequent`.
- **Get Statistics**: for any **measure**, use `min`, `max`, `avg`, `sum`, `median`, `pc75`, `pc90`, `pc95`, `pc99`.
- **Set Start and End Conditions**: set the transaction boundaries with **separate queries** for the start and the end. This splits one ID into several transactions, which form a **transaction group**.
- Visualization: **List Aggregates**. Results are sorted by the **transaction ID in lexicographic order, ascending (A to Z)** by default.
- **Transaction side panel**: see all logs in the transaction, and search for specific logs inside it.
- **Transaction group side panel** (when start/end conditions are used): see the transactions of the group **in sequence**, see all logs of each transaction, and view statistics for each transaction plus **summary statistics** for the whole group.
- Export to CSV: up to **500** transactions.
- The current docs give no numeric limit for the maximum duration or span of a transaction.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/transactions/, https://docs.datadoghq.com/logs/explorer/visualize/#list-aggregates-of-logs, https://docs.datadoghq.com/logs/explorer/export/

### Common pitfalls (exam traps)
- Analytics on logs that an exclusion filter dropped: these logs are not indexed, so they do not appear. Use log-based metrics, temporarily disable the filter, or rehydrate.
- Avg or percentiles on an attribute that has no measure: create a **measure** (from a numerical field in the side panel), not just a dimension facet. Unique count works on a qualitative facet.
- A new facet or pipeline change does not backfill. Use Calculated Fields for already indexed logs.
- Sum of group counts > total log count: multi-valued fields count a log in each group.
- Second-level groups are the top values *within* each top first-level value, not the global top values.
- Formula `A/B` needs both queries grouped by the same field.
- Patterns use 10k samples: narrow the query to reveal rare patterns. The default clustering field is `message`. The default grouping is Status + Service.
- Transactions pull in logs that do not match the query, as long as they share the transaction ID.
- Pattern list sort = count descending. Transaction list sort = transaction ID ascending.

Sources: https://docs.datadoghq.com/logs/explorer/analytics/, https://docs.datadoghq.com/logs/explorer/facets/, https://docs.datadoghq.com/logs/explorer/calculated_fields/

## Visualizing

### Where visualizing fits in the Log Explorer
- Log Explorer workflow: **Search & filter -> Analyze (group) -> Visualize -> Export**. Visualizations define how the outcome of filters and aggregations is displayed; pick them in the logs query editor.
- Visualization types in the Log Explorer: **List** (individual logs, or aggregates for Patterns/Transactions), **Timeseries**, **Top List**, **Table** (nested tables), **Tree Map**, **Pie Chart**.
- "Group into" choices: **Fields**, **Patterns**, **Transactions**. The fields you selected to group, aggregate and measure are kept when you switch between visualizations and aggregation types.
- Aggregations are supported for **indexed logs only**. To aggregate non-indexed (excluded) logs: temporarily disable exclusion filters, generate **log-based metrics**, and/or **rehydrate** from archives.
- Natural Language Queries (click **Ask** in the search field) can build visualizations from plain English, e.g. "Top 20 services by errors" (not on GovCloud sites; disable in Organization Settings > Preferences, needs `org_management`).
- A Saved View stores the query, live time range, the default visualization (log stream, patterns or analytics with their visualization properties), the visible facet subset, and the list's column configuration.
- Choosing the right visualization:
  - Need to read individual events -> **List of logs**.
  - Trend over time / spike detection -> **Timeseries**.
  - Rank values of ONE facet by a measure ("top 15 customers by unique sessions") -> **Top List**.
  - Rank across up to several facets plus extra measures per row -> **Table (nested table)**.
  - Share of a whole -> **Pie Chart** (radial slices) or **Tree Map** (nested rectangles, size + color, hierarchy when several attributes selected).
  - Noisy repeated messages -> **Patterns**; a sequence of events (session, request across services) -> **Transactions**.
  - Single KPI number on a dashboard -> **Query Value** widget.
Sources: https://docs.datadoghq.com/logs/explorer/, https://docs.datadoghq.com/logs/explorer/visualize/, https://docs.datadoghq.com/logs/explorer/analytics/, https://docs.datadoghq.com/logs/explorer/search/, https://docs.datadoghq.com/logs/explorer/saved_views/

### Lists
- Lists are **paginated** results of logs or aggregates; useful when individual results matter and you do not know in advance what defines a match.
- **List of logs** - columns:
  - Use the **table** (interactions in its first row/header) to **sort, rearrange, remove** columns (preferred method for these).
  - Use the **facet panel** (left) or **log side panel** (right) to **add** a column for a field (preferred method for adding).
  - **Options** button: controls **Content Height** and **Content Display** per log.
- **Default sort: by timestamp, most recent on top** - fastest and recommended for general use. You can also sort by a measure (lowest/highest first) or lexicographically by a facet's value.
- Pitfall: any attribute or tag can be added as a column, but sorting is only reliable if you **declare a facet** first; non-faceted attribute columns do not sort reliably.
- Column configuration is saved with Saved Views.
- **List aggregates** (Patterns/Transactions): columns are derived from the aggregation. Default sort:
  - **Patterns**: number of matching events per pattern, **descending** (more to less).
  - **Transactions**: lexicographic order of the **transaction id**, **ascending** (A to Z).
Sources: https://docs.datadoghq.com/logs/explorer/visualize/#lists

### Timeseries
- Shows the evolution of a **single measure** (or a facet **unique count**) over the selected time frame, optionally **split by facets** (visualize page: "up to three"; analytics page: "up to four dimensions" - see Ambiguities).
- Example in docs: top 50 URL paths by p95 of `duration` over the last 15 minutes.
- Display options: **roll-up interval**; display as **bars** (recommended for **counts and unique counts**), **lines** (recommended for **statistical aggregations**: avg, percentiles...), or **areas**; **colorset**.
- Multiple queries and formulas are supported in Timeseries.
Sources: https://docs.datadoghq.com/logs/explorer/visualize/#timeseries, https://docs.datadoghq.com/logs/explorer/analytics/#visualize-log-groups

### Top List
- Top values of **one facet** according to a chosen measure, e.g. top 15 customers by unique sessions over the last day.
- Fields aggregation supports **one dimension for Top List** (vs. several for Timeseries, Table, Tree Map, Pie Chart).
- Getting-started workflow: aggregate into **Fields** and visualize as **Top List** to see top logging services; click a value > View Logs to open matching logs.
Sources: https://docs.datadoghq.com/logs/explorer/visualize/#top-list, https://docs.datadoghq.com/logs/explorer/analytics/#visualize-log-groups, https://docs.datadoghq.com/getting_started/logs/

### Nested tables (Table)
- Top values from **up to three facets** (visualize page) according to a chosen measure - **the first measure in the list** - plus the value of additional measures for each row. You can update the query or view the logs for either dimension.
- With multiple measures, the top/bottom list is determined by the **first measure**.
- **Subtotals may differ** from the sum of shown values because only a subset (top or bottom) is displayed; events with **null or empty** values for a dimension are **not shown as a sub-group**.
- A Table with **one measure and one dimension is the same as a Top List**, just displayed differently.
- Example in docs: top 10 availability zones, and for each the top 10 versions by number of error logs, with unique counts of hosts and container IDs.
- Multi-dimension ordering: top values by the first dimension, then the second dimension within the top values of the first, then the third within the second.
Sources: https://docs.datadoghq.com/logs/explorer/visualize/#nested-tables, https://docs.datadoghq.com/logs/explorer/analytics/#visualize-log-groups

### Pie chart and Tree map
- **Pie chart**: shows data as a **percentage of a whole**; compare dimensions such as services, users, hosts, countries. Example: percentage breakdown by service.
- **Tree map**: percentage of a whole as **nested rectangles**; compare dimensions with both **size and color**; selecting **multiple attributes** shows a **hierarchy** of rectangles.
- Dashboard widgets: both can show a single dataset or **nested proportions**; difference is radial slices (pie) vs nested rectangles (treemap). Both support formulas, context links (on by default), **filter and focus** on one category (treemap: click outer portion, back button top-left; pie: click outer ring, click center to go back).
- Pie chart widget: **Total amount display** (Automatic shows total in the center once the graph is big enough); legend **Aside**, **Table**, or off (Automatic = Aside on dashboard, Aside + Table in full screen).
Sources: https://docs.datadoghq.com/logs/explorer/visualize/#pie-chart, https://docs.datadoghq.com/logs/explorer/visualize/#tree-map, https://docs.datadoghq.com/dashboards/widgets/pie_chart/, https://docs.datadoghq.com/dashboards/widgets/treemap/

### Group by Fields: measures
- Per group: **count of logs**, **count of unique values** (`count unique of`), or **statistical operations** (`min`, `max`, `avg`, percentiles) on a measure. A log with several values for the grouped field is counted in **each** group (`team:sre` and `team:marketplace`). Measures carry BYTES or TIME units. Details: **Aggregations > Group into Fields** and **Facets vs measures**.
Sources: https://docs.datadoghq.com/logs/explorer/analytics/#group-logs-by-fields, https://docs.datadoghq.com/logs/explorer/facets/

### Patterns
- Default clustering on `message`, grouped by **Status** and **Service**; **10,000 log samples**; **List** visualization; pattern side panel (sample logs, append the search filter, Grok kickstart); **Pattern Inspector** (values highlighted **yellow**); CSV export up to **300**. Details: **Aggregations > Group into Patterns**.
Sources: https://docs.datadoghq.com/logs/explorer/analytics/patterns/, https://docs.datadoghq.com/logs/explorer/export/

### Transactions
- Groups indexed logs by a shared attribute (`requestId`, `orderId`); each transaction includes **all logs belonging to it**, not only matching ones; **Duration** and **Maximum Severity** are added automatically; Find Key Items, Get Statistics, Start and End Conditions; List Aggregates sorted by transaction ID ascending; CSV export up to **500**. Details: **Aggregations > Group into Transactions**.
Sources: https://docs.datadoghq.com/logs/explorer/analytics/transactions/, https://docs.datadoghq.com/logs/explorer/visualize/#list-aggregates-of-logs

### Multiple queries, functions and formulas in the Log Explorer
- **Multiple queries** only in **Timeseries** and **Table**; **functions** (Σ icon) in **all** visualizations; **formulas** need all queries grouped by the same field; a **Timeshift** (week before) on a formula compares with a week earlier. Details: **Aggregations > Multiple queries, formulas and functions**.
Sources: https://docs.datadoghq.com/logs/explorer/analytics/#multiple-queries, https://docs.datadoghq.com/logs/explorer/analytics/#functions, https://docs.datadoghq.com/logs/explorer/analytics/#formulas

### Exporting from the Log Explorer
- Export menu (Saved View, Dashboard/Notebook widget, Monitor, Metric, cURL, CSV, Share View), CSV limits (**100,000** logs, **300** patterns, **500** transactions; timeseries, top list and table also downloadable), CSV sanitizing, **Save to notebook** (a single log persists after it ages out of retention) and the 1000-logs-per-call API limit: **Domain 5 > Exporting > Log Explorer Export menu**.
- **Analyze in Notebooks** (Log Explorer button): with "Use as a computational data source" it adds a **data source cell** with the same query; such cells use a **local time fixed** to the export-time frame (cells created inside the notebook default to the global time). Columns shown in the Explorer are included.
Sources: https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/notebooks/advanced_analysis/

### Dashboard widgets with log data
- Graph editor (pencil icon) tabs: **Edit** (default), **JSON**, **Share**. Quick Graphs: press `G` anywhere (or Cmd/Ctrl+K, dashboards submenu); supports Timeseries, Top List, Query Value, Geomap.
- Querying event data (logs) in a widget: filter (key:value + full text) -> choose **measure** (pick aggregation) or **facet** (unique count) -> split by a facet -> **rollup** interval (available steps depend on global timeframe) -> optional functions.
- **List widget** (replaces the old Log Stream widget; the Log Stream page now says to use the List widget): data source **Logs** shows individual log events. Logs options: **Group by Patterns or Transactions**; storage location **Standard Indexes**, **Standard Indexes + Flex Logs**, or **Online Archives** (depending on config); **message column lines: 1, 3, or 10**; choose columns, sort by a displayed column asc/desc, search query. On screenboards and notebooks choose custom or global timeframe. JSON: `"type": "list_stream"`, `data_source` `logs_stream` (default), `logs_pattern_stream` (group_by up to 4 items), `logs_transaction_stream` (one group_by required); `columns[].width` `auto|compact|full`; `response_format: "event_list"`.
- **Timeseries widget**: data from Metric, Indexed Spans, or **Log Events**; display as lines, areas, bars; last incomplete interval shaded "partial data"; line Style (solid/dashed/dotted) and Stroke (normal/thin/thick); palettes Classic / Consistent (16 colors); automatic labels (max 3 per series, none if > 6 series); event overlays; markers; **dual y-axis** (click **Add Graph**, choose left/right axis); y-axis Min/Max/Scale (linear default, log, pow, sqrt)/Always include zero (default on); legend Automatic/Compact/Expanded/None; **Compare Time** tab in inspect mode.
- Timeseries JSON: legacy `log_query` object is **DEPRECATED** - use `queries` + `formulas` with an events query `"data_source": "logs"`, `compute.aggregation` one of `count, cardinality, median, pc75, pc90, pc95, pc98, pc99, sum, min, max, avg`, `group_by[].facet/limit/sort`, `search.query`, optional `indexes` (omit or `[]` = all indexes); `response_format: "timeseries"`.
- **Top List widget**: Display modes **Stacked** (default) or **Flat**; **Relative** (percent of total) vs **Absolute**; Relative only for **count data** (count metrics or log events); Visual Formatting Rules; context links on by default.
- **Table widget**: columns via **+ Add Query** / **+ Add Formula**; aliases via **as...**; column formatting rules (threshold, range, text, trending); search bar Auto. **N/A cells**: each column is queried **independently** and rows are joined by matching group names, so groups may not overlap; mitigate by raising query limits and sorting by the "driving" column.
- **Query Value widget**: one value from a metric, APM, or **log** query, reduced as `avg`, `min`, `sum`, `max`, or `last` (percentiles where supported); conditional formatting (background/font color, custom image); optional timeseries background (Min to Max, Line, Bars); Change Indicator (relative/absolute, compare to previous period/day/week/month/custom). Targets **150 points** (vs 1,500 for line/bar graphs).
- **Widget menus**: export icon -> Copy, Share snapshot, Declare incident, Add to incident, Create case, **Save to notebook**, Link to widget, Download as PNG/SVG/**CSV**. Context menu: Edit, Clone, Split graph, Create custom links, **Create monitor**, Delete. Full screen: change time frame, pause, **export the graph to a dashboard or notebook**, copy the query, download CSV.
- **CSV export from widgets**: Bar Chart, List, Pie Chart, Scatter Plot, Table, Timeseries, Top List, Treemap; one widget at a time; enabled by default; only **Datadog Support** can disable/re-enable it for the org (not from the UI).
- Copy/paste widgets with Cmd/Ctrl+C / Cmd/Ctrl+V between dashboards and notebooks (dashboard: under cursor; notebook: new cell at end).
- Global time: widgets default to `Global Time`; a widget with a local frame shows its local window applied to the global window.
Sources (Query Value 150-point target is on the Rollup page): https://docs.datadoghq.com/dashboards/functions/rollup/, https://docs.datadoghq.com/dashboards/querying/, https://docs.datadoghq.com/dashboards/guide/quick-graphs/, https://docs.datadoghq.com/dashboards/widgets/list/, https://docs.datadoghq.com/dashboards/widgets/log_stream/, https://docs.datadoghq.com/dashboards/widgets/timeseries/, https://docs.datadoghq.com/dashboards/widgets/top_list/, https://docs.datadoghq.com/dashboards/widgets/table/, https://docs.datadoghq.com/dashboards/widgets/query_value/, https://docs.datadoghq.com/dashboards/widgets/configuration/

### Formulas and functions over log queries in dashboards
- Each query gets a letter (`a`, `b`, ...); write arithmetic in the **Formula** box, e.g. ratio of error logs to info logs `status:error / status:info`. Comma graphs separately (`a, b, c`) - visualizations only, not monitors.
- **Hide a query**: click its letter label (blue = shown, grey = hidden); hidden queries are **still used** in the formula.
- **Formulas are not lettered; arithmetic cannot be done between formulas.**
- Point-by-point compare: `minimum()` / `maximum()`, e.g. `minimum(status:error, status:warn)`. Using `min()`/`max()` for this is **deprecated**.
- `time()`: Unix time in **seconds** for the queried range (formula only). Log `@timestamp` is Unix **milliseconds**: use `time() - (max:@timestamp / 1000)` or `1000 * time() - max:@timestamp`. In scalar widgets (query value, table) it returns the end of the range.
- Functions via the **Σ** (Add Function) icon. Timeshift: `timeshift(q, -<seconds>)`, `calendar_shift(q, "-7d", "UTC")`, `hour_before()`; `day_before()`, `week_before()`, `month_before()` are **being deprecated** -> use calendar shift (`-1d`, `-7d`, `-1mo`/`-30d`/`-4w`). Exclusion: `exclude_null()`, `clamp_min/max()`, `cutoff_min/max()`.
- Rollup: `.rollup(<aggregator>, <interval_seconds>)`, aggregator `avg` (default), `sum`, `min`, `max`, `count`; max **1,500 points** per series; default intervals depend on time frame and line vs bar (e.g. past hour: 20s line, 1m bar; past day: 5m line, 20m bar).
Sources: https://docs.datadoghq.com/dashboards/querying/#advanced-graphing, https://docs.datadoghq.com/dashboards/functions/, https://docs.datadoghq.com/dashboards/functions/timeshift/, https://docs.datadoghq.com/dashboards/functions/rollup/, https://docs.datadoghq.com/dashboards/functions/exclusion/

### Template variables with log widgets
- Template variables can be defined on a tag or an **attribute** (facet or measure). Default value `*`; available values default `(all)`.
- Log/APM/RUM template variables based on facets **start with `@`**, e.g. `@http.status_code`. Wildcards allowed mid-value (`eng*@example.com`) or multiple (`*prod*`). **Add to all** adds the variable to all log/APM/RUM widgets.
- Values in the dropdown are populated from the sources the widgets use (log widgets -> log values).
- Embed a value: `$<NAME>.value`, e.g. `env:staging-$service.value`.
- Notebooks support template variables too.
Sources: https://docs.datadoghq.com/dashboards/template_variables/

### Notebooks with log data
- Collaborative rich-text documents with live graphs: investigations, postmortems, runbooks. Create from **Dashboards > New Notebook** or **New Notebook** on the Notebooks List page; templates in the Template Gallery.
- Notebooks support **all widget types**; insert graphs with slash commands (`/` then type) or Add Cell; **Quick Edit** inline, or pencil / Cmd/Ctrl+click for the full graph editor. Graph size XS, S, **M (default)**, L, XL; legends auto-disabled for XS and S.
- **Time controls**: all graphs linked to the **global notebook time** by default. Changing the global picker or scrubbing updates the URL but is not saved; **Set Default Time** saves it. **Click-and-drag zoom on a graph changes the notebook's global time; it does not unlink the graph.** To give one graph its own time frame, edit it and toggle off **Global Time**.
- **Graph snapshots**: automatic for graphs with a **fixed** time range, to preserve the view past data retention; switching the graph to a global time range (e.g. Past 1 hour) removes the snapshot; when data is past retention the inline snapshot is replaced if you edit the underlying graph.
- Modes: Editing / Viewing (read-only). Version history (preview, restore, clone). Download as PDF from the kebab menu (UI only, one notebook at a time, no API). Permissions: full access by default; Share > Private to me or Custom (roles/teams/users as Editor).
- Widgets in a notebook are saved **last write wins** in multiplayer editing.
- Analysis features: Data Source cell (`/datasource`) for joins, SQL, transformations over log data.
Sources: https://docs.datadoghq.com/notebooks/, https://docs.datadoghq.com/notebooks/advanced_analysis/, https://docs.datadoghq.com/logs/explorer/export/

### Ambiguities and pitfalls
- **Group-by limit for Timeseries/Table**: the Log Visualizations page says Timeseries splits "by up to three" facets and nested tables use "up to three" facets; the Log Analytics page says Fields aggregation supports "up to four dimensions" for Timeseries, Table, Tree Map, and Pie Chart. Three facets is valid under both statements; a question asking for an exact maximum is ambiguous, so prefer questions that only require "more than one" or "three". Both pages agree Top List supports **one** dimension.
- The List widget's JSON allows up to 4 group-by items for `logs_pattern_stream`.
- Aggregations ignore excluded (non-indexed) logs: counts in analytics can be lower than ingestion.
- Pattern lists are built from a 10,000-log sample, so rare messages may be missed on broad queries.
- Sorting by a non-faceted column is unreliable.
- Dashboard Table N/A cells come from independent column queries, not missing data.
Sources: https://docs.datadoghq.com/logs/explorer/visualize/, https://docs.datadoghq.com/logs/explorer/analytics/#visualize-log-groups, https://docs.datadoghq.com/dashboards/widgets/list/

# Domain 5: Log Utilization

## Monitors & Alerting

### What a log monitor evaluates
- A **log monitor** alerts when a specified type of log exceeds a user-defined threshold over a given period of time. It requires Log Management to be enabled.
- It evaluates **indexed logs only**. Logs dropped by an index exclusion filter, logs over an index daily quota, and logs that matched no index are **not** seen by a log monitor (they are still seen by Live Tail and by log-based metrics).
- **Flex Tier logs are not supported for monitors** (even though the Log Explorer can show them). Only **Standard Tier** logs are supported. Flex Logs page: "Monitors are not supported in Flex Logs"; if an index is switched to Flex only, its logs "are no longer queryable in monitors or in Watchdog Insights".
- **Maximum rolling time window for a log monitor: `2 days`** (48 hours). Generic custom window range in the UI: 1 minute to 48 hours (1 month / 730 hours for metric monitors).
- **Default limit: 1000 log monitors per account.** If you hit it, consolidate with **multi alerts** (one grouped monitor instead of many copies) or contact Support.
- Other limits that come up: monitor tags up to **80** per monitor; monitor notification rules default limit **1000 per organization**; a downtime can target at most **32** monitor tags.
- API monitor `type` for log monitors: `log alert`. Query format:
  `logs(query).index(index_name).rollup(rollup_method[, measure]).last(time_window) operator #`
  - `rollup_method`: `count`, `avg`, `cardinality`; `time_window`: `#m` (1-2880) or `#h` (1-48), consistent with the 2-day maximum.
  - Example: `logs("service:checkout status:error").index("*").rollup("count").last("5m") > 100`
- Pitfall: a log monitor is not the tool for anything that must count logs that are not indexed, or needs a window longer than 2 days: use a **log-based metric** + **metric monitor** instead (see below).

Sources: https://docs.datadoghq.com/monitors/types/log/, https://docs.datadoghq.com/logs/log_configuration/flex_logs/, https://docs.datadoghq.com/monitors/configuration/, https://docs.datadoghq.com/api/latest/monitors/, https://docs.datadoghq.com/monitors/manage/, https://docs.datadoghq.com/monitors/notify/notification_rules/

### Creating a log monitor (UI paths)
- Main navigation: **Monitors > New Monitor > Logs** (`/monitors/create/log`).
- From the **Log Explorer**: the Export menu lets you export/save the current exploration as a **Saved View**, **Dashboard widget / Notebook widget**, **Monitor** ("to trigger alerts on predefined thresholds"), **Metric** (Generate new metric, for long-term KPIs), **cURL command**, **CSV**, or **Share View**. Exporting to a monitor carries the current search query into a new log monitor.
  - The Log Management best-practices guide words the same action as: in the Log Explorer, enter a query (for example `index:main`), click **More...** and select **Create monitor**.
- You can also create a monitor directly from an **advanced search** (subqueries / Reference Tables) in the Log Explorer.
- Configuration sections in order: **Define the search query**, **Set alert conditions**, **Configure notifications and automations**, **Define permissions and audit notifications**.
- Preview graphs at the top: **Evaluated Data** (how the monitor would have evaluated history with current thresholds, state transitions, who would be notified, supported for Logs) and **Source Data** (raw query output, no thresholds).
- Monitor templates exist (Monitors > Templates) for preconfigured monitors.

Sources: https://docs.datadoghq.com/monitors/types/log/, https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/, https://docs.datadoghq.com/monitors/configuration/

### Define the search query: count, attribute, measure
- Query uses the same logic as a **Log Explorer search** (same search syntax). The graph above the fields updates as you type.
- Choose what to monitor:
  - **Log count**: search bar (optional) and do **not** select an attribute or measure. Datadog counts matching logs over the window and compares to the threshold.
  - **Facet or attribute**: alerts on the **unique value count** of the attribute (for example the number of unique `user.email` values). Any attribute can be used, but only facets appear in autocomplete. (API: `cardinality` rollup.)
  - **Measure**: alerts on the numeric value of the measure (like a metric monitor) and you must choose an aggregation: `min`, `avg`, `sum`, `median`, `pc75`, `pc90`, `pc95`, `pc98`, `pc99`, or `max`.
- **Σ Modify Query** menu: **Functions and formulas** (transform/combine queries) and **Advanced search** (subqueries, Reference Tables) to scope alerts to curated datasets.
- API `aggregation` option for logs alerts: `{"metric": "count", "type": "count", "groupBy": "core_service"}`; `type` is `count`, `cardinality` or `avg`.

Sources: https://docs.datadoghq.com/monitors/types/log/, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### Group by and simple vs multi alert
- Group logs by tags, attributes and **up to four facets**. Top values are picked by the first dimension, then the second within those, and so on.
- Dimension limits:
  - **1 facet**: 1000 top values
  - **2 facets**: 30 top values per facet (at most 900 groups)
  - **3 facets**: 10 top values per facet (at most 1000 groups)
  - **4 facets**: 5 top values per facet (at most 625 groups)
  - Total limit irrespective of facet count: **1000** combinations; if you raise one dimension, Datadog lowers the others. Default top values per group-by: 10 (the fourth defaults to 5). Example given: 10 / 10 / 5 / 2.
  - With multiple queries/formulas you can choose top or bottom values per dimension.
- **Simple Alert**: aggregates over all reporting sources, **one alert** when the aggregated value meets the condition. Reduces noise. A query with no grouping defaults to Simple Alert.
- **Multi Alert**: applies the alert to **each group**; one alerting event per group meeting the condition (for example one alert per `service`). A grouped query switches to Multi Alert automatically.
- **Notification grouping**: in Multi Alert you can remove dimensions from the notification grouping (for example group by `service` and `host` but notify once per `service`); dimensions not aggregated on become **Sub Groups**. You can also remove all and notify as a Simple Alert.
  - API: `notify_by` = list of tags, must be a subset of the query's group-by tags; `["*"]` = notify as a simple alert. `groupby_simple_monitor` is **deprecated** (use `notify_by`).
- In Multi Alert, group values are available as variables (`{{service.name}}`, `{{@facet.name}}`).

Sources: https://docs.datadoghq.com/monitors/types/log/, https://docs.datadoghq.com/monitors/configuration/#set-alert-aggregation, https://docs.datadoghq.com/monitors/guide/monitor_api_options/, https://docs.datadoghq.com/api/latest/monitors/

### Alert conditions, thresholds and recovery
- Comparators for log monitors: `above`, `above or equal to`, `below`, `below or equal to`, `equal to`, `not equal to`.
- **Alert threshold** (required), **Warning threshold** (optional), **Alert recovery threshold** and **Warning recovery threshold** (optional, under Set alert conditions > Advanced Options; API `critical_recovery` / `warning_recovery` in `options.thresholds`).
- Without a recovery threshold, the monitor recovers as soon as the alert condition is no longer met. With one, it recovers only after **passing** the recovery threshold:
  - `>` alert threshold -> recovers when `<=` recovery threshold
  - `>=` -> `<`; `<` -> `>=`; `<=` -> `>`
  - Purpose: reduce noise from a flapping monitor.
- Decimal thresholds below 1 need a leading zero (`0.5`, not `.5`).
- API thresholds dict for logs alerts, e.g. `{"critical": 100, "warning": 50}`.
- Two notification types: **alert** and **warning**.

Sources: https://docs.datadoghq.com/monitors/types/log/#set-alert-conditions, https://docs.datadoghq.com/monitors/configuration/#thresholds, https://docs.datadoghq.com/monitors/guide/recovery-thresholds/

### Evaluation window, frequency and delays
- **Rolling** window: fixed size, start point shifts (last 5 min, 15 min, 1 hour, or custom). Log monitors: max **2 days**.
- **Cumulative** windows: **Current hour** (starts at a configurable minute), **Current day** (configurable hour/minute; example: monitor a daily log index quota starting at 2:00pm UTC), **Current month** (month-to-date, **metric monitors only**). Cumulative windows reset when their span is reached.
- **Evaluation frequency** (default, depends on window):
  - window < 24 h: every **1 minute**
  - 24 h <= window < 48 h: every **10 minutes**
  - window >= 48 h: every **30 minutes**
  - Can also be a custom daily/weekly/monthly schedule.
- **Evaluation delay** (`evaluation_delay`, seconds, non-negative integer, max **86400** = 24 h): shifts the evaluated window back. Doc example: delay 900 s, window last 5 minutes, at 7:00 -> evaluates 6:40-6:45. Datadog recommends 15 min for backfilled cloud metrics.
- **New group delay** (`new_group_delay`, default **60** s; Multi Alert only): wait before alerting on a group not seen in the last 24 h (for example new containers). `new_host_delay` (default 300) is deprecated.

Sources: https://docs.datadoghq.com/monitors/configuration/#evaluation-window, https://docs.datadoghq.com/monitors/configuration/#evaluation-frequency, https://docs.datadoghq.com/monitors/configuration/#evaluation-delay, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### No data, below conditions, auto-resolve, group retention
- `NO DATA` for a log monitor = no logs matched the query during the time frame.
- **Notify when everything stopped**: set the condition to **`below 1`**; this notifies when no logs match the query in the time frame across all groups.
- **Grouped + `below` condition**: triggers **if and only if** there are logs for a given group and its count is below the threshold, **or** there are no logs for **all** groups. A single group that stops sending logs entirely (while other groups still send) does **not** trigger. To catch one service going silent, scope the query to that service (for example `service:backend`, `below 1`).
- **On missing data** options (UI): Evaluate as zero / Show last known status, Show NO DATA, Show NO DATA and notify, Show OK.
  - Defaults: **count** queries -> **Evaluate as zero**; other query types (measure, etc.) -> **Show last known status**. With `default_zero()` the behaviour is locked to evaluate as zero.
  - Example: a log count monitor `> 10` with no matching logs evaluates 0 -> `OK`.
  - API `on_missing_data`: `default`, `show_no_data`, `show_and_notify_no_data`, `resolve` (applies to Logs, APM Trace Analytics, Audit, CI, Error Tracking, Events, RUM monitors). Older generic keys: `notify_no_data` (default `false`), `no_data_timeframe`.
  - The monitor must have been able to evaluate data before it can alert on missing data.
  - If the monitor recovers on no data, the recovery message has no event data; group by extra tags to keep info available via `{{tag.name}}`.
- **Auto resolve** (`timeout_h`, 0-24 h; UI: Never, After 1 hour, ...): only works when data stops arriving; a monitor does not auto-resolve from ALERT/WARN while data is still reporting. Default/recommended: **Never**. To remind people about an unresolved issue, use **renotify**.
- **Group retention**: how long a non-reporting group stays in the monitor status. Default **24 hours** (48 h for host monitors / service checks that notify on no data). Custom value **1 h to 72 h** for multi alert monitors that support On missing data, including **Logs** (API `group_retention_duration`, e.g. `60m`, `1h`, `2d`). Dynamic group retention shortens it automatically for monitors with many churning groups.

Sources: https://docs.datadoghq.com/monitors/types/log/#no-data-and-below-alerts, https://docs.datadoghq.com/monitors/configuration/#no-data, https://docs.datadoghq.com/monitors/configuration/#auto-resolve, https://docs.datadoghq.com/monitors/configuration/#group-retention-time, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### Notification message, @-notifications and routing
- A unique **title** is required; multi alert titles get the triggering tags inserted automatically (API `include_tags`, default `true` -> `[Triggered on {host:h1}] Title`).
- Message supports **Markdown** and variables (Slack/email render only basic formatting: no headers, no tables).
- **@-notifications**: `@<DD_USER_EMAIL>` (active Datadog user), `@<EMAIL>` (any address), integrations as `@<INTEGRATION>-<VALUE>`: `@slack-...`, `@pagerduty-...`, `@webhook-...`, `@teams-...`, `@jira-...`, `@servicenow-...`; `@team-handle` routes to a Datadog Team's channel; `@incident-...` auto-creates an incident (on alert, warn or no data); workflows and cases can be added too.
  - A space is required before the handle: `Disk space is low @ops-team@company.com` (correct) vs `low@ops-team@company.com` (incorrect).
  - Handles with parentheses `()` are not parsed; emails with `/` are not supported; pending-invite or disabled users get nothing.
- **Dynamic handles**: build handles from tag variables, e.g. `@slack-{{service.name}}` -> `@slack-ad-server` (posts to `#ad-server`). Add a fallback (`{{#is_exact_match "kube_namespace.owner" ""}} @slack-example {{/is_exact_match}}`) because a missing attribute renders empty and makes an invalid handle.
- **Notification rules** (Monitors > Settings > Notification Rules, New Rule): recommended way to route recipients by tag scope (Boolean `AND`/`OR`/`NOT`, only `key:*` wildcards); can enable Slack threading. Needs `monitor_config_policy_write` or `monitor_notification_rules_write`.
- **Toggle additional content**: Default, Hide Query, Hide Handles, Hide All (API `notification_preset_name`, default `show_all`).
- **Metadata**: Priority **P1 (highest) to P5**, monitor tags (independent of Agent tags), Teams. `{{override_priority 'P1'}}` overrides the priority in a message block.
- **Test Notifications** button (bottom right) works for **logs** monitors; you pick the transition and group; test events carry `[TEST]` in the title; variables populate with a randomly selected group.

Sources: https://docs.datadoghq.com/monitors/notify/, https://docs.datadoghq.com/monitors/notify/variables/#dynamic-handles, https://docs.datadoghq.com/monitors/notify/notification_rules/, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### Conditional variables
- Syntax: opening and closing pair, e.g.
  ```
  {{#is_alert}}
    Error rate too high on {{service.name}} @pagerduty-checkout
  {{/is_alert}}
  {{#is_recovery}} Recovered @pagerduty-checkout {{/is_recovery}}
  ```
- Main ones: `{{#is_alert}}`, `{{#is_warning}}`, `{{#is_no_data}}`, `{{#is_recovery}}` (from ALERT, WARNING, UNKNOWN or NO DATA), `{{#is_alert_recovery}}` (ALERT -> OK), `{{#is_warning_recovery}}` (WARNING -> OK), `{{#is_alert_to_warning}}`, `{{#is_no_data_recovery}}`, `{{#is_renotify}}`, `{{#is_unknown}}`, `{{#is_priority 'P1'}}`; `^` negates (`{{^is_alert}}`); `{{else}}` is supported.
- `{{#is_match "<var>.name" "str" ["str2"]}}` = substring match; `{{#is_exact_match ...}}` = exact match, also works with `"value"` and with `""` to test that a tag/attribute is empty or missing.
- State-based blocks cannot be combined (a monitor is in one state at a time) but attribute matches can be nested (e.g. `is_match` inside `is_renotify`).
- **Text or handles outside any conditional block are sent on every state transition**; inside a block only on matching transitions. If you page a handle in an alert block, add the same handle in a recovery block.

Sources: https://docs.datadoghq.com/monitors/notify/variables/#conditional-variables

### Attribute, tag and template variables for log monitors
- **Multi alert (group-by) variables**: grouped by tag -> `{{key.name}}` (e.g. `{{env.name}}`, `{{service.name}}`; tag key with a period -> `{{[dot.key.test].name}}`). Grouped by facet -> `{{@facet_key.name}}` (e.g. `{{@machine_id.name}}`; facet with periods -> `{{[@network.client.ip].name}}`).
- **Matching attribute/tag variables** (from a log that matched the query): `{{log.attributes.key}}` and `{{log.tags.key}}`. Drop the `@`; bracket keys with dots: `{{log.attributes.[error.message]}}`, `{{log.tags.env}}`. Click **{{ Add Variable** to list available variables.
  - If the chosen log lacks the attribute, the variable **renders empty**; do not use these variables for routing with `{{#is_match}}`.
  - With formulas & functions, values come from events of the **first query**.
- **Reserved log variables** `{{log.key}}`: `message`, `service`, `status`, `source`, `span_id`, `timestamp`, `trace_id`, `link`, `host` (e.g. `{{log.service}}`, `{{log.message}}`).
- **`{{log.link}}`** = link to the **Log Explorer scoped on the logs matching the query**.
- **Built-in template variables**: `{{value}}` (breaching value), `{{threshold}}`, `{{warn_threshold}}`, `{{alert_recovery_threshold}}`, `{{warn_recovery_threshold}}`, `{{comparator}}`, `{{first_triggered_at}}`, `{{last_triggered_at}}` (UTC date/time), `{{first_triggered_at_epoch}}`, `{{last_triggered_at_epoch}}` (epoch **milliseconds**), `{{triggered_duration_sec}}`.
  - `first_triggered_at` set on OK -> non-OK; `last_triggered_at` set on any move into a non-OK state (incl. WARN -> ALERT). Renotifications keep the same values if the state did not change.
- **Dynamic links** (dashboards, host map, monitors, logs): e.g. a Log Explorer link around the alert time:
  `https://app.datadoghq.com/logs?from_ts={{eval "last_triggered_at_epoch-10*60*1000"}}&to_ts={{eval "last_triggered_at_epoch+10*60*1000"}}&live=false` (add `service=`, `host=`, `status=` params). Dashboard link: `https://app.datadoghq.com/dashboard/<ID>/<NAME>?from_ts=...&to_ts=...&live=false` or `.../dash/integration/system_overview?tpl_var_scope=host:{{host.name}}`.
- `{{eval "..."}}` supports `+ - * / ^ %` and functions (`humanize_bytes`, `int`, ...); `{{local_time 'last_triggered_at' 'Asia/Tokyo'}}`; `{{urlencode "service.name"}}`; comments `{{!-- --}}`; `{{{{raw}}}}` to print literal braces.
- Variables are **HTML-encoded** by default; use **triple braces** `{{{var}}}` for raw output (keeps `&` in URLs).
- Composite monitor with a log sub-monitor `a`: `{{a.log.message}}`.

Sources: https://docs.datadoghq.com/monitors/notify/variables/, https://docs.datadoghq.com/monitors/guide/template-variable-evaluation/

### Log samples and breaching values in notifications
- When a log monitor triggers, log **samples** or **breaching values** can be added to the notification (Slack, Jira, webhooks, Microsoft Teams, PagerDuty, email):

| Monitor setup | Added to the message |
|---|---|
| Ungrouped Simple-Alert, log count | Up to 10 log samples |
| Grouped Simple-Alert, log count | Up to 10 facet or measure values |
| Grouped Multi Alert, log count | Up to 10 log samples |
| Ungrouped Simple-Alert, measure | Up to 10 log samples |
| Grouped Simple-Alert, measure | Up to 10 facet or measure values |
| Grouped Multi Alert, measure | Up to 10 facet or measure values |

- Logs without a message are not included in samples. **Samples are not shown in recovery notifications.**
- Disable via the checkbox at the bottom of Configure notifications & automations (label depends on grouping). API: `enable_logs_sample` (default `false`).

Sources: https://docs.datadoghq.com/monitors/types/log/#log-samples-and-breaching-values-toplist, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### Renotification and escalation
- Optional; reminds the team a problem is not solved. Configure the **renotify interval**, the states that renotify (**alert, no data, warn**), and optionally a cap (e.g. stop renotifying after 1 occurrence).
- Escalation message: in a `{{#is_renotify}}` block in the main message (**recommended**), in the Renotification message field, or via API `escalation_message`. With an `{{#is_renotify}}` block the original message is also sent, so put only extra details there (use `{{^is_renotify}}` for first-notification-only text).
- API: `renotify_interval` (minutes), `renotify_statuses` (defaults to **`alert` and `no data`** when an interval is set), `renotify_occurrences`, `escalation_message`.
- Attribute/tag variables in a renotification are populated with data available at renotification time; `{{first/last_triggered_at}}` do not change if the state did not change; `{{triggered_duration_sec}}` does.
- Renotify vs auto-resolve: auto-resolve only acts when data stops; renotify is for issues still in progress.

Sources: https://docs.datadoghq.com/monitors/notify/#renotify, https://docs.datadoghq.com/monitors/notify/variables/#triggered-variables, https://docs.datadoghq.com/monitors/guide/monitor_api_options/

### Monitors on log-based metrics vs log monitors
- **Log-based metrics** (Logs > Configuration > Generate Metrics > + New Metric, or **Export > Generate new metric** from Log Explorer analytics) are computed from the **entire ingest stream**, so they include logs later dropped by **exclusion filters**. 10-second granularity, **15 months** retention, billed as **custom metrics**. Count of logs (`*`) or a distribution of a numeric attribute; only logs with timestamps in the past 20 minutes are aggregated; tags only if you add group-by dimensions.
- Alert on them with a **metric monitor** (Monitors > New Monitor > Metric): threshold, change, anomaly, outlier, forecast; window up to 1 month (730 h); cumulative **current month** window is metric-only.
- **Log monitor**: indexed Standard Tier logs only, max 2-day window, can alert on unique counts and measures, can include log samples and `{{log.*}}` variables.
- Choose a log-based metric + metric monitor when: logs are excluded from indexing (or sampled), you need long windows / anomaly detection on long history, or long-term KPIs.
- **Log usage metrics** (free, 15 months): `datadog.estimated_usage.logs.ingested_events` and `...ingested_bytes`, tags `datadog_index`, `datadog_is_excluded`, `service` (+ `status` on ingested_events). Best practices: anomaly monitor on `ingested_events` filtered `datadog_is_excluded:false`, sum by `service`, `datadog_index` for indexing spikes; metric monitor with cumulative month window for month-to-date indexed volume; daily quota: event monitor on `source:datadog datadog_index:* "daily quota reached"` grouped by `datadog_index`, current day window, `above or equal to 1`; alert at 80% of a daily quota.

Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/, https://docs.datadoghq.com/monitors/types/metric/, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/#monitor-log-usage, https://docs.datadoghq.com/monitors/configuration/#cumulative-time-windows

### Watchdog on logs (high level)
- Watchdog is Datadog's AI engine; built in, **no setup**.
- **Log anomaly detection**: ingested logs are analyzed at intake; Watchdog aggregates by detected patterns and `environment`, `service`, `source`, `status`, looking for the **emergence** or a **sudden increase** of **warning or error** logs.
- All log anomalies show as **Watchdog Insights** in the Log Explorer (banner above results, matching search context and role restrictions). Log-specific insight types: **Log Anomaly Detection** and **Error Outliers** (over-represented `key:value` pairs among errors).
- **Severe** anomalies go to the **Watchdog Alert Explorer** and can be alerted on with a **Watchdog monitor** (Monitors > New Monitor > Watchdog; scope by Environment, Alert Category, Team, tags; log anomalies matched on `service`, `source`, `env`). Severe = contains **error logs**, lasts **at least 10 minutes**, significant increase, low **noise** score per service.
- Minimum history for log anomalies: **24 hours**; best with six weeks. An anomaly is `expired` after 48 h ongoing.
- Disable log anomaly detection with the **Log Anomalies** toggle on the Log Management pipelines page.

Sources: https://docs.datadoghq.com/watchdog/, https://docs.datadoghq.com/watchdog/alerts/, https://docs.datadoghq.com/monitors/types/watchdog/, https://docs.datadoghq.com/logs/explorer/insights/

### Managing monitors (context)
- Monitor List (Monitors > Manage): search, bulk Mute, Unmute, Resolve, Delete, Edit Recipients, Edit Tags, Edit Teams, Export to Terraform. Triggered Monitors page shows one row per triggered group (Alert, Warn, No Data).
- **Downtimes** silence alerts and notifications but do **not** stop state transitions; scheduled from Manage Downtimes > Schedule Downtime, by monitor name or monitor tags, plus group scope.
- Permissions: everyone can view monitors; editing needs **Monitors Write** (Admin and Standard roles have it by default); restrict access per team/role/user (Viewer, Muter, Editor). `notify_audit` notifies tagged users when the monitor is changed.

Sources: https://docs.datadoghq.com/monitors/manage/, https://docs.datadoghq.com/monitors/downtimes/, https://docs.datadoghq.com/monitors/configuration/#permissions

## Metric Generation

### Why generate metrics from logs
- Logging without Limits decouples ingestion from indexing. Many logs are mainly useful as telemetry (KPIs, trends over long periods), so storing every one in an index is expensive.
- Log-based metrics are "a cost-efficient way to summarize log data from the entire ingest stream".
- They are computed on **all ingested logs**: even if index exclusion filters (or no matching index, or daily quotas) keep logs out of the Log Explorer, those logs still feed log-based metrics. Excluded logs "are discarded from indexes, but still flow through the Livetail and can be used to generate metrics and archived."
- Resulting metric: datapoints every **10 seconds**, retained **15 months** ("visualize trends and anomalies over all of your log data at 10s granularity for 15 months"). Compare: index retention is typically days; Flex Logs months.
- Typical uses:
  - Long-term KPIs (requests, checkouts, error counts by service) beyond index retention.
  - Cost reduction: generate a metric for a high-volume, low-value log type (for example 200 OK access logs), then exclude those logs from the index with an exclusion filter. Trends keep working from the metric.
  - Tracking excluded patterns: Logging without Limits guide flow = find noisy pattern (Patterns view) > Add Exclusion Filter > create a log-based metric with the same query > anomaly monitor on that metric.
  - Tracking unparsed logs: count metric with query `datadog.pipelines:false`, grouped by ownership dims such as `service` and `team`; then a metric monitor with a quota per `team`. (A Log Explorer query only sees unparsed *indexed* logs; the metric covers non-indexed ones too.)
- Datadog docs scope note: these docs are for cloud logging; on-premises metric generation is in Observability Pipelines (out of scope for this exam).
- Export menu in the Log Explorer lists "Metric" as the way "to aggregate your logs into long term KPIs, as they are ingested in Datadog."
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/, https://docs.datadoghq.com/logs/guide/getting-started-lwl/, https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters, https://docs.datadoghq.com/logs/guide/detect-unparsed-logs/, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/, https://docs.datadoghq.com/logs/explorer/export/

### Where to create one (UI paths)
- **Generate Metrics page**: Logs > Configuration area, URL `/logs/pipelines/generate-metrics`. Steps in the docs: navigate to the Generate Metrics page > select the **Generate Metrics** tab > click **+ New Metric** (LwL guide: "Click New Metric in the top right corner").
- **From the Log Explorer**: build an Analytics search, then **Export** menu > **Generate new metric** (query is carried over).
- Other Export menu items (for distractor awareness): Saved View, Dashboard widget, Notebook widget, Monitor, cURL command, CSV (up to 100,000 individual logs, 300 Patterns, 500 Transactions), Share View.
- API: `/api/v2/logs/config/metrics` (GET list, POST create, GET/PATCH/DELETE `/{metric_id}`). Requires `logs_generate_metrics`.
- Permission: **Logs Generate Metrics (`logs_generate_metrics`)** "Create custom metrics from logs"; default role = **Datadog Standard Role** (not Read Only). Not to be confused with `logs_write_pipelines`, `logs_write_processors`, `logs_write_exclusion_filters`, `logs_modify_indexes`. Parallel permissions exist for other products: `apm_generate_metrics`, `rum_generate_metrics`, `processes_generate_metrics`.
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/#generate-a-log-based-metric, https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/api/latest/logs-metrics/, https://docs.datadoghq.com/account_management/rbac/permissions/#log-management, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/

### Defining the metric (form fields, in order)
1. **Query to filter the log stream** (Define Query)
   - Log Explorer search syntax, e.g. `service:web-store status:info "updating recommendations with customer_id" "url shops"`.
   - Evaluated **against the log stream at ingest time, not against indexed logs**.
   - Does **not** support every Explorer feature: no **full-text search** (`*:search_term`). Search syntax page: full-text syntax cannot be used in "log-based metric filters" (nor index, archive, pipeline, rehydration filters, Live Tail).
   - A query that returns results in the Explorer can still match no logs here. Fix suggested by the docs: rewrite the term as a **quoted phrase**, e.g. `message:"Database operation failed."`, then check the metric in the **Metrics Explorer** before relying on it.
   - Only logs ingested with a **timestamp within the past 20 minutes** are aggregated (late/old-timestamped logs are not counted).
   - Docs also say "Exclude the index from the query" (do not filter on `index:`; the metric works on the ingest stream, before index routing).
   - API key: `filter.query`, default `*`.
2. **Field to track**
   - `*` = **count** of all logs matching the query.
   - A numeric attribute/measure (e.g. `@network.bytes_written`, `@duration`) = **distribution** metric; creates `count`, `min`, `max`, `sum`, `avg` aggregations. If the attribute is a measure facet, the metric value is the attribute value.
   - API: `compute.aggregation_type` = `count` or `distribution` (only these two enum values; no gauge/rate/histogram). `compute.path` (e.g. `@duration`) used only for distribution.
3. **Group by** (dimensions = tags)
   - By default log-based metrics have **no tags** unless explicitly added (no automatic `host`, `env`, `service`).
   - Any attribute or tag in the logs can be a dimension (e.g. `@http.status_code`, `env`). Tag name = attribute/tag name **without the `@`** (group by `@http.status_code` gives tag `http.status_code`), applied in `<KEY>:<VALUE>` format.
   - API: `group_by[].path` (required) and optional `group_by[].tag_name` (by default the path is used as tag name; set e.g. `"tag_name": "status_code"` to rename).
   - Warning: do not group by unbounded / very high cardinality attributes such as timestamps, user IDs, request IDs, session IDs (each tag combination is a billable custom metric).
4. **Percentile aggregations** (distribution only): optional **p50, p75, p90, p95, p99** ("Calculate percentiles" checkbox; API `compute.include_percentiles: true`). Percentile metrics are also custom metrics and billed.
5. **Name** - must follow the custom metric naming convention (see below). API: `data.id` is the metric name; `data.type` is always `logs_metrics`.
- Datapoints generated at **10-second** intervals; on dashboards, `count unique` uses values within that 10-second interval.

API example (create):
```json
{
  "data": {
    "id": "logs.page.load.count",
    "type": "logs_metrics",
    "attributes": {
      "compute": {"aggregation_type": "distribution", "include_percentiles": true, "path": "@duration"},
      "filter": {"query": "service:web-api AND @http.status_code:[200 TO 299]"},
      "group_by": [{"path": "@http.status_code", "tag_name": "status_code"}]
    }
  }
}
```
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/#add-a-new-log-based-metric, https://docs.datadoghq.com/logs/explorer/search_syntax/#full-text-search, https://docs.datadoghq.com/api/latest/logs-metrics/create-a-log-based-metric/, https://docs.datadoghq.com/logs/guide/getting-started-lwl/

### Count vs distribution metrics
- Count: number of matching logs per 10 s interval, per tag combination.
- Distribution: server-side aggregation of raw values (DDSketch), so percentiles are **globally accurate** across all sources. Unlike HISTOGRAM (Agent-side aggregation; default `avg`, `count`, `median`, `95percentile`, `max`).
- Distribution default aggregations: `count`, `sum`, `min`, `max`, `avg`. Optional percentiles p50/p75/p90/p95/p99.
- Use a distribution for latency/size SLIs ("p95 of `@duration` by service"); use a count for event volume ("number of 5xx logs by service").
- A metric name used for a distribution should not be reused for other metric types (overshadowing).
Sources: https://docs.datadoghq.com/metrics/distributions/, https://docs.datadoghq.com/metrics/types/

### Updating a log-based metric (limitations)
- Editable after creation: **stream filter query**, **aggregation groups** (group-by tags, e.g. to cut cardinality), **percentile selection** (check/uncheck Calculate percentiles).
- **Not editable**: metric **type** (count vs distribution) and **name**. To change either, create a **new** metric.
- The `logs_generate_metrics` permission is global and covers creating, editing and deleting log-based metrics.
- Related: log monitors only evaluate indexed logs, which is why excluded patterns are tracked with a log-based metric plus a metric/anomaly monitor.
- No backfill (inferred; the docs do not use the word "backfill"): the metric is computed from the ingest stream as logs arrive (only logs with timestamps within the last 20 minutes); it is not computed from logs already sitting in indexes, so a new metric (or a changed filter) has no history for earlier periods. For past data use Log Explorer analytics on indexed logs.
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/#update-a-log-based-metric

### Billing as custom metrics
- "Metrics created from ingested logs are billed as Custom Metrics." Also percentile metrics.
- Custom metric = unique combination of **metric name + tag values** (including host tag).
- Counting (cardinality-based billing): COUNT/RATE/GAUGE = 1 per tag value combination. DISTRIBUTION = **5 x** tag value combinations (count, sum, min, max, avg). Adding percentiles = another **5 x** combinations, so total **2 x 5 x combos** (e.g. 4 combos: 20 without, 40 with percentiles).
- Billable usage = monthly average of distinct hourly custom metrics; not affected by datapoint frequency or number of queries.
- Allotments: Pro 100, Enterprise 200 custom metrics per host. (Some contracts use Metric Name pricing instead.)
- Metrics without Limits can restrict the tag allowlist (indexed vs ingested custom metrics).
- Users with a Datadog Admin role can see the monthly average number of ingested and indexed custom metrics per hour, plus a top custom metrics table, on the Usage details page.
- Log-based metric percentiles are only p50/p75/p90/p95/p99 in the Generate Metrics form; arbitrary percentiles (for example p99.9) belong to the Metrics Catalog "advanced query" option for distributions, not to the log-based metric form.
Sources: https://docs.datadoghq.com/metrics/custom_metrics/, https://docs.datadoghq.com/account_management/billing/custom_metrics/#counting-custom-metrics, https://docs.datadoghq.com/metrics/metrics-without-limits/

### Metric naming convention
- Must **start with a letter**.
- Only ASCII alphanumerics, underscores `_`, and periods `.`. Other characters (including spaces) are converted to underscores; Unicode not supported.
- Max **200 characters** (fewer than 100 preferred for UI).
- Names are **case sensitive**.
- Valid: `checkout.payment_errors`, `logs.unparsed`. Invalid start: `5xx.errors`.
Sources: https://docs.datadoghq.com/metrics/custom_metrics/#naming-custom-metrics

### Logs usage metrics (free, out of the box)
- Estimated usage metrics, near real time: `datadog.estimated_usage.logs.ingested_events`, `datadog.estimated_usage.logs.ingested_bytes`. Free and kept 15 months.
- Uses: graph estimated usage, monitor it, alert on spikes/drops, assess impact of code changes.
- Tags: `datadog_index` (routing query that matched the log to an index), `datadog_is_excluded` (whether it matched an exclusion query), `service`. Extra `status` tag only on `ingested_events`.
- `N/A` value for `datadog_index` / `datadog_is_excluded` = log was ingested but did not match any inclusion/exclusion criteria to be routed to an index.
- Best practice: anomaly monitor on `ingested_events` with `datadog_is_excluded:false` (indexed volume) summed by `service` and `datadog_index`; set unit `byte` on `ingested_bytes` in the Metrics Catalog.
- Pipelines page also shows per-pipeline estimated usage and links the Logs Estimated Usage dashboard.
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/#logs-usage-metrics, https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/#log-usage-metrics

### Common pitfalls
- Expecting the metric to only count indexed logs (it counts all ingested matches, including excluded).
- Expecting tags to be inherited (none unless grouped).
- Using full-text search `*:term` in the filter (unsupported) or relying on an Explorer-only feature; verify in Metrics Explorer.
- Grouping by `@usr.id`, `@request_id`, session IDs, timestamps (cost explosion).
- Expecting history/backfill or that late logs (timestamp older than 20 minutes) are counted.
- Trying to rename or change type in place (create a new metric instead).
- Forgetting percentiles are billed (5 x combos more).
Sources: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/, https://docs.datadoghq.com/account_management/billing/custom_metrics/

## Exporting

### Log Explorer Export menu
- From the Log Explorer, depending on the current aggregation (list, patterns, transactions, timeseries, top list, table...), you can **export** or **save** the exploration as:
  - **Saved View**: an investigation starting point for yourself or teammates.
  - **Dashboard widget** or **Notebook widget**: for reporting or consolidation.
  - **Monitor**: alert on predefined thresholds (the way to notify stakeholders from a search query).
  - **Metric** (Generate New Metric): aggregate logs into long-term KPIs, computed as logs are ingested (log-based metrics are kept 15 months like other custom metrics).
  - **cURL command**: test the query from the Explorer, then build custom reports with the Datadog Logs API.
  - **CSV**: up to **100,000 logs** at once for individual logs, **300** for Patterns, **500** for Transactions. Timeseries, top list and table views can also be downloaded as CSV.
  - **Share View**: share a link to the current view by email, Slack and other notification integrations.
- **Save to notebook** (single log): from the log side panel select Save to notebook. The log is shown in a reader-friendly format and stays in the notebook **even after the log event ages out of retention**.
- Log side panel Share button: Copy to clipboard (`Ctrl+C` / `Cmd+C`) copies the log JSON; Share Event shares the log plus underlying view via email, Slack, etc.
- The Logs API returns at most **1,000 logs** per call; use pagination for longer lists.

#### CSV export formatting (sanitization)
Datadog sanitizes CSV exports for spreadsheet compatibility, so values/column names can differ from the original logs:
- Removes line breaks (`\n`, `\r\n`, `\r`) without inserting spaces: `foo\nbar` becomes `foobar`.
- Replaces consecutive spaces with a single space.
- Prefixes values starting with formula characters `=`, `+`, `-`, `@`, tab or carriage return with a single quote `'` (prevents formula execution).
- Adds numeric suffixes to duplicate column names, e.g. `message(1)`.
- Encloses values in double quotes and escapes inner double quotes as `""`.
- To get logs **without** these changes: use the **Log Search API** or **Log Archives**.

#### Saved Views (what an exported Saved View holds)
- What a Saved View stores (query + live time range, default visualization, facet subset), default view vs shared views, and the actions: **Domain 3 > Explorer Functionality > Saved views and the default view**.

Sources: https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/logs/explorer/saved_views/, https://docs.datadoghq.com/logs/explorer/side_panel/

### Log Archives: concepts and setup
- Archives forward **all ingested logs, indexed or not** (logs dropped by index exclusion filters or daily quota are still archived) to **your own** cloud storage: **Amazon S3, Azure Storage, Google Cloud Storage**. Purpose: long-term, storage-optimized retention, compliance, auditability; access later through **Rehydration** or **Archive Search**.
- UI: **Logs > Log Archiving & Forwarding** page (`/logs/pipelines/archives`), **Archives** tab, **Add a new archive**.
- Setup steps: (1) set up the cloud provider integration, (2) create a storage bucket, (3) set read and/or write permissions, (4) route logs to/from the archive, (5) advanced settings (encryption, storage class, tags), (6) validate.
- Permission: only users with **Logs Write Archives** (`logs_write_archives`, Datadog Admin role by default) can create, modify, delete or reorder archives and restrict archive read access to roles. (The archives page text calls it the `logs_write_archive` permission but links to `logs_write_archives`, the name on the RBAC permissions page.)
- Metrics for archived logs (including successful retries): `datadog.archives.logs.bytes`, `datadog.archives.logs.count`.
- Archives are also manageable via API: `GET/POST /api/v2/logs/config/archives`, `GET/PUT/DELETE /api/v2/logs/config/archives/{archive_id}`, readers (`/readers` grant/revoke role), order (`GET/PUT /api/v2/logs/config/archive-order`). API body attributes: `name`, `query` (filter), `destination` (`s3` / `azure` / `gcs`), `include_tags`, `compression_method` (`GZIP` or `ZSTD`, default `ZSTD`), `partitioning_attributes`, `lookup_attributes`, `rehydration_max_scan_size_in_gb`, `rehydration_tags`.

#### Integration per cloud
- **S3**: AWS integration for the account holding the bucket, normally via a role Datadog assumes (role delegation). AWS China accounts: access keys as alternative.
- **Azure**: Azure integration with an **App Registration** in the subscription holding the storage account. Azure ChinaCloud and GermanyCloud not supported; Azure GovCloud in Preview.
- **GCS**: Google Cloud integration with a **service account** in the project holding the bucket.

#### Bucket creation pitfalls
- S3: do **not** make the bucket publicly readable. On US1/US3/US5, consider `us-east-1` to limit inter-region transfer fees. On GovCloud S3 FIPS endpoints, bucket names with dots (.) are not supported.
- Azure: storage account with standard performance or Block blobs premium, **hot or cool** access tier; create a **container** (name needed in Datadog). Do **not** set **immutability policies** (Datadog may need to rewrite the last data in rare cases, typically a timeout).
- GCS: choose "Set object-level and bucket-level permissions"; do **not** add a **retention policy** (same rewrite reason).
- GovCloud sites (US1-FED, US2-FED): archiving sends logs outside the Datadog GovCloud environment; Datadog is not responsible for them.

#### Cloud permissions
- **S3 IAM policy** (attach to the Datadog integration role, default name `DatadogIntegrationRole`):
```json
{"Version":"2012-10-17","Statement":[
 {"Sid":"DatadogUploadAndRehydrateLogArchives","Effect":"Allow",
  "Action":["s3:PutObject","s3:GetObject"],
  "Resource":["arn:aws:s3:::<BUCKET>/<OPTIONAL_PATH>/*"]},
 {"Sid":"DatadogRehydrateLogArchivesListBucket","Effect":"Allow",
  "Action":"s3:ListBucket","Resource":["arn:aws:s3:::<BUCKET>"]}]}
```
  - `s3:PutObject` alone is enough to **upload** archives; `s3:GetObject` + `s3:ListBucket` are needed to **search / rehydrate**.
  - Resources for `PutObject`/`GetObject` must **end with `/*`** (object-level); `ListBucket` is on the bucket ARN.
  - Attach: IAM > Roles > Datadog role > Add permissions > Attach policies.
- **Azure**: storage account > Access Control (IAM) > Add > Add Role Assignment > **Storage Blob Data Contributor** for the Datadog app.
- **GCS**: IAM Admin > Edit principal > ADD ANOTHER ROLE > **Storage Object Admin** (recommended for writing). Least-privilege custom role for uploads: `storage.objects.create`, `.get`, `.list`, `.delete` (delete needed for write retries that overwrite objects); `storage.multipartUploads.*` not required.

#### Routing a bucket (Add a new archive)
- Archive filter query: which logs go to this archive (search syntax).
- S3: select AWS account + role, bucket name, optional **prefix** directory.
- Azure: archive type, Azure tenant + client of the Datadog app, **storage account name** and **container name**, optional prefix.
- GCS: archive type, GCS service account, bucket name, optional prefix.
- If the bucket restricts network access by IP, allowlist the **webhook IPs** from the IP ranges list. US3 Azure: firewall rules not supported.

Sources: https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/api/latest/logs-archives/, https://docs.datadoghq.com/logs/log_configuration/indexes/

### Log Archives: advanced settings, ordering, format, validation
- **Datadog tags**: "Include all log tags in your archives" (on by default for new archives in the UI; increases archive size). Needed if you want to filter on tags such as `env:prod` in rehydration queries. Can also **add tags on rehydrated logs** (rehydration tags) to align with Restriction Queries / `logs_read_data`.
- **Maximum scan size** (GB) per archive for Archive Search and Rehydration: users must **estimate scan size** first; if the estimate exceeds the max, reduce the time range.
- **Partition attributes** (up to **2** per archive): low-cardinality fields (`service`, `source`, `env`, `status`); logs co-located by value, non-matching partitions skipped. **Lookup attributes** (up to **2** per archive): high-cardinality IDs (`trace_id`, `@usr.id`, `@http.request_id`, `@transaction_id`); index built at write time. Tags/reserved attributes are entered without `@`, other attributes with `@`. Only logs archived **after** configuring them benefit.
- **Compression**: default **zstd** (`.json.zst`), better ratio and faster decompression, recommended for Archive Search; option **gzip** (`.json.gz`). Changing compression only affects **new** archive files.
- **Storage class / tier**:
  - S3: pick a storage class or use an S3 lifecycle configuration. Archive Search supports only S3 Standard, Standard-IA, One Zone-IA, Glacier Instant Retrieval, and Intelligent-Tiering only if both optional asynchronous archive access tiers are disabled. Others (for example Glacier Flexible Retrieval, Glacier Deep Archive) must be moved first.
  - Azure: archiving and Archive Search support only **Hot** and **Cool** tiers.
  - GCS: Standard, Nearline, Coldline, Archive supported.
- **S3 server-side encryption** (Encryption Type dropdown): *Default S3 Bucket-Level Encryption* (default; Datadog sends no encryption headers, bucket default applies), *Amazon S3 managed keys* (forces SSE-S3), *AWS Key Management Service* (forces SSE-KMS with a customer-managed key; provide the **CMK ARN**; CMK policy must allow the Datadog role `kms:Encrypt/Decrypt/ReEncrypt*/GenerateDataKey*/DescribeKey` and grants).
- **Multiple archives**: a log goes only into the **first archive whose filter matches**; order matters. Example: archive 1 `env:prod`, archive 2 `*` -> prod logs only in archive 1, everything else in archive 2.
- **Format**: compressed **JSON**; path `/<prefix>/dt=<YYYYMMDD>/hour=<HH>/archive_<HHmmss.SSSS>.<UUID>.json.zst` (or `.json.gz`), organized by date and hour. Prefix `/` if none.
- **Validation**: pipelines enrich logs before archiving. After create/update, next upload may take several minutes; **check the bucket after 15 minutes**. If still pending, check that the archive filter is valid and matches logs in **Live Tail**. Upload failures (settings/permission changes) highlight the archive on the config page (hover for error + fix) and generate an **event** in the Events Explorer (you can monitor these events).

Sources: https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/explorer/archive_search/

### Rehydrating from Archives (historical views)
- Log Rehydration captures logs from customer-owned storage-optimized archives back into the search-optimized Log Explorer, to analyze logs that are **old** or were **excluded from indexing**. Datadog now recommends **Archive Search** as the first way to access archived logs (Search & Rehydration mode for full platform access).
- **Historical views**: rehydrate by **time frame + query filter**. Up to **1 billion** log events per historical view. **Index exclusion filters do not apply** to historical views. CSV download of a historical view is limited to the **last 90 days**.
- Prerequisites: an archive (S3, Azure, GCS) with read access: S3 via **role delegation** (IAM role; only role-delegated archives are rehydratable), Azure via Entra ID + Storage Blob Data Contributor, GCS via service account + **Storage Object Viewer** (least privilege: `storage.objects.get`, `storage.objects.list`). S3 rehydration policy: `s3:GetObject` on `<bucket>/*` + `s3:ListBucket` on the bucket.
- Steps: Logs > Log Archiving & Forwarding > **Rehydration** page (`/logs/pipelines/historical-views`) > **New Historical View** > time period > archive > (optional) **Estimate scan size** > name > indexing query > log limit > retention > (optional) notifications with `@handle` > **Rehydrate from Archive**.
  - **Name**: must begin with a lowercase letter; only lowercase letters, numbers and `-` (e.g. `checkout-incident-2026`).
  - **Query**: Log Explorer search syntax; tags in the query (e.g. `env:prod`, `version:x.y.z`) work only if logs were **archived with their tags**.
  - **Log limit**: when reached, reloading stops but already rehydrated logs stay accessible.
  - **Retention**: how long rehydrated logs stay searchable; options depend on contract; **default 15 days**.
- Status: **PENDING** until ready, then **ACTIVE** (query column links to the view in Log Explorer). In Log Explorer: Index facet / index selector > select the **Historical indexes**.
- **Cancel** ongoing rehydration (wrong time range, typo in query): already indexed logs stay queryable until end of retention; **all scanned and indexed logs are still billed**.
- **Delete**: delete icon > confirm; permanently deleted **one day** after deletion is initiated (can cancel deletion meanwhile). Deleted views viewable for up to **1 year** via View dropdown. Otherwise views remain until retention expires.
- **Notifications**: events auto-generated at start and end (Events Explorer). Template variables: `{{archive}}`, `{{from}}`, `{{to}}`, `{{scan_size}}`, `{{number_of_indexed_logs}}`, `{{explorer_url}}`.
- **Settings** (admins with Logs Write Archives): default rehydration **volume limit** (in millions of logs per view; can allow override) and allowed **retention periods** (e.g. 3, 7, 15, 30, 45, 60, 90, 180 days).
- **Scan size**: the query is applied **after** files for the time period are downloaded, so scan size = **total volume in the time window**, not the matching logs. `service:A` still scans `service:B` logs. **Reducing the date range** is the most effective way to cut scan size and cloud transfer costs.
- **RBAC**: `logs_read_archives` (Logs Read Archives, read archive config; can be scoped to specific roles per archive) + `logs_write_historical_view` (Logs Write Historical Views, global; trigger rehydration). Both needed to rehydrate from a given archive. Rehydrated content can be tagged (rehydration tags) so restriction queries apply.

#### Archive Search (related, recommended path)
- Queries archives directly, streaming results in real time, no re-indexing; charged for scan only. **Up to 100,000 logs retained for 24 hours** at no extra cost on a dedicated results page.
- Modes: **Search** (results page only) vs **Search & Rehydration** (full platform access, custom retention, more than 100,000 logs). You can rehydrate before launch or after completion within the 24-hour window. Rehydrated results can go to Standard Indexing or Flex storage.
- Limits: no aggregations/visualizations; results not queryable from Dashboards, Notebooks or Log Explorer unless rehydrated. Query preview downloads a sample of up to 1,000 logs. Running searches can be cancelled (keeps retrieved logs) or duplicated.
- Permissions: Search mode via `logs_archive_search` (named Logs Write Archive Search `logs_write_archive_search` on the RBAC page); both modes via `logs_write_historical_view`; plus `logs_read_archives` per archive. Restriction queries still apply on the results page.
- UI: Logs > Archive Search > New Search.

Sources: https://docs.datadoghq.com/logs/log_configuration/rehydrating/, https://docs.datadoghq.com/logs/explorer/archive_search/, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/, https://docs.datadoghq.com/account_management/rbac/permissions/

### Forwarding logs to custom destinations
- Log Forwarding sends logs **from Datadog** (after Datadog pipelines process/standardize them) to **Splunk, Elasticsearch, HTTP endpoints, Microsoft Sentinel, Google SecOps (Chronicle)**. Any **ingested** log can be forwarded, indexed or not. Format: **JSON**, **GZIP-compressed by default**.
- Permission: `logs_write_forwarding_rules` (Logs Write Forwarding Rules, Admin role) to create/edit/delete destinations.
- Retries: on failure, retries for **2 hours** with exponential backoff; first retry after **1 minute**, delays grow to max **8-12 minutes** (10 min +/-20%).
- Metrics (forwarded incl. retries, and dropped): `datadog.forwarding.logs.bytes`, `datadog.forwarding.logs.count`.
- Setup: allowlist **webhook IPs** (IP ranges list) > Logs > **Log Archiving & Forwarding** > **Custom Destinations** > **New Destination** > filter query (search syntax) > **Destination Type** > configure > **Select Tags to Forward** (All tags / No tags / Specific Tags with Include or Exclude) > **Save**.
  - **HTTP**: name; **Define endpoint** must start with `https://` (e.g. Sumo Logic HTTP Source URL). Optional: disable GZIP if the endpoint does not support compressed payloads. Auth: **Basic Authentication** (username/password) or **Request Header** (e.g. `Authorization: Basic <base64 user:pass>`).
  - **Splunk**: endpoint must start with `https://`, e.g. `https://<account>.splunkcloud.com:8088`; `/services/collector/event` is **appended automatically**; auth = **Splunk HEC token**; **indexer acknowledgment must be disabled**; optional sourcetype (default `_json`, or Send without sourcetype).
  - **Elasticsearch**: `https://` endpoint, **Destination Index Name**, optional **Index Rotation** (`No Rotation` default, Every Hour/Day/Week/Month); username + password.
  - **Microsoft Sentinel**: app registration via the Azure integration; Logs Ingestion Endpoint (DCE), DCR **Immutable ID** (Monitoring Metrics Publisher role on the DCR), Stream Declaration Name (e.g. `Custom-MyTable`).
  - **Google SecOps (Chronicle)**: GCP service account with Chronicle write access; Customer ID, Regional Endpoint, Namespace; Project ID, Private Key ID, Private Key, Client Email, Client ID.
- Status: hover the destination status to see the % of matching logs forwarded in the **past hour**. Edit/Delete via the destination's Edit / Delete (Confirm) buttons; deleting stops forwarding.
- GovCloud: only ports **443 and 8088** open for forwarding; logs leave the GovCloud environment.
- API: `/api/v2/logs/config/custom-destinations` (get all, create, get, update, delete).
- Out of exam scope: Observability Pipelines (forwarding directly from your environment).

Sources: https://docs.datadoghq.com/logs/log_configuration/forwarding_custom_destinations/, https://docs.datadoghq.com/api/latest/logs-custom-destinations/

### Accessing log data programmatically (Logs Search API)
- Requires a Datadog **API key** (`DD-API-KEY`) and an **application key** (`DD-APPLICATION-KEY`); the app-key creator must have permission to the data (`logs_read_data`; OAuth scope `logs_read_data`).
- Search endpoint (v2): `POST https://api.<site>/api/v2/logs/events/search` (also `GET /api/v2/logs/events`). Legacy v1: `POST /api/v1/logs-queries/list` (pagination via `nextLogId` -> `startAt`).
- Body example:
```json
{"filter":{"from":"2026-11-01T00:00:00+00:00","to":"2026-11-01T00:15:00+00:00","query":"service:checkout status:error","indexes":["main"]},
 "sort":"-@pageViews",
 "page":{"limit":1000}}
```
  - `filter.query`: Log search syntax (default `*`). `filter.from` / `filter.to`: ISO-8601, Unix ms timestamp, or date math (`now`, `now-1h`, `-2d`; units `s`,`m`,`h`,`d`); API defaults `now-15m` / `now`. `filter.indexes` default `["*"]`. `filter.storage_tier`: `indexes` (default), `online-archives`, `flex`.
  - **Sort**: `timestamp` = ascending; `-timestamp` / default = descending by timestamp; facet sort with `@` (e.g. `@pageViews` asc, `-@pageViews` desc) per the guide.
  - **Limit**: `page.limit` default **50**, max **1000** logs per response.
  - **Pagination**: take `meta.page.after` from the response and send it as `page.cursor` in the next request (same query). `links.next` gives a ready URL. When `data` is empty/null, all pages are returned. Use **absolute** time ranges when paginating (relative ranges can miss results).
- Response: `data[]` (each `type: "log"`, `id`, `attributes` with `status`, `service`, `tags`, `timestamp`, `host`, `message`, nested custom `attributes`), `meta.page.after`, `links.next`.
- **Aggregate** endpoint: `POST /api/v2/logs/analytics/aggregate` with `compute` (`count`, `cardinality`, `sum`, `avg`, `min`, `max`, `median`, `pc75`...`pc99`; `type` `total` default or `timeseries`), `group_by` (facet, limit up to 10,000 buckets), `filter`.
- Send logs: `POST https://http-intake.logs.<site>/api/v2/logs` (ingestion, API key only).
- Datadog recommends archives, not the log list API, for archiving logs.

Sources: https://docs.datadoghq.com/logs/guide/access-your-log-data-programmatically/, https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination/, https://docs.datadoghq.com/api/latest/logs/

### Common pitfalls
- CSV export is capped (100,000 / 300 / 500) and sanitized; use the API (paginated, 1,000 per page) or archives for raw, complete data.
- Archive filter order: a log lands only in the first matching archive.
- Archives include non-indexed logs; exclusion filters and daily quotas do not stop archiving, and exclusion filters do not apply to historical views.
- Rehydration query filters do not reduce scan size; narrow the time range.
- Tag-based rehydration queries need archives configured to include tags.
- S3 rehydration/Archive Search need role delegation and `GetObject` + `ListBucket`; resources for object actions must end with `/*`.
- Azure: no immutability policies, Hot/Cool tiers only. GCS: no retention policy.
- Splunk forwarding fails if HEC indexer acknowledgment is enabled; do not add `/services/collector/event` yourself.
- Canceling a rehydration does not refund scanned/indexed logs.

Sources: https://docs.datadoghq.com/logs/explorer/export/, https://docs.datadoghq.com/logs/log_configuration/archives/, https://docs.datadoghq.com/logs/log_configuration/rehydrating/, https://docs.datadoghq.com/logs/log_configuration/forwarding_custom_destinations/

# Domain 6: Log Troubleshooting

## Ingestion Issues

Troubleshooting "my logs are missing / wrong" in Datadog Log Management. Work out WHERE the log stops: at the source (Agent/forwarder never sends it), at intake (dropped, truncated), in processing (wrong time, wrong status, unparsed), or at indexing/access (excluded, quota, restriction query). The quickest split is **Live Tail**: if the log is in Live Tail it reached Datadog, so the problem is indexing or access, not collection.

### Triage flow: where did the log go?

| Symptom | Most likely cause | Where to look |
| --- | --- | --- |
| Not in Live Tail, not in Explorer | Never sent (Agent config, permissions, network, site/API key) or dropped at intake (timestamp older than 18 h) | `datadog-agent status` (Logs Agent section), `/var/log/datadog/agent.log`, `datadog.estimated_usage.logs.drop_count` |
| In Live Tail, missing from Log Explorer | Index exclusion filter, index filter matches no index, daily quota reached | Indexes page (exclusion filters, order, filters), Event Explorer `datadog_index:<index>`, estimated usage metrics with `datadog_index` / `datadog_is_excluded` tags |
| Missing for today only, no config change | Daily quota reached | Log Explorer bar graph shows "daily quota reached"; Event Explorer `datadog_index:{index_name}` |
| You see no logs at all but teammates do | Your role is part of a restriction query (or Legacy Permissions limit indexes) | Ask a Datadog admin; Data Access page (Logs > Configuration > Data Access) |
| Log present but cut off | Over 1 MB at intake (truncated), or indexed field truncation (75 KiB message / 25 KiB other fields) in grouped views | `datadog.estimated_usage.logs.truncated_count`, `...truncated_bytes` |
| Wrong time / shifted hours | Timezone of raw timestamp, missing date remapper, unsupported date format, user display time zone | Preferences > Time zone, Grok `date()` matcher `timezone` param, Log Date Remapper |
| Status shows Info for warnings/errors | Default status is `INFO`; real level not remapped | Grok `word()` + Log Status Remapper, or Preprocessing for JSON logs status list |
| No attributes in the side panel | Log not parsed by any pipeline | `datadog.pipelines:false`, Patterns, custom pipeline or integration `source` |

- Logging Without Limits decouples ingestion from indexing: exclusion filters that are too broad exclude more than intended. Parsed and unparsed JSON logs can match index filters in unexpected ways, especially with free-text search on short strings.
- **Estimated Usage Metrics**: if logs seem not indexed or at the wrong rate, check the Log Management estimated usage dashboard. Tags: `datadog_index`, `datadog_is_excluded`, `service`, `status`. Example metric: `datadog.estimated_usage.logs.ingested_events` (includes excluded logs).
  - `datadog_index:N/A` on a datapoint = those logs match **no index** in the org; review index order and filter queries.
  - Estimated Usage Metrics **do not respect daily quotas** (they keep counting after a quota is hit).
- Missing logs, data access: role part of a **restriction query** (Logs RBAC "Logs Read Data" + Data Access page). **Legacy Permissions** can also limit Log Explorer access to specific indexes or to a single index at a time.
- Log shows a trace ID but trace is missing: logs and traces are sampled independently; not a config error (cross-product, low exam priority).

Sources: https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/

### Agent configuration checklist (logs not leaving the host)

Common config issues to triple-check (Log Collection Troubleshooting Guide):
1. `api_key` is defined in `datadog.yaml` (and it is the API key of your Datadog org).
2. `logs_enabled: true` is set in `datadog.yaml` (default is `false`; container env var `DD_LOGS_ENABLED=true`).
3. By default the Agent collects **no** logs: at least one `.yaml` file in `conf.d/` must contain a `logs:` section with the right values (for example `conf.d/<CUSTOM_LOG_SOURCE>.d/conf.yaml`).
4. YAML parsing errors: YAML is finicky, validate the file.
5. **Restart the Agent** after any config change: changes in `datadog-agent` configuration are not taken into account until restart.
6. **No new logs written**: the Agent only collects logs written **after** it started tailing/listening. Default `start_position` for files is `end`; `beginning` does not support wildcard paths; a stored offset takes precedence over `beginning`/`end` (use `forceBeginning`/`forceEnd` to override).

```yaml
# /etc/datadog-agent/datadog.yaml
api_key: <DATADOG_API_KEY>
site: datadoghq.eu        # must match your org's site; default datadoghq.com
logs_enabled: true
```

```yaml
# /etc/datadog-agent/conf.d/myapp.d/conf.yaml
logs:
  - type: file
    path: /var/log/myapp/*.log
    service: myapp
    source: go
```

Agent Troubleshooting checklist (general):
- Agent container stops right after starting: can be a hostname detection issue.
- Host connected to the internet, or through a proxy? If proxy, is the Agent configured for it?
- API key in `datadog.yaml` corresponds to your Datadog platform (Organization Settings > API Keys).
- **Site** in `datadog.yaml` matches your org. Default site is US1 `datadoghq.com` (`app.datadoghq.com`). Set `site:` or `DD_SITE` (for example `datadoghq.eu`, `us3.datadoghq.com`, `us5.datadoghq.com`, `ap1.datadoghq.com`).
- Only **one** Datadog Agent running on the host.
- Restarted the Agent after editing a yaml file?
- Then run `status`, read the Agent logs, enable debug mode, and if still stuck contact support with a flare.

Config file locations: Linux/AIX `/etc/datadog-agent/datadog.yaml`, checks in `/etc/datadog-agent/conf.d/`; macOS `/opt/datadog-agent/etc/datadog.yaml`; Windows `%ProgramData%\Datadog\datadog.yaml` (`C:\ProgramData\Datadog\conf.d`).

Sources: https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/agent/troubleshooting/, https://docs.datadoghq.com/agent/troubleshooting/site/, https://docs.datadoghq.com/agent/logs/, https://docs.datadoghq.com/agent/configuration/agent-configuration-files/

### Agent commands for log troubleshooting

Sub-command CLI: `<AGENT_BINARY> <SUB_COMMAND> <OPTIONS>`; `<AGENT_BINARY> --help` lists sub-commands.

| Subcommand | What it does |
| --- | --- |
| `status` | Agent status and enabled integrations; has a **Logs Agent** section |
| `configcheck` | Print all configurations **loaded & resolved** of a running Agent |
| `check <CHECK_NAME>` | Run the specified check (Linux: `sudo -u dd-agent datadog-agent check <CHECK_NAME>`, `--check-rate` to include rate metrics) |
| `stream-logs` | Stream the logs being processed by a running Agent |
| `flare` | Collect a flare and send it to Datadog support |
| `diagnose` | Execute connectivity diagnosis |
| `config` | Runtime configuration management (`config list-runtime`, `config get <SETTING>`, `config set log_level debug`) |
| `health` | Print current Agent health |
| `hostname` | Print the hostname used by the Agent |
| `restart-service` / `start-service` / `stopservice` | Windows only (service control manager) |
| `launch-gui` | Start the Agent GUI |

Platform forms of status: Linux `sudo datadog-agent status`; Docker `sudo docker exec -it <CONTAINER_NAME> agent status`; Kubernetes `kubectl exec -it <POD_NAME> -- agent status`; Windows `& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" status`; Cluster Agent `datadog-cluster-agent status`. Service-level status on Linux source installs: `sudo service datadog-agent status`; systemd: `sudo systemctl status datadog-agent`, `sudo journalctl -u datadog-agent.service`.

**Reading the Logs Agent section of `status`:**
```text
==========
Logs Agent
==========
    Reliable: Sending compressed logs in HTTPS to agent-http-intake.logs.datadoghq.com on port 443
    BytesSent: ...
    LogsProcessed: 604328
    LogsSent: 60431
  ============
  Integrations
  ============
  myapp
  -----
    - Type: file
      Path: /var/log/myapp/*.log
      Service: myapp
      Source: go
      Status: OK
        1 files tailed out of 1 files matching
      Inputs: /var/log/myapp/app.log
```
- `Logs Agent is not running` = log collection is not enabled in the Agent (`logs_enabled`).
- No Integrations and `LogsProcessed: 0` / `LogsSent: 0` = logs enabled, but no source/container selected for collection.
- The transport line shows HTTPS vs TCP and the intake endpoint and port.
- Permission errors appear per source: "The file does not exist", "Access is denied", "Could not find any file matching pattern `<path>`, check that all its subdirectories are executable".
- "N files tailed out of M files matching" with N < M points to the open files limit.
- Docker: "The log file tailer could not be made, falling back to socket" = Agent cannot read `/var/lib/docker/containers` (mount `-v /var/lib/docker/containers:/var/lib/docker/containers:ro`).
- Clocks section shows **NTP offset**; the NTP docs tie a significant offset to incorrect alert triggers, metric delays and gaps in metric graphs (outbound UDP 123 must be allowed for NTP).

**configcheck**: shows `Configuration provider`, `Configuration source` (for containers the container ID), and `Log Config` applied from Autodiscovery, for example `[{"service":"example-service","source":"example-source"}]`. With `logs_config.container_collect_all` and no unique config, it shows `[{}]`.

**stream-logs**: prints each log the Agent sees in real time, with integration name, type, status, timestamp, hostname, service, source, tags and message. Filters: `--name` (Kubernetes `Namespace/Pod Name/Container`, names found in `agent status` Integrations list), `--service`, `--source`. `Ctrl + C` to exit. Example: `kubectl exec -it <AGENT_POD> -- agent stream-logs --name default/my-pod/my-container`.

**Runtime config** (Agent 6.19+/7.19+): `datadog-agent config set log_level debug` changes some settings without restart; changes do **not** persist (lost at restart). `config list-runtime` lists editable params.

Sources: https://docs.datadoghq.com/agent/configuration/agent-commands/, https://docs.datadoghq.com/containers/troubleshooting/log-collection/, https://docs.datadoghq.com/agent/troubleshooting/agent_check_status/, https://docs.datadoghq.com/agent/troubleshooting/config/, https://docs.datadoghq.com/agent/troubleshooting/ntp/

### Agent's own logs, debug mode and flares

- Agent log directory: Linux/AIX `/var/log/datadog/`; macOS Agent 7.28+/6.28+ `/opt/datadog-agent/logs`; Windows `C:\ProgramData\Datadog\logs`.
- Files: `agent.log`, `process-agent.log`, `trace-agent.log`, `system-probe.log`, `jmxfetch.log` (>= 7.24), `dogstatsd.log` (>= 7.46).
- Check for errors: `sudo grep -i error /var/log/datadog/agent.log`.
- Rotation: rollover every **10MB** by default, **one** backup kept (`agent.log.1`, overwritten on next rollover). Settings `log_file_max_size` (default 10485760 bytes) and `log_file_max_rolls` (default 1).
- Install logs: Linux `$(pwd)/ddagent-install.log`, macOS `/tmp/dd_agent.log`, Windows `%TEMP%\MSI*.LOG`.
- Agent logging permission issue (`Permission denied: '/var/log/datadog/...'`): the log files and directory must be owned by `dd-agent`: `sudo chown -R dd-agent:dd-agent /var/log/datadog/` then restart. `/opt/datadog-agent/run` must also be owned by `dd-agent`.
- **Debug mode**: default Agent log level `INFO`. Set `log_level: DEBUG` in `datadog.yaml` (uncomment), restart, wait a few minutes. Container: `DD_LOG_LEVEL=debug`; Helm `logLevel: DEBUG`. Runtime (6.19+/7.19+): `agent config set log_level debug` (not possible for the trace-agent container: redeploy). Levels: `OFF`, `CRITICAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`; `'OFF'` must be quoted. Enable DEBUG only for a limited window, then set back to INFO.
- **Flare**: gathers the Agent's configuration files and logs into an archive; removes sensitive info (passwords, API keys, proxy credentials, SNMP community strings); prompts for confirmation before upload. `sudo datadog-agent flare <CASE_ID>` (Linux), `docker exec -it dd-agent agent flare <CASE_ID>`, `kubectl exec -it <AGENT_POD_NAME> -- agent flare <CASE_ID>`, Windows `agent.exe flare <CASE_ID>`. Without a case ID, enter your email to create a new case. Can also be sent from **Fleet Automation** (needs Remote Configuration): select Agent > **Support** > **Send Support Ticket** > **Send Ticket** (optionally enable Debug mode). Manual submission: archive is first written in local `/tmp`. Not supported via `flare` command or Fleet on US1-FED/US2-FED (`ddog-gov.com`): manual only.
- Support ticket for missing logs: raw log sample (text file or raw JSON); if in Live Tail but not Explorer, the **Get All Indexes** API response; if sent by the Agent and nowhere in the UI, an **Agent flare**; for other sources (Lambda Forwarder, Kinesis Firehose) details of the originating source.

Sources: https://docs.datadoghq.com/agent/configuration/agent-log-files/, https://docs.datadoghq.com/agent/troubleshooting/debug_mode/, https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/, https://docs.datadoghq.com/agent/troubleshooting/permissions/, https://docs.datadoghq.com/logs/troubleshooting/

### File permissions (Agent cannot read the file)

- The Agent does **not** run as root (and running as root is not recommended). Default Agent user: Linux/macOS `dd-agent` (the troubleshooting guide's table lists `datadog-agent`; most other pages, commands and the official example use `dd-agent`), Windows `ddagentuser`.
- The Agent needs **read + execute** on every directory in the path (execute to traverse, read+execute to list files for wildcards) and **read** on the file.
- Linux diagnosis: `namei -m /path/to/log/file` shows mode of each path element. Fix: `sudo chmod o+rx /path/to/logs`, or `chmod 755 <folder>` + `chmod 644 <file>`.
- Log rotation can reset permissions: set permissions as `644` in the log rotation config (for example `create 644 mysql adm`) so the Agent keeps read access after rotate.
- **ACLs** (Linux): verify ACLs with `getfacl` / `setfacl -m u:dd-agent:rx /var/log/test-dir`.
  - `setfacl -m u:dd-agent:rx <dir>` alone applies only to the directory, not existing files.
  - `setfacl -R -m u:dd-agent:rx /var/log/apache` = recursive, covers existing files.
  - `setfacl -R -d -m u:dd-agent:rx /var/log/apache` = default ACL, inherited by files created later (including by rotation). Run both.
  - When a default ACL does not apply (for example `copytruncate`), add a logrotate `postrotate` script with `/usr/bin/setfacl -m u:dd-agent:rx <file>` (for example in `/etc/logrotate.d/dd-agent_ACLs`); avoid duplicate logrotate entries (`error: duplicate log entry for <FILE>`).
  - No ACLs: use group-based access / world-readable `create 644` in logrotate.
- Heightened-permission files (syslog, journald): options are (not recommended) root, change file permissions (`chmod 755` dir, `chmod 644` file), or use a root-privileged shipper (Rsyslog, Syslog-ng, NXLog, FluentD, Logstash) sending to Datadog or to the local Agent.
- **Windows**: `icacls path\to\logs /t` to inspect; grant with `icacls "path\to\folder" /grant "ddagentuser:(OI)(CI)(RX)" /t`. `(OI)(CI)` inheritance makes future (rotated) files inherit permissions. PowerShell alternative: `Get-Acl` / `FileSystemAccessRule("ddagentuser","ReadAndExecute","Allow")` / `Set-Acl`. Then `agent.exe restart-service` and `agent.exe status`.
- **Journald**: journal files are readable by the `systemd-journal` group; add the Agent user: `usermod -a -G systemd-journal dd-agent`. If permissions are wrong, journald sends an **empty payload**, so there is no explicit error message.
- **Docker socket** (host-installed Agent): `usermod -a -G docker dd-agent` to fix "permission denied ... /var/run/docker.sock"; a host Agent cannot read `/var/lib/docker/containers` (root only), so it collects from the socket.

Sources: https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/, https://docs.datadoghq.com/logs/guide/setting-file-permissions-for-rotating-logs/, https://docs.datadoghq.com/logs/guide/custom-log-file-with-heightened-read-permissions/, https://docs.datadoghq.com/integrations/journald/, https://docs.datadoghq.com/containers/troubleshooting/log-collection/

### Files not tailed: open files limit and wildcards

- `logs_config.open_files_limit` in `datadog.yaml` = max number of log files the Agent tails **simultaneously**. Exists to prevent performance issues when wildcards hit huge directories. Container env var: `DD_LOGS_CONFIG_OPEN_FILES_LIMIT`. Default varies by Agent version and OS (see example config files). Raising it may increase Agent resource use.
```yaml
logs_config:
  open_files_limit: 500
```
- When more files match than the limit: default `file_wildcard_selection_mode: by_name` sorts filenames in **reverse lexicographic order** (newer timestamps / higher numbers first). `by_modification_time` (Agent 7.40.0+) tails the most recently modified files first, but is less performant and increases disk I/O.
- Example: limit 500, 700 matches: `by_name` tails app.log.700 to app.log.201; `by_modification_time` tails the 500 most recently written.
- Wildcards: `path: /var/log/myapp/*.log`; `exclude_paths` (Agent >= 6.18) to skip files; path values are **case sensitive**; recursive `**` needs `logs_config.enable_recursive_glob: true` (Agent 7.76.0+, off by default).

Sources: https://docs.datadoghq.com/logs/guide/increase-number-of-log-files-tailed/, https://docs.datadoghq.com/agent/logs/advanced_log_collection/#tail-directories-using-wildcards

### Network: transport, ports, proxy

- Default transport is **compressed HTTPS** on port **443** (Agent v6.19+/v7.19+). The HTTPS connectivity test runs **only at startup**: if it fails, or there was no connectivity at start, the Agent uses TCP and does not change until the next restart. Check the transport line in `status`. Batch limits, `batch_wait`, `compression_level`: **Domain 2 > Enabling Log Collection > Transport, compression, limits**.
- Enforce HTTPS: `logs_config.force_use_http: true` (env `DD_LOGS_CONFIG_FORCE_USE_HTTP=true`; transport page also lists `DD_LOGS_CONFIG_USE_HTTP=true`). Enforce TCP: `logs_config.force_use_tcp: true`. **Always enforce a specific transport when using a proxy.**
- TCP log collection is **not supported** (no delivery guarantee). Legacy TCP: US1 `agent-intake.logs.datadoghq.com:10516`; EU port 443; no TCP endpoint on US3, US5, AP1, AP2, UK1, US1-FED, US2-FED.
- Firewall: allow outbound TCP 443 for logs over HTTPS; use `https://ip-ranges.<site>` (`logs` section) for IP inclusion lists. NTP uses UDP 123.
- **Proxy** (HTTPS logs use the same proxy settings as other data):
```yaml
proxy:
  http: http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>
  https: http://<USER>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>
  no_proxy:
    - <HOST_TO_BYPASS>
no_proxy_nonexact_match: true
logs_config:
  force_use_http: true
```
  Env vars: `DD_PROXY_HTTP`, `DD_PROXY_HTTPS`, `DD_PROXY_NO_PROXY` (space-separated), `DD_NO_PROXY_NONEXACT_MATCH`; env vars override the file. Restart after changes. Squid recommended; HAProxy/NGINX not recommended (must maintain Datadog domain lists). A SOCKS5 proxy (`logs_config.socks5_proxy_address`) enforces TCP. TCP proxy: `logs_config.logs_dd_url` + `logs_no_ssl`.

Sources: https://docs.datadoghq.com/agent/logs/log_transport/, https://docs.datadoghq.com/agent/configuration/proxy/, https://docs.datadoghq.com/agent/configuration/network/, https://docs.datadoghq.com/logs/log_collection/#logging-endpoints, https://docs.datadoghq.com/agent/logs/proxy/

### Dropped and truncated logs (intake limits)

- **Timestamp window**: logs with an official date more than **18 hours in the past** are **dropped at intake** (not even visible in Live Tail). Date remapper doc: events can be submitted up to 18 h in the past and **2 hours in the future**. A Preview allows up to 7 days in the past. Find impacted `service`/`source` with `datadog.estimated_usage.logs.drop_count` ("total number of events dropped during ingestion"). Fix at the source.
- JSON logs not appearing via the Forwarder: an attribute parsed as timestamp must be current and in the correct format.
- **Truncation**: logs above **1MB** are truncated; check `datadog.estimated_usage.logs.truncated_count` and `datadog.estimated_usage.logs.truncated_bytes`. HTTPS API accepts up to 1MB per log; recommended size <= 25 KB; the Agent splits a log at **900 KB**.
- **Indexed field truncation**: for indexed logs, values are truncated to **75 KiB** for `message` and **25 KiB** for other fields. Full text is stored and visible in list queries; the truncated version shows in grouped queries (group by that field).
- Other per-log limits (tags, attributes, nesting, null values): **Domain 1 > Logging Formats > Log size and attribute limits**.
- **Kinesis Firehose**: intake limit **65,536 events per batch**; Datadog recommends Kinesis buffer size **2 MiB**; lower the buffer size to reduce events per batch, otherwise logs may be dropped.

Sources: https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/log_collection/, https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/, https://docs.datadoghq.com/account_management/billing/usage_metrics/, https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/

### Indexed? Exclusion filters, daily quota, access

- Live Tail shows logs after processing but before indexing; if in Live Tail and not Explorer, check the Indexes page for **exclusion filters** and index filters/order.
- **Daily quota**: once reached, logs are no longer indexed but still go to Live Tail, archives and log-based metrics. Log Explorer shows a "daily quota reached" message on the bar graph. Verify historical quota hits in the **Event Explorer** with tag `datadog_index:{index_name}`. Default reset 2:00pm UTC; warning threshold minimum 50%; quota changes take effect immediately.
- Lambda forwarder guide lists the three reasons for "in Live Tail but not in Explorer": exclusion filters, daily quota exceeded, timestamp older than 18 hours.

Sources: https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/log_configuration/indexes/#set-daily-quota

### Wrong timestamp
- By default the intake generates a timestamp at reception and appends it as a date attribute. Timestamps are **stored in UTC** and **displayed in the user's local time zone**. First check **Preferences > Time zone**.
- Epoch timestamps are parsed as UTC by default; logs from New York (UTC-5) can appear 5 h in the past, Australia (UTC+10) 10 h ahead.
- Raw logs: Grok Parser with `date()` matcher into an attribute, then **Log Date Remapper** (Add Processor > Date remapper > add attribute in "Set date attribute(s)" > Create). Parsing a date does **not** set the official date by itself.
- Timezone fix: add `timezone` param to the date matcher, for example `%{date("yyyy-MM-dd HH:mm:ss","UTC+1"):date}`.
- JSON logs: add a custom date attribute (for example `mytimestamp`) **first** in the **Preprocessing for JSON logs** date list. Near misses (epoch seconds, epoch nanoseconds) are not recognized and may be dropped: epoch seconds -> remove `timestamp` from the list, Arithmetic Processor `* 1000`, Log Date Remapper; custom format -> Grok parser with **Extract from** `mytimestamp`, then date remapper.
- Multiple date remappers on a log: the **last** one in pipeline order wins. Pipeline changes affect **new logs only**. Formats, defaults and timezone syntax: **Domain 1 > Logging Formats > Timestamps and date formats**.
- Agent-side: the NTP docs list incorrect alert triggers, metric delays and metric graph gaps as offset symptoms (Clocks section of `status`); they do not describe log timestamp effects, so fix log time issues with the steps above.
Sources: https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/, https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/logs/log_configuration/processors/log_date_remapper/, https://docs.datadoghq.com/logs/log_configuration/pipelines/#preprocessing, https://docs.datadoghq.com/logs/log_configuration/parsing/#parsing-dates

### Wrong status (Info for warnings or errors)
- By default the intake assigns status `INFO` (appended as `status`).
- Raw logs: Grok `word()` matcher into a custom attribute, for example `MyParsingRule %{word:log_status}: %{word:user.name} %{word:action}.*` on `WARNING: John disconnected on 09/26/2017`, then **Log Status Remapper** (Add Processor > Status remapper > "Set status attribute(s)" `log_status` > Create).
- JSON logs: `status` is a reserved attribute. Default status attributes: `status`, `severity`, `level`, `syslog.severity`. Add a custom one (for example `logger_severity`) in **Preprocessing for JSON logs** and place it **first**.
- Status mapping (`f*` -> emerg, `w*` -> warning, `s*` -> OK, unknown -> info): full table in **Domain 1 > Log severity levels and Datadog status**.
- Multiple status remappers: only the **first** in pipeline order counts, and across all matching pipelines only the first status remapper encountered applies (opposite of date remapper). New logs only after changes.
Sources: https://docs.datadoghq.com/logs/guide/logs-show-info-status-for-warnings-or-errors/, https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/

### Unparsed logs

- Single log: open it; the **Event Attributes** panel shows a message that no attributes were extracted.
- Many logs: query `datadog.pipelines:false` in the Log Explorer = indexed logs without custom attributes after pipeline processing. **Patterns** view aggregates common formats to kickstart custom pipelines.
- Fix: custom pipeline, or set `source` to an integration name so the integration pipeline applies automatically.
- Track non-indexed logs too: log-based metric (for example `logs.unparsed`) on `datadog.pipelines:false`, group by owner dimensions (`service`, `team`), then a metric monitor as a per-team quota.
- Parsing issue investigation: identify the log's pipeline (integration pipelines filter on `source`, so check `source`), clone integration pipelines to troubleshoot, compare with samples (timestamp format often the culprit), remove attributes from the end of the rule and add `.*` to find the culprit.
- JSON `host`/`hostname`/`syslog.hostname` attributes override the Agent hostname via preprocessing, so logs miss host-level tags; query `@host:* OR @hostname:* OR @syslog.hostname:*`.

Sources: https://docs.datadoghq.com/logs/guide/detect-unparsed-logs/, https://docs.datadoghq.com/logs/faq/how-to-investigate-a-log-parsing-issue/, https://docs.datadoghq.com/containers/troubleshooting/log-collection/

### Duplicates

- Lambda: the Datadog Lambda Extension enables log collection by default. When migrating from the Forwarder to the Extension, **remove the log group subscription** to the Forwarder or you get duplicate logs.
- To stop Forwarder collection for a function: remove the subscription filter from the function's CloudWatch log group. Extension: `DD_SERVERLESS_LOGS_ENABLED=false` (or `enableDDLogs: false`).
- General: only one Agent per host (checklist item).

Sources: https://docs.datadoghq.com/serverless/aws_lambda/troubleshooting/, https://docs.datadoghq.com/serverless/aws_lambda/logs/

### Lambda Forwarder and cloud forwarding basics

1. Are logs reaching Datadog? Use **Live Tail** filtered by `source:lambda`, `source:aws`, `source:s3`, `source:cloudwatch`, or the `forwardername` tag (`forwardername:*`, `forwardername:<FUNCTION_NAME>`), which the Forwarder adds to every log.
2. In Live Tail but not Explorer: exclusion filters, daily quota, timestamp older than 18 h. Not in Live Tail: not reaching Datadog.
3. Permissions: the Forwarder uses a **resource-based policy** (not the Datadog integration role) to allow log sources to invoke it: `aws lambda get-policy --function-name <FUNCTION_NAME>`; Action/Resource must exactly match the Forwarder docs.
4. AWS console **Monitoring** tab: invocations, errors, logs. No invocations = trigger problem. Datadog metrics tagged `functionname`: `aws.lambda.invocations`, `aws.lambda.errors`, `aws.lambda.duration`, `aws.lambda.throttles`.
5. Triggers (CloudWatch Logs or S3): S3 bucket Properties > Events or `aws s3api get-bucket-notification-configuration --bucket <BUCKET>`; CloudWatch log group "Subscriptions" or `aws logs describe-subscription-filters --log-group-name <LOG_GROUP>`. Log group delivery metrics (tag `log_group`): `aws.logs.incoming_log_events`, `aws.logs.forwarded_log_events`, `aws.logs.delivery_errors`, `aws.logs.delivery_throttling`.
6. Automatic triggers failing: Forwarder ARN in the AWS integration **Log Collection** tab; required permissions on the integration role; Lambda log group source needs the extension; CloudWatch log group must not already have **two subscribers** (the maximum).
7. Forwarder's own logs: "View logs in CloudWatch", search `?ERROR ?Error ?error`; set `DD_LOG_LEVEL=debug` on the Forwarder temporarily (verbose; disable afterwards). `INCLUDE_AT_MATCH` / `EXCLUDE_AT_MATCH` filters can drop logs; if both match, the log is **excluded**. Debug logs show whether logs were discarded by the filter.
8. Forwarder `DD_SITE` must match your site; API key via `DD_API_KEY`, `DD_API_KEY_SECRET_ARN`, `DD_API_KEY_SSM_NAME`, or `DD_KMS_API_KEY`. S3 files with a JSON array are ingested as one event. Lambda function debug: `DD_LOG_LEVEL=debug` on the function too. Serverless flare: `datadog-ci lambda flare -f <function_arn> -e <email> -c <case_id> --with-logs`.
9. Lambda extension: logs enabled by default; filter START/END with `DD_LOGS_CONFIG_PROCESSING_RULES` `exclude_at_match` `(START|END) RequestId`; keep `REPORT` logs.

Sources: https://docs.datadoghq.com/logs/guide/lambda-logs-collection-troubleshooting-guide/, https://docs.datadoghq.com/logs/guide/forwarder/, https://docs.datadoghq.com/serverless/aws_lambda/troubleshooting/, https://docs.datadoghq.com/serverless/aws_lambda/logs/

### Container quick hits

- Agent only collects container logs when log collection is enabled and either `logs_config.container_collect_all` (default false) or Autodiscovery labels/annotations select the container; also respects container include/exclude rules; Agent only collects from containers on its own node.
- Run commands against the Agent pod **on the same node** as the app container.
- Docker logs read from file by default (6.33/7.33+); `DD_LOGS_CONFIG_DOCKER_CONTAINER_USE_FILE=false` disables; split lines: check Docker uses the `json-file` driver.
- New hosts: host tags can take minutes to be inherited; `DD_LOGS_CONFIG_EXPECTED_TAGS_DURATION` makes the Agent attach host tags for a period. New containers: `DD_LOGS_CONFIG_TAGGER_WARMUP_DURATION` (seconds, default 0).
- Short-lived Jobs: Agent looks for new containers every 5 s; with `ttlSecondsAfterFinished` keep at least 15 s.

Sources: https://docs.datadoghq.com/containers/troubleshooting/log-collection/
