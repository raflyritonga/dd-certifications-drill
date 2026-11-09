# Datadog APM & Distributed Tracing Fundamentals — Study Notes

Built from the APM & Distributed Tracing Fundamentals exam guide (2025 edition, file dated August 2025), the official practice questions, and the Datadog docs pages behind each subdomain. Every fact was re-checked against the live docs in November 2026. Each section ends with a Sources line listing the pages it came from.

# The exam guide

## What the exam covers
- The APM & Distributed Tracing Fundamentals certification exam is for people who can show an overall knowledge of Datadog's APM & Distributed Tracing tools, **independent of a specific job role**.
- Topics it tests (from the guide's introduction):
  - Understand different tracing architectures
  - Understand automatic and dynamic instrumentation methods
  - Understand and implement manual instrumentation
  - Understand how to use APM features: Services, Search Syntax, Live Search vs Retained Search, Profiles, Deployment Tracking, Error Tracking, Span Summary
  - Visualize insights using Service Performance Dashboards and Trace Metrics
  - Troubleshoot applications using Trace Search (during incidents) and Monitors & Alerting
- Each exam allows a **maximum seat time of 2 hours**.

## Intended candidates
- Ideal candidates have **a minimum of six months of hands-on experience** with Datadog's APM & Distributed Tracing product and its related features, and understand how APM works and how it is best used in production.
- Recommended Datadog knowledge (the guide's list):
  - General Application Performance Monitoring (APM)
  - Datadog APM setup and use
  - Datadog tracing libraries
  - Instrumentation Types
  - Trace/Log Correlation
  - Datadog APM: Services, Search Syntax, Live Search vs Retained Search, Trace Search, Flame Graphs, Profile Collection, Deployment Tracking, Error Tracking, Monitors and Alerting, Span Summary

## Exam format and scoring
| Item | Value |
|---|---|
| Total questions | **90** multiple-choice |
| Scored questions | **75** (count toward the final score) |
| Pre-test questions | **15**, unscored, not identified to the candidate |
| Seat time | 2 hours maximum |
| Unanswered questions | Scored as incorrect, so answer everything |

- **Pre-test items**: Datadog collects candidate performance on the 15 pre-test questions to evaluate them for use on future exam forms. They do not affect your score and look like any other question.
- The guide does not publish a passing score or domain weights.

## Question type
- Only one type: **multiple choice** with **one correct response** and **two or more incorrect responses (distractors)**.
- Pick the response that **most accurately** answers the question. Distractors are designed to look plausible in the context of the question. The official practice questions have three options each and say "Choose only ONE best answer".

## Out of scope (non-exhaustive list from the guide)
Job tasks earners will not be required to perform:
- Programming
- Systems Architecture
- Testing

## Content outline
The guide lists four domains and their subdomains, without weights.

| Domain | Subdomain | What it covers |
|---|---|---|
| APM Fundamentals | APM Rationale | Why distributed tracing: microservices in many languages and platforms, RED signals, percentiles vs averages, Apdex, MTTR |
| APM Fundamentals | Datadog Approach to APM | SDK to Agent to backend, core terms, trace metrics on 100% of traffic, ingestion vs indexing, product surfaces, correlation, pricing |
| APM Fundamentals | Tracing Architectures | Trace, span, root and service entry spans, span tags vs attributes, context propagation, baggage, span links, inferred services, OpenTelemetry, Lambda Extension |
| APM Fundamentals | Language Level Differences — Automatic Instrumentation | How each SDK auto-instruments (Java agent, `ddtrace-run`, `dd-trace` init, Go Orchestrion, Ruby gem, .NET CLR profiler, PHP extension) and Single Step Instrumentation |
| APM Fundamentals | OOTB Tracer vs Community Tracer | Official Datadog SDKs vs community libraries for unsupported languages, the Agent tracing API, what the SDK vs the Agent does, OpenTelemetry |
| APM Fundamentals | Tagging | Tag rules, unified service tagging (`env`, `service`, `version`), primary tags, tags available on trace metrics, peer tags, tag enrichment |
| APM Fundamentals | Retention Periods for APM Data | Live Search 15 min, indexed spans 15/30 days, trace metrics 15 months, profiles 8 days, Error Tracking, billing allotments |
| Application Instrumentation | Datadog Tracing Libraries | SDK configuration, Agent connection env vars, core `DD_*` variables, Java and Python specifics, Remote Configuration, startup and debug logs, runtime metrics |
| Application Instrumentation | Instrumentation Types | Automatic (SSI or manually managed SDK), code-based custom instrumentation (Datadog API, OpenTelemetry API), Dynamic Instrumentation, OpenTelemetry options |
| Application Instrumentation | Datadog Agent Architecture | trace-agent, `apm_config`, ports 8126/4317/4318/443, how SDKs find the Agent, Docker and Kubernetes, Agent sampling, rate limits, Lambda Extension |
| Application Instrumentation | Sampling vs Retention | Head-based sampling, SDK rules, error/rare samplers, force keep/drop, Ingestion Control, adaptive sampling, retention filters, Intelligent retention filter |
| Application Instrumentation | APM Data Security | Agent obfuscation, `replace_tags`, `ignore_resources`, SDK query-string and header settings, Sensitive Data Scanner, Live Debugger redaction, RBAC |
| Application Instrumentation | Profile Collection | Enabling the Continuous Profiler per language (`DD_PROFILING_ENABLED`, `-javaagent` before `-jar`, Go `profiler.Start`), requirements, SSI |
| Insight Discovery | Software Catalog | Catalog views, entity discovery, entity definitions (v2 to v3), ownership, integrations, permissions, Scorecards |
| Insight Discovery | Search Syntax | Span tags vs attributes (`@`), reserved attributes, boolean operators, wildcards, ranges, escaping, facets and measures, Trace Queries |
| Insight Discovery | Trace Live vs Retained Search | Live Search (15 min, all ingested) vs indexed search, where each data set can be used, visualizations, retention filters' effect |
| Insight Discovery | Profilers | Profile types, flame graph, timeline, call graph, comparing profiles, Automated Analysis, traces to profiles, endpoint profiling, retention |
| Insight Discovery | Deployment Tracking | `version` tag, version breakdowns, Deployments section, deployment comparison, strategies, Faulty Deployment Detection, Deployment Gates |
| Insight Discovery | Error Tracking | Which spans become issues (`error.type`, `error.message`, `error.stack`), grouping, explorer, issue states, monitors, suspect commits, Exception Replay |
| Insight Discovery | Span Summary | Execution time, Span Summary table on the Resource page, Trace View visualizations, span side panel tabs, span links |
| Insight Discovery | Service Performance Dashboards | Service and Resource pages, Service Map, trace metrics namespace, DDSketch percentiles, Apdex, primary operation, copying graphs to dashboards, Find correlated metrics |
| Troubleshooting Application using APM | Using Trace Search (during incident) | Spike to traces workflow, Trace Explorer filters, Watchdog insights, Trace View, correlated logs, RUM and Synthetics, postmortem notebooks, tracer troubleshooting |
| Troubleshooting Application using APM | Monitors & Alerting | APM Metrics and Trace Analytics monitors, anomaly detection, Watchdog, Error Tracking monitors, SLOs and SLO alerts, notification variables |

## Recommended learning resources
- **APM & Distributed Tracing Fundamentals Certification Learning Path**: a series of 16 courses covering key exam topics (completing it does not guarantee a passing score). https://learn.datadoghq.com/bundles/apm-distributed-tracing-fundamentals-certification-learning-path
- **Practice exam**: a 25-question practice exam, free, take it any time at your own pace. https://learn.datadoghq.com/courses/apm-distributed-tracing-fundamentals-practice-exam (the copy of the official example questions in this repo has 23 of them).
- **Documentation** the guide says candidates may overlook (reading them is not a shortcut; steady practice with the core curriculum remains essential):
  - Getting Started with Tags: https://docs.datadoghq.com/getting_started/tagging/
  - APM & Continuous Profiler client libraries: https://docs.datadoghq.com/developers/community/libraries/#apm--continuous-profiler-client-libraries (now served at `/extend/community/libraries/`)
  - Profiler Visualizations: https://docs.datadoghq.com/profiler/profile_visualizations/
  - Correlate APM Data with Other Telemetry: https://docs.datadoghq.com/tracing/other_telemetry/
  - Anomaly Monitor (set alert conditions): https://docs.datadoghq.com/monitors/types/anomaly/#set-alert-conditions
  - SLOs: https://docs.datadoghq.com/service_management/service_level_objectives/ (current pages live under `/service_level_objectives/`)
  - Datadog Lambda Extension: https://docs.datadoghq.com/serverless/libraries_integrations/extension/
  - Set Up the OpenTelemetry Collector: https://docs.datadoghq.com/opentelemetry/setup/collector_exporter/
  - Advanced Usage — ddtrace documentation: https://ddtrace.readthedocs.io/en/stable/advanced_usage.html

## What the official practice questions lean on
- **Retention and Live vs retained search**: Live Search shows all ingested traces for **15 minutes**; 1 million indexed spans per month retained **15 days**; the **Intelligent retention filter** is always on; spans from the Intelligent **and** custom retention filters are available in notebooks and dashboards after 15 minutes; a postmortem notebook uses **trace metrics**.
- **Tagging**: `service` tracks services, `version` tracks deployments, monitors link to services when scoped with `service`; custom tags are NOT available on trace metrics (env, service, version and the second primary tag are).
- **Profiler setup**: `DD_PROFILING_ENABLED`; Java `-javaagent` goes **before** `-jar`; the official answer says the profiler can always be enabled with in-code configuration; profiles are searched with facets.
- **Error Tracking**: an error span needs `error.message`, `error.type` and `error.stack`.
- **Dashboards and metrics**: percentiles p50, p75, p90, p95, p99; copy a service page graph with Ctrl/Cmd+C; "Find correlated metrics"; Apdex = ratio of requests meeting a time threshold.
- **Fundamentals**: every span has a name, duration and start time; the main challenge of distributed apps is many languages and platforms; custom spans = custom instrumentation; community tracers for unsupported languages; RUM correlation allows the origins the browser app calls.

## What changed in the product since the 2025 guide
- **Catalog**: Service Catalog became Software Catalog and is now just **Catalog**, part of the Internal Developer Portal; entity definitions moved to schema **v3** (`apiVersion: v3`, `kind`, `metadata.name`, `owner`).
- **Datadog SDKs**: the docs now call the tracing libraries "Datadog SDKs"; there is an official **Rust SDK** (OpenTelemetry API based, no automatic instrumentation). The community libraries page moved to `/extend/community/libraries/`.
- **Single Step Instrumentation** is the recommended setup path; instrumentation rules (Agent 7.73+) and Kubernetes targets (Agent 7.64+) control what gets instrumented.
- **Intelligent retention filter** spans are now retained **30 days** (custom filters still 15 days); the Data Retention Periods page says indexed spans are kept "15 or 30 days, determined by customer plan".
- **Rare sampler** is off by default since Agent 7.41.0; `DD_TRACE_SAMPLE_RATE` is deprecated for Java, Python and Go in favour of `DD_TRACE_SAMPLING_RULES`; adaptive sampling (Agent 7.53.0+) sets a monthly ingestion target.
- **Agent 7.80.0+ on Linux** starts the trace-agent only after it receives trace data (socket activation), so `agent status` can show APM "not running" before the first trace.
- **RUM**: `allowedTracingOrigins` (the term in the official practice question) is now `allowedTracingUrls`.
- **`DD_LOGS_INJECTION`** now defaults to `true` in Python (v3.10.0+), Java and Node.js.
- **OpenTelemetry**: the DDOT Collector (embedded in the Agent) is the recommended OTel option; for an upstream Collector the recommended path is the OTLP HTTP exporter plus the `span_metrics` connector rather than the Datadog Exporter.
- **Lambda Extension**: v88+ is next-generation only.
- **Profiler**: "code hotspots" is now the **Profiles** tab on a span (Trace to Profiling).
- **Monitors**: Recommended Monitors are now **Monitor Templates**; the old `adaptive` anomaly algorithm is no longer used.
- **Service Map**: node borders follow **Service Health** (Critical/Warning) instead of the old green/yellow/red/gray monitor colours.

# Domain 1: APM Fundamentals

## APM Rationale

### Why APM: the distributed-systems problem
- Datadog APM "provides deep visibility into your applications, enabling you to identify performance bottlenecks, troubleshoot issues, and optimize your services" through distributed tracing, out-of-the-box dashboards and correlation with other telemetry (logs, RUM, synthetics, profiles, DBM).
- Glossary definition: **APM** (synonyms: Tracing, Distributed Tracing) "monitors requests, errors, and latency in your application". Distributed traces correlate with browser sessions, logs, profiles, synthetic checks, network, processes and infrastructure metrics across hosts, containers, proxies and serverless functions.
- **Distributed tracing** = tracking application requests as they flow from frontend devices to backend services and databases; used to troubleshoot requests with **high latency or errors**.
- Modern apps are **microservice architectures**: a **service** groups endpoints, queries or jobs (examples: an API service of URL endpoints, a database service of queries, a `crond` service of periodic jobs). One user request (for example checkout) crosses many services (`web-store` -> `auth-service` -> `payment-db`, `ad-server`). Services are written in different languages (Datadog SDKs: Java, Python, Ruby, Go, Node.js, PHP, C++, .NET, Rust) and run on different platforms (hosts, containers, Kubernetes, serverless). Per-host metrics or per-service logs alone cannot show the path a single request took or which hop added the time; a trace can.
- What APM answers that metrics/logs alone cannot:
  - Where time is spent across services within one request (flame graph, % Exec Time, Avg Time per Request graph).
  - Which dependency is slow or failing (dependency map, Service Map, trace map with red-bordered failing nodes).
  - Which resource (endpoint/query) is slow (Resources list sorted by p99, resource page).
  - Which version/deployment introduced errors or latency (Deployment Tracking via `version` tag).
- Use cases on the APM overview page: understand how requests flow (Trace Explorer), monitor service health (service/resource pages), correlate traces with DBM, RUM, logs, synthetics, profiles, control data flow (Ingestion Controls + retention filters keep spans 15 days).

Sources: https://docs.datadoghq.com/tracing/, https://docs.datadoghq.com/glossary/#apm, https://docs.datadoghq.com/glossary/#distributed-tracing, https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/

### Core vocabulary used when justifying APM
- **Trace**: tracks the time spent by an application processing a request **and the status** of that request; consists of one or more spans.
- **Span**: a logical unit of work in a distributed system for a given period; multiple spans construct a trace.
- **Service entry span**: the entrypoint method for a request to a service (immediate parent on the flame graph has a different color). **Trace root span**: first span of a trace; its start marks the beginning of the trace.
- **Resource**: a particular domain of an application, typically an instrumented web endpoint (`GET /productpage`), database query or background job.
- **Trace context propagation**: passing trace identifiers (trace ID and parent span ID) between services by **injecting** them into HTTP headers; the downstream service **extracts** them and continues the trace, so Datadog can stitch spans from different services into one distributed trace. This is what makes polyglot (multi-language) request paths visible end to end.
  - Default formats (`DD_TRACE_PROPAGATION_STYLE`): `datadog,tracecontext,baggage`. Datadog headers take precedence on extraction; W3C `tracecontext` gives interoperability with OpenTelemetry and other tracers. Extract/inject-only overrides: `DD_TRACE_PROPAGATION_STYLE_EXTRACT`, `DD_TRACE_PROPAGATION_STYLE_INJECT`. `DD_TRACE_PROPAGATION_BEHAVIOR_EXTRACT` default `continue` (others `restart`, `ignore`). With auto-instrumentation, propagation is automatic.
- **Instrumentation**: adding code to capture and report observability data. Single Step Instrumentation (SSI) is the recommended start (no code changes); manually managed SDKs for full control; Dynamic Instrumentation (UI, no redeploy) or code-based custom instrumentation for custom spans.
- **Baggage**: key-value business/context data propagated across service boundaries alongside traces.

Sources: https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/glossary/#trace-root-span, https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/, https://docs.datadoghq.com/tracing/trace_collection/

### The RED signals: requests, errors, duration (latency)
- Every service page and resource page has out-of-the-box graphs built on these signals:
  - **Requests and Errors**: total requests (hits) and errors; dropdown: Requests by Version, Requests per Second by Version, Requests and Errors Per Second.
  - **Errors**: total errors; dropdown: Errors by Version, Errors per Second by Version, Errors per Second, % Error Rate by Version, % Error Rate.
  - **Latency**: latency percentiles as a timeseries; dropdown: Latency by Version, Historical Latency (compare with previous day and week), Latency Distribution, Latency by Error, **Apdex**.
  - **Avg Time per Request** (fourth graph, only for services with downstream services): average execution time per request broken down by downstream service; dropdown: Total Time Spent, % of Time Spent. Built on **sampled** trace data, unlike the other top graphs which use **unsampled** data. Leaf services like Postgres or Redis (final operations that call no other service) have no sub-services graph.
- Watchdog performs automatic anomaly detection on the Requests, Latency and Error graphs (overlay on the graph; click the Watchdog icon for a side panel). Hovering a latency spike offers **Investigate With Bits AI**.
- Export: arrow on the upper-right corner of a graph exports it to an existing dashboard.
- The RED signals come from **trace metrics** (namespace `trace.<SPAN_NAME>.<METRIC_SUFFIX>`):
  - `trace.<SPAN_NAME>.hits` (COUNT) = requests; `.hits.by_http_status` (COUNT).
  - `trace.<SPAN_NAME>.errors` (COUNT); `.errors.by_http_status` (COUNT).
  - `trace.<SPAN_NAME>` (DISTRIBUTION) = latency distribution, **recommended for all latency measurement**.
  - `trace.<SPAN_NAME>.apdex` (GAUGE), HTTP/web services only.
  - Legacy: `trace.<SPAN_NAME>.duration` and `.duration.by_http_status` (GAUGE), kept for backward compatibility, **no percentile aggregations**. Average latency with host-tag filters: `sum:trace.<SPAN_NAME>.duration{<FILTER>}.rollup(sum).fill(zero) / sum:trace.<SPAN_NAME>.hits{<FILTER>}.rollup(sum).fill(zero)`.
- Trace metrics are calculated from **100% of application traffic regardless of trace ingestion sampling** (exceptions: OpenTelemetry SDK-level sampling, X-Ray sampling, rare application-side sampling such as Ruby's). With the OTel Collector, put the `span_metrics` connector before `tail_sampling` (or use the Datadog Connector).
- Trace metric tags: `env`, `service`, `version`, `resource`, `http.status_code`, `http.status_class`, `rpc.grpc.status_code` (Agent 7.65.0+), Agent host tags and additional primary tags. **Other span tags are not available on trace metrics.**
- Trace metrics are retained **15 months** (like any Datadog metric); usable in dashboards, monitors and SLOs.
- Resources list columns: Requests, Requests per second, Total time, Avg/p75/p90/p95/p99/Max Latency, Errors, Error Rate. Sort to find high-traffic or slow resources.

Sources: https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/tracing/services/resource_page/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/, https://docs.datadoghq.com/glossary/#trace-metric

### Latency percentiles vs averages
- **Percentile** (glossary): how a score compares to others in the dataset, or the percentage of values that fall below a given value. p99 = 800 ms means 99% of requests completed in 800 ms or less; the slowest 1% took longer. Max (p100) is the single slowest.
- Averages hide the tail: a few very slow requests barely move an average but show in p95/p99. Apdex docs explicitly say response-time averages and percentiles "can be misleading when there are extreme data points", which is why Apdex exists as a counterbalance.
- APM latency is a **DDSketch-based distribution** (`trace.<SPAN_NAME>`): one metric instead of a separate metric per percentile and per service/resource/primary tag. DDSketch uses **relative-error** guarantees (instead of rank-error), so percentile estimates are closer to the true value; most noticeable as a **reduction in p99** values after the switch. Datadog stitches queries on the new metric with the older latency metrics so history is preserved.
- Query syntax change: before `avg:trace.http.request.duration.by.resource_service.99p{service:foo, resource:abcdef1234}`; after `p99:trace.http.request{service:foo, resource:abcdef1234}`. p100 after: `max:trace.http.request{...}`.
- Distribution metrics support percentile aggregations p50, p75, p90, p95, p99 (any custom percentile with up to two decimals on custom distributions), computed server-side with DDSketch.
- Where percentiles show up: service Latency graph (deselect all but p50 and use **Compare to Last > Week** for week-over-week), Latency Distribution graph, resource latency distribution with percentile selectors, Resources list p75/p90/p95/p99/Max, Deployments table p50/p75/p90/p95/p99/max.
- APM metric monitor options: Requests per second, Errors per second, Apdex, Error rate, Avg latency, p50 latency, p75 latency, p90 latency, p99 latency; **Threshold** or **Anomaly** alert (anomaly accounts for trends, day-of-week and time-of-day seasonality; guide example: anomaly alert on p99 latency of a database service, set "Alert when" to 100%). Evaluation window 1 minute to 48 hours.
- Pitfall: the "Debug the slowest trace" workflow = Service page -> sort Resources by **p99** latency (enable via cog / Change Columns) -> resource page -> Traces table sorted by duration -> View Trace -> flame graph -> Host tab.

Sources: https://docs.datadoghq.com/glossary/#percentile, https://docs.datadoghq.com/tracing/guide/ddsketch_trace_metrics/, https://docs.datadoghq.com/metrics/distributions/, https://docs.datadoghq.com/tracing/guide/week_over_week_p50_comparison/, https://docs.datadoghq.com/monitors/types/apm/, https://docs.datadoghq.com/tracing/guide/alert_anomalies_p99_database/, https://docs.datadoghq.com/tracing/guide/slowest_request_daily/

### Apdex: a user-satisfaction score
- **Apdex** (Application Performance Index) is an open standard for reporting, benchmarking and tracking application performance based on user satisfaction with response time. It converts many measurements into one number on **[0;1]**: 0 = no users satisfied, 1 = all users satisfied.
- One threshold **T** (set per service) defines three buckets:
  - **Satisfied**: response time **below T**.
  - **Tolerated**: **>= T and <= 4T**.
  - **Frustrated**: **> 4T, or the request returns an error** (an error is frustrated however fast it was).
- Formula: **Apdex = (Satisfied + Tolerated / 2) / Total requests**. Example: T = 200 ms, 1,000 requests, 600 under 200 ms, 300 between 200 and 800 ms, 100 over 800 ms -> (600 + 150) / 1000 = **0.75**.
- Choosing T matters: frustrated requests are 4x slower than "normal" (T = 3 s: users wait 3 s but will not tolerate 12 s).
- Configuration: **administrators only**, **per service**, and the threshold must be set before scores are calculated. Path: Catalog -> hover a web service -> Service Page -> click the **Latency graph title** -> select **Apdex** -> **pencil icon** (top left of the widget, visible to admins only) -> enter threshold -> Save. Apdex is **only available for web services**.
- Show Apdex in the Catalog via the configuration menu in the upper-right corner of the page.
- Metric: `trace.<SPAN_NAME>.apdex`, GAUGE, for HTTP/web services; tags `env`, `service`, `version`, `resource`/`resource_name`, `synthetics`, additional primary tags. Apdex is also an APM monitor option.

Sources: https://docs.datadoghq.com/tracing/guide/configure_an_apdex_for_your_traces_with_datadog_apm/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/#apdex, https://docs.datadoghq.com/monitors/types/apm/

### Finding where time is spent and which dependency fails
- **Trace View**: Flame Graph (default; color-coded spans on a timeline showing execution path and where time was spent; legend groups by Service (default), Base service, Host or Container and shows **% Exec Time** or span count; **Errors** checkbox under Filter Spans highlights error spans), Span List (sort by RESOURCE, SPANS, AVG DURATION, EXEC TIME, % EXEC TIME), Waterfall (one row per span, relative and absolute duration, HTTP status), Map (service nodes with % of total execution time; failing service entry span -> red border; error on exit span -> red edge). Traces > 100MB open in Trace Preview (Waterfall and Map only).
- **Execution time**: total time a span is active, not waiting for a child span. Sequential children: parent execution time = parent duration minus time covered by children. Concurrent children: overlapping time is divided by the number of concurrently active spans.
- **Service dependency map** (service page) is powered by APM metrics: request counts, error rates, latency; left-hand table shows requests and error rates over time to "identify failing dependencies". Inferred services (databases, queues, third-party APIs) = purple background node. Click a dependency node to scope requests/errors/latency to calls from this service to that dependency and see which queries/resources are slow or failing.
- **Resource dependency map**: based on a sample of ingested spans, rates upscaled by sampling rates; only for service-entry span resources.
- **Service Map**: decomposes the app into services and draws observed dependencies in real time; scoped by `env` (plus optional second primary tag). When inspecting a service, services on the **left are closer to customers**, services on the **right are more likely root causes**. Nodes age out after 30 days without traces. Node borders red/yellow from Service Health. Monitor status circles in the guide: green = all quiet, yellow = warning, red = alerting, gray = no monitor.
- **Span summary** (resource page) helps detect N+1 problems (Avg Spans/trace, % of Traces, avg duration, share of execution time).
- Correlation shortens investigation: inject trace ID, span ID, `env`, `service`, `version` into logs (set `DD_ENV`, `DD_SERVICE`, `DD_VERSION`); logs must be JSON or parsed. Traces and logs are sampled independently, so a log can reference a trace that was not retained. Host tab in trace view shows CPU/memory of the host during the request.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/glossary/#execution-time, https://docs.datadoghq.com/tracing/services/service_page/#dependencies, https://docs.datadoghq.com/tracing/services/resource_page/, https://docs.datadoghq.com/tracing/services/services_map/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/

### MTTR and incident-response benefits
- **Watchdog RCA** helps "reduce mean time to recovery (MTTR) by automating preliminary investigations during incident triage". It **requires APM**; unified service tagging recommended. Starts whenever Watchdog finds an APM anomaly.
  - Data considered: APM error rate, latency and hit rate metrics; APM deployment tracking; APM traces; Agent infra metrics (CPU, memory, disk); AWS instance status checks; log pattern anomalies.
  - Components: **Root cause** (a state change: version change from Deployment Tracking, traffic increase from hit rate, AWS instance failure, running out of disk space), **Critical failure** (where the root cause first degrades performance; always a latency or error rate increase), **Impact** (indirectly affected services; RUM views/users affected). Watchdog **never** classifies higher latency or new errors as the root cause.
- **Service health** (Catalog, service page, dependency maps, service pills): Critical if a non-muted paging monitor (PagerDuty/Opsgenie) is in `ALERT` within the past 2 days, an incident of any severity is active, a faulty deployment is ongoing, or an APM latency/error-rate Watchdog alert is ongoing. Warning: paging monitor in `WARN`, stable incident, or log anomaly.
- **Deployment Tracking** (`version` tag): Requests/Errors by Version, versions table with Error Types indicator (new error types vs previous version), latency p50-p99/max columns; enables **Automatic Faulty Deployment Detection** (monitor on Events with `tags:deployment_analysis`). The version section appears only with more than one version in the time frame.
- **Error Tracking** groups similar error spans into issues (fingerprint from error type, message, stack frames); error spans need `error.stack`, `error.message`, `error.type`. Reduces noise for triage.
- **APM monitors** (Monitors > New Monitor > APM): APM Metrics (threshold/anomaly) or Trace Analytics (indexed spans from custom retention filters only). Automatic APM monitors (trial only) on service entry points (`span.kind:server`/`consumer`): error-rate threshold (default 10%) and Watchdog anomaly monitors.
- **Incident Management Analytics** measures: Time to Detect (earliest impact -> detection), Time to Repair (detection -> last customer impact), **Time to Resolve** (declaration -> resolved), Time to Internal Response (detection -> declaration), **Time from Detect to Resolve** (detection -> resolved; includes detection-to-declaration gap), Customer Impact Duration, Status Active/Stable Duration. Used to "assess your mean time to resolution". Timestamp overrides (Incidents > Settings > Information, needs Incidents Write) fix inflated MTTR.
- DORA metric for recovery: **Failed deployment recovery time** (time to recover from a deployment that fails and needs immediate intervention).
- Pitfall: "MTTR" expands differently by page: Watchdog RCA says mean time to **recovery**; Incident Analytics says mean time to **resolution**.

Sources: https://docs.datadoghq.com/watchdog/rca/, https://docs.datadoghq.com/tracing/services/service_page/#service-health, https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/tracing/error_tracking/, https://docs.datadoghq.com/monitors/types/apm/, https://docs.datadoghq.com/incident_response/incident_management/analytics/, https://docs.datadoghq.com/dora_metrics/

## Datadog Approach to APM

### Big picture: how Datadog APM is built
- Datadog APM = code-level distributed tracing from browser/mobile apps down to backend services and databases, plus out-of-the-box service dashboards and correlation with logs, RUM, Synthetics, profiles, DBM and infrastructure.
- Data flow (the "APM lifecycle"): instrumented application (Datadog SDK / tracing library) -> Datadog Agent (trace-agent) -> Datadog backend. Traces start in your instrumented applications and flow into Datadog. Then: **ingestion** (what is sent) -> optional Processing Pipelines -> **trace metrics / span-based custom metrics** -> **retention filters** (what is indexed) -> Trace Explorer, dashboards, monitors.
- Application instrumentation = (1) SDK setup (add a Datadog SDK) + (2) span creation. Spans are generated automatically as soon as the SDK loads (**auto-instrumentation**); optional custom spans via **Dynamic Instrumentation** (UI rules, no code change, no redeploy) or **code-based custom instrumentation** (tracing API calls in code, requires deploy).
- SDK setup options: **Single Step Instrumentation (SSI)** - recommended; installs the Agent and loads SDKs into processes at runtime with one command, no code changes (for example `DD_APM_INSTRUMENTATION_ENABLED=host DD_APM_INSTRUMENTATION_LIBRARIES=python:4 ... install_script_agent7.sh`). **Manually managed SDKs** - you install/configure the SDK (`pip install ddtrace`, run with `ddtrace-run python app.py`); full control via env vars and code. Options can be combined.
- Languages without an official SDK: use community SDKs (community tracing client libraries). OpenTelemetry is the vendor-neutral alternative.
- Agent side: by default the Agent receives traces with `apm_config.enabled: true` in `datadog.yaml` and listens at `http://localhost:8126`. For containers set `apm_non_local_traffic: true` (`DD_APM_NON_LOCAL_TRAFFIC`). The tracer first tries the Unix socket `/var/run/datadog/apm.socket`, then falls back to `http://localhost:8126`; override with `DD_TRACE_AGENT_URL` (or `DD_AGENT_HOST` / `DD_TRACE_AGENT_PORT`). Stats/runtime metrics go to `/var/run/datadog/dsd.socket` or `localhost:8125` (DogStatsD). Set `DD_SITE` in the Agent for non-US1 sites.
- Datadog-specific env vars (`DD_SERVICE`, `DD_ENV`, `DD_VERSION`) are NOT read by OpenTelemetry SDKs; OTel uses `service.name`, `deployment.environment.name`, `service.version` resource attributes.

Sources: https://docs.datadoghq.com/tracing/, https://docs.datadoghq.com/tracing/trace_collection/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/getting_started/tracing/, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/

### Core terms (APM Terms and Concepts)
- **Service**: groups endpoints, queries or jobs for the purpose of scaling instances (for example an API service, a DB service, a crond service). Each service has a Service page.
- **Resource**: a particular domain of the app - typically an instrumented web endpoint (`GET /productpage`, `ShoppingCartController#checkout`), DB query, or background job. Each resource has a Resource page with trace metrics scoped to it.
- **Trace**: tracks the time spent processing a request and its status; one or more spans.
- **Trace root span**: the first span of a trace (entry-point method of the traced request). **Service entry span**: the entry-point method for a request to a service (immediate parent on the flame graph is a different color).
- **Trace context propagation**: injecting trace ID and parent span ID into headers so the downstream service extracts them and continues the trace. **Baggage**: key-value business context propagated across service boundaries.
- **Execution time**: time a span is active (not waiting on a child); concurrent children split overlapping time.
- **Retention filters**: tag-based controls in the UI deciding which spans are indexed for 15 days. **Ingestion controls**: send up to 100% of traces to Datadog for live search and analytics for 15 minutes.
- Endpoints on a Service page are connected by service name AND the `span.name` of the entry-point span (for example `web.request`).

Sources: https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/glossary/

### Trace metrics (calculated before sampling)
- Trace metrics capture request counts (hits), error counts and latency. They are calculated from **100% of the application's traffic, regardless of ingestion sampling**, and by default are computed **in the Datadog Agent** from traces the SDK sends to it. Datadog SDK/Agent ingestion sampling does not affect them (see the exceptions below).
- Namespace `trace.<SPAN_NAME>.<METRIC_SUFFIX>`: `trace.<SPAN_NAME>.hits` (COUNT), `.hits.by_http_status`, `.errors` (COUNT), `.errors.by_http_status`, `trace.<SPAN_NAME>` (DISTRIBUTION - latency, recommended), `.apdex` (GAUGE, web services), legacy `.duration` / `.duration.by_http_status`.
- Tags available on trace metrics: `env`, `service`, `version`, `resource`, `http.status_code`, `http.status_class`, `rpc.grpc.status_code` (Agent 7.65.0+), Agent/host tags and additional primary tags. **Other (custom) span tags are not available on trace metrics.**
- Retention: trace metrics are kept 15 months like any Datadog metric. Ingested spans: 15 minutes (Live). Indexed spans: 15 days. Span-based custom metrics: 15 months.
- Exceptions where trace metrics represent only sampled traffic: application-side sampling (for example Ruby option, not recommended), **OpenTelemetry SDK sampling** (put the `span_metrics` connector before sampling in the Collector to compute from all traffic), and AWS X-Ray sampling.
- Runtime metrics (`DD_RUNTIME_METRICS_ENABLED`, default false in Python) are sent to the Agent over the DogStatsD port.
- Generate custom metrics from spans/traces: APM > Generate Metrics > New Metric. Works on **ingested** spans whether or not they are indexed (spans dropped by sampling cannot generate metrics); names cannot start with `trace.*`; 15-month retention; billed as custom metrics, so avoid high-cardinality group-bys (user/request/session IDs); only the filter query and group-by can be edited after creation.

Sources: https://docs.datadoghq.com/tracing/metrics/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/, https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/

### Ingestion (what is sent to Datadog)
- Ingestion controls = mechanisms in the Agent and SDKs that decide which traces go from the app to Datadog. Each ingested span has an `ingestion_reason`.
- **Head-based sampling** (default): keep/drop decided at the root span and propagated, so traces are kept or dropped whole.
  - Agent (`ingestion_reason:auto`, shown as `Automatic`): Agent sends rates to SDKs targeting **10 traces per second per Agent** (`DD_APM_TARGET_TPS` / `apm_config.target_traces_per_second`). Only applies to Datadog SDKs, not OTel SDKs.
  - SDK rules (`ingestion_reason:rule`): `DD_TRACE_SAMPLING_RULES` (by service/resource), rate limit `DD_TRACE_RATE_LIMIT` default **100 traces/s per service instance**. `DD_TRACE_SAMPLE_RATE` deprecated in several SDKs -> `[{"sample_rate":0.1}]`.
- Agent catch-up samplers: **error** sampler (`ingestion_reason:error`) up to **10 traces/s per Agent** (`DD_APM_ERROR_TPS`, `0` disables); **rare** sampler (`ingestion_reason:rare`) up to **5 traces/s per Agent**, disabled by default since Agent 7.41 (`DD_APM_ENABLE_RARE_SAMPLER`).
- Force keep/drop (`ingestion_reason:manual`), single span sampling `DD_SPAN_SAMPLING_RULES` (`single_span`), product reasons `rum`, `synthetics`, `synthetics-browser`, `lambda`, `xray`, `appsec`, `data_jobs`, `otel`.
- Legacy App Analytics is fully deprecated (use single span sampling or head-based sampling); App Analytics filters became retention filters on October 20, 2020.
- Ingestion Control page (APM > Ingestion Control): Monthly Ingestion vs allotment, adaptive sampling, per-service table (Ingested Traces/s, Ingested Bytes/s, Downstream Bytes/s, Traffic Breakdown, Configuration `APM Agent`/`APM Local`/remote). Remote configuration needs Agent 7.41.1+ (Agent-level sampling params 7.42.0+). Precedence: remote > local, rules > global rate, tracer > Agent.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/

### Indexing (retention filters) and where data is searchable
- Retention filters decide which **ingested** spans are indexed; they do **not** affect what the Agent collects and sends (use ingestion controls for that). Permission `apm_retention_filter_write` required to edit. Page: APM > Retention Filters (Add Retention Filter, Retention Query, Span rate, optional Trace rate, Add Filter). Filters are evaluated in order; a span caught by an upper filter is not seen by lower ones.
- **Intelligent retention filter** (always on): diversity sampling (one span per env/service/operation/resource every 15 min max, p75/p90/p95 latency spans, diverse errors) + 1% flat sampling (1% of RUM sessions with traces by `session_id`, uniform 1% of ingested spans by `trace_id`). Spans it indexes are **not counted toward indexed-span usage**; retained **30 days**; excluded from trace analytics monitors.
- **Default retention filters**: `Error Default` (`status:error`), `App and API Protection Default`, `Synthetics Default`, `Dynamic Instrumentation Default`.
- **Custom retention filters**: any tag/attribute query, for example `@transaction_amount:>100`, `resource_name:"GET /checkout" @duration:>2s env:prod`; indexed 15 days; count toward indexed-span usage. Trace rate indexes whole traces (queryable in Trace Queries) and can greatly increase usage.
- `retained_by` facet values: `retention_filter`, `trace_retention_filter`, `diversity_sampling`, `flat_sampled` (`@retention_reason:rum` / `trace`).
- Trace Explorer: **Live Search** = all ingested spans for the last 15 minutes (rolling), any tag on any span, no sampling; default view. Time range > 15 minutes = **indexed spans only** ("Search - Only Indexed Data"). A tag present only on non-indexed spans returns nothing outside Live Search. Export to dashboards/monitors only from retained spans.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/tracing/trace_explorer/

### APM product surfaces
- **Catalog** (formerly Service Catalog / Software Catalog; now under Internal Developer Portal) - centralized view of software entities and infrastructure; every APM service listed; service type from `span.type` (Web, DB, Cache, Custom, Serverless function); span summaries and service/resource statistics retained up to 30 days.
- **Service page**: service health (Critical/Warning from paging monitors, incidents, Watchdog), monitors (attached if `service:<SERVICE_NAME>` is tagged/queried/grouped), Watchdog Insights, summary cards, OOTB graphs (Requests and Errors, Errors, Latency incl. Apdex, Avg Time per Request). **Avg Time per Request is built on sampled trace data; the other top graphs use unsampled data.** Export graphs to a dashboard via the arrow on each graph. Tabs: Deployments, Error Tracking, Security, Databases, Infrastructure, Runtime Metrics, Profiling, Memory Leaks, Traces, Log patterns, Costs.
- **Service Map**: no setup required; built from APM and RUM data; scoped by `env` (and optional second primary tag); nodes age out after 30 days without traces; node border colored by Service Health; rendered from complete traces with root spans (when spans are missing, for example after APM connection errors, the map may be unavailable for that window).
- **Trace Explorer**: Live Search 15 min vs indexed 15 days; Watchdog outlier tags surface in search suggestions, facets ("OUTLIERS") and Analyze buttons.
- **Trace View**: Flame Graph (default), Span List, Waterfall, Map; traces > 100MB open in Trace Preview (Waterfall and Map only); tabs for logs, infrastructure, processes, network, security, profiles, span links.
- **Continuous Profiler**: CPU, memory, IO by method/class/line; processes with both tracing and profiling are automatically linked (Profiles tab on a span). Flame graphs retained 8 days, profile metrics 1 month, exported flame graphs 1 year.
- **Error Tracking**: groups similar error spans into issues using a fingerprint of error type, message and stack frames; needs `error.stack`, `error.message`, `error.type` on a span in a complete trace; no extra SDK or config.
- **Deployment Tracking**: uses the reserved `version` tag; version section appears only when more than one version reported in the time frame; compare any two versions within the past 30 days.
- **Watchdog**: built-in AI engine, no setup; Automatic Faulty Deployment Detection compares new `version` with previous ones; notify via an Event monitor with `tags:deployment_analysis` (recommended 60 min recovery).

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/, https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/tracing/services/services_map/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/profiler/, https://docs.datadoghq.com/tracing/error_tracking/, https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/watchdog/, https://docs.datadoghq.com/watchdog/faulty_deployment_detection/

### Correlating traces with other telemetry
- **Unified service tagging**: reserved tags `env`, `service`, `version` tie traces, metrics, logs, profiles together. Traced apps: set `DD_ENV`, `DD_SERVICE`, `DD_VERSION`; Kubernetes labels `tags.datadoghq.com/env|service|version`. Requires Agent 6.19/7.19+. Automatic APM version tagging from image tag / git SHA (Agent 7.52.0+).
- **Logs**: inject trace ID, span ID, `env`, `service`, `version` into logs (Python: `dd.trace_id`, `dd.span_id`, `dd.env`, `dd.service`, `dd.version`; `DD_LOGS_INJECTION` now defaults to `true`; older `ddtrace<3.11` needed it set explicitly). Logs must be JSON or parsed so attributes exist; custom parsing must remap `dd.trace_id` with the Trace Remapper. **Traces and logs are sampled independently** - a log can reference a trace that was not ingested/retained; not a config error.
- **RUM**: Browser SDK `allowedTracingUrls` (first-party backend URLs; formerly `allowedTracingOrigins`), mobile `firstPartyHosts`; `traceSampleRate` (default 100%) samples only backend traces, not RUM sessions; `traceContextInjection` default `sampled`. Headers `x-datadog-trace-id`, `x-datadog-parent-id`, `x-datadog-origin: rum`, `x-datadog-sampling-priority`, plus `traceparent`/`tracestate`; CORS must allow these headers. Default propagators `datadog` + `tracecontext`. `ingestion_reason:rum`.
- **Synthetics**: HTTP, multistep API and browser tests generate traces when backend is traced; browser tests need allowed URLs in Synthetic Settings > Integration Settings. Headers `x-datadog-origin: synthetics` / `synthetics-browser`, `x-datadog-parent-id: 0` (test is root), `x-datadog-sampling-priority: 1` (Agent keeps the trace). Retained 15 days by the `Synthetics Default` retention filter. By default 100% of synthetic HTTP and browser tests generate backend traces (source: ingestion_mechanisms page, not the Synthetic APM page).
- **Profiles**: automatic when both tracing and Continuous Profiler run in the process.
- **DBM**: inject trace IDs into DBM data collection (Connect DBM and Traces).
- **Infrastructure**: Trace View shows host/container metrics, processes, network for the span; `service` tag joins APM to infra, logs and custom metrics.

Sources: https://docs.datadoghq.com/tracing/other_telemetry/, https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python/, https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/, https://docs.datadoghq.com/synthetics/apm/, https://docs.datadoghq.com/profiler/connect_traces_and_profiles/

### APM pricing basics
- Tiers: **APM** $31/host/month; **APM Pro** $35 (adds Data Streams Monitoring); **APM Enterprise** $40 (adds DSM + Continuous Profiler with **4 profiled containers per host**, extra $2/container). Universal Service Monitoring included in all tiers.
- Every APM host includes **1 million indexed spans and 150 GB of ingested spans per month** (pooled). Fargate task: $6/task/month, 195,000 indexed spans + 30 GB ingested. Lambda: 150,000 indexed spans per 1M invocations.
- Overage: **$1.70 per million indexed spans**, **$0.10 per GB ingested spans**. Ingestion is metered by **volume (bytes)**; billed metrics `datadog.estimated_usage.apm.ingested_bytes` and `datadog.estimated_usage.apm.indexed_spans` (`ingested_spans`, `ingested_traces` are informational). Intelligent retention filter spans are free.
- Host counting: hosts with APM sending traces counted hourly; HWMP bills the **ninth highest** hourly measurement (eighth in February) = ~99th percentile, ignoring the top 1% spikes. Fargate: average tasks measured every 5 minutes.
- Containers: bill the underlying host running the Agent; one Agent per container makes each container a host (price = APM host price x number of containers). Kubernetes: priced by **nodes, not pods**; pause containers not billed.
- Universal Service Monitoring is included in all APM tiers (APM, APM Pro, APM Enterprise) at no additional cost.
- Worked example: 5 APM hosts, 30M indexed, 900 GB ingested -> $155 + 25 x $1.70 + 150 x $0.10 = $212.50.
- APM Edge Devices: standard Agent 7.75.0+ with `DD_APM_MODE=edge` / `apm_config.mode: edge`; the Datadog IoT Agent does not support APM; no OTel support.
- Usage dashboards: APM Traces Estimated Usage, APM Ingestion Reasons. `sampling_service` attributes ingested bytes to the service that made the sampling decision.

Sources: https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/, https://docs.datadoghq.com/tracing/trace_pipeline/metrics/

### Common pitfalls
- A retention filter (even at 0%) does not reduce ingestion or the ingested-bytes bill; change sampling instead.
- Lowering ingestion sampling does not change Requests/Errors/Latency graphs or monitors on trace metrics (Datadog SDKs); OTel SDK sampling does.
- Custom span tags cannot be used to filter trace metrics; use span-based custom metrics or indexed-span queries.
- Searching beyond 15 minutes only sees indexed spans.
- Data retention table lists APM indexed spans as "15 or 30 days, determined by customer plan"; intelligent filter spans 30 days.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/data_security/data_retention_periods/

## Tracing Architectures

### Core data model: trace, span, root span, service entry span
- **Trace**: tracks the time spent by an application processing a request and the status of that request. Each trace consists of **one or more spans**. Distributed calls across services are stitched together because a trace ID is injected/extracted through headers.
- **Span**: a logical unit of work in a distributed system for a given period. Multiple spans construct a trace.
- **Trace root span**: the *first* span of a trace. It is the entry-point method of the traced request; its start marks the beginning of the trace.
- **Service entry span**: a span that is the entrypoint method for a request *to a service*. In the flame graph you spot it because its immediate parent is a **different color** (a different service). Every root span is also a service entry span, but a trace has many service entry spans. Glossary example: `rack.request` (root span and service entry span), `aspnet_coremvc.request`, the topmost green span below it, and every orange `mongodb` span are service entry spans.
- **Parent/child**: each span (except the root) points to its parent with `parent_id`; children are nested work. Only one parent per span; other causal relationships use span links.
- **Execution time**: total time a span is active (not waiting for a child span). With concurrent children, overlapping time is divided by the number of concurrently active spans.
- **Service**: groups endpoints, queries or jobs that do a piece of work (for example a `web-store` API service, a `payment-db` database service, a `crond` job service). Found in the Software Catalog (UI: Catalog), the Service Map and per-service Service pages.
- **Resource**: a particular domain of the application: typically an instrumented web endpoint, database query or background job. Example resource names: `GET /productpage`, `ShoppingCartController#checkout`. Each resource has a Resource page with trace metrics.
- **Operation name (span name)**: groups resources under a static name, for example `web.request` for web endpoints, `db.query` for DB queries. Endpoints are connected to a service not only by the service name but also by the `span.name` of the **entry-point span** of the trace (pitfall: endpoints missing from the expected Service page).
- **Trace metrics**: computed on service entry spans (and measured spans); kept **15 months** like other metrics; calculated on 100% of traffic, not affected by ingestion controls (exception: in Lambda, `trace.<OPERATION_NAME>.hits` is calculated on sampled invocations only).
- **Span summary** table: only for resources containing service entry spans; shows average spans per trace, % of traces, average duration, % execution time (helps detect N+1 queries).
- Agent tracing API (`PUT http://localhost:8126/v0.3/traces`, an Agent API, not an intake API). Body = array of traces, each trace = array of spans. Span fields:
  - `trace_id` (int64, lower 64 bits; for 128-bit set upper 64 bits in `meta` tag `_dd.p.tid`, lowercase hex), `span_id` (int64, unsigned 64-bit), `parent_id` (int64)
  - `name` (span name, max **100** characters), `service` (max **100** characters), `resource` (max **5000** characters)
  - `start` (int64, **nanoseconds** since UNIX epoch), `duration` (int64, **nanoseconds**)
  - `error` (int32, set `1` for error, add message/type/stack in `meta`), `meta` (string to string), `metrics` (string to float64), `type` (`web`, `db`, `cache`, `custom`)
  - All spans of a trace share the same `trace_id`; `trace_id` and `span_id` must differ.
- **IDs**: SDKs generate **128-bit trace IDs** and **64-bit span IDs** by default; Datadog accepts 128- or 64-bit trace IDs and only 64-bit span IDs. To generate 64-bit trace IDs set `DD_TRACE_128_BIT_TRACEID_GENERATION_ENABLED=false`. 128-bit Datadog trace IDs keep randomness in the **lower-order 64 bits** (W3C recommendation) so 64-bit and 128-bit spans of the same trace still match.
- **Trace view**: header shows root span's service, resource, trace ID, end-to-end duration, start time. Visualizations: **Flame Graph** (default; group by Service (default), Base service, Host or Container), **Span List**, **Waterfall**, **Map**. In Map view, a service node with an erroring service entry span gets a red border; inferred services have a dashed outline (purple background on the map). Traces over **100MB** open in Trace Preview mode (service entry spans, error spans, long-running spans, linked spans).
- Service Map: built from complete traces including root spans; nodes/edges age out after **30 days** without traces.

Sources: https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/glossary/, https://docs.datadoghq.com/tracing/guide/send_traces_to_agent_by_api/, https://docs.datadoghq.com/tracing/guide/span_and_trace_id_format/, https://docs.datadoghq.com/opentelemetry/reference/trace_ids/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/tracing/services/services_map/, https://docs.datadoghq.com/serverless/aws_lambda/configuration/

### Span tags vs span attributes, reserved attributes, span kind
- **Span attributes** = content of the span, collected by automatic or manual instrumentation (for example `http.url`, `http.status_code`, `error.message`). Query with `@`: `@http.url`, `@peer.db.name:users @peer.db.system:postgres`. Shown in the **Info** tab of the trace side panel.
- **Span tags** = context enrichment from host, container or Catalog (host tags `hostname`, `availability-zone`, `cluster-name`; container tags `container_name`, `kube_deployment`, `pod_name`). Queried **without** `@`. Shown in the **Infrastructure** tab.
- **Reserved attributes** (present on every span, queryable without `@`): `env`, `service`, `operation_name`, `resource_name`, `status`, `ingestion_reason`, `trace_id`.
- Facets are NOT required to search spans, generate metrics from spans, or index spans with retention filters. String fields can only become facets; numeric fields can become facets or measures. Measures support units (time, bytes), for example `duration:>20ms`.
- Span tag naming domains: Reserved, Core, Network communications, HTTP requests, Database, Message queue, Remote procedure calls, Errors (full list in Default Standard Attributes).
- APM core attributes: `language` (`cpp`, `dotnet`, `go`, `jvm`, `javascript`, `php`, `python`, `ruby`), `env` (from `DD_ENV`), `version` (from `DD_VERSION`), `component` (library/integration that created the span), **`span.kind`** = `server`, `client`, `producer`, `consumer` or `internal` (OpenTelemetry SpanKind).
- HTTP request/response headers (`http.request.headers.*`) are not collected by default; configure with `DD_TRACE_HEADER_TAGS`.
- Base service / overrides: base service = default `DD_SERVICE`; **integration override** = service name set automatically by an integration (for example on DB client spans); **custom override** = set manually. In the trace side panel the base service is the `@base_service` attribute; overridden name is the `service` reserved attribute; the inferred entity comes from peer attributes.

Sources: https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention/, https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/standard-attributes/?product=apm, https://docs.datadoghq.com/tracing/guide/base_service/

### Trace context propagation
- Definition: passing trace identifiers (trace ID, parent span ID, sampling decision) between services, injected into headers by the caller and extracted by the callee, so Datadog can stitch spans into one distributed trace. Automatic with auto-instrumentation.
- **Default formats (extract and inject)**: `datadog,tracecontext,baggage` (Datadog takes higher precedence when extracting). This maximizes compatibility with older Datadog SDKs while interoperating with OpenTelemetry (W3C).
- Supported values: `datadog`, `tracecontext` (W3C Trace Context), B3 single (language-dependent value, for example `b3` in Python/Ruby, `b3 single header` in Java/Go/Node), `b3multi`, `baggage` (not in Rust), `none` (do nothing). Java also supports `xray`.
- Env vars:
  - `DD_TRACE_PROPAGATION_STYLE`: comma-separated list for both extraction and injection; can be overridden by the extract/inject-specific variables.
  - `DD_TRACE_PROPAGATION_STYLE_EXTRACT` / `DD_TRACE_PROPAGATION_STYLE_INJECT`: highest precedence for extraction/injection; use when a service must accept one format and send another.
  - `OTEL_PROPAGATORS`: both extraction and injection; **lowest** precedence; ignored if any Datadog propagation variable is set; use only when migrating from the OTel SDK to the Datadog SDK.
  - `DD_TRACE_PROPAGATION_BEHAVIOR_EXTRACT`: `continue` (default; continue valid incoming trace), `restart` (always start a new trace; a valid incoming context becomes a **span link** on the service entry span), `ignore` (new trace, headers ignored).
- Multiple formats: extraction follows list order; the **first valid context continues the trace; additional valid contexts become span links**. `baggage` is added to the existing context.
- Datadog headers: `x-datadog-trace-id` (lower 64 bits of the 128-bit trace ID, decimal), `x-datadog-parent-id` (64-bit span ID of current span, decimal), `x-datadog-origin` (product that started the trace: `rum`, `synthetics`, `synthetics-browser`), `x-datadog-sampling-priority` (sampling decision, integer), `x-datadog-tags` (supplemental trace state incl. the **higher 64 bits** of the trace ID in hex). Python: `DD_TRACE_X_DATADOG_TAGS_MAX_LENGTH` default 512 (0 disables).
- Java system properties: `-Ddd.trace.propagation.style=...`, `-Dotel.propagators=...`, `.inject`, `.extract`. Ruby: `c.tracing.propagation_extract_style` / `propagation_inject_style`. .NET history: since 2.48.0 default `datadog, tracecontext`; before that `tracecontext, Datadog`; before 2.22.0 only Datadog injection. Rust SDK (Preview, built on OTel SDK) supports `datadog` and `tracecontext` only, manual propagation with `HeaderInjector`/`HeaderExtractor`.
- Pitfalls: message queues may lose context (manual extract/inject APIs exist, for example .NET `SpanContextExtractor`/`SpanContextInjector`, PHP `consume_distributed_tracing_headers`).

Sources: https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/, https://docs.datadoghq.com/tracing/glossary/#trace-context-propagation, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/

### Baggage
- Baggage = key-value pairs (business/contextual data) propagated across service boundaries alongside traces (W3C Baggage headers). Enabled by default (part of `datadog,tracecontext,baggage`); to disable set `DD_TRACE_PROPAGATION_STYLE=datadog,tracecontext`.
- Baggage as span tags: by default keys `user.id`, `session.id`, `account.id` are added as span tags named `baggage.<key>` (for example `baggage.user.id`). Python: `DD_TRACE_BAGGAGE_TAG_KEYS` (`*` = all). Min versions: Java 1.52.0, Python 3.7.0, Ruby 2.20.0, Go 2.2.2, .NET 3.23.0, Node 5.54.0, PHP 1.10.0, C++ 1.9.0 (Nginx only); not in Rust.

Sources: https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/#baggage, https://docs.datadoghq.com/tracing/glossary/#baggage

### Span links
- OpenTelemetry concept, supported by Datadog for OTel SDKs and Datadog SDKs. Correlate spans that are **causally related but have no parent-child relationship**, within one trace or across traces. Forward and backward links supported.
- Use cases (fan-in, listed under "Common use cases"): scatter-gather / map-reduce, message aggregation (for example Kafka Streams), transactional messaging, event sourcing. The overview adds that links are useful for systems that execute requests in batches or process events asynchronously.
- Creating: Datadog SDK API in **Python, Node.js, Go, PHP**; for **Java, .NET, Ruby** use the **OpenTelemetry API** with the Datadog SDK. C++/Proxy not yet supported. OTel SDK links arrive through OTLP ingest.
- Minimums: **Agent v7.52.0+** for Datadog SDK span links; SDKs Go 1.61.0, Java 1.26.0, .NET 2.53.0, Node 5.3.0, PHP 0.97.0, Python 2.5.0, Ruby 2.0.0.
- Viewing: Trace Explorer > trace view > **Span Links** tab. Linked spans display only when the corresponding spans are **ingested and indexed** (for example by a retention filter).
- Propagation link: with multiple valid incoming contexts or `restart` extract behavior, extra contexts become span links.
- Serverless **Span Auto-linking** (Python/Node.js): links spans when async segments cannot carry context, for S3 change notifications (`PutObject`, `CompleteMultipartUpload`, `CopyObject`) and DynamoDB Streams (`PutItem` needs extra config, `UpdateItem`, `DeleteItem`, `BatchWriteItem`, `TransactWriteItems`). Sampling and retention filters can hide auto-links.

Sources: https://docs.datadoghq.com/tracing/trace_collection/span_links/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/serverless/aws_lambda/distributed_tracing/#span-auto-linking

### Inferred services and peer tags
- Datadog discovers uninstrumented dependencies (databases, queues, third-party APIs) by analyzing **outbound requests** (client spans) of instrumented services, and collects performance metrics for them. Browse in the Catalog by entity type (database, queue, third-party API); inferred services have dashed outlines in flame graph/map.
- Agent setup: **v7.60.0+ nothing to configure** (`apm_config.compute_stats_by_span_kind` and `apm_config.peer_tags_aggregation` on by default). v7.55.1-v7.59.1: set both to `true` (`DD_APM_COMPUTE_STATS_BY_SPAN_KIND`, `DD_APM_PEER_TAGS_AGGREGATION`). v7.50.3-v7.54.1: also set `apm_config.peer_tags` (`DD_APM_PEER_TAGS`) list. OTel Collector: recommended `span_metrics` connector dimensions; Datadog Connector needs collector-contrib v0.95.0+ with `compute_stats_by_span_kind`, `peer_tags_aggregation`, `peer_tags`.
- Naming: external APIs default to `net.peer.name` (for example `api.stripe.com`); databases default to `db.instance`. Rename with renaming rules.
- Peer tags (derived from source attributes): `peer.db.name` (`db.name`, `mongodb.db`, `db.instance`, `cassandra.keyspace`, `db.namespace`), `peer.db.system` (`db.system`, `db.type`...), `peer.hostname` (`peer.hostname`, `hostname`, `net.peer.name`, `db.hostname`, `out.host`, `http.host`, `server.address`, ...), `peer.messaging.destination` (`topicname`, `messaging.destination`, `amqp.queue`...), `peer.aws.sqs.queue` (`queuename`), `peer.aws.s3.bucket` (`bucketname`, `aws.s3.bucket`), `peer.aws.dynamodb.table` (`tablename`), `peer.aws.kinesis.stream` (`streamname`), `peer.kafka.bootstrap.servers`, `peer.rpc.service`, `peer.rpc.system`, `peer.service`.
- Precedence: **Database** `peer.db.name` > `peer.aws.s3.bucket`/`peer.aws.dynamodb.table`/`peer.cassandra.contact.points`/`peer.couchbase.seed.nodes` > `peer.hostname` > `peer.db.system`. **Queue** `peer.messaging.destination` > `peer.kafka.bootstrap.servers`/`peer.aws.sqs.queue`/`peer.aws.kinesis.stream` > `peer.messaging.system`. **Inferred service** `peer.service` > `peer.rpc.service` > `peer.hostname`. `peer.service` is highest priority overall if set; Datadog never sets it for inferred DBs and queues.
- IP-looking peer values are redacted to **`blocked-ip-address`** (avoids high cardinality), so such a dependency can appear.
- Migrate to global default service naming: `DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED=true` stops integrations setting service names different from `DD_SERVICE` (integration overrides). Warning: impacts monitors, dashboards, retention filters, span metrics that use old names; update to `service:<DD_SERVICE>`.
- Not available by default on gov sites (request form).

Sources: https://docs.datadoghq.com/tracing/services/inferred_services/, https://docs.datadoghq.com/tracing/guide/base_service/

### OpenTelemetry vs Datadog tracing architectures
- Two decisions: how to instrument (Full OTel SDK+API; OTel API with Datadog SDK; OTel instrumentation libraries with Datadog SDK) and how to send data.
- Send options (current docs):
  1. **Datadog Agent with DDOT Collector (Recommended)**: Datadog Distribution of OTel Collector inside the Agent; adds Fleet Automation, Live Container Monitoring, Kubernetes Explorer, Live Processes, CNM, USM, 1,000+ integrations. Ships datadogexporter, datadogconnector, spanmetricsconnector, otlp/otlphttp exporters, tailsampling, transform, etc.; custom components possible. Custom Datadog components: Infrastructure Attribute Processor (k8s tags), Converter, DD Flare Extension.
  2. **Upstream OpenTelemetry Collector** (self-managed, for tail-based sampling and transformations). Current recommended config (Collector Contrib v0.154.0+): `otlp` receiver (gRPC `0.0.0.0:4317`, HTTP `0.0.0.0:4318`) > `resource_detection` processor > `forward/traces_sample` connector + **`span_metrics` connector** (RED metrics powering Catalog, Service page, Resource page) > **`otlp_http` exporter** to `https://otlp.<DD_SITE>` with header `dd-api-key`, `zstd` compression, batches 2 MiB-4 MiB (413 means too big). `datadog` **extension** only reports config for Fleet Automation (exports no telemetry). `cumulativetodelta` for metrics. Put sampling (for example `tail_sampling`) in the second `traces/sample` pipeline so span metrics are computed on **all** traces. Tail sampling across multiple Collectors needs a gateway that routes all spans of a trace to one Collector. Not for serverless/ECS Fargate/EKS Fargate/Lambda.
     - **Datadog Exporter + Datadog Connector** (older way): exporter forwards traces/metrics/logs without the Agent; connector computes trace metrics. Still supported, existing configs need not migrate, but new configs should use OTLP HTTP + `span_metrics`. Batch processor required in non-dev; trace intake 3.2MB.
  3. **OTLP Ingest in the Agent**: OTel SDK exports OTLP to the local Agent. Since Agent 6.32.0/7.32.0 (traces, metrics), 6.48.0/7.48.0 (logs). Off by default. `otlp_config.receiver.protocols.grpc.endpoint` (default port **4317**) / `http.endpoint` (**4318**); env `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_GRPC_ENDPOINT` / `..._HTTP_ENDPOINT` (must be passed to both core Agent and trace Agent; use `0.0.0.0` in containers). When enabled, **metrics and traces on by default; logs off** (enable `logs_enabled: true` + `otlp_config.logs.enabled: true` / `DD_OTLP_CONFIG_LOGS_ENABLED`). Helm: `datadog.otlp.receiver.protocols.grpc.enabled: true`. App side: `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317|4318`. **Agent must run on the same host** as the OTel-generating app/collector. OTel SDK data cannot use AAP, Continuous Profiler, Ingestion Rules.
  4. **Direct OTLP intake** (no Agent/Collector; serverless, managed platforms): limits `/v1/traces` 15 MiB uncompressed, `/v1/logs` 5.1 MiB, `/v1/metrics` 512 KiB compressed (413 if exceeded).
- Compatibility table: Datadog SDK + DDOT supports everything; OTel SDK setups lack **App and API Protection, Continuous Profiler, Data Jobs Monitoring, Data Streams Monitoring, RUM (full)**; OTel SDK + upstream Collector also lacks DBM, CNM, Live Containers, Live Processes, USM. Span links and distributed tracing work everywhere; Direct OTLP trace metrics reflect only sampled spans.
- Best practices: do not mix Datadog SDK and OTel SDK in one app (exception: Python needs both installed for OTel API support); do not run Datadog Agent and a separate OTel Collector on the same host. EKS Fargate not supported for the Collector (wrong host billing).
- OTel API with Datadog SDK: set `DD_TRACE_OTEL_ENABLED=true` (default false).
- Unified service tagging in OTel: resource attributes `service.name`, `deployment.environment.name`, `service.version`.
- Service-entry span mapping for OTel: root span, `server`, `consumer` = service entry span; `client`, `producer` = measured span; `internal` = no trace metrics. Enable: automatic with OTLP HTTP + `span_metrics`; Datadog Exporter/Connector `traces::compute_top_level_by_span_kind: true` (v0.100.0+); Agent OTLP ingest `apm_config.features: ["enable_otlp_compute_top_level_by_span_kind"]` (v7.53.0+). Change kind with the `transform` processor.
- Operation names for OTel spans: `enable_operation_and_resource_name_logic_v2` (default on DDOT Agent 7.65+, Collector v0.126.0+, OTLP ingest Agent 7.66+). Rules: `operation.name` wins; HTTP server `http.server.request`, client `http.client.request`; DB client `<db.system>.query`; messaging `<system>.<operation>`; no match server `server.request`, client `client.request`, unspecified `internal`. Opt out: `DD_APM_FEATURES=disable_operation_and_resource_name_logic_v2` or feature gate `-datadog.EnableOperationAndResourceNameV2`.
- Glossary: OTLP Receiver accepts OTLP; OTLP is OTel's native protocol.

Sources: https://docs.datadoghq.com/opentelemetry/, https://docs.datadoghq.com/opentelemetry/setup/, https://docs.datadoghq.com/opentelemetry/setup/collector_exporter/, https://docs.datadoghq.com/opentelemetry/setup/collector_exporter/datadog_exporter/, https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent/, https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest/, https://docs.datadoghq.com/opentelemetry/setup/ddot_collector/, https://docs.datadoghq.com/opentelemetry/compatibility/, https://docs.datadoghq.com/opentelemetry/mapping/service_entry_spans/, https://docs.datadoghq.com/opentelemetry/migrate/migrate_operation_names/, https://docs.datadoghq.com/opentelemetry/reference/concepts/

### Serverless tracing with the Datadog Lambda Extension
- Architecture: runtime-specific **Datadog Lambda Library** + **Datadog Lambda Extension**. The extension is a lightweight version of the Datadog Agent running inside the Lambda execution environment; submits custom metrics, enhanced metrics, traces and logs asynchronously, directly to Datadog; collects logs via the Lambda Telemetry API (no CloudWatch needed). Analogous to Agent + SDK on hosts.
- Extension vs **Forwarder**: extension skips CloudWatch Logs (lower cost) and is a simple Lambda layer (no subscription filter per log group). Forwarder still needed for logs of other AWS services (API Gateway, AppSync, Lambda@Edge). Only logs from many functions: Forwarder OK; metrics + traces: migrate to the extension.
- Next-generation extension: GA; v67-v87 opt out with `DD_EXTENSION_VERSION: compatibility`; **v88+ only next-gen**. APM tracing supported for Python, Node.js, Go, Java, .NET, Ruby. v67+ optimized cold starts (set `DD_SERVERLESS_APPSEC_ENABLED=false`). v90+ supports Lambda Managed Instances (detected via `AWS_LAMBDA_INITIALIZATION_TYPE`; continuous background flushing, default 30 s).
- Overhead: added cold-start init; extension flush time counted in `aws.lambda.duration` / `aws.lambda.enhanced.duration` but happens after the response is returned. Real function time: `aws.lambda.enhanced.runtime_duration`. Flush overhead: `aws.lambda.post_runtime_extensions_duration` / `aws.lambda.enhanced.post_runtime_duration`. Default: flush at end of each invocation; with steady invocations (more than once per minute) it batches and flushes periodically. Far-region functions: `DD_SERVERLESS_FLUSH_STRATEGY=periodically,60000`.
- Install (Python example): layers `arn:aws:lambda:<REGION>:464622532012:layer:Datadog-Extension:<v>` and `Datadog-<RUNTIME>:<v>` (ARM suffix `-ARM`), container image `public.ecr.aws/datadog/lambda-extension:<TAG>`. Handler redirect: set handler to `datadog_lambda.handler.handler` and `DD_LAMBDA_HANDLER=<original handler>`. Env: `DD_SITE`, `DD_API_KEY_SECRET_ARN` (plaintext secret), `DD_TRACE_ENABLED=true`, `DD_ENV`/`DD_SERVICE`/`DD_VERSION`. **Do not set `DD_AGENT_HOST` or `DD_TRACE_AGENT_URL`** in serverless. Tools: Serverless Plugin, CloudFormation macro (SAM), CDK construct, Datadog CLI, Terraform; quick start via Fleet Automation.
- Distributed tracing: Python/Node.js automatically trace through API Gateway, SQS, SNS, SNS->SQS, Kinesis, EventBridge, DynamoDB, S3, Step Functions; inject context in outgoing AWS SDK requests and extract from the Lambda event. Inferred spans for managed triggers (disable `DD_TRACE_MANAGED_SERVICES=false`); rename upstream services with `DD_SERVICE_MAPPING=old:new`; newer layers name services after the resource (`[function_name]`, `[queue_name]`...), revert with `DD_TRACE_AWS_SERVICE_REPRESENTATION_ENABLED=false`.
- Custom/non-HTTP propagation: put Datadog context in payload `_datadog` (Python `get_dd_trace_context`, Node `getTraceHeaders`), extract in consumer with `DD_TRACE_EXTRACTOR=<FILE NAME>.<FUNCTION NAME>`. Hybrid Lambda + hosts: install `dd-trace` everywhere (recommended). X-Ray merging: `DD_MERGE_XRAY_TRACES=true` (Ruby `DD_MERGE_DATADOG_XRAY_TRACES`), Node/Python only, may cost more.
- Sampling: `DD_TRACE_SAMPLING_RULES` (for example `[{"sample_rate":0.1}]`); `DD_TRACE_SAMPLE_RATE` deprecated. Head-based: set rate on the root service.
- Logs/traces link with extension: Lambda request ID on the `aws.lambda` span (`request_id`) and logs (`lambda.request_id`). With Forwarder: `dd.trace_id` injection (`DD_LOGS_INJECTION`).
- OpenTelemetry on Lambda: (recommended) OTel API with Datadog SDK, `DD_TRACE_OTEL_ENABLED=true`; or any OTel SDK exporting OTLP to the extension (Preview, extension v53+) with `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_HTTP_ENDPOINT=localhost:4318` or `..._GRPC_ENDPOINT=localhost:4317`; do **not** add the Datadog tracing layer; custom metrics over the extension's OTLP endpoint not supported. Useful for runtimes without Datadog tracing (for example Rust, PHP).

Sources: https://docs.datadoghq.com/serverless/libraries_integrations/extension/, https://docs.datadoghq.com/serverless/aws_lambda/, https://docs.datadoghq.com/serverless/guide/extension_motivation/, https://docs.datadoghq.com/serverless/aws_lambda/distributed_tracing/, https://docs.datadoghq.com/serverless/aws_lambda/configuration/, https://docs.datadoghq.com/serverless/aws_lambda/instrumentation/python/, https://docs.datadoghq.com/serverless/aws_lambda/opentelemetry/

### Common pitfalls and changes since the 2025 guide
- Root span is not the same as a service entry span: one root per trace, many entry spans.
- `OTEL_PROPAGATORS` loses to any `DD_TRACE_PROPAGATION_*` variable.
- Span links are not visible unless the linked spans are indexed.
- Datadog Exporter is no longer the recommended Collector path for new setups (OTLP HTTP exporter + `span_metrics` is); DDOT Collector is the overall recommended OTel option.
- Service Catalog is now Software Catalog (UI "Catalog").
- Lambda extension v88+ is next-gen only.

Sources: https://docs.datadoghq.com/opentelemetry/setup/collector_exporter/, https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/, https://docs.datadoghq.com/serverless/libraries_integrations/extension/

## Language Level Differences — Automatic Instrumentation

### Big picture: SSI vs manually managed SDKs
- Instrumentation = SDK setup (add a Datadog SDK) + span creation. Spans are generated automatically as soon as the SDK is loaded ("auto-instrumentation"); custom spans are optional.
- Two ways to get the SDK in:
  - **Single Step Instrumentation (SSI)** (recommended): Datadog installs and loads SDKs into application processes *at runtime* with a single command. No code changes. Low setup complexity, standard defaults with optional overrides.
  - **Manually managed SDKs**: you install/configure the SDK in code or build process. Code changes: yes. Full control through env vars and code.
- Custom spans without code changes: **Dynamic Instrumentation** (rules in the Datadog UI, applied at runtime, no redeploy). Custom spans in code: **code-based custom instrumentation** (requires deploy). Options can be combined (SSI + custom code spans; manual SDK + Dynamic Instrumentation).
- Agent side: `datadog.yaml` `apm_config` `enabled: true`; Agent listens for traces at `http://localhost:8126`. Containers: `apm_non_local_traffic: true` / `DD_APM_NON_LOCAL_TRAFFIC=true`.
- SDK connection default: tries UDS `/var/run/datadog/apm.socket` first, falls back to `http://localhost:8126`. Override with `DD_TRACE_AGENT_URL` (e.g. `http://custom-hostname:1234` or `unix:///var/run/datadog/apm.socket`). Stats: `/var/run/datadog/dsd.socket` then `localhost:8125`.
- Official SDK languages: Java, Python, Ruby, Go, Node.js, PHP, C++, Rust, .NET Core, .NET Framework (+ Android, iOS). Unsupported language -> **community SDKs**.
- Every language has a *Compatibility Requirements* page (runtime versions, OS/arch, integrations). Languages listed there: Java, Python, Ruby, Go, Node.js, PHP, C++, .NET Core, .NET Framework, Rust.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/

### Java (dd-java-agent)
- Download `dd-java-agent.jar`: `wget -O dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'` (or `curl -Lo`, or Dockerfile `ADD`). Latest build of a major: `https://dtdg.co/java-tracer-vX` (e.g. `-v1`; no minor numbers). Specific versions: Maven Central. RC builds on GitHub releases (test outside prod).
- Run: `java -javaagent:/path/to/dd-java-agent.jar -Ddd.profiling.enabled=true -Ddd.logs.injection=true -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar path/to/your/app.jar`
- **`-javaagent` must come BEFORE `-jar`**, as a JVM option, not an application argument. Anything after `-jar app.jar` is passed to the app.
- **Never add `dd-java-agent` to the classpath** (unexpected behavior).
- Each setting is an env var or a system property: `DD_ENV`/`dd.env`, `DD_SERVICE`/`dd.service`, `DD_VERSION`/`dd.version`, `DD_LOGS_INJECTION`/`dd.logs.injection` (MDC injection), `DD_PROFILING_ENABLED`/`dd.profiling.enabled`, `DD_TRACE_SAMPLE_RATE`/`dd.trace.sample.rate`, `DD_TRACE_SAMPLING_RULES`/`dd.trace.sampling.rules`. Since 1.18.3, with Remote Configuration, `DD_LOGS_INJECTION` and `DD_TRACE_SAMPLE_RATE` can be set in the Software Catalog UI.
- App servers: Spring Boot -> `my_app.conf` with `JAVA_OPTS=-javaagent:...`; Tomcat Linux -> `setenv.sh` `CATALINA_OPTS="$CATALINA_OPTS -javaagent:..."`; Tomcat Windows service -> `tomcat@VERSION_MAJOR@w.exe` > Java tab > Java Options; JBoss standalone -> `standalone.conf` `JAVA_OPTS` (Windows `standalone.conf.bat`), domain mode -> `domain.xml` `<option value="-javaagent:..."/>`; Jetty -> `jetty.sh` `JAVA_OPTIONS` or `start.ini` under `--exec`; WebSphere -> Servers > WebSphere application servers > Java and Process Management > Process Definition > Java Virtual Machine > Generic JVM arguments.
- How it works: JVM `java-agent` instrumentation capability; a registered java-agent modifies class files **at load time**. **Classes loaded with a remote ClassLoader are not instrumented automatically.** Captures timing (JVM NanoTime), tags, unhandled errors + stack traces, total count of traces.
- Remote Configuration enabled by default; disable with `DD_REMOTE_CONFIG_ENABLED=false` / `-Ddd.remote_config.enabled=false`.
- Java 24+: may see JNI native access warnings -> `--enable-native-access=ALL-UNNAMED` (SSI adds this flag automatically on 24+).
- Compatibility: latest tracer supports JVM 8+. Tracer v1: Java 8-17 GA (x86/x86-64; arm64 Linux/Mac Preview), 18-27 GA (incl. arm64), 28+ Preview. Java 7 only on tracer v0 = End-of-life. No early-access Java versions supported. Oracle JDK, OpenJDK, GraalVM.
- Integrations: most enabled by default. Disable all: `DD_INTEGRATIONS_ENABLED=false` / `-Ddd.integrations.enabled=false`. Per integration: `DD_INTEGRATION_<NAME>_ENABLED=true` / `-Ddd.integration.<name>.enabled=true`. Preview integrations disabled by default (e.g. `-Ddd.integration.jdbc-datasource.enabled=true`, `grizzly-client`, `hazelcast`).

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/

### Python (ddtrace)
- Install: `pip install ddtrace` (pip >= 18.0.0).
- Run: **prefix the entry-point command with `ddtrace-run`**: `python app.py` -> `ddtrace-run python app.py` (e.g. `DD_SERVICE=... DD_ENV=... DD_VERSION=... ddtrace-run python app.py`).
- When `ddtrace-run` cannot be used: `import ddtrace.auto`, normally **the first thing** at application start-up. Profiling equivalent: `DD_PROFILING_ENABLED=true ddtrace-run ...` or `import ddtrace.profiling.auto`.
- `ddtrace-run --info`: checks configuration/Agent connectivity; reflects env-var config only, **not** changes made in code at runtime.
- Config via env vars (recommended for Agent host/port etc.). `DD_PATCH_MODULES="redis:true,requests:false"` overrides which integrations are auto-patched by `ddtrace.auto`/`ddtrace-run` (enable off-by-default ones or disable default ones). `DD_TRACE_<INTEGRATION>_ENABLED` toggles one integration. Beta `snowflake` integration is off by default; `DD_PATCH_MODULES=snowflake:true` opts in.
- `DD_TRACE_ENABLED` default `true`; when disabled instrumentation still runs but no trace data is sent. `DD_TRACE_AGENT_PORT` default `8126`; must match Agent `receiver_port`/`DD_APM_RECEIVER_PORT`. Host precedence: `DD_TRACE_AGENT_URL` > `DD_TRACE_AGENT_HOSTNAME` > `DD_AGENT_HOST` > UDS `/var/run/datadog/apm.socket` > `localhost`.
- Versions: dd-trace-py v4 (GA, min Agent 7.63.0) drops Python 3.8 -> CPython 3.9+. v3 Maintenance until May 31, 2026 (3.8+). v2 EOL (3.7-3.13). v3.0.0 dropped Python 3.7. Lifecycle: GA 12 months after x.0.0, Maintenance 6 months, EOL at 18 months. Linux, macOS, Windows supported.
- Compatibility table has an "Automatic" column: some integrations (Django, Flask, aiohttp client) are patched automatically; others (asgi, Bottle, Falcon, CherryPy, aiohttp server) are not and need manual setup.
- Pitfall (SSI): preforking WSGI servers (uWSGI prefork, gunicorn `--preload`, mod_wsgi daemon preload) can crash with SIGSEGV under SSI -> disable SSI for service, use lazy loading, or install manually with `pip install ddtrace` + `ddtrace-run`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/, https://ddtrace.readthedocs.io/en/stable/installation_quickstart.html, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/

### Node.js (dd-trace)
- Latest tracer supports Node.js `>=18`. `npm install dd-trace`. EOL Node 16: `npm install dd-trace@latest-node16` (dd-trace 4.x). With SSI or Serverless the library is pre-installed (add as dev dependency `-D` for local tracing). `dd-trace-api` = public API package for custom instrumentation with SSI/Serverless.
- **The SDK must be imported and initialized BEFORE any other module**; otherwise missing URL routes, disconnected/missing spans.
- Command line: `node --require dd-trace/init app.js` (config via env vars only). Programmatic config: `node --require ./dd-trace.js app.js` where file contains `require('dd-trace').init({...})`.
- Can't control CLI (e.g. Next.js `next start`, Nest.js): `NODE_OPTIONS='--require dd-trace/init' npm start` (also applies to child Node processes) or edit `package.json` start script.
- ESM apps need an *additional* argument: Node < 20.6 `--loader dd-trace/loader-hook.mjs`; Node >= 20.6 `--import dd-trace/register.js`; shorthand for both on >= 20.6: `--import dd-trace/initialize.mjs`.
- Transpilers (TypeScript, Webpack, Babel): init the SDK in an external file and import it as a whole.
- `DD_TRACE_ENABLED` default `true`; some instrumentation occurs at import time; to fully disable, import conditionally or set `DD_TRACE_ENABLED=false`.
- How it works: intercepts `require()` calls. **Bundlers** replace `require()` so dd-trace still sees built-ins (`fs`, `http`) but misses third-party libraries (express routes, mysql queries). Fix: mark modules as external, or use bundler plugins: `dd-trace/esbuild` (dd-trace@3+, Node 16.17/18.7+), experimental `dd-trace/webpack` (dd-trace@5.94.0+), Next.js `webpack` externals in `next.config.js`. Native modules (`@datadog/*`, `.node`) must stay external; ship a small `node_modules/`. Dynamic Instrumentation is not supported with bundling.
- Release lines: semver; previous major enters maintenance when next major releases, for one year. Odd-numbered (non-LTS) Node versions get no specific releases.
- SSI limitation: ESM modules are not instrumented by SSI (min Node.js SDK 4.0).

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/nodejs/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/nodejs/

### Go (dd-trace-go v2 + Orchestrion)
- Go is compiled: **no runtime agent / no SSI injection**. Two ways:
  1. **Compile-time instrumentation with Orchestrion**: no source code changes, max coverage (your code + all dependencies + standard library), ideal for CI/CD. Exclusive: App and API Protection **Exploit Prevention** (RASP, e.g. LFI).
  2. **Manual instrumentation**: dd-trace-go + integration (contrib) packages, e.g. `github.com/DataDog/dd-trace-go/contrib/gin-gonic/gin/v2`; complete control, requires source changes.
- Orchestrion requirements: two latest Go runtime releases; app managed with Go modules (vendoring supported).
- Install: `go install github.com/DataDog/orchestrion@latest` (GOBIN/GOPATH/bin on `$PATH`), then `orchestrion pin` (registers in `go.mod`, creates `orchestrion.tool.go`), commit `go.mod go.sum orchestrion.tool.go`.
- Use (one of): `orchestrion go build .` / `orchestrion go run .` / `orchestrion go test ./...`; or `go build -toolexec="orchestrion toolexec" .`; or `export GOFLAGS="${GOFLAGS} '-toolexec=orchestrion toolexec'"` then plain `go build`.
- UST: `DD_ENV`, `DD_SERVICE`, `DD_VERSION` set in the **runtime** environment. Profiler included; enable at runtime with `DD_PROFILING_ENABLED=true`.
- `//dd:span custom_tag:tag_value` directive creates custom spans. Operation name precedence: explicit `span.name:` tag > function's declared name > first tag value (for anonymous function literals). Functions returning `error` get it attached automatically.
- `//orchestrion:ignore` prevents any modification on annotated code (caller-side only; callee/library-side integrations can't be opted out locally).
- Remove integrations: edit imports in `orchestrion.tool.go` (default imports `github.com/DataDog/dd-trace-go/orchestrion/all/v2` = everything). If you list specific ones, update manually to add new ones.
- Tracer versions: v2 recommended (GA 2025-06-04); v1 Maintenance from 2025-06-04, EOL 2025-12-31. Two latest Go releases fully supported, third newest in maintenance. Page also states Go `1.18+` and Agent `>= 5.21.1`.
- Pitfall: SSI preload doesn't work for statically linked launchers (common with Go).

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/go/

### Ruby (datadog gem v2)
- Gem is `datadog` (v2.x); legacy `ddtrace` gem = v1.x docs.
- Agent: `DD_APM_ENABLED=true` / `apm_enabled: true`; containers `DD_APM_NON_LOCAL_TRAFFIC=true`. Agent listens HTTP on `8126`; change with `DD_APM_RECEIVER_PORT` or UDS `DD_APM_RECEIVER_SOCKET`.
- Rails/Hanami: Gemfile `gem 'datadog', require: 'datadog/auto_instrument'`, `bundle install`, create `config/initializers/datadog.rb` with `Datadog.configure do |c| ... end`.
- Other Ruby apps: `gem 'datadog'`, require supported libraries first, then `require 'datadog/auto_instrument'` (**must be AFTER requiring the libraries/frameworks**), then a `Datadog.configure` block.
- Activate/configure a single integration: `c.tracing.instrument :integration_name, **options` inside `Datadog.configure`. Per-integration env var e.g. `DD_TRACE_ACTION_CABLE_ENABLED`.
- Connection priority: explicit settings > UDS `/var/run/datadog/apm.socket` > HTTP `127.0.0.1:8126`.
- Disable in tests: `DD_TRACE_ENABLED=false` or `c.tracing.enabled = false`.
- Manual spans: `Datadog::Tracing.trace(name, **options) { |span, trace| }`; spans with `nil` service or resource are discarded by the Agent.
- Compatibility: MRI 2.5 through 4.0 latest; 2.4 and older EOL; JRuby EOL (< 2.31.0). OS: Linux x86_64/aarch64; macOS dev only; Windows unimplemented.
- SSI: Ruby SDK 2.6.0+, glibc 2.17+, not Alpine/musl, Bundler >= 2.4 < 4.0. Backup `Gemfile`/`Gemfile.lock` before uninstalling SSI.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/ruby/

### .NET (CLR Profiling API)
- Auto instrumentation relies on the **.NET CLR Profiling API, which allows only one subscriber** -> run only one APM solution. (SSI compatibility page, .NET known issue: a pre-existing profiler takes precedence and no Datadog traces arrive; remove its `CORECLR_*` vars / `LD_PRELOAD` entries.)
- .NET Core: supports .NET Core 3.1, .NET 5-10. .NET Framework: >= 4.6.1.
- Install machine-wide: Windows MSI (x64 MSI instruments 64- and 32-bit apps; only x64 from v3.0.0), run as admin; scripted `Start-Process -Wait msiexec -ArgumentList '/qn /i datadog-apm.msi'`. Linux: `.deb`/`.rpm`/`tar` into `/opt/datadog` + `/opt/datadog/createLogPath.sh` (log dir `/var/log/datadog/dotnet`). Per-application: NuGet **`Datadog.Trace.Bundle`** — **does not instrument IIS apps** (use MSI for IIS). Trimmed apps: `Datadog.Trace.Trimming`.
- Enable via env vars, then restart:
  - .NET Core Linux: `CORECLR_ENABLE_PROFILING=1`, `CORECLR_PROFILER={846F5F1C-F9AE-4B07-969E-05C26BC060D8}`, `CORECLR_PROFILER_PATH=/opt/datadog/Datadog.Trace.ClrProfiler.Native.so`, `DD_DOTNET_TRACER_HOME=/opt/datadog` (Alpine: musl path `linux-musl-x64/`).
  - .NET Core Windows (non-IIS): `CORECLR_ENABLE_PROFILING=1` (MSI sets the rest).
  - .NET Framework Windows (non-IIS): `COR_ENABLE_PROFILING=1`.
  - IIS: MSI adds all required env vars; no configuration. .NET Core on IIS: app pool **.NET CLR version = No Managed Code**. Restart with `net stop /y was` then `net start w3svc` (avoid IIS Manager GUI and `iisreset.exe`). Env vars for all IIS sites: multi-string `Environment` under `HKLM\System\CurrentControlSet\Services\WAS`.
  - Windows service: multi-string `Environment` in `HKLM\System\CurrentControlSet\Services\<SERVICE NAME>`.
  - Linux service: `EnvironmentFile=` in systemd unit, or `systemctl set-environment` (all services).
- **Don't set the profiler env vars globally**: the runtime loads the library into *every* .NET process started with them.
- Custom instrumentation: from v3.0.0 requires automatic instrumentation too; add `Datadog.Trace` NuGet; `Datadog.Trace.Tracer.Instance`; keep MSI and NuGet versions in sync, don't mix majors.
- View data: APM > APM Traces.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework/

### PHP (ddtrace extension)
- Latest `dd-trace-php` needs PHP 7+; PHP 5 only up to tracer 0.99 (EOL from 1.0).
- Install the extension with the official installer: `curl -LO https://github.com/DataDog/dd-trace-php/releases/latest/download/datadog-setup.php` then `php datadog-setup.php --php-bin=all` (APM). Add `--enable-appsec` (AAP) and/or `--enable-profiling`. Windows: APM only (no appsec/profiling flags). Without `--php-bin` the installer is interactive. Alpine: `apk add libgcc` first.
- Restart PHP (PHP-FPM or Apache SAPI). Tracing is enabled by default once the extension is installed; it wraps functions/methods by modifying PHP's runtime.
- Troubleshoot: `phpinfo()` page -> `ddtrace` section diagnostics. Apache ZTS: use `-zts` extension file. Remove: unlink `98-ddtrace.ini` and `99-ddtrace-custom.ini`. CLI scripts need extra steps.
- SSI (PHP SDK 1.6.0+) auto-disables with JIT or Xdebug, ionCube Loader, NewRelic, Blackfire, pcov; force with `DD_INJECT_FORCE=true`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/php/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/

### C++ and Rust
- **C++ does not provide integrations for automatic instrumentation**; `dd-trace-cpp` is used by proxy tracing (Envoy, NGINX). Requires a C++17 toolchain; built with CMake/CPM/manual; link `dd_trace::static` or shared. Platforms: x86_64/arm64 Linux, x86_64 Windows, arm64 macOS.
- Rust also has an official SDK and a compatibility page.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/cpp/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/cpp/

### Single Step Instrumentation (SSI): how it works
- Prerequisite: remove custom instrumentation code and restart; **SSI is automatically disabled if custom instrumentation is detected**.
- The **injector** is a shared library. Linux: `LD_PRELOAD` (explicit env var or system-wide `/etc/ld.so.preload`). Docker: Datadog custom `runc` shim (`dd-shim`) injects the library and sets `LD_PRELOAD`. Kubernetes: Admission Controller (mutating webhook) mutates pod spec: init containers or Datadog CSI driver, env vars, volumes. Windows: DLL loaded by a Datadog kernel driver.
- Injector detects runtime, evaluates rules/deny list, sets env vars or args, then is done **before `main` runs** (no background process). No kernel modules/eBPF; runs with app's privileges.
- Per-runtime mechanism: Java `JAVA_TOOL_OPTIONS` with `-javaagent:`; Python `PYTHONPATH`; Node.js `NODE_OPTIONS` with `--require`/`--import`; Ruby `RUBYOPT -r`; .NET `CORECLR_*` profiler vars; PHP `PHP_INI_SCAN_DIR`; NGINX re-exec with `-g "load_module ...;"`.
- Languages SSI injects: **Java, Python, Node.js, .NET, Ruby, PHP** (Linux/Docker/K8s). **Not Go, not C++.** Windows: .NET on IIS (GA); host-wide Java + .NET in Preview.
- Minimum SDKs: Java 1.44.0, Python 2.20.1 (runtime 3.7+), Ruby 2.6.0, Node.js 4.0, .NET 3.7.0, PHP 1.6.0. If SDK or runtime unsupported, SSI falls back gracefully (app runs uninstrumented).
- **`DD_TRACE_ENABLED=false` does NOT stop SSI** from loading the SDK (injector runs first). Use platform removal steps.
- Linux distros: Amazon Linux 2022/2023, CentOS 7/8, Debian 10-12, RHEL 7-9, Ubuntu 20/22/24, Fedora 40, AlmaLinux/Oracle/Rocky 8; x86_64 + arm64. Not supported: ECS Fargate, hardened SELinux, Windows K8s node pools; EKS Fargate Preview. Tiny VMs (`t2.micro`) can time out (analyzer has one second) -> `t2.small`+.
- Enable SDK-dependent products with env vars: `DD_RUNTIME_METRICS_ENABLED`, `DD_LOGS_INJECTION`, `DD_PROFILING_ENABLED` (also `auto` = recommended for SSI), `DD_DATA_STREAMS_ENABLED`, `DD_APPSEC_ENABLED`, `DD_IAST_ENABLED`, `DD_DYNAMIC_INSTRUMENTATION_ENABLED`, `DD_DATA_JOBS_ENABLED`, `DD_APPSEC_SCA_ENABLED`; host-wide via `application_monitoring.yaml`.
- Troubleshooting: Fleet Automation (facets `single_step_instrumentation`, `single_step_instrumentation_status`; Agent 7.68.2+); injector debug `DD_APM_INSTRUMENTATION_DEBUG=true` (writes to stderr; file via `DD_APM_INSTRUMENTATION_OUTPUT_PATHS`); K8s annotation `admission.datadoghq.com/apm-inject.debug: "true"`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/, https://docs.datadoghq.com/tracing/guide/injectors/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting/

### SSI on Linux, Docker, Windows
- Linux: `DD_API_KEY=... DD_SITE=... DD_APM_INSTRUMENTATION_ENABLED=host bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"`, then **restart applications** (preload only affects newly launched processes). Pin SDKs: `DD_APM_INSTRUMENTATION_LIBRARIES=java:1,python:3` (`java`, `js`, `python`, `dotnet`, `ruby`, `php`). Verify: `cat /etc/ld.so.preload && ls /opt/datadog-packages/ | grep apm`. Update SDK: re-run install command + restart. Remove: `dd-host-install --uninstall` + restart services.
- Existing Agents: **APM > Instrument a Service** > Deploy on existing hosts > select Agents > Configure SDKs installation > rollout strategy (auto-pause after 3 consecutive failures or 10% failures) > Apply Instrumentation.
- Instrumentation rules (Agent v7.73+): APM > Service Setup > Manage Instrumentation Rules; Allow/Block rules, evaluated in order (first match wins), default allow/block; conditions on Executable, Executable Full Path, Arguments, Working Directory, Language, Entry Point File (+ IIS Application Pool on Windows); deployed via Remote Configuration within 50 seconds. Not on gov site.
- Docker: on the Docker host run installer with `DD_APM_INSTRUMENTATION_ENABLED=docker DD_NO_AGENT_INSTALL=true`, run the Agent container with `DD_APM_ENABLED`, `DD_APM_NON_LOCAL_TRAFFIC`, `DD_APM_RECEIVER_SOCKET=/var/run/datadog/apm.socket` and `-v /var/run/datadog:/var/run/datadog`. **Recreate app containers** (instrumentation applied at container creation; `docker stop`/`docker start` does not instrument). Verify `docker system info --format '{{.DefaultRuntime}}'` = `dd-shim`. Per service opt-out: `DD_INSTRUMENT_SERVICE_WITH_APM=false`. Remove all: `dd-container-install --uninstall` + restart Docker. Rootless Docker: set socket in `/etc/datadog-agent/inject/docker_config.yaml`.
- Windows: IIS-only `DD_APM_INSTRUMENTATION_ENABLED=iis`, `DD_APM_INSTRUMENTATION_LIBRARIES=dotnet:3` (Agent 7.67.1+, .NET SDK 3.19.0+). Chocolatey can't enable SSI. Restart IIS apps (not whole server). Host-wide (Preview): all Java apps + .NET in IIS; .NET outside IIS needs an allow rule. Remove: `datadog-installer.exe remove datadog-apm-library-dotnet`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/linux/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/docker/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/windows/

### SSI and library injection on Kubernetes
- Requires Kubernetes v1.20+, Datadog Admission Controller, Linux nodes. Enable with Helm `datadog.apm.instrumentation.enabled: true` (`datadog-values.yaml`) or Operator `spec.features.apm.instrumentation.enabled: true` (`datadog-agent.yaml`), then restart apps. **SSI does not instrument the namespace where the Agent runs.** Admission Controller can't modify existing pods.
- Verify: pod `initContainers` include `datadog-init-apm-inject` and `datadog-lib-<language>-init`.
- Injection modes: `auto` (default, Agent 7.76.0+), `init_container`, `csi` (Datadog CSI driver, faster pod startup; `datadog.csi.enabled: true`). Per pod: `admission.datadoghq.com/apm-inject.injection-mode`.
- Targeting (Agent v7.64+): `targets` list with `name`, `namespaceSelector` (`matchNames`/`matchLabels`/`matchExpressions`), `podSelector`, `ddTraceVersions` (e.g. `java: "default"`, `python: "3.1.0"`), `ddTraceConfigs` (env vars like `DD_PROFILING_ENABLED: auto`). **Targets evaluated in order; first match wins.** `disabledNamespaces` always takes precedence; `enabledNamespaces` vs `disabledNamespaces` (legacy: only one). Legacy cluster-level `libVersions`.
- `DatadogInstrumentation` CRD (v7.85+, Operator 1.31+/Helm 3.255.0+): `targetRef` (Deployment, StatefulSet, DaemonSet, Job, CronJob, Argo Rollout), `spec.config.apm` (`enabled`, `ddTraceVersions`, `ddTraceConfigs` names must start `DD_`). Precedence: pod annotations > DDI > Remote Configuration policies > Agent `targets`/`enabledNamespaces` > cluster-wide.
- UST: automatic label extraction via `kubernetesResourcesLabelsAsTags` (not compatible with Remote Configuration -> use `ddTraceConfigs`); or `tags.datadoghq.com/env|service|version` labels.
- Image registry: `DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_CONTAINER_REGISTRY` default `gcr.io/datadoghq` (alternatives `docker.io/datadog`, `public.ecr.aws/datadog`); images `apm-inject`, `dd-lib-<lang>-init`; default version tag `0`. EKS with Calico CNI: Cluster Agent `useHostNetwork: true`. Strict PodSecurity: `DD_ADMISSION_CONTROLLER_AUTO_INSTRUMENTATION_INIT_SECURITY_CONTEXT`.
- Opt out a pod: label `admission.datadoghq.com/enabled: "false"` (also disables other mutating webhooks). Disable cluster-wide: `instrumentation.enabled: false`.
- **Local SDK injection** (pod-level alternative to SSI, Kubernetes v1.14+, Cluster Agent v7.40+ Java/Python/Node.js, v7.44+ .NET/Ruby): Admission Controller only mutates pods labeled `admission.datadoghq.com/enabled: "true"` unless `mutateUnlabelled: true`; annotate `admission.datadoghq.com/<lang>-lib.version: "<tag>"` (annotation table lists `java`, `js`, `python`, `dotnet`, `ruby`; PHP appears only in the list of SDK release repos). Injected version takes precedence over a manually installed tracer. From v7.73.0 no injection into `kube-system` or the Cluster Agent's namespace.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/, https://docs.datadoghq.com/tracing/guide/local_sdk_injection/

### Common pitfalls (quick list)
- Java: `-javaagent` after `-jar`; agent jar on classpath; remote ClassLoader classes.
- Python: forgetting `ddtrace-run` prefix; `ddtrace.auto` not imported first; `--info` ignores in-code config.
- Node: dd-trace not first; framework CLIs (`next start`) -> `NODE_OPTIONS`; ESM needs `--import`/`--loader`; bundlers hide third-party `require()`.
- Go: expecting a runtime agent or SSI; forgetting `orchestrion` in the build.
- Ruby: `datadog/auto_instrument` required before the libraries.
- .NET: two APM vendors (one CLR profiler); global profiler env vars; NuGet bundle for IIS; `iisreset`.
- SSI: `DD_TRACE_ENABLED=false` doesn't stop injection; restart (host) or recreate (Docker) apps; Agent namespace not instrumented in K8s.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting/

## OOTB Tracer vs Community Tracer

### Terminology: tracer = Datadog SDK
- Current docs call the language tracing libraries **Datadog SDKs** (older material: "tracer", "tracing library", "client library"). Same thing: the in-process library that creates spans, propagates context and ships traces to the Agent.
- Instrumentation = adding code to an application to capture and report observability data (traces, metrics, logs). Datadog provides instrumentation libraries for many languages and frameworks.
- Application instrumentation = (1) **SDK setup** (add a Datadog SDK) + (2) **span creation**. Spans are generated automatically as soon as the SDK loads (**auto-instrumentation**); custom spans are optional.
- Ways to get the SDK in: **Single Step Instrumentation (SSI, recommended)** installs/loads SDKs at runtime with one command, no code changes; **manually managed SDKs** = you install/configure the SDK in code or build, full control via env vars and code.
- Custom spans: **Dynamic Instrumentation** (rules in the Datadog UI, applied at runtime, no code change, no redeploy) or **code-based custom instrumentation** (explicit tracing API calls, needs a deploy). These can be combined with either SDK setup method.
- Prefer vendor-neutral? The Application Instrumentation page points to the OpenTelemetry docs.

Sources: https://docs.datadoghq.com/tracing/trace_collection/, https://docs.datadoghq.com/tracing/glossary/

### Official (Datadog-maintained, "OOTB") tracers
- Libraries page, section **APM & Continuous Profiler client libraries** ("Datadog-official and community contributed trace client libraries"); columns: Languages, Libraries, Official, Author, Notes. Official rows show Author = Datadog:
  - C++: `dd-trace-cpp` (C++17, static or shared lib; tested on Linux, Windows, macOS)
  - .NET: `dd-trace-dotnet` (tracing, AAP, CI Visibility, Dynamic Instrumentation, continuous profiler)
  - Rust/C++/C: `ddprof` - command-line **profiler** for compiled languages (CPU + memory allocation); a profiler, not a tracer
  - Go: `dd-trace-go`; Java: `dd-trace-java`; Node.js: `dd-trace-js`; PHP: `dd-trace-php`; Python: `dd-trace-py`; Ruby: `dd-trace-rb`
- "Add the Datadog SDK" page lists the official SDKs: Java, Python, Ruby, Go, Node.js, PHP, C++, **Rust**, .NET Core, .NET Framework, Android, iOS. Compatibility Requirements page lists Java, Python, Ruby, Go, Node.js, PHP, C++, .NET (Core and Framework), Rust.
- **Rust (new since 2025):** official Datadog Rust SDK = `dd-trace-rs` repo / `datadog-opentelemetry` crate, built on the OpenTelemetry API and SDK. **No automatic instrumentation**: you create spans, add attributes/events and propagate context manually with the OpenTelemetry API. MSRV Rust 1.84; OpenTelemetry crate 0.31. Rust does not support Datadog `ManualKeep`/`ManualDrop`; force keep/drop by setting the OTel `sampling.priority` attribute on the root span.
- C++ (`dd-trace-cpp`): needs a C++17 compiler; platforms x86_64/arm64 Linux, x86_64 Windows, arm64 macOS.
- Datadog recommends regularly upgrading to the latest SDK; Support tickets ask for SDK startup logs, debug logs, version info (language, framework, Agent, SDK) checked against Compatibility Requirements.

Sources: https://docs.datadoghq.com/extend/community/libraries/#apm--continuous-profiler-client-libraries, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/rust/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/rust/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/cpp/, https://docs.datadoghq.com/tracing/troubleshooting/

### Community tracers
- Use when the language has **no official Datadog SDK**. Docs: "To instrument an application written in a language that does not have official library support, see the list of community SDKs."
- Community rows on the libraries page (Official column empty, third-party Author):
  - Elixir: `spandex` (Zach Daniel) - macros/functions for spans, async trace propagation, Phoenix via middleware plugs, exports to Datadog
  - Java: `apm-client` (Chas Honton) - servlet, JAX-RS client/server, CDI bean methods; sends spans to a local Datadog APM collector via REST
  - Ruby: `ddtrace-rb-method-wrapper` (Brandfolder) - extension of ddtrace to wrap specific methods into custom spans (`DatadogTraceWrapper`)
  - Rust: `datadog-apm` (Pipefy) - "unofficial" Rust APM library
  - Go row also shows `datadog-go` (Matt Ho), which is actually a DogStatsD client (listing quirk)
- Support implications: community libraries are authored and maintained by third parties (Author column), not Datadog. The libraries page itself has no explicit support statement; by analogy with the OTel "Custom Components" support level, expect to take library issues to the maintainer, not Datadog.
- Many community libraries are extensions of official SDKs (e.g. Ruby method wrapper), not replacements.
- The page moved: `/developers/community/libraries/` now 301-redirects to `/extend/community/libraries/` (breadcrumb "Extend Datadog > Community > Libraries").

Sources: https://docs.datadoghq.com/extend/community/libraries/#apm--continuous-profiler-client-libraries, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/

### Agent tracing API (how community/custom tracers ship spans)
- Traces go from instrumented code to the Agent over an HTTP API. SDKs simplify this; use the API directly for apps that cannot use the libraries or languages without an official SDK.
- It is an **Agent API, not a server-side API**: `PUT http://localhost:8126/v0.3/traces`; the Agent forwards to Datadog.
- Body: array of traces; each trace = array of spans; spans in a trace share `trace_id`; `trace_id` and `span_id` must differ.
- Span fields: `duration` (int64, **nanoseconds**), `error` (int32, 1 = error; put message/type/stack in `meta`), `meta` (string->string), `metrics` (string->float64), `name` (<=100 chars), `parent_id`, `resource` (<=5000 chars), `service` (<=100 chars), `span_id` (64-bit unsigned), `start` (ns since UNIX epoch), `trace_id` (lower 64 bits; upper 64 bits of a 128-bit ID go in `meta` tag `_dd.p.tid`, lowercase hex), `type` enum `web`, `db`, `cache`, `custom`.
- SDKs support 64-bit and 128-bit trace IDs.

Sources: https://docs.datadoghq.com/tracing/guide/send_traces_to_agent_by_api/

### What the tracer (SDK) does vs what the Agent does
- **SDK/tracer** (in-process): auto-instruments supported frameworks, creates spans, propagates trace context, applies head-based sampling decisions at the trace root, collects tags/data (DB statements, URI params, client IP, etc. per language settings), sends traces to the Agent; runtime metrics via DogStatsD (UDP 8125).
- SDK default destination: Unix domain socket `/var/run/datadog/apm.socket` first; if absent, `http://localhost:8126`. Override with `DD_TRACE_AGENT_URL` (e.g. `http://custom-hostname:1234` or `unix:///var/run/datadog/apm.socket`); `DD_AGENT_HOST` / `DD_TRACE_AGENT_PORT` (default 8126) in many SDKs. Stats: `/var/run/datadog/dsd.socket`, else `localhost:8125`.
- **Agent** (trace agent): receives traces (`apm_config: enabled: true` by default in `datadog.yaml`, listens on `localhost:8126`); in containers set `apm_non_local_traffic: true` (`DD_APM_NON_LOCAL_TRAFFIC=true`) to accept traffic from other containers/hosts; custom receiver port `receiver_port` / `DD_APM_RECEIVER_PORT`.
- Agent sampling: by default (Agent-level mechanism) the Agent continuously sends sampling rates to SDKs to apply at the root of traces, targeting **10 traces per second** overall, split across services by traffic; ingestion reason `auto`, labeled `Automatic` in Ingestion Control. `target_traces_per_second` / `DD_APM_TARGET_TPS` (default 10). **Only applies to Datadog SDKs, no effect on OpenTelemetry SDKs.** Any SDK-level setting overrides the Agent mechanism. Remote config from Agent 7.42.0.
- SDK-level: sampling rules by service/resource, rate limit default 100 traces/s per service instance (ignored with the Agent default mechanism).
- Agent-side extra samplers: error sampler (up to 10 traces/s per Agent), rare sampler (up to 5 traces/s per Agent); capture local traces only.
- Agent obfuscation: credit card numbers obfuscated by the Agent by default; Agent obfuscates resource names and DB statements; configured in `datadog.yaml` or env vars.
- Trace metrics (hits, errors, latency) are calculated from 100% of traffic regardless of ingestion sampling (Datadog SDK setups). With OTel SDKs sampling at the SDK, APM metrics are calculated from sampled data.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://docs.datadoghq.com/tracing/configure_data_security/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/

### OpenTelemetry as the standard alternative
- OTel = standardized protocols for collecting and routing telemetry. Two key decisions: **how to instrument** and **how to send data**. Feature availability depends on both.
- Instrumentation options: **Full OpenTelemetry** (OTel SDK + API, vendor-neutral; some Datadog features unsupported); **OTel API + Datadog SDK** (vendor-neutral code, full Datadog feature set); **OTel instrumentation libraries** with the Datadog SDK (cover frameworks Datadog SDKs do not).
- OTel API with Datadog SDK: set `DD_TRACE_OTEL_ENABLED=true` (Java also `dd.trace.otel.enabled`); not required for Go and Ruby SDKs (instrumentation libraries page). Depend only on the OTel API, not the OTel SDK. SDK-specific operations (SpanProcessors, OTLP trace exporters) not supported. Disable the duplicate Datadog instrumentation when replacing it with an OTel one.
- Datadog SDK OTel API support (Traces/Metrics/Logs): .NET, Python, Node.js, Java, Go, PHP all yes; Ruby Metrics = Alpha.
- Sending options: **Datadog Agent with DDOT Collector (recommended)** - DDOT = Datadog Distribution of OpenTelemetry Collector embedded in the Agent (Fleet Automation, Live Containers, Kubernetes Explorer, Live Processes, CNM, USM, 1,000+ integrations); **OpenTelemetry Collector** (upstream, Datadog Exporter, tail-based sampling); **direct OTLP ingest** (agentless: serverless, managed platforms); **OTLP ingest in the Agent**.
- Feature compatibility: only **Datadog SDK + DDOT** gets App and API Protection, Continuous Profiler, Data Jobs Monitoring, Data Streams Monitoring, RUM. DBM, CNM, Live Containers, Live Processes, USM need DDOT (not upstream Collector/direct). Distributed tracing, trace metrics, runtime metrics, span links, correlation, Cloud SIEM work in all setups (direct OTLP: trace metrics from sampled spans).
- OTLP ingest in the Agent: since 6.32.0/7.32.0 (traces, metrics), logs since 6.48.0/7.48.0. **Off by default**. `otlp_config.receiver.protocols.grpc.endpoint` (default port **4317**) / `...http.endpoint` (**4318**); env vars `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_GRPC_ENDPOINT`, `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_HTTP_ENDPOINT` (set on core and trace Agent). Logs ingestion disabled by default. Supported setup = an ingesting Agent on every OTel-data-generating host; you cannot send OTel data from one host to an Agent on another host. OTel SDK data cannot use AAP, Continuous Profiler, Ingestion Rules.
- Unsupported runtime (example **Bun**): use the OpenTelemetry SDK (OTel Node.js SDK) and export OTLP (`OTEL_EXPORTER_OTLP_ENDPOINT`, e.g. `http://localhost:4318` HTTP or 4317 gRPC; `OTEL_SERVICE_NAME`) to DDOT, an OTel Collector, or direct OTLP ingest. Bun-native APIs (`Bun.serve()`, `bun:sqlite`) need manual spans.
- Support levels: **Datadog Supported Components** (Datadog Exporter, Datadog Connector, Infra Attribute Processor); **Community Supported Components** (OTel components included with DDOT by default); **Custom Components** (custom Collector components, instrumentation of unsupported runtimes): Datadog gives guidance only, does not directly support - go to the OTel community or maintainers.
- Best practices: avoid mixed instrumentation (Datadog SDK + OTel SDK in the same app = undefined behavior; exception: some languages such as Python need both installed). Do not run the Datadog Agent and a separate OTel Collector on the same host. AWS EKS Fargate not supported for the OTel Collector.
- Runtime metrics: Datadog SDKs via DogStatsD (UDP 8125); OTel SDKs via OTLP (4317/4318).

Sources: https://docs.datadoghq.com/opentelemetry/, https://docs.datadoghq.com/opentelemetry/instrument/, https://docs.datadoghq.com/opentelemetry/compatibility/, https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent/, https://docs.datadoghq.com/opentelemetry/guide/instrument_unsupported_runtimes/, https://docs.datadoghq.com/opentelemetry/instrument/dd_sdks/instrumentation_libraries/, https://docs.datadoghq.com/opentelemetry/instrument/api_support/

### Common pitfalls
- Assuming Rust has only a community tracer: current docs list an official Rust SDK (manual-only, OTel API). The libraries table still shows only the Pipefy community crate.
- `ddprof` is an official profiler, not a tracer.
- The tracing API is local (`localhost:8126`), not a Datadog intake URL; times are nanoseconds.
- `DD_APM_TARGET_TPS` does nothing for OTel SDK apps.
- Full OTel SDK loses Continuous Profiler, AAP, DSM, RUM correlation features available with the Datadog SDK.
- Datadog does not directly support community libraries or OTel instrumentation of unsupported runtimes.

Sources: https://docs.datadoghq.com/tracing/trace_collection/compatibility/rust/, https://docs.datadoghq.com/extend/community/libraries/#apm--continuous-profiler-client-libraries, https://docs.datadoghq.com/opentelemetry/compatibility/

## Tagging

### Tag fundamentals (Getting Started with Tags)
- Tags add dimensions to telemetry so it can be filtered, aggregated and compared. Format `<key>:<value>` (recommended; allows grouping by key) or bare `<value>`.
- Reserved tag keys: `host` (correlate metrics, traces, processes, logs), `device`, `source` (span filtering + automatic log pipelines), `service`, `env`, `version` (scope application data across metrics, traces, logs), `team` (ownership).
- Tag string rules:
  - Must start with a letter; may then contain Unicode letters, numbers, underscores, minuses, colons, periods, forward slashes (`@` only for logs sent over HTTP). Other characters (commas, spaces, emoji, backslashes) become underscores. Leading/trailing underscores removed; repeated underscores collapsed.
  - Max 200 characters for the whole tag (key + `:` + value).
  - Span tags and metric tags are normalized to lowercase (avoid camelCase). Span attributes and log attributes are case-sensitive and not normalized.
  - The key is everything before the FIRST colon: `env:staging:east` -> key `env`, value `staging:east`.
  - Never tag with unbounded values (epoch timestamps, user IDs, request IDs) -> cardinality explosion.
- `DD_TAGS` (Agent env var) is whitespace-separated: `DD_TAGS="key1:val1 key2:val2"` = 2 tags. `DD_TAGS="test:this is a test"` = 4 tags (`test:this`, `is`, `a`, `test`). Use YAML or integration annotations for values with spaces (they become underscores: `test:this_is_a_test`).
- Assigning tags: config files (`datadog.yaml` `tags:` list, integration `conf.d` YAML), UI, API, DogStatsD. In containers use Autodiscovery + unified service tagging.
- Host tag inheritance: all metrics, logs, traces inherit host-level tags. Use distinct key names (e.g. `infra_service` instead of a host-level `service`) to avoid duplicate keys.
- Tag precedence: the Agent does NOT enforce precedence. It collects every source and emits every unique value, so one key can have several values (`service:payments`, `service:checkout`, ...). Filter explicitly downstream.
- Container tag extraction env vars: `DD_CONTAINER_LABELS_AS_TAGS`, `DD_CONTAINER_ENV_AS_TAGS`, `DD_KUBERNETES_POD_LABELS_AS_TAGS` (JSON maps label->tag; wildcards like `{"*":"kube_%%label%%"}`), `DD_CHECKS_TAG_CARDINALITY` / `DD_DOGSTATSD_TAG_CARDINALITY` = `low` (default; cluster-level like `kube_namespace`) | `orchestrator` (pod-level, `pod_name`; `task_arn` on ECS) | `high` (container-level, `container_id`).
- UI host tags (Host Map / Infrastructure List > Add Tags) take up to 5 minutes to apply. Changing hostname: old name stays in UI 2 hours.
- Span metadata must be a typed tree: `key` cannot be both a string and have `key.subkey`.
- Usage in APM: Trace Explorer search bar `<KEY>:<VALUE>` (e.g. `service:coffee-house`), Service Map navigation filtered by `service:`.

Sources: https://docs.datadoghq.com/getting_started/tagging/, https://docs.datadoghq.com/getting_started/tagging/assigning_tags/, https://docs.datadoghq.com/getting_started/tagging/using_tags/

### Unified service tagging (UST): concepts and requirements
- Ties telemetry together with three reserved tags: `env`, `service`, `version`. Benefits: deployment impact via trace and container metrics filtered by version; seamless pivot between traces, metrics, logs; view data by env or version.
- `version` should change with every deployment; two different code versions need distinct values.
- Log `service` defaults to the container short-image if no Autodiscovery log config exists.
- Host information is excluded for database and cache spans (the span's host is not the DB/cache host).
- Requirements: Agent 6.19.x / 7.19.x or higher. Min SDKs: .NET 1.17.0, C++ 0.1.0, Go 1.24.0, Java 0.50.0, Node 0.20.3, PHP 0.47.0, Python 0.38.0, Ruby 0.34.0.

Sources: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/

### UST in containers (Kubernetes, Docker, ECS)
- Enable Autodiscovery; for Docker the Agent needs access to the Docker socket.
- Kubernetes full configuration: labels on BOTH the parent workload (Deployment etc.) and pod template:
  ```yaml
  tags.datadoghq.com/env: "<ENV>"
  tags.datadoghq.com/service: "<SERVICE>"
  tags.datadoghq.com/version: "<VERSION>"
  ```
  plus, for APM apps, env vars `DD_ENV`, `DD_SERVICE`, `DD_VERSION` for the tracer (manually or via the downward API, `valueFrom.fieldRef.fieldPath: metadata.labels['tags.datadoghq.com/env']`). The Cluster Agent Admission Controller automatically injects the three env vars to match the labels.
- Per-container labels in multi-container pods: `tags.datadoghq.com/<CONTAINER_NAME>.env|service|version`.
- DD_* env vars only needed if the app uses APM; labels alone cover Kubernetes CPU/memory/network/disk metrics, container tagging, log collection, KSM.
- OTel alternative in pod: `OTEL_RESOURCE_ATTRIBUTES="service.name=...,service.version=...,deployment.environment.name=..."` and `OTEL_SERVICE_NAME` (OTEL_SERVICE_NAME wins over `service.name`).
- Global env for a single-env cluster: Operator `spec.global.tags: ["env:<ENV>"]`, Helm `datadog.tags: ["env:<ENV>"]`. Becomes a host-level tag, applied to KSM, and is the default `env` on APM spans. Pitfall: a pod with a different `env` gets BOTH env tags.
- Docker full config: env vars + labels `com.datadoghq.tags.env|service|version` (service/version can be in the Dockerfile `ENV`/`LABEL`; env often at `docker run -e DD_ENV=... -l com.datadoghq.tags.env=...`). Partial config (untraced software like Redis, PostgreSQL, NGINX): labels only.
- ECS: env vars + `dockerLabels` in the task definition; `DD_VERSION` optional with automatic version tagging. On Fargate, put them on the APPLICATION container, not the Agent container. On Fargate with Fluent Bit/FireLens, UST works for metrics and traces only, not log collection.
- Automatic version tagging (APM data only, Agent 7.52.0+): if you set version it is never overridden; otherwise priority 1 your value, 2 `{image_tag}_{first 7 of git sha}`, 3 `{image_tag}` or the 7-char sha if only one exists. Non-containerized or to include Git SHA: embed Git info in build artifacts (Source Code Integration).

Sources: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/

### UST in non-containerized, serverless and OpenTelemetry setups
- Scope env vars to a single process: `DD_ENV=<env> DD_SERVICE=<service> DD_VERSION=<version> /bin/my-service`, or have Chef/Ansible write them to systemd/initd.
- Traces: `DD_ENV` on the SDK keeps env close to the app. `DD_VERSION` is added to spans of the SDK's own service (generally `DD_SERVICE`); spans created with an external service's name do not get `version`. If version is on spans it is added to the trace metrics. One service per span. A different `service` host tag shows up on all trace metrics from that host.
- Logs: enable automatic log injection; SDK injects env/service/version.
- Custom StatsD metrics: tags are append-only (two env values -> both). DogStatsD clients auto-add env/service/version from DD_* vars, except the .NET and PHP clients.
- System metrics: set `env:` (and `tags: - service:<SERVICE>` for one service per host) in `datadog.yaml`; version not recommended. Multiple services per host: set only `env`, use the process check (`process.d/conf.yaml`) with `service:` per instance; a global service tag would give process metrics two services.
- RUM: set `service`, `env`, `version` in the init. Synthetics: Integration Settings > APM Integration for Browser Tests URLs (wildcards `*`).
- Serverless: see Lambda "connect telemetry using tags".
- OpenTelemetry mapping: `deployment.environment.name` (Agent 7.58.0+, Exporter v0.110.0+) or deprecated `deployment.environment` -> `env`; `service.name` -> `service`; `service.version` -> `version`. `DD_SERVICE`/`DD_ENV`/`DD_VERSION` are NOT supported out of the box in OTel config. Set via `OTEL_RESOURCE_ATTRIBUTES`, SDK `Resource`, or Collector `transform` processor.

Sources: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/

### Configuring tags in the Datadog SDK
- `DD_ENV`: global `env` on all tracer telemetry. `DD_SERVICE` (aliases `DD_SERVICE_NAME`, `OTEL_SERVICE_NAME`): `service` on every span; if unset the SDK guesses (Node: `package.json` name; .NET: IIS app/entry assembly/process; Java: auto-detected from application class). `DD_VERSION`: version tag on traces and logs (e.g. `1.2.3`, `6c44da20`).
- `DD_TAGS` (tracer): custom tags on all spans, comma-separated `key:value` in the Python SDK (`layer:api,team:intake`); Java `-Ddd.tags=datacenter:njc,key:val`. Note: the Agent's `DD_TAGS` is whitespace-separated.
- Python in code: `span.set_tag("num_ingredients", 3)` (local), `tracer.set_tags({...})` (global, every span). Go: `WithGlobalTag`.
- `DD_TRACE_HEADER_TAGS`: HTTP headers as span tags (default key `http.request.headers.<h>`). `DD_SERVICE_MAPPING`: rename integration services. `DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED` (default false): integrations stop setting their own service names (use with inferred services).
- Verify runtime config: Service page > Service Config > SDK Configuration tab.
- Base service = default `DD_SERVICE`; integration override = service name set automatically by an integration; custom override = set manually.

Sources: https://docs.datadoghq.com/tracing/trace_collection/library_config/, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/dd-api/, https://docs.datadoghq.com/tracing/guide/service_overrides/

### Deployment tracking with `version`
- `version` applies to infrastructure metrics (host, container, process, NPM), trace metrics, traces, profiles, logs.
- Service page: Requests/Errors widgets can be scoped by version (Total Requests by Version, Requests Per Second by Version, Total Errors / Errors per second / % Error Rate by Version); exportable to dashboards and monitors.
- Version section (Deployments tab): versions active in the time range, first/last seen, Error Types indicator (error types not seen in the previous version), requests/s, error rate; optional columns: new endpoints, time active, total requests/errors, latency p50/p75/p90/p95/p99/max. Appears only if MORE THAN ONE version reported in the selected interval.
- Deployment comparison: click a version row; compares to the immediately previous version by default, or any two versions within the past 30 days. Sections: comparison graphs, error comparison, endpoint comparison (+ profiler comparison if enabled; View Profiles button).
- Automatic Faulty Deployment Detection needs `version`; monitor via New Monitor > Events with `tags:deployment_analysis`.
- Strategies: rolling, blue/green, canary, shadow.
- Data volume: max 30 unique versions per env+service per 40-minute interval.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/tracing/services/service_page/

### Linking monitors to services
- A monitor is attached to an APM service if `service:<SERVICE_NAME>` is in the monitor's tags (metadata), in the monitor query, or the query is grouped by service. Synthetic tests tagged `service:<SERVICE_NAME>` also attach.

Sources: https://docs.datadoghq.com/tracing/services/service_page/#service-monitor

### Primary tags (env and the second primary tag)
- Primary tags scope an entire APM app (requests/s, latency, error rate, Apdex, traces). Different rules from normal tags.
- `env` is the default, mandatory primary tag; untagged data gets `env:none`.
- Recommended: set env in the SDK (`DD_ENV` picked up automatically, or global tag in code). Agent alternatives: top-level `env: <ENV>` in `datadog.yaml` (or `DD_ENV` in containers) or a host tag `tags: env:<ENV>` (or `DD_TAGS`). Do NOT set different env on tracer and Agent: duplicate tagging on trace metrics.
- APM pages show an `env` dropdown; `<TAG_NAME>:*` shows all values.
- Additional (second) primary tag: e.g. datacenter, availability zone, cluster, region. Defined in APM Settings (`/apm/settings/default-settings`). Only org administrators. Changes take up to 2 hours. Up to 100 unique values per tag. Must be a host or container tag; span-level tags added by the SDK cannot be primary tags. Tag enrichment tags cannot be primary tags either (enrichment runs after primary tag resolution). Never add `resource`, `name`, `service` as host tags (SDK always sets them). A second dropdown appears in the Catalog Performance tab.
- Changing a previously set primary tag: historical APM data aggregated by the old tag becomes inaccessible; APM monitors scoped to the old tag show No Data.
- Container-based primary tags (Docker/Kubernetes pod metadata, Linux): on by default in Agent 7.65.0+; select in APM Settings; up to 2 hours. Disable with `DD_APM_FEATURES=disable_cid_stats` (append to existing comma list) and restart the Agent. Primary tag values should avoid capitals and special characters.
- Pitfall: putting partitions in service names (`web-store-us-1`, `web-store-eu-1`) or env in service names (`prod-web-store`) inflates service count; use a primary tag (region) / env instead.
- Data volume guidelines per 40-minute interval: 5000 env+service combos; 100 primary tag values per additional primary tag; 100 operation names per env+service; 1000 resources per env+service+operation; 30 versions per env+service. Truncation: service/operation/type 100 chars, resource 5000, tag key 200, tag value 25000; max 1024 span tags per span. Spans accepted 18h in the past to 2h in the future.

Sources: https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/, https://docs.datadoghq.com/tracing/troubleshooting/#data-volume-guidelines

### Tags available on trace metrics
- Namespace `trace.<SPAN_NAME>.<SUFFIX>`; computed on 100% of traffic regardless of ingestion sampling (except SDK-side OTel sampling, app-side sampling, X-Ray).
- Tags: `env`, `service`, `version`, `resource` (`resource_name`), `http.status_code`, `http.status_class`, `rpc.grpc.status_code` (Agent 7.65.0+), Datadog Agent host tags, additional primary tags (`synthetics` on latency distribution and apdex). Other (custom) span tags are NOT available on trace metrics.
- Legacy `.duration` / `.duration.by_http_status` metrics list no `version` tag.
- To get metrics by a custom span tag/attribute: APM > Generate Metrics (span-based custom metrics; any span tag or attribute as a group-by; 15-month retention; names cannot start with `trace.`).
- Peer tags: with `apm_config.compute_stats_by_span_kind` and `apm_config.peer_tags_aggregation` (default on in Agent 7.60.0+; must be enabled manually on 7.50.3-7.59.1 with `DD_APM_COMPUTE_STATS_BY_SPAN_KIND` and `DD_APM_PEER_TAGS_AGGREGATION`, plus an explicit `DD_APM_PEER_TAGS` list on 7.50.3-7.54.1) the Agent computes stats for client/producer spans aggregated by peer tags (powers inferred services).

Sources: https://docs.datadoghq.com/tracing/metrics/metrics_namespace/, https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/, https://docs.datadoghq.com/tracing/services/inferred_services/

### Span tags vs span attributes and search syntax
- Span attributes = content of the span from auto/manual instrumentation (`http.url`, `http.status_code`, `error.message`); shown on the Info/Overview tab of the trace side panel; query with `@` (`@http.url`, `@peer.db.name:users`).
- Span tags = context enriched from host, container, Catalog (`hostname`, `availability-zone`, `cluster-name`, `container_name`, `kube_deployment`, `pod_name`); shown on the Infrastructure tab; query without `@`.
- Reserved attributes queryable without `@`: `env`, `service`, `operation_name`, `resource_name`, `status`, `ingestion_reason`, `trace_id` (query syntax page also lists `span_id`, `timestamp`, `type`).
- Non-standard tag format: `tags:"auto-discovery.cluster-autoscaler.k8s.io/daffy"`.
- Facets not required for search, span metrics, or retention filters.
- Span tag naming domains (Default Standard Attributes): reserved, core, network, HTTP, database, message queue, RPC, errors.

Sources: https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention/, https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/

### Peer tags (inferred services)
- Datadog maps standard span attributes to `peer.*` tags to name inferred databases, queues, third-party APIs.
- Examples: `peer.db.name` <- `db.name`, `mongodb.db`, `db.instance`, `cassandra.keyspace`, `db.namespace`; `peer.db.system` <- `db.system`, `db.type`...; `peer.hostname` <- `net.peer.name`, `out.host`, `db.hostname`, `http.host`, `server.address`...; `peer.messaging.destination` <- `topicname`, `messaging.destination(.name)`...; `peer.aws.s3.bucket` <- `bucketname`, `aws.s3.bucket`; `peer.aws.sqs.queue` <- `queuename`; `peer.aws.dynamodb.table` <- `tablename`; `peer.aws.kinesis.stream` <- `streamname`; `peer.rpc.service`, `peer.service`.
- Precedence: Database `peer.db.name` > S3 bucket/DynamoDB table/Cassandra contact points/Couchbase seed nodes > `peer.hostname` > `peer.db.system`. Queue `peer.messaging.destination` > Kafka bootstrap servers/SQS queue/Kinesis stream > `peer.messaging.system`. Inferred service `peer.service` > `peer.rpc.service` > `peer.hostname`. `peer.service` always wins if set; Datadog never sets it for inferred DBs/queues.
- IP-like peer values are redacted to `blocked-ip-address`.
- Default names: external APIs by `net.peer.name` (e.g. `api.stripe.com`), databases by `db.instance`. Rename with renaming rules.

Sources: https://docs.datadoghq.com/tracing/services/inferred_services/#peer-tags

### Tag enrichment (Preview)
- Adds tags without code changes/redeploys, from Catalog (IDP) Entity Metadata, another tag's value, or a fixed value. Preview (request access); not supported on the ddog-gov sites (app.ddog-gov.com, us2.ddog-gov.com).
- Requires the Datadog Admin Role. UI: IDP > Manage > Tag Enrichment (+ Add Rule), or Service page > Service Config > banner > Add Tags.
- Default rules: toggle `team` or `system`; only services with Entity Metadata are enriched; tag only added when telemetry has no value for it.
- Custom rules: select entities (Build Advanced Query: Add Condition = AND, multiple values = OR); tags `team`, `system`, custom; source per tag; apply only-if-missing or append; choose telemetry types. Up to an hour to fully apply.
- Behavior: all telemetry except DSM, Events, Orchestration; not retroactive; metadata updates propagate; rules applied in creation order (top wins); applied after service remapping rules; applied after primary tag resolution, so enriched tags cannot be primary tags.

Sources: https://docs.datadoghq.com/tracing/services/tag_enrichment/

## Retention Periods for APM Data

### Cheat sheet: how long each kind of APM data lives

| Data | Default retention | Where it is used |
| --- | --- | --- |
| Ingested spans/traces (all spans the Agent sends, after ingestion sampling) | **15 minutes**, rolling window | Trace Explorer **Live Search** |
| Spans indexed by **custom** retention filters (incl. default filters such as `Error Default`) | **15 days** | Trace Explorer indexed search, dashboards, notebooks, trace analytics monitors |
| Spans indexed by the **Intelligent retention filter** (diversity sampling + 1% flat sampling) | **30 days** | Trace Explorer, dashboards, notebooks, Trace Queries (NOT trace analytics monitors) |
| Indexed spans per the Data Retention Periods table | "15 or 30 days, determined by customer plan" (so 15 days is the default, not a hard limit) | — |
| Trace metrics (`trace.<SPAN_NAME>.*`) and custom span-based metrics | **15 months** (all Datadog metrics: tags and values 15 months) | Dashboards, monitors, Metric Explorer, notebooks |
| Span summaries, service and resource statistics (Catalog / service + resource pages) | **up to 30 days** ("Services/resources statistics: 30 days") | For older data use trace metrics in Metric Explorer |
| APM "Errors" (Data Retention Periods table) | 15 days | — |
| APM "Viewed traces" | Retained for the duration of the account | — |
| Service metadata (Service Catalog / Software Catalog) | Retained for the duration of the account | — |
| Continuous Profiler: flame graphs, call graphs, thread timelines | **8 days** | Profiles |
| Profiler: flame graph exported to a notebook | **1 year** | Notebooks |
| Profiler: individual profiles opened in the UI at least once | **1 year** | Profiles |
| Profiler: profile metrics | **30 days** ("one month") | Dashboards |
| Error Tracking: error samples | **30 days** | Error Tracking issue panel |
| Error Tracking: issues | **1 year after last activity** | Error Tracking Explorer |
| Dashboards, notebooks, monitors | Duration of the account | — |

- Live Search = everything ingested, last 15 min, no sampling. Past 15 min = only indexed spans (15 days custom, 30 days intelligent).
- Anything that must live longer than 15/30 days must be a metric (trace metric or span-based custom metric, 15 months) or exported (flame graph to notebook, 1 year).
- `tracing/metrics` page wording: "Ingested span and traces are kept for 15 minutes. Indexed spans and traces that retention filters keep are stored in Datadog for 15 days. But if you generate custom metrics from ingested data, the metrics are retained for 15 months."
- Exam guide/official sample: "default APM plan includes 1 million indexed spans per month, retained for 15 days". A post-mortem notebook after an incident uses **trace metrics** (they outlive spans).

Sources: https://docs.datadoghq.com/data_security/data_retention_periods/, https://docs.datadoghq.com/tracing/metrics/, https://docs.datadoghq.com/tracing/trace_explorer/

### Ingestion vs indexing (the trace pipeline)

- Two independent stages: **ingestion** (what the SDK/Agent sends to Datadog, controlled by ingestion controls/sampling) and **retention/indexing** (what Datadog keeps past 15 minutes, controlled by retention filters in the UI).
- Retention filters do **not** affect what the Agent collects/sends ("ingested"). To reduce ingested volume use ingestion controls (`DD_TRACE_SAMPLING_RULES`, `DD_TRACE_SAMPLE_RATE`, `DD_APM_TARGET_TPS`, adaptive sampling, resource-based sampling at APM > Ingestion Control).
- Glossary: Retention filters = "tag-based controls set within the Datadog UI that determine what spans to index in Datadog for 15 days". Ingestion controls = "send up to 100% of traces to Datadog for live search and analytics for 15 minutes".
- Both ingested (GB) and indexed (count) spans may impact the bill.
- Trace metrics are calculated on **100% of traffic** regardless of ingestion sampling (computed in the Agent by default); APM metrics are not impacted by ingestion controls.
- What happens to a span that is ingested but not indexed: searchable in Live Search for 15 min, then gone from search. It still contributed to trace metrics (100% of traffic) and can feed custom span-based metrics (generated from ingested spans regardless of indexing). Spans dropped by sampling (never ingested) cannot generate span-based metrics.
- Data volume guideline: spans may have timestamps up to **18 hours in the past** and **2 hours in the future**. Limits per 40-minute interval: 5000 unique env+service combos, 100 primary tag values per additional primary tag, 100 operation names per env+service, 1000 resources per env+service+operation, 30 versions per env+service. Truncation: service/operation/type 100 chars, resource 5000, tag key 200, tag value 25000; max 1024 span tags per span.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/, https://docs.datadoghq.com/tracing/troubleshooting/#data-volume-guidelines

### Trace Explorer: Live Search (15 minutes) vs indexed search (15 days)

- Trace Explorer (APM > Traces, `app.datadoghq.com/apm/traces`) searches ingested or indexed spans with any tag on any span.
- **Live Search** is the **default** view. Shows all spans ingested in the **last 15 minutes (rolling)**, displayed **without any sampling**, as soon as the Agent sends them and before retention filters run. Indicator: "Live Search - All ingested data".
- Live Search query is matched against all ingested traces across any span and any tag (not just indexed ones). You can filter on attributes that are not facets (e.g. type `cart.value` in the query bar, or click it in the trace side panel).
- Live Search list view: spans/second shown at top; high-throughput streams show some spans for visual clarity; Pause/Play button top right; selecting a span pauses the stream. Option box above the table: service entry spans, root spans, or all spans.
- Live Search timeseries/top list: "Exporting to dashboards and monitors is only possible using retained spans."
- **Switch to indexed search**: change the **time selector** (top right) to any period **greater than 15 minutes**. Indicator: "Search - Only Indexed Data".
- Indexed search: all spans indexed by custom retention filters **and** the intelligent retention filter are searchable. If you filter on a tag that appears only on spans not indexed by any retention filter, the search returns **no results** (unlike Live Search).
- Clicking any indexed span always shows its **complete trace context** (all parent/child spans) in the flame graph/waterfall, even spans that were not indexed. But only the indexed spans are **searchable**.
- From the indexed timeseries view: export the query to a dashboard, monitor, or notebook.
- Span links only display when the corresponding spans are ingested and indexed.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/trace_explorer/search/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/

### Retention filters (custom, default, order, permissions)

- UI: **APM > Retention Filters** (`app.datadoghq.com/apm/traces/retention-filters`). Columns: Filter Name, Filter Query, Retention Rate (0-100%, uniformly chosen among matching spans), Spans Indexed, Last Updated, Enabled toggle.
- Permission required to create, delete, modify, enable or disable: **`apm_retention_filter_write`**.
- Create: Add Retention Filter -> Retention Query -> **Span rate** -> optional **Trace rate** -> name -> Add Filter. Datadog shows an estimate of the % change in global indexing volume.
- Custom filters keep matching spans for **15 days**. Query examples: `@transaction_amount:>100`; `resource_name:"GET /checkout" @duration:>2s env:prod`; `service:delivery-api @version:v2.0`.
- **Order matters**: filters are evaluated serially; if a span matches a filter earlier in the list it is kept or dropped there, and a lower matching filter does not catch it. Spans retained by an upstream filter do not show up in a downstream filter's Edit window.
- Two types: **span-level** (span query + span rate; indexes only matching spans; queryable in Span Explorer) and **trace-level** (adds a trace rate; indexes all spans of traces containing matching spans; queryable in Span Explorer **and Trace Queries**). Span rate is evaluated first; trace rate applies only to traces selected by the span rate. A trace rate can significantly increase indexed span usage.
- Indirectly indexed spans (kept only because of a trace rate) are not evaluated by trace analytics monitors.
- **Default retention filters**: `Error Default` (indexes `status:error`; query and rate configurable, e.g. `status:error, env:production`; can be disabled), `App and API Protection Default`, `Synthetics Default`, `Dynamic Instrumentation Default` (each enabled only if that product is used).
- Legacy: as of **October 20, 2020**, App Analytics filters were automatically transitioned to Retention Filters (marked with an *i* for Legacy App Analytics Filters). "Analyzed Spans" = legacy name for indexed spans.
- Usage: `Spans Indexed` column is powered by `datadog.estimated_usage.apm.indexed_spans` (billed dimension, tagged `env`, `service`). Ingested: `datadog.estimated_usage.apm.ingested_bytes` (billed), `..._ingested_spans`, `..._ingested_traces`. Dashboards: APM Traces Estimated Usage, APM Ingestion Reasons.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/tracing/trace_pipeline/metrics/, https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/

### Intelligent retention filter (diversity sampling + 1% flat sampling)

- Always active; cannot be replaced by custom filters; keeps a representative selection of traces. Spans it indexes are retained for **30 days** and are **not counted toward indexed span usage** (do not impact the bill).
- **Diversity sampling** scans **service entry spans** and keeps (30 days):
  - at least one span (and its trace) per combination of **environment, service, operation, resource** every **15 minutes at most** (so service and resource pages always have example traces, even for low-traffic endpoints);
  - high-latency spans for **`p75`, `p90`, `p95`** per combination;
  - a representative selection of errors (e.g. status codes 400s, 500s).
  - Not uniformly sampled: biased toward errors and high latency.
- **One percent flat sampling** (30 days): all traces correlated with **1% of ingested RUM sessions** that had traces (decision on `session_id`), plus a **uniform 1%** of ingested spans (decision on `trace_id`, so all spans of a trace share it). Proportionally representative; low-traffic services may be missing on short time frames.
- Both capture **complete traces**, so Trace Queries work on them.
- `retained_by` attribute on every retained span: `retention_filter` (custom/default filter, no trace rate; NOT in Trace Queries), `trace_retention_filter` (filter with trace rate), `diversity_sampling`, `flat_sampled` (refine with `@retention_reason:rum` or `@retention_reason:trace`).
- For uniformly representative analytics, exclude diversity spans: `-retained_by:diversity_sampling`. Include them when counting unique values (e.g. unique merchants).
- Spans indexed by the intelligent retention filter are **included** in Trace Explorer aggregated views, dashboards and notebooks, but **excluded** from APM **trace analytics monitor** evaluation.
- Troubleshooting: "more spans in the Trace Explorer than on the Monitors page" with no custom filters is expected: Monitors use spans from custom retention filters only; dashboards/notebooks use custom + intelligent.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#datadog-intelligent-retention-filter, https://docs.datadoghq.com/tracing/guide/leveraging_diversity_sampling/, https://docs.datadoghq.com/tracing/troubleshooting/#trace-retention

### Trace Queries data window

- Trace Queries combine 2+ span queries (`a`, `b`, ...) with operators `&&`, `||`, `->` (indirect upstream), `=>` (direct parent), `NOT`; trace-level filters `span_count(a)`, `total_span_count`, `trace_duration`. Trace list shows up to 50 sample traces. Flow Map is powered by a sample of ingested traffic.
- Trace Queries run on traces indexed by the **intelligent retention filter** and **trace-level retention filters** (filters with a trace rate). Spans kept by a span-level custom filter without a trace rate (`retained_by:retention_filter`) are not in Trace Queries, because trace queries need all spans of a trace indexed.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_queries/#how-trace-queries-source-data, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#trace-search-and-analytics-on-indexed-spans

### Long-term data: trace metrics and custom span-based metrics (15 months)

- Trace metrics (`trace.<SPAN_NAME>.<METRIC_SUFFIX>`: hits, errors, latency/duration, Apdex) are computed on 100% of traffic and behave like any other Datadog metric: dashboards, monitors, notebooks; **15-month** metric retention. Use them for long-range comparisons and post-mortems.
- **Generate custom metrics from spans/traces**: APM > Generate Metrics -> New Metric. Built from **ingested** spans, regardless of whether a retention filter indexes them; stored as custom metrics with **15-month retention**. Metric type Spans or Traces (trace metrics from Trace Queries emitted after the trace completes). Names starting with `trace.*` are not allowed. Billed as custom metrics; avoid high-cardinality group-bys. After creation only the filter query and aggregation groups can be edited.
- Span-based metrics depend on ingestion sampling (50% ingestion -> metric based on 50% of spans), so they can differ from trace metrics.

Sources: https://docs.datadoghq.com/tracing/metrics/, https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/, https://docs.datadoghq.com/tracing/troubleshooting/#trace-metrics

### Software Catalog and service/resource page data windows

- Catalog (renamed from Service Catalog/Software Catalog, at `app.datadoghq.com/services`): "Span summaries and service and resource statistics are retained for **up to 30 days**. For deeper analysis on APM trace metrics, use **Metric Explorer**."
- APM-instrumented services missing from the Catalog list: usually they have not emitted performance data **in the past hour** for the selected `env` (or other primary tag). Hover on the Performance tab columns to see which envs are active.
- Service metadata (entity definitions, `service.datadog.yaml`) is retained for the duration of the account (Data Retention Periods table still says "Service Catalog").
- Ingestion Control service table lists services with data ingested in the past one hour.
- Diversity sampling guarantees example traces on service and resource pages even for low-traffic endpoints.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/, https://docs.datadoghq.com/internal_developer_portal/catalog/troubleshooting/, https://docs.datadoghq.com/data_security/data_retention_periods/

### Continuous Profiler retention

- Flame graphs, call graphs and thread timelines: **8 days** by default.
- Profile metrics (e.g. top CPU by method, memory by thread, CPU by version): **one month (30 days)**.
- Export a flame graph to a **notebook** to keep it **1 year**.
- Individual profiles opened in the UI at least once: **1 year**.
- APM Enterprise includes Continuous Profiler with **4 profiled containers per host per month**; extra containers billed ($2 each in examples).

Sources: https://docs.datadoghq.com/profiler/, https://docs.datadoghq.com/data_security/data_retention_periods/, https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/

### Error Tracking retention

- Error samples: **30 days**. Issues: **1 year after last activity**.
- Auto-resolve: an issue is RESOLVED if last seen in a version more than 14 days old and a newer version does not report it; without `version` tags, after 14 days with no new errors. Issues marked `New` if first seen less than two days ago.
- `EXCLUDED` status stops collecting new errors for an issue and stops counting them toward usage/billing.
- Error span must have `error.stack`, `error.message`, `error.type` and belong to a complete trace.

Sources: https://docs.datadoghq.com/data_security/data_retention_periods/, https://docs.datadoghq.com/tracing/error_tracking/issue_states/, https://docs.datadoghq.com/tracing/error_tracking/explorer/

### Billing allotments tied to retention

- APM Host ($31), APM Pro ($35, + Data Streams Monitoring), APM Enterprise ($40, + DSM + Continuous Profiler): each includes **1 million Indexed Spans and 150 GB of Ingested Spans per month per APM host**.
- Fargate: **195,000 Indexed Spans and 30 GB Ingested Spans** per task.
- Lambda: 150,000 indexed spans per 1 million invocations.
- Overage: **$1.70 per million indexed spans**, **$0.10 per GB ingested**. Example: 5 hosts, 30M indexed, 900 GB ingested -> 25M indexed overage and 150 GB ingested overage. Pricing examples assume the default **15-day** indexed span retention.
- Ingestion is metered by volume (GB), indexing by span count. Spans indexed by the intelligent retention filter do not count.
- Host billing: APM hosts are counted once an hour; on a high watermark plan Datadog bills on the ninth highest hourly measurement of the month (eighth in February). Kubernetes is priced by nodes, not pods.
- No Flex/long-term archive tier for spans is documented in current APM docs; long-term = metrics, or "15 or 30 days determined by customer plan" for indexed spans.

Sources: https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/, https://docs.datadoghq.com/account_management/billing/pricing/#apm, https://docs.datadoghq.com/data_security/data_retention_periods/

### Common pitfalls

- "15 minutes" = Live Search of ingested spans; "15 days" = custom-filter indexed spans; "30 days" = intelligent-filter spans, span summaries, profile metrics, Error Tracking samples; "15 months" = metrics; "8 days" = profiles; "1 year" = notebook-exported flame graphs, opened profiles, Error Tracking issues after last activity.
- Disabling or editing retention filters does not reduce ingested GB.
- Trace analytics monitors need custom retention filters; intelligent-filter spans are excluded.
- Trace Queries need complete traces: intelligent filter or a trace rate.
- An indexed span shows the full trace, but non-indexed spans of that trace are not searchable.
- Live Search data cannot be exported to dashboards/monitors; use retained spans.
- Filter order: the first matching filter decides.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/tracing/trace_explorer/

# Domain 2: Application Instrumentation

## Datadog Tracing Libraries

### What the SDKs are and how they are configured
- The docs now call the tracing libraries **Datadog SDKs** ("Configure the Datadog SDK", "Add the Datadog SDK"). Official SDKs: Java, Python (`ddtrace`), Ruby, Go, Node.js (`dd-trace`), PHP, C++, .NET Core and .NET Framework, Rust, plus Android and iOS. For a language with no official SDK, use a **community SDK** (community tracing libraries).
- Setup has two steps: (1) install and configure the Agent, which receives traces at `http://localhost:8126` by default (`apm_config: enabled: true` in `datadog.yaml`), and (2) add the SDK to the application.
- Containers: set `apm_non_local_traffic: true` in `apm_config` so the Agent accepts traces from other containers.
- SDKs are configured with **environment variables** (the recommended approach and common to all languages), plus language-specific options: Java system properties (`-Ddd.*`), Python `ddtrace.config`, Node.js `init({...})`, .NET `web.config`/`app.config`/`datadog.json`, PHP INI (`datadog.*`).
- Check what a service is actually running with: **APM Service Page > Service Config > SDK Configuration** tab.
- Rules that apply to every SDK:
  - DD_ env vars are UPPER_SNAKE_CASE.
  - An env var set on the process **overrides** host-level `application_monitoring.yaml`.
  - Remotely set (Remote Configuration) sampling settings **take precedence over local** configuration.

Sources: https://docs.datadoghq.com/tracing/trace_collection/library_config/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/

### Agent connection: DD_AGENT_HOST, DD_TRACE_AGENT_PORT, DD_TRACE_AGENT_URL
- Default trace target: the SDK first tries the Unix domain socket **`/var/run/datadog/apm.socket`**. If that socket does not exist, it sends to **`http://localhost:8126`**. Stats and metrics follow the same pattern: first `/var/run/datadog/dsd.socket`, then `localhost:8125` (DogStatsD).
- `DD_AGENT_HOST`: the Agent host for trace submission. It also sets the host the SDK uses for runtime-metric (DogStatsD) submission. Defaults: `localhost` in Python and the runtime metrics docs, `127.0.0.1` in Node.js. It is **ignored if `DD_TRACE_AGENT_URL` is set**.
- `DD_TRACE_AGENT_PORT`: Trace Agent port, **default `8126`**. It is ignored if `DD_TRACE_AGENT_URL` is set. If the Agent's `receiver_port` or `DD_APM_RECEIVER_PORT` is not 8126, then `DD_TRACE_AGENT_PORT` or `DD_TRACE_AGENT_URL` must match it.
- `DD_TRACE_AGENT_URL`: the full URL, either HTTP or a UDS, for example `http://custom-hostname:1234` or `unix:///var/run/datadog/apm.socket`. It **has priority over host and port**. In Java the default is `http://<DD_AGENT_HOST>:<DD_TRACE_AGENT_PORT>` (alias `DD_TRACE_URL`).
- `DD_TRACE_AGENT_HOSTNAME` (Python): takes precedence over `DD_AGENT_HOST`. The fallback chain is DD_AGENT_HOST, then the UDS, then localhost.
- DogStatsD settings:
  - `DD_DOGSTATSD_PORT`: default `8125`. It must match the Agent's `dogstatsd_port`.
  - `DD_DOGSTATSD_URL`: `udp://` or `unix://` only. It takes precedence over `DD_AGENT_HOST` and `DD_DOGSTATSD_PORT`.
  - `DD_DOGSTATSD_HOST`: can be overridden by `DD_AGENT_HOST`.
- Python only: `DD_TRACE_AGENT_TIMEOUT_SECONDS` (default `2.0`), `DD_TRACE_WRITER_INTERVAL_SECONDS` (flush every `1.0` s), `DD_TRACE_WRITER_BUFFER_SIZE_BYTES` (20 MB), `DD_TRACE_PARTIAL_FLUSH_ENABLED` (default true), `DD_TRACE_PARTIAL_FLUSH_MIN_SPANS` (Python `300`, Java `1000`).
- Where `DD_AGENT_HOST` should point in containers:
  - ECS on EC2: the EC2 metadata endpoint.
  - ECS Fargate and EKS Fargate: **do not set** `DD_AGENT_HOST`. The Agent is a sidecar on localhost.
  - Elastic Beanstalk single container: the gateway IP (usually `172.17.0.1`).
  - Kubernetes: a UDS, `status.hostIP` through the downward API, or the Admission Controller.
  - Docker: the Agent container.
- Test connectivity from the app container with `curl -X GET http://{agent_ip}:{agent_port}/info`. Check the Agent with `agent status` and look at the APM Agent section (`Receiver: 0.0.0.0:8126`).
- Agent 7.80.0+ on Linux: the trace-agent starts only after it receives trace data (socket activation), so "not running" can be normal. Turn this off with `apm_config.socket_activation.enabled: false` or `DD_APM_SOCKET_ACTIVATION_ENABLED=false`.
- Python agentless mode (ddtrace v4.15.0+):
  - Set `DD_AGENTLESS_ENABLED=true`, `DD_API_KEY` and `DD_SITE`. The SDK raises an error at startup if the API key is missing.
  - Sent without an Agent: traces, Remote Config, Dynamic Instrumentation, Test Optimization, LLM Observability.
  - Still need an Agent: runtime metrics, profiling and tracer flares.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://docs.datadoghq.com/tracing/trace_collection/library_config/java/, https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/

### Core env vars to know
- Unified service tagging:
  - `DD_SERVICE`: the `service` tag on every span. Aliases are `DD_SERVICE_NAME` and `OTEL_SERVICE_NAME`. If unset, the SDK auto-detects it: Node.js uses `package.json` `name`, Java uses the application class, .NET uses the IIS app name or entry assembly.
  - `DD_ENV`: the `env` tag on traces, metrics, logs and profiles.
  - `DD_VERSION`: the `version` tag.
- `DD_TAGS`: global tags on spans, as comma-separated `key:value` pairs (Python also accepts spaces). Python alias: `OTEL_RESOURCE_ATTRIBUTES`. Java's `DD_TRACE_SPAN_TAGS` adds tags to every span only.
- `DD_TRACE_ENABLED`: default `true`. Turns tracing on or off. Per the registry: "When disabled, instrumentation still runs but no trace data is sent". In the Java example, `-Ddd.trace.enabled=false` logs "Tracing is disabled, not installing instrumentations."
- `DD_APM_TRACING_ENABLED` (alias `DD_TRACING_ENABLED`): default `true`. If false, tracing still runs to support other products (for example AppSec), but only periodic heartbeat traces and manually kept traces are sent.
- `DD_TRACE_DEBUG`: default `false`. Debug mode. It takes precedence over `DD_TRACE_LOG_LEVEL` (alias `DD_LOG_LEVEL`). OTel alias: `OTEL_LOG_LEVEL`.
- `DD_TRACE_STARTUP_LOGS`: startup configuration logs. On by default in most SDKs, except **Node.js 2.x+, where they are off by default**.
- `DD_LOGS_INJECTION`: injects trace and span IDs into logs.
  - The registry shows **default `true`** for Python, Java and Node.js.
  - Python changed to default true in **v3.10.0**, when `ddtrace-run` or `import ddtrace.auto` is used. Before that it was off by default.
  - Set `DD_LOGS_INJECTION=false` to disable it.
  - Python log record attributes: `dd.trace_id`, `dd.span_id`, `dd.service`, `dd.env`, `dd.version`.
- `DD_RUNTIME_METRICS_ENABLED`: default **`true` for Java and .NET 6+ (v3.40.0+)**, `false` for all other languages.
- `DD_TRACE_SAMPLE_RATE` (alias `OTEL_TRACES_SAMPLER`): a 0.0-1.0 root sample rate. The ingestion docs mark it **deprecated for Java, Python and Go**. Use `DD_TRACE_SAMPLING_RULES='[{"sample_rate":0.1}]'` instead. Ruby still documents `DD_TRACE_SAMPLE_RATE` as a global rate.
- `DD_TRACE_SAMPLING_RULES`:
  - A JSON array of objects. Each object needs `sample_rate` (0.0-1.0 inclusive) and may also have `service`, `name`, `resource`, `tags` and `max_per_second`.
  - Rules are evaluated **in order, and the first match wins**.
  - Examples: `[{"sample_rate": 0.2}]`; `[{"service": "a.*", "name": "b", "sample_rate": 0.1}, {"sample_rate": 0.2}]`; `[{"tags": {"tier": "premium"}, "sample_rate": 1}]`.
  - The service name match is case-sensitive.
  - Traces kept by these rules get `ingestion_reason: rule`. The Agent default gets `auto`.
- `DD_TRACE_RATE_LIMIT`: default **100 traces per second per service instance**. It applies only when SDK sampling rules or a sample rate are set. It is ignored under the Agent's default mechanism (the Agent's target is 10 traces per second, `DD_APM_TARGET_TPS`).
- `DD_SPAN_SAMPLING_RULES` and `DD_SPAN_SAMPLING_RULES_FILE`: single-span sampling. If both are set, the env var wins and the file is ignored.
- `DD_TRACE_HEADER_TAGS`: turns HTTP headers into span tags. The header list is case-insensitive and acts as an allowlist; with no config, no headers are traced. With no custom tag name, the tag key is `http.request.headers.<header>` or `http.response.headers.<header>`. Example: `User-Agent:http.useragent`.
- `DD_SERVICE_MAPPING`: renames the service names that integrations produce, for example `postgres:postgresql,defaultdb:postgresql` or (Java) `-Ddd.service.mapping=postgresql:web-app-pg`.
- `DD_TRACE_HTTP_SERVER_ERROR_STATUSES`: default `500-599`. Example: `500-599,404`. `DD_TRACE_HTTP_CLIENT_ERROR_STATUSES`: default `400-499` (Java).
- Query strings:
  - `DD_HTTP_SERVER_TAG_QUERY_STRING` (default true).
  - `DD_TRACE_HTTP_CLIENT_TAG_QUERY_STRING` (default true).
  - `DD_TRACE_OBFUSCATION_QUERY_STRING_REGEXP` redacts sensitive query strings. Setting it to `""` disables obfuscation. An invalid regex means query strings are not traced.
- Propagation:
  - `DD_TRACE_PROPAGATION_STYLE_EXTRACT` and `_INJECT`: default `datadog,tracecontext,baggage`.
  - `DD_TRACE_PROPAGATION_BEHAVIOR_EXTRACT`: `continue` (default), `restart` (incoming context becomes a span link) or `ignore`.
  - `DD_TRACE_128_BIT_TRACEID_GENERATION_ENABLED`: default true.
  - `DD_TRACE_X_DATADOG_TAGS_MAX_LENGTH`: default `512`.
- `DD_TRACE_REPORT_HOSTNAME`: default false. When false, the Agent's hostname is used.
- `DD_INSTRUMENTATION_TELEMETRY_ENABLED`: default true. Set it to false to opt out.
- `DD_PROFILING_ENABLED`: default false. Enables the Continuous Profiler.
- `DD_DATA_STREAMS_ENABLED`: default false.
- `DD_DBM_PROPAGATION_MODE`: `disabled` (default), `service` or `full`.
- OpenTelemetry aliases are accepted for several keys, for example `OTEL_SERVICE_NAME`, `OTEL_RESOURCE_ATTRIBUTES`, `OTEL_TRACES_SAMPLER` and `OTEL_TRACES_EXPORTER`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://docs.datadoghq.com/tracing/trace_collection/library_config/java/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://ddtrace.readthedocs.io/en/stable/configuration.html

### Java SDK specifics
- Download `dd-java-agent.jar` from `https://dtdg.co/latest-java-tracer`. For the latest build of one major version, use `https://dtdg.co/java-tracer-vX`, for example `java-tracer-v1`. Specific versions are on Maven.
- Attach the agent with `-javaagent:/path/to/dd-java-agent.jar`.
  - Put it **before `-jar`**, as a JVM option, not an application argument.
  - **Never add `dd-java-agent` to the classpath.**
  - Example: `java -javaagent:/path/dd-java-agent.jar -Ddd.profiling.enabled=true -Ddd.logs.injection=true -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar app.jar`.
- System properties vs env vars:
  - Every option has both forms. **If both are set, the system property takes priority.**
  - List system properties before `-jar`.
  - Converting: `dd.service` becomes `DD_SERVICE` (uppercase it and replace `.` or `-` with `_`). `DD_TAGS` becomes `dd.tags` (lowercase it and replace `_` with `.`).
- Where to put `-javaagent` per app server:
  - Spring Boot: `my_app.conf` with `JAVA_OPTS=-javaagent:...`.
  - Tomcat: `setenv.sh` `CATALINA_OPTS`.
  - JBoss: `standalone.conf` `JAVA_OPTS`, or `domain.xml`.
  - Jetty: `jetty.sh` `JAVA_OPTIONS`, or `start.ini` under `--exec`.
  - WebSphere: Generic JVM arguments.
- Runtimes: v1 is GA for Java 8 to 27 (Java 28+ is Preview). Java 7 (tracer v0) is EOL. Classes loaded with a remote ClassLoader are not auto-instrumented. Java 24+ may show JNI warnings, which `--enable-native-access=ALL-UNNAMED` suppresses.
- Integrations:
  - Integrations in Preview are **disabled by default**. Enable one with `-Ddd.integration.<NAME>.enabled=true` or `DD_INTEGRATION_<NAME>_ENABLED=true`.
  - The Java configuration registry also lists `DD_TRACE_<NAME>_ENABLED` as the primary per-integration key, with `DD_INTEGRATION_<NAME>_ENABLED` and `DD_TRACE_INTEGRATION_<NAME>_ENABLED` as aliases (for example `DD_TRACE_JDBC_DATASOURCE_ENABLED`). So `DD_TRACE_<NAME>_ENABLED` is NOT Python-only.
  - Disable all integrations by default with `DD_INTEGRATIONS_ENABLED=false` (`-Ddd.integrations.enabled=false`).
  - Disabled by default: JDBC Datasource (`DD_INTEGRATION_JDBC_DATASOURCE_ENABLED=true`), Grizzly, Hazelcast, Ignite, JAX-WS, Mule, Netty Promise, Ning, Spark Java, TIBCO, URL Connection.
- Other Java options:
  - `dd.trace.methods` traces methods with no code change, for example `-Ddd.trace.methods=store.db.SessionManager[saveSession,loadSession]`. The span's operation name is `trace.annotation` and its resource is `SessionManager.saveSession`.
  - `@Trace` takes `operationName`, `resourceName` and `noParent`, and needs `dd-trace-api`.
  - `dd.trace.annotations` treats other annotations as `@Trace`.
  - `dd.trace.db.client.split-by-instance=true` gives each DB instance its own service.
  - `dd.trace.classes.exclude` lists classes the tracer must not modify.
  - JMX: `DD_JMXFETCH_ENABLED` default true. Use `DD_JMXFETCH_CONFIG_DIR` plus `DD_JMXFETCH_CONFIG` to add custom JMX metrics. `dd.trace.jmx.tags` tags JMX metrics.
  - `TraceInterceptor` (`onTraceComplete`, `priority`) filters or changes spans.
- Remote Configuration is on by default in the Java SDK. Disable it with `DD_REMOTE_CONFIG_ENABLED=false` or `-Ddd.remote_config.enabled=false`.
- Diagnostic CLI (0.82.0+): `java -jar dd-java-agent.jar sampleTrace -c 1` sends a sample trace to test the connection.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/, https://docs.datadoghq.com/tracing/trace_collection/library_config/java/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/

### Python SDK (ddtrace) specifics
- Install with `pip install ddtrace` (needs pip 18.0.0+). Instrument by prefixing the entry point with **`ddtrace-run`**, for example `ddtrace-run python app.py`, `ddtrace-run gunicorn myapp.wsgi:application`, `ddtrace-run python manage.py runserver`.
- **`ddtrace-run --info`** prints a readable tracer health check and configuration. It shows **only env var configuration, not changes made in code**.
- `import ddtrace.auto` as the very first import gives the same automatic instrumentation (plus profiling, ASM, DI where enabled) when you cannot use `ddtrace-run`.
  - Do not combine it with `ddtrace-run`.
  - Gunicorn with gevent workers and no ddtrace-run: import `ddtrace.auto` as early as possible.
  - uWSGI: `ddtrace-run` is **not supported**. Use `--import=ddtrace.bootstrap.sitecustomize` and enable threads, plus `lazy-apps` or `py-call-uwsgi-fork-hooks`.
- Which integrations get patched:
  - Most are patched automatically by ddtrace-run or `ddtrace.auto`. Some are off by default: **urllib3, httplib, aiobotocore**, MLflow and others.
  - Turn them on with `DD_PATCH_MODULES="urllib3:true"` (format `module:bool,...`) or `DD_TRACE_<INTEGRATION>_ENABLED=true`, for example `DD_TRACE_URLLIB3_ENABLED`.
  - Turn one off with `DD_TRACE_DJANGO_ENABLED=false`.
  - Or patch manually: `from ddtrace import patch; patch(aiobotocore=True)`. The docs say calling `patch()` directly is not recommended.
  - Override an integration's service name with `DD_<INTEGRATION>_SERVICE`, for example `DD_URLLIB3_SERVICE`.
- Compatibility: ddtrace 4.x is GA and needs Agent 7.63.0+ and CPython 3.9+. 3.x is in Maintenance until May 31, 2026. 2.x and earlier are EOL.
  - Support lifecycle: GA lasts 12 months, Maintenance 6 months, and a major version is EOL 18 months after its x.0.0 release.
  - v4 dropped Python 3.8. v3 dropped Python 3.7.
- Manual and advanced API, from `from ddtrace import tracer`:
  - `@tracer.wrap(name, service=..., resource=...)` is a decorator.
  - `with tracer.trace("op.name", resource=...) as span:` is a context manager.
  - With `span = tracer.trace("op")`, you **must call `span.finish()`**, or the span is not sent.
  - `tracer.current_span()` and `tracer.current_root_span()` return the active span and the local root.
  - `span.set_tag("k", v)` adds a local tag. `tracer.set_tags({...})` adds a global tag to every span.
  - Errors: `span.error = 1`, or `root_span.set_exc_info(exc_type, exc_val, exc_tb)`. An exception raised inside an active span marks the span as an error and attaches the stack and message. `span.record_exception(e)` reports a handled error (3.1.1+).
  - `span.link_span(ctx, attributes=...)` adds a span link.
  - Baggage: `span.context.set_baggage_item(...)`.
  - The `ddtrace-api` package (Preview) is a stable interface only. Use it with `from ddtrace_api import tracer`.
- Context:
  - Use `tracer.current_trace_context()` and `tracer.context_provider.activate(ctx)` to continue a trace across threads or processes.
  - Before crossing an execution boundary, run `tracer.sample(tracer.current_root_span())` so the whole trace gets the same sampling decision.
  - The futures integration propagates context to `ThreadPoolExecutor` automatically.
  - asyncio copies contextvars to new tasks.
- Trace filters:
  - Subclass `TraceFilter` and implement `process_trace(self, trace)`. **Return the trace to keep it, or `None` to drop the whole trace chunk.**
  - Register it with `tracer.configure(trace_processors=[MyFilter()])`.
  - Filters run in sequence, before traces are sent to the Agent.
- Distributed tracing is supported out of the box for aiohttp, Bottle, Django, Falcon, Flask, Pyramid, Requests and Tornado. Use `HTTPPropagator` for custom transports. ddtrace uses lazy sampling.
- Logging:
  - The SDK logs through the `ddtrace` logger.
  - The `logging` integration is patched by default under ddtrace-run or `ddtrace.auto`, or with `ddtrace.patch(logging=True)`.
  - Your log format must include `%(dd.trace_id)s`, `%(dd.span_id)s` and the other `dd.*` attributes.
- OpenTracing for Python is deprecated. Use the Datadog API or the OpenTelemetry API.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/, https://ddtrace.readthedocs.io/en/stable/advanced_usage.html, https://ddtrace.readthedocs.io/en/stable/basic_usage.html, https://ddtrace.readthedocs.io/en/stable/integrations.html, https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/dd-api/

### Host-level config: application_monitoring.yaml (Linux)
- File: **`/etc/datadog-agent/application_monitoring.yaml`**. It applies to every SDK loaded on the host, including SDKs loaded through Single Step Instrumentation.
- Put keys under **`apm_configuration_default:`**, for example:
  ```yaml
  apm_configuration_default:
    DD_PROFILING_ENABLED: true
    DD_DATA_STREAMS_ENABLED: true
    DD_APM_TRACING_ENABLED: false
  ```
- **Environment variables override the file.** Restart services after you change it.
- Any library configuration env var is allowed in the file. The Go SDK supports only APM tracing options.
- Minimum SDK versions: Java v1.47.0, Python v3.2.0, Node.js v5.41.0, .NET v3.25.0, PHP v1.8.0, Ruby v2.18.0, Go v2.1.0.

Sources: https://docs.datadoghq.com/tracing/trace_collection/library_config/application_monitoring_yaml/

### Configuration at runtime (Remote Configuration)
- Configuration at runtime changes SDK configuration from the Datadog UI **without restarting** the application or redeploying.
- It needs **Remote Configuration**. It is not supported on the US1-FED/ddog-gov sites.
- UI path:
  1. Software Catalog in APM.
  2. Open the service's Full Page.
  3. **Service Info > Service Config > SDK & Agent Configurations**.
  4. Select an environment, click **Edit** on the row, and confirm.
- "Updates applied to X instances" confirms the change. An instance is one Remote Configuration client, normally one per process.
- The **Setup Guidance** tab no longer has an editing panel. It shows a banner pointing to the SDK & Agent Configurations tab.
- Options you can change at runtime:
  - Custom sampling rate (`DD_TRACE_SAMPLE_RATE`).
  - Log injection (`DD_LOGS_INJECTION`).
  - HTTP header tags (`DD_TRACE_HEADER_TAGS`).
  - Custom span tags (`DD_TAGS`).
  - Resource-based sampling (`DD_TRACE_SAMPLING_RULES`).
  - Adaptive Sampling (Datadog sets rates to meet a monthly ingested volume budget).
- Minimum SDK versions for these options:
  - Sample rate, log injection and header tags: Java 1.17.0+, Node.js 4.11+/3.32+/2.45+, Python 2.4.0+ (sample rate) or 2.6.0+ (logs and headers), .NET 2.33.0+, Ruby 1.13.0+. Go 1.59.0+ is listed for sample rate and header tags only (no Go entry for log injection).
  - Resource-based sampling: Java 1.34.0+, Python 2.9.0+.
- Setting up Remote Configuration for tracing:
  - Prerequisites: Agent **7.47.0+**, the `org_management` permission (to enable RC for the org), `api_keys_write` (to give an API key the RC capability), and the **APM Remote Configuration Read** and **APM Remote Configuration Write** permissions.
  - Steps: enable RC for the organization (Organization Settings > Remote Configuration), enable the RC capability on the API key, then restart the Agent.
  - From Agent 7.47.0, `remote_configuration.enabled` is **true by default**. Opt out with `remote_configuration: enabled: false`, `DD_REMOTE_CONFIGURATION_ENABLED=false`, or Helm `datadog.remoteConfiguration.enabled: false`. You can also opt out per API key or for the whole org; the org level is **not recommended**.
- SDK statuses in the Remote Configuration UI:

| Status | Meaning |
| --- | --- |
| CONNECTED | Working. |
| UNAUTHORIZED | The Agent's API key lacks the RC capability (`APM Remote Configuration Read`). Fix: enable RC on the API key. |
| CONNECTION ERROR | `remote_config.enabled` is true, but the Agent cannot reach the RC endpoints. Allow outbound HTTPS. |
| DISABLED | The Agent has `remote_config.enabled: false`. |
| NOT CONNECTED | The SDK is not found in the RC service. Check the Agent config or proxy. |
| UNSUPPORTED AGENT | Upgrade the Agent. |
| NOT DETECTED | The SDK does not support RC. Upgrade the SDK. |
| UNKNOWN | For example, on Fargate. |

- SDK side: `DD_REMOTE_CONFIGURATION_ENABLED` (alias `DD_REMOTE_CONFIG_ENABLED`) defaults to true.
- Sampling from the Ingestion Control page uses RC. **Remote settings take precedence over local ones.**

Sources: https://docs.datadoghq.com/tracing/trace_collection/runtime_config/, https://docs.datadoghq.com/tracing/guide/remote_config/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/

### Tracer startup logs
- Startup logs capture what the SDK knows at startup. Search for these prefixes: `DATADOG TRACER CONFIGURATION`, `DATADOG TRACER DIAGNOSTICS`, `DATADOG ERROR` or `DATADOG CONFIGURATION`.
- `CONFIGURATION`: JSON of the applied settings, for example `service`, `env`, `agent_url`, `debug`, `sample_rate`, `sampling_rules`, `log_injection_enabled` and `runtime_metrics_enabled`. Where the SDK checks Agent connectivity, the JSON has an **`agent_error`** key that shows whether the Agent is reachable.
- `DIAGNOSTICS` or `ERROR`: the SDK hit an error at startup.
- If there are no logs at all, make sure application logs are not silenced and the log level is at least `INFO`.
- Per language:
  - **Java:** no Diagnostics logs. Use debug mode for that check.
  - **.NET:** files in `/var/log/datadog/dotnet/` (Linux) or `%ProgramData%\Datadog .NET Tracer\logs\` (Windows), or `/datadog-lib/logs` with K8s library injection. Change the path with `DD_TRACE_LOG_DIRECTORY`. `DD_TRACE_LOGFILE_RETENTION_DAYS` (2.19.0+, default `32`) deletes old files. The managed log holds the configuration and the native log holds diagnostics.
  - **PHP:** `phpinfo()` page or `php --ri=ddtrace`. At runtime: `\DDTrace\startup_logs()`. In DEBUG mode, the logs go to `error_log` once per process on the first request.
  - **Go:** a WARN `DIAGNOSTICS` line for an unreachable Agent or for errors parsing `DD_TRACE_SAMPLING_RULES`.
  - **Node.js:** **off by default since 2.x**. Enable with `DD_TRACE_STARTUP_LOGS=true`.
  - **Python:** configuration logs at INFO and diagnostics at ERROR. With no logging configuration, only Diagnostics go to stderr. To see startup logs, add a logger, or set `DD_TRACE_DEBUG=true` and run with `ddtrace-run`.
  - **Ruby:** enable with `c.diagnostics.startup_logs.enabled = true` or `DD_TRACE_STARTUP_LOGS=true`. One configuration line per product (PROFILING, CORE, TRACING).
  - **C++:** no diagnostics lines. In Envoy, watch `tracing.datadog.reports_failed` and `tracing.datadog.reports_dropped`.
- Turn startup logs off in any language with `DD_TRACE_STARTUP_LOGS=false`, but only if they cause problems. Turn them back on when you send debug logs to support.
- If you see only CONFIGURATION lines, compare them with your deployment settings and check the Compatibility Requirements.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/tracer_startup_logs/, https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/

### Tracer debug logs and tracer flares
- Debug mode is **off by default**. Datadog does **not recommend it in production**, because it raises the number of events sent to your loggers.
- How to enable it per language:
  - Java: `-Ddd.trace.debug=true` or `DD_TRACE_DEBUG=true`. The Java tracer uses SLF4J SimpleLogger: `-Ddatadog.slf4j.simpleLogger.logFile=<path>`, and `...jsonEnabled=true` (or `DD_LOG_FORMAT_JSON`, 1.58.0+) for JSON output.
  - Python: `DD_TRACE_DEBUG=true`.
    - `DD_TRACE_LOG_FILE=ddtrace_logs.log` writes to a file, relative to the working directory. The default max size is **15728640 bytes (about 15 MB) with 1 backup**. Change the size with `DD_TRACE_LOG_FILE_SIZE_BYTES` and the file level with `DD_TRACE_LOG_FILE_LEVEL`.
    - If the app sets the **root logger to DEBUG**, ddtrace debug logs appear too. To stop that, set `DD_TRACE_LOG_LEVEL` (v4.4.0+; cannot be combined with `DD_TRACE_DEBUG=true`), or call `logging.getLogger("ddtrace").setLevel(logging.WARNING)`.
    - In code: `logging.getLogger("ddtrace.tracer").setLevel(logging.DEBUG)`.
  - Go: `DD_TRACE_DEBUG=true` or `tracer.WithDebugMode(true)`. Abandoned spans: `DD_TRACE_DEBUG_ABANDONED_SPANS=true`, with a default timeout of `10m` (`DD_TRACE_ABANDONED_SPAN_TIMEOUT`).
  - Node.js: `DD_TRACE_DEBUG=true`. Logs go to `console.log` and `console.error`, or to a custom logger with `debug()` and `error()`. Below 2.x you could enable it in code, which is no longer supported.
  - .NET: `DD_TRACE_DEBUG` (env, `web.config`, `app.config` or `datadog.json`), or `GlobalSettings.SetDebugEnabled(true)`. On Linux, create the log directory first.
  - PHP: `DD_TRACE_DEBUG=true`. Files with `DD_TRACE_LOG_FILE` or `datadog.trace.log_file` (0.98.0+). Otherwise logs go to the PHP `error_log`.
  - Ruby: `DD_TRACE_DEBUG=true`. Messages are tagged `[ddtrace]`.
- What debug logs show: how the SDK started, spans being finished, and whether traces reached the Agent.
  - Python, sent: `sent 1.57KB ... to http://localhost:8126/v0.4/traces`. Failed: `failed to send traces to Datadog Agent at ...`.
  - Java, sent: `Successfully sent 1 of 2 traces to the DD agent`.
  - Node.js: `Response from the Agent: OK` versus `Error from the Agent`.
- **Automated debug log collection (tracer flare):**
  - Supported only for **Java (1.26.0+), Python (3.12.0+), Node.js (5.15.0+ or 4.39.0+) and .NET (2.46.0+)**.
  - Needs **Remote Configuration** enabled and an API key configured for RC. Not available on ddog-gov.
  - Steps: **Fleet Automation**, select the Agent, **Support**, **Send Support Ticket**. Give a Zendesk ticket number or one is created. Optionally enable **Debug mode** (the log level is reset afterward) and application tracer-level logs. Click **Send Ticket**.
  - If your service is not listed, there is likely a connection error, so collect logs manually.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/, https://ddtrace.readthedocs.io/en/stable/advanced_usage.html

### Runtime metrics
- Runtime metrics cover memory, garbage collection, CPU and threads. The SDK collects them and sends them to the Agent **through DogStatsD (UDP 8125 by default)**. Without a Datadog SDK, see OTel runtime metrics.
- Defaults per language:
  - Enabled by default: Java (0.29.0+, Java 8+) and .NET 6+ (v3.40.0+).
  - Opt-in: Python (0.30.0+, Preview), Ruby (0.44.0+, also needs the `dogstatsd-ruby` gem), Go (1.18.0+), Node.js (3.0.0+).
  - **Not supported: PHP and C++.**
  - JMX metric collection is not supported in AWS Lambda.
- Setup step 1, the Agent: enable DogStatsD.
  - In containers, `dogstatsd_non_local_traffic: true` must be on. It is the default, so turn it back on only if it was disabled.
  - Set `DD_SITE` on the Agent for non-US1 sites.
- Setup step 2, the application (env vars):
  - `DD_RUNTIME_METRICS_ENABLED`: default true for Java and .NET 6+, false for the rest.
  - `DD_RUNTIME_METRICS_RUNTIME_ID_ENABLED`: adds a `runtime_id` tag to every metric so you can correlate metrics with individual processes. Default true for Java, false for Node.js, Ruby and Python. It does not exist for .NET and Go, which always report it.
  - `DD_AGENT_HOST`: default `localhost`.
  - `DD_DOGSTATSD_PORT`: default `8125`.
  - `DD_RUNTIME_METRICS_DIAGNOSTICS_METRICS_API_ENABLED`: .NET only, uses `System.Diagnostics.Metrics`.
- Setup step 2, the application (code):
  - Java and .NET: **only env vars**. Java can add custom JMX metrics.
  - Python: `from ddtrace.runtime import RuntimeMetrics; RuntimeMetrics.enable()`, **only when you are not using `ddtrace-run`**.
  - Ruby: `c.runtime_metrics.enabled = true`.
  - Go: `tracer.Start(tracer.WithRuntimeMetrics())`, plus `WithDogstatsdAddr("host:8125")` for a non-default address.
  - Node.js: `init({ runtimeMetrics: true })`.
- Where to see them: the service's details page, the **flame graph Metrics tab**, and the default runtime dashboards.
- Troubleshooting:
  - To link runtime metrics in flame graphs, the **`env` tag (case-sensitive) must be set and match**.
  - On Fargate, set `DD_DOGSTATSD_TAGS` on the Agent task with a matching `env`.
  - .NET Framework on IIS: add the app pool account (`IIS APPPOOL\<pool>`) to the **Performance Monitor Users** group.
- Metric names:
  - Java: `jvm.heap_memory`, `jvm.non_heap_memory` (Metaspace + CompressedClassSpace + CodeCache), `jvm.thread_count`, `jvm.gc.*` and others. `new_gc_metrics: true` in `jmx.d/conf.yaml` replaces `jvm.gc.cms.count`/`parnew.time` with major/minor collection metrics.
  - Python: `runtime.python.cpu.percent`, `runtime.python.mem.rss`, `runtime.python.gc.count.gen0..2`, `runtime.python.thread_count`.
  - Go: `runtime.go.num_goroutine` and `runtime.go.mem_stats.*`.
  - Ruby: `runtime.ruby.*`.

Sources: https://docs.datadoghq.com/tracing/metrics/runtime_metrics/

### Integrations auto-instrumented by the libraries
- Each SDK auto-instruments the frameworks, datastores and libraries listed on its Compatibility Requirements page.
- Python examples:
  - Automatic: Django, Flask, FastAPI, Starlette, Sanic, Celery, Requests, Redis, psycopg, pymongo, botocore, gRPC, asyncpg.
  - Not automatic: urllib3, httplib, aiobotocore, SQLAlchemy, Kombu, Tornado, Pyramid, Bottle and others. These need patching or env-var enablement.
- Java: most integrations are on by default. Preview integrations and some others are off. Toggle per integration with `DD_INTEGRATION_<NAME>_ENABLED` (registry primary key: `DD_TRACE_<NAME>_ENABLED`), or turn off all with `DD_INTEGRATIONS_ENABLED=false` (`DD_INTEGRATIONS_ENABLED=true` is the default and does not enable integrations that are off by default).
- Python: `DD_TRACE_<INTEGRATION>_ENABLED` (for example `DD_TRACE_REDIS_ENABLED=false`) and `DD_PATCH_MODULES=redis:true,requests:false`. Some Python integrations (for example redis, kafka, avro) also accept `DD_INTEGRATION_<NAME>_ENABLED` aliases; urllib3 does not. Per-integration service name: `DD_<INTEGRATION>_SERVICE`.
- If an integration you need is not supported, add custom instrumentation (Java `dd.trace.methods` or `@Trace`; Python `tracer.wrap` or `tracer.trace`), or ask support for a feature request.
- Common pitfalls:
  - Traces missing for a library: check that it appears in the Compatibility page and is enabled by default. Check `integrations_loaded` in the startup logs (Node.js and Ruby).
  - Containers sending to `localhost`: wrong unless on Fargate. Set `DD_AGENT_HOST` or use the UDS.
  - Port mismatch: the Agent `receiver_port` changed but `DD_TRACE_AGENT_PORT` did not.
  - Runtime metrics missing: DogStatsD port 8125/UDP is not reachable, or non-local traffic is disabled.
  - Two APM Java agents loaded at the same time is unsupported.

Sources: https://docs.datadoghq.com/tracing/trace_collection/compatibility/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/python/, https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/, https://ddtrace.readthedocs.io/en/stable/integrations.html

## Instrumentation Types

### The big picture: SDK setup vs span creation
- Instrumentation = adding code to an app to capture and report observability data (traces, metrics, logs) to Datadog.
- Application instrumentation has two parts:
  1. **SDK setup**: add a Datadog SDK (tracer) to the app.
  2. **Span creation**: capture work as spans.
- **Auto-instrumentation**: spans are generated automatically by default as soon as the SDK is loaded, for supported frameworks and libraries (web servers, DBs, caches, HTTP clients). Sufficient for most users.
- The docs assume a Datadog Agent is installed and configured to receive traces.
- Two ways to do **SDK setup**:
  | | Single Step Instrumentation (recommended) | Manually managed SDKs |
  |---|---|---|
  | How | Datadog installs and loads SDKs into app processes at runtime with a single command | You install and configure SDKs in app code or build process |
  | Code changes | No | Yes |
  | Setup complexity | Low | Medium (environment + build config) |
  | Config control | Standard defaults + optional overrides | Full control through env vars and code |
  | When | Start here: fast, consistent instrumentation across services | Progress to this when you need granular control over SDK behavior/config |
- Two ways to add **custom spans**:
  | | Dynamic Instrumentation | Code-based custom instrumentation |
  |---|---|---|
  | How | Rules configured in Datadog UI, applied at runtime | Explicit tracing API calls in code |
  | Code changes | No | Yes |
  | Deployment required | No | Yes (to add or modify spans) |
  | When | Add custom spans without code changes or redeploys | Complex instrumentation logic, or spans permanently defined in code |
- Options combine: e.g., SSI + code-based custom spans, or manually managed SDKs + Dynamic Instrumentation.
- Exam vocabulary: "automatic instrumentation" = SSI or Datadog SDKs (auto spans for supported libraries). "Custom instrumentation" = writing your own spans/tags with an API (Datadog API, OpenTelemetry API, OpenTracing legacy). The DI page also uses "manual custom instrumentation" for code-based spans. Official example: writing custom spans = **Custom Instrumentation** (not "Manual" or "Dynamic").
- Prefer vendor-neutral? Use OpenTelemetry (see OTel section).
- Unsupported language with no official SDK: use community SDKs (APM tracing client libraries). Elixir: Datadog provides no Elixir SDK; use the OpenTelemetry SDK for Elixir. Rust and Elixir support the OpenTelemetry API only, not the Datadog API; C++ supports only the Datadog API (no OTel API).
- Official SDKs: Java, Python, Ruby, Go, Node.js, PHP, C++, Rust, .NET Core, .NET Framework, Android, iOS.

Sources: https://docs.datadoghq.com/tracing/trace_collection/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/server-side/

### Manually managed Datadog SDKs (Agent side + app side)
- Steps: 1) install/configure the Agent; 2) add the Datadog SDK to the app.
- Agent receives traces by default: `apm_config` `enabled: true` in `datadog.yaml`, listening at `http://localhost:8126` (TCP 8126).
- Containers: set `apm_non_local_traffic: true` in `apm_config` (env `DD_APM_NON_LOCAL_TRAFFIC=true`).
- Trace client first tries the Unix domain socket `/var/run/datadog/apm.socket`; if absent, sends to `http://localhost:8126`. Override with `DD_TRACE_AGENT_URL`. Stats/DogStatsD: `/var/run/datadog/dsd.socket`, else `localhost:8125`.
- Python: `pip install ddtrace` (pip >= 18.0.0), then prefix entry point: `ddtrace-run python app.py`; `ddtrace-run --info` checks configuration (does not reflect runtime in-code changes). In code alternative: `import ddtrace.auto` as early as possible. Configuration via env vars is recommended. dd-trace-py v4 drops Python 3.8; v3 dropped 3.7.
- Java: download `dd-java-agent.jar` (`https://dtdg.co/latest-java-tracer`); `-javaagent:dd-java-agent.jar` must come **before** `-jar`. System properties `-Ddd.service`, `-Ddd.env`, `-Ddd.version`.
- AWS Lambda: see Serverless tracing docs (not SSI). Other envs: Heroku, Cloud Foundry, Elastic Beanstalk, Azure App Service.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python/

### Single Step Instrumentation (SSI)
- Automatically installs and loads the Datadog SDKs with no extra configuration; "onboarding time from days to minutes". When you install/update the Agent with APM Instrumentation enabled, the Agent loads the SDK into supported processes. No code changes.
- Prerequisites: remove custom instrumentation code and restart ("SSI is automatically disabled if custom instrumentation is detected"); check the SSI compatibility guide.
- After instrumenting: optionally configure Unified Service Tags; enable SDK-dependent products.
- Platforms: Linux host/VM, Docker, Kubernetes, Windows (IIS .NET GA; host-wide Java+.NET in Preview). **ECS Fargate is not supported**; EKS Fargate is Preview. Architectures x86_64 and arm64. Hardened SELinux not supported; very small instances (`t2.micro`) can time out (the preload library gives the analyzer one second) - use `t2.small`+.
- SSI languages: Java (SDK >= 1.44.0), Python (SDK >= 2.20.1, Python 3.7+), Ruby (>= 2.6.0; glibc 2.17+, not Alpine/musl), Node.js (>= 4.0; ESM not supported), .NET (>= 3.7.0), PHP (>= 1.6.0). No Go (compiled). If SDK or runtime unsupported, SSI falls back gracefully and the app runs uninstrumented.
- **Linux** new install:
  ```
  DD_API_KEY=<KEY> DD_SITE="<SITE>" DD_APM_INSTRUMENTATION_ENABLED=host \
  bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
  ```
  then restart apps. Default installs latest SDKs. Pin versions with `DD_APM_INSTRUMENTATION_LIBRARIES` = comma-separated `language:major` pairs, keys `java`, `js`, `python`, `dotnet`, `ruby`, `php` (e.g. `java:1,python:3`). Update SDK: re-run the install command (also updates Agent) and restart apps.
- Existing Agents: **APM > Instrument a Service** > "Deploy on existing hosts" (remote, through the Agent via Fleet). Rollout pauses if 3 consecutive Agents fail or failures reach 10%. Click **Apply Instrumentation**.
- Verify Linux: `sudo datadog-agent status`; `/etc/ld.so.preload` lists the injector; `/opt/datadog-packages/datadog-apm-*`.
- Linux removal: `dd-host-install --uninstall`, then restart services.
- Host injection only applies to **newly launched** processes (start a new shell or restart); the troubleshooting page says Docker injection does not have this preload limitation, but Docker SSI still only applies when a container is created (recreate containers; `docker stop`/`docker start` is not enough).
- **Instrumentation rules** (Linux, Agent 7.73+): **APM > Service Setup > Manage Instrumentation Rules** > Add or Edit Rules > Allow Rule / Block Rule, conditions (attribute + operator `equals`/`not equals`/`prefix`/`contains` + value). Attributes: Operating System, Executable, Executable Full Path, Arguments, Working Directory, Language, Entry Point File. Rules evaluated **in order; first match wins**; set a default (allow/block) for non-matching processes. Deployed via Remote Configuration within 50 seconds, or Export the config file. Bits AI can generate rules.
- **Docker**: on the Docker host run `DD_APM_INSTRUMENTATION_ENABLED=docker DD_NO_AGENT_INSTALL=true bash -c "$(curl ... install_script_agent7.sh)"`, run the Agent container (`DD_APM_ENABLED=true`, `DD_APM_NON_LOCAL_TRAFFIC=true`, `DD_APM_RECEIVER_SOCKET=/var/run/datadog/apm.socket`, mount `/var/run/datadog`), then **recreate** app containers. `docker stop`/`docker start` does NOT instrument (instrumentation applies at container creation). Verify `docker system info --format '{{.DefaultRuntime}}'` = `dd-shim`. One Agent per node. Rootless Docker: set socket in `/etc/datadog-agent/inject/docker_config.yaml`.
- **Kubernetes**: requirements Kubernetes v1.20+, Helm, kubectl, Datadog Admission Controller enabled, Linux nodes only. Enable with `apm.instrumentation.enabled: true` (Operator: `spec.features.apm.instrumentation.enabled: true` in `datadog-agent.yaml`; Helm: `datadog.apm.instrumentation.enabled: true` in `datadog-values.yaml`), then restart apps. By default instruments all services in all namespaces, **except the namespace where the Agent is installed** (install the Agent in its own namespace).
  - Verify: app pod init containers `datadog-init-apm-inject` and `datadog-lib-<language>-init`.
  - Targeting (Agent v7.64+): `targets` list, each with `name` (metadata only), `namespaceSelector` (`matchNames`/`matchLabels`/`matchExpressions`), `podSelector` (`matchLabels`/`matchExpressions`), `ddTraceVersions` (SDK version per language, e.g. `java: "default"`, `python: "3.1.0"`), `ddTraceConfigs` (env vars such as `DD_PROFILING_ENABLED`, UST overrides). Targets evaluated in order; first match takes precedence. Also `enabledNamespaces` / `disabledNamespaces`.
  - USTs: recommended automatic label extraction with `kubernetesResourcesLabelsAsTags` (Agent 7.69, Operator 1.16.0, Helm chart 3.120.0) - NOT compatible with Remote Configuration (then use `ddTraceConfigs`).
  - Injection modes: `auto` (default, Agent 7.76.0+), `init_container`, `csi` (Datadog CSI driver; faster pod startup).
  - Opt a pod out: label `admission.datadoghq.com/enabled: "false"` on the **pod template** (`spec.template.metadata.labels`), apply, restart (also disables other mutating webhooks; the documented alternative for Agent versions without instrumentation rules); or DatadogInstrumentation (DDI) resource `spec.config.apm.enabled: false`. Cluster-wide off: `instrumentation.enabled: false`.
- **Windows**: IIS install with `DD_APM_INSTRUMENTATION_ENABLED=iis` (+ `DD_APM_INSTRUMENTATION_LIBRARIES=dotnet:3`), Agent 7.67.1+, .NET SDK 3.19.0+. Chocolatey install cannot enable SSI. Restart IIS apps (not whole server).
- SDK-dependent products after SSI (env vars, `true`/`false`): `DD_RUNTIME_METRICS_ENABLED`, `DD_LOGS_INJECTION`, `DD_PROFILING_ENABLED` (also `auto` = only eligible processes, recommended for SSI), `DD_DATA_STREAMS_ENABLED`, `DD_APPSEC_ENABLED`, `DD_IAST_ENABLED`, `DD_DYNAMIC_INSTRUMENTATION_ENABLED`, `DD_DATA_JOBS_ENABLED`, `DD_APPSEC_SCA_ENABLED`. Host-wide: `application_monitoring.yaml`.
- SSI adds a small amount of startup time.

Sources: https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/linux/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/docker/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/windows/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/compatibility/

### How SSI works: the injector, and SSI pitfalls
- The injector is a shared library loaded at runtime.
  - Linux: `LD_PRELOAD` (env var) or system-wide `/etc/ld.so.preload`.
  - Docker: same `LD_PRELOAD` via a custom `runc` shim that replaces Docker's default runtime (`dd-shim`).
  - Kubernetes: Datadog Admission Controller (mutating admission webhook) mutates the pod spec: init containers or CSI driver deliver injector + SDK, sets env vars (`LD_PRELOAD`), mounts volumes.
  - Windows: injector DLL loaded by a Datadog kernel driver.
- Injector detects runtime, evaluates rules/deny list, sets env vars/args to load the SDK, emits telemetry; finishes before the app's `main` (not a background process). Uses no kernel modules/eBPF; runs with the app's privileges.
- Per-runtime: Java `JAVA_TOOL_OPTIONS` with `-javaagent:...`; Python `PYTHONPATH`; Node.js `NODE_OPTIONS` with `--require`/`--import`; Ruby `RUBYOPT -r`; .NET `CORECLR_ENABLE_PROFILING`/`CORECLR_PROFILER`/`CORECLR_PROFILER_PATH`; PHP `PHP_INI_SCAN_DIR`; NGINX re-exec with `load_module`.
- **`DD_TRACE_ENABLED=false` does not stop SSI** (the injector runs before the SDK reads its env vars). Use platform removal steps or instrumentation rules.
- Java: SSI does not inject into apps that already use `-javaagent`. .NET: CLR allows one profiler per process; a pre-existing profiler (`CORECLR_*`) wins and no Datadog traces arrive. PHP: SSI auto-disables with JIT, Xdebug, ionCube, NewRelic, Blackfire, pcov; force with `DD_INJECT_FORCE=true`. Ruby: SSI modifies the `Gemfile`; back it up before uninstalling. Python: preforking WSGI servers (uWSGI prefork, gunicorn `--preload`) can SIGSEGV; mitigate by lazy loading or manual `ddtrace-run`.
- Internal default deny list (IDEs, databases, etc.).
- Custom instrumentation with SSI still requires importing the SDK; .NET `DD_TRACE_METHODS` still available.
- Troubleshooting: Fleet Automation shows process-level and K8s cluster SSI insights; injector debug logs.

Sources: https://docs.datadoghq.com/tracing/guide/injectors/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting/

### Code-based custom instrumentation (Datadog API, OpenTelemetry API, OpenTracing)
- Purpose: monitor in-house code or complex functions not captured by automatic instrumentation; embed tracing code to programmatically create, modify, or delete traces; add span tags; remove unwanted spans.
- Prereq: Agent installed and configured.
- Three API choices (tabs on the docs page):
  1. **OpenTelemetry API (Recommended)**: Datadog SDKs implement the OTel API -> vendor-neutral code + Datadog native implementation/features. Languages: Java, Python, Ruby, Go, Node.js, PHP, .NET, iOS, Android, Rust, Elixir.
  2. **Datadog API**: Java, Python, Ruby, Go, Node.js, PHP, C++, .NET, Android.
  3. **OpenTracing (Legacy)**: Java, Python, Node.js, Ruby, .NET, PHP, Android. OpenTracing is **archived and unsupported**; use only if OTel or ddtrace custom instrumentation does not work.
- Server-side (backend services) vs **client-side** custom instrumentation: client-side = mobile apps (Android, iOS). Android uses `dd-sdk-android-trace` + `dd-sdk-android-trace-otel` (2.11.0+), creates `OtelTracerProvider` registered in `GlobalOpenTelemetry`, initialized with a **client token** (never an API key, for security) and a tracking consent (`PENDING` batches but does not send, `GRANTED` sends, `NOT_GRANTED` collects nothing).

Sources: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/, https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/client-side/, https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/client-side/android/

### Datadog API details (Python and Java)
- Python (`from ddtrace import tracer`):
  - Decorator `@tracer.wrap()` (optional name, `service=`, `resource=`): traces the function wherever it is called from.
  - Context manager `with tracer.trace("sandwich.make", resource="...") as span:` for an arbitrary block.
  - Manual: `span = tracer.trace("name")` ... `span.finish()` (must finish yourself).
  - Active span: `tracer.current_span()`; local root span: `tracer.current_root_span()`.
  - Tags: `span.set_tag("num_ingredients", 3)`; global tags on every span: `tracer.set_tags({...})` (or `DD_TAGS`).
  - Errors: exception raised inside an active span is attached automatically; manual `span.error = 1`; on local root: `root_span.set_exc_info(exc_type, exc_val, exc_tb)` (sets error type, marks error, adds traceback).
  - Span links: `span_b.link_span(span_a.context, attributes={...})`.
  - Baggage: `span.context.set_baggage_item(...)`, `get_all_baggage_items()`, `remove_baggage_item()`.
  - `ddtrace-api` package (Preview): stable public API interface only; import from `ddtrace_api`; requires `ddtrace>=3.1` + `ddtrace-run`; avoids multiple copies of `ddtrace` with SSI + custom instrumentation.
- Java (interoperates with `opentracing-api`; `GlobalTracer.get().activeSpan()`):
  - `span.setTag("customer.id", ...)`; global tags `-Ddd.tags=datacenter:njc,key:value`.
  - Errors: `span.setTag(Tags.ERROR, true)` + `span.log(Collections.singletonMap(Fields.ERROR_OBJECT, ex))`, or set `DDTags.ERROR_MSG`, `ERROR_TYPE`, `ERROR_STACK`. Root span: cast to `MutableSpan`, `getLocalRootSpan()`, `setError(true)`.
  - **`dd.trace.methods`** system property (no code change): `-Ddd.trace.methods=store.db.SessionManager[saveSession,loadSession]`; operation name `trace.annotation`, resource `SessionManager.saveSession`.
  - **`@Trace`** annotation (from `dd-trace-api` dependency; works only when `dd-java-agent.jar` is attached): args `operationName` (default: method name), `resourceName` (default: operationName).
- .NET: `DD_TRACE_METHODS`. PHP: `DDTrace\trace_method()` wrapper. Ruby: `Datadog::Tracing.trace('name') do |span| ... end`. Go: v2 tracer recommended (`github.com/DataDog/dd-trace-go/v2`); explicitly pass context.

Sources: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/server-side/, https://ddtrace.readthedocs.io/en/stable/

### Guide: Instrument a custom method
- Goal: deep visibility into business logic by tracing any method, or blocks inside methods; then use the flame graph and monitors.
- Clue: a span (e.g. `http.request POST /charge/`) that takes a long time **without direct child spans** means the request needs further instrumentation.
- Example traces `BackupLedger.write` (method-level span) plus a child span `BackupLedger.persist` per transaction with a custom tag `transaction.id`.
  - Java: `@Trace` on the method; inline block with `GlobalTracer.get()` + `tracer.buildSpan("BackupLedger.persist").startActive(true)` in try-with-resources (otherwise call `scope.close()`).
  - Python: `@tracer.wrap()` on the method; `with tracer.trace('BackupLedger.persist') as span: span.set_tag('transaction.id', ...)`.
  - Java, Python, PHP support method decorators/wrappers + code blocks; Ruby, Go, Node.js, .NET use code blocks.
- The guide uses OpenTracing (deprecated) - concepts still apply; follow OTel custom instrumentation for new code.
- To see results: Software Catalog (Catalog) > service > specific resource > time `The past 15 minutes` > **span summary table** (aggregate span info; spot spans repeating abnormally, e.g. `n+1` DB access) > Traces list > flame graph.

Sources: https://docs.datadoghq.com/tracing/guide/instrument_custom_method/

### Dynamic Instrumentation (DI)
- Add **metrics, spans, and span tags** to running production systems **without restarts or code changes**, including in third-party libraries. Datadog sends the instrumentation config, applied dynamically to the running service. Stop collecting by disabling the instrumentation in Datadog.
- Not supported: Azure App Services, serverless; not on US1-FED/gov sites.
- **Live Debugger vs DI**: same technology, same expression language, some shared config. Live Debugger = investigate a problem; **logpoints** capture log events and variable snapshots, auto-expire when the Debug Session ends. DI = add custom APM instrumentation; dynamic spans, span tags and metrics **remain active until you disable them**. **Dynamic log instrumentations now live in Live Debugger.**
- Requirements: Datadog Agent **7.49.0+**; Unified Service Tagging (`service`, `env`, `version`); **Remote Configuration enabled in the Agent**; recommended Source Code Integration.
  - SDK min (in-app / manual enablement): Java 1.48.0 / 1.34.0 (JDK 8+, no Kotlin coroutines); Python 3.10.0 / 2.2.0; .NET 3.57.0 / 2.54.0; PHP 1.5.0 (no file/line instrumentations).
- Permissions: `debugger_read` (Dynamic Instrumentation Read Configuration); write: `debugger_write` (any env) or `debugger_write_preprod` (pre-prod only).
- Enable in-app (recommended): **Dynamic Instrumentation Settings page** (enable service+env), or just create an instrumentation (auto-enables). Manually: `DD_DYNAMIC_INSTRUMENTATION_ENABLED=true` (Java also `-Ddd.dynamic.instrumentation.enabled=true`) plus `DD_SERVICE`, `DD_ENV`, `DD_VERSION`, optional `DD_TAGS`. Python in-code: set env var then `import ddtrace.auto`. If APM not enabled: `DD_APM_ENABLED=true`, Agent listening on 8126/TCP.
- Create: Dynamic Instrumentation page > **Create Instrumentation** (or service three-dot menu > Add an instrumentation for this service) > choose service, runtime, environment, version (optional) > location (class+method or file+line; PHP class+method only).
- **Dynamic metric**: type Metric; name prefixed `dynamic.instrumentation.metric.probe.`; types count, gauge, histogram. Count expression optional (default increments by 1 per invocation); gauge (last value) and histogram (distribution) require a metric expression. Metrics auto-enabled on all matching instances, **not rate limited**, run on every invocation.
- **Dynamic span**: type Span; emits a span when a method executes; alternative to code custom spans; exceptions -> span `error` tag.
- **Dynamic span tag**: adds a tag to an existing span: the **active** span or the **service entry** span; name + value expression + optional condition (only added when true); more tags allowed. Note: internal spans are not indexed by default (may not be searchable).
- Sensitive data scrubbing available.
- Expression language (shared): access locals, params, nested fields (`request.headers["Host"]`), comparisons (`<`,`>`,`>=`,`<=`,`==`,`!=`,`instanceof`), logic (`&&`,`||`,`!`/`not()`), `null`. **No method calls**, **no arithmetic** (`i + 1`). Contextual vars: `@return`, `@duration` (ms, method exit), `@exception`, `@it` (collection predicates). Functions: `isDefined`, `len`, `isEmpty`, `substring`, `startsWith`, `endsWith`, `contains`, `matches`, `any`, `all`, `filter`. Metric expressions must evaluate to a number; conditions to a Boolean; span tag values/log templates use braces `{user.name}`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/, https://docs.datadoghq.com/dynamic_instrumentation/expression-language/, https://docs.datadoghq.com/tracing/live_debugger/

### Live Debugger and Remote Configuration (dependencies of DI)
- Live Debugger: logpoints = auto-expiring, non-breaking breakpoints; conditional capture; built-in sensitive data scrubbing. Requires Agent 7.49.0+ (Go: 7.73.0+), UST, Remote Configuration, Agent log collection `logs_enabled: true` (or `apm_config.debugger_logs_enabled_override: true` / `DD_APM_DEBUGGER_LOGS_ENABLED_OVERRIDE=true`). Permissions `live_debugger_read`, `live_debugger_write`, `live_debugger_redaction_write`.
- Remote Configuration for tracing: Agent 7.47.0+; enabled by default in the Agent since 7.47.0 (`remote_configuration.enabled: true`; env `DD_REMOTE_CONFIGURATION_ENABLED`; Helm `datadog.remoteConfiguration.enabled`). Org-level toggle at Organization Settings > Remote Configuration (needs `org_management`); API key needs the Remote Configuration capability (`api_keys_write`). SDK statuses: CONNECTED, UNAUTHORIZED (API key lacks RC), CONNECTION ERROR (Agent can't reach RC endpoints), DISABLED (Agent RC set false), NOT CONNECTED, UNSUPPORTED AGENT, NOT DETECTED (SDK doesn't support RC), UNKNOWN (e.g. Fargate).

Sources: https://docs.datadoghq.com/tracing/live_debugger/, https://docs.datadoghq.com/tracing/guide/remote_config/

### OpenTelemetry with Datadog
- Two key decisions: **how to instrument** and **how to send data**. OTel API + Datadog SDK gives more Datadog features than OTel SDK alone.
- Instrument options:
  - **Full OpenTelemetry**: OTel SDK + API (vendor-neutral; some Datadog features unsupported).
  - **OpenTelemetry API + Datadog SDK**: set `DD_TRACE_OTEL_ENABLED=true` (Java also `dd.trace.otel.enabled`; not needed for Go and Ruby). Depend on OTel API only (not the OTel SDK) in Java. Node.js: `tracer.init()` then `new tracer.TracerProvider().register()`. Go: `ddotel.NewTracerProvider()` + `otel.SetTracerProvider(provider)`. OTel spans merge with Datadog spans into one trace. SDK-specific operations (SpanProcessors, OTLP trace exporters) not supported. Datadog SDK can also export OTLP.
  - **OTel instrumentation libraries + Datadog SDK**: cover frameworks Datadog SDK lacks; `DD_TRACE_OTEL_ENABLED=true`; disable the Datadog integration to avoid duplicate spans. Min Traces API versions: Java 1.35.0, Python 2.10.0, Ruby 2.1.0, Go 1.67.0, Node.js 4.3.0, PHP 0.94.0, .NET 2.53.0.
- Python OTel API: `trace.get_tracer(__name__)`, `with tracer.start_as_current_span("op")`, `trace.get_current_span()`, `set_attribute()`, `add_event()` (ddtrace 2.9.0+), `record_exception()`. Java OTel: `Span.current().setAttribute(...)`, `setStatus(ERROR, ...)`.
- Send options:
  1. **Datadog Agent with DDOT Collector (Recommended)**: DDOT (Datadog Distribution of OTel Collector) embedded in the Agent; gives Fleet Automation, Live Container Monitoring, Kubernetes Explorer, Live Processes, CNM, USM, 1,000+ integrations; automatic UST enrichment.
  2. **Upstream OpenTelemetry Collector** (Contrib): manage your own; tail-based sampling and transformations. Current recommended config: OTLP HTTP exporter to Datadog OTLP intake + **span metrics connector** (RED metrics powering Catalog and Service Page) + resource detection processor + Datadog extension (reports config to Fleet Automation, exports no telemetry). Legacy Datadog Exporter + Datadog Connector still documented. Not for ECS Fargate/EKS Fargate/Lambda. Tail sampling across multiple Collectors needs a gateway.
  3. **OTLP Ingest in the Agent**: OTel SDK -> Agent over OTLP. Traces and metrics since Agent 6.32.0/7.32.0; logs since 6.48.0/7.48.0. Off by default. gRPC **4317**, HTTP **4318**. `datadog.yaml`: `otlp_config.receiver.protocols.grpc.endpoint: 0.0.0.0:4317` / `http.endpoint: 0.0.0.0:4318`. Env: `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_GRPC_ENDPOINT`, `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_HTTP_ENDPOINT` (set on both core Agent and trace Agent; use `0.0.0.0` in containers). Metrics and traces on by default once enabled; logs off (`otlp_config.logs.enabled: false`) to avoid unexpected log billing. Agent must be on the same host as the OTel app/collector. OTel SDK data can't use App and API Protection, Continuous Profiler, Ingestion Rules.
  4. **Direct OTLP ingest** (agentless): when an Agent/Collector is not feasible (serverless, managed platforms like Cloudflare/Vercel/Heroku, strict resource limits). Not recommended for production workloads in general. Payload limits: metrics `/v1/metrics` 512 KiB compressed; logs `/v1/logs` 5.1 MiB uncompressed; traces `/v1/traces` 15 MiB uncompressed; over limit = HTTP 413.
- Feature compatibility: Continuous Profiler, App and API Protection, Data Jobs Monitoring, RUM (full), Data Streams Monitoring: **Datadog SDK + DDOT only**. DBM, CNM, Live Containers, Live Processes, USM: Datadog SDK + DDOT and OTel SDK + DDOT. Distributed tracing, trace metrics, runtime metrics, span links, correlated telemetry: all setups (direct OTLP trace metrics computed from sampled spans).
- Best practices: avoid mixing a Datadog SDK and an OTel SDK in the same app (undefined behavior; exception: Python needs both installed); do not run the Datadog Agent and a separate OTel Collector on the same host.
- Runtime metrics: Datadog SDK via DogStatsD (UDP 8125); OTel SDK via OTLP (4317/4318).

Sources: https://docs.datadoghq.com/opentelemetry/, https://docs.datadoghq.com/opentelemetry/instrument/, https://docs.datadoghq.com/opentelemetry/instrument/api_support/, https://docs.datadoghq.com/opentelemetry/instrument/dd_sdks/instrumentation_libraries/, https://docs.datadoghq.com/opentelemetry/setup/, https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent/, https://docs.datadoghq.com/opentelemetry/setup/collector_exporter/, https://docs.datadoghq.com/opentelemetry/setup/ddot_collector/, https://docs.datadoghq.com/opentelemetry/setup/agentless/, https://docs.datadoghq.com/opentelemetry/compatibility/

### Common pitfalls (quick list)
- Restarting a Docker container with stop/start does not apply SSI; recreate it.
- Apps in the Agent's own Kubernetes namespace are never instrumented by SSI.
- `DD_TRACE_ENABLED=false` does not disable SSI.
- Java: `-javaagent` must precede `-jar`; SSI skips apps already using `-javaagent`.
- DI with Remote Configuration disabled in the Agent = no instrumentation delivered.
- DI expressions cannot call methods or do arithmetic.
- Dynamic metrics are not rate limited (run on every invocation).
- Using an OTel instrumentation library alongside the matching Datadog integration creates duplicate spans.
- Mobile tracing must use a client token, not an API key.
- OpenTracing is archived; new custom instrumentation should use the OTel API (recommended) or Datadog API.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/troubleshooting/, https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/, https://docs.datadoghq.com/opentelemetry/compatibility/

## Datadog Agent Architecture

### The Agent's role in APM and its processes
- Pipeline: Datadog SDK (tracer) in the app -> **Datadog Agent** (trace-agent / "APM Agent") on the same host/node -> Datadog backend (APM intake) -> UI. The docs assume an Agent "installed and configured to receive traces" before you add an SDK.
- Agent 6/7 = a **main process** (infrastructure metrics, logs, DogStatsD; components: **Collector** runs checks every 15 s, **Forwarder** sends payloads over HTTPS) plus optional processes spawned if enabled in `datadog.yaml`:
  - **APM Agent** (trace-agent): collects traces. **Enabled by default.**
  - **Process Agent**: live processes (by default only collects containers).
  - **Agent Data Plane** (Preview): takes over DogStatsD; disabled by default.
- Windows service names: `DatadogAgent`, `datadog-trace-agent`, `datadog-process-agent`.
- In Kubernetes (Agent 7.19+, Helm/DaemonSet) the Agent pod has **dedicated containers**: `agent` (Agent + Log Agent), `process-agent`, **`trace-agent`**, `system-probe`.
- What the trace-agent does: receives spans from SDKs (HTTP/TCP 8126 or UDS), computes trace metrics/stats, applies **Agent-side sampling** (sends sampling rates back to SDKs, error and rare samplers), **obfuscation** and tag replacement, **filtering** (ignore resources, filter tags), enforces rate limits (connections, memory, CPU), and ships traces + stats to the intake over HTTPS 443.
- Agent CPU is correlated with **spans received per second**; it buffers unprocessed payloads in memory, so CPU throttling can lead to out-of-memory.

Sources: https://docs.datadoghq.com/agent/architecture/, https://docs.datadoghq.com/tracing/trace_collection/, https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/, https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_resource_usage/

### Enabling APM in datadog.yaml (`apm_config`)
- Main config file: `datadog.yaml` - Linux/AIX `/etc/datadog-agent/datadog.yaml`, macOS `/opt/datadog-agent/etc/datadog.yaml`, Windows `%ProgramData%\Datadog\datadog.yaml`.
- "By default, the Datadog Agent is configured to receive traces in your `datadog.yaml` file under **`apm_config`** with `enabled: true` and listens for trace data at `http://localhost:8126`."
- Env var equivalent: `DD_APM_ENABLED` - default `true` (K8s table: Agent 7.18+; Docker page: Trace Agent enabled by default since Agent 6.0.0). Re-enable in the Docker Agent with `-e DD_APM_ENABLED=true`.
- Containers: set `apm_non_local_traffic: true` in `apm_config` (env `DD_APM_NON_LOCAL_TRAFFIC=true`) so the Agent accepts traces from other containers / non-local interfaces.
- Env var naming: config options in capital snake case with `DD_` prefix; most APM keys use `DD_APM_*` (for example `apm_config.receiver_port` -> `DD_APM_RECEIVER_PORT`).
- Example:
```yaml
apm_config:
  enabled: true
  receiver_port: 8126          # 0 disables the HTTP receiver
  apm_non_local_traffic: true  # containers
  target_traces_per_second: 10
  errors_per_second: 10
  connection_limit: 2000
  max_memory: 500000000
  max_cpu_percent: 50
```
- `DD_SITE` must be set on the Agent (default `datadoghq.com`) so traces go to the right site.
- **Agent 7.80.0+ on Linux: socket activation** - the trace-agent **starts only after receiving trace data** (reduces memory). So `agent status` can show APM "Not running or unreachable on localhost:8126" even though APM is correctly configured and no traces have been sent yet. Disable with `apm_config.socket_activation.enabled: false` or `DD_APM_SOCKET_ACTIVATION_ENABLED=false`.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/agent/configuration/agent-configuration-files/, https://docs.datadoghq.com/containers/docker/apm/, https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/

### Ports, protocols and network traffic
- **Inbound (local)**: APM receiver **8126/TCP** - "Includes Tracing and the Profiler". DogStatsD **8125/UDP** (127.0.0.1 unless `dogstatsd_non_local_traffic: true`). go_expvar server (APM) **5012/TCP** (trace-agent debug endpoints; `DD_APM_DEBUG_PORT`, `0` disables). go_expvar integration server 5000, IPC API 5001 (`cmd_port`), GUI 5002 (Windows/macOS default; Linux `-1` = off), Process Agent 6062/6162.
- **OTLP receiver** (when enabled): **4317** gRPC, **4318** HTTP.
- **Outbound**: Agent -> Datadog over SSL/TLS, **443/TCP** ("Most Agent data uses port 443", APM included). Traffic is **always initiated by the Agent**; Datadog never opens sessions back to the Agent.
- **APM destinations**: `trace.agent.<SITE>` (for example `https://trace.agent.datadoghq.com`) and `instrumentation-telemetry-intake.<SITE>`. Profiling: `intake.profile.<SITE>`. Remote Configuration: `config.<SITE>`. Metrics: `<VERSION>-app.agent.<SITE>` (allow `*.agent.<SITE>`). Flares: `<VERSION>-flare.agent.<SITE>`.
- Static IPs: `https://ip-ranges.<SITE>` (JSON; `apm` section = IPs that receive APM data; `/apm.json`). Domains are CNAMEs to static IPs; allowlist the whole set.
- Agent 7.67.0+ uses FQDN with a trailing dot (for example `trace.agent.datadoghq.com.`); disable in 7.72.0+ with `convert_dd_site_fqdn.enabled: false` / `DD_CONVERT_DD_SITE_FQDN_ENABLED=false`.
- Changing ports: `receiver_port` (Trace Collection Configuration section) / `DD_APM_RECEIVER_PORT`; `dogstatsd_port` / `DD_DOGSTATSD_PORT`. If you change the APM receiver port on the Agent you **must also change the SDK** (`DD_TRACE_AGENT_PORT` or `DD_TRACE_AGENT_URL`).
- `DD_APM_DD_URL`: APM endpoint (default `https://trace.agent.datadoghq.com`), also used to point APM at a proxy as `<ENDPOINT>:<PORT>` (proxy must handle TCP). `DD_PROXY_HTTPS`: general proxy URL.
- Security warning: make the Agent reachable only by your apps/trusted sources (firewall); untrusted access lets attackers write traces/metrics into your account or read config.

Sources: https://docs.datadoghq.com/agent/configuration/network/, https://docs.datadoghq.com/agent/architecture/, https://docs.datadoghq.com/containers/kubernetes/apm/

### How SDKs find the Agent (DD_AGENT_HOST, DD_TRACE_AGENT_URL, UDS)
- Default: the SDK tries the Unix domain socket **`/var/run/datadog/apm.socket`**; if it does not exist, it sends to **`http://localhost:8126`**. Stats/DogStatsD: `/var/run/datadog/dsd.socket`, else `localhost:8125`.
- `DD_TRACE_AGENT_URL` (for example `http://custom-hostname:1234` or `unix:///var/run/datadog/apm.socket`) - HTTP or UDS; **has priority** over host/port settings; `DD_AGENT_HOST` is ignored when it is set.
- `DD_AGENT_HOST` - Agent host for traces (and DogStatsD); `DD_TRACE_AGENT_PORT` - default `8126`. Java system properties `-Ddd.agent.host`, `-Ddd.agent.port`.
- Python fallback chain (ddtrace config docs): `DD_TRACE_AGENT_URL` > `DD_TRACE_AGENT_HOSTNAME` > `DD_AGENT_HOST` > UDS `/var/run/datadog/apm.socket` > `localhost`.
- Agent side: `DD_APM_RECEIVER_SOCKET` (UDS path; off by default; if set it takes priority over host/port and must point to a valid socket file). `DD_BIND_HOST` (default `localhost`) - host to listen on for DogStatsD and traces (Docker APM page; the docs do not say how it interacts with `apm_non_local_traffic`, so do not quiz that).
- Python trace API: `DD_TRACE_API_VERSION` defaults to `v0.5` (v0.4 on Windows, in GCP or Azure Functions, or when ASM, IAST or AI Guard is enabled); `v0.3` no longer supported.

Sources: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://docs.datadoghq.com/containers/docker/apm/

### Docker setups
- From the host only: `docker run ... -p 127.0.0.1:8126:8126/tcp ...`. From any host: `-p 8126:8126/tcp`.
- From other containers (Docker network): `docker network create <NETWORK_NAME>`; run the Agent with `--name datadog-agent --network <NETWORK_NAME> -e DD_APM_ENABLED=true -e DD_APM_NON_LOCAL_TRAFFIC=true`; run the app on the same network with `-e DD_AGENT_HOST=datadog-agent` (container name; port 8126 is the default so `DD_TRACE_AGENT_PORT` is optional). With docker-compose, the network is the one under `networks`.
- Docker host IP: link Agent port 8126 to the host and point the tracer to the container's default route (from `ip route`, typically `172.17.0.1`).
- UDS: mount `/var/run/datadog/` into both containers; Agent `DD_APM_RECEIVER_SOCKET=/var/run/datadog/apm.socket`; app `DD_TRACE_AGENT_URL=unix:///var/run/datadog/apm.socket`.
- Commands work the same with `nerdctl` (containerd) or `podman`. Image: `registry.datadoghq.com/agent`.
- Other Docker Agent APM env vars: `DD_APM_CONNECTION_LIMIT` (2000 per 30 s), `DD_APM_IGNORE_RESOURCES`, `DD_APM_FILTER_TAGS_REQUIRE` / `_REJECT` (+ `_REGEX_` variants in 7.49+), `DD_APM_REPLACE_TAGS`, `DD_HOSTNAME`, `DD_LOG_LEVEL` (default `info`; `trace|debug|info|warn|error|critical|off`). Full list: `apm_config` section of `datadog-agent_linux.yaml.example`.

Sources: https://docs.datadoghq.com/containers/docker/apm/

### Kubernetes setups (UDS, hostPort, service, Admission Controller)
- Three transports: **UDS** (recommended), **TCP** (`<host IP>:8126` via hostPort), **Kubernetes service**. All three can be used at once. Each makes data land on the Agent pod on the **same node** (correct tagging/balancing).
- **Helm**: APM **enabled by default over UDS** (or Windows named pipe): `datadog.apm.socketEnabled: true`, `hostSocketPath: /var/run/datadog/`, `socketPath: /var/run/datadog/apm.socket`. Disable APM with `socketEnabled: false`. TCP: `datadog.apm.portEnabled: true`, `datadog.apm.port: 8126`. Apply: `helm upgrade -f datadog-values.yaml <RELEASE> datadog/datadog`.
- **Operator** (`DatadogAgent` `datadoghq.com/v2alpha1`): `features.apm.enabled: true`; `features.apm.unixDomainSocketConfig.path`; TCP: `features.apm.hostPortConfig.enabled: true`, `hostPort: 8126`. Apply: `kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml`.
- App pods, UDS: `hostPath` volume `/var/run/datadog/` mounted at `/var/run/datadog` + `DD_TRACE_AGENT_URL=unix:///var/run/datadog/apm.socket`.
- App pods, TCP: `DD_AGENT_HOST` from the downward API `valueFrom.fieldRef.fieldPath: status.hostIP` (requires Agent hostPort / TCP enabled).
- hostPort warning: opens a port on the node - restrict with a firewall. If the network plugin does not support `hostPorts`, add **`hostNetwork: true`** to the Agent pod spec (shares the host network namespace; port conflicts stop the pod from starting).
- Kubernetes service option: for when `hostPath` (UDS) and `hostPort` are unavailable; K8s 1.22+ `internalTrafficPolicy: Local` routes to the Agent pod on the same node; Helm/Operator create this service automatically on 1.22+; needs the APM port enabled.
- Extra trace-agent env vars: Operator `override.nodeAgent.containers.trace-agent.env`; Helm `agents.containers.traceAgent.env`; DaemonSet: container env.
- K8s APM env var table defaults: `DD_APM_ENABLED` true (7.18+), `DD_APM_RECEIVER_PORT` 8126, `DD_APM_NON_LOCAL_TRAFFIC` true (7.18+ per K8s page; the Docker APM page lists its default as `false` and tells you to set it to `true` when tracing from other containers, so do not quiz a single default), `DD_APM_DD_URL` `https://trace.agent.datadoghq.com`, `DD_APM_TARGET_TPS` 10, `DD_APM_ERROR_TPS` 10, `DD_APM_MAX_EPS` 200, `DD_APM_MAX_MEMORY` 500000000, `DD_APM_MAX_CPU_PERCENT` 50, `DD_APM_CONNECTION_LIMIT` 2000, `DD_APM_DEBUG_PORT` 5012, `DD_APM_ENV` sets `env` on traces, `DD_APM_LOG_FILE`.
- **Datadog Admission Controller**: component of the **Cluster Agent** (v7.40+), a `MutatingAdmissionWebhook`. Injects `DD_AGENT_HOST`, `DD_TRACE_AGENT_URL`, `DD_ENTITY_ID`, `DD_EXTERNAL_ENV`, and standard tags (`env`, `service`, `version`) from pod labels (not overwriting existing `DD_ENV`/`DD_SERVICE`/`DD_VERSION`; pod labels > ownerReference labels). Enabled by default with the Operator and with Helm chart v2.35.0+ (`clusterAgent.admissionController.enabled`).
  - Injection rule: pod label `admission.datadoghq.com/enabled: "true"`, or `mutateUnlabelled: true` (`DD_ADMISSION_CONTROLLER_MUTATE_UNLABELLED`). Label `"false"` always opts out. `mutateUnlabelled: false` + no label = no injection.
  - Communication mode: `admission_controller.inject_config.mode` or pod label `admission.datadoghq.com/config.mode`: `hostip` (default; host IP in `DD_AGENT_HOST`), `service` (local-service DNS name in `DD_AGENT_HOST`, K8s 1.22+), `socket` (UDS path in `DD_TRACE_AGENT_URL` + volume; `DD_DOGSTATSD_URL`), `csi` (Datadog CSI volume, Cluster Agent 7.67+). Auto-set to `socket` when APM or DSD socket is enabled (Helm 3.22.0+/Operator 1.1.0+). Pod mode overrides global. Helm `clusterAgent.admissionController.configMode`, Operator `features.admissionController.agentCommunicationMode`.
  - Cluster Agent 7.39+ can also inject SDKs (Single Step Instrumentation / local SDK injection).
- Flare / status for the dedicated trace-agent container: `kubectl exec -it <AGENT_POD> -c trace-agent -- agent flare <CASE_ID> --local`; for status, `exec` into the trace-agent container.

Sources: https://docs.datadoghq.com/containers/kubernetes/apm/, https://docs.datadoghq.com/containers/cluster_agent/admission_controller/, https://docs.datadoghq.com/tracing/guide/setting_up_apm_with_kubernetes_service/, https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/

### Agent-side sampling and filtering
- Head-based sampling **in the Agent is the default** (`ingestion_reason: auto`): the Agent continuously sends sampling rates to SDKs, targeting **10 traces per second per Agent** overall, distributed across services by traffic. `apm_config.target_traces_per_second` / `DD_APM_TARGET_TPS` (default 10). Only applies to Datadog SDKs (not OTel SDKs). Target fluctuates. Services show as `Automatic` on the Ingestion Control page. Any SDK sampling rule overrides the Agent.
- Remote Configuration (Agent 7.42.0+): set the Agent rate from the Ingestion Control page without restarting; remote config beats local env vars and `datadog.yaml`.
- **Error sampler** (`ingestion_reason: error`): up to **10 traces/s per Agent**; `errors_per_second` / `DD_APM_ERROR_TPS` (Agent 7.33+); `0` disables. Local traces only (distributed traces may be incomplete).
- **Rare sampler** (`ingestion_reason: rare`): combinations of `env`, `service`, `name`, `resource`, `error.type`, `http.status` at up to **5 traces/s per Agent**. **Disabled by default since Agent 6/7.41.0**: enable with `apm_config.enable_rare_sampler` / `DD_APM_ENABLE_RARE_SAMPLER=true`. (7.33-7.40: enabled by default, `DD_APM_DISABLE_RARE_SAMPLER`.)
- Error/rare samplers ignore services with SDK sampling rules; to include spans dropped by SDK rules/`manual.drop`: `DD_APM_FEATURES=error_rare_sample_tracer_drop` (7.41+).
- SDK rate limit (`DD_TRACE_RATE_LIMIT`, 100 traces/s per service instance) is an SDK setting, ignored when using the Agent default mechanism.
- Agent filtering (drops traces **and** excludes them from trace metrics; applies to all services sending to that Agent): `apm_config.ignore_resources` / `DD_APM_IGNORE_RESOURCES` (regex on resource name, for example `["(GET|POST) /healthcheck"]`); `apm_config.filter_tags.require` / `.reject` (`DD_APM_FILTER_TAGS_REQUIRE="key1:value1 key2:value2"`, exact match on root span tags, OR logic; regex variants Agent 7.49+). Contrast: sampling rules keep requests in trace metrics.
- `DD_APM_MAX_EPS` (default 200, "maximum number of APM events per second to sample") and `datadog.trace_agent.events.max_eps.*` relate to APM events (the legacy App Analytics model), not to the traces-per-second target.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/, https://docs.datadoghq.com/containers/kubernetes/apm/

### Obfuscation and scrubbing in the Agent
- Resource names: **SQL numeric literals and bind variables obfuscated** (`SELECT data FROM table WHERE key=123 LIMIT 10` -> `SELECT data FROM table WHERE key = ? LIMIT ?`); strings must be in single quotes (double-quoted values are treated as identifiers, not obfuscated); **Redis quantized to command tokens** (`MULTI\nSET k1 v1\nSET k2 v2` -> `MULTI SET SET`).
- `apm_config.obfuscation` defaults: `mongodb` (on), `elasticsearch` (on), `redis` (on; `remove_all_args` off), `memcached` (on), `http` (**off**: `remove_query_string`, `remove_paths_with_digits`), `remove_stack_traces` (**off**), `credit_cards` (**on**; `luhn: false` by default, enabling Luhn costs CPU; `keep_values`). Env vars: `DD_APM_OBFUSCATION_<TYPE>_ENABLED`, `DD_APM_OBFUSCATION_HTTP_REMOVE_QUERY_STRING`, `DD_APM_OBFUSCATION_REMOVE_STACK_TRACES`, `DD_APM_OBFUSCATION_CREDIT_CARDS_LUHN`. `keep_values` = keys excluded from obfuscation; `obfuscate_sql_values` = keys included.
- Credit card scan: value must be exactly a card number (internal spaces allowed): `4111 1111 1111 1111` -> `?`, `CC-4111 1111 1111 1111` not redacted.
- Lambda Extension uses `DD_APM_CONFIG_OBFUSCATION_HTTP_REMOVE_QUERY_STRING` / `..._REMOVE_PATHS_WITH_DIGITS`.
- `replace_tags` / `DD_APM_REPLACE_TAGS`: list of `name` (`*` = all tags, `resource.name` = resource), `pattern` (regex), `repl`.
- Agent telemetry off: `apm_config.telemetry.enabled: false` / `DD_APM_TELEMETRY_ENABLED=false`.
- Metric: `datadog.trace_agent.obfuscation.sql_cache.hits` / `.misses`.

Sources: https://docs.datadoghq.com/tracing/configure_data_security/

### Agent rate limits and resource usage
- **Connection limit**: default **2000** connections per 30 s window. Log: `http.Server: http: Accept error: request has been rate-limited; retrying in 80ms`. Raise `apm_config.connection_limit` / `DD_APM_CONNECTION_LIMIT`.
- **Memory**: `apm_config.max_memory` / `DD_APM_MAX_MEMORY` (default 500000000 bytes, if surpassed the API rate limits requests). At **150% of max_memory** the trace-agent kills itself (`Killing process. Memory threshold exceeded` ... `OOM`; metric `datadog.trace_agent.receiver.oom_kill`). Set `0` (Agent 7.23.0+) to let the orchestrator manage memory.
- **CPU**: `max_cpu_percent` / `DD_APM_MAX_CPU_PERCENT` default **50** (= 0.5 core; 100 = 1 core) in non-Kubernetes environments; when reached, payloads are refused until CPU drops (`datadog.trace_agent.receiver.ratelimit`; `Limited Resource` warning in the Ingestion Control Service Table View). Set `0` (7.23.0+) to let the orchestrator manage it.
- Sizing: use `datadog.trace_agent.receiver.spans_received` (spans/s). Benchmarks (Agent 7.39.0, c5.2xlarge): 2,000 spans/s ~0.05 core/35 MB; 11,000 ~0.2/40; 32,000 ~0.6/60; 58,000 ~1/70; 130,000 ~2/130.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/agent_rate_limits/, https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_resource_usage/

### Agent APM metrics (`datadog.trace_agent.*`)
- Sent by the Agent when APM is enabled; an APM monitoring dashboard JSON can be imported.
- `cpu_percent` (gauge, % of one core: 50 = half a core, 200 = two cores), `heap_alloc`, `heartbeat` (+1 every 10 s), `panic`, `started` (+1 per start), `profile` (reverse proxy for profile endpoints created).
- Receiver: `receiver.spans_received`, `receiver.spans_dropped`, `receiver.spans_filtered`, `receiver.traces_received`, `receiver.trace`, `receiver.traces_filtered` (ignored resources), `receiver.traces_priority`, `receiver.payload_accepted`, `receiver.payload_refused` (rejected because of sampling), `receiver.error` (decode/format errors), `receiver.oom_kill`, `receiver.tcp_connections`, `receiver.traces_bytes`, `receiver.out_chan_fill`, `normalizer.spans_malformed`.
- Writers: `trace_writer.*` (`bytes`, `bytes_uncompressed`, `payloads`, `retries`, `errors`, `dropped`, `dropped_bytes`, `flush_duration`, `queue_fill`, `connection_fill`, `spans`, `traces`, `events`, `encode_ms`, `compress_ms`); `stats_writer.*` (`bytes`, `stats_buckets`, `retries`, `splits`, `errors`, `dropped`, ...). Bytes are counted after gzip unless `_uncompressed`.
- Legacy events: `events.max_eps.current_rate`, `.max_rate` (= `max_events_per_second`), `.reached_max`, `.sample_rate`.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_metrics/

### Agent status and troubleshooting connection errors
- SDK-side: look in tracer startup logs / debug logs (for example Python `DATADOG TRACER DIAGNOSTIC - Agent not reachable at http://localhost:8126`, Go `connect: connection refused`, Java diagnostic `java -jar dd-java-agent.jar sampleTrace -c 1`). Some languages need `DD_TRACE_STARTUP_LOGS=true`.
- Agent-side: `agent status` (Agent 6.20.0/7.20.0+; Linux `sudo datadog-agent status`; Docker `docker exec -it <CONTAINER> agent status`; K8s `kubectl exec -it <POD> -- agent status`, or the trace-agent container). APM section `APM Agent` shows `Status: Running`, `Pid`, `Receiver: 0.0.0.0:8126`, `Endpoints: https://trace.agent.datadoghq.com`, `Receiver (previous minute)`, `Default priority sampling rate: 100.0%`. Failure: `Status: Not running or unreachable on localhost:8126` = APM not configured (or, 7.80+ Linux, not started yet by socket activation).
- Host-based: SDK should send to `localhost:8126`/`127.0.0.1:8126`; if the Agent is not listening, check port conflicts on 8126.
- Containerized: `localhost` is usually wrong (exceptions: **ECS on Fargate and EKS on Fargate** - do not set `DD_AGENT_HOST`). Test from the app container: `curl -X GET http://{agent_ip}:{agent_port}/info`.
- `DD_AGENT_HOST` per setup: ECS on EC2 -> EC2 metadata endpoint (host IP); Elastic Beanstalk single container -> gateway IP (usually `172.17.0.1`); multi-container -> link to Agent container name; Kubernetes/EKS -> UDS, `status.hostIP`, or Admission Controller (check NetworkPolicies when using TCP); Docker -> Agent container name.
- If `agent_url` in startup logs does not match `DD_AGENT_HOST`, check how the web server passes env vars (for example PHP with Apache/Nginx).
- Support needs: environment info, proxy config, config files, startup/debug logs, Agent flare (from the trace-agent container for dedicated containers). `agent diagnose` runs connectivity diagnosis; `agent configcheck` prints loaded configs.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/, https://docs.datadoghq.com/agent/configuration/agent-commands/, https://docs.datadoghq.com/tracing/troubleshooting/

### OTLP ingest in the Agent
- Since Agent 6.32.0/7.32.0 the Agent ingests OTLP traces and metrics over gRPC or HTTP; logs since 6.48.0/7.48.0. **Off by default.**
- `datadog.yaml`: `otlp_config.receiver.protocols.grpc.endpoint: 0.0.0.0:4317` or `...http.endpoint: 0.0.0.0:4318`. When enabled, metrics and traces are on; **logs off by default** (`otlp_config.logs.enabled`, plus `logs_enabled: true`) to avoid unexpected billing.
- Env vars `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_GRPC_ENDPOINT` / `..._HTTP_ENDPOINT` must be passed to **both the core Agent and the trace Agent** processes (DaemonSet: both `agent` and `trace-agent` containers; map hostPort 4317/4318 on the core `agent` container). In containers use `0.0.0.0`, not `localhost`.
- Helm `datadog.otlp.receiver.protocols.grpc.enabled: true`; Operator `features.otlp.receiver.protocols.grpc.enabled: true`.
- App side: `OTEL_EXPORTER_OTLP_ENDPOINT` (for example `http://localhost:4317`; K8s `http://$(HOST_IP):4318` with `HOST_IP` from `status.hostIP`). Some libraries need `/v1/traces` path.
- Supported setup: an ingesting Agent **on every OTel-data-generating host**; you cannot send from one host to an Agent on a different host.
- OTel SDK data cannot be used by some Datadog products (App and API Protection, Continuous Profiler, Ingestion Rules). `DD_APM_TARGET_TPS` does not affect OTel SDKs.
- Known issue (Agent 7.61.0+ in Docker): `failed to register process metrics: process does not exist` - set `HOST_PROC=/proc`, remove `/proc` mount, or `pid: host`.

Sources: https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent/

### Serverless: Datadog Lambda Extension instead of the Agent
- In AWS Lambda there is no host Agent: the **Datadog Lambda Extension** is a lightweight version of the Datadog Agent that runs inside the Lambda execution environment (added as a Lambda layer, or in the image) and submits custom metrics, enhanced metrics, traces and logs **asynchronously** directly to Datadog. Recommended over the **Datadog Forwarder** (which reads CloudWatch Logs) when collecting metrics and traces; Forwarder still needed for other AWS service logs (API Gateway, AppSync, Lambda@Edge).
- Config is via env vars (capital snake case of `datadog.yaml` keys): `DD_API_KEY` / `DD_API_KEY_SECRET_ARN` / `DD_API_KEY_SSM_ARN` (one required), `DD_SITE`, `DD_TRACE_ENABLED` (default true), `DD_APM_ENABLED`, `DD_APM_REPLACE_TAGS`, `DD_APM_IGNORE_RESOURCES`, `DD_SERVERLESS_FLUSH_STRATEGY` (`end` or `periodically,<ms>`).
- Overhead: adds cold-start init time; flush time is counted in `aws.lambda.duration`/`aws.lambda.enhanced.duration` but happens **after** the response is returned. Actual function performance: **`aws.lambda.enhanced.runtime_duration`**; flush overhead: `aws.lambda.post_runtime_extensions_duration` / `aws.lambda.enhanced.post_runtime_duration`. Default flush at end of each invocation; with frequent invocations (> once per minute) batches and flushes periodically. Far-away region: `DD_SERVERLESS_FLUSH_STRATEGY=periodically,60000`.
- Next-generation extension: GA; v67-v87 opt out with `DD_EXTENSION_VERSION: compatibility`; **v88+ only next-gen**. APM tracing supported for Python, Node.js, Go, Java, .NET, Ruby. Lambda Managed Instances supported in v90+ (background flushing, default 30 s).
- OTel in Lambda: `DD_TRACE_OTEL_ENABLED=true` for the OTel API via Datadog SDK; any OTel SDK can export to the extension at `http://localhost:4318/v1/traces` (Preview).

Sources: https://docs.datadoghq.com/serverless/libraries_integrations/extension/, https://docs.datadoghq.com/serverless/guide/extension_motivation/, https://docs.datadoghq.com/serverless/guide/agent_configuration/, https://docs.datadoghq.com/serverless/aws_lambda/opentelemetry/

### Common pitfalls
- Sending to `localhost:8126` from a container when the Agent is in another container/node (except Fargate).
- Agent in a container without `DD_APM_NON_LOCAL_TRAFFIC=true` rejects traffic from other containers.
- Changing `receiver_port` on the Agent without changing `DD_TRACE_AGENT_PORT`/`DD_TRACE_AGENT_URL` in the SDK.
- `DD_TRACE_AGENT_URL` silently overrides `DD_AGENT_HOST`.
- K8s TCP setup without enabling hostPort on the Agent, or a CNI without hostPort support (use `hostNetwork: true`, UDS, or the service).
- Admission Controller with `mutateUnlabelled: false` and no pod label = nothing injected.
- APM env vars for the trace-agent set on the wrong container (must reach the `trace-agent` container).
- OTLP endpoint env var set only on the core Agent container.
- Agent 7.80+ Linux: APM "not running" in `agent status` before first trace is expected (socket activation).

Sources: https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/, https://docs.datadoghq.com/containers/kubernetes/apm/

## Sampling vs Retention

### Ingestion vs retention: the trace pipeline
- Two independent, fully customizable stages: **ingestion** (which traces/spans the SDK + Agent send to Datadog) and **retention / indexing** (which ingested spans are kept and searchable for 15 days).
- Pipeline order: SDK + Agent ingestion mechanisms -> Datadog ingests -> Live Search (all ingested spans, rolling **15 minutes**, no sampling) -> retention filters -> indexed spans (custom filters: **15 days**; Intelligent Retention Filter: **30 days**).
- Other pipeline stages: Processing Pipelines (transform/normalize span attributes after ingestion, not supported on ddog-gov sites), Generate Metrics (from ingested spans), Usage Metrics.
- Retention filters do **not** change what is ingested. To control ingestion use ingestion controls (Agent/SDK settings, Ingestion Control page).
- Ingestion controls do **not** change APM trace metrics (`trace.*`): they are computed on 100% of traffic by the Agent (exception: OpenTelemetry SDK sampling, application-side sampling such as Ruby's, X-Ray sampling).
- Both ingested spans (GB) and indexed spans (count) can affect the bill. APM host includes **150 GB ingested spans** and **1 million indexed spans** per month (Fargate task: 30 GB / 195,000). Overage: $0.10 per GB ingested, $1.70 per million indexed. Default indexed span retention: 15 days.
- Trace Explorer: Live Search is the default view ("Live Search - All ingested data"); switch to indexed data ("Search - Only Indexed Data") with the time selector. Exporting to dashboards and monitors requires retained (indexed) spans.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/, https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/

### Head-based sampling (default) and Agent rates (`ingestion_reason:auto`)
- Default mechanism. Keep/drop decision made at the start of the **root span**, propagated downstream in the request context (e.g. HTTP headers) -> trace kept or dropped as a whole -> complete traces.
- Rates can be set at the **Agent** level (default) or in the **SDK** (SDK settings override the Agent).
- Agent continuously sends sampling rates to SDKs, targeting **10 traces per second per Agent** overall, split across services by traffic (e.g. A gets 7 tps, B gets 3 tps). Low-traffic apps get 100%. It is a target averaged over time, not a hard limit; spikes can exceed it.
- Config: `target_traces_per_second` in `datadog.yaml` (default 10) or env `DD_APM_TARGET_TPS` (default 10). Changing it impacts sampling rates for **all services** reporting to that Agent.
- Only affects Datadog SDKs; no effect on OpenTelemetry SDKs (even through OTLP ingest in the Agent).
- Remote Configuration of Agent sampling (target TPS, error, rare) needs Agent **7.42.0+**; no Agent restart; remote settings take precedence over env vars and `datadog.yaml`.
- Services using this mechanism are labeled `Automatic` (ingestion mechanisms page) / `APM Agent` (Ingestion Control service table) / `AUTOMATIC` (per-resource table) in the Configuration column.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://docs.datadoghq.com/tracing/guide/ingestion_sampling_use_cases/

### User-defined sampling rules in SDKs (`ingestion_reason:rule`)
- Set a sampling rate applied at the root of the trace by service and/or resource (overrides Agent default). Still head-based: no incomplete traces.
- `DD_TRACE_SAMPLING_RULES` - JSON array, evaluated in order (first match). Example: `[{"service": "my-service", "resource": "GET /checkout", "sample_rate": 1},{"service": "my-service", "sample_rate": 0.2}]` = 100% of GET /checkout, 20% of other endpoints. Java system property `-Ddd.trace.sampling.rules=...`. Service name is case sensitive.
- Resource-based local rules: Java v1.26.0+, Python v2.8.0+, Go v1.60.0+.
- `DD_TRACE_SAMPLE_RATE` (global rate) is **deprecated** for Java, Python, Go: replace `DD_TRACE_SAMPLE_RATE=0.1` with `DD_TRACE_SAMPLING_RULES='[{"sample_rate":0.1}]'`. Ruby, PHP, .NET, C++, Node.js docs still show `DD_TRACE_SAMPLE_RATE` as the global rate. Node.js in code: `tracer.init({ingestion: {sampler: {sampleRate: 0.1, rules: [...]}}})`.
- **Rate limiter**: `DD_TRACE_RATE_LIMIT` = max traces per second **per service instance**; default **100**. Automatically enabled when you set a percentage via rules; ignored when the Agent default mechanism applies. Excess traces dropped at the root.
- All spans of traces sampled by an SDK rule carry `ingestion_reason:rule`; services marked configured (`CONFIGURED` / `APM Local` / `Configured Local`).
- Error and rare samplers are **ignored** for services with library sampling rules.
- .NET 2.35.0+: per-service `DD_TRACE_SAMPLE_RATE` can be set from the Software Catalog UI with Remote Configuration.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/, https://docs.datadoghq.com/tracing/guide/ingestion_sampling_use_cases/

### Error and rare samplers (Agent)
- Catch traces **not** caught by head-based sampling; keep local traces (spans on the same host) -> distributed traces may be incomplete.
- **Error sampler** (`ingestion_reason:error`): up to **10 traces per second per Agent**. `errors_per_second` / `DD_APM_ERROR_TPS` (default 10), Agent 7.33+. Set to `0` to disable; set arbitrarily high to keep all errors.
- **Rare sampler** (`ingestion_reason:rare`): catches combinations of `env`, `service`, `name`, `resource`, `error.type`, `http.status` at up to **5 traces per second per Agent**. Agent 6/7.41.0+: **disabled by default**; enable with `apm_config.enable_rare_sampler` / `DD_APM_ENABLE_RARE_SAMPLER=true` (default false). Agent 7.33-7.40: enabled by default, disable with `DD_APM_DISABLE_RARE_SAMPLER`.
- By default spans dropped by SDK rules or `manual.drop` are excluded from error/rare samplers; include them (Agent 6/7.41.0+) with `DD_APM_FEATURES=error_rare_sample_tracer_drop` on the trace agent.
- Both remotely configurable with Agent 7.42.0+ (Ingestion Control > Configure Datadog Agent Ingestion, click `Apply`).
- Pitfall: error/rare samplers are ignored for services that have SDK sampling rules.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#error-and-rare-traces, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/

### Force keep / drop (`ingestion_reason:manual`) and single span sampling (`ingestion_reason:single_span`)
- Manual Keep on a span: span and all its children ingested (trace may look incomplete if the span is not the root). Manual Drop: no child span ingested; error and rare samplers ignored for it.
- APIs: Java `span.setTag(DDTags.MANUAL_KEEP, true)` / `MANUAL_DROP`; Python `span.set_tag(MANUAL_KEEP_KEY)` / `MANUAL_DROP_KEY` from `ddtrace.constants`; Ruby `trace.keep!` / `trace.reject!`; Go `ext.ManualKeep` / `ext.ManualDrop`; Node `tags.MANUAL_KEEP`; .NET `Tags.ManualKeep`; C++ `USER_KEEP`/`USER_DROP` priority; Rust uses OTel `sampling.priority`.
- Set Manual Keep **before context propagation**, or the entire trace may not be kept across services. It can still be dropped by Agent/server rules.
- Use cases: force keep critical transactions; force drop health checks.
- **Single span sampling**: `DD_SPAN_SAMPLING_RULES='[{"service": "my-service", "name": "http.request", "sample_rate":1.0, "max_per_second": 50}]'` (by service and operation name; Go 1.60+ also resource and tags). Agent **7.40.0+**. Keeps individual spans without full traces, e.g. so span-based metrics use 100% of traffic.
- Single span rules **cannot drop** spans kept by head-based sampling; they only keep additional spans that head-based sampling dropped.
- Legacy App Analytics is fully deprecated: use single span sampling (individual spans) or head-based sampling (complete traces).

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#force-keep-and-drop, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#single-spans

### Other ingestion reasons
- `rum` (RUM-linked backend traces; browser `traceSampleRate` 0-100, default 100%, browser SDK 4.30.0+; iOS/Flutter/React Native `tracingSamplingRate`; Android `traceSampleRate`).
- `synthetics`, `synthetics-browser` (100% of synthetic HTTP/browser tests generate backend traces by default).
- `lambda`, `xray` (serverless), `appsec` (App and API Protection), `data_jobs` (Spark/Databricks), `otel` (OpenTelemetry), `analytics` (deprecated App Analytics).
- Ingestion reasons glossary defaults: auto = 10 tps/Agent; rule = null; error = 10 tps/Agent (null if rules are defined); rare = 5 tps/Agent (null if rules are defined); manual = null; analytics (deprecated) = null.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#product-ingested-spans, https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control/#ingestion-reasons-glossary

### Ingestion Control page (APM > Ingestion Control)
- Header: Monthly Ingestion (month-to-date, projected end-of-month, allotment), APM Adaptive Sampling (target coverage, services vs limit), Ingestion Over Time (by origin APM / other products / OTel).
- Service table tabs: All services, Managed by APM, Managed by other Datadog products, Managed by OTel. Columns: Type, Name (root and non-root services with data in past 1 hour), Ingested Traces/s, Ingested Bytes/s, **Downstream Bytes/s** (bytes for which the service makes the sampling decision, incl. downstream services; based on `sampling_service`), Traffic Breakdown, Configuration (`APM Agent`, `APM Local`, `APM Remote`, `OTel`, `RUM`, `Synthetics`, `AppSec`, `CI Visibility`, `AWS X-Ray`; `N Configurations` badge), Adaptive Sampling (`Full`, `Partial`, `Compatible`, `Not Compatible`, `Disabled`), Infrastructure (hidden by default, enable in **Options**).
- To reduce global volume, sort by **Downstream Bytes/s**. Toggle **Root services only**.
- **Traffic Breakdown** colors: blue = complete traces ingested; gray = complete traces not retained (Agent automatic rate or sampling rules); orange = dropped by the **SDK rate limiter** (default 100 traces/s; warning icon when >= 25% dropped by rate limiter); red = dropped due to **Agent CPU or RAM limit** (can create incomplete traces; fix by increasing Agent CPU/memory).
- Service Ingestion Summary (click a service): sampling rates by resource (Ingested bytes, Downstream bytes, Configuration `Automatic` / `Local Configured` / `Remote Configured`), Ingestion reasons breakdown, **Top sampling decision makers** (upstream services that decide for a non-root service), Agent and SDK versions. Effective Sampling Rate can show <100% on 1-4 hour windows; expected.
- **Manage Ingestion Rate** -> Datadog adaptive sampling rates, or **Custom sampling rates only** -> **Add new rule** (glob patterns, `*`) -> apply **Remotely** (no redeploy, observe in Live Search, takes effect < 1 minute) or **Locally** (generated config, redeploy).
- **Configure Datadog Agent Ingestion**: head-based target (10 tps/Agent), error sampling (10 tps/Agent), rare sampling (5 tps/Agent, off by default).
- Remote sampling requirements: Agent **7.41.1+**, Remote Configuration enabled, `APM Remote Configuration Write` permission; SDKs Java 1.34.0, Go 1.64.0, Python 2.9.0, Ruby 2.0.0 (2.4.0 in resource-based guide), Node 5.16.0, PHP 1.4.0, .NET 2.53.2, C++ 0.2.2.
- Dashboards: APM Traces Estimated Usage, APM Ingestion Reasons.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/, https://docs.datadoghq.com/tracing/guide/resource_based_sampling/, https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control/

### Sampling rule precedence
1. Remotely configured sampling rules (resource-based sampling from UI)
2. Adaptive sampling rules
3. Locally configured sampling rules (`DD_TRACE_SAMPLING_RULES`)
4. Remotely configured global sampling rate
5. Locally configured global sampling rate (`DD_TRACE_SAMPLE_RATE`)
6. Agent rates (`DD_APM_TARGET_TPS`, local or remote)
- Summary: Tracer settings > Agent settings; Sampling rules > Global sampling rate; Remote > Local.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/#sampling-rules-precedence

### Adaptive sampling
- Pick a **monthly ingested volume target**; Datadog adjusts rates per env/service/resource via Remote Configuration + sampling rules; keeps at least **one trace per service/resource/env every 5 minutes**.
- Requirements: Agent **7.53.0+**, Remote Configuration, `APM Remote Configuration Write` (custom roles also `APM Service Ingest Write`); by default only `Datadog Admin` can modify. Not available on ddog-gov sites. SDK minimums include Java 1.34.0, Go 1.68.0, Python 3.14.2, Ruby 2.0.0, Node 5.16.0, .NET 2.54.0, PHP 1.4.0, C++ 0.2.2, Rust 0.4.0.
- Limits: 800 `service/env` combos for adaptive; 1000 for remote sampling configuration (a pair using both counts once in each).
- Target: **Manage Adaptive Sampling Target** -> "Set target by number of APM hosts" (recommended; % of allotment = 150 GB x APM hosts + 50 GB x traced serverless invocations + 10 GB x Fargate tasks; recomputed every 30 minutes) or "Set target by data volume" (fixed GB/month; must raise when onboarding new services).
- Onboard: Ingestion Control -> service -> Manage Ingestion Rate -> Datadog adaptive sampling rates -> optional explicit resource rates -> Apply. Takes effect in 5-6 minutes; rates recomputed every 10 minutes. Configuration shows `ADAPTIVE REMOTE`.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling/

### Reducing ingestion: playbook
- Services labeled automatic at the top -> lower `DD_APM_TARGET_TPS` (global). Lower `DD_APM_ERROR_TPS`; stop rare sampling (guide still cites `DD_APM_DISABLE_RARE_SAMPLER=true`, but on Agent 7.41.0+ rare sampling is off unless `DD_APM_ENABLE_RARE_SAMPLER=true`).
- Few high-throughput services -> SDK sampling rules (local requires redeploy; remote does not).
- Database/cache spans: databases rarely start traces -> find **Top Sampling Decision Makers** and set rules on the upstream root services (e.g. `web-store` 10%), optionally add `DD_SPAN_SAMPLING_RULES` to keep 100% of `web-store` spans for span-based metrics.
- Effects: RED trace metrics stay 100% accurate; span-based **count** metrics drop; **distribution** metrics (e.g. duration) stay representative; metric monitors on span-based metrics and count-based trace analytics monitors (`type:trace-analytics`) are affected; monitors on `trace.*` metrics are not.
- OpenTelemetry: SDK `TraceIdRatioBased`/`ParentBased`, Collector tail/probabilistic sampling -> APM metrics are sampled unless the `span_metrics` connector (or Datadog Connector) sits before the sampling processor.

Sources: https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control/, https://docs.datadoghq.com/tracing/guide/ingestion_sampling_use_cases/

### Retention filters
- APM > **Retention Filters** page. Columns: Filter Name, Filter Query, Retention Rate (0-100%, uniformly chosen), Spans Indexed (`datadog.estimated_usage.apm.indexed_spans`), Last Updated, Enabled toggle. Permission `apm_retention_filter_write` to create/delete/modify/enable/disable.
- **Order matters**: a span matching an earlier filter is kept or dropped there; lower filters never see it (also not shown in a downstream filter's Edit window).
- Three kinds: Intelligent Retention Filter (always on), Default Retention Filters, Custom Retention Filters (any number, any span tag/attribute).
- **Default filters**: `Error Default` (`status:error`, query and rate configurable, can be disabled; e.g. `status:error, env:production`), `App and API Protection Default`, `Synthetics Default`, `Dynamic Instrumentation Default`.
- Create: **Add Retention Filter** -> Retention Query (Trace Explorer syntax) -> **Span rate** -> optional **Trace rate** -> name -> **Add Filter**. Datadog shows estimated % change in indexed volume. Examples: `@transaction_amount:>100`, `resource_name:"GET /checkout" @duration:>2s env:prod`, `service:delivery-api @version:v2.0`.
- **Span-level** filters index only matching spans (Span Explorer). **Trace-level** (Trace rate set) index all spans of matching traces -> queryable in **Trace Queries** too. Span rate evaluated first, trace rate applied to traces selected by span rate. Trace rate can significantly increase indexed usage. Indirectly indexed spans are not evaluated by trace analytics monitors.
- Indexed span: searchable in Trace Explorer, dashboards, monitors for **15 days**; clicking it shows the complete trace (flame graph) but only indexed spans are searchable.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

### Intelligent Retention Filter
- Always active; composed of **diversity sampling** + **one percent flat sampling**; retains for **30 days**; spans it indexes are **not counted** toward indexed span usage (no bill impact). Trace Queries are based on its data.
- Diversity sampling scans **service entry spans**: at least one span (and trace) per env/service/operation/resource every 15 minutes at most; `p75`, `p90`, `p95` latency spans per combination; representative errors (e.g. 400s, 500s). Not uniform: biased toward errors and high latency.
- 1% flat sampling: traces of 1% of ingested RUM sessions with traces (by `session_id`) + uniform 1% of ingested spans (by `trace_id`). Proportionally representative; low-traffic services may be missing on short time frames.
- Exclude diversity data for proportional analytics: `-retained_by:diversity_sampling`; include it to count unique values (e.g. unique merchants).
- `retained_by` values: `retention_filter` (custom/default filter, no trace rate; not in Trace Queries), `trace_retention_filter` (filter with trace rate), `diversity_sampling`, `flat_sampled` (+ `@retention_reason:rum` or `@retention_reason:trace`).
- Spans indexed by custom filters **and** the Intelligent filter appear by default in Trace Explorer aggregated views (timeseries, toplist, table), dashboards and notebooks (i.e. searchable after 15 minutes).
- Spans indexed by the Intelligent filter are **excluded** from APM trace analytics monitor evaluation -> create a custom retention filter for spans you want to alert on.
- Legacy names: "App Analytics" / "Analyzed Spans" replaced by ingestion controls + retention filters.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#datadog-intelligent-retention-filter, https://docs.datadoghq.com/tracing/guide/leveraging_diversity_sampling/

### Generate metrics from spans and traces
- APM > **Generate Metrics** -> **New Metric** -> name (cannot start with `trace.*`) -> type Spans or Traces -> query (same syntax as Trace Explorer) -> value (`*` to count, or numeric attribute like `@cassandra_row_count` for count/min/max/sum/percentiles) -> group by (no tags by default) -> preview -> **Create Metric**.
- Built from all **ingested** spans regardless of retention filters; dropped spans (sampling/filtering) cannot generate metrics. Stored as **custom metrics** (billed as such) with **15-month** retention. Avoid high-cardinality group-bys (user IDs, request IDs, timestamps).
- After creation only the **stream filter query** and **aggregation groups** can change; to change name or type, create a new metric.
- Trace-based metrics (from Trace Queries) emitted after the trace completes (long traces = delay).
- Trace metrics (`trace.*`) are generated automatically for 100% of traffic; span-based metrics are for extra dimensions.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/

### Usage metrics
- `datadog.estimated_usage.apm.ingested_bytes` (**billed**; ingestion metered by volume; tagged `env`, `service`, `sampling_service`, `ingestion_reason`), `datadog.estimated_usage.apm.ingested_spans`, `datadog.estimated_usage.apm.ingested_traces` (only head-based sampled traces; requests per second), `datadog.estimated_usage.apm.indexed_spans` (**billed**; tagged `env`, `service`).
- `sampling_service` attributes ingested bytes to the service that **makes the sampling decision** (A starts trace and calls B, C -> all bytes `sampling_service:A`).
- Dashboards: **APM Traces Estimated Usage** (global, infra with APM, ingestion by service/env/ingestion_reason, indexing by service/env) and **APM Ingestion Reasons**.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/metrics/

### Legacy App Analytics
- Deprecated. Services with legacy configuration show `Legacy Setup` on the Ingestion Control page -> remove App Analytics options and use Agent/SDK sampling mechanisms; use retention filters to index.
- Legacy options: `DD_TRACE_ANALYTICS_ENABLED=true` (global, web integrations), `DD_<INTEGRATION>_ANALYTICS_ENABLED`, Java `-Ddd.trace.analytics.enabled=true`, Go `tracer.WithAnalytics(true)`, Node `analytics: true`; Python only for ddtrace 3.x or older. Ingestion reason `analytics`.

Sources: https://docs.datadoghq.com/tracing/legacy_app_analytics/, https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control/

### Common pitfalls
- Confusing 15 minutes (Live Search), 15 days (custom-filter indexed spans), 30 days (Intelligent filter), 15 months (generated metrics).
- Retention filters never reduce ingestion; ingestion controls never change `trace.*` metrics.
- `DD_TRACE_RATE_LIMIT` (SDK, per service instance, default 100) vs `DD_APM_TARGET_TPS` (Agent, default 10) vs `DD_APM_ERROR_TPS` (10) vs rare (5).
- Rare sampler is off by default on current Agents.
- Error/rare samplers ignored for services with SDK rules.
- Single span rules only add spans; they never remove head-kept spans.
- Retention filter order: first match wins.
- Intelligent filter data is not billed but is excluded from trace analytics monitors.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

## APM Data Security

### Where sensitive data can be removed (big picture)
- Two remediation points: **at collection** (configure the Datadog SDK/tracer or the Datadog Agent, so data never leaves your infrastructure) and **at ingestion** (Sensitive Data Scanner in the Datadog backend, so data has already left your environment but is redacted before it is indexed and shown in the UI).
- Datadog's tools and policies comply with **PCI v4.0** (the PCI page says **v4.0.1**). Datadog is a *Connected PCI environment*, NOT a cardholder data environment (CDE): it is the customer's responsibility to prevent cardholder data (CHD) from entering Datadog. Recommended tools for PCI: Sensitive Data Scanner, Audit Trail (audit events searchable up to **90 days**), File Integrity Monitoring, Cloud Security.
- Data in motion is protected with **TLS and HSTS**; stored data with encryption, access controls and authentication.
- Trace/span data is generated by SDKs for APM, Continuous Profiler, CI Visibility and App and API Protection (AAP). AAP has its own automatic redaction ("data privacy").
- Names you choose (service names, resource names, tags, dashboard titles, monitor names, CI branch names) are data too: do not put PII in them.
- Personal-data categories the SDKs can collect: Name, Email, Client IP, Credit card numbers (PAN), Database statements (literals / bind variables), Geographic location, URI parameters, URI userinfo, Login ID.
- Per-language defaults worth remembering:
  - Credit card numbers: obfuscated **by the Datadog Agent by default** for every language.
  - Database statements: obfuscated by the SDK in .NET, PHP, Python; in Go "Database statements are obfuscated by the Datadog Agent"; Java does **not collect** DB statements by default (must be enabled).
  - Python: client IP, geographic location and URI parameters are **not collected by default**.
  - Ruby and Go: client IPs not collected by default. Node.js: URI parameters not collected by default. PHP: name and email not collected by default.
  - URI userinfo: passwords within the userinfo of a URL are **not collected** by Datadog.

Sources: https://docs.datadoghq.com/tracing/configure_data_security/, https://docs.datadoghq.com/data_security/, https://docs.datadoghq.com/data_security/pci_compliance/

### Agent: default resource-name obfuscation (SQL, Redis)
- Span `resource` names can contain sensitive data; the Agent obfuscates known cases **before setting the resource name**:
  - **SQL numeric literals and bind variables are obfuscated**: `SELECT data FROM table WHERE key=123 LIMIT 10` -> `SELECT data FROM table WHERE key = ? LIMIT ?`.
  - **SQL literal strings are identified by standard ANSI single quotes (`'`)**. Double-quoted (`"`) values are treated as **identifiers**, not strings, so they are **not obfuscated** (pitfall for SQL dialects that allow double-quoted strings).
  - **Redis queries are quantized by keeping only command tokens**: `MULTI\nSET k1 v1\nSET k2 v2` -> `MULTI SET SET`.
- Database Monitoring Agent: obfuscates all query bind parameters before sending to Datadog (query metrics, samples, explain plans never show them).

Sources: https://docs.datadoghq.com/tracing/configure_data_security/#resource-names, https://docs.datadoghq.com/data_security/

### Agent: trace obfuscation (`apm_config.obfuscation`)
- Configured in `datadog.yaml` under `apm_config:` -> `obfuscation:` or with `DD_APM_OBFUSCATION_*` env vars on the Agent. Several types can be enabled at once. Obfuscation has a performance cost and may hide useful non-sensitive info.
- Metadata that can be obfuscated: MongoDB queries, ElasticSearch request bodies, Redis commands, MemCached commands, HTTP URLs, stack traces, credit card numbers.

| Target | Default | Key / env var | Notes |
|---|---|---|---|
| MongoDB (span type `mongodb`) | **enabled** | `obfuscation.mongodb.enabled` / `DD_APM_OBFUSCATION_MONGODB_ENABLED` | `keep_values` (`DD_APM_OBFUSCATION_MONGODB_KEEP_VALUES`) = keys to **exclude** from obfuscation; `obfuscate_sql_values` (`..._OBFUSCATE_SQL_VALUES`) = keys to include. If unset, all keys obfuscated. |
| ElasticSearch (type `elasticsearch`) | **enabled** | `obfuscation.elasticsearch.enabled` / `DD_APM_OBFUSCATION_ELASTICSEARCH_ENABLED` | same `keep_values` / `obfuscate_sql_values` |
| Redis (type `redis`) | **enabled** | `obfuscation.redis.enabled` / `DD_APM_OBFUSCATION_REDIS_ENABLED` | `remove_all_args` (`DD_APM_OBFUSCATION_REDIS_REMOVE_ALL_ARGS`) replaces **all args with a single `?`**; disabled by default |
| MemCached (type `memcached`) | **enabled** | `obfuscation.memcached.enabled` / `DD_APM_OBFUSCATION_MEMCACHED_ENABLED` | |
| HTTP URLs (types `http`, `web`) | **NOT obfuscated by default** | `obfuscation.http.remove_query_string` / `DD_APM_OBFUSCATION_HTTP_REMOVE_QUERY_STRING`; `obfuscation.http.remove_paths_with_digits` / `DD_APM_OBFUSCATION_HTTP_REMOVE_PATHS_WITH_DIGITS` | act on `http.url`; paths-with-digits replaces any path segment containing a digit with `?`. **Lambda Extension** uses `DD_APM_CONFIG_OBFUSCATION_HTTP_REMOVE_QUERY_STRING` / `DD_APM_CONFIG_OBFUSCATION_HTTP_REMOVE_PATHS_WITH_DIGITS` |
| Stack traces | **disabled** | `obfuscation.remove_stack_traces: true` / `DD_APM_OBFUSCATION_REMOVE_STACK_TRACES=true` | replaces stack traces with `?` |
| Credit cards (all span types, all metadata) | **enabled** | `obfuscation.credit_cards.enabled` / `DD_APM_OBFUSCATION_CREDIT_CARDS_ENABLED` | matches replaced with `?`. `luhn: false` by default; `DD_APM_OBFUSCATION_CREDIT_CARDS_LUHN=true` adds a Luhn checksum to cut false positives (more CPU). `keep_values` / `DD_APM_OBFUSCATION_CREDIT_CARDS_KEEP_VALUES` = known-safe keys to skip |

- Credit card scan matches values that are **exactly** a card number (internal whitespace allowed): `4111 1111 1111 1111` -> `?`, but `CC-4111 1111 1111 1111` is **not** redacted. Pattern-based, so other long numbers can be false positives (fix: Luhn).

```yaml
apm_config:
  obfuscation:
    http:
      remove_query_string: true
      remove_paths_with_digits: true
    redis:
      enabled: true
      remove_all_args: true
    remove_stack_traces: true
    credit_cards:
      enabled: true
      luhn: true
```

Sources: https://docs.datadoghq.com/tracing/configure_data_security/#trace-obfuscation

### Agent: `replace_tags` / `DD_APM_REPLACE_TAGS`
- Scrubs sensitive data in **span tags** (and the resource) using regexes, at the Agent. `datadog.yaml`: `apm_config.replace_tags`; env var `DD_APM_REPLACE_TAGS` (JSON array).
- Each rule: `name` (tag key; `*` = all tags; `resource.name` = the resource), `pattern` (regexp), `repl` (replacement string; can use capture groups like `$1`). Omitting `repl` with pattern `(?s).*` removes the value.

```yaml
apm_config:
  replace_tags:
    - name: "http.url"
      pattern: "token/(.*)"
      repl: "?"
    - name: "resource.name"
      pattern: "(.*)\/$"
      repl: "$1"
    - name: "*"
      pattern: "foo"
      repl: "bar"
    - name: "error.stack"
      pattern: "(?s).*"
    - name: "error.message"
      pattern: "[0-9]{10}"
      repl: "[REDACTED]"
```
- Kubernetes: set `DD_APM_REPLACE_TAGS` for Datadog Operator in `override.nodeAgent.env` (`datadog-agent.yaml`), for Helm in `agents.containers.traceAgent.env` (`datadog-values.yaml`), for manual manifests in the **`trace-agent` container**.
- Docker compose: single-line JSON, e.g. `- DD_APM_REPLACE_TAGS=[{"name":"http.url","pattern":"token/(.*)","repl":"?"}]`.

Sources: https://docs.datadoghq.com/tracing/configure_data_security/#replace-tags

### Agent: ignoring unwanted resources (`ignore_resources`, `filter_tags`) vs sampling
Three approaches (Ignoring Unwanted Resources guide):
1. **Sampling rules** (tracer, `DD_TRACE_SAMPLING_RULES`): request stays in **trace metrics**, but is not ingested. Recommended approach, e.g. `DD_TRACE_SAMPLING_RULES='[{"resource": "GET healthcheck", "sample_rate": 0.0}]'` or by tag `{"tags": {"http.url": "http://.*/healthcheck$"}, "sample_rate": 0.0}`. Sampling decision uses the **first (root) span**; a rule on a tag that is not on the trace root span is not applied.
2. **Filtering in the Agent**: dropped traces are **excluded from trace metrics too**; applies to **all services sending to that Agent**.
3. **Tracer configuration** (per service / app-specific logic): also removes requests from trace metrics; may cause sampling inaccuracy in distributed traces.

`ignore_resources` (Agent):
- Drops traces whose **global root span** resource name matches any of a list of **regular expressions** (Go `regexp` syntax).
- `datadog.yaml`: `apm_config.ignore_resources: ["(GET|POST) /healthcheck","API::NotesController#index"]` (entries in double quotes, comma-separated).
- Env var: `DD_APM_IGNORE_RESOURCES="(GET|POST) /healthcheck,API::NotesController#index"` (comma-separated list) - set on the **Agent container** (in Kubernetes with dedicated containers, the **trace-agent** container).
- Regex must match the **resource name**, not the URL: e.g. resource `Api::HealthchecksController#index` (operation `rack.request`, `http.url` `/api/healthcheck`) -> `Api::HealthchecksController#index$`.
- Docker Compose escapes `$` as `$$` (`Api::HealthchecksController#index$$`). Escaping special characters may be needed depending on deployment.

`filter_tags` (Agent 6.27.0/7.27.0+):
- Drops traces whose **root span** matches span tags. Whole trace dropped; individual spans cannot be selectively dropped.
- `DD_APM_FILTER_TAGS_REQUIRE="key1:value1 key2:value2"`: keep only traces whose root span has an exact match; others dropped.
- `DD_APM_FILTER_TAGS_REJECT="key1:value1 key2:value2"`: drop traces whose root span matches.
- Env var format: **space-separated** `key:value` pairs; `datadog.yaml` uses lists: `apm_config.filter_tags.require: ["db:sql", "db.instance:mysql"]`, `reject: ["outcome:success"]`.
- **Exact string match**; multiple tags use **OR logic** (dropped if root span matches any). For regex: `DD_APM_FILTER_TAGS_REGEX_REQUIRE` / `DD_APM_FILTER_TAGS_REGEX_REJECT` (Agent **7.49+**).
- Backend-generated tags (`http.path_group`, `http.url_details.*`, `http.useragent_details.*`) are created after ingestion and **cannot** be used to filter at the Agent. Since 1 Oct 2022 the backend remaps tags to span tag semantics; to filter at the Agent, use the original "remap from" names (e.g. Python `http.query.string`, not `http.url_details.queryString`; `error.msg`, not `error.message`).
- Tracer-side alternatives: Ruby `Datadog::Tracing::Pipeline::SpanFilter` with `before_flush`; Python `TraceFilter` subclass whose `process_trace` returns `None` to drop, registered with `tracer.configure(trace_processors=[...])`; Node.js `blocklist` on the `http` plugin (server matches path, client matches full URL; configure before importing the module); Java `TraceInterceptor` returning an empty list from `onTraceComplete`.

Sources: https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/, https://docs.datadoghq.com/tracing/configure_data_security/#ignore-resources

### Tracer (SDK) side: query strings, headers, client IP, processing
- `http.url` holds the full URL including the query string. By default the SDK parses the query string and **redacts suspicious-looking values**; matches are replaced with `<redacted>`.
  - `DD_TRACE_OBFUSCATION_QUERY_STRING_REGEXP`: override the redaction regex (platform-specific regex syntax). Python: alias `DD_OBFUSCATION_QUERY_STRING_REGEXP`; setting it to an **empty string disables** obfuscation; the default regex targets keys like `password`/`pwd`/`pass`, `secret`, `api_key`/`access_key`, `token`, `signature`, `auth`/`authorization`, bearer tokens, GitHub tokens (`gh[opsu]_`), JWTs, private keys and SSH keys. (Replaced `DD_TRACE_OBFUSCATION_QUERY_STRING_PATTERN` in ddtrace v1.19.0.)
  - `DD_HTTP_SERVER_TAG_QUERY_STRING=false`: do not collect the query string on **server** spans (default `true`).
  - `DD_TRACE_HTTP_CLIENT_TAG_QUERY_STRING` (alias `DD_HTTP_CLIENT_TAG_QUERY_STRING`), default `true`: query strings and fragments are added to `http.url` on **HTTP client** spans; set `false` to stop.
- **Header tags are opt-in**: `DD_TRACE_HEADER_TAGS` maps **case-insensitive** header names to tag names (matching header values are applied as tags on **root spans**), e.g. `DD_TRACE_HEADER_TAGS=CASE-insensitive-Header:my-tag-name,User-ID:userId,My-Header-And-Tag-Name`. Entries without a tag name are allowed; default tag key is then `http.request.headers.<header>` / `http.response.headers.<header>`. Default value: none (no headers collected). Can also be changed at runtime from the UI (Software Catalog > service > Service Config > SDK & Agent Configurations) with Remote Configuration.
- Client IP: `DD_TRACE_CLIENT_IP_ENABLED` (Python default `false`) collects client IP from request headers into `http.client_ip`; `DD_TRACE_CLIENT_IP_HEADER` names a custom header to read it from.
- Span processing APIs to modify/remove sensitive data in code: Java **TraceInterceptor**, Ruby **Processing Pipeline**, Python **Trace Filtering** (`TraceFilter`).
- AWS Lambda payloads: request/response JSON can be scrubbed (`Obfuscating AWS Lambda payload contents`); Python SDK `DD_TRACE_CLOUD_REQUEST_PAYLOAD_TAGGING` / `DD_TRACE_CLOUD_RESPONSE_PAYLOAD_TAGGING` take JSONPath entries to redact for AWS SDK requests/responses.
- Telemetry: SDK instrumentation telemetry (host, OS, runtime, integrations, dependencies, diagnostic logs, crash dumps with obfuscated stack traces). Disable on the Agent with `apm_config.telemetry.enabled: false` / `DD_APM_TELEMETRY_ENABLED=false`; on the app with `DD_INSTRUMENTATION_TELEMETRY_ENABLED=false` (Datadog says users on the government sites `app.ddog-gov.com` and `us2.ddog-gov.com`, where instrumentation telemetry is unavailable but enabled by default, should set `DD_INSTRUMENTATION_TELEMETRY_ENABLED=false` on the app and `DD_APM_TELEMETRY_ENABLED=false` on the Agent).

Sources: https://docs.datadoghq.com/tracing/configure_data_security/#library, https://docs.datadoghq.com/tracing/trace_collection/library_config/python/, https://ddtrace.readthedocs.io/en/stable/configuration.html, https://docs.datadoghq.com/tracing/trace_collection/runtime_config/

### Sensitive Data Scanner (SDS) for APM spans
- Stream-based pattern matching service to **identify, tag, and optionally redact or hash** sensitive data. Scans logs, **APM spans**, RUM events, Event Management events, Agent Observability (LLM) traces, cloud storage (S3, detect only) and code repositories (Secret Scanning, detect only).
- In the cloud: data **leaves your environment first**, then is scanned during processing and redacted **before indexing / display**. For APM, **span attribute values only** are scanned. To redact before data leaves your premises, use **Observability Pipelines** + the SDS processor (logs).
- Setup: **Scanning group** = query filter (Log Search Syntax) + toggles for Logs / APM / RUM / Events + optional **sampling 10%-99%** per product. New groups are **disabled by default** (toggle on). Up to **20 scanning groups** per org (telemetry). In the group, click **APM Spans** to preview filtered spans.
- **Scanning rules**: library rules from the **Scanning Rule Library** (emails, credit cards, API keys, tokens...) with recommended keywords, or **custom regex rules** (PCRE subset; no lookarounds/backreferences, atomic groups, etc.). Up to **750 rules** per org. Keywords: max **20 per rule**, default must be within **30 characters before** the match; case-insensitive.
- **Action on Match**: scan **Entire Event** (optionally exclude attributes) or **Specific Attributes** (no `@` prefix in attribute paths).
- Actions: **Redact** (replace with a chosen token, e.g. `[sensitive_data]`), **Partially redact**, **Hash** (non-reversible; FarmHash 64-bit fingerprint), **Mask** (logs, APM spans, RUM: users with **`Data Scanner Unmask`** can view the original value; unmask in Findings page, Log/Trace/RUM Explorer; never via API/Terraform/archives). Redact, partial redact and hash are **irreversible**. Mask is not recommended for credentials. Masked data accessed through the API, Terraform or archives always stays obfuscated; unmasking does not work on rehydrated logs. (Doc inconsistency: the rule-setup steps label Mask "available for logs only", but the overview and Mask action section say logs, APM spans and RUM events.)
- When a scanning group uses **sampling**, obfuscating actions (redact/partially redact/hash) **cannot** be selected - you must scan all matching data to obfuscate.
- SDS does **not** scan integer/float/double values (numeric strings are scanned). Rules affect only data ingested **after** the rule is created. SDS does **not** affect rules defined on the Agent.
- Excluded namespaces for spans (never redacted), e.g. `trace_id`, `span_id`, `parent_id`, `resource`, `service`, `env`, `host`, `name`, `operation_name`, `duration`, `meta._dd.*`, `metrics._dd.*`.
- Suppressions (Match exactly / Start with / End with) ignore risk-accepted values (not redacted, not in Findings).
- Tags: Datadog recommends adding `sensitive_data` and `sensitive_data_category` tags; for **APM and RUM**, alert by creating **monitors on those tags** (logs use security notification rules). OOTB dashboard: **Sensitive Data Scanner Overview**. Findings page lists matches by rule/group.
- Permissions (Compliance section): `data_scanner_read`, `data_scanner_write`, `data_scanner_unmask` - all default to **Datadog Admin Role**. UI path: Organization Settings > Sensitive Data Scanner (`/organization-settings/sensitive-data-scanner/configuration`).
- Session Replay masking (on device, permanent) differs from SDS Mask (on ingestion, can be unmasked).

Sources: https://docs.datadoghq.com/security/sensitive_data_scanner/, https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data/

### Live Debugger / Dynamic Instrumentation redaction
- Live Debugger logpoints capture logs and variable snapshots (Capture Variables: rate-limited to **1 execution/second**; without capture **5000/s per instance**). Logs have `source:dd_debugger`.
- Three layers of protection:
  1. **Identifier and type rules** - redact in your infrastructure, **before upload**.
  2. **Redaction modes** - **Strict Mode** (redacts all values **except numbers and Booleans**; Bits Live Debugger not available) and **Targeted Mode** (redacts known sensitive patterns - credit cards, API keys, IPs, other PII - plus a high-entropy secrets scanner shown as `[REDACTED:HIGH_ENTROPY]`). Modes **cannot be disabled, only switched**; Targeted Mode is applied automatically in pre-production envs like `staging`/`preprod`. Changing mode needs **Live Debugger Redaction Write** (`live_debugger_redaction_write`, default Admin).
  3. **Sensitive Data Scanner** rules with filter `source:dd_debugger` - redaction happens **after upload** to Datadog (not a substitute for in-infrastructure rules).
- Default: values tied to sensitive identifiers such as `password` and `accessToken` are redacted **before data leaves the host**; each SDK has built-in language-specific rules.
- Env vars are set **in the application's environment, not on `datadog-agent`**:
  - `DD_DYNAMIC_INSTRUMENTATION_REDACTED_IDENTIFIERS=firstName,lastName,phoneNumber` - add identifiers (applies anywhere: arguments, locals, fields, dict keys).
  - `DD_DYNAMIC_INSTRUMENTATION_REDACTION_EXCLUDED_IDENTIFIERS=cookie,sessionid` - remove identifiers from the default list.
  - `DD_DYNAMIC_INSTRUMENTATION_REDACTED_TYPES=MyCompany.Authentication.UserCredential,MyCompany.BillingAddress` - redact variables of these classes and **prevent probes from being set inside those classes** (Python supports `*` wildcards, e.g. `Secret*`).
- Permissions: `live_debugger_read` (Read Only), `live_debugger_write` (Standard), `live_debugger_redaction_write` (Admin); Dynamic Instrumentation: `debugger_read` (Read Only), `debugger_write` (Admin), `debugger_write_pre_prod` (Standard), **`debugger_capture_variables`** (Admin) for probes that capture local variables, arguments, fields, return values.

Sources: https://docs.datadoghq.com/tracing/live_debugger/sensitive-data-scrubbing/, https://docs.datadoghq.com/tracing/live_debugger/, https://docs.datadoghq.com/account_management/rbac/permissions/

### RBAC for APM data
- Managed roles: **Datadog Admin**, **Datadog Standard**, **Datadog Read Only**. Managed roles get new permissions automatically; custom roles do not unless **Automatic Updates** ("Automatically Receives Permissions") is set. When giving a user a custom role, remove their managed role to enforce it.
- APM permissions (default role): `apm_read` - Read and query APM and Trace Analytics (Read Only); `apm_retention_filter_read` (Read Only) / `apm_retention_filter_write` (Admin); `apm_service_ingest_read` (Read Only) / `apm_service_ingest_write` (Admin); `apm_apdex_manage_write` (Admin); `apm_tag_management_write` - second primary tag (Admin); `apm_primary_operation_write` (Standard); `apm_generate_metrics` - metrics from spans (Standard); `apm_pipelines_read`/`_write`; `apm_remote_configuration_read` (Standard) / `apm_remote_configuration_write` (Admin); `apm_service_renaming_write` (Admin); `continuous_profiler_read` (Read Only).
- Sensitive-data related: `data_scanner_unmask` controls who sees SDS-masked span values; logs RBAC can use SDS tags to restrict access to logs with sensitive data.

Sources: https://docs.datadoghq.com/account_management/rbac/permissions/#apm, https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data/

### Common pitfalls
- HTTP URL query strings are **not** obfuscated by the **Agent** by default (`remove_query_string` is off), but SDKs redact suspicious query-string values by default via the obfuscation regex.
- `ignore_resources` matches the **resource name** of the **root span** with regex; `filter_tags` needs **exact** tag matches (regex only with `_REGEX_` variants, Agent 7.49+); both drop whole traces and remove them from trace metrics. To keep metrics but drop ingestion, use sampling rules (`sample_rate: 0.0`).
- Agent env vars must go on the **trace-agent** container in Kubernetes; DI redaction env vars go on the **application**, not the Agent.
- SDS redaction happens after data leaves your environment; Agent/SDK settings act before.
- Credit card obfuscator only redacts values that are exactly card numbers.
- Double-quoted SQL values are treated as identifiers and not obfuscated.

Sources: https://docs.datadoghq.com/tracing/configure_data_security/, https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/

## Profile Collection

### What the Continuous Profiler is and where data shows up
- The profiler ships **inside the Datadog SDKs** (tracing libraries). If a service already sends traces, you do not install anything new; you only enable profiling. The exception is `ddprof` (C/C++/Rust), a separate native profiler (Preview).
- It finds CPU, memory and I/O bottlenecks broken down by method/class/line number. Java uses technologies such as JDK Flight Recorder to keep overhead low in production.
- Profiles appear "after a couple of minutes" on **APM > Profiles** (in-app link: `app.datadoghq.com/profiling`, named "Datadog APM > Profiler page" in the setup docs). If they do not, follow the language troubleshooting page.
- **Upload cadence**: by default profiles are uploaded **once a minute**; depending on language a process is profiled for 15 to 60 seconds per profile. Data Collection Resolution guide: Profiles and Profile metrics have a **60 second** collection interval and 60 s minimum resolution. Python: `DD_PROFILING_UPLOAD_INTERVAL` default `60.0` seconds.
- **Retention**: flame graphs, call graphs and thread timelines are kept **8 days**; profile metrics **1 month**; a flame graph exported to a **Notebook is kept 1 year**.
- Default search facets on the Profiles page: **Env, Service, Version, Host, Runtime** (for example `JVM`, `CPython`). Profiles from `ddprof` show under the *native* runtime.
- Visualizations: Flame graph (default), Timeline view (Explorer > Visualize as **Thread Timeline**), Timeseries/Table, Call graph, Profile List (single profile; tabs Profiles, Insights, Metrics, Runtime Info, Related Processes).
- Continuous Profiler is **not activated by default** when the SDK/APM is installed: you must explicitly enable it per application (stated explicitly for .NET; `DD_PROFILING_ENABLED` defaults to `false` in Ruby, .NET and Python).

Sources: https://docs.datadoghq.com/profiler/, https://docs.datadoghq.com/profiler/profile_visualizations/, https://docs.datadoghq.com/extend/guide/data-collection-resolution/, https://ddtrace.readthedocs.io/en/stable/configuration.html

### Common requirements (all languages)
- **Datadog Agent v6+** installed and running; **Agent v7+ recommended**.
- If APM is not enabled on the Agent: set `DD_APM_ENABLED=true` and expose port **`8126/TCP`** (the trace Agent port; profiles are sent to the same Agent endpoint as traces). .NET defaults: `DD_AGENT_HOST=localhost`, `DD_TRACE_AGENT_PORT=8126`, `DD_TRACE_AGENT_URL` overrides both.
- **Unified service tags**: set `DD_SERVICE`, `DD_ENV`, `DD_VERSION` (or in-code equivalents). These drive the Profiling UI and correlation with traces. Custom profile tags: `DD_TAGS` comma-separated `<key>:<value>` (for example `layer:api,team:intake`). ddprof: `environment`, `service`, `service_version` are "recommended, as they are used by the Profiling UI".
- .NET defaults if tags are not set: env `unspecified-environment`, version `unspecified-version`, service auto-derived from the entry assembly or process name.
- Optional for every language: **Source Code Integration** to link profiles to Git repositories.
- Serverless: Java, Go, Ruby, PHP, ddprof **not supported** (for example AWS Lambda). Python and Node.js: **Preview** on some serverless platforms such as AWS Lambda; Node.js also Preview on Google Cloud Run. .NET: Azure App Service (Windows and Linux) **Web Apps only**, Function Apps not supported; not supported on AWS Lambda.

Sources: https://docs.datadoghq.com/profiler/enabling/, https://docs.datadoghq.com/profiler/enabling/supported_versions/

### Enabling: which method per language
| Language | Env var `DD_PROFILING_ENABLED` | In-code option | Launcher / notes |
|---|---|---|---|
| Java | yes (`DD_PROFILING_ENABLED=true`) | no; JVM system property `-Ddd.profiling.enabled=true` | `-javaagent:dd-java-agent.jar` must come **before `-jar`** |
| Python | yes, with `ddtrace-run` | `from ddtrace.profiling import Profiler; prof = Profiler(...); prof.start()` | `DD_PROFILING_ENABLED=true ddtrace-run python app.py` |
| Go | only with Orchestrion builds | **required**: `profiler.Start(...)` + `defer profiler.Stop()` | package `github.com/DataDog/dd-trace-go/v2/profiler` |
| Ruby | yes | `Datadog.configure { \|c\| c.profiling.enabled = true }` | start with `bundle exec ddprofrb exec ...` |
| Node.js | yes | `require('dd-trace').init({ profiling: true, ... })` | `node -r dd-trace/init app.js` if `init` not already called |
| .NET | yes (`1`/`true`, `Auto` with SSI, `0`/`false`) | no | CLR profiler env vars (`CORECLR_*` / `COR_*`) or SSI |
| PHP | yes / INI | no | `php datadog-setup.php --enable-profiling --php-bin=all` |
| C/C++/Rust | n/a | C API `ddprof_start_profiling()` (library mode) | wrap the command: `./ddprof myapp --arg1` |
- Key exam idea: **Go is the language that needs code** (`profiler.Start`) unless the app is built with **Orchestrion**, which adds the profiler code; then `DD_PROFILING_ENABLED=true` enables it at runtime.
- `DD_PROFILING_ENABLED` is the standard env var name (not `DD_APM_PROFILING_ENABLED`, not `DD_PROFILER_ENABLED`).

Sources: https://docs.datadoghq.com/profiler/enabling/

### Java
- Download: `wget -O dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'` (or curl / Dockerfile `ADD`).
- Command-line form:
  `java -javaagent:dd-java-agent.jar -Ddd.service=<svc> -Ddd.env=<env> -Ddd.version=<ver> -Ddd.profiling.enabled=true -jar <svc>.jar <flags>`
- Env var form: `export DD_PROFILING_ENABLED=true` (+ `DD_SERVICE`, `DD_ENV`, `DD_VERSION`) then `java -javaagent:dd-java-agent.jar -jar ...`.
- **`-javaagent` must be before `-jar`**: that makes it a JVM option; after `-jar <file>` it is passed to the application as an argument.
- Supported: all JVM languages (Java, Scala, Groovy, Kotlin, Clojure); only actively maintained LTS JDKs and the latest GA release. Linux minimums: OpenJDK 8u352+/11.0.17+/17.0.5+/21+, Oracle 8u351+, OpenJ9 8u372+/11.0.18+/17.0.6+, Azul Platform Prime 23.05.0.0+. Supported-versions table: min runtime JDK 8+, feature complete JDK 11+.
- Linux profile types: CPU, Wallclock (latency), Allocations, Live heap, Exception, I/O. Windows: CPU, Allocations, I/O, Exception (no wallclock, no live heap).
- **Engines**: Datadog Profiler = default on **Linux** (perf-based CPU sampling, wallclock, full set); **JFR** = Windows, macOS, and Linux fallback. Datadog engine default since dd-trace-java v1.7.0 (`DD_PROFILING_DDPROF_ENABLED`). Switch CPU to JFR: `DD_PROFILING_DDPROF_CPU_ENABLED=false`.
- Wallclock: samples all threads on or off CPU with active tracing; enabled by default; Datadog-engine only, not on Windows.
- Allocation (Datadog engine) needs Java 11+, auto-disabled below 11.0.23/17.0.11/21.0.3. JFR allocation enabled by default on JDK 16+, not on 8-15 (overhead).
- Live heap: enabled by default on Linux since v1.61.0; toggle `DD_PROFILING_HEAP_ENABLED` (all live heap) vs `DD_PROFILING_DDPROF_LIVEHEAP_ENABLED` (Datadog engine only). Heap histogram metrics: `DD_PROFILING_HEAP_HISTOGRAM_ENABLED=true` (Java 17.0.9+, not with ZGC).
- GraalVM native image (Preview): GraalVM 17+; set `DD_PROFILING_ENABLED=true` and `DD_PROFILING_DIRECTALLOCATION_ENABLED=true`; only JFR-based; no wallclock or live heap.
- **Overhead tuning**: `-Ddd.profiling.jfr-template-override-file=minimal` (500 ms threshold for ThreadSleep/ThreadPark/JavaMonitorWait vs 100 ms default; disables allocation and exception events) or `=comprehensive` (10 ms threshold, more events, more overhead). Custom `.jfp` override file, e.g. `jdk.InitialSystemProperty#enabled=false` to drop sensitive system properties; overrides applied at JVM startup (restart needed).
- Exceptions overwhelming the profiler: `-Ddd.integration.throwables.enabled=false` (temporarily).
- `/proc/sys/kernel/perf_event_paranoid` = `3` -> no perf events, falls back to **itimer** (degraded CPU profiles); set to `2` or lower.
- Kubernetes pods evicted for disk: profiler writes to ephemeral storage (usually `/tmp`); add a small ephemeral-storage request (~100MB). Temp dir issues: `-Ddd.profiling.tempdir=<writable, exec-enabled dir>`; with SSI put `DD_PROFILING_TEMPDIR` in `application_monitoring.yaml`. v1.47.0+ uses PID-specific subdirectories.
- Missing profiles: turn on debug mode and open a support ticket with OS and runtime details.
- Java 8 vendors need JFR backport: Azul u212 (u262 recommended), AdoptOpenJDK/RedHat/Corretto/Liberica u262, upstream u272.

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=java, https://docs.datadoghq.com/profiler/profiler_troubleshooting/java/

### Python
- `pip install ddtrace` (pip 18+). Enable: `DD_PROFILING_ENABLED=true DD_ENV=prod DD_SERVICE=my-web-app DD_VERSION=1.0.3 ddtrace-run python app.py`.
- Manual lifecycle: `from ddtrace.profiling import Profiler`; `prof = Profiler(env=..., service=..., version=...)`; `prof.start()` **as early as possible, before other imports**. Unset args fall back to `DD_ENV`/`DD_SERVICE`/`DD_VERSION`.
- `os.fork`: profiler automatically restarted in the child on supported Python versions.
- Code provenance (which library runs the code) on by default; disable with `DD_PROFILING_ENABLE_CODE_PROVENANCE=0`.
- ddtrace config: `DD_PROFILING_ENABLED` "Enable Datadog profiling when using ddtrace-run", default False; `DD_PROFILING_UPLOAD_INTERVAL` 60.0 s; `DD_PROFILING_MAX_TIME_USAGE_PCT` 1.0 (CPU budget of stack profiler); `DD_PROFILING_TAGS`; `DD_PROFILING_ENDPOINT_COLLECTION_ENABLED` True; `DD_PROFILING_MAX_FRAMES` 64.
- Alpine (no binary wheel): install build tools first (`gcc musl-dev linux-headers`).
- Missing profiles: debug mode + support ticket; see ddtrace troubleshooting.

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=python, https://docs.datadoghq.com/profiler/profiler_troubleshooting/python/, https://ddtrace.readthedocs.io/en/stable/configuration.html

### Go
- Requires one of the **two latest major Go releases**. `go get github.com/DataDog/dd-trace-go/v2/profiler` (v1 users: migrate to v2).
- Code:
  `err := profiler.Start(profiler.WithService("svc"), profiler.WithEnv("env"), profiler.WithVersion("1.0"), profiler.WithTags("k:v"), profiler.WithProfileTypes(profiler.CPUProfile, profiler.HeapProfile))` then `defer profiler.Stop()`.
- **Default profile types: CPU and Heap only.** `BlockProfile`, `MutexProfile`, `GoroutineProfile` are off by default to keep overhead low; add them via `profiler.WithProfileTypes`.
- Env alternatives for tags: `DD_ENV`, `DD_SERVICE`, `DD_VERSION`, `DD_TAGS`.
- **Orchestrion** auto-instrumentation adds the profiler code; enable at runtime with `DD_PROFILING_ENABLED=true`.
- Trace to Profiling + Endpoint Profiling: `dd-trace-go` 1.51.0+ (enabling page).
- C calls in CPU profiles: optional `ianlancetaylor/cgosymbolizer` (experimental; rare deadlocks).
- PGO (Go 1.21+) with Datadog CPU profiles: "save up to 14% CPU".

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=go, https://docs.datadoghq.com/profiler/profiler_troubleshooting/go/

### Ruby
- Ruby **2.5+** (3.2.3+ recommended); JRuby and TruffleRuby not supported. Linux glibc and Alpine musl, x86-64 and aarch64.
- `gem 'datadog', '~> 2.30'`; gems older than 2.30 also need `pkg-config`/`pkgconf`.
- Enable via env (`DD_PROFILING_ENABLED=true`) or in code `Datadog.configure do |c| c.profiling.enabled = true ... end` (Rails: `config/initializers/datadog.rb`). **In-code values take precedence over env vars.**
- Start command: `bundle exec ddprofrb exec ruby myapp.rb` (Rails: `bundle exec ddprofrb exec bin/rails s`). If not possible (for example **Phusion Passenger**): `require 'datadog/profiling/preload'` in the entry point (such as `config.ru`).
- **Single Step APM Instrumentation cannot be used to set up the Ruby profiler.** Not supported on serverless.
- Options: `DD_PROFILING_ALLOCATION_ENABLED` (false), `DD_PROFILING_MAX_FRAMES` (default **400**; deeper stacks grouped as `Truncated Frames`), `DD_PROFILING_EXPERIMENTAL_HEAP_ENABLED`, `DD_PROFILING_NO_SIGNALS_WORKAROUND_ENABLED` (avoid `SIGPROF`, for native-extension `EINTR` issues, e.g. old `libmysqlclient`, `rugged`, Passenger < 6.0.19).
- Resque jobs: set `RUN_AT_EXIT_HOOKS=1` or short jobs produce no profiles.

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=ruby, https://docs.datadoghq.com/profiler/profiler_troubleshooting/ruby/

### Node.js
- Node.js **18+**. `npm install --save dd-trace@latest`.
- Env: `DD_PROFILING_ENABLED=true` (+ UST vars). If the tracer is not already initialized: `node -r dd-trace/init app.js`.
- In code: `require('dd-trace').init({ profiling: true, env: 'prod', service: 'my-web-app', version: '1.0.3' })`.
- Source maps: deployed `.map`/inline maps used automatically; uploaded source maps (Preview) need dd-trace 5.93.0+ and `@sourceMappingURL` annotations.
- Trace to Profiling and Endpoint Profiling: default on **Linux and macOS, not available on Windows**.
- Troubleshooting: "No native build was found ... abi=109" -> package-manager Node reporting wrong ABI (Ubuntu 24.04 Node 18) or bundler (esbuild/webpack/Next.js) issues; install Node from nodejs.org. `ERR_DLOPEN_FAILED` on Alpine -> unsupported musl; upgrade dd-trace/musl. Higher **event loop utilization** on idle apps after enabling is expected (signal wakes loop; CPU stays low).
- Isolate overhead: `DD_PROFILING_CODEHOTSPOTS_ENABLED=false`, `DD_PROFILING_TIMELINE_ENABLED=false`, `DD_PROFILING_ENDPOINT_COLLECTION_ENABLED=false`.

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=node_js, https://docs.datadoghq.com/profiler/profiler_troubleshooting/nodejs/

### .NET
- Runtimes (64-bit): .NET Framework 4.6.1+, .NET Core 2.1/3.1, .NET 5-10. OS: Windows 10 / Server 2012+, Linux glibc 2.17+ and musl. Continuous Profiler does not support ARM64 (requirements list) and not AWS Lambda.
- **Containers need more than one core**; profiler disabled below 1 core; override with `DD_PROFILING_MIN_CORES_THRESHOLD` (e.g. `0.5`, costs more CPU).
- **Not activated by default when the APM package is installed**; explicitly set `DD_PROFILING_ENABLED`. Profiler ships with the SDK since v2.8.0. The CLR Profiling API allows only one subscriber: run a single APM solution.
- **SSI on Linux**: only `DD_PROFILING_ENABLED` is needed. Values: `1`/`true` on, `0`/`false` off, `Auto` = profile only if (1) a trace was created and (2) the app runs > **30 seconds** (Preview; avoids short-lived processes). If APM was manually installed before, **remove** `CORECLR_ENABLE_PROFILING`, `CORECLR_PROFILER`, `CORECLR_PROFILER_PATH` and the `Datadog.Linux.ApiWrapper.x64.so` entry in `LD_PRELOAD`, otherwise the old version is silently used.
- Manual Linux: `CORECLR_ENABLE_PROFILING=1`, `CORECLR_PROFILER={846F5F1C-F9AE-4B07-969E-05C26BC060D8}`, `CORECLR_PROFILER_PATH=/opt/datadog/Datadog.Trace.ClrProfiler.Native.so`, `DD_DOTNET_TRACER_HOME=/opt/datadog`, `LD_PRELOAD=/opt/datadog/continuousprofiler/Datadog.Linux.ApiWrapper.x64.so`, `DD_PROFILING_ENABLED=1`. .NET Framework uses `COR_ENABLE_PROFILING`/`COR_PROFILER`. MSI installs v2.14.0+ do not need `CORECLR_PROFILER`/`COR_PROFILER`.
- **IIS**: set `DD_PROFILING_ENABLED` in the `Environment` multi-string value under `HKLM\System\CurrentControlSet\Services\WAS` and `...\W3SVC` (applies to all IIS apps; IIS 10+ can set per app in `applicationhost.config`). Then `net stop /y was` and `net start w3svc`; a reset/restart does not always work. Windows services: `Environment` value under `HKLM\System\CurrentControlSet\Services\<Service>`. NuGet `Datadog.Trace.Bundle` does not instrument IIS apps.
- Datadog does **not recommend enabling the profiler machine-wide** or for all IIS apps (fixed per-process overhead). Reduce: `DD_PROFILING_ENABLED=auto` with SSI, SSI instrumentation rules, `DD_PROFILING_WALLTIME_ENABLED=0`, more CPU cores.
- Keep traces but stop profiles: `DD_PROFILING_ENABLED=0` with `CORECLR_ENABLE_PROFILING=1`.
- Config defaults: wall time, CPU, exceptions, lock, GC on (`true`); allocation, live heap, HTTP, heap snapshot off. `DD_TRACE_LOG_DIRECTORY` default `%ProgramData%\Datadog .NET Tracer\logs\` (Linux logs under `/var/log/datadog`).
- Missing profiles: check Agent; loader log `dotnet-native-loader-*` for `Continuous Profiler initialized successfully`; `DD_TRACE_DEBUG=true`; in `DD-DotNet-Profiler-Native-*` log, `libddprof error: Failed to send profile.` = cannot reach Agent (check `DD_TRACE_AGENT_URL`); `Http code: 200` success, 403 = invalid API key; replaced signal handler disables CPU and wall time.
- Feature versions: Trace to Profiling 2.30.0+, Endpoint Profiling 2.15.0+, CPU 2.15.0+, wall time 2.7.0+.

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=dot_net, https://docs.datadoghq.com/profiler/profiler_troubleshooting/dotnet/

### PHP
- PHP **7.1+** on 64-bit Linux; ZTS builds since dd-trace-php 0.99+; debug builds not supported. glibc 2.17+; Alpine 3.13+ (musl 1.2) plus `apk add libgcc`.
- Install: download `datadog-setup.php`, run `php datadog-setup.php --enable-profiling --php-bin=all` (interactive; prints the non-interactive args). Configure: `php datadog-setup.php config set -d datadog.service=app-name -d datadog.env=prod -d datadog.version=1.3.2`. Restart Apache/PHP-FPM/FrankenPHP after INI changes.
- Verify: `php -v` lists `with datadog-profiling vX`.
- Feature versions: Trace to Profiling 0.89.0+ (connect page: 0.98+ with `DD_PROFILING_TIMELINE_ENABLED=1` / `datadog.profiling.timeline_enabled=1`), Endpoint Profiling 0.79.0+, Timeline 0.98.0+, Source Code Integration 1.13.0+.
- Missing profiles: run **`phpinfo()` from the web server, not the CLI** (each SAPI configured independently); the profiler adds diagnostics to it.
- Overhead: disable `datadog.profiling.allocation_enabled`, `datadog.profiling.experimental_cpu_time_enabled`, `datadog.profiling.exception_enabled`, `datadog.profiling.timeline_enabled` (leaves only wall time). Sampling distances: `datadog.profiling.exception_sampling_distance` (default 100), `datadog.profiling.allocation_sampling_distance` (default 4194304 bytes = 4 MB).

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=php, https://docs.datadoghq.com/profiler/profiler_troubleshooting/php/

### C, C++, Rust (ddprof, Preview)
- Linux (glibc or musl), amd64/arm64; `perf_event_paranoid` must be **2 or less**; symbols must not be stripped.
- Standalone: `./ddprof myapp --arg1` (env `DD_ENV`/`DD_SERVICE`/`DD_VERSION` or `--environment --service --service_version`). If launched with a shell builtin, use `exec ./ddprof myapp`. Library: `ddprof_start_profiling()` from `dd_profiling.h`, link `-ldd_profiling` (static preferred to avoid `libdd_profiling.so` not found). `--global` profiles all processes (debug only, elevated permissions).
- Missing profiles: `-l debug`; "Error calling perfopen on watcher" = permissions (`perf_event_paranoid`, `CAP_PERFMON`, `CAP_SYS_ADMIN`).

Sources: https://docs.datadoghq.com/profiler/enabling/?prog_lang=c, https://docs.datadoghq.com/profiler/profiler_troubleshooting/ddprof/

### Single Step Instrumentation (SSI) and host-level config
- SSI loads the SDK; then enable SDK-dependent products. Continuous Profiler: `DD_PROFILING_ENABLED`. All product vars accept `true`/`false`; **`DD_PROFILING_ENABLED` also accepts `auto`, recommended for SSI** (profiles only eligible processes).
- Linux host: `/etc/datadog-agent/application_monitoring.yaml` under `apm_configuration_default:` (for example `DD_PROFILING_ENABLED: true`); applies to all SDKs on the host; **env vars override it**; restart services. Go SDK reads only tracing options from this file.
- Kubernetes: Agent targets with `ddTraceConfigs` (for example `- name: "DD_PROFILING_ENABLED"` / `value: "auto"`), or the `DatadogInstrumentation` CRD (Agent and Cluster Agent v7.85+).
- Ruby profiler cannot be set up with SSI.

Sources: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/linux/, https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/kubernetes/, https://docs.datadoghq.com/tracing/trace_collection/library_config/application_monitoring_yaml/

### Connecting traces and profiles
- Processes with both APM tracing and the profiler enabled are **linked automatically**: in a trace, select a span and open the **Profiles** tab (code hotspots / "Trace to Profiling integration").
- Prerequisites: Java on by default (Linux/macOS, not Windows); manual Java spans must be **activated in a scope** (`tracer.activateSpan(span)`) for the link. Python: dd-trace-py 2.12.0+/2.11.4+/2.10.7+ and `DD_PROFILING_TIMELINE_ENABLED=true` (the Datadog page says to set it, but current ddtrace docs list its default as `True`, so do not ask "what must be set" for Python). Ruby: on by default with dd-trace-rb 1.22.0+. Node.js: default on Linux/macOS, not Windows (5.11.0+/4.35.0+/3.56.0+). Go: `DD_PROFILING_EXECUTION_TRACE_ENABLED=true` and `DD_PROFILING_EXECUTION_TRACE_PERIOD=15m` (records up to 1 minute or 5 MiB every 15 minutes; dd-trace-go 1.37.0+, 1.52.0+ for timeline). .NET: default, 2.30.0+. PHP: 0.98+ and `DD_PROFILING_TIMELINE_ENABLED=1`.
- Go queries: Profile List `go_execution_traced:yes`; Trace Explorer `@go_execution_traced:yes` (with `@`).
- Span **timeline view**: lanes are threads (goroutines for Go; one JS thread for Node; one lane per PHP thread). Top lanes = runtime activity (GC, etc.).
- **Open in Profiling** then **Focus On**: *Span & Children* (span and descendant spans in the same service), *Span only*, *Span time period* (all threads while the span was active), *Full profile* (60 s of the whole process).
- **Endpoint profiling**: scope flame graphs by endpoint, find top resource-consuming endpoints; on by default once profiling is on (Java requires the Datadog profiler, not JFR; Python 0.54.0+; Go 1.37.0+; Node 5.0.0+/4.24.0+/3.45.0+; .NET 2.15.0+; PHP 0.79.0+). **Per endpoint call** shows resource use per request, useful while traffic shifts. APM Service page **Profiling** tab correlates latency changes to code changes.

Sources: https://docs.datadoghq.com/profiler/connect_traces_and_profiles/

### Pitfalls checklist
- Enabling tracing does not enable profiling; set `DD_PROFILING_ENABLED` (or equivalent).
- `-javaagent` after `-jar` = ignored as JVM option.
- Go: env var alone does nothing without `profiler.Start` (unless Orchestrion).
- Ruby: forgot `ddprofrb exec` or preload; SSI cannot enable Ruby profiling; Resque needs `RUN_AT_EXIT_HOOKS=1`.
- .NET: container with < 1 core; leftover `CORECLR_*` vars under SSI; IIS needs full stop/start; `Auto` needs a trace and > 30 s runtime.
- PHP: diagnose with `phpinfo()` from the web server SAPI.
- Agent unreachable on 8126 / wrong `DD_TRACE_AGENT_URL`.
- Linux `perf_event_paranoid` 3 degrades Java CPU profiles and blocks ddprof.

# Domain 3: Insight Discovery

## Software Catalog

### Naming and where it lives
- Current docs call it **Catalog**, part of the **Internal Developer Portal (IDP)**. It was "Service Catalog", then "Software Catalog"; `/internal_developer_portal/software_catalog/` now serves the Catalog page. Old names still appear in places (e.g. "Service Catalog Write permission", event `source:software_catalog`, API "software-catalog", Terraform `software_catalog`).
- In app: **APM > Catalog** (app URL `/services` or `/software`). Setup page: **Catalog > Manage / Setup & Config** (`/software/settings/get-started`).
- IDP = Catalog + Scorecards + Self-Service Actions + Engineering Reports + Overview Pages (+ Campaigns, External Provider Status). It's fully managed, driven by live telemetry.
- Catalog = a centralized, real-time inventory of entities (services, APIs, systems, datastores, queues, frontends, custom kinds) enriched with ownership and operational metadata; integrates observability, security and cost tools.
- Entity = smallest building block of a microservice architecture. APM "service" = group of related endpoints, queries or jobs; in APM it's an identifier to group traces and aggregate metrics, not necessarily a logical service.
- Teams: Datadog Teams are the ownership unit; filter by team across IDP (Catalog, Scorecards, Engineering Reports); team hierarchies (parent/child subteams); GitHub Integration for Teams can sync GitHub teams.

Sources: https://docs.datadoghq.com/internal_developer_portal/, https://docs.datadoghq.com/internal_developer_portal/catalog/, https://docs.datadoghq.com/getting_started/internal_developer_portal/

### Catalog views (lenses)
- **Ownership**: team's Slack, repo, on-call info.
- **Reliability**: entities with recent deploys, rising error rates, open incidents, failing monitors. Related incidents (Datadog Incident Management + PagerDuty) show in Reliability tab. Incidents auto-link, but apply `SERVICE` tags to incidents; PagerDuty must be set up manually.
- **Performance**: latency, traffic, error rate, Apdex **by environment**. Performance tab has **Libraries** sub-tab (external libraries + versions) and **Dependencies** sub-tab.
- **Security**: vulnerable libraries and live attacks (App and API Protection, APM Security Views).
- **Costs**: AWS costs linked to code/infra changes, powered by **Cloud Cost Management**.
- **Software Delivery**: CI pipeline health, static analysis violations, DORA metrics.
- **Relationships**: dependency graph; hover a service card to see infra it runs on.
- **Infrastructure**: cloud resources (needs Resource collection, free for Infrastructure Monitoring customers); resources link to entities running on them.
- **Saved Views** pin frequently used views.
- Clicking an entity opens a **side panel** (tabs such as Ownership, Performance, Security, Costs, Definition, Setup Guidance); **Service Page** button (top right of side panel) or hover service name > **Service Page** opens the full APM service page. Selecting a service in Catalog leads to the service page.
- Service health (Critical/Warning/Ok from monitors, incidents, Watchdog) shows in Catalog, service pages, dependency maps, service pills. Critical: non-muted monitor with paging integration (PagerDuty/Opsgenie) in ALERT and triggered in past 2 days, any active incident, faulty deployment, APM latency/error Watchdog alert.
- Use entity type (e.g. `datastore type` facet) rather than the legacy `type` filter (from `span.type`).
- **Retention**: span summaries and service/resource statistics in Catalog retained up to **30 days**; use **Metric Explorer** for deeper analysis on APM trace metrics.
- Dashboards: **Developer Portal** data source queries Catalog entities (services, queues, frontend apps, APIs, systems); group/filter by ownership, tier, lifecycle, definition version. Widgets: Query Value, Top List, Table, Treemap, Pie, Bar.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/, https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/internal_developer_portal/use_cases/incident_response/, https://docs.datadoghq.com/internal_developer_portal/use_cases/production_readiness/, https://docs.datadoghq.com/internal_developer_portal/use_cases/appsec_management/

### How entities get into Catalog (discovery)
Three ways: detected from telemetry, declared in an entity definition, imported from third party (Backstage, ServiceNow).
- **Automatic by default**: APM, **USM** (eBPF-based, no code instrumentation, golden signals: requests, errors, durations), **RUM**.
  - APM + USM detect: `service`, `datastore`, `queue`, external providers, inferred services, endpoints. SDKs classify uninstrumented dependencies (DB, queue, third-party API) = inferred services.
  - RUM discovers **frontend apps** (shown as **Frontend Apps** in the component selector).
  - Performance metrics tie to the service's **primary operation**. USM-only service -> USM metrics; APM-only or APM+USM -> APM trace metrics.
- **Manual import from other telemetry**: logs, host/container/network/process metrics. **Import Entries** tab: Datadog searches that source for valid `DD_SERVICE` tags; entities marked `kind:service`. Only do it if `DD_SERVICE` tags are well maintained. Imported entries appear in **Explore**, and **may expire unless you add metadata** (owner, contacts) via API, GitHub or GitLab. **Clear Previously Imported Services** removes imported services from the default Explore view (docs: all services that "do not have metadata or do not have APM, USM, or RUM telemetry").
- Managing auto-named/inferred services: renaming rules, filter inferred entities by type, remove service overrides (e.g. `service:my-service-http-client`). Prefer inferred entities over arbitrary service overrides; use Unified Service Tagging (`service`, `env`, `version`) consistently.
- Correlation: to auto-link a definition to telemetry, `name` must **exactly match** the telemetry's primary identifier (the `service` tag for services).
- Troubleshooting:
  - APM service missing from list: no performance data in the **past hour** for the selected `env` (or other primary tag). Hover the Performance columns to see active environments.
  - Telemetry type missing: Catalog uses `DD_SERVICE` tag in all telemetry (infra metrics, logs, CNM) -> fix Unified Service Tagging.
  - SLO count in Setup Guidance counts SLOs with `service` tags matching service names.
  - Monitors associated when tagged, scoped or grouped by `service` or APM primary tags; Setup Guidance monitor count excludes muted monitors/groups.
  - "Adding metadata for RUM services is not supported" (troubleshooting page) - but v3 `kind: frontend` can link to a RUM app (see ambiguities).

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/, https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/discover_entities/, https://docs.datadoghq.com/internal_developer_portal/catalog/troubleshooting/

### Entity definitions: files, versions, fields
- Kubernetes-style YAML ("entity definitions") = canonical source of truth.
- File names: `service.datadog.yaml` or `entity.datadog.yaml` (both accepted). Multiple entities in one file: separate YAML documents with `---`.
- Name field: `dd-service` (schema v2.2 and earlier) vs `name` / `metadata.name` (v3.0+).
- Schema versions supported: **v3.0** (latest), **v2.2**, **v2.1**, **v2** (earliest supported). v3.0 NOT supported on ddog-gov (US1-FED/US2-FED) sites.
  - v2: basic metadata, team, contacts, links, separate `repos` and `docs` lists, `integrations.pagerduty` as URL string.
  - v2.1: service groupings, `application`, `tier`, `lifecycle` (production / experimental / deprecated); Application and Teams usable as grouping variables.
  - v2.2: user annotations (`extensions`), `ci-pipeline-fingerprints` (CI pipeline association), override auto-detected `type` and `languages`, looser `contact.type`/`link.type` validation.
  - v3.0: expanded data model (multiple kinds), multi-ownership, manual dependency declaration, system metadata inheritance, `codeLocations`, saved logs/events queries for systems, custom entities.
- v2.2 -> v3.0 changes: `schema-version` -> `apiVersion` (`v3`); new `kind` (service, queue, datastore, system, api, ...); `dd-service` -> `metadata.name`; `team` -> `metadata.owner` + `metadata.additionalOwners` (each with `name`, `type` e.g. operator/stakeholder/team); `lifecycle`, `tier`, `languages`, `type` -> under `spec`; `links`, `contacts`, `description`, `tags` -> under `metadata`; `application` -> its own `kind: system` (no longer a field on a service).
- v3 extra keys: `metadata.displayName`; `integrations.pagerduty.serviceURL`; `integrations.opsgenie.serviceURL` + `region`; `spec.components` (systems/APIs); `spec.dependsOn`; `spec.componentOf`; `spec.implementedBy` (API); `datadog.codeLocations` (`repositoryURL` + `paths` globs); `datadog.logs` / `datadog.events` (name + query); `datadog.pipelines.fingerprints`; `extensions`.
- Links: `links` field holds repos/docs/runbooks/dashboards (`type`: runbook, doc, repo, dashboard, other; optional `provider` e.g. github, wiki, gdoc). Use `links` for GitHub/GitLab source links.
- Contacts: `type` slack, email, microsoft-teams, ... with `contact` value.
- Example v3:
  ```yaml
  apiVersion: v3
  kind: service
  metadata:
    name: web-store
    owner: shopist
    additionalOwners:
      - name: sre-team
        type: operator
  spec:
    lifecycle: production
    tier: "1"
    dependsOn:
      - service:cws-webapp
  ```
- **Inheritance**: explicit `inheritFrom: <entity_kind>:<name>`; implicit - components (`service`, `datastore`, `queue`, `ui`) inherit all metadata from their system when only one system is defined in the file and `inheritFrom` is absent. A component in several systems must be listed in each system's YAML.
- Custom extensions (`extensions`, Limited Availability): org-specific metadata; reserved key `datadoghq.com/cd-visibility` for CD Visibility commit detection.
- Validation: schemas reject invalid values; warnings shown in the **Definition** tab of the side panel. JSON Schema registered in **Schema Store** -> IDE autocomplete/validation.
- Migration to v3: `pup idp migrate-schema <file|dir>` (no Datadog auth needed); writes `entity.datadog.yaml`; converts `application` into companion `kind: system` + `spec.componentOf`; normalizes link types (`wiki`->`doc`, `code`->`repo`, `url`/`oncall`->`other`); unknown top-level fields -> `extensions`.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/entity_model/, https://docs.datadoghq.com/internal_developer_portal/catalog/entity_model/v3_migration/

### Native and custom entity kinds (v3)
- Native: `service`, `system`, `api`, `datastore`, `queue`, `frontend`.
- **System**: group of entities cooperating for a broader function (same meaning as Backstage System Model); list members in `spec.components` (e.g. `service:orders-app`, `api:products`, `system:...`). System page aggregates relationships, scorecards, logs, events across components.
- **API**: collection of endpoints grouped logically (alternative to APM-service grouping; endpoint-to-service mapping not modifiable). OpenAPI spec inline (`spec.type: openapi`, `spec.interface.definition`) or by file (`spec.interface.fileRef`). `spec.implementedBy` lists implementing services. **Play Request** sends test HTTP requests (Public Location default, or Synthetics Private Location). Endpoints = APM resources of web services.
- **Datastore**: inferred by APM (outbound DB calls) or manual. For inferred ones `metadata.name` must exactly match the peer tags, e.g. `peer.db.name:web-store-mongo,peer.db.system:mongodb`. Peer tags: `peer.db.name`, `peer.db.system`, `peer.aws.dynamodb.table`, `peer.aws.s3.bucket`, `peer.cassandra.contact.points`, `peer.couchbase.seed.nodes`. With Database Monitoring, page shows query throughput/latency/errors.
- **Queue**: Kafka, SQS, RabbitMQ, Pub/Sub; inferred name must match peer tags e.g. `peer.messaging.destination:checkout-events`; also `peer.aws.sqs.queue`, `peer.aws.kinesis.stream`, `peer.kafka.bootstrap.servers`, `peer.messaging.system`. With Data Streams Monitoring, shows throughput/latency/errors.
- **Frontend**: browser SPA or mobile app; link to RUM app by name or `rum_application:<id>`; **Add Metadata** on an existing frontend app autofills the ID; `spec.type: browser`.
- **Custom entities**: any kind (library, pipeline, ML model). Create via **APM > Catalog > Manage > Manage Custom Entity Types > Add Custom Entity Type**, or Catalog API; then appears in the `kind` dropdown.
- **Manual dependencies** (v3 only): `spec.dependsOn`, also `ownedBy`, `partOf`. View: side panel > Performance > Dependencies sub-tab (or Service Page > Dependencies). **Include Detected** off = only manual; on = manual listed above auto-detected.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/entity_model/native_entities/, https://docs.datadoghq.com/internal_developer_portal/catalog/entity_model/custom_entities/, https://docs.datadoghq.com/internal_developer_portal/use_cases/dependency_management/

### Creating and syncing definitions (UI, API, Terraform, GitHub/GitLab)
- **UI**: Catalog Setup & Config > **Create a New Entry** > pick **Kind** (Service, API, System, ...) > fill metadata (ownership, links) > optionally switch to **YAML** or **JSON** (shows generated code + cURL; flags invalid data) > **Save Entry** (or run the cURL). Needs Catalog (Service Catalog) **Write** permission. Edit existing: entity page > **Edit in UI**.
- **Terraform**: `datadog_service_definition_yaml` resource (v2.x) / `datadog_software_catalog` (v3); needs Datadog Provider **v3.16.0+**.
- **API**: Service Definition API (schema v2.x; `POST /api/v2/services/definitions`, `GET|DELETE /api/v2/services/definition/<service_name>`) or Catalog API (v3+). Open-sourced GitHub Action solutions exist.
- **GitHub integration**: integration tile > **Repo Configuration** tab > **Link GitHub Account**. Datadog scans every repo it can read for `service.datadog.yaml` / `entity.datadog.yaml`; changes reflect within minutes. Adds an **Edit in GitHub** button on the entity's **Definition** tab.
- **GitLab**: GitLab Source Code integration, same file names.
- Pick ONE path per entity: updating the same service from both a source code integration and the API can overwrite each other.
- Validation errors for synced definitions: **Event Management**, filter `source:software_catalog` and `status:error`.
- Datadog Software Metadata Provider also mentioned as automation option.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/create_entities/, https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/

### Importing from Backstage and ServiceNow
- Backstage: (1) **Datadog Backstage plugin** (`@datadog/backstage-plugin-datadog-entity-sync-backend`, runs as backend service, syncs on configurable schedule, filterable; needs API key, application key and site), or (2) import descriptor files via API/Terraform (replace YAML with Backstage YAML) or GitHub integration, which scans for **`catalog-info.yaml`**.
- Mapping: `kind:component` -> service, `kind:system` recognized; `metadata.name` -> `dd-service`; `metadata.namespace` -> tag `namespace:...`; `spec.lifecycle` -> `lifecycle`; `spec.owner` -> `team`; `metadata.links` -> `links`; annotation `github.com/project-slug` -> repo link; `pagerduty.com/service-id` + `pagerduty.com/account` -> `integration.pagerduty`; `metadata.description` -> `description`; `spec.system` -> `application`; `spec.dependsOn` -> `dependsOn`; other `spec` values -> custom tags.
- Whole file processed as a unit: if any section lacks `kind:component` or `kind:system`, the **entire** `catalog-info.yaml` is rejected. `kind:system` and `dependsOn` require schema v3.0.
- ServiceNow: **Service Ingestion** feature of the ServiceNow integration; regular query against CMDB CI tables.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/import_entities/, https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/

### Ownership, on-call and integrations
- Ownership links entities to **Datadog Teams**: team filtering across products, attribute Scorecards/Campaigns, route notifications and on-call context.
- Team = name, **handle** (unique id, usable as facet `team:bits-demo`), members, optional description. Create in Organization Settings or from Catalog.
- Set owner: entity > **Edit in UI** > **Ownership** section > **Owner** + **Additional owners** (search name or paste `team:<handle>`) > **Save Entry**. In code, handles must exactly match existing Teams.
- Best practices: Teams not individuals; one primary owner; lowercase hyphenated handles; provision Teams via SAML/SCIM; use team filter; subteams for hierarchies.
- PagerDuty: set up integration, paste PagerDuty API Access Key on integration tile, add `integrations.pagerduty` (v2: URL; v3: `serviceURL`). One PagerDuty service per Catalog service. Shows on-call and active PD incidents.
- Opsgenie: API key with **configuration access** + **read**; add account + region in tile; `integrations.opsgenie.service-url` + `region`; then an **On Call** box appears in the **Ownership** tab.
- PagerDuty/Opsgenie IDP integrations not supported on ddog-gov sites.
- Action Catalog lets you act on integrated tools (Jira, Slack, GitHub, etc.).

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/ownership/, https://docs.datadoghq.com/internal_developer_portal/integrations/

### Permissions and setup guidance
- **Catalog Read**: Catalog list, Discover UI, `GET /api/v2/services/definition/<service_name>`. Default in **Datadog Read Only Role** and **Datadog Standard Role**.
- **Catalog Write**: `POST /api/v2/services/definitions`, `DELETE /api/v2/services/definition/<service_name>`, finishing Discover Services onboarding, updating metadata in UI. Default in **Datadog Admin Role** and **Datadog Standard Role**.
- **Setup Guidance** tab (click entity): automatic checks for recommended setup (tracing, logs, profiling, monitors, SLOs, Error Tracking). Reflects **entity activity, not billing**: e.g. `Infrastructure Monitoring` may show `Not Detected` if the service hasn't emitted infra metrics for a long time even though hosts run the Agent.

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/, https://docs.datadoghq.com/internal_developer_portal/use_cases/production_readiness/

### Scorecards (high level)
- Evaluate Catalog entities against pass/fail rules. Three out-of-the-box scorecards: **Production Readiness**, **Observability Best Practices**, **Ownership & Documentation** (10 OOTB rules). Not supported on ddog-gov sites.
- OOTB rules evaluated **every 24 hours** (once per day); default evaluation can be turned off. OOTB rules initially scoped to `kind:service`.
  - Production Readiness: any SLOs defined; any monitors defined; on-call specified; last deployment within **3 months** (APM/USM services).
  - Observability Best Practices: deployment tracking active (`version` tag via UST); logs correlation active (APM services, past hour of logs).
  - Ownership & Documentation: team defined; contacts defined; code repos defined; docs defined.
- Setup: Scorecards page in Catalog (docs link `/services/scorecard`) > enable/disable rules > **View your scores**. Overall % per scorecard; scorecard overview page also calls the third one "Documentation & Ownership".
- Custom rules: **Create Rule** (name, scorecard, description, owning team, level, scope) or Scorecards API (`/scorecard/rules`, outcomes to `/scorecard/outcomes/batch`) or Workflow Automation (**Update scorecard rule outcome** action, Scorecards blueprints; publish workflow or it won't run). Outcomes: `pass`, `fail`, `skip` (skip excludes from score).
- Scoring: each rule = % entities passing; scorecard overall % = passing evaluations across all rules, **not** entities passing all rules; skipped/disabled rules excluded. **By Kind** / **By Team** tabs average each entity's score.
- Levels: 1 Basic, 2 Intermediate, 3 Advanced; rules without a level default to **Level 3**; entity starts at **Level 0** and advances when all rules of a level pass.
- Scopes: by `kind`, `team`, `tier`, custom tags; all conditions must match (use `OR` for multiple values of one field); unscoped rule = all entities. Outcomes of entities leaving a scope are hidden, reappear if scope removed.
- Reports can be delivered to Slack. Example: cost compliance via custom rule that checks `team` tag on infra.

Sources: https://docs.datadoghq.com/internal_developer_portal/scorecards/, https://docs.datadoghq.com/internal_developer_portal/scorecards/scorecard_configuration/, https://docs.datadoghq.com/internal_developer_portal/scorecards/custom_rules/, https://docs.datadoghq.com/getting_started/internal_developer_portal/

### Common pitfalls
- Definition `name` that doesn't exactly match the `service` tag (or peer tags for inferred datastores/queues) -> metadata won't attach to telemetry.
- Expecting `dd-service` in a v3 file (it's `metadata.name`), or `team` in v3 (it's `owner`/`additionalOwners`), or `application` (now `kind: system`).
- Mixing GitHub sync and API writes for one entity -> overwrites.
- Imported-from-logs services without metadata can expire.
- Service "missing" usually = no data in the past hour for the selected `env`.
- Catalog statistics only go back 30 days; use Metric Explorer for longer trace metrics.
- Monitors only link to a service if tagged/scoped/grouped with `service` (or primary tags).
- Scorecard overall % is not "% of entities passing everything".

Sources: https://docs.datadoghq.com/internal_developer_portal/catalog/troubleshooting/, https://docs.datadoghq.com/internal_developer_portal/catalog/set_up/create_entities/

## Search Syntax

### Where search happens: Live Search vs indexed search
- Trace Explorer (APM > Traces, `app.datadoghq.com/apm/traces`) searches ingested or indexed spans using any tag on any span.
- **Live Search** (default view): all ingested spans for a rolling **15 minutes**, no sampling. Indicator: "Live Search - All ingested data". Query matches across **any span** and **any tag**, not just indexed ones.
- **Indexed search**: set the time selector (top right) to any period **greater than 15 minutes**. Indicator: "Search - Only Indexed Data". Spans indexed by custom retention filters are kept **15 days**; spans indexed by the intelligent retention filter are kept **30 days**.
- Pitfall: if you filter by a tag that appears only on spans not indexed by any retention filter, an indexed search returns **no results** (Live Search would have found them).
- Same search syntax in Live and indexed views.
- Live timeseries can group by only **one** dimension; indexed timeseries can split by up to three; Group by in the list view: up to **four** dimensions.
- Exporting to dashboards and monitors only works with retained (indexed) spans. APM queries in dashboards/notebooks use all indexed spans; APM monitors use spans indexed by custom retention filters only (intelligent retention filter spans are excluded from trace analytics monitors).
- All search parameters are stored in the page URL (shareable).
- Live list view: spans/second shown at top; Pause/Play button top right; selecting a span pauses the stream.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/visualize/

### Terms: span tags vs span attributes
- A query = *terms* + *operators*. Two term types:
  - **Span attribute**: content of the span, collected by automatic or manual (custom) instrumentation, or remapped in the backend (for example peer attributes). Examples: `http.url`, `http.status_code`, `error.message`, `db.statement`, `peer.db.name`.
  - **Span tag**: context enrichment from the host or container the service runs on. Examples: host tags `hostname`, `availability-zone`, `cluster-name`; container tags `container_name`, `kube_deployment`, `pod_name`.
- **Attributes need the `@` prefix**: `@git.commit.sha:12345`, `@http.url:...`. Nested JSON is addressed with dots (`git.commit.sha`).
- **Tags do not use `@`**: `hostname:web-server`, `kube_deployment:canary`, `availability-zone:us-east`.
- In the trace side panel: span tags appear in the **Infrastructure** tab; span attributes appear in the span info tab (query syntax page calls it the "Overview" tab, span tag semantics page calls it the "Info" tab; Trace View page calls it "Span Info").
- Clicking a tag/attribute in the side panel lets you add it to the search query (one-click search) or copy the value.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention/

### Reserved attributes (no `@`)
- Reserved attributes are present on every span and are queried **without** `@`.
- Span Tags/Attributes page list: `env`, `service`, `operation_name`, `resource_name`, `status`, `ingestion_reason`, `trace_id`.
- Query Syntax page list: `env`, `operation_name`, `resource_name`, `service`, `status`, `span_id`, `timestamp`, `trace_id`, `type`, `link`.
- `env` = value of `DD_ENV`; `version` = `DD_VERSION` (marked "APM core (Reserved)" in standard attributes).
- `status:error` selects error spans (the `Error Default` retention filter uses `status:error`).
- Examples: `service:payment-api status:error`, `resource_name:"/api/v1/checkout" @http.method:POST`, `resource_name:"GET /checkout" @duration:>2s env:prod`.
- Not reserved (need `@`): `@span.kind` (values `server`, `client`, `producer`, `consumer`, `internal`), `@component`, `@language`, `@http.status_code`, `@http.route`, `@error.type`, `@error.message`, `@error.stack`, `@db.system`, `@duration`, `@base_service`.
- `service` = service name (if it's an override, `@base_service` holds the service that emitted the span). With global default service naming (`DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAME_ENABLED=true`), `service` is the service **emitting** the span.
- Uninstrumented dependencies (inferred services: databases, queues, third parties) are searched with **peer attributes**, e.g. `@peer.db.name:users @peer.db.system:postgres`. Other peer tags: `peer.service`, `peer.hostname`, `peer.aws.s3.bucket`, `peer.aws.sqs.queue`, `peer.messaging.destination`, `peer.messaging.system`, `peer.rpc.service`, `peer.kafka.bootstrap.servers`... Agent 7.60.0+ collects all source attributes by default.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/standard-attributes/?product=apm, https://docs.datadoghq.com/tracing/services/inferred_services/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

### Boolean operators
| Operator | Meaning | Example |
|---|---|---|
| `AND` | intersection; **default** when no operator is written | `authentication AND failure` |
| `OR` | union | `authentication OR password` |
| `-` | exclusion | `authentication AND -password` |
- Parentheses group terms: `(hostname:web-server OR env:prod)`, `(service:api AND -kube_deployment:canary)`, `language:(go OR python)`.
- `service:web-store env:prod` = both conditions (implicit AND).
- Search is `key:value` plus full-text.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/search/

### Wildcards, numeric comparisons, ranges, units
- Multi-character wildcard `*`: `service:web*` (services starting with web), `@url:data*`, `@url:*user\=JaneDoe*`.
- Numeric comparisons on numerical attributes: `<`, `>`, `<=`, `>=`: `@http.response_time:>100`.
- Ranges: `@http.status_code:[400 TO 499]` (all 4xx).
- Durations accept units: `@duration:>2s`, `duration:>20ms`, `@duration:>1s`; trace-level `trace_duration:>5s`.
- Measures support units (time in seconds, size in bytes) for orders of magnitude at query and display time. **Unit is a property of the measure, not of the field**. Docs example: a `duration` measure in nanoseconds; `duration:>20ms` queries spans from services A and B consistently. (The query_syntax page version of this example also mentions scaling with arithmetic-processor multipliers `*1000000`/`*1000`; the span_tags_attributes page omits that step.)
- `duration` standard attribute (Performance group) is in **nanoseconds**; Datadog uses it as the default measure for trace search. The span_tags_attributes page example also uses "a `duration` measure in nanoseconds".
- Measures are (long) integer or double.
- Trace View span search (inside a single trace, waterfall/flame graph): free text on service/resource/operation name, `key:value`, groups `language:(go OR python)`, booleans, ranges `duration:>200ms`; **wildcards are NOT supported** there. With the `Error` checkbox, only matching spans in error state are returned.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

### Escaping and non-standard tags
- Special characters requiring escape with `\`: `?`, `>`, `<`, `:`, `=`, `"`, `~`, `/`, `\`.
  - `user=JaneDoe` inside url: `@url:*user\=JaneDoe*`.
- Spaces in attribute names (not recommended) must be escaped: `@user.first\ name:myvalue`.
- Tags not following tagging best practices: do not use `key:value`; use `tags:<MY_TAG>`, e.g. `tags:"auto-discovery.cluster-autoscaler.k8s.io/daffy"`.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/

### Autocomplete, saved searches, columns
- Search bar autocomplete completes queries from existing values; in Trace Queries span-query editors it suggests facets and recent queries. In Live Search you can type `process_id` and autocomplete new process IDs.
- Watchdog outlier tags appear as search suggestions (flagged as correlated with errors/latency) and in an "OUTLIERS" section at the top of the facet list.
- Saved searches store query, columns and time horizon; found via autocomplete by name or query; delete with the bin icon in the Trace search dropdown.
- Add columns via the Options button or from a facet/side panel; default list sort = timestamp, newest first.
- When filtered on error spans, "Group into Issues" shows Error Tracking issues instead of individual error spans.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/trace_explorer/visualize/

### Service entry spans, root spans, all spans
- **Service entry span**: entrypoint method of a request to a service (immediate parent in the flame graph has a different color).
- **Trace root span**: first span of a trace; its start marks the trace start.
- Box above the trace table selects **Service entry spans**, **Root spans**, or **All spans**. Use on high-traffic apps to show only entry points. It only filters the list; other spans still appear in the flame graph of the trace.
- You can filter on attributes that are not facets: click the attribute in the trace details panel to add it to the query, or type it (e.g. `cart.value`) in the search bar.
- Diversity sampling (intelligent retention filter) scans service entry spans.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/glossary/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

### Facets and measures
- Facets are created on tags and attributes to map them to a type (string, int) and show them in the facet list. **Facets are NOT required** to search spans, generate metrics from spans, or index spans with retention filters.
- **Qualitative facets**: relative insights (e.g. `datacenter`), unique counts (e.g. `usr.email`), frequent filtering (env). Show a top list of unique values with span counts.
- **Measures (quantitative facets)**: aggregate (p95, sums), compute highest latency services, filter continuous values. Show a min/max slider in the facet panel.
- Create from **trace side panel** (field path and type pre-filled): numeric field -> facet or measure; string field -> facet only.
- Create from **facet list** with **+ Add**: tag key name for infrastructure tags; attribute path with `@` prefix for span attributes. Works even before matching spans exist.
- Facet panel selections update the search bar and URL.
- Hiding facets is personal (does not affect teammates) unless you update a saved view; hidden facets remain findable in facet search. Facet groups only affect the facet list (no impact on search or analytics). The search facets box matches display name and field name.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/span_tags_attributes/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/

### Trace Queries (searching by span relationships)
- Find whole traces based on properties of multiple spans and their relationships. Two or more span queries labeled `a`, `b`, `c`... combined in the **Traces matching** field. "Add another span query" adds a query.
| Operator | Meaning | Example |
|---|---|---|
| `&&` | both spans in the trace | `service:web-store && service:payments-go` |
| `\|\|` | either span in the trace | `service:web-store \|\| service:mobile-store` |
| `->` | indirect: left span is upstream (anywhere) of right | `service:checkoutservice -> service:quoteservice` |
| `=>` | direct: left span is direct parent of right | `service:checkoutservice => service:shippingservice` |
| `NOT` | traces that do not contain matching spans | `service:web-store && NOT(service:payments-go)` |
- **Where** statement trace-level filters: `span_count(a):>10` (occurrences of a span query), `total_span_count:>1000` (spans in trace), `trace_duration:>5s` (end-to-end duration).
- Flow Map: request path and dependencies of matching traces; powered by a sample of ingested traffic; click a node to filter on traces containing that service.
- Trace list: up to **50** sample traces; columns show **root span** attributes and root span duration (not end-to-end).
- Analytics (Timeseries, Top List, Table): you must pick which span query (`a`, `b`...) to aggregate from: the one whose spans carry the grouped attribute.
- Data source: traces indexed by the **intelligent retention filter** (flat 1% + diversity sampling, both capture complete traces) and **trace-level retention filters** (with a **Trace rate** set). Spans retained by a filter without a trace rate (`retained_by:retention_filter`) are not in Trace Queries. Trace rate can significantly increase indexed span usage.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_queries/, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/

### Common pitfalls
- Forgetting `@` on attributes (`http.status_code:500` searches a tag, not the attribute); adding `@` to reserved attributes or infra tags is unnecessary.
- Using `key:value` for tags with non-standard formats (use `tags:"..."`).
- Not escaping `=`, `:`, `/`, spaces.
- Expecting non-indexed spans in searches longer than 15 minutes.
- Thinking a facet is required before searching.
- Confusing `->` (any upstream) with `=>` (direct parent); `@duration` (one span) with `trace_duration` (end-to-end, Where clause).
- Wildcards don't work in the Trace View span search bar.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/trace_queries/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/

## Trace Live vs Retained Search

### Two data sets in the Trace Explorer
- Trace Explorer (APM > Traces, `app.datadoghq.com/apm/traces`) searches **all ingested** spans (Live) or **indexed** spans (retained), using any tag on any span.
- **Ingested** spans = what your ingestion controls (SDK sampling rules, Agent options) send to Datadog. Ingested traces are available as **Live** traces for a **rolling 15-minute window**.
- **Indexed (retained)** spans = ingested spans kept by retention filters:
  - **Custom retention filters** (including the default ones such as `Error Default`) -> retained **15 days**.
  - **Intelligent retention filter** (diversity sampling + 1% flat sampling) -> retained **30 days** (current docs; older material says 15 days for everything).
- Glossary wording: ingestion controls send "up to 100% of traces to Datadog for live search and analytics for 15 minutes"; retention filters "determine what spans to index in Datadog for 15 days" (the glossary does not mention the 30-day intelligent-filter retention).
- Data Retention Periods page: APM indexed spans "15 or 30 days, determined by customer plan"; errors 15 days; services/resources statistics 30 days; viewed traces kept for the life of the account.
- Both ingested and indexed spans can affect the bill.
- Pitfall: retention filters never change what is ingested (what Live Search sees). To change ingestion use Ingestion Controls; to change what is kept after 15 minutes use retention filters.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/data_security/data_retention_periods/

### Switching modes and UI indicators
- **Live Search is the default view** on the Traces page.
- Indicator in Live mode: **"Live Search - All ingested data"**. Indicator when searching indexed spans: **"Search - Only Indexed Data"**.
- Switch Live -> indexed by using the **time selector in the top right-hand corner**: pick any time period **greater than 15 minutes** (for example `Past 1 Hour`, `Past 1 Day`). Time range can be a preset or a custom time frame.
- All search parameters live in the page URL (shareable). Saved searches/saved views store query, columns and time horizon.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/

### Live Search (last 15 minutes)
- Spans display as soon as the Agent sends them, **before** retention filters index them; all ingested spans for the last 15 minutes (rolling), **displayed without any sampling**.
- Query is matched against all ingested traces across **any span** and **any tag**, not only indexed ones. Same search syntax as other trace views.
- List view use cases: watch a deployment by filtering on a version tag; search 100% of ingested traces for an `org_id`/`customer_id` on a problematic child span; confirm a new `process_id`; watch load-test duration of a child resource; one-click queries from the trace panel; add/remove/sort columns.
- Received **spans per second** shown at top of the table. High-throughput streams show only some spans for visual clarity, but the search query still searches all available spans.
- **Pause/Play** button at top right pauses/resumes the stream. **Selecting any span pauses the stream** and opens the trace side panel.
- Span selector above the trace table: **service entry spans**, **root spans**, or **all spans**. Only filters the list; other spans still appear in the flame graph of the trace.
- You can filter on attributes that are **not facets** (example `cart.value`): click the attribute in the trace details panel to add it, or type `cart.value` in the search bar.
- Live Timeseries view: graph requests/errors matching criteria (for example errors on `ShoppingCart##checkout` with cart value >= $100), canary deployments, latency by region; can also show a **top list** (most impacted customers, availability zones, any tag).
- **Live Explorer timeseries can group by only ONE dimension** (indexed timeseries: up to three).
- **Exporting to dashboards and monitors is only possible using retained spans** (not from Live data).
- Ingestion Control changes applied with Remote Configuration (no redeploy) can be observed in the Live Search Explorer.
- Request Flow Map = service map + live exploring; scope traces by tags to map request flow between services; Export saves a PNG; Cluster/Flow layouts.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/#live-search-for-15-minutes, https://docs.datadoghq.com/tracing/trace_explorer/visualize/, https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/

### Indexed (retained) search
- Search retained spans the same way as Live; switch by choosing a time range > 15 minutes.
- List view: spans indexed by custom retention filters **and** the intelligent retention filter are searchable. If you filter on a tag that only exists on spans **not indexed by any retention filter**, you get **no results** (unlike Live Search).
- Timeseries view ("trace analytics"): spans from custom and intelligent filters are available; from the timeseries view **export the query to a dashboard, monitor or notebook**. Export menu also offers **generate a new metric** for the query.
- When you click an indexed span you always see the **complete trace** (all parent/child spans) in flame graph/waterfall, even if those spans were not indexed. But **only indexed spans are searchable**.
- Span links display only when the linked spans are ingested **and** indexed.
- Latency Breakdown may be missing for incomplete traces (error and rare samplers capture pieces of traces).

Sources: https://docs.datadoghq.com/tracing/trace_explorer/#indexed-spans-search-with-15-day-retention, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#create-your-own-retention-filter, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/

### Where each data set can be used (dashboards, notebooks, monitors)
- Trace Explorer aggregated views (timeseries, top list, table), dashboards and notebooks: **all indexed spans** (custom + intelligent retention filter).
- **Trace Analytics monitors**: only spans indexed by **custom retention filters**; spans indexed by the **intelligent retention filter are excluded**. Spans **indirectly** indexed by trace-level retention filters (spans in a retained trace that did not match the query) are also not evaluated.
- Trace Analytics monitors: Monitors > New Monitor > APM > Trace Analytics; default limit 1000 per account; group by up to four facets; evaluation window 5 minutes to 48 hours.
- Long-term trends without retention: **Generate Metrics** (APM > Generate Metrics) builds custom metrics from **all ingested spans** regardless of retention filters, kept **15 months**; names cannot start with `trace.`; billed as custom metrics. Spans dropped by sampling cannot generate metrics.
- Trace metrics (`trace.*`) are computed on 100% of traffic independently of sampling/retention.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#export, https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#trace-search-and-analytics-on-indexed-spans, https://docs.datadoghq.com/monitors/types/apm/, https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/

### Visualizations
- **List**: individual spans; default sort by timestamp (newest first); sort by any column; add columns from facet panel, trace side panel or **Options** button; Group into Issues for error spans (Error Tracking).
- **Trace Groups** in list view: group by up to **four** dimensions; per group REQUESTS, ERRORS, P95 Latency; group-by value can come from the span, `parent(a)` or `root`.
- **Timeseries**: measure (aggregation such as p95 of `Duration`) or unique count of a tag; split by up to **three** tags; rollup (for example `10min`); bars (counts), lines (statistical aggregations) or areas. Live Explorer: **one** group-by dimension.
- **Top list**: span count, unique count or measure split by **one** tag dimension.
- **Table**: top values from up to **three** dimension combinations; table grouped by one dimension = top list.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/visualize/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#trace-groups

### How retention filter choice affects what you find after 15 minutes
- Retention filters page: APM > Retention Filters (`/apm/traces/retention-filters`). Columns: Filter Name, Filter Query, Retention Rate (0-100%, uniform choice among matching spans), Spans Indexed (powered by `datadog.estimated_usage.apm.indexed_spans`), Last Updated, Enabled toggle. Permission `apm_retention_filter_write` to create/modify/enable/disable.
- **Order matters**: a span matching an earlier filter is kept or dropped there; later filters never see it.
- Default filters: `Error Default` (`status:error`, configurable/disableable), `App and API Protection Default`, `Synthetics Default`, `Dynamic Instrumentation Default`.
- Intelligent filter (always active, not billed): diversity sampling on **service entry spans** (at least one span per env/service/operation/resource combination every 15 minutes at most; p75/p90/p95 latency spans; diverse errors) and **1% flat sampling** (by `trace_id`; plus traces linked to 1% of RUM sessions by `session_id`). Flat sample is uniform so low-traffic services may be missing on short time frames.
- Span-level vs trace-level filters: span rate only -> only matching spans indexed (`retained_by:retention_filter`, not in Trace Queries); adding a **Trace rate** indexes complete traces (`retained_by:trace_retention_filter`, usable in Trace Queries). Span rate is evaluated first; trace rate can greatly increase indexed usage.
- `retained_by` values: `retention_filter`, `trace_retention_filter`, `diversity_sampling`, `flat_sampled` (refine with `@retention_reason:rum` or `@retention_reason:trace`).
- Trace Queries run on traces from the intelligent retention filter and trace-level retention filters.
- Example custom filter queries: `@transaction_amount:>100`, `resource_name:"GET /checkout" @duration:>2s env:prod`, `service:delivery-api @version:v2.0`.

Sources: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/, https://docs.datadoghq.com/tracing/trace_explorer/trace_queries/#how-trace-queries-source-data, https://docs.datadoghq.com/tracing/trace_pipeline/metrics/

### Query syntax reminders (both modes)
- `AND` default, `OR`, `-` exclusion. Attributes need `@` (`@http.status_code:[400 TO 499]`, `@http.response_time:>100`); reserved attributes without `@`: `env`, `operation_name`, `resource_name`, `service`, `status`, `span_id`, `timestamp`, `trace_id`, `type`, `link`.
- Wildcard `service:web*`; non-standard tags `tags:"..."`; escape special characters and spaces (`@user.first\ name:myvalue`).

Sources: https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/

## Profilers

### What the Continuous Profiler is
- Finds CPU, memory and I/O bottlenecks broken down by method name, class name and line number. Runs in production with low overhead (for example, it uses JDK Flight Recorder technologies on the JVM).
- Think of it as a "deeper" tracer: a fine-grained view of your code without adding instrumentation. APM tells you *which request/span* is slow; the profiler tells you *which line of code* consumes the resource.
- The profiler ships inside the Datadog SDKs (tracing libraries). Enable it with `DD_PROFILING_ENABLED=true` (Java system property `-Ddd.profiling.enabled=true`; Node.js in code `require('dd-trace').init({ profiling: true })`; Python `ddtrace-run` plus the env var, or `ddtrace.profiling.Profiler().start()`; Go `profiler.Start(...)` in code). Profiles appear on **APM > Profiles** "after a couple of minutes". Agent v6+ required, v7+ recommended; profiles are sent through the Agent's APM intake (8126/TCP).
- Java: `-javaagent:dd-java-agent.jar` must come **before** `-jar` (so it is a JVM option, not an application argument).
- Tag profiles with Unified Service Tagging: `DD_SERVICE`, `DD_ENV`, `DD_VERSION`; extra tags with `DD_TAGS` (`layer:api,team:intake`).
- Not supported on most serverless platforms (Java, Go, Ruby: not supported on AWS Lambda; Python and Node.js: Preview on AWS Lambda). Single Step APM Instrumentation cannot set up the Ruby profiler; for .NET with SSI only `DD_PROFILING_ENABLED` must be set.
- Optional: Source Code Integration links profiling frames to your Git repository (View repository commit, source code previews).

Sources: https://docs.datadoghq.com/profiler/, https://docs.datadoghq.com/profiler/enabling/, https://docs.datadoghq.com/getting_started/profiler/

### Retention
| Data | Retention |
|---|---|
| Flame graphs, call graphs, thread timelines | **8 days** |
| Flame graphs exported to a notebook (Profiling Flame Graph widget) | **1 year** |
| Individual profiles opened in the UI at least once | **1 year** |
| Profile metrics (timeseries, for dashboards) | **30 days** ("one month" on the overview page) |
- Notebook widget: the 1-year retention applies when the widget uses a fixed **Custom time** range, and that range must be inside the 8-day profiling retention window when you create the widget.
- Pitfall: an 8-day-old flame graph cannot be re-aggregated, but the profile *metrics* for the same period (for example CPU by method, CPU by version) are still available for 30 days.

Sources: https://docs.datadoghq.com/profiler/, https://docs.datadoghq.com/data_security/data_retention_periods/, https://docs.datadoghq.com/dashboards/widgets/profiling_flame_graph/

### Profile types (by language)
General meaning of the main types:
- **CPU**: time each function spent *running on the CPU*. Excludes off-CPU waiting (I/O, sleep, locks, channels).
- **Wall Time**: *elapsed* time in each function, including on-CPU time, waiting for I/O and anything else while it runs. Use it for latency questions ("why is this request slow even though CPU is low?").
- **Allocations / Allocated Memory**: number / bytes of heap allocations, **including allocations later freed**. Useful for garbage-collection load ("too much garbage").
- **Heap Live Size / Heap Live Objects / Live Heap**: memory/objects **not yet garbage collected** (still in use). Use it for overall memory usage and **memory leaks**.
- **Lock**: time waiting for (and in Python, holding) locks.
- **Thrown Exceptions**: number (and type) of exceptions thrown, caught or uncaught.
- **File I/O / Socket I/O**: time reading/writing files or sockets.

Per language (current docs):
- **Java**: CPU, Allocations and Allocated Memory (Java 11), Live Heap (v1.61.0+, Java 11+, enabled by default on Linux since v1.61.0), Wall Time, Class Load, Thrown Exceptions, File I/O, Lock, Socket I/O. CPU covers JVM-run code (Java, Kotlin) but not JVM operations or native code. Engines: **Datadog profiler** (default on Linux, uses perf; full set incl. wallclock) and **JFR** (Windows, macOS, Linux fallback; fewer types). Datadog recommends the Datadog profiler over JFR.
- **Python**: Wall Time, Lock Wait Time, Locked Time, Lock Acquires, Lock Releases, CPU (POSIX), Heap Live Size, Allocated Memory, Allocations (3.5+). Python CPU includes Python and native code.
- **Go**: CPU Time, Allocations (`alloc_objects`), Allocated Memory (`alloc_space`), Heap Live Objects (`inuse_objects`), Heap Live Size (`inuse_space`, ~50% of RSS at GOGC=100), Mutex, Block, Goroutines. Default profiling period 60s.
  - Only **CPU and Heap** profiles are enabled by default; Block, Mutex, Goroutine are opt-in via `profiler.WithProfileTypes(...)` (overhead).
  - **Mutex**: stack traces point to the `Unlock()` that let a blocked goroutine proceed (what *causes* contention). **Block**: waiting on mutexes and channel operations; stacks point to the blocked `Lock()` (where the program *gets blocked*). Block does not capture sleep, GC, network or syscalls, and records operations **only after they unblock**, so it cannot debug a stuck application. Block profiler can add noticeable overhead; prefer high rates (`100000000` = 100 ms).
  - **Goroutines**: snapshot of goroutine counts per function; a growing count means a goroutine leak. Needs stop-the-world pauses (~1 µs per goroutine, once per period).
  - Delta profiles: since Go profiler `1.33.0` Allocations/Allocated Memory/Mutex/Block show values *during the profiling period* instead of accumulated since process start (on by default; `WithDeltaProfiles` can disable from 1.35.0).
- **Ruby**: CPU, Wall Time, Allocations (v2.3.0+, manual enablement), Heap Live Objects/Size (Preview, Ruby 3.1+, manual enablement), GVL profiling in Timeline (Ruby 3.2+). Env vars: `DD_PROFILING_ALLOCATION_ENABLED`, `DD_PROFILING_EXPERIMENTAL_HEAP_ENABLED`, `DD_PROFILING_MAX_FRAMES` (default 400).
- **Node.js**: CPU (Linux and macOS, not Windows), Wall Time, Heap Live Objects, Heap Live Size (stacks truncated to 64 frames), Allocated Memory / Allocations (Preview, Node.js 26+ and `DD_PROFILING_ALLOCATION_ENABLED=true`).
- **.NET**: Wall Time, CPU (v2.15+), Thrown Exceptions (v2.31+), Allocations (v3.28+), Lock (v2.49+), Live Heap (v3.28+, .NET 7+), Outgoing HTTP requests in Timeline (Preview), Thread lifetime in Timeline, GC CPU consumption. Toggles: `DD_PROFILING_WALLTIME_ENABLED`, `DD_PROFILING_CPU_ENABLED`, `DD_PROFILING_EXCEPTION_ENABLED`, `DD_PROFILING_LOCK_ENABLED` (default true); `DD_PROFILING_ALLOCATION_ENABLED`, `DD_PROFILING_HEAP_ENABLED`, `DD_PROFILING_HTTP_ENABLED`, `DD_PROFILING_HEAPSNAPSHOT_ENABLED` (default false).
- **PHP**: Wall Time, CPU, Allocations and Allocated memory (v0.88+, period 67s, not with JIT on some 8.0/8.1/8.2 versions), Thrown Exceptions (v0.92+), File I/O and Socket I/O (Preview).
- **Rust/C/C++ (ddprof)**: CPU, Allocations, Allocated memory (period 59s).
- **Full Host (eBPF)**: CPU Time; multi-threaded CPU time can exceed elapsed time ("1m 30s per minute"). No timeline view.

Sources: https://docs.datadoghq.com/profiler/profile_types/, https://docs.datadoghq.com/profiler/enabling/supported_versions/, https://docs.datadoghq.com/profiler/profiler_troubleshooting/java/

### Searching profiles (Profile Search / Explorer)
- Go to **APM > Profiles** and select a service. Filter with infrastructure tags or application tags (from your tracing environment configuration).
- Default **facets**: **Env** (`production`, `staging`), **Service**, **Version**, **Host**, **Runtime** (`JVM`, `CPython`).
- The search query uses tags/facets, for example `env:prod service:movies-api-java`; Go execution-traced profiles can be found with `go_execution_traced:yes` in the profile list (`@go_execution_traced:yes` in Trace Explorer).
- **Visualize as** options documented for the Explorer include Flame Graph (default visualization), Thread Timeline and Profile List; the docs also describe Timeseries/Table and Call graph visualizations.
- Profile **metrics** (timeseries) such as top CPU by method, top allocations by thread, CPU by version can be graphed on dashboards to track performance over deployments.

Sources: https://docs.datadoghq.com/profiler/profile_visualizations/#search-profiles, https://docs.datadoghq.com/profiler/

### Visualizations
**Flame graph** (default visualization)
- Each row: a frame called by the frame above it (for example `Thread.run()` -> `Thread.runWith(...)` -> ...).
- **Width of a frame = how much of the total resource (for example CPU) it consumed**, including what it calls.
- **Self time** = time a method spent itself without calling another method (the part of the box with nothing below it). Example: `parse()` 309 ms total, child `String.length()` 112 ms -> 197 ms self time.
- The side **"CPU time by Method"** top list counts **self time only**.
- By default darker frames = higher CPU usage; the most resource-intensive methods are grouped on the **leftmost** side.
- The flame graph **does not represent the progression of time**: side-by-side frames may have run concurrently or interleaved; identical call stacks are merged.
- Can be added to dashboards and notebooks with the **Profiling Flame Graph widget** (Show = profile type, by = frame granularity such as method or line, scope to methods/endpoints with `per Minute by Endpoint` or `per Endpoint Call`).

**Timeline view / Thread Timeline**
- Equivalent to the flame graph but shows time-based patterns and work distribution over a single profile, a single process, or a trace.
- Helps you isolate spiky methods, sort out complex interactions between threads, and surface runtime activity (GC, JIT/compilation) that impacted the process.
- Access: **APM > Profiles > Explorer**, set **Visualize as** to **Thread Timeline**.
- Lanes: Java/Python/Ruby = one lane per **thread** (pools grouped); Go = one lane per **goroutine** (grouped by `go` statement); Node.js = one lane for the JavaScript thread plus async activity lanes (DNS, TCP connect); .NET = threads grouped by name (`Managed Threads`); PHP = one lane per PHP thread (fibers in the same lane). Lanes on top = runtime activity (for example GC). Not supported for Full Host profiling.

**Call graph**
- Same data as the flame graph, but each method appears **once as a single node**; edges show which methods called each other.
- **Edge thickness** = time spent calling other methods; **color and size** of a node = **self time**.

**Timeseries and Table**: broad set of per-runtime metrics.

**Single profile**
- By default profiles are **uploaded once a minute**; depending on the language each process is profiled for **15 to 60 seconds** (Go default period 60s, PHP 67s, ddprof 59s).
- Open one: **Visualize as > Profile List**, click an item. Header shows service, env, version.
- Tabs: **Profiles** (flame graph + summary table, switch profile type), **Insights** (heuristics suggesting potential issues), **Metrics** (profiler metrics from all profiles of the same service), **Runtime Info** (runtime properties and profile tags), **Related Processes**.
- Upper-right options: Compare this profile with others, View repository commit, View traces for the same process and time frame, Download the profile, Open in full page.

Sources: https://docs.datadoghq.com/profiler/profile_visualizations/, https://docs.datadoghq.com/getting_started/profiler/, https://docs.datadoghq.com/dashboards/widgets/profiling_flame_graph/

### Comparing profiles
- Compare a profile with: profiles from a different time, an average of the service's profiles over time, or profiles with different tags (env, version, data center, availability zone, pod, canary).
- Shows whether the service takes more/less time, memory, allocations, exceptions, or involves more/less code.
- Works best when the application had a **similar workload (total requests)** in both periods.
- Entry points:
  - **APM > Profiles > Comparison**: pick a service and two time periods.
  - From a single profile: click **⇄ Compare**; the selected profile becomes **Profile B (comparison target)**; Profile A (**baseline**) is an aggregation time frame + tags or a specific profile ID.
  - From the Explorer aggregated view: click **Compare To** to compare with another version's aggregated profile. (The monolith guide also uses Compare next to the search field with `Previous 15 minutes`.)
- Select the metric to compare (depends on language), for example check allocation spikes while investigating CPU.
- Legend colors: **red** (deepening) = more time in B; **green** (deepening) = less time in B; **purple** = only in profile A; **blue** = only in profile B. Hover a method to see the metric comparison.

Sources: https://docs.datadoghq.com/profiler/compare_profiles/, https://docs.datadoghq.com/profiler/guide/isolate-outliers-in-monolithic-services/

### Automated Analysis (insights)
- Automatically detects performance issues from profiling data. Each insight gives: a high-level summary, contextual insights (affected methods, packages, processes), and recommended **Next Steps**; **Fix with Bits** asks Bits Code to generate a fix.
- Where: Profile explorer -> **Insights** section at the top of the page, within a flame graph view, within a timeline view (including the span timeline). An **Insights list page** shows all insight types across services: service and runtime, insight type, **priority (high, medium, low)**; filter by insight name, runtime, service, env.
- Java examples: Virtual Thread Pinning (High), Virtual Thread Submit Failure (High), Allocation Stall, CPU Burst (>75% CPU across a 10s window), CPU Burst Saturation (>= 1 s at 100%), Deadlocked Threads Detected, **Explicit GC** (`System.gc()` calls), GC Pause Peak Duration (a pause > 1 s), **GC Pauses** (> 10% of time in GC pauses), GC Setup, Thrown Exceptions (rate > 10K/minute by default), VMOperation Peak Duration (> 2 s), Duplicated Flags (for example `-Xmx2g -Xmx5g`), **GC Overhead** (> 20% CPU in GC/allocation), High Lock Contention, Primitive Value Boxing (> 5% CPU), Thread Pool Size (CPU-bound pool larger than core count), Context Switches (> 50k/s), Unbalanced Parallelism.
- Python: High Lock Contention. Go: GC Overhead, High Lock Contention. Ruby: GC Overhead. Node.js: CPU Starvation (High, no CPU samples for >= 100 ms), Event Loop Blocking, CPU Burst, GC Overhead, Libuv Pool Overload. .NET: Sync-over-Async Blocking, Exception Overhead, Excessive String Concatenation, High Lock Contention, GC Overhead.

Sources: https://docs.datadoghq.com/profiler/automated_analysis/

### Traces to profiles (Profiles tab on a span, formerly "code hotspots")
- Processes with both APM tracing and the profiler enabled are **automatically linked**: in a trace, click a span and open the **Profiles** tab to see profiling data and the lines of code for that span.
- Prerequisites: Java enabled by default on Linux/macOS (not Windows); for **manually instrumented Java code, spans must be activated in a scope** (`tracer.activateSpan(span)`) for the profiler to link. Ruby `dd-trace-rb` 1.22.0+. Node.js Linux/macOS only. .NET `dd-trace-dotnet` 2.30.0+. PHP 0.98+ with `DD_PROFILING_TIMELINE_ENABLED=1`. Python: `dd-trace-py` 2.12.0+/2.11.4+/2.10.7+ and `DD_PROFILING_TIMELINE_ENABLED=true`. Go: `DD_PROFILING_EXECUTION_TRACE_ENABLED=true` and `DD_PROFILING_EXECUTION_TRACE_PERIOD=15m` (records up to 1 minute or 5 MiB of execution trace every 15 minutes).
- **Span execution timeline view**: shows how threads contributed to the request over the span's duration; isolate time-consuming methods, thread interactions, runtime activity (lanes on top may be unrelated to the request), Automated Analysis highlights.
- **Open in Profiling** opens the data on a full page; **Focus On** selector:
  - **Span & Children**: selected span plus descendant spans in the same service.
  - **Span only**: only the selected span.
  - **Span time period**: all threads during the time the span was active.
  - **Full profile**: 60 seconds of the whole service process that executed the span.
- From a single profile, "View traces for the same process and time frame" goes the other way.

Sources: https://docs.datadoghq.com/profiler/connect_traces_and_profiles/

### Endpoint profiling
- Scope flame graphs by **endpoint** (resource) to find endpoints that are slow or consume the most CPU, memory, exceptions; identify bottleneck methods; see whether third-party code or runtime libraries are responsible.
- Enabled by default in all supported languages when profiling is on (Java requires the Datadog profiler, not JFR; Node.js only on Linux and macOS, not Windows).
- **Per Minute by Endpoint** = total consumption; **Per endpoint call** (`CPU Time per Endpoint Call`) = average consumption per request, which stays meaningful when traffic changes (progressive rollouts, daily traffic patterns).
- Service Page **Profiling** tab correlates latency/throughput changes with code performance changes (example: lock contention increase on `/GET train` caused by `Thread.sleep(...)`).
- Monolith guide: change **Show - Avg of** to `CPU Cores for Top Endpoints`, then `CPU - Average Time Per Call for Top Endpoints` to tell a traffic increase from a per-request regression. Group by **Trace Operation** (Java) for operation-level granularity.
- Custom business-logic labels: Java `Profiling.get().newScope()` + `scope.setContextValue("customer_name", ...)` and declare keys with `DD_PROFILING_CONTEXT_ATTRIBUTES=customer_name` (`-Ddd.profiling.context.attributes`, comma-separated for several); Go `pprof.Labels` + `profiler.WithCustomProfilerLabelKeys(...)` (v1.60.0+); Node.js `tracer.profiling.runWithLabels()` + `setCustomLabelKeys()` (dd-trace 5.97.0+, Node 24+). Then select the key under the **CPU time by** dropdown.

Sources: https://docs.datadoghq.com/profiler/connect_traces_and_profiles/#break-down-code-performance-by-api-endpoints, https://docs.datadoghq.com/profiler/guide/isolate-outliers-in-monolithic-services/, https://docs.datadoghq.com/tracing/services/service_page/#profiling

### Using profiles to find CPU and memory issues
- CPU problem: open the CPU flame graph for the time range, find the widest frames and high self time; check whether a lot of CPU is in GC (getting-started example: ~6% CPU in GC -> look at **Allocated Memory**, where `replyJSON()` allocated 17.47 GiB in one minute).
- Latency with low CPU: use **Wall Time**, Lock, I/O profiles or the timeline.
- Memory leak: use **Heap Live** profiles (memory not yet garbage collected) and compare profiles over time to see retained objects growing. Allocation profiles show churn/GC pressure, not leaks.
- **Memory Leaks walkthrough**: APM > Catalog > service > Service Page > **Memory Leaks** tab. Requires a **containerized** service with the Kubernetes or Container integration, Continuous Profiler enabled, profiles tagged with **`container_id`**, and heap profiling enabled (Java: heap histogram `DD_PROFILING_HEAP_HISTOGRAM_ENABLED=true`, Java 17.0.9+, not ZGC; .NET: `DD_PROFILING_HEAPSNAPSHOT_ENABLED`). Steps: scope data, recommend integrations/upgrades, explain runtime memory management, confirm leaks by inspecting retained objects with profile comparisons.
- Java exception storms (exceptions used for control flow) can overwhelm the profiler: temporarily disable with `-Ddd.integration.throwables.enabled=false`.
- Go: Profile-Guided Optimization (Go 1.21+) can use Datadog CPU profiles to save up to 14% CPU.

Sources: https://docs.datadoghq.com/getting_started/profiler/, https://docs.datadoghq.com/profiler/guide/solve-memory-leaks/, https://docs.datadoghq.com/profiler/profiler_troubleshooting/java/

## Deployment Tracking

### The `version` tag and Unified Service Tagging (requirement)
- Deployment Tracking is driven by the `version` tag, one of the three reserved Unified Service Tagging (UST) tags: `env`, `service`, `version`.
- `version` is applied to infrastructure metrics (host, container, process, NPM checks), trace metrics, traces, profiles and logs.
- `version` is expected to change with every deployment: two different versions of the code should have distinct `version` values.
- Without `version` you get no version breakdowns on the Service page, no Deployments section, no deployment comparison and no Automatic Faulty Deployment Detection (FDD). Change Tracking also needs a `version` tag on the service to show backend code deployments (source: APM).
- UST requirements: Datadog Agent 6.19.x / 7.19.x or higher; an SDK that supports the reserved-tag config. Minimum SDKs: .NET 1.17.0+, C++ 0.1.0+, Go 1.24.0+, Java 0.50.0+, Node 0.20.3+, PHP 0.47.0+, Python 0.38.0+, Ruby 0.34.0+.
- Tracer env vars: `DD_ENV`, `DD_SERVICE`, `DD_VERSION`.
- `DD_VERSION` adds `version` to all spans of the SDK's own service (generally `DD_SERVICE`). Spans the service creates with the name of an *external* service do NOT get `version`.
- As long as `version` is on spans, it is added to the trace metrics generated from those spans (so `version` is available on trace metrics, alongside `env` and `service`).
- If logs injection is enabled, the SDK injects `env`, `service`, `version` into logs; DogStatsD clients add them to custom metrics (not the .NET and PHP DogStatsD clients).
- Non-containerized: export per process, e.g. `DD_ENV=<env> DD_SERVICE=<service> DD_VERSION=<version> /bin/my-service`, or populate systemd/initd files via Chef/Ansible. For Agent-level system metrics, adding `version` is NOT recommended (Agent config doesn't change per service process invocation).

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/, https://docs.datadoghq.com/change_tracking/change_types/

### Setting `version` per platform
- Kubernetes (full config): labels on BOTH parent workload and pod template: `tags.datadoghq.com/env`, `tags.datadoghq.com/service`, `tags.datadoghq.com/version`; for APM also set `DD_ENV`/`DD_SERVICE`/`DD_VERSION`, manually or via the downward API (`fieldPath: metadata.labels['tags.datadoghq.com/version']`). The Cluster Agent Admission Controller injects these three env vars automatically to match the labels.
- Multiple containers per pod: `tags.datadoghq.com/<CONTAINER_NAME>.version`.
- Docker: env vars + labels `com.datadoghq.tags.env`, `com.datadoghq.tags.service`, `com.datadoghq.tags.version` (e.g. `ENV DD_VERSION <VERSION>` and `LABEL com.datadoghq.tags.version="<VERSION>"` in the Dockerfile). Labels only (partial config) for untraced software like Redis/NGINX.
- ECS: `environment` + `dockerLabels` in the task definition. On Fargate, put tags on the application container, not the Agent container. On Fargate with Fluent Bit/FireLens, UST covers metrics and traces only, not logs.
- OpenTelemetry: `service.version` -> `version`; `service.name` -> `service`; `deployment.environment.name` (Agent 7.58.0+, Exporter v0.110.0+) or deprecated `deployment.environment` -> `env`. `DD_SERVICE`/`DD_ENV`/`DD_VERSION` are NOT supported out of the box in OTel config. Set via `OTEL_RESOURCE_ATTRIBUTES="service.name=...,deployment.environment.name=...,service.version=1.2.3"`, the SDK `Resource`, or the Collector transform processor. `OTEL_SERVICE_NAME` beats `service.name` in `OTEL_RESOURCE_ATTRIBUTES`.

Sources: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/

### Automatic version tagging (containerized, APM data only)
- Applies only to APM data. Requires Datadog Agent 7.52.0+.
- Priority order: (1) your own `version` value (never overridden); (2) `{image_tag}_{first_7_digits_of_git_commit_sha}`; (3) `{image_tag}` or `{first_7_digits_of_git_commit_sha}` if only one is available.
- In containers, if `image_tag` is enough, no further config. Outside containers, or to include the Git SHA, embed Git information in build artifacts (Source Code Integration; SDKs then tag spans with `git.commit.sha` and `git.repository_url`).
- On ECS, `DD_VERSION` is described as optional with automatic version tagging.

Sources: https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/#automatic-version-tagging-for-apm-data-in-containerized-environments, https://docs.datadoghq.com/source_code/service-mapping/

### Version breakdowns on the Service page and Resource page
- Requests widget (when `version` is available): Total Requests by Version / Requests Per Second by Version. Current Service page dropdown names: Requests by Version, Requests per Second by Version, Requests and Errors Per Second.
- Errors widget: Total Errors by Version (named "Errors by Version" in the current Service page dropdown), Errors Per Second by Version, % Error Rate by Version (plus overall Errors per Second and % Error Rate).
- Latency graph: Latency by Version (plus Historical Latency, Latency Distribution, Latency by Error, Apdex).
- Requests and Errors widgets can be exported to dashboards and monitors. Resource page offers the same version scoping, also exportable.
- `version` can be used in Trace Explorer (Live Search and indexed spans) to filter or group; Analytics with `version` can be exported to dashboards/monitors.
- Profiles can be searched by version; View Profiles (top right of Deployment Comparison page) opens Continuous Profiler scoped to either compared version.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/tracing/services/service_page/#out-of-the-box-graphs, https://docs.datadoghq.com/tracing/services/resource_page/

### Deployments section (versions deployed)
- Services with `version` tags show versions in the Deployments section/tab of the Service page: all versions active during the selected time interval, active versions at the top.
- Appears ONLY if more than one version is reporting during the selected time interval.
- Default columns: version name; first seen / last seen times of traces for that version; Error Types indicator; requests per second; error rate (% of total requests).
- Error Types indicator = number of error types in a version that did not appear in the immediately previous version. It does NOT prove the version introduced them; a good starting point for investigation.
- Optional columns (add/remove, selection is saved): endpoints active in this version but not the previous one; Time active (first trace to last trace sent for that version); total Requests; total Errors; Latency p50/p75/p90/p95/p99/max.
- Summary cards at top of Service page highlight potential faulty deployments and let you click into the latest deployment or view all deployments.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/#versions-deployed, https://docs.datadoghq.com/tracing/services/service_page/#deployments

### Deployment comparison page
- Click any version row to open the version comparison page. Default: selected version vs the immediately previous version; you can change it to compare ANY two versions within the past 30 days.
- Comparison Graphs: Requests and Errors graphs highlight the two selected versions; all other versions in gray. With Continuous Profiler enabled, also CPU Time / Allocated Memory per APM resource, with pivot to Profile Comparison.
- Error Comparison: error types only in the source version (troubleshooting), no longer appearing in the source version (validating fixes), active in both. Pivot to live or historical traces. Caveat: based on *observed* error types; a rare error may show as "no longer appearing" only because it hasn't been seen yet.
- Endpoint Comparison: requests, latency, errors per endpoint; sort by Value to check highest-throughput endpoints are healthy, by % Change to spot large latency/error-rate changes.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/#deployment-comparison

### Deployment strategies
- Rolling deploys: watch traffic shift from old to new version across hosts/containers.
- Blue/green: compare requests/errors by `version` to detect one cluster with higher error rate, a cluster missing SLOs, or a cluster receiving traffic that shouldn't be.
- Canary: deployed to a limited number of hosts or fraction of customers; compare error rates, traces and behavior of the canary version; traces of a removed canary remain available to investigate.
- Shadow: release candidate receives copied production traffic, users only see production results; compare error rates/traces to decide whether to release.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/#deployment-strategies

### Automatic Faulty Deployment Detection (Watchdog)
- Enabled by configuring services with the `version` tag. On every deploy, Watchdog compares the new version with previous versions to spot new error types or increases in error rates. Goal: reduce MTTD; finds faulty deployments within minutes.
- Results on the APM Service page and the Resource page of affected endpoints. A currently active faulty version shows a pink banner at the top of the service page; the Deployments table marks versions found faulty in the past.
- View Details (in banner) or clicking a version in the Deployments table opens a slide-out panel: error-rate increase graphs, error type of new errors, affected endpoint, HTTP status code (example: `db.utils.OperationalError` on `/inventory` with 500).
- A faulty deployment is added as an event in the Event Explorer. Alerting: New Monitors > Events, query includes `tags:deployment_analysis`. Or Suggested Monitors button > Enable (button only shown if the service has no monitor configured yet).
- Each deployment is repeatedly analyzed; recommended monitor recovery time: 60 minutes to avoid re-alerting on the same deployment.
- Not flagged despite errors when: error type not new (in preceding versions or recent deployments); errors few and transient; not enough previous deployments for a baseline; error rate not significantly higher; the pattern is common during deployments of this service even when not faulty.
- Service health shows Critical when a faulty deployment is ongoing (Watchdog Insights condition).

Sources: https://docs.datadoghq.com/watchdog/faulty_deployment_detection/, https://docs.datadoghq.com/tracing/services/service_page/#service-health

### Deployment Gates (high level)
- Purpose: evaluate a rollout with monitors and APM Faulty Deployment Detection so the pipeline can halt releases on regressions. Not supported on the government sites (app.ddog-gov.com, us2.ddog-gov.com). The FDD analysis runs automatically for all APM-instrumented services, no prior setup required.
- Gate: defined for service + environment + optional identifier (default `default`; e.g. `pre-deploy`, `canary-20pct`). Rule: checks monitors or runs FDD on the deployed version. A gate passes only if ALL active rules pass.
- A gate does NOT stop a deployment itself; the pipeline decides (halt, rollback, alert).
- Rule types: Monitor (fails if a monitor group is `ALERT` or `NO_DATA` during the period, no groups match, an explicit ID doesn't exist, or >300 monitors match; muted monitors excluded; `query` and `monitor_ids` are mutually exclusive; `duration` default 0, max 7200 s) and APM Faulty Deployment Detection (`faulty_deployment_detection`; new error types or significant error-rate increase vs previous versions; duration recommended at least 900 s / 15 min, max 7200 s / 2 h; `allowed_resources` XOR `excluded_resources`; evaluated per additional primary tag value plus aggregate; detection at resource level; not for `database` or inferred services).
- Configuration sources: Inline (rules sent in each request / `--config` JSON file; no gate ID; no setup in Datadog) vs Preconfigured (created in Software Delivery > Deployment Gates > Configuration, API or Terraform; has an ID; referenced by service/env/identifier). Both appear on the Evaluations page.
- Evaluations are asynchronous: request -> evaluation ID returned -> pipeline polls (`in_progress`) -> `pass`/`fail`. `datadog-ci` and the GitHub Action poll for you; Argo Rollouts AnalysisTemplate also supported.
- `datadog-ci deployment gate --service <svc> --env <env> [--identifier default] [--version 1.0.1]`; `--version` required when the gate has an FDD rule. Command available in datadog-ci v3.17.0+ (`--config` v5.19.0+). Needs `DD_API_KEY`, `DD_APP_KEY`, `DD_BETA_COMMANDS_ENABLED=1` (Preview command).
- Evaluation modes: Active vs Dry run. A dry-run gate always returns `pass` to the pipeline but the real result is recorded on the Evaluations page; a dry-run rule's result is excluded from the gate result. Inline: `dry_run` (API, snake case) / `dryRun` (datadog-ci config, camel case); per-rule `dry_run` overrides gate-level.

Sources: https://docs.datadoghq.com/deployment_gates/, https://docs.datadoghq.com/deployment_gates/setup/preconfigured/, https://docs.datadoghq.com/deployment_gates/setup/inline/

### Change Tracking (related)
- Backend code deployments appear as changes on the Service page changes timeline, monitor status pages and dashboards (Show Overlays). Requirement: `version` tag on the service. Frontend deployments come from RUM deployment tracking.

Sources: https://docs.datadoghq.com/change_tracking/, https://docs.datadoghq.com/change_tracking/change_types/

### Common pitfalls
- Reusing the same `version` for different builds hides deployments; versions must be distinct per deploy.
- Deployments section hidden when only one version reported in the selected time range: widen the time range.
- Error Types indicator / Error Comparison show *observed* differences, not proof of cause or fix.
- In OTel, set `service.version`, not `DD_VERSION`.
- On Kubernetes, label both the workload and the pod template; on ECS Fargate, tag the app container.
- FDD alerting is an Events monitor on `tags:deployment_analysis`, with 60 min recovery recommended.

Sources: https://docs.datadoghq.com/tracing/services/deployment_tracking/, https://docs.datadoghq.com/watchdog/faulty_deployment_detection/, https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/

## Error Tracking

### What Error Tracking is (APM / backend)
- Error Tracking groups thousands of similar error events into a single **issue**. An issue aggregates error data: how many users were impacted, when the error first occurred, which commit probably caused it.
- Lets you: track/triage/debug fatal errors, group errors into issues to cut noise, set monitors on new or high-impact issues, follow issues over time (first seen, still ongoing, how often).
- Sources: errors from **APM traces**, **Logs** and **RUM** (Browser/Mobile SDKs) all land in one unified Error Tracking Explorer. Features vary by source (for example, Exception Replay exists only for APM-based errors).
- APM setup: available for **all languages supported by APM**; requires **no additional SDK and no configuration changes**. Optional: GitHub integration / Source Code Integration to see code snippets in stack traces.
- APM issues include: distribution of impacted spans, the latest most relevant stack trace, span attributes, host tags, container tags and metrics.
- Standalone Backend Error Tracking (no full APM): Agent **v7.61+**; `datadog.yaml`: `core_agent: enabled: false` and `apm_config: error_tracking_standalone: enabled: true`. Docker env vars: `DD_CORE_AGENT_ENABLED=false`, `DD_APM_ERROR_TRACKING_STANDALONE_ENABLED=true`. Helm: `datadog.apm.errorTrackingStandalone.enabled: true`.
- Retention: **error samples 30 days**; **issues 1 year after last activity**.
- UI: APM > Error Tracking (`app.datadoghq.com/apm/error-tracking`); settings at Error Tracking > Settings.

Sources: https://docs.datadoghq.com/tracing/error_tracking/, https://docs.datadoghq.com/error_tracking/, https://docs.datadoghq.com/error_tracking/apm/, https://docs.datadoghq.com/error_tracking/backend/getting_started/dd_libraries/, https://docs.datadoghq.com/data_security/data_retention_periods/

### Which spans become Error Tracking issues
- An error span must carry all three span attributes **`error.type`**, **`error.message`**, **`error.stack`** AND **belong to a complete trace** to be tracked.
- The stack must have **at least two lines** and **one meaningful frame** (a frame with a function name and a filename in most languages).
- If an error is reported multiple times within a service, **only the top-most error is kept** (the exam guide frames this as the service entry span; the docs' troubleshooting example query for eligible spans is `@_top_level:1 @error.stack:* AND @error.message:* AND error.type:*`).
- Setting only `error:1` on a span marks it as an error in APM but is not enough for Error Tracking without the three attributes.
- Error Tracking computes a **fingerprint** for each error span from error type, error message and stack trace frames; same fingerprint = same issue.
- Stack-trace attribute used:
  - All languages except Go: the **handling** stack (where the error was caught, e.g. a catch block or middleware) is in `error.stack` - not always where it was thrown.
  - Go tracer **v2.7.0+**: throwing stack in `error.stack` (used if available), handling stack in `error.handling_stack` (fallback).
  - Go tracer before v2.7.0: throwing stack in `error.details` (used if available), handling stack in `error.stack` (fallback).
- **No error samples on an issue panel (APM)**: all errors are processed, but only retained errors show as samples -> the spans must be retained by a **custom retention filter**.
- **Errors not found**: check the three attributes, and that the error matches at least one inclusion rule and no exclusion filter (Manage Data Collection).
- RUM (for contrast): only errors with source `custom`, `source`, `report` or `console` AND a stack trace; `network` errors and browser-extension errors are not processed.

Sources: https://docs.datadoghq.com/tracing/error_tracking/, https://docs.datadoghq.com/tracing/error_tracking/stack_traces/, https://docs.datadoghq.com/error_tracking/troubleshooting/

### Making custom / handled errors trackable
- Python (`ddtrace`): an exception raised while a span is active is captured automatically; the span is flagged as error with stack trace and message attached as tags.
  ```
  with tracer.trace("throws.an.error") as span:
      raise Exception("Oops!")
  ```
- Manual flag: `span.error = 1` (marks span erroneous only). To mark the local root span with the full exception: `root_span = tracer.current_root_span()` then `root_span.set_exc_info(exc_type, exc_val, exc_tb)` - sets error type, marks error, adds traceback.
- Java (OpenTracing API): set the error tag and use `Span.log()` with an "error event" map containing `Fields.ERROR_OBJECT -> Throwable` and/or `Fields.MESSAGE -> String`.
- .NET OTel API example: `SetTag("error", 1)`, `error.message`, `error.stack`, `error.type`.
- **Capturing handled errors** (errors caught in code that would otherwise be invisible): supported for **Python and Ruby** only; Agent **7.61.0+**; `dd-trace-py` **3.8.0+** (Python 3.10+), `dd-trace-rb` **2.16.0+**. Reported as **span events** on the span where handled and directly to Error Tracking. Handled errors carry `error.handling:handled`. Only APM Error Tracking / Standalone Backend Error Tracking (not Logs/RUM).
  - Python automatic: `DD_ERROR_TRACKING_HANDLED_ERRORS` = `user` | `third_party` | `all` (user code, third-party packages, or both); or `DD_ERROR_TRACKING_HANDLED_ERRORS_INCLUDE=module1,module2` (full module names, e.g. `mysite.security`). Python 3.10/3.11 need `instrument_main()` to instrument `__main__`.
  - Python manual: `span.record_exception(e)` (optionally `span.record_exception(e, {"foo": "bar"})`) - creates a span event and reports to Error Tracking.
- Standalone backend ET can also take errors sent via OpenTelemetry API span events.

Sources: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python/dd-api/, https://docs.datadoghq.com/error_tracking/backend/capturing_handled_errors/, https://docs.datadoghq.com/error_tracking/backend/capturing_handled_errors/python/

### Error grouping (fingerprinting)
- Default grouping properties: **`service`**, **`error.type`** (or `error.kind`), **`error.message`**, **`error.stack`** (filename + function name of the **top-most meaningful frame** = the error's *location*).
- If any of these differ, errors go to different issues: no grouping **across services** or **across error types**.
- Message normalisation: Error Tracking **ignores numbers, punctuation, and anything between quotes or parentheses**; only word-like tokens are used. Tip: put variables in error messages inside quotes or parentheses for better grouping. Variable stack frame properties (versions, ids, dates) are removed.
- **Custom grouping**: set span tag **`error.fingerprint`** (any string, no required format) on the error span.
  - Takes precedence over the default strategy.
  - Can apply to a subset of errors; coexists with default grouping for the rest.
  - Value used as-is (converted to a standardized fingerprint format).
  - Same service + same `error.fingerprint` -> same issue; **different `service` -> different issues** even with the same fingerprint.
  - Python: `span.set_tag('error.fingerprint', 'my-custom-grouping-material')`.

Sources: https://docs.datadoghq.com/tracing/error_tracking/error_grouping/

### Error Tracking Explorer
- Each row is an issue: error type and message, path to file where errors fire, first/last seen, occurrences-over-time graph, count in selected time range.
- Issue tags: **`New`** = first seen **less than two days ago** and in FOR REVIEW; **`Regression`** = was RESOLVED and occurred again in a newer version; **`Crash`** = application crashed; **Suspected Cause** label.
- Time range: top-right timeline; shows issues having occurrences in that period.
- Sort: **Relevance** (age, occurrences over last day, notable increase in past hour, crashes), **Count** (total occurrences in range), **Newest** (first seen), **Impacted Sessions** (RUM sessions).
- Facets auto-created from a predefined list; Edit (pencil) icon shows/hides facets. Common attributes: `error.message`, `error.type`, `error.stack`, `error.handling`.
- `error.handling`: APM errors are `handled` if a parent span reports a successful operation (`HTTP 200`, `gRPC OK`) or successful error handling (`HTTP 400`, `gRPC NOT_FOUND`); RUM errors are `unhandled` if not captured manually.
- Issue-level filters: **Sources** (All, Browser, Mobile, Backend; narrow by log source or SDK/language), **Fix available** (AI-generated fix), **Teams**, **Assigned to**, **Suspected Cause**.
- Suspected Cause categories (assigned at issue creation, editable by clicking the label): Code Exception, Failed Request, Illegal Object Access, Invalid Argument, Network.
- Issue panel: upper part = lifecycle (first/last occurrence, total count, count over time); APM issues show span tags (resource, operation name) with links to the trace and linked logs; lower part = error samples (stack trace, impacted users).
- Export the explorer search query directly to create an Error Tracking monitor.
- Query to find errors with Exception Replay snapshots: `@error.debug_info_captured:true`.

Sources: https://docs.datadoghq.com/tracing/error_tracking/explorer/, https://docs.datadoghq.com/error_tracking/suspected_causes/

### Issue states and lifecycle
- Five states: **FOR REVIEW** (new or regressed; needs attention), **REVIEWED** (triaged, needs fixing now or later), **RESOLVED** (fixed, no longer occurring), **IGNORED** (no further action; can be snoozed), **EXCLUDED** (stops collecting new errors, no longer counts toward usage/billing).
- **All issues start in FOR REVIEW.** Change status manually by clicking the status and picking from the dropdown. History: issue details panel > **Activity** tab (Activity Timeline).
- **Automatic review** -> REVIEWED when: the issue is **assigned**, or a **work item is created** from it (e.g. Jira/Linear/Work Management).
- **Automatic resolution** -> RESOLVED: if last reported in a version **more than 14 days old** and a newer version was released without the error; without `version` tags, if **no new errors in the last 14 days**. (Page also says "auto-resolution logic does not take version into account" - contradictory.)
- **Regression detection**: a RESOLVED issue that recurs in a **newer version** (or recurs at all in code without versions) moves back to **FOR REVIEW** with a **Regression** tag (same issue, context kept, no duplicate). Configure `version` tags (Unified Service Tagging / deployment tracking).
- **EXCLUDED**: click status > EXCLUDED. Excluded issues remain visible in the **IGNORED tab**; select any other status to resume collection.
- **Snooze** (moves to IGNORED until a condition, then back to **FOR REVIEW**): hover IGNORED and choose **For…** (duration), **Until this occurs again…** (occurrences), **Until this affects an additional…** (distinct users; requires `@usr.id`). Counting starts at snooze time. Snoozed issues appear in the IGNORED tab. Any manual status change (even to IGNORED) cancels the snooze. Combined conditions / other attributes (e.g. `@account.id`) only via the Datadog MCP Server `update_datadog_error_tracking_issue` tool.
- **Linked GitHub PRs** (paste issue URL from Actions > Link a Pull Request into PR description; needs GitHub integration with PR read, Source Code Integration and Error Tracking Issue Write permission): FOR REVIEW + PR linked -> REVIEWED; REVIEWED + linked PR merged -> RESOLVED (only when the last open linked PR merges; closing without merge does not resolve); RESOLVED + PR reopened or new open PR linked -> REVIEWED.

Sources: https://docs.datadoghq.com/tracing/error_tracking/issue_states/, https://docs.datadoghq.com/error_tracking/regression_detection/, https://docs.datadoghq.com/error_tracking/link_pull_requests/

### Controlling what is ingested (cost)
- Error Tracking > Settings (`/error-tracking/settings/rules`): **Rules** and **Rate limits**.
- Rule = scope (inclusion filter query, e.g. `service:my-web-store`) + optional nested exclusion filters (e.g. `env:staging`). Evaluated in order; **first matching active rule wins**. Default rule: `*` inclusion with no exclusions (catch-all). Reorder with the six-dot drag handle.
- Rate limit: errors/day cap on billable errors; after cap, ingestion stops until next day; emits a `Rate limit applied` event.
- **Dynamic Sampling**: on by default; samples errors of one spiking issue based on daily rate limit and history; emits `Dynamic Sampling activated` event; can be disabled in settings.
- Alternatives: mark issue EXCLUDED; drop whole traces with ignore-resources config.

Sources: https://docs.datadoghq.com/error_tracking/manage_data_collection/, https://docs.datadoghq.com/tracing/error_tracking/

### Error Tracking monitors
- Create: **Monitors > New Monitor > Error Tracking**. Default limit **1000** Error Tracking monitors per account.
- Two alerting conditions: **New Issue** (issue occurs for first time **or a regression occurs**) and **High Impact** (issues with a high number of impacted end users).
- New Issue monitors alert only on issues in **For Review**; regressions move to For Review so they are covered by default. Only consider issues created/regressed **after the monitor was created or last edited**; **24-hour lookback**. "Alert on all new issues" = error count > 0 over past day.
- High Impact monitors alert on issues in **For Review or Reviewed**.
- Source selector: All, Browser, Mobile, Backend. Suggested metrics: Error Occurrences, Impacted Users (user emails), Impacted Sessions (session IDs); **with All or Backend selected, only Error Occurrences is available**. Custom measure = count of unique values of a facet.
- Defaults: evaluation window **last 1 day**; threshold **0** (triggers on first occurrence). Use **multi alert** (one notification per issue, grouped by `issue.id`).
- Query syntax (Terraform/API): `error-tracking("{filter}").source("backend").new().rollup("count").by("issue.id").last("1d") > 0`; High Impact uses `.impact()`. `.source()` takes one of `"all"`, `"browser"`, `"mobile"`, `"backend"` (one at a time).
- Notification variables: `{{issue.attributes.error.type}}`, `.error.message`, `.error.stack`, `.error.file`, `.error.is_crash`, `.error.category`, `.error.handling`.
- **Ignored issues are automatically muted** from monitor notifications.
- `issue.age` / `issue.regression.age` not added by default (can miss alerts, e.g. issue first seen in staging then prod a week later); not recommended.
- Too noisy: triage issues (Reviewed/Ignored/Resolved), expand the evaluation window, raise the threshold.

Sources: https://docs.datadoghq.com/tracing/error_tracking/monitors/, https://docs.datadoghq.com/monitors/types/error_tracking/

### Suspect commits, Source Code Integration, ownership
- Suspect commit criteria: modifies one of the lines in the stack trace; authored **before** the first error occurrence; authored **no more than 90 days** before it; the **most recent** commit meeting these. Shown on the issue panel; **View Commit** button opens GitHub. Commits made before setup are not displayed.
- Requirements: **Source Code Integration** (Integrations > **Link Source Code**) and the **GitHub integration** with read permissions for **pull requests and contents**.
- Source Code Integration: SDK reads Git info embedded in the build and tags every span with `git.commit.sha` and `git.repository_url`. Options: `DD_GIT_COMMIT_SHA` and `DD_GIT_REPOSITORY_URL` env vars, Docker build args, OCI image labels `org.opencontainers.image.revision` / `org.opencontainers.image.source`, setuptools (`import ddtrace.sourcecode.setuptools_auto`, `DD_MAIN_PACKAGE`); OTel: `vcs.repository.url.full`, `vcs.ref.head.revision`. Python: Agent 7.35.0+, client 1.12.0+.
- In the issue panel: under Latest Event, **Connect to preview** for inline snippets (GitHub/GitLab), or View file / View Git blame / View commit.
- **Auto Assign**: assigns issue to the **author of the suspect commit** and notifies them; needs SCI + GitHub integration (Contents, Members); toggle globally or per service in Error Tracking settings.
- **Issue Team Ownership** priority: (1) `team` attribute on the error event (e.g. `span.set_tag("team", "payments-backend")`), (2) GitHub `CODEOWNERS` of the top-most in-repo stack frame (third-party frames skipped). Service ownership always applied and stays dynamic. Team/CODEOWNERS assignment is immutable. GitHub only.

Sources: https://docs.datadoghq.com/tracing/error_tracking/suspect_commits/, https://docs.datadoghq.com/integrations/guide/source-code-integration/, https://docs.datadoghq.com/source_code/service-mapping/, https://docs.datadoghq.com/source_code/service-mapping/python/, https://docs.datadoghq.com/source_code/features/, https://docs.datadoghq.com/error_tracking/auto_assign/, https://docs.datadoghq.com/error_tracking/issue_team_ownership/

### Exception Replay
- Captures execution context and **local variable values** (plus stack trace) when an exception occurs; shown in Error Tracking with the issue. Built on **Dynamic Instrumentation**. Production-safe: rate-limited, sensitive data auto-redacted.
- **GA for Python, Java, .NET, PHP**; **enabled by default when supported**. **APM-based exceptions only** (not Logs or RUM). Not available on GovCloud/FedRAMP sites (`app.ddog-gov.com`, `us2.ddog-gov.com`).
- Requirements: Agent **v7.49.0+** and an APM-instrumented app. Enablement: by environment (default on; Remote Configuration required; Python >= 3.15.0, Java >= 1.54.0, .NET >= 3.57.0, PHP >= 1.19.0), by service in-app (Exception Replay Settings page; Remote Config required), or by env var **`DD_EXCEPTION_REPLAY_ENABLED=true`** (no Remote Config needed; overrides in-app setting).
- Snapshots are emitted as **logs** (`source:dd_debugger`) linked to spans: create a dedicated logs index filtering `source:dd_debugger`, no sampling, placed ahead of other indexes (first match wins).
- With Source Code Integration, hover variable names in the code preview to see captured values.
- Redaction: **Strict Mode** (redacts all except numbers and Booleans) or **Targeted Mode** (known sensitive patterns + high-entropy scanner -> `[REDACTED:HIGH_ENTROPY]`; auto in `staging`/`preprod`). Modes cannot be disabled, only switched. Identifier-based redaction (e.g. `password`, `accessToken`) before data leaves the host; extend via custom identifiers, class/type rules, Sensitive Data Scanner.
- Rate limit: **one snapshot per exception type per instance per hour**; some runtimes capture only after the **second occurrence**.
- Missing snapshots: not enabled, outside time window, third-party package exclusions (`DD_THIRD_PARTY_DETECTION_EXCLUDES`), `source:dd_debugger` logs dropped by index retention/exclusion filters, FedRAMP, Java classes compiled with `-parameters` on JDK 18 and below, .NET FIPS hosts before tracer 3.55.0.
- Find errors with snapshots: `@error.debug_info_captured:true`.

Sources: https://docs.datadoghq.com/tracing/error_tracking/exception_replay/

## Span Summary

### Core terms: trace, span, root span, service entry span
- **Trace**: tracks the time spent processing a request and the request's status. Each trace has one or more spans.
- **Span**: a logical unit of work in a distributed system for a given period. Multiple spans make a trace. Span ID + trace ID are numerical identifiers generated by the SDK; together they correlate traces and logs.
- **Trace root span**: the first span of a trace; the entry-point method of the traced request; its start marks the beginning of the trace.
- **Service entry span**: the entrypoint method for a request to a service. Visual cue: on a flame graph, its immediate parent is a **different color** (different service). A root span is also a service entry span (glossary example: `rack.request` is both root and service entry span; every `mongodb` span is a service entry span of the mongodb service).
- **Resource**: a particular domain of an application, typically an instrumented web endpoint, database query or background job (e.g. `GET /productpage`, `ShoppingCartController#checkout`). Web resources are grouped under a static span name such as `web.request`; DB resources under `db.query`.
- **Span tag**: key-value pair on a span to correlate a request with other telemetry or to filter in searches.
- Trace Explorer span list can be restricted to **service entry spans**, **root spans**, or **all spans** (box above the trace table). This only filters the list; the other spans still appear in the flame graph when you open a trace.

Sources: https://docs.datadoghq.com/glossary/#trace-root-span, https://docs.datadoghq.com/glossary/#service-entry-span, https://docs.datadoghq.com/tracing/glossary/, https://docs.datadoghq.com/tracing/trace_explorer/

### Execution time (and "active" spans)
- **Execution time** = total time a span is **active**, i.e. not waiting for a child span to complete. Computed by adding up the time a span has no running child spans.
- Non-concurrent children: parent exec time = parent duration minus the time covered by its (sequential) children; each leaf child's exec time = its own width.
- **Concurrent children**: overlapping time is **divided by the number of concurrently active spans**. Example: child span B runs 100 ms; sibling span C runs 40 ms fully inside B -> overlap 40 ms split 2 ways -> C = 20 ms, B = 60 + 20 = 80 ms; the parent gets 0 ms for that period.
- "A span is considered active when it's not waiting for a child span to complete. The active spans at a given time, for a given trace, are all the **leaf spans** (spans without children)."
- **Sublayer metrics**: execution duration of a given type or service within a trace; tagged `sublayer_service` and `sublayer_type`; only available if a service has downstream dependencies.
- Resource page "Avg Time per Request" graph breaks down average execution time per request across downstream services (dropdown: Total Time Spent, % of Time Spent). It is built on **sampled trace data**, unlike the other top graphs (unsampled). No sub-services graph for leaf services like Postgres or Redis.
- Pitfall: a long span with little exec time is mostly waiting on children; a long span with high exec time is doing work itself (or has un-instrumented work inside it).
- The current APM docs do not define a separate "critical path" view for traces; "critical path" in the glossary is a CI Pipeline Visibility term. For APM, reason with execution time / % Exec Time.

Sources: https://docs.datadoghq.com/glossary/#execution-time, https://docs.datadoghq.com/glossary/#sublayer-metric, https://docs.datadoghq.com/tracing/services/resource_page/#span-summary, https://docs.datadoghq.com/tracing/services/resource_page/#avg-time-per-request

### Span Summary table (Resource page)
- Location: **Resource page** (APM > service > resource), section "Span summary". The glossary: the Resource page "shows the span summary widget with an aggregate view of spans for all traces, latency distribution of requests, and traces".
- Gives a span analysis breakdown of **all matching traces** for the resource. Metrics are per span (span name/service row):
  - `Avg Spans/trace` - average number of occurrences of the span, for traces including the current resource **where the span is present at least once**.
  - `% of Traces` - percentage of traces including the current resource where the span is present at least once.
  - `Avg Duration` - average duration of the span, for traces including the current resource where the span is present at least once.
  - `Avg % Exec Time` - average ratio of execution time for which the span was active, for traces including the current resource where the span is present at least once.
- Glossary long names: Average spans per trace, Percentage of traces, Average duration, Average percentage of execution time.
- Purpose: shows how often a span shows up, what % of traces contain it, its average duration and its typical share of execution time -> helps **detect N+1 problems** (e.g. a DB query span with a high `Avg Spans/trace`).
- **Only available for resources containing service entry spans.** (Same restriction for the resource Dependency Map: only for service-entry span resources.)
- Pitfall: averages exclude traces where the span is absent (they are not averaged over all traces of the resource); `% of Traces` tells you how often it is present.
- Other Resource page items: Requests and Errors, Errors, Latency (incl. Latency Distribution, Apdex), Avg Time per Request; Dependency Map (based on a sample of ingested spans, request rates upscaled); Frontend Impact (needs RUM, web resource, built on indexed trace data from the past 1 hour); Traces list (filtered on env, service, operation, resource); export graphs to dashboards via the up-arrow.

Sources: https://docs.datadoghq.com/tracing/services/resource_page/#span-summary, https://docs.datadoghq.com/glossary/#span-summary, https://docs.datadoghq.com/tracing/glossary/#resources

### Trace View: header and visualizations
- Trace View shows all spans of one trace plus metadata. Four visualizations: **Flame Graph**, **Span List**, **Waterfall**, **Map**.
- **Trace header**: root span's service name, resource name, trace ID, end-to-end trace duration, trace start time. Permalink: click **Open Full Page** and save the URL.
- **Flame Graph** (DEFAULT): all color-coded spans on a timeline; shows execution path and where time was spent. Navigate: scroll to zoom, click-and-drag to move, **minimap** to zoom to selected span or out to full trace. Legend groups spans by **Service (default)**, **Base service** (service the span is emitted from), **Host** or **Container**; display **% Exec Time** or **Spans** (span count) per group. **Errors** checkbox under Filter Spans highlights error spans. Inferred-service spans have a **dashed outline**.
- **Span List**: displays resources by group (**service by default**), sorted by **count of spans**; good for scanning latency by resource/group. Filter by type/name with buttons and text search. Sortable columns: **RESOURCE, SPANS, AVG DURATION, EXEC TIME, % EXEC TIME**.
- **Waterfall**: every span is a row on a timeline; good for isolating relevant parts. Each row: relative duration (bar length = **percentage of total trace duration**), absolute duration in ms, service + resource name, HTTP status code when applicable, color by service (default), host or container via **Color by** dropdown. Inferred-service spans have a **dashed underline**. Chevron (>) expands/collapses descendants; **Expand all (+)** / **Collapse all (-)**.
- **Map** (trace map): one node per service in this single trace; service-level transaction lifecycle and dependencies. To prevent cyclic dependencies, a service that calls a service already invoked by the original service is shown as a **duplicated node**. Inferred services: dashed outline + **purple background**. Nodes show **% of total execution time** per service. Service entry span in error -> node gets a **red border**; error in a **service exit span** -> the **edge** to the next service is red. Hover the error state for entry-span operation/resource/error message; **View Entry Span** switches to Waterfall.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#trace-visualizations

### Focus, Trace Preview, span search
- **Focus on a span** (Waterfall and Flame Graph only): narrows the view to the span and its children; visualization rescales with that span as the new root. Flame graph: select span, click focus icon next to the minimap. Waterfall: hover span, click focus icon on its right. Reset focus to return. Focus only changes the display; it does **not** filter search results or alter the trace.
- **Trace Preview**: when a trace exceeds **100MB** it cannot be fully visualized in the default side panel. Preview returns only critical spans: service entry spans, error spans, long-running spans, spans linked to other spans/traces. Only **Waterfall and Map** views available. In Waterfall, extra spans are grouped in **numbered pills** (click to expand).
- **Span search** (Waterfall and Flame Graph): matching spans highlighted; arrows navigate between matches. With the `Error` checkbox selected, results are matching spans in an error state.
  - Free text matches service, resource or operation name: `web`
  - Key-value: `service:web-ui`
  - Group: `language:(go OR python)`; Boolean: `service:event-query OR terminator`; Range: `duration:>200ms`; numerics support `<`, `>`, `<=`, `>=`.
  - **Wildcards are NOT supported** in the trace search bar.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#focus-on-a-span, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#trace-preview, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#span-search

### Span side panel ("More information") and its tabs
- Height-adjustable bottom of the Trace View. Span header: service, operation, resource names + latency; click a naming pill to pivot or narrow the Trace Explorer search. For client calls to a DB/queue/third party, the header shows the service and the **inferred entity**.
- On traces with errors: **Investigate With Bits AI** launches an automated investigation (walks span tree, correlates logs). In Trace Explorer, sorting by Duration offers Investigate With Bits AI for latency.
- **Span Info**: all span metadata incl. custom tags; click a tag to add to Trace Explorer query or copy value. Conditionally: error message + stack trace (error spans), SQL query markup (DB spans), RUM context (RUM spans), Spark metrics (Spark job spans), git warning (CI Test missing git info). When service is overridden: shows **Base service** (`@base_service` attribute), **Service override** (`service` reserved attribute) and **Inferred service** (from peer attributes / peer tags like `peer.db.name`).
- **Infrastructure**: toggle host-level vs container-level; tags + CPU, Memory, I/O graphs with overlay of when the trace occurred.
- **Logs**: logs related to the service at the time of the trace. Hover a log -> a line showing its timestamp appears on the flame graph. Click a log -> Log Explorer search. Correlation needs trace/span IDs injected into logs (`env`, `service`, `version` via `DD_ENV`, `DD_SERVICE`, `DD_VERSION`); logs must be JSON or parsed into attributes. Logs and traces are sampled independently.
- **Processes**: processes on the underlying host/pod at time of request (CPU, RSS memory); click -> Live Processes page. Requires **process collection** enabled. Not supported for **serverless and browser** traces.
- **Network**: network dependencies; volume, errors (**TCP retransmits**), latency (**TCP round-trip time**) to separate app vs network issues; click -> Network Analytics. Requires **Cloud Network Monitoring**. Not supported for serverless traces.
- **Security**: attack attempts targeting the trace's services (pattern, detection rule, whether a vulnerability was found); **View in AAP** -> App and API Protection.
- **Profiles**: code hotspots; values on left = time spent in each method during the selected span. Requires profiler + tracer in same process (auto-linked); Java manual spans need scope activation (`tracer.activateSpan(span)`); Python needs `DD_PROFILING_TIMELINE_ENABLED=true`; PHP `DD_PROFILING_TIMELINE_ENABLED=1`; Go `DD_PROFILING_EXECUTION_TRACE_ENABLED`. Span execution timeline view: lanes per thread (goroutine in Go). **Open in Profiling** -> Focus On: Span & Children, Span only, Span time period, Full profile (60 s of the process).
- **Span Links**: spans causally related without a parent-child relationship; click a span in the flame graph to see linked spans. Only displayed when the linked spans are **ingested and indexed** (e.g. via a retention filter).
- Metrics: the Runtime Metrics doc says runtime metrics show in "the flame graph Metrics tab" (need matching, case-sensitive `env` tag), though the Trace View page's tab list does not include a Metrics tab.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#more-information, https://docs.datadoghq.com/tracing/guide/service_overrides/, https://docs.datadoghq.com/profiler/connect_traces_and_profiles/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/, https://docs.datadoghq.com/tracing/metrics/runtime_metrics/

### Span links
- OpenTelemetry concept; supported for OTel SDKs and Datadog SDKs. Correlate spans **causally related but not parent-child**, within the same trace or **across traces**. Forward links (to a later span) and backward links (to an earlier span) both supported.
- Best for **fan-in**: Scatter-Gather / Map-Reduce, Message Aggregation (e.g. Kafka Streams), Transactional Messaging, Event Sourcing; batch and async processing.
- Datadog SDK API: Python, Node.js, Go, PHP. Java, .NET, Ruby: use the OpenTelemetry API (Datadog SDK sends them). OTel SDK links arrive via OTLP ingest.
- Minimums: Agent **v7.52.0+**; Go 1.61.0, Java 1.26.0, .NET 2.53.0, Node 5.3.0, PHP 0.97.0, Python 2.5.0, Ruby 2.0.0; C++/Proxy not supported.
- Viewed in the Trace View **Span Links** tab.

Sources: https://docs.datadoghq.com/tracing/trace_collection/span_links/, https://docs.datadoghq.com/tracing/trace_explorer/trace_view/#more-information

### Data availability pitfalls when opening a trace
- Live Search: all ingested spans, last 15 minutes rolling, unsampled. Indexed: custom retention filters 15 days; Intelligent retention filter 30 days.
- Selecting a span in Live Search pauses the stream and opens the trace side panel.
- Filter on non-facet attributes by clicking them in the trace details panel (e.g. `cart.value`).

Sources: https://docs.datadoghq.com/tracing/trace_explorer/

## Service Performance Dashboards

### Service Page: layout and out-of-the-box graphs
- Reached by selecting a service in the **Catalog** (formerly Service Catalog / Software Catalog; the docs now just say "Catalog"). A service = a set of processes that do the same job (web framework, database...).
- Sections: Service health, Service monitor, Watchdog Insights carousel, Summary cards (deployments, Error Tracking issues, SLOs, Incidents, security signals), Dependencies map, out-of-the-box graphs, Resources list, then tabs: Deployments, Error Tracking, Security, Databases, Infrastructure (Kubernetes), Runtime Metrics, Profiling, Memory Leaks, Traces, Log patterns, Costs, Frontend activity.
- Use the **dropdown above each graph** (click the graph title) to switch the view.
- **Requests and Errors** graph: total requests (hits) and errors over time. Dropdown: Requests by Version, Requests per Second by Version, Requests and Errors Per Second.
- **Errors** graph: total error count. Dropdown: Errors by Version, Errors per Second by Version, Errors per Second, **% Error Rate by Version**, % Error Rate. Use a percentage view (not a count) to compare a canary that takes a small share of traffic.
- **Latency** graph: latency percentiles as a timeseries. Dropdown: Latency by Version, **Historical Latency** (current latency distribution vs previous day and week), **Latency Distribution** (distribution over the selected time frame), Latency by Error (segmented by error vs non-error), **Apdex** (score over time; web services only).
- **Avg Time per Request** (4th graph, the "sub-services" breakdown): only for services with downstream services; average execution time spent per request in each downstream service. Dropdown: Total Time Spent, % of Time Spent. Built on **sampled trace data**; the other top graphs use **unsampled** data (trace metrics). Not shown for final operations like Postgres or Redis that call nothing.
- **Watchdog** runs automatic anomaly detection on the Requests, Latency and Errors graphs; an anomaly shows as an overlay, click the Watchdog icon for a side panel.
- Hover a latency spike → **Investigate With Bits AI** launches an automated investigation (tag divergence and bottlenecks across affected traces).
- **Export**: arrow / export icon at the upper-right corner of each graph exports it into a dashboard. (APM dashboard guide: Total Requests graph → `export` → `Export to Dashboard` → `New Timeboard` → `View Dashboard`; the exported widget is titled like "Hit/error count on service". Click the pencil icon on the dashboard widget to see the exact metrics used.)
- Service health: Critical if a non-muted paging (PagerDuty/Opsgenie) monitor is in `ALERT` and triggered in the `past 2 days`, an incident of any severity is active, a faulty deployment or an APM latency/error-rate Watchdog alert is ongoing. Warning: paging monitor in `WARN` within 2 days, incident stable, log anomaly ongoing. Shown in Catalog, service pages, dependency maps, service pills; also colors Service Map node borders (red/yellow).
- Monitors attach to a service when `service:<SERVICE_NAME>` is in metadata tags, in the query, or the query is grouped by service. Synthetic tests can be tagged `service:<SERVICE_NAME>` too.
- Dependencies (callout, most sites): map powered by APM metrics; groups dependencies by operation name; inferred services (databases, queues, third-party APIs) shown as **purple** nodes; service overrides shown on the edges.

Sources: https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/tracing/guide/apm_dashboard/

### Resources list and Resource Page
- Resource = a particular action of a service (endpoint, DB query, background job). For HTTP services with external interface, the list shows endpoints.
- Resources list on the service page: sort by requests, latency, errors or time. Configurable columns: Requests, Requests per second, Total time, Avg/p75/p90/p95/p99/Max Latency, Errors, Error Rate (no p50 column listed). Missing p99 column → cog icon **Change Columns** → flip the switch for `p99` (slowest-request guide).
- Click a resource → side panel (requests/errors/latency graphs, resource dependency map, span summary). Keyboard keys toggle between resources. **Open Full Page** opens the full resource page.
- Resource page has the same OOTB graphs (Requests and Errors, Errors, Latency, Avg Time per Request) + **Export to dashboard** (up arrow, upper-right) + a resource **latency distribution** graph with top-right percentile selectors (zoom into a percentile) and percentile markers on hover.
- **Dependency Map** (resource): flow graph of upstream and downstream dependencies scoped to requests through that service + resource; click a node, `set as start/end` to focus on a path. Based on a **sample of ingested spans**, request rates **upscaled** by sampling rates. Only available for **service-entry span** resources.
- **Frontend Impact**: requires RUM and a web-service resource; built on **indexed** trace data from the **past 1 hour**; columns RUM View Name, App Name, Sessions, Error Rate Per Sessions, P95 Latency, Requests; "Isolate this View", "View Traces".
- **Span summary** (only for resources containing service entry spans), per span: `Avg Spans/trace` (avg occurrences per trace where present), `% of Traces` (share of traces with the span at least once), `Avg Duration`, `Avg % Exec Time` (share of execution time while the span was active, i.e. not waiting on a child; active spans = leaf spans).
- Traces section: Trace search modal pre-filtered on env, service, operation and resource name. Endpoint resources get a **Definition** section.
- Slowest trace workflow: Catalog → service page → sort Resources by p99 → open slowest resource → time `1d One Day` → Traces table sorted by duration → View Trace → Host tab → Open Host Dashboard.

Sources: https://docs.datadoghq.com/tracing/services/resource_page/, https://docs.datadoghq.com/tracing/services/service_page/#resources, https://docs.datadoghq.com/tracing/guide/slowest_request_daily/

### Service Map
- Decomposes the application into services and draws observed dependencies in real time. Visualizes APM and RUM data; no setup required.
- Group by **team** or **application**. Filter with facets (service type, last deploy time, monitor status, incident status) or fuzzy name match. Scope by time range.
- Scoped by `env` and optionally a second primary tag; changing the scope draws a different map. (The page also says the map reveals a service's connections to services in other environments, e.g. `staging` - see ambiguity note.)
- Hover = animated request-direction lines. Click → **Inspect**: isolates the service with its callers and callees; services on the left are closer to customers, on the right more likely root causes. Node collapsed when two filtered services are connected through services outside the filter.
- `service` tag is special: links APM services to logs, infrastructure (Host Map) and custom metrics; monitors tagged by service in "Say what's happening" show their status on the map.
- Nodes = services as instrumented (match the Catalog); edges = aggregate calls. New services/connections appear within moments; age out after **30 days** with no traces; you can query nodes with data within the last 30 days; nodes only appear if they have data in the selected time frame.
- Node border colored red or yellow from **Service Health** (current docs; the old green/yellow/red/gray monitor-circle colors are no longer documented).
- Rendered from **complete traces including root spans**; dropped spans (APM connection errors) can make the map unavailable for a time window.
- Dashboard equivalent: **Topology Map widget** with the Service Map data source (callers point into the mapped service; mapped service points to its callees). Other data sources: Data Streams, Network Path.

Sources: https://docs.datadoghq.com/tracing/services/services_map/, https://docs.datadoghq.com/dashboards/widgets/topology_map/

### Trace metrics namespace
- Collected once trace collection is enabled; request counts, error counts, latency. Computed on **100% of the application's traffic**, regardless of ingestion sampling. Used for dashboards, monitors, SLOs. Retained **15 months** like any Datadog metric.
- Exceptions (metrics reflect only sampled traffic): application-side sampling (e.g. some Ruby SDK options, not recommended), **OpenTelemetry SDK-level sampling**, X-Ray sampling. With the OTel Collector, place the `span_metrics` connector **before** any sampling processor such as `tail_sampling` (Datadog Connector does the same in existing configs).
- Generated for service entry spans and some integration-specific operations (Django: root request span, each middleware, the view).
- Format: `trace.<SPAN_NAME>.<METRIC_SUFFIX>`; `<SPAN_NAME>` = operation name / `span.name` (e.g. `redis.command`, `pylons.request`, `rails.request`, `mysql.query`). Any metric starting with `trace.` is APM data.
- Tags: `env`, `service`, `version`, `resource`, `http.status_code`, `http.status_class`, `rpc.grpc.status_code` (Agent 7.65.0+), Agent host tags, additional primary tags. **Other span tags are NOT available on trace metrics.**
- `trace.<SPAN_NAME>.hits` COUNT, any service. `trace.<SPAN_NAME>.hits.by_http_status` COUNT, HTTP/web services when http metadata exists (adds `http.status_class`).
- `trace.<SPAN_NAME>` **DISTRIBUTION** - latency distribution; recommended for all latency use cases; tags also include `synthetics`.
- `trace.<SPAN_NAME>.errors` COUNT; `trace.<SPAN_NAME>.errors.by_http_status` COUNT.
- `trace.<SPAN_NAME>.apdex` **GAUGE**, HTTP/web services only.
- Legacy: `trace.<SPAN_NAME>.duration` GAUGE (total time of spans in an interval incl. children seen in the service; **no percentile aggregations**); avg latency with host-tag filters: `sum:trace.<SPAN_NAME>.duration{<FILTER>}.rollup(sum).fill(zero) / sum:trace.<SPAN_NAME>.hits{<FILTER>}.rollup(sum).fill(zero)`. `trace.<SPAN_NAME>.duration.by_http_status` GAUGE.
- Example widget (guide): metric `trace.rack.requests.errors`, from `service:web-store`, sum by `http.status_code`; add `runtime.ruby.thread_count` via "Graph additional: Metrics" to correlate latency with runtime metrics.
- Trace metrics are tagged by the host receiving traces; visible in the **Metrics Catalog** (e.g. `web.request` entry span). Exportable from Service/Resource page and queryable from dashboards; APM monitors can be created from New Monitors, Service or Resource page.
- Don't set different `env` on tracer and Agent (duplicate tagging on trace metrics). Additional primary tags: admin-only APM Settings, up to 100 unique values, up to 2 hours to apply, must be host/container tags.

Sources: https://docs.datadoghq.com/tracing/metrics/metrics_namespace/, https://docs.datadoghq.com/glossary/, https://docs.datadoghq.com/tracing/guide/apm_dashboard/, https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/

### DDSketch distribution metrics and percentiles
- Single metric `trace.<SPAN_NAME>` (DISTRIBUTION) replaces per-percentile and per-tag-combination metrics; service and resource pages use it automatically.
- Datadog stitches queries on the new metric to the equivalent older latency metrics so full history shows.
- DDSketch = **relative-error** guarantees (previously rank-error) → percentiles closer to true values; most visible as a reduction in p99. Calculated on the backend, so not identical to an in-code custom distribution metric.
- Terraform migration: `avg:trace.http.request.duration.by.resource_service.99p{service:foo, resource:abcdef1234}` → `p99:trace.http.request{service:foo, resource:abcdef1234}`; `...75p` → `p75:`; p100 `avg:...100p{}` → `max:trace.http.request{...}`. Old metrics still exist; Terraform keeps working.
- Distributions in general: aggregated server-side as DDSketch; percentiles p50, p75, p90, p95, p99 (and custom percentiles up to two decimals for custom distributions after enabling in the Metrics Catalog); threshold queries ("count values...") usable for SLOs.

Sources: https://docs.datadoghq.com/tracing/guide/ddsketch_trace_metrics/, https://docs.datadoghq.com/metrics/distributions/

### Apdex
- Apdex = open standard user-satisfaction score on [0;1] (0 none satisfied, 1 all satisfied) based on response time; counterbalances averages/percentiles skewed by extremes.
- Threshold **T**: Satisfied < T; Tolerated >= T and <= 4T; Frustrated > 4T **or error**. Apdex = (Satisfied + Tolerated/2) / Total.
- Set **per service by an administrator** before scores are calculated: Catalog → web service → Service Page → click Latency graph title → **Apdex** (web services only) → pencil icon top-left (admins only) → enter threshold → save.
- Show Apdex in the Catalog via the configuration menu (upper right); Catalog Performance view compares latency, traffic, error rate and Apdex by environment.
- Metric `trace.<SPAN_NAME>.apdex` (GAUGE, web services).

Sources: https://docs.datadoghq.com/tracing/guide/configure_an_apdex_for_your_traces_with_datadog_apm/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/#apdex

### Primary operation
- Service-level trace metrics (errors, throughput, latency) are computed from resources matching a single span name = **primary operation**; used by the Service Page, Catalog and Service Map.
- Backend auto-selects the entry-point operation by **highest request throughput**. Examples: web `servlet.request`, `flask.request`, `web.request`; db `postgres.query`, `db.query`; custom `trace.annotation`, `method.call`.
- Override (admin): **APM settings** page → **Primary Operation Name** tab → edit icon → **Set Manually** → select operation → Save.
- Other span names = secondary operations, viewable via a dropdown on the resources list, but **not used for service-level statistics**.
- Custom spans: set the span name statically (e.g. `web.request`) and put dynamic values in the resource (e.g. `/user/profile`). OpenTracing: operation name = resource; "component" tag = span name.
- Endpoints missing from a service page: endpoints are linked to a service by service name *and* the entry-point span's `span.name`.

Sources: https://docs.datadoghq.com/tracing/guide/configuring-primary-operation/, https://docs.datadoghq.com/tracing/glossary/

### Getting APM graphs onto dashboards (copy/paste, export, widgets)
- Copy a widget on Dashboards, Notebooks, the **APM Service page** and **APM Resource page** with `Ctrl`/`Cmd` + `C` (hover the graph) or share icon → **Copy**. Paste with `Ctrl`/`Cmd` + `V`: in a **dashboard** → new widget under the mouse cursor; in a **notebook** → new cell at the end.
- Pasting into Slack/Microsoft Teams shows a preview + link depending on **Widget Share URLs** (admin sets Public or Private in Organization Settings; can disable).
- Timeboard group: hover group, `Ctrl`/`Cmd` + `C`; pasted into a screenboard/notebook, widgets are pasted individually. Multiple screenboard widgets: edit mode, `Shift` + click, `Ctrl`/`Cmd` + `C`.
- **Datadog Clipboard**: personal; open via "Open Clipboard" popup after a copy or `Cmd/Ctrl + Shift + K`; holds max **20** signals, oldest (left-most) removed automatically; does not copy query text/JSON; export clips to Dashboards, Notebooks or Incidents; "Add current page" adds a URL.
- Widget export menu: Copy, Share snapshot; Declare incident, Add to incident, Create case, Save to notebook, Link to widget; Download as PNG/SVG/CSV. Three-dot menu: Edit, Clone (adjacent copy), Split graph, Create custom links, Create monitor, Metrics info, Delete. Full screen: export to dashboard/notebook or copy query, download CSV.
- **Service Summary widget**: shows a chosen service's service-page graphs on a dashboard. Configure env + service, widget size, information (Hits, Errors, Latency, Breakdown, Distribution, Resource - **Resource requires the large size**), number of columns (`one_column`/`two_column`/`three_column`), title. API type `trace_service`.
- Manual widget: Add Widget → Timeseries → choose `trace.*` metric, `from` scope, `sum by`. Template variables: **Add Variable** in header, choose tag (e.g. `Region`), then values update all applicable widgets. Search Events or Logs overlay to correlate deployments.
- Full-screen timeseries **Compare Time** tab: Previous period = Period, Day, Week, Month or Custom; Overlay vs Grid. Week-over-week guide: keep only p50 in the latency legend, expand, check `Week` in "Compare to Last".
- Dashboard widgets for APM: Timeseries (latency, error rate, throughput), Service Summary, Topology Map; Top List, Query Value etc.

Sources: https://docs.datadoghq.com/dashboards/widgets/configuration/#copy-and-paste-widgets, https://docs.datadoghq.com/dashboards/guide/datadog_clipboard/, https://docs.datadoghq.com/dashboards/widgets/service_summary/, https://docs.datadoghq.com/tracing/guide/apm_dashboard/, https://docs.datadoghq.com/dashboards/widgets/timeseries/#compare-time, https://docs.datadoghq.com/tracing/guide/week_over_week_p50_comparison/

### Find correlated metrics, Watchdog Explains and graph insights
- **Graph Insights** = Metric Correlations + Watchdog Explains + dashboard anomaly detection; all for Timeseries widgets with the **Metric** data source.
- **Metric Correlations** ("Find correlated metrics"): finds other metrics with irregular behavior at the same time. Start from dashboards, notebooks, APM, Watchdog alerts or monitor status pages: **left click any graph → Find correlated metrics**, or full-screen graph → **Correlations** tab. Auto-detects the area of interest; adjust via Edit Search / click-drag.
  - Single metric only: for multi-metric graphs open full screen, select one series in the legend, then Correlations tab.
  - Sources: APM services, integrations, dashboards, custom metrics. **Custom metrics is the only category not selected by default** (at least one namespace/metric must be chosen). Tag filter box scopes the search. Results: Type, Source, Correlations (count), Preview. Export icon → dashboard, notebook, or copy query.
- **Watchdog Explains** (old URL dashboards/correlations now redirects here): detects anomalies on timeseries (avg, sum, min, max aggregations), highlights them with a **pink box** → **Investigate Anomaly** opens full-screen view with tag groups that contributed; click a tag to remove/isolate it. Seasonality: looks back up to **three weeks** (e.g. previous Mondays at 9:00). Disable on a dashboard: **Anomalies** → **Turn Off**; affects only your own view.
- Dashboard anomaly detection groups co-occurring anomalies into issues; can delegate root cause analysis to Bits Investigation.
- Related: from the dashboard guide, related events via **Search Events or Logs**; anomaly monitor for p99 database latency (APM monitor, Anomaly Alert, "Alert when" 100%).

Sources: https://docs.datadoghq.com/dashboards/graph_insights/, https://docs.datadoghq.com/dashboards/graph_insights/correlations/, https://docs.datadoghq.com/dashboards/graph_insights/watchdog_explains/, https://docs.datadoghq.com/tracing/guide/alert_anomalies_p99_database/

### Common pitfalls
- "Avg Time per Request" is sampled; Requests/Errors/Latency are unsampled trace metrics (except OTel SDK, app-side or X-Ray sampling).
- Custom span tags cannot group trace metrics; use additional primary tags (host/container tags) instead.
- `.duration` cannot give percentiles; use `p95:trace.<SPAN_NAME>{...}`; p100 → `max:`.
- Apdex absent for non-web services; pencil icon only for admins.
- Resource dependency map and span summary need service-entry span resources.
- Correlation search works on one series at a time; custom metrics must be selected explicitly.

Sources: https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/

# Domain 4: Troubleshooting Application using APM

## Using Trace Search (during incident)

Typical incident workflow: spot a spike on the service page (or a dashboard / monitor) -> pivot to the traces behind the graph -> filter the Trace Explorer (`status:error`, `@http.status_code`, `resource_name`, `version`) -> open a trace and find the slow or failing span in the Trace View -> check correlated logs, host/container metrics, processes, network, profiles, RUM session or Synthetic test -> when resolved, write the postmortem in a notebook (trace metrics + retained spans).

### 1. Spotting the spike on the service page
- Service page = select a service in the **Catalog** (Software Catalog; formerly Service Catalog). Sections: Service health, Service monitors, Watchdog Insights carousel, summary cards, out-of-the-box graphs, Resources, dependency map, and tabs (Deployments, Error Tracking, Security, Databases, Infrastructure, Runtime Metrics, Profiling, Memory Leaks, Traces, Log patterns, Costs, Frontend activity).
- **Service health** = Critical / Warning / Ok, combining monitors, incidents and Watchdog Insights.
  - Critical: non-muted monitor with a paging integration (PagerDuty or Opsgenie) in `ALERT` and triggered within the past 2 days; an active incident of any severity; an ongoing faulty deployment; an ongoing APM latency/error-rate Watchdog alert.
  - Warning: non-muted warning monitor with paging integration in `WARN` within past 2 days; a stable incident; an ongoing log anomaly alert.
- Monitors attach to a service if `service:<SERVICE_NAME>` is in the monitor tags/metadata, in the query, or the query is grouped by service. Synthetic tests attach when tagged `service:<SERVICE_NAME>`.
- OOTB graphs: **Requests and Errors** (dropdown: Requests by Version, Requests per Second by Version, Requests and Errors Per Second), **Errors** (Errors by Version, Errors per Second by Version, Errors per Second, % Error Rate by Version, % Error Rate), **Latency** (Latency by Version, Historical Latency vs previous day/week, Latency Distribution, Latency by Error, Apdex), **Avg Time per Request** (downstream breakdown; built on *sampled* trace data, unlike the other top graphs which use unsampled data). No sub-services graph for terminal services like Postgres/Redis.
- **Watchdog** runs automatic anomaly detection on the Requests, Latency and Error graphs; if an anomaly is found an **overlay** appears on the graph; click the Watchdog icon for a side panel.
- Hover a latency spike -> **Investigate With Bits AI** (automated investigation of tag divergence and bottlenecks).
- Export a graph: arrow icon top-right of each graph -> export to a pre-existing dashboard (official exam example also mentions hover + Ctrl/Cmd+C to copy a graph).
- Resources list: sort by requests, latency, errors, total time; columns include Requests, Requests per second, Total time, Avg/p75/p90/p95/p99/Max latency, Errors, Error Rate. Click a resource -> side panel (graphs, resource dependency map, span summary); **Open Full Page** for the resource page. Guide "slowest trace": sort Resources by p99 (enable via cog / Change Columns), set time to `1d`, sort Traces table by duration, **View Trace**, then the Host tab and **Open Host Dashboard**.
- **Traces tab** on the service page: list of traces already filtered on the service, environment and operation name; drill down with core facets (status, resource, error type).
- **Deployments** tab (needs `version` tag): versions active in the time frame, first/last seen, **Error Types** indicator (error types not seen in the previous version - does not prove the version introduced them), requests/s, error rate.

Sources: https://docs.datadoghq.com/tracing/services/service_page/, https://docs.datadoghq.com/tracing/guide/slowest_request_daily/

### 2. Pivoting from a graph to traces (dashboards, notebooks)
- Clicking a dashboard widget opens the context menu with **default context links**: Hosts (Host Map if several hosts, Host Dashboard if one), Containers (Live Containers), Processes (Live Processes), **APM Traces** (opens a side panel with the underlying traces, linking to the Trace Explorer), RUM Events, Profiles, **Logs** (side panel with underlying logs linking to the Log Explorer). "More Related Data Actions" shows more.
- Context links embed a **filter** (widget filters + template variables + the clicked series for grouped queries) and a **time range**: for timeseries and heatmap widgets the time range is the **time bucket of the clicked data point**; for other widgets it is the full widget time range.
- Custom context links: variables `{{timestamp_start}}`, `{{timestamp_end}}`, query variables (`{{@MerchantTier.value}}`), template variables (`{{$env.value}}`).
- Widget export menu: Copy, Share snapshot; "Use within Datadog": **Declare incident**, **Add to incident**, Create case, **Save to notebook**, Link to widget; share externally: PNG / SVG / CSV. Context menu (three dots): Edit, Clone, Split graph, Create custom links, **Create monitor**, Metrics info, Delete.
- Trace metrics on dashboards: any metric starting with `trace.` is APM data (for example `trace.rack.requests.errors`, `trace.rack.request.duration.by.service.99p`); correlate with `runtime.*` metrics (e.g. thread count) and infrastructure metrics on the same widget; export Trace Explorer (Analytics) timeseries to a dashboard.

Sources: https://docs.datadoghq.com/dashboards/guide/context-links/, https://docs.datadoghq.com/dashboards/widgets/configuration/, https://docs.datadoghq.com/tracing/guide/apm_dashboard/

### 3. Trace Explorer during an incident (Live vs indexed, filters)
- **Live Search** (default view): all ingested spans for the last **15 minutes** (rolling), unsampled, any span and any tag. Indicator "Live Search - All ingested data". Pause/Play button freezes the stream; selecting a span pauses it. Option to show only **service entry spans**, **root spans**, or all spans.
- **Indexed search**: change the time selector to any period > 15 minutes. Indicator "Search - Only Indexed Data". Custom retention filters keep spans **15 days**; the Intelligent retention filter keeps them **30 days**. Searching a tag that only appears on non-indexed spans returns nothing.
- Live timeseries: group by only **one** dimension (indexed: up to three). Export to dashboards/monitors only from retained spans. Indexed timeseries -> export to dashboard, monitor or **notebook**.
- Spans retained by the intelligent filter are excluded from trace analytics **monitor** evaluations; monitors use custom retention filter spans only, while dashboards and notebooks use custom + intelligent filter spans.
- Query syntax: span attributes need `@` (`@http.status_code:[500 TO 599]`, `@http.response_time:>100`); reserved attributes without `@`: `env`, `operation_name`, `resource_name`, `service`, `status`, `span_id`, `timestamp`, `trace_id`, `type`, `link`; span tags (host, container, `version`, `availability-zone`) without `@`. Operators `AND` (default), `OR`, `-`. Wildcard `service:web*`. Non-standard tags: `tags:"..."`. Escape `? > < : = " ~ / \` and spaces (`@user.first\ name:myvalue`).
- Incident queries: `service:checkout status:error`, `status:error @http.status_code:[500 TO 599]`, `resource_name:"POST /pay"`, `version:2.4.1`, `env:prod`.
- Filter on attributes that are not facets by clicking the attribute in the trace panel or typing its name.
- Visualizations: List, Timeseries, Top list (e.g. top customers hit by errors), Table (up to 3 dimensions), Request Flow Map. List view: when filtered on error spans, **Group into Issues** shows Error Tracking issues; `See all errors` returns to spans. `Latency Breakdown` may be missing for incomplete traces (error and rare samplers capture partial traces).
- Trace Groups: group by up to 4 dimensions; from Span (default), `parent(a)` or `root`; metrics REQUESTS, ERRORS, P95 Latency.
- Sort the list by **Duration** -> **Investigate With Bits AI** for an automated latency investigation.
- Trace Patterns (Preview) group spans with similar structure.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/, https://docs.datadoghq.com/tracing/trace_explorer/visualize/, https://docs.datadoghq.com/tracing/troubleshooting/#trace-retention

### 4. Watchdog insights in the Trace Explorer
- Two insight types: **Anomalies** (pre-calculated Watchdog alerts matching the query; full list in the Watchdog Alert explorer) and **Outliers** (tags that appear too often in errors or push latency up; calculated dynamically on the current query and time frame).
- APM outliers appear in the Trace Explorer, Service page and Resource page. In the Trace Explorer they are integrated with Tag Analysis:
  - search bar suggestions with an indicator for error or latency correlation;
  - group-by recommendations highlight outlier facets;
  - **"OUTLIERS" section** at the top of the facets sidebar;
  - the **Analyze** button next to the RED metrics (error and latency graphs) is highlighted.
- **Error outliers**: statistically over-represented `key:value` pairs among errors (examples `env:staging`, `availability_zone:us-east-1a`, `cluster_name:chinook`, `version:v123456`). Card: field name + proportion of errors vs overall traces. Side panel: timeseries of error traces with the field, associated tags, related Error Tracking issues and failing spans.
- **Latency outliers**: computed on span duration; card shows the latency distribution vs baseline; side panel X axis p50, p75, p99, max.
- **Filter on Insight** (inverted triangle icon on the card): narrows the explorer to the insight; the outlier then disappears because the filtered scope becomes the baseline.
- Outlier links (Copy Link) expire with the retention of the underlying data.
- Watchdog Explains (graph insights) answers "what is the source of the spike?" on latency/error/request graphs.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/#analyzing-anomalies-with-integrated-insights, https://docs.datadoghq.com/watchdog/insights/

### 5. Trace View: finding the slow or failing span
- Trace header: root span service, resource, trace ID, end-to-end duration, start time. **Open Full Page** = permalink.
- Visualizations: **Flame Graph** (default), **Span List**, **Waterfall**, **Map**.
  - Flame Graph: legend groups by Service (default), Base service, Host or Container; show **% Exec Time** or **Spans**; tick **Errors** under **Filter Spans** to highlight error spans. Inferred services: dashed outline.
  - Span List: resources grouped (service by default), sorted by span count; columns RESOURCE, SPANS, AVG DURATION, EXEC TIME, % EXEC TIME.
  - Waterfall: one row per span, relative and absolute duration (ms), service + resource, HTTP status code, Color by service (default)/host/container; Expand all (+) / Collapse all (-).
  - Map: one node per service; duplicated nodes avoid cycles; % of execution time per node; **red border** = the service's **entry span** is in error; **red edge** = error in a service **exit** span; hover -> View Entry Span (switches to Waterfall). Inferred services: dashed outline + purple background.
- **Focus on a span** (Flame Graph and Waterfall): rescales the view with that span as root; display only, does not filter search results.
- **Trace Preview**: traces > **100MB** cannot be fully shown; Preview mode returns service entry spans, error spans, long-running spans, and spans linked to other spans/traces. Only **Waterfall** and **Map** are available; numbered pills fetch hidden span groups.
- **Span search** in the trace (Waterfall / Flame Graph): free text (service, resource, operation), `key:value` (`service:web-ui`), group `language:(go OR python)`, boolean `service:event-query OR terminator`, range `duration:>200ms` (`<`, `>`, `<=`, `>=`). **Wildcards are NOT supported.** With the `Error` checkbox selected only matching error spans are returned.
- On traces with errors: **Investigate With Bits AI** in the trace detail panel walks the span tree and correlates with logs.
- Span detail tabs:
  - **Span Info**: all metadata/custom tags (click a tag to add it to the search or copy it); error message + stack trace on error spans; SQL markup; RUM context; base service / service override / inferred service.
  - **Infrastructure**: host-level or container-level tags and CPU, Memory, I/O graphs with an overlay of when the trace occurred.
  - **Logs**: logs related to the service at the time of the trace; hovering a log draws its timestamp on the flame graph; clicking opens the Log Explorer.
  - **Processes**: processes on the underlying host/pod (CPU, RSS); needs **process collection**; not for serverless and browser traces.
  - **Network**: network dependencies, volume, TCP retransmits (errors), TCP RTT (latency); needs **Cloud Network Monitoring**; not for serverless traces.
  - **Security**: attack attempts; View in AAP.
  - **Profiles**: code hotspots (time per method during the span).
  - **Span Links**: only shown when the linked spans are ingested and indexed.
- "Missing error message and stack trace" on an error span: either an unhandled exception, or an HTTP status 400-599; exceptions handled in try/catch do not populate `error.message`, `error.type`, `error.stack` -> use custom instrumentation to set them.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/trace_view/, https://docs.datadoghq.com/tracing/troubleshooting/

### 6. Correlated logs (trace_id / span_id injection, DD_LOGS_INJECTION)
- Correlation injects trace ID, span ID, `env`, `service`, `version` into logs. Configure the tracer with `DD_ENV`, `DD_SERVICE`, `DD_VERSION` (unified service tagging).
- Logs must be sent as **JSON** or parsed by the language log integration pipeline; language-level log attributes must become Datadog attributes.
- Trace panel Logs section has four options: `trace_id` (logs with that trace ID), `host`, `container_id`, `pod_name` (logs from that host/container/pod in the trace's time frame).
  - Empty for host/container/pod: check logs are sent from that host/container/pod, exist in the time frame, and have a correct timestamp.
  - Empty for `trace_id`: logs lack a standard `trace_id` attribute -> extract the trace ID into an attribute and remap it to the reserved `trace_id`.
    - JSON logs: automatic (tracer injects, reserved attribute remappers remap). If not, ensure the attribute is `dd.trace_id` and check the **Trace Id** section of **Preprocessing for JSON logs** (reserved attributes).
    - With a log integration: set `source` to the language (`java`, `python`, `ruby`...); clone the pipeline if the format is not recognised.
    - Custom parsing: extract trace and span IDs **as strings**, then add a **Trace remapper** on the attribute.
- Trace remapper processor (`type: trace-id-remapper`): `sources` default `dd.trace_id`; `is_enabled` default `false`. Trace IDs and span IDs are not displayed as log attributes in the UI.
- Traces and logs are **sampled independently**: a log can carry a trace ID whose trace was not ingested/retained (log side panel says the trace is missing); not a configuration error.
- IDs: SDKs generate 128-bit trace IDs and 64-bit span IDs by default; Datadog accepts 128- or 64-bit trace IDs; `DD_TRACE_128_BIT_TRACEID_GENERATION_ENABLED=false` for 64-bit.
- Python: `ddtrace-run` or `import ddtrace.auto` enables the logging integration; for library injection on older `ddtrace<3.11` set `DD_LOGS_INJECTION=true`. Log format must include `dd.env`, `dd.service`, `dd.version`, `dd.trace_id`, `dd.span_id`. `ddtrace.trace.tracer.log_correlation` for non-stdlib loggers (e.g. structlog processor).
- Java: since tracer **0.74.0** automatic injection into **JSON** logs; older versions: `-Ddd.logs.injection=true` or `DD_LOGS_INJECTION=true`. Log4j2, Log4j, SLF4J/Logback. Since 1.18.3 with Remote Configuration, `DD_LOGS_INJECTION` can be set in the Catalog UI. Manual: OpenTelemetry API (recommended) or `CorrelationIdentifier.getTraceId()/getSpanId()` (return `"0"` without an active span).
- Node.js: automatic injection for `bunyan`, `pino`, `winston`; only works for **JSON**-formatted logs; older tracers: `DD_LOGS_INJECTION=true` or `logInjection` in `init()`; init the tracer before importing the logger.
- Go: manual (span context with `%v`) or the logrus hook (`dd_logrus`); custom parsing must keep `dd.trace_id`, `dd.span_id`, `dd.service`, `dd.env`, `dd.version` as strings.
- Ruby: Rails with `ActiveSupport::TaggedLogging` (default), `semantic_logger` or `lograge` is automatic (disable TaggedLogging with lograge); add a trace remapper. Manual: `Datadog::Tracing.log_correlation`.
- PHP: automatic since **1.12.0** (older: `DD_LOGS_INJECTION` / INI `datadog.logs_injection`); PSR-3 loggers (Monolog, Laminas). Default adds IDs to the log context; or placeholders `%dd.trace_id%`, `%dd.span_id%`, `%dd.service%`, `%dd.version%`, `%dd.env%` (case-sensitive; brackets needed for the default pipeline). Monolog v3 JSON with `extra.dd.trace_id` -> add `extra.dd.trace_id` to the **Trace Id Attributes** field in Preprocessing for JSON logs.

Sources: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/, https://docs.datadoghq.com/tracing/troubleshooting/correlated-logs-not-showing-up-in-the-trace-id-panel/, https://docs.datadoghq.com/logs/log_configuration/processors/trace_remapper/, https://docs.datadoghq.com/logs/troubleshooting/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/java/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/nodejs/, https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/php/, https://docs.datadoghq.com/tracing/guide/span_and_trace_id_format/

### 7. RUM and traces
- Links frontend RUM resources (XHR/Fetch, native requests) to backend traces. Prereqs: APM on the target services, HTTP server, distributed-tracing-capable library; Browser SDK `allowedTracingUrls`, Mobile SDK `firstPartyHosts`. Uses APM paid data (may affect APM billing).
- Browser: set `allowedTracingUrls` (first-party origins your browser app calls) and the `service` field. Match types: `string` (URL **starts with** the value), `RegExp` (matches any substring - anchor with `^`), `function` (returns `true`). Over-broad patterns can cause CORS errors.
- `traceSampleRate`: share of backend traces kept (default 100%); does not affect RUM session sampling. `traceContextInjection`: `sampled` (default; unsampled requests get no decision so the backend head-based sampling decides) or `all`.
- End-to-end tracing only for requests after SDK init; not the initial HTML document.
- Default propagators: `tracecontext` + `datadog`; others `b3`, `b3multi` via `{ match, propagatorTypes }`.
- Headers: `x-datadog-trace-id`, `x-datadog-parent-id`, `x-datadog-origin: rum`, `x-datadog-sampling-priority` (1 sampled / 0 not); W3C `traceparent` (00-<128-bit trace id>-<64-bit parent>-01/00) and `tracestate: dd=s:..;o:..`.
- Headers are **not CORS-safelisted**: the server must return `Access-Control-Allow-Headers` and accept **preflight (OPTIONS)** requests.
- Mobile SDKs (Android, iOS, React Native, Flutter, KMP): all subdomains of the listed first-party hosts are traced by default.
- Verify: request headers in the browser; RUM Explorer query `@_dd.trace_id:*` for resources with traces; session panel shows request duration breakdown, span flame graph and **View Trace in APM**.
- From a trace to RUM: in the trace view click **VIEW** (all traces during the view) or **RESOURCE**, then **See View in RUM** / **See Resource in RUM**.
- Retention: ingested traces available 15 min in Live Search; create retention filters to keep longer. With RUM Without Limits, cross-product retention filters keep traces of chosen sessions; by default 1% of RUM sessions and their traces are retained at no extra cost.

Sources: https://docs.datadoghq.com/tracing/other_telemetry/rum/

### 8. Synthetic tests and traces
- Available for HTTP API tests, Multistep API tests and Browser tests. Prereqs: endpoint traced in APM, HTTP server, distributed-tracing library. API tests: link is automatic. Browser tests: allow the URLs in **Synthetic Settings** (Integrations) to add APM headers.
- Wildcards in allowed URLs: in the domain `*` matches one label (no dots); in the path `*` matches anything including `/` (`https://*.datadoghq.com/*` allows `www.datadoghq.com/...` but not `www.docs.datadoghq.com/...`).
- Headers: `x-datadog-trace-id` (generated by Synthetics backend, links trace to result), `x-datadog-parent-id: 0` (test is the root span), `x-datadog-origin: synthetics` (API tests; spans tagged `ingestion_reason:synthetics`), `x-datadog-origin: synthetics-browser` (browser tests; `ingestion_reason:synthetics-browser`), `x-datadog-sampling-priority: 1` (Agent keeps the trace). W3C `traceparent` also supported.
- These traces are retained **15 days** by the **Synthetics Default** retention filter. Synthetic test results: 15 months.

Sources: https://docs.datadoghq.com/tracing/other_telemetry/synthetics/, https://docs.datadoghq.com/data_security/data_retention_periods/

### 9. Notebooks for postmortems
- Notebooks: collaborative rich-text documents with live graphs, for investigations, postmortems, runbooks. Create: **Dashboards > New Notebook**, or **New Notebook** on the Notebooks List page.
- **Template Gallery**: Incident Response **postmortem**, Incident Report, SLO Specification; custom templates possible.
- Type tags: Postmortem, Runbook, Investigation, Documentation, Report; up to 5 teams; favorites.
- Slash commands (`/`) to insert graphs; graph editor -> Save. Images: PNG/JPG/JPEG/GIF, max 4MB. Comments, @mentions, real-time multiplayer (widgets last-write-wins).
- Time: graphs linked to the notebook global time by default; drag-zoom changes global time; **Set Default Time**; individual graphs can be unlinked from global time.
- **Graph snapshots**: graphs with a **fixed time range** are automatically snapshotted to preserve the view before data retention limits apply; switching to a relative global time (e.g. `Past 1 hour`) removes the snapshot; a graph past its retention shows the inline snapshot.
- Modes: Editing / Viewing. Version history (preview, restore, clone). Permissions: default full access; Share > Private to me or Custom. Download as PDF (UI only, one notebook at a time).
- Data for a postmortem: `trace.*` trace metrics are computed on **100%** of traffic regardless of ingestion sampling (metrics kept 15 months) - the official example says the postmortem notebook uses trace metrics; custom span-based metrics only reflect ingested spans; indexed spans in notebooks/dashboards come from custom retention filters + the intelligent filter (15 / 30 days); export Trace Explorer timeseries to a notebook; dashboards widgets have **Save to notebook**.
- Data retention: APM indexed spans 15 or 30 days; services/resources statistics 30 days; viewed traces kept for the account lifetime; dashboards, notebooks, monitors kept for the account lifetime; metrics 15 months.

Sources: https://docs.datadoghq.com/notebooks/, https://docs.datadoghq.com/tracing/troubleshooting/#trace-metrics, https://docs.datadoghq.com/data_security/data_retention_periods/

### 10. Tracer troubleshooting when traces are missing
- Components: SDK -> Agent (port **8126**) -> Datadog. Check connection errors in **startup logs** or **debug logs** (with the application logs).
- Typical errors: `Failed to connect to localhost/127.0.0.1:8126`, `Agent not reachable at http://localhost:8126`, `ECONNREFUSED 127.0.0.1:8126`, Go `lost 1 traces ... connection refused`. .NET managed logs show connection-refused errors even without debug mode.
- **Java diagnostic CLI** (0.82.0+), run where `dd-java-agent.jar` is (inside the app container): `java -jar /path/to/dd-java-agent.jar sampleTrace -c 1`.
- Agent side: `agent status` (Agent 6.20/7.20+) APM Agent section: `Status: Running`, `Receiver: 0.0.0.0:8126`, or `Not running or unreachable on localhost:8126`. On Linux, Agent 7.80.0+ starts the trace-agent only after receiving trace data (socket activation) - disable with `apm_config.socket_activation.enabled: false` / `DD_APM_SOCKET_ACTIVATION_ENABLED=false`. Kubernetes with dedicated containers: exec into the trace-agent container.
- Host-based: SDK should send to `localhost:8126`/`127.0.0.1:8126`; check port conflicts on 8126.
- Containers: `localhost` is usually wrong (exceptions: **ECS on Fargate**, **EKS on Fargate** - do not set `DD_AGENT_HOST`). Test from the **application container**: `curl -X GET http://{agent_ip}:{agent_port}/info`. `DD_AGENT_HOST`: ECS on EC2 -> EC2 metadata endpoint; Elastic Beanstalk single container -> gateway IP (usually `172.17.0.1`); multi-container -> link to the Agent container name; Kubernetes/EKS -> Unix Domain Socket, `status.hostIP`, or Admission Controller; Docker -> Agent container. If `agent_url` in startup logs differs from `DD_AGENT_HOST`, check env var cascading (PHP Apache/Nginx).
- **Startup logs**: `DATADOG TRACER CONFIGURATION` (JSON; `agent_error` key where a connectivity check runs), `DATADOG TRACER DIAGNOSTICS`, `DATADOG ERROR`. Java has no diagnostics lines (use debug mode). Node.js 2.x+ disabled by default: `DD_TRACE_STARTUP_LOGS=true`. Python: config at INFO, diagnostics at ERROR; without logging config only diagnostics to stderr. PHP: `phpinfo()` or `php --ri=ddtrace`. Log level must be at least INFO.
- **Debug mode**: `DD_TRACE_DEBUG=true` (off by default; not recommended in production). Java `-Ddd.trace.debug=true` (SLF4J SimpleLogger; `DD_LOG_FORMAT_JSON` since 1.58.0). Python: `DD_TRACE_LOG_FILE` (relative to cwd), default file size 15728640 bytes (~15MB) + one backup, `DD_TRACE_LOG_FILE_SIZE_BYTES`; root logger at DEBUG also enables ddtrace debug logs -> `DD_TRACE_LOG_LEVEL` (v4.4.0+) or override the `ddtrace` logger. Go: `tracer.WithDebugMode(true)`; abandoned spans `DD_TRACE_DEBUG_ABANDONED_SPANS=true`, timeout `DD_TRACE_ABANDONED_SPAN_TIMEOUT` default `10m`. Node: `Response from the Agent: OK` = tracer fine; `Error from the Agent` = network/Agent issue; neither = tracer not instrumenting. .NET: also `GlobalSettings.SetDebugEnabled(true)`; logs in `/var/log/datadog/dotnet/` (Linux; create the directory first), `%ProgramData%\Datadog .NET Tracer\logs\` (Windows), `/datadog-lib/logs` (K8s library injection); `DD_TRACE_LOG_DIRECTORY`; `DD_TRACE_LOGFILE_RETENTION_DAYS` default 32. PHP: `DD_TRACE_LOG_FILE` / `datadog.trace.log_file` (0.98.0+), else PHP error_log.
- **Automated debug log collection (tracer flare)**: Java 1.26.0+, Python 3.12.0+, Node.js 5.15.0+/4.39.0+, .NET 2.46.0+; needs Remote Configuration; Fleet Automation > Agent > Support > Send Support Ticket > enable Debug mode + application tracer logs. Not on US1-FED/gov sites. If the service isn't listed there is likely an app-Agent connection error -> collect logs manually.
- Support ticket: trace links/screenshots, SDK startup logs, SDK debug logs, **Agent flare** (does not help if traces never reach the Agent), environment description, custom tracing code, versions.
- **SDK Configurations** view: Service Page > **Service Config > SDK & Agent Configurations**; shows active config per instance and source (Remote Configuration at Runtime, Code, Remote Fleet Automation, Local environment variable, Local file, Default). Missing if no instance active in the last 15 minutes, telemetry disabled, intake unreachable, or service override on spans.
- Other: one service shown as several (`service:test-mongodb`) -> inferred services or `DD_SERVICE_MAPPING` / `DD_TRACE_SERVICE_MAPPING` (.NET; Ruby supports neither). Data volume guidelines: spans accepted up to 18 h in the past / 2 h in the future; per 40-min interval 5000 env+service combinations, 100 operation names per env+service, 1000 resources per env+service+operation, 30 versions per env+service; resource truncated at 5000 chars, service/operation/type 100; max 1024 span tags. Usage spikes: `datadog.estimated_usage.apm.ingested_spans` / `indexed_spans`.

Sources: https://docs.datadoghq.com/tracing/troubleshooting/, https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/, https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/, https://docs.datadoghq.com/tracing/troubleshooting/tracer_startup_logs/, https://docs.datadoghq.com/tracing/troubleshooting/sdk_configurations/

### Common pitfalls
- Live Search shows all spans only for 15 minutes; a filter on a tag that exists only on non-indexed spans returns nothing once the time range is > 15 minutes.
- An empty `trace_id` log section with a populated `host` section means correlation (injection/remapping) is broken, not that logs are missing.
- Custom log parsing must keep trace/span IDs as strings and add a Trace remapper.
- Node.js auto log injection needs JSON logs; Java auto injection (0.74.0+) targets JSON logs.
- Trace-view span search does not support wildcards, unlike the Trace Explorer.
- Map: red node border = entry span error; red edge = exit span error.
- Containers: `localhost:8126` is wrong except on ECS/EKS Fargate.
- Agent flare does not help when traces never reach the Agent; use SDK startup/debug logs.
- Debug mode increases log volume; do not leave it on in production.
- For long-lived postmortem graphs use trace metrics and fixed-time notebook graphs (snapshots), not Live Search.

Sources: https://docs.datadoghq.com/tracing/trace_explorer/, https://docs.datadoghq.com/tracing/troubleshooting/

## Monitors & Alerting

### APM monitor types at a glance

| Monitor | Data it evaluates | Typical use |
| --- | --- | --- |
| **APM Metrics** monitor (Monitors > New Monitor > APM > APM Metrics) | Trace metrics (`trace.<SPAN_NAME>.*`), computed from 100% of traffic | Service/resource-level alerts on hits, errors, error rate, Apdex, latency (threshold or anomaly) |
| **Trace Analytics** monitor (Monitors > New Monitor > APM > Trace Analytics) | **Indexed spans** (only those kept by **custom retention filters**) | Alerts on any span search query, facets and measures (e.g. spike in slow requests, custom span tags) |
| **Anomaly** monitor (Monitors > New Monitor > Anomaly) | Any metric, including `trace.*` metrics, with `anomalies()` | Seasonal/trending metrics where fixed thresholds fail |
| **Watchdog** monitor (Monitors > New Monitor > Watchdog) | Watchdog alert events (APM, Infrastructure, Logs) | Get notified about Watchdog-detected anomalies |
| **Error Tracking** monitor (Monitors > New Monitor > Error Tracking) | Error Tracking issues | New issues / regressions, high-impact issues |
| **Event** monitor with `tags:deployment_analysis` | Watchdog Faulty Deployment Detection events | Notify on faulty deployments |
| **SLO alerts** (error budget, burn rate) | SLO status | Alert on SLO budget consumption |

- APM metric monitors "work like regular metric monitors" but with controls tailored to APM: alerts at the service level on hits, errors and latency measures.
- Trace Analytics ("Analytics") monitors "visualize APM data over time and set up alerts based on Indexed Spans", e.g. alert on a spike in slow requests.
- Service-level monitors are shown on the **Catalog** (Software Catalog, formerly Service Catalog) and **Service Map**; resource-level monitors show on individual **resource pages**.

Sources: https://docs.datadoghq.com/monitors/types/apm/

### APM Metrics monitors (threshold and anomaly)

- **Scope**: choose **primary tags** (env, optional second primary tag), **service**, and **resource** from dropdowns. Custom span tags are NOT available (trace metrics carry only `env`, `service`, `version`, `resource`, `http.status_code`, `http.status_class`, `rpc.grpc.status_code` (Agent 7.65.0+), Agent host tags and additional primary tags).
- **Threshold alert**: alert when **Requests per second, Errors per second, Apdex, Error rate, Avg latency, p50 latency, p75 latency, p90 latency, or p99 latency** is `above`, `above or equal to`, `below`, `below or equal to` an Alert threshold (and optional Warning threshold) over the last 5 minutes, 15 minutes, 1 hour, etc., or **custom between 1 minute and 48 hours**.
- **Anomaly alert**: for the same metric list; "Alert when `<ALERT_THRESHOLD>`%, `<WARNING_THRESHOLD>`% of values are `<NUMBER>` deviations above or below / above / below the prediction during the past 5 minutes, 15 minutes, 1 hour, etc." (custom 1 minute to 48 hours on the APM page).
- Advanced alert conditions (no data, evaluation delay, etc.) are the standard monitor options; "full data window" is a metric-monitor option.
- Trace metrics are computed from **100% of application traffic regardless of ingestion sampling** (exceptions: OTel SDK-level sampling, application-side sampling in a few SDKs, X-Ray). So APM Metrics monitors give accurate request/error/latency alerts even with heavy sampling.
- Trace metric names: `trace.<SPAN_NAME>.hits` (COUNT), `.hits.by_http_status`, `.errors` (COUNT), `.errors.by_http_status`, `.apdex` (GAUGE, web services), `trace.<SPAN_NAME>` (DISTRIBUTION latency; recommended for all latency use cases), legacy `.duration`, `.duration.by_http_status`. Other span tags are NOT tags on trace metrics.

Sources: https://docs.datadoghq.com/monitors/types/apm/, https://docs.datadoghq.com/tracing/metrics/metrics_namespace/

### Automatic APM monitors

- Available to **new organizations**; activate as soon as the Agent is installed and spans flow. **Note: automatic monitor creation is only available during a trial.**
- Created for **service entry points**: operations tagged `span.kind:server` or `span.kind:consumer`.
- **Error rate threshold monitors** per service entry point, built on APM trace metrics; **default error rate 10%** (configurable).
- **Watchdog anomaly monitors**: detect unusual latency, errors and hits for all services without manual thresholds.
- Manage them on the Monitors page (edit, clone, disable).

Sources: https://docs.datadoghq.com/monitors/types/apm/#automatic-apm-monitors

### Trace Analytics monitors (indexed spans)

- Default limit: **1000 Trace Analytics monitors per account**; if hit, use **multi alerts** or contact Support.
- Define the search query with the same syntax as Trace Explorer search.
- Monitor over:
  - **trace count**: search bar only, no facet/measure selected; Datadog counts traces over the time frame.
  - **facet**: alerts on the **Unique value count** of the facet.
  - **measure**: like a metric monitor; choose aggregation `min, avg, sum, median, pc75, pc90, pc95, pc98, pc99, max`.
- Group by **up to four facets**.
- **Simple alert**: one alert when one or more groups breach (less noise). **Multi alert**: one alert per group, e.g. group by `@resource.name` to alert per resource.
- Alert conditions: above / above or equal / below / below or equal; last 5 minutes, 15 minutes, 1 hour, or **custom between 5 minutes and 48 hours** (APM Metrics custom minimum is 1 minute).
- **No data / below alerts**: to be notified when a group stops sending spans, set the condition to **below `1`**.
- **Pitfall**: Trace Analytics monitors **only evaluate spans retained by custom retention filters, not the Intelligent retention filter**. Spans indexed only *indirectly* by trace-level retention filters (spans in a matching trace that do not match the query themselves) are also NOT evaluated.
- Custom group retention (1 to 72 hours) is supported for multi alert monitors with "On missing data" support: APM Trace Analytics, Audit Logs, CI Pipelines, Error Tracking, Events, Logs, RUM.

Sources: https://docs.datadoghq.com/monitors/types/apm/, https://docs.datadoghq.com/monitors/configuration/

### Anomaly detection (anomaly monitors and APM anomaly alerts)

- Identifies when a metric behaves differently than in the past, accounting for **trends, seasonal day-of-week and time-of-day patterns**. Good for metrics with strong trends/recurring patterns; poor on new metrics (needs history).
- Path: Monitors > New Monitor > Anomaly. Editor shows **Historical View** and **Evaluation Preview** graphs.
- Alert conditions: values `above or below` (default), `above`, or `below` the gray band for the last 15 minutes, 1 hour, etc., or custom **15 minutes to 2 weeks**; recover if within bounds for at least ... (same range).
  - **Trigger window**: time the metric must be anomalous before alerting (too short = false alarms).
  - **Recovery window**: recommended to equal the trigger window. Minimum accepted = `trigger_window * (1 - threshold) + 1 min` (50% & 4h -> 121 min; 80% & 4h -> 49 min); max = trigger window.
- **Advanced options**: Deviations (band width, the `bounds` parameter), Algorithm (`basic`, `agile`, `robust`), Seasonality (`hourly`, `daily`, `weekly`) for agile/robust, Daylight savings (agile/robust with weekly/daily), Rollup, Thresholds (% of points anomalous for alert, warning, recovery).
- **Algorithms**:
  - `basic`: no repeating seasonal pattern; lagging rolling quantile; little data, adjusts quickly, no seasonality/trend knowledge.
  - `agile`: seasonal metrics expected to shift; robust SARIMA; quickly adjusts to level shifts but less robust to recent long-lasting anomalies; **not scale-insensitive** (adding 1000 can hide a level shift). May flag the return to normal as anomalous.
  - `robust`: seasonal and stable metrics where slow level shifts are anomalies; seasonal-trend decomposition; predictions stay constant through long anomalies; slower to accept intended level shifts (e.g. after a code change). `basic` and `robust` are scale-insensitive.
  - The old `adaptive` algorithm is no longer used (existing monitors keep working).
- **Seasonality**: hourly (5:15 like 4:15), daily (5pm like yesterday 5pm), weekly (Tuesday like past Tuesdays).
- **Required history**: at least **3x the seasonality** (weekly -> 3 weeks, daily -> 3 days, hourly -> 3 hours); seasonal algorithms may use **up to six weeks** of history. Robust/agile show no bounds during the first few seasons; basic shows bounds shortly after a metric appears.
- **API query**: `avg(<query_window>):anomalies(<metric_query>, '<algorithm>', <deviations>, direction='<direction>', alert_window='<alert_window>', interval=<interval>, count_default_zero='<count_default_zero>' [, seasonality='<seasonality>']) >= <threshold>`
  - `query_window` (e.g. `last_4h`): only the data range in notification graphs, does not affect evaluation; recommended about **5x** `alert_window`; must be >= `alert_window`.
  - `direction`: `above`, `below`, `both`. `interval`: rollup seconds, <= 1/5 of `alert_window`. `seasonality` omitted with `basic`. `threshold`: fraction (0 to 1] of points in `alert_window` that must be anomalous.
  - `options.thresholds`: `critical`, `critical_recovery`, `warning`, `warning_recovery` (0 to 1). `options.threshold_windows`: `trigger_window` (must equal `alert_window`) and `recovery_window`.
  - Anomaly monitors via API: enterprise plans; Datadog strongly recommends exporting a monitor's JSON from the UI.
- Functions not allowed inside `anomalies()`: `cumsum()`, `integral()`, `outliers()`, `piecewise_constant()`, `robust_trend()`, `trend_line()`.
- To ignore anomalies below value X: composite of anomaly monitor A and threshold monitor B (`A && B`).
- Monitors use UTC; set a timezone on the anomaly monitor to correct daylight-savings shifts.

Sources: https://docs.datadoghq.com/monitors/types/anomaly/, https://docs.datadoghq.com/monitors/guide/anomaly-monitor/

### Guide: alert on anomalous p99 latency of a database service

1. New Monitor > **APM**.
2. Primary Tags: choose the **environment**; Service: the **database service**. Resource: leave `*` to watch overall performance (or pick specific queries).
3. Choose **Anomaly Alert**, For: **p99 latency** (chart then shows expected baseline).
4. Set **Alert when** to **100%**: all values for the selected duration must be anomalous; recommended starting point, tune over time.
5. Edit notification, make sure your user is in the Configure notifications and automations field (type `@` to add others), click **Save**.
6. Switch from **Edit** to **Status** tab to see status, mute, investigate.
7. In Catalog > service page > Monitor section, the new monitor appears with suggested monitors.
- Guide's service map legend: green = all monitors quiet, yellow = warnings but no alerts, red = one or more alerting, gray = no monitor. (Current Service Map page instead says node borders are colored by **Service Health**.)

Sources: https://docs.datadoghq.com/tracing/guide/alert_anomalies_p99_database/

### Linking monitors to services, suggested monitors, Service Health

- A monitor is attached to an APM service if `service:<SERVICE_NAME>` is **tagged in the monitor metadata, included in the monitor query, or the query is grouped by service**. Synthetic tests tagged `service:<SERVICE_NAME>` are also attached.
- The `service` tag links APM services to logs, infrastructure, custom business metrics; monitors on any metric (including business metrics) tagged by service show status on the Service Map.
- Service page **Service monitor** panel: active monitors and Synthetic tests for the service, plus a **list of proposed monitors depending on the service type**; enable them directly or create APM monitors.
- **Service Health** (Catalog, service pages, dependency maps, service pills) combines monitors, incidents and Watchdog:
  - **Critical**: a non-muted monitor **with a paging integration (PagerDuty or Opsgenie)** in `ALERT` and triggered within the **past 2 days**; an active incident of any severity; an ongoing faulty deployment; an ongoing APM latency/error rate Watchdog alert.
  - **Warning**: non-muted paging monitor in `WARN` within past 2 days; a stable incident; an ongoing log anomaly alert.
- Monitor Templates (formerly Recommended Monitors): **Monitors > Templates**; with fewer than 10 monitors the Monitor List auto-recommends Integration-Monitor Templates.
- Faulty deployment: "Suggested Monitors" button on the service page only appears if the service has no monitor yet.

Sources: https://docs.datadoghq.com/tracing/services/service_page/#service-monitor, https://docs.datadoghq.com/tracing/services/services_map/, https://docs.datadoghq.com/monitors/templates/

### Watchdog alerts and Watchdog monitors

- Watchdog = Datadog's AI engine: proactive alerts, insights, RCA; **no setup required**.
- **APM coverage**: scans all services and resources for anomalies in **error rate, latency, hits**. Ignores barely used endpoints: needs **at least 0.5 requests per second**. A hit-rate anomaly with **no impact on latency or error rate is ignored**.
- **Required history**: metric anomalies (APM, USM, Infrastructure) need **two weeks** minimum; log anomalies **24 hours**; best with **six weeks**.
- Alert status: `ongoing`, `resolved`, `expired` (**ongoing over 48 hours**). Watchdog Alert Explorer shows alerts from the **last 6 months**. Facets include Alert Category (`apm`, `infrastructure`, `logs`), Alert Type, Alert Status, APM Primary Tag, Environment, Service, End User Impacted (needs RUM), Root Cause (needs APM), Team, Log Anomaly Type/Source/Status.
- Where Watchdog alerts appear: Watchdog Alert Explorer, APM Service Page, Catalog (pink **binoculars** icon next to the service), Watchdog Insights panel in all explorers, metric graphs.
- Archiving an alert (folder icon) hides it and the binoculars icon but does not stop future detection.
- **Watchdog monitor**: Monitors > New Monitor > Watchdog. Predefined selectors: **Environment** (`env` tag), **Alert Category**, **Team** (from Catalog); additional tag filters and Group By. Log anomalies matched by `service`, `source`, `env`.
- Customize sensitivity or watch other metrics with Anomaly, Forecast, Outlier monitors (same seasonal algorithms).
- **Watchdog RCA** requires APM; root cause types: version changes (deployment tracking), traffic increases, AWS instance failures, running out of disk. A latency/error increase is a **critical failure**, never the root cause.
- **Faulty Deployment Detection**: compares new version to previous versions; pink banner on service page; adds an event in Event Explorer. To notify: **Events monitor** with `tags:deployment_analysis`; recommended **recovery time 60 min**.

Sources: https://docs.datadoghq.com/watchdog/, https://docs.datadoghq.com/watchdog/alerts/, https://docs.datadoghq.com/monitors/types/watchdog/, https://docs.datadoghq.com/watchdog/rca/, https://docs.datadoghq.com/watchdog/faulty_deployment_detection/

### Error Tracking monitors

- Path: Monitors > New Monitor > **Error Tracking**. Default limit **1000 Error Tracking monitors per account**.
- Alerting conditions:
  - **New Issue**: issue occurs for the first time **or a regression occurs** (regressions are moved back to For Review). Evaluates issues in **For Review** only; only issues created/regressed after the monitor was created or last edited; **24-hour lookback**. Query clause `.new()`.
  - **High Impact**: issues with many impacted end users; evaluates **For Review or Reviewed** issues. Query clause `.impact()`.
- Source: All, Browser, Mobile, Backend (`.source("all"|"browser"|"mobile"|"backend")`, one at a time).
- Metrics: Error Occurrences, Impacted Users (user emails), Impacted Sessions (session IDs). For **All or Backend** issues only **Error Occurrences** is available. Custom measure = unique count of facet.
- Defaults: window **last 1 day**, threshold **0** (alerts on first occurrence). Example: `error-tracking("{filter}").source("backend").new().rollup("count").by("issue.id").last("1d") > 0`.
- Use **multi alert** (one notification per issue) - intended experience.
- Variables: `{{issue.attributes.error.type}}`, `.message`, `.stack`, `.file`, `.is_crash`, `.category`, `.handling`; `{{issue.link}}`.
- **Ignored** issues are automatically muted from monitor notifications.
- Noise reduction: triage (Reviewed, Ignored, Resolved), expand evaluation window, raise threshold. `issue.age` / `issue.regression.age` not recommended (can miss first prod occurrence).
- Issue states: FOR REVIEW, REVIEWED, RESOLVED, IGNORED, EXCLUDED. Auto-resolve after 14 days (version-aware).

Sources: https://docs.datadoghq.com/tracing/error_tracking/monitors/, https://docs.datadoghq.com/error_tracking/issue_states/

### SLOs on APM data

- Terms: **SLI** (metric or aggregation of monitors), **SLO** (target % for SLI over time), **SLA**, **Error budget** = 100% - target.
- Create: SLO manage page > **New SLO +** > type; target + rolling window **7, 30, or 90 days**; target should be stricter than SLAs; targets must be < 100% (100% = 0 budget and division by zero in alert evaluation).
- **Metric-based (By Count)**: count-based SLI = good events / (good + bad). UI queries: **Sum of the good events** and **Sum of the bad events** (total-events query is legacy, API only). Must use COUNT, RATE, or percentile-enabled DISTRIBUTION metrics (distribution: `count values...` threshold queries). Group with `sum by`. Up to **3 decimal places**. Missing data ignored. Best practice: **use metric-based whenever possible** (volume weighted). APM example: good/bad from `trace.<SPAN_NAME>.hits` and `.errors`, or span-based custom metrics.
- **Monitor-based (By Monitor Uptime)**: time-based SLI from monitor uptime. Supports Metric monitor types (Metric, Integration, **APM Metric**, Anomaly, Forecast, Outlier), Synthetic, Service Checks. Up to **20 monitors**, or one multi alert monitor with up to **20 selected groups**. `WARN` counts as `OK`. Granularity 1 minute; 7/30-day targets 2 decimals, 90-day 3 decimals. **Muting a monitor does not affect the SLO** (use status corrections). Missing data follows monitor setting (Show NO DATA and notify = downtime; Show NO DATA / Show OK = uptime; Show last known status = keep last state).
- **Time Slice (By Time Slices)**: custom uptime condition on a metric (e.g. p95 latency < 1s), no monitor needed; slices of **1 or 5 minutes**; all metric types including gauges; missing data = uptime; corrections = uptime; overall uptime requires all groups up. Can export a single-metric-monitor SLO or import from a monitor.
- Remaining error budget % = `100 * (current status - target) / (100 - target)`.
- Status corrections (Scheduled Maintenance, Outside Business Hours, Deployment, Other); one-time or recurring (RRULE); by SLO name or by tags.
- Burn rate indicator on SLO list: rolling 2 hours; red > 6, yellow 1 to 6.
- Deleted SLOs restorable for 30 days. Permissions: `slos_write`, `slos_corrections`.

Sources: https://docs.datadoghq.com/service_level_objectives/, https://docs.datadoghq.com/service_level_objectives/metric/, https://docs.datadoghq.com/service_level_objectives/monitor/, https://docs.datadoghq.com/service_level_objectives/time_slice/, https://docs.datadoghq.com/service_level_objectives/guide/slo_types_comparison/

### SLO alerts: error budget and burn rate

- Both available for metric-based SLOs, **monitor-based SLOs made only of metric monitor types** (Metric, Integration, APM Metric, Anomaly, Forecast, Outlier), and time slice SLOs. Not for monitor-based SLOs on Synthetic tests or service checks.
- Create from SLO: **Save and Set Alert** (or **Set up Alerts** in the side panel), choose **Error Budget** or **Burn Rate** tab.
- **Error budget alert**: threshold on % of budget consumed, e.g. `error_budget("slo_id").over("30d") > 75`. Monitor type `slo alert`.
- **Burn rate**: how fast the budget is consumed relative to target length. `target length / burn rate = time to exhaust` (30d, burn 2 -> 15 days; burn 3 -> 10 days). Observed error rate = burn rate x ideal error rate. Max burn rate = `1 / (1 - target)` (96% -> 25).
- Burn rate alert = long window AND short window both >= threshold. Long window **1 to 48 hours**; short window auto **1/12 of long** in UI (change via API/Terraform, must be < long).
- Recommended (99.9%): 7-day 16.8/1h/5m, 5.6/6h/30m, 2.8/24h/120m; **30-day 14.4/1h/5m**, 6/6h/30m, 3/24h/120m; 90-day 21.6/1h/5m, 10.8/6h/30m, 4.5/24h/120m.
- Query: `burn_rate("slo_id").over("30d").long_window("1h").short_window("5m") > 14.4`.
- Groups: time slice -> alert on groups or overall (error budget and burn rate); metric-based -> burn rate per group possible, error budget overall only; monitor-based -> overall only.

Sources: https://docs.datadoghq.com/service_level_objectives/error_budget/, https://docs.datadoghq.com/service_level_objectives/burn_rate/

### Monitor configuration options relevant to APM alerts

- Aggregation: average, max, min, sum. Evaluation windows: rolling (up to 1 month for metric monitors) or cumulative (current hour/day/month).
- Evaluation frequency: window < 24h -> 1 min; 24-48h -> 10 min; >= 48h -> 30 min.
- No data options: Evaluate as zero, Show last known status, Show NO DATA, Show NO DATA and notify, Show OK.
- Group retention default 24h; new group delay default 60s; evaluation delay max 86400 s (15 min recommended for cloud metrics).
- Simple alert (one notification) vs Multi alert (one per group, e.g. p99 latency by service).
- Renotify from `alert`, `no data`, `warn`; escalation message via `{{#is_renotify}}`. Priority P1 to P5, `{{override_priority 'P1'}}`.

Sources: https://docs.datadoghq.com/monitors/configuration/, https://docs.datadoghq.com/monitors/notify/

### Notification template variables

- Conditional: `{{#is_alert}}`, `{{#is_warning}}`, `{{#is_recovery}}` (from ALERT, WARNING, UNKNOWN or NO DATA), `{{#is_alert_recovery}}` (ALERT -> OK), `{{#is_warning_recovery}}` (WARNING -> OK), `{{#is_alert_to_warning}}`, `{{#is_no_data}}`, `{{#is_no_data_recovery}}`, `{{#is_renotify}}`, `{{#is_unknown}}`, `{{#is_priority 'P1'}}`, `{{#is_match "tag.name" "str"}}` (substring), `{{#is_exact_match ...}}` (exact; `""` = tag missing/empty). Negate with `^`, `{{else}}` supported. Text outside conditionals is sent on every transition.
- Multi alert tag variables: `{{service.name}}`, `{{env.name}}`, `{{host.name}}`; service group extras `{{service.team}}`, `{{service.docs}}`, `{{service.links}}`, `{{service.links[Runbook]}}`. Facet groups: `{{@facet.name}}`; dotted keys with brackets `{{[dot.key].name}}`.
- Trace Analytics matching attributes: `{{span.attributes.key}}`, `{{span.tags.key}}`; reserved `{{span.env}}`, `operation_name`, `resource_name`, `service`, `status`, `span_id`, `trace_id`, `type`, `link`. `{{span.link}}` links to Trace Explorer scoped on matching spans (`{{log.link}}`, `{{rum.link}}`, `{{issue.link}}` for others).
- Template: `{{value}}`, `{{threshold}}`, `{{warn_threshold}}`, `{{alert_recovery_threshold}}`, `{{warn_recovery_threshold}}`, `{{comparator}}`, `{{first_triggered_at}}`, `{{last_triggered_at}}` (+ `_epoch`), `{{triggered_duration_sec}}`, `{{local_time 'last_triggered_at' 'Asia/Tokyo'}}`.
- Dynamic handles: `@slack-{{service.name}}`; add a fallback with `{{#is_exact_match "x" ""}}`. Triple braces `{{{var}}}` = raw, unencoded.
- Percentile distribution queries (p50/p75/p95/p99) produce no snapshot graph in notifications.

Sources: https://docs.datadoghq.com/monitors/notify/variables/, https://docs.datadoghq.com/monitors/notify/
