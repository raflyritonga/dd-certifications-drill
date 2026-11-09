1. Why are logs important? (Choose only ONE best answer)
A. They help break down slow requests by time spent in code on CPU, GC, lock contention, and I/O.
B. They help identify trends over long periods of time.
C. They help pinpoint the cause of problems and are written records for audit/compliance purpose. (correct)

2. Which log search query should be used to find logs with an error status that contain the indication of their info severity in their log message? (Choose only ONE best answer)
A. status:error and info (correct)
B. error and severity:info
C. status:error and severity:info

3. Which logging format is automatically parsed by Datadog? (Choose only ONE best answer)
A. XML
B. JSON (correct)
C. IIS

4. Which of the following is a key benefit of using Logging Without Limits (Choose only ONE best answer)
A. generating metrics
B. archiving all logs (correct)
C. detecting anomalies

5. By default, which directory contains logs for processes running on a Linux distribution? (Choose only ONE best answer)
A. /tmp/
B. /etc/logrotate/
C. /var/log/ (correct)

6. Which Datadog product should be used to automatically detect security signals from logs? (Choose only ONE best answer)
A. Datadog SIEM (correct)
B. Datadog CSPM
C. Datadog AppSec

7. What is the maximum number of facets supported by Timeseries and Table visualizations? (Choose only ONE best answer)
A. 3 (correct)
B. 4
C. 5

8. How would a URL be generated that dynamically links to the appropriate dashboard in an alert’s message? (Choose only ONE best answer)
A. Create an advanced alert condition.
B. Add a priority to the alert.
C. Use a template variable. (correct)


9. On Linux systems, which directory should the Agent’s ‘dd-agent’ user own in order to write to log files? (Choose only ONE best answer)
A. /tmp/log/
B. /var/log/datadog/ (correct)
C. /etc/datadog-agent/

10. To present data so it is more easily understood, move a column in the Log Explorer by (Choose only ONE best answer)
A. clicking on a column header’s dropdown menu and selecting an Insert option.
B. Move from left to right by dragging and dropping them (6 dots icon). (correct)
C. clicking on a column header’s dropdown menu and selecting a Move option.

11. Which of the following should be done to visualize log counts by facet in the Log Explorer? (Choose only ONE best answer)
A. Click the Group into Fields button, and group by a facet in the dropdown list. (Correct)
B. Click the Group into Patterns button, and group by status and service.
C. Click the Group into Patterns button, and group by status.

12. Which of the following should be done to aggregate logs into long-term key performance indicators (KPIs)? (Choose only ONE best answer)
A. Click the Export button and select Generate New Metric. (correct)
B. Click the Export button and select Export to Dashboard.
C. Click the Export button and select Export to Monitor.

13. Logs provide insight into an application by helping users understand (Choose only ONE best answer)
A. why the application failed. (correct)
B. how the application performed.
C. the application queue size.

14. How can specific logs be filtered from processing based on value? (Choose only ONE best answer)
A. Set the exclude type with a pattern to test log data against in the Datadog Agent.
B. Set the exclude_at_match type with a pattern to test log data against in the Datadog Agent. (correct)
C. Create a list of filter patterns in the Datadog application.

15. If log data is important but contains sensitive material, how can that log be processed with the sensitive data hidden? (Choose only ONE best answer)
A. Add a log processing rule with a ‘mask sequence’ type to match sensitive data patterns and mask it. (correct)
B. Add a log parsing pipeline to match sensitive data patterns and mask it.
C. Mask the log data at the application-level before emitting it.

16. How can string data in a JSON object from a source that does not have an integration be parsed? (Choose only ONE best answer)
A. Parse the data at the application-level prior to emitting the log from the source.
B. Use the generic JSON processing pipeline to parse the data.
C. Create a custom processing pipeline to parse the data based on the tagged source. (correct)


17. How can a sortable column based on a log’s attribute be added to the List View of the Log Explorer? (Choose only ONE best answer)
A. from both the List View “Options” dropdown menu and from the facets panel on the left side of the Explorer (correct)
B. from only the List View “Options” dropdown menu
C. from the Configuration submenu item under Logs in the main navigation

18. From the Log Explorer, how can product stakeholders be notified of business-critical data based on a search query? (Choose only ONE best answer)
A. Export the search query to a new dashboard.
B. Export the search query to a new notebook.
C. Export the search query to a new monitor. (correct)

19. How are logs collected from JavaScript applications? (Choose only ONE best answer)
A. Datadog SDKs or libraries (correct)
B. filing a support ticket
C. uploading Gzip files to Datadog

20. Which Datadog Agent command allows printing of all configurations loaded in a running Agent? (Choose only ONE best answer)
A. config
B. configload
C. configcheck (Correct)

21. Which of the following is a benefit of leveraging Standard Attributes in logs? (Choose only ONE best answer)
A. version control
B. easy to search (correct)
C. API access

22. How long are log-based metrics retained in Datadog? (Choose only ONE best answer)
A. 15 days
B. 15 weeks
C. 15 months (correct)

23. By default, where are web application browser logs stored? (Choose only ONE best answer)
A. not stored by default (correct)
B. in the browser application’s directory on the host machine
C. on the server that hosts the web application

24. The Datadog Agent tails logs from (Choose only ONE best answer)
A. files on disk. (Correct)
B. TCP/UDP Sockets.
C. stdout/stderr

25. Which query searches logs coming from both nginx and redis? (Choose only ONE best answer)
A. source:nginx AND redis
B. source:(-nginx AND redis)
C. source:nginx AND source:redis (correct)
