# Datadog Fundamentals — Fact Sheet

Compiled from the Aug 2026 exam guide and the Datadog docs/pricing pages it links to. All facts re-checked against the live docs in October 2026.
Exam format: 75 scored + 15 unscored pre-test multiple-choice questions, one correct answer, 2 hours max.

## Exam content outline
- **Essential Concepts**: Config file modification, hardware concepts, metadata, networking, Datadog observability
- **Infrastructure Development**: Agent installation, API key, application key, running the Agent, Agent hostname
- **Networking & Agent Configuration**: Datadog ports, Datadog IP addresses, Autodiscovery
- **Data Collection**: DogStatsD, crawlers, Agent integrations, API endpoints, tagging best practices, metrics & timeseries
- **Troubleshooting Datadog**: Agent commands, Agent logs, Agent config files
- **Data Visualization & Utilization**: Host Map, dashboards, using metrics, using tags, monitors and alerts

---

## 1. Ports & network (heavily tested)

**Direction:** traffic is always *initiated by the Agent* to Datadog (outbound). All Agent traffic is sent over SSL/TLS.

### Outbound (Agent → Datadog)
| Port | Proto | Purpose |
|---|---|---|
| **443** | TCP | Almost everything: metrics, APM traces, live processes/containers, CNM, USM, logs over HTTPS (default/recommended) |
| **10516** | TCP (TLS) | Legacy logs over TCP, US1 (`agent-intake.logs.datadoghq.com`). TCP logs are deprecated/not supported; HTTPS on 443 is the default since Agent 6.19/7.19 |
| **10514** | TCP (no TLS) | Legacy unencrypted logs over TCP, US1. Deprecated |
| **123** | UDP | NTP (time sync). The NTP check flags offsets over 60 seconds by default |
| **8443** | TCP | Custom Agent Autoscaling |
| **8042** | TCP | Remote Configuration connectivity test (telemetry only, only when Remote Config is on) |
| 443 | TCP | EU logs TCP intake also uses 443 (`agent-intake.logs.datadoghq.eu`) |

### Inbound / local (Agent services on the host)
| Port | Proto | Purpose | Config |
|---|---|---|---|
| **8125** | **UDP** | DogStatsD | `dogstatsd_port` / `DD_DOGSTATSD_PORT`. Bound to localhost unless `dogstatsd_non_local_traffic: true` / `DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true` |
| **8126** | **TCP** | APM trace receiver (tracers + profiler) | `receiver_port` / `DD_APM_RECEIVER_PORT`. `DD_APM_NON_LOCAL_TRAFFIC=true` to accept from other containers |
| **5000** | TCP | go_expvar server (Agent internal metrics) | `expvar_port` |
| **5001** | TCP | IPC API (Agent CLI ↔ running Agent) | `cmd_port` |
| **5002** | TCP | Agent browser GUI | `GUI_port` (enabled by default on Windows/macOS, off on Linux; `-1` disables) |
| **5012** | TCP | APM go_expvar server | |
| **6062** | TCP | Process Agent debug endpoints | |
| **6162** | TCP | Process Agent runtime configuration | |

If you change the DogStatsD or APM port, update the tracing library or client configuration to match.

### Destinations
- Metrics, events, service checks, metadata: `<VERSION>-app.agent.<site>` (allowlist `*.agent.<site>`)
- APM: `trace.agent.<site>` · Live processes/containers/CNM/USM: `process.<site>` · Profiling: `intake.profile.<site>`
- Agent flare: `<VERSION>-flare.agent.<site>` · Remote Config: `config.<site>`
- Install packages: `install.datadoghq.com`, `yum.datadoghq.com`, `apt.datadoghq.com`, `keys.datadoghq.com`
- **IP ranges**: `https://ip-ranges.datadoghq.com/` (per-site `ip-ranges.<site>`), JSON with IPv4/IPv6 CIDRs per section (agents, api, apm, logs, process…). Allowlist all of them because the active subset changes.
- Sites: US1 `datadoghq.com` · US3 `us3.datadoghq.com` · US5 `us5.datadoghq.com` · EU1 `datadoghq.eu` · AP1 `ap1.datadoghq.com` · AP2 `ap2.datadoghq.com` · US1-FED `ddog-gov.com`. Set with `site:` / `DD_SITE` (default `datadoghq.com`).

