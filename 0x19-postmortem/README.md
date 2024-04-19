# 0x19. Postmortem


![0d0a7a75c2376e7fda7c49981ad129ba.jpg](https://i.postimg.cc/FHQvDMPz/0d0a7a75c2376e7fda7c49981ad129ba.jpg)

In the story of the movie “Ron’s Gone Wrong”, where every child craves the companionship of a shiny new B-Bot, there lived a young boy named Barney. Unlike his peers, Barney didn't have the luxury of owning a B-Bot due to his family's financial struggles. But fate had a quirky sense of humour, for on Barney's birthday, he received a most unexpected gift – a malfunctioning B-Bot named Ron.
Ron was a glitchy anomaly in the world of perfect B-Bots. Instead of being the flawless companion Barney had dreamed of, Ron's programming was riddled with errors, causing chaos and confusion at every turn.
In the parallel digital universe, troubleshooting comes to be the tool to solve issues and bugs that occur all the time. Since we mentioned Disney stories, one popular platform that runs on WordPress is actually "The Walt Disney Company's Newsroom" website. This platform serves as a central hub for news and press releases related to The Walt Disney Company and its various subsidiaries.
As Barney and Ron embarked on their journey to fix Ron's programming, they encountered challenges, setbacks, and moments of doubt, much like the teams working tirelessly behind the scenes of a platform like "The Walt Disney Company's Newsroom" to solve issues and bugs behind running softwares. But through perseverance both Barney and Ron, as well as the digital heroes, triumphed in the end.




**Issue Summary**
On April 2nd, between 4:30 PM and 8:58 PM GMT, The Walt Disney Company's Newsroom website experienced a widespread outage, displaying a 500 Internal Server Error to all users attempting to access the platform. This prevented access to the blog page and all related content, disrupting access to news and press releases related to The Walt Disney Company and its subsidiaries. The root cause was traced back to a typo in the PHP configuration files during a recent update to the WordPress installation, which managed and published the platform's content.

**Timeline (all times GMT Time)**
4:22 PM: An update related to a WordPress plugin was pushed, introducing changes to the platform's functionality.
4:30 PM: Outage begins, with users reporting the issue to the administration.
5:49 PM: Content creators, engineers and DevOps Teams are alerted via pagers.
8:15 PM: A successful configuration change rollback is performed, and investigation into the issue begins, focusing initially on server configuration files.
8:23 PM: Server restarts commence, and the root cause is identified using the strace tool to trace system calls and signals. A typo in the WordPress installation's configuration files is discovered.
8:58 PM: 100% of traffic is restored as the issue is resolved.

**Root Cause**
The outage was initially suspected to be related to server configuration due to the 500 Internal Server Error. After investigation, it was determined that the recent changes introduced a typo in the WordPress installation's configuration files, leading to the platform's inability to serve content properly.

**Corrective and Preventative Measures**
Code Review Process: Implement a rigorous code review process for all updates and changes to the WordPress installation, ensuring that configuration files are thoroughly checked for errors before deployment.
Automated Testing: Introduce automated testing procedures to validate configuration changes and updates, flagging any discrepancies or potential issues before they impact the production environment.
Monitoring and Alerting: Enhance monitoring and alerting systems to promptly detect and notify teams of critical errors or anomalies, enabling faster response times and resolution of issues
Rollback Procedures: Establish clear rollback procedures to swiftly revert changes in case of emergencies, minimising downtime and impact on users while investigations are conducted.

**Documentation and Training:**
Provide comprehensive documentation and training for team members responsible for managing and maintaining the platform, emphasising best practices and procedures to prevent similar incidents in the future.
By implementing these measures, The Walt Disney Company can mitigate the risk of similar outages and ensure the continued reliability and availability of its Newsroom website for users worldwide.
