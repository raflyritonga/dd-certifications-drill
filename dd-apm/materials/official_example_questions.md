1. The Live Search view will display all ingested traces for how long? (Choose only ONE best answer)
A. 15 minutes (correct)
B. 24 hours
C. 15 days

2. Which tags are NOT available with tracing application metrics? (Choose only ONE best answer)
A. env, service, version
B. custom tags (Correct)
C. second primary tag

3. What is the MINIMUM information contained on every span? (Choose only ONE best answer)
A. name, duration, and environment
B. type, duration, and start time
C. name, duration, and start time (correct)

4. What is the PRIMARY challenge to monitoring the performance of typical distributed application environments? (Choose only ONE best answer)
A. Services are written in many languages and run on many platforms. (correct)
B. Services are encrypted by several types of encryption.
C. Services take a very long time to respond to requests.

5. Which of the following options BEST describes the percentile distribution metrics that are available for distribution metrics in APM? (Choose only ONE best answer)
A. p50, p75, p90, p95, and p99 (correct)
B. p01, p05, p10, and p25
C. any arbitrary percentile

6. The default APM pricing plan includes 1 million indexed spans per month, retained for how long? (Choose only ONE best answer)
A. 7 days
B. 15 days (Correct)
C. 30 days

7. The Datadog Continuous Profiler can always be enabled with which method? (Choose only ONE best answer)
A. in-code configuration (correct)
B. environment variable
C. both environment variable and in-code configuration

8. Which of the following tags is used to track service deployments? (Choose only ONE best answer)
A. service
B. env
C. version

9. What are the three span tags that must be present on an error span for Datadog Error Tracking to process it? (Choose only ONE best answer)
A. error.message, error.type, and error.stack (correct)
B. error.msg, error.type, and error.stacktrace
C. err.msg, err.type, and err.stack

10. Which filter is always on to retain a subset of important spans? (Choose only ONE best answer)
A. App Analytics Retention Filter
B. Datadog Intelligent Retention Filter (correct)
C. Custom Retention Filter

11. When configuring the RUM SDK to correlate browser requests with APM traces, what is the origin that allowedTracingOrigins should allow? (Choose only ONE best answer)
A. calls made by the browser application (correct)
B. calls made by the receiving backend web server to a third party application
C. calls for the endpoints used by the receiving backend web server

12. A java application needs to be configured with profiling. Where must `-javaagent` be placed and why? (Choose only ONE best answer)
A. Anywhere after the `java` command; The placement does not matter because the profiler library will be loaded in any order.
B. After the `-jar` command; To ensure that the profiler is loaded as late as possible for profiling to occur.
C. Before the `-jar` command; To ensure that the profiler is loaded as early as possible for profiling to occur. (correct)

13. What is the environment variable that enables profiling for the tracing libraries that support this option? (Choose only ONE best answer)
A. DD_PROFILING_ENABLED (correct)
B. DD_APM_PROFILER_ENABLED
C. DD_APM_PROFILING_ENABLED

14. Which tag is used to track services? (Choose only ONE best answer)
A. env
B. service (correct)
C. version

15. Which search technique returns certain profiles on the Search Profile page? (Choose only ONE best answer)
A. using facets (correct)
B. using scopes
C. filtering out profiles on the Datadog Agent

16. What filters allow indexed spans to be available in a Notebook or Dashboard after 15 minutes? (Choose only ONE best answer)
A. spans retained by the Custom Retention Filter only
B. spans retained by the Datadog Intelligent Retention Filter only
C. spans retained by the Datadog Intelligent Retention Filter and the Custom Retention Filter (correct)

17. Assume that an increase in errors has been spotted on the Errors graph of the Service Page. After the incident is resolved what data is used in the resulting post mortem notebook? (Choose only ONE best answer)
A. trace metric (correct)
B. indexed spans
C. screenshot

18. Monitors will be linked to services in the service map and on dashboards if the query is scoped with which tag? (Choose only ONE best answer)
A. env
B. service (correct)
C. version

19. What is the type of instrumentation that would be needed to write custom spans? (Choose only ONE best answer)
A. Manual Instrumentation
B. Custom Instrumentation (correct)
C. Dynamic Instrumentation

20. What can be used to create spans for an unsupported language? (Choose only ONE best answer)
A. Community Tracers (correct)
B. Datadog Agent
C. Datadog Tracer

21. One way to add a service summary page’s Latency graph to a dashboard is to (Choose only ONE best answer)
A. right-click on the graph, select Save As, and specify a dashboard name.
B. hold the mouse pointer over the graph, press Ctrl/ cmd+C top copy it, open the clipboard, and select the target dashboard to export it to. (correct)
C. click the Service Config button and specify the dashboard name in the Dashboards list.


22. A user is looking at some unusual measurements in a graph of a service’s latency metric, and wants to see if there are similar unusual things happening in other metrics that Datadog is collecting at the same time (for example, from integrations). To see this information, they should click on the graph and select: (Choose only ONE best answer)
A. “Find correlated metrics”.
B. “View related logs”.
C. “View related profiles”.

23. What does an Apdex score measure? (Choose only ONE best answer)
A. user satisfaction with the performance of a service in terms of ratio of requests that return without error.
B. the relative performance of a service compared to its past performance.
C. user satisfaction with the performance of a service, in terms of the ratio of requests that are met within a specified time threshold.