### Connectivity loss
Metrics are buffered in memory up to `forwarder_retry_queue_payloads_max_size` and dropped beyond that. Agent 7.27+ can spill to disk when `forwarder_storage_max_size_in_bytes` > 0 (path `/opt/datadog-agent/run/transactions_to_retry`), only while disk usage is under 80%.

---

## 2. Allotments & billing (heavily tested)

### Allotments per parent unit
| Plan | Included |
|---|---|
| **Infrastructure Pro** (per host) | **100 custom metrics**, 100 ingested custom metrics, **5 containers** (hourly), **500 custom events/month** |
| **Infrastructure Enterprise** (per host) | **200 custom metrics**, 200 ingested, **10 containers** (hourly), **1,000 custom events/month** |
| DevSecOps Pro / Enterprise | Same as Pro (100 / 5 containers) / Enterprise (200 / 10 containers) |
| **APM / APM Pro / APM Enterprise** (per APM host) | **1,000,000 indexed spans/month** (1,370/hour), **150 GB ingested spans/month** |
| APM Pro & Enterprise | + 1 Data Streams Monitoring client host per APM host |
| APM Enterprise only | + 1 Continuous Profiler host per APM host, + 4 profiled containers |
| Continuous Profiler (per profiled host) | **4 profiled containers** (pooled across hosts; overage $2/container) |
| **Database Monitoring** (per DB host) | **200 normalized queries** |
| Serverless Functions APM (per 1M invocations) | 300,000 indexed spans, 50 GB ingested spans |
| Serverless Workload Monitoring, Functions | **5 custom metrics per function** |
| Serverless Workload Monitoring, Apps | 20 custom metrics per app instance |
| Pipeline Visibility (per committer) | 400,000 pipeline spans/month |
| Test Optimization (per committer) | 1,000,000 test spans/month |
| CSM Pro / CSM Enterprise (per host) | 5 / 20 containers |
| Workload Protection (per host) | 4 containers |

### Rules
- Custom metric allotments are **pooled across the whole account**, not per host (3 Pro hosts = 300 custom metrics usable in any split).
- Containers are metered **hourly** only; the allotment is per hour.
- **Hourly on-demand**: included usage is subtracted each hour; at month end on-demand usage is averaged over all hours.
- **Monthly on-demand**: usage averaged across all hours, then commitments and allotments subtracted at month end.
- Indexed spans are **summed** (not averaged) at month end.
- **Host billing (High Watermark Plan)**: hosts metered hourly; bill on the **99th percentile** (top 1% of hours discarded). Alternative: Hybrid Monthly/Hourly Plan (MHP).
- Containers recorded every 5 minutes; billed on fractional hours.
- Logs: **ingested per GB**, **indexed per million events** (rate depends on retention).
- Synthetics: API tests per **10,000** runs; browser tests per **1,000** runs.
- RUM: per 1,000 sessions; a session expires after 15 min inactivity or 4 h continuous activity.
- CI Visibility: billed on committers (≥3 commits in the month).
- A host running the Agent that's also discovered by a cloud integration (e.g., AWS EC2) is **not billed twice**.

### Custom metrics
- A custom metric is a **unique combination of metric name + tag values (including host)**.
- Custom = anything via **DogStatsD** or a **custom Agent check**, Marketplace integrations, or non-Datadog integrations. Some standard integrations can emit custom metrics: JMX, ActiveMQ XML, Go-Expvar (capped at 350 by default); Prometheus/OpenMetrics, Nagios, WMI, PDH, Windows perf counters (no cap); MySQL/Postgres/Oracle/SQL Server custom queries.
- Billable = **average number of distinct custom metrics per hour over the month**. Submission frequency and query count don't matter.
- Counting per tag combination: count, rate, gauge = 1 · **histogram = 5** (avg, count, median, 95percentile, max) · **distribution = 5** (count, sum, min, max, avg), **+5 with percentiles (p50/p75/p90/p95/p99) = 10**.
- Example: `request.Latency` with endpoint∈{X,Y} × status∈{200,400} = 4 combos → gauge 4; histogram 20; distribution 20 (40 with percentiles).
- Adding a tag that adds no granularity (state when city is already there) doesn't increase the count; reordering tags doesn't create new metrics.
- **Metrics without Limits**: *ingested* = everything sent; *indexed* = what's queryable after the tag allowlist. Ingested overage $0.10 per 100.
- Name rules: start with a letter, ASCII alphanumerics, `_` and `.` only (others become `_`), max **200** chars, case-sensitive. Values are 32-bit; timestamp no more than **10 min in the future or 1 hour in the past**. Fractional-second timestamps are rounded to the nearest second.
- Viewing usage requires the Admin role or the `usage_read` permission (Usage page; top 5,000 custom metrics). Metrics Summary shows near-real-time cardinality per metric.

