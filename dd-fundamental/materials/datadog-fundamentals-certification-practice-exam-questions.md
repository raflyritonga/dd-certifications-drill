1. Can the Datadog Agent be installed and run on any operating system?
A. No, it only supports running on Linux based operating systems.	
B. No, you need to check the version of your operating system to ensure its compatibility. (Correct)
C. Yes, it can run on any version of an operating system without issue

2. Which of the following is a correct statement?
A. No one is billed twice if they are running the Agent on an AWS EC2 instance that is also picked up by the Datadog AWS integration. (Correct)
B. Host level metrics can be obtained with almost no delay by relying on those provided by cloud services for a cloud based host.
C. Host level metrics can be obtained with a higher resolution by using those provided by cloud services instead of the Datadog Agent.

3. Which of the following is a valid data source to populate an integration template when using the Datadog Agent's Autodiscovery feature in a Docker environment?
A. Key-value stores (correct)
B. Helm Chart
C. ConfigMap

4. Dogstatsd uses UDP instead of TCP because
A. it is very reliable given it guarantees the delivery of applications metric data to DogstatsD.
B. it is a connection-oriented protocol so the application will wait to transmit data in case DogStatsD isn't available.
C. it allows the application to send metrics to DogStatsD and resume its work without waiting for a response. (Correct)

5. Datadog Authentication (crawler) based integrations
A.use credentials provided by the user in Datadog for obtaining metrics with the API. (Correct)
B.are installed with the Datadog Agent and use a Python class method called check to define the metrics to collect.
C.use the Datadog API to allow monitoring of applications based on the language they are written in.

6. In Datadog, metrics submitted with a fractions of a second timestamp
A. are rounded to the nearest whole second. (Correct)
B. are stored in milliseconds to account for the fraction.
C. are rejected by the metrics endpoint upon submission.

7.Which of the following commands will display the distribution and version of a Linux host?
A. cat /etc/os* (correct)
B. uname -n
C. hostname

8. When wanting to install the Datadog Agent on 10 hosts by using a new Ansible server, the Ansible server has been set up, hosts have been added to the inventory file, and the necessary connectivity has been verified. Which step should be taken NEXT on the Ansible server?
A. Run the Datadog Agent installation command.
B. Install the Datadog role from Ansible Galaxy. (Correct)
C. In the ansible.cfg file, set the host_key_checking variable to False.

9. When a user wants to instrument an application to send custom metrics to Datadog, how should they edit the Agent configuration file?
A.Un-comment the use_dogstatsd and dogstatsd_port parameters. (Correct)
B.Un-comment the use_dogstatsd parameter and set it to true.
C.Un-comment the dogstatsd_port parameter and set it to 8125.

10. Which feature allows the ability to submit custom metrics programmatically to Datadog?
A.Datadog Agent
B.DogStatsD (correct)
C.Datadog API

11. What is the main difference between Linux OS and Windows?
A. Linux is a free open source OS while Windows is a proprietary OS. (Correct)
B. Linux is a free OS while Windows is a paying OS.
C. Linux is more secure than Windows

12. Unified service tagging is a best practice that ties Datadog telemetry together through the use of which three standard tags?
A. host, service, and source
B. service, device, and version
C. env, service, and version (correct)

13. To run an agent subcommand, this syntax must be used: <AGENT_BINARY><SUB_COMMAND> <OPTIONS>
In order to get all the configurations loaded and resolved, which of the following subcommands should be used?
A.diagnose
B.configcheck (correct)
C.check

14. Once an integration is enabled/configured, the out of box dashboards are
A. to be cloned and used as templates. (Correct)
B. the source of truth for all metrics collected for the integration.
C. empty until new widgets are created.

15. To configure the Agent log level to collect critical, error, and warn logs only, how should the local datadog.yaml file be modified?
A. Replace # log_level: INFO with log_level: CRITICAL.
B. Replace # log_level: INFO with log_level: ERROR.
C. Replace # log_level: INFO with log_level: WARN. (Correct)

16. For a host running in AWS, how does the Datadog agent determine the hostname?
A. The hostname must be configured in the agent's datadog.yaml file.
B. The agent automatically discovers the EC2 instance id. (Correct)
C. The agent uses the IP address.

17. When a Datadog user account is disabled, what happens to the API and application keys that were created by this account?
A. API keys created by the disabled account remain valid. Application keys created by the disabled account are revoked. (Correct)
B. API keys created by the disabled account remain valid. Application keys are transferred to the admin account that created the disabled account. If this admin account is also disabled, the application keys are revoked.
C. API and application keys created by the disabled account are revoked.

18. When a user is making configuration changes in a datadog.yaml file, which of the following is true?
A. The Datadog Agent must be restarted to apply changes made to datadog.yaml. (correct)
B. The Datadog Agent must be stopped before making any changes to datadog.yaml. Changes at runtime may result in an error.
C. Changes can be made dynamically in datadog.yaml.

19. Which of the following BEST describes custom metrics in Datadog?
A. All non-Agent metrics, such as those submitted by an integration, are considered custom metrics.
B. Any metric submitted using DogStatsD or a custom Agent Check is a considered a custom metric. (Correct)
C. All metrics that are submitted by a community integration are considered custom metric

20. Which of the following is a deployment tool?
A. Kubernetes
B. Red Hat Enterprise Linux
C. Ansible (correct)

21. After making configuration changes to datadog.yaml while the Agent is running, the Agent will apply the changes
A. the next time it starts. (Correct)
B. during the next check cycle.
C. when it receives the reload command.

22. What is the purpose of the auto_conf.yaml file in an integration's conf.d directory?
A. It is an example configuration template for the integration.
B. It allows the agent to AutoDiscover services and monitor them using the integration. (Correct)
C. It configures the integration to run automatically.

23. An application is instrumented to send custom metrics via StatsD. What needs to be done in order to send histogram metrics?
A. Use StatsD to send histogram metric types.
B. Add DogstatsD instrumentation to send histogram metric types. (Correct)
C. Calculate histogram values in the application and use StatsD to send them as metrics.

24. The agent on an Ubuntu host has been temporarily stopped in order to edit a configuration file, but needs to started again. What is the command to run?
A. sudo datadog-agent restart
B. sudo service datadog-agent restart
C. sudo service datadog-agent start (correct)

25. For a Datadog Agent running on a host, what is the definitive method for determining its default configuration values?
A. Examine its original datadog.yaml file. (Correct)
B. Read the Agent documentation on docs.datadoghq.com.
C. Run the command datadog-agent configcheck.