---

## 3. Agent

- Agent v7 is the current major version (Go core; Python 3 checks). Components: **Collector** (runs checks, default every **15 s**), **Forwarder** (sends over HTTPS), **DogStatsD** (flush every **10 s**), **Trace Agent** (APM), **Process Agent**, System Probe.
- Runs as user **`dd-agent`** on Linux. For the Docker integration on a host Agent, add it to the docker group: `usermod -a -G docker dd-agent`.
- Install: one-line script with `DD_API_KEY` and `DD_SITE` (`install_script_agent7.sh`); config management via Ansible (install from **Ansible Galaxy** first: current docs use the collection `ansible-galaxy collection install datadog.dd`; the standalone `datadog.datadog` role is legacy), Chef, Puppet, SaltStack; containers via Docker / Helm / Datadog Operator.
- Docker: image `registry.datadoghq.com/agent:7` (also gcr.io/datadoghq/agent); mounts `/var/run/docker.sock`, `/proc/`, `/sys/fs/cgroup/`; env `DD_API_KEY` (required), `DD_SITE`, `DD_HOSTNAME`, `DD_TAGS` (space-separated), `DD_LOGS_ENABLED`, `DD_APM_ENABLED` (default true), `DD_APM_NON_LOCAL_TRAFFIC`, `DD_DOGSTATSD_NON_LOCAL_TRAFFIC`, `DD_CONTAINER_EXCLUDE`.
- Always check OS/version compatibility before installing.

### Config files
| | datadog.yaml | conf.d |
|---|---|---|
| Linux | `/etc/datadog-agent/datadog.yaml` | `/etc/datadog-agent/conf.d/` |
| macOS | `/opt/datadog-agent/etc/datadog.yaml` | `/opt/datadog-agent/etc/conf.d/` |
| Windows | `%ProgramData%\Datadog\datadog.yaml` | `%ProgramData%\Datadog\conf.d` |

- Each integration has `conf.d/<check>.d/`. Rename `conf.yaml.example` → `conf.yaml` to enable. `conf.yaml.default` enables core checks (cpu, memory, disk…) and is ignored if other config exists. `auto_conf.yaml` = Autodiscovery template. `metrics.yaml` = JMX bean list. Empty files are ignored. All valid YAML files in a check folder are loaded.
- Custom check: `checks.d/<name>.py` + `conf.d/<name>.yaml` (**names must match**), class extends `AgentCheck` and implements `check(self, instance)`. `min_collection_interval` sets frequency.
- **Changes to datadog.yaml or check configs require an Agent restart** (applied the next time it starts).
- The original/example `datadog.yaml` (`datadog.yaml.example`) documents every option and its default value (commented out).
- Key options: `api_key`, `site`, `hostname`, `tags`, `env`, `log_level`, `logs_enabled`, `apm_config.enabled`, `process_config`, `use_dogstatsd`, `dogstatsd_port`, `dogstatsd_non_local_traffic`, `proxy` (`https:`, `http:`, `no_proxy`), `histogram_aggregates`, `histogram_percentiles`.
- `log_level` values: trace, debug, **info (default)**, warn, error, critical, off. Setting `warn` logs warn + error + critical.

### Agent logs
- Linux `/var/log/datadog/` (agent.log, process-agent.log, trace-agent.log, system-probe.log, jmxfetch.log, dogstatsd.log if enabled)
- macOS `/opt/datadog-agent/logs/` · Windows `C:\ProgramData\Datadog\logs\`
- Rotated at 10 MB by default.

### Commands (`<AGENT_BINARY> <SUB_COMMAND> <OPTIONS>`)
- Linux service: `sudo systemctl start|stop|restart datadog-agent` or `sudo service datadog-agent start|stop|restart`. `restart` only for a running Agent; after a stop use `start`.
- `datadog-agent status` (overall state: running checks, forwarder, DogStatsD, logs, APM) · `check <name>` (run one check, show output) · **`configcheck`** (prints all configs loaded and resolved) · **`diagnose`** (connectivity diagnosis) · **`flare`** (collects logs + config with secrets scrubbed, sends to Support, optionally with case ID) · `health` · **`hostname`** (prints hostname the Agent uses) · `launch-gui` · `jmx` · `stream-logs` · `config` (runtime config) · `version` · `import` · Windows-only `start-service`, `restart-service`, `stopservice`.
- Docker: `docker exec -it <container> agent status`. Kubernetes: `kubectl exec -it <pod> -- agent status`. Cluster Agent: `datadog-cluster-agent status`.
- macOS (current docs): stop `sudo launchctl kill SIGTERM system/com.datadoghq.agent`, start `sudo launchctl kickstart system/com.datadoghq.agent`, restart `kickstart -k`; or the systray app. Windows: service `DatadogAgent`, `agent.exe` in `%ProgramFiles%\Datadog\Datadog Agent\bin\`.

### Hostname
- `datadog-agent hostname` prints it. Resolution order includes: configured (`hostname` / `DD_HOSTNAME`), cloud/container providers (GCE, Azure, Fargate, container/kubelet), FQDN (if `hostname_fqdn`), OS hostname, and on **AWS EC2 the instance ID** (when the OS hostname is a default EC2 hostname like `ip-10-…`).
- **Host aliases**: when a host has multiple uniquely identifiable names (e.g., `i-abcd1234` instance ID, `ip-192-0-0-1`, `myhost.mydomain`), Datadog picks one canonical name and adds the others as aliases (visible in Infrastructure List).
- Containers: Agent 7.40+ exits if it can't reliably determine the hostname; fix by giving kubelet/metadata/runtime access or setting `DD_HOSTNAME`.

### API & Application keys
- **API key**: org-level, required by the **Agent** and to **submit** data (metrics, events, logs). Default limit **50 per org**. Revoked API keys can be restored within **7 days**. Remain valid when their creator is disabled.
- **Application key**: tied to a **user** (or service account), used *with* the API key for programmatic **read/manage** access (query metrics, create dashboards/monitors). Inherits creator's permissions unless scoped. **Revoked when the user is disabled**; never transferred (use service accounts to share). Revocation is permanent.
- **Client tokens**: for browser/mobile (RUM, browser logs) instead of API keys.
- Headers: `DD-API-KEY`, `DD-APPLICATION-KEY`. Validate API key: `GET /api/v1/validate`.
- Keys don't expire; store in a secrets manager. If exposed: revoke, scrub, create new, update services, audit.

---

## 4. Data collection

### Integrations (1,000+)
- **Agent-based**: installed with the Agent, Python check class with a `check` method, configured in `conf.d`.
- **Authentication (crawler)-based**: you give Datadog credentials (in the UI); Datadog pulls metrics via the provider API (AWS, Azure, GCP, Slack, PagerDuty…). Cloud metrics arrive with delay and lower resolution than the Agent (CloudWatch ~10 min latency, 1–5 min granularity vs 15 s for Agent).
- **Library**: Datadog API / tracing libraries (ddtrace) instrument applications by language.
- Out-of-the-box dashboards appear when an integration is enabled; they can't be edited, so **clone them**.

### DogStatsD
- Bundled with Agent v6+, enabled by default on **UDP 8125**. Also Unix Domain Socket.
- Linux Agent 7.65+ runs process collection inside the core Agent (not a separate process-agent).
- Implements StatsD + adds **histograms, distributions, service checks, events, tags**. Timers are implemented as histograms.
- **UDP** = fire-and-forget: the app doesn't wait for a response and isn't blocked if DogStatsD is down.
- Aggregates each metric into one point per **10-second flush interval**.
- Datagram: `metric.name:value|type|@sample_rate|#tag1:value,tag2`. Types: `c` count, `g` gauge, `ms` timer, `h` histogram, `s` set, `d` distribution.
- DogStatsD is on by default (`use_dogstatsd: true`, `dogstatsd_port: 8125`). The official practice exam still expects "un-comment `use_dogstatsd` and `dogstatsd_port`" as the answer for enabling custom metrics.
- Clients: Python `datadog`, Ruby `dogstatsd-ruby`, Go `datadog-go`, Java, PHP, .NET. Plain StatsD clients work but lose Datadog extensions (no histograms/tags).
- Kubernetes: pass `DD_AGENT_HOST` from `status.hostIP`. Origin detection (v6.10+) adds pod tags.

### Metric types
| Submission | DogStatsD → in-app | Behavior in a flush interval |
|---|---|---|
| COUNT | RATE (via DogStatsD) / COUNT (API) | sum of values |
| RATE | RATE | count per second |
| GAUGE | GAUGE | last value |
| SET | GAUGE | number of unique values |
| HISTOGRAM | GAUGE + RATE | Agent-side `.avg .count .median .95percentile .max` |
| DISTRIBUTION | GAUGE + COUNT | raw values aggregated server-side across all hosts; enables global percentiles |

Example values `[1,1,1,2,2,2,3,3]` over 10 s: COUNT 15, RATE 1.5/s, HISTOGRAM avg 1.88 / count 0.8 / median 2 / p95 3 / max 3.

### Autodiscovery
- Detects containers and applies integration templates automatically.
- Template sources: **Kubernetes pod annotations** (`ad.datadoghq.com/<container>.checks`), **Docker labels** (`com.datadoghq.ad.checks` since Agent 7.36; older Agents used `com.datadoghq.ad.check_names`, `init_configs`, `instances`), **`auto_conf.yaml` files**, **key-value stores** (etcd, Consul, ZooKeeper), Kubernetes ConfigMaps (K8s only).
- Template variables: `%%host%%`, `%%port%%`, `%%env_<VAR>%%`, `%%pid%%`, `%%hostname%%`.

### API
- Base `https://api.<site>/api/` (v1 and v2). Submit metrics `POST /api/v2/series` (API key only). Query timeseries `GET /api/v1/query` (API + application key). Events `POST /api/v1/events`. Logs `POST https://http-intake.logs.<site>/api/v2/logs`.
- 401/403 = bad or missing key; 429 = rate limited (`X-RateLimit-*` headers).

### Unified service tagging
- Reserved tags **`env`, `service`, `version`** tie metrics, traces and logs together.
- Env vars `DD_ENV`, `DD_SERVICE`, `DD_VERSION`; Docker labels `com.datadoghq.tags.env|service|version`; Kubernetes labels `tags.datadoghq.com/env|service|version`.

### Tags
- Format `key:value` (recommended) or `value`. Must start with a letter; up to **200 chars**; lowercase-normalized for metrics; allowed: letters, numbers, `_ - : . /`; other chars → `_`. Key = everything before the first colon.
- Reserved: `host`, `device`, `source`, `service`, `env`, `version`, `team`.
- Assign via config files, UI, API, DogStatsD; integrations inherit host tags (cloud tags).
- Avoid unbounded values (user IDs, request IDs, timestamps): they explode cardinality and cost.

---

## 5. Visualization, search & monitors

### Query → graph
1. Scope sources by tags (`{env:prod}` or `{*}`)
2. **Time aggregation (rollup)** per source per bucket (default avg; ~300 points per graph; 1-day view ≈ 288 five-minute buckets)
3. **Space aggregation** across sources (avg/sum/min/max) — `avg by {host}` = one line per host
4. Functions/arithmetic applied last.
- `.as_count()` / `.as_rate()` for counts. `.rollup(sum, 60)`.

### Metric query syntax
`avg:system.cpu.user{env:prod,role:db} by {host}` — comma inside `{}` = AND; also `AND`, `OR`, `NOT`, `IN`, `NOT IN`; `!tag:value` excludes; wildcards `host:web-*`.

### Common metrics
`system.cpu.user` (user-space processes), **`system.cpu.system` (kernel)**, `system.cpu.iowait`, `system.cpu.idle`, `system.cpu.stolen` (hypervisor), `system.load.1/5/15`, `system.mem.used/usable`, `system.swap.used`, `system.disk.in_use` (fraction), `system.net.bytes_rcvd/sent`, `datadog.agent.up`.
Metrics are retained **15 months**.

### Host Map & Infrastructure List
- Host Map: one hexagon per host; **Filter by**, **Group by** (tags), **Fill by** (color, default CPU %), **Size by** metric. Green→orange/red. Container Map is the same for containers.
- Host List (Infrastructure > Hosts, formerly Infrastructure List): all hosts reporting via Agent or cloud integration; default shows hosts active in last 15 min; shows hostnames + aliases, tags, apps/integrations, Agent version. Not for billing estimates.
- Software Catalog (the docs now title it "Catalog", under Internal Developer Portal): consolidated view of all discovered services.
- Week-over-week comparison on a timeseries: `calendar_shift("-7d")` (older `week_before()` is deprecated).

### Dashboards
- Layout types (all still listed in the docs): **Dashboards** (grid layout, the default), **Timeboards** (automatic layout, all widgets share the time frame, good for troubleshooting), **Screenboards** (free-form, mixed widgets, status boards).
- Widgets: timeseries, query value, top list, table, heatmap, distribution, host map, change, scatter plot, pie, log stream, monitor summary, SLO, note, group.
- **Template variables** (`$env`) to rescope a dashboard. Integration dashboards → clone to edit.

### Log search
- Tags: `service:web status:error`; attributes with `@`: `@http.status_code:>=500`. Boolean `AND`, `OR`, `-` / `NOT` exclusion, wildcard `*`, ranges `[400 TO 499]`.
- **Facets** (qualitative, for filtering/grouping) vs **measures** (quantitative, ranges & aggregation). You need a facet to filter/group by an attribute in the facet panel.
- Live Tail, Patterns, saved views. `logs_enabled: true` to collect logs with the Agent.

### Monitors
- Types: host (is the Agent reporting — `datadog.agent.up`), metric (threshold/change/anomaly/outlier/forecast), integration, live process, process check (`process.up`), network (TCP/HTTP check), service check, logs, APM, RUM, synthetics, event, composite (combine monitors with `&&`, `||`, `!`), SLO, watchdog, CI, etc.
- **Simple alert** = one alert for the aggregated query; **multi alert** = one alert per group (`by {host}`).
- Thresholds: **alert**, **warning**, alert recovery, warning recovery. Evaluation window (e.g. last 5 min). "Notify if data is missing" → **No Data** state. Renotify, priority P1–P5. States: OK, Warn, Alert, No Data.
- Message variables: `{{value}}`, `{{threshold}}`, `{{host.name}}`, `{{#is_alert}}…{{/is_alert}}`, `{{#is_warning}}`, `{{#is_recovery}}`, `{{#is_no_data}}`, `{{^is_alert}}` (not). Notify with `@email`, `@slack-<channel>`, `@pagerduty-<service>`, `@webhook-<name>`, `@team`.
- **Downtimes** silence notifications during maintenance.

---

## 6. Computing & Linux basics
- **CPU** executes instructions; **load average** = processes running/waiting (compare to core count); **iowait** = CPU idle waiting on disk.
- **RAM**: volatile, holds apps/data in current use. **Swap**: disk used as RAM when RAM is full (slow). Many **page faults** → insufficient RAM.
- Storage: HDD vs SSD, IOPS, throughput, latency, inodes; persistent/non-volatile.
- Linux: `cat /etc/os-release` or `cat /etc/os*` (distro & version), `uname -a` (kernel), `uname -n`/`hostname` (hostname), `top`/`htop`, `free -m`, `df -h`, `du -sh`, `ps aux`, `grep`, `tail -f`, `systemctl`, `journalctl`, `chmod 755`, `chown`, `sudo`, `ss -tulpn`/`netstat -tulpn`, `lsof -i`, `curl`, `ping`, `traceroute`, `dig`/`nslookup`, `nc -zv host port`. Packages: `apt` (Debian/Ubuntu), `yum`/`dnf` (RHEL/CentOS/Amazon Linux). `/etc` = config, `/var/log` = logs, `/proc` = process/kernel pseudo-filesystem.
- Linux = free, open-source; Windows = proprietary.
- **YAML**: spaces only (no tabs), `key: value`, lists with `-`, `#` comments, indentation defines nesting. **JSON**: `{}` objects, `[]` arrays, double-quoted strings, no comments, no trailing commas. **Python**: indentation-significant, `def`, `class`, `import`. **Shell**: `#!/bin/bash`, `$VAR`, `export`, `|`, `>`/`>>`, `2>&1`, `&&`.

## 7. Networking basics
- **TCP**: connection-oriented, 3-way handshake (SYN, SYN-ACK, ACK), reliable, ordered. **UDP**: connectionless, no delivery guarantee, low overhead, less reliable.
- Well-known ports: HTTP 80, HTTPS 443, SSH 22, DNS 53, NTP 123/UDP, SNMP 161/UDP (traps 162), syslog 514, SMTP 25.
- A **port** is a standardized endpoint for communication between devices/processes.
- IPv4 private ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`; loopback `127.0.0.1`. CIDR `/24` = subnet mask 255.255.255.0 (256 addresses). `192.168.1.1/16` and `192.168.2.1/16` are in the same subnet; with `/24` they aren't.
- HTTP status: 2xx success, 3xx redirect, 4xx client error (400, 401 unauthorized, 403 forbidden, 404, 429 too many requests), 5xx server error.
- DNS resolves names to IPs; proxies forward traffic; firewalls must allow the Agent's outbound traffic.
- Cloud Network Monitoring metrics: throughput (bytes), TCP retransmits, latency, connections.
