# 0x14. MySQL

MySQL is a popular open-source relational database management system. It uses SQL (Structured Query Language) for querying and managing data.
The master-slave system replication configuration in MySQL is a method which is used to create and maintain multiple copies of the same database. The 'master' server is the primary source of the data, and the 'slave' server is a replica of the master server.
The master logs the updates, which then get transferred to the slave. The slave outputs a query for the updates and applies them to its own database. This system is used for load balancing, backup, and for failover scenarios. It's important to note that the master-slave system is unidirectional, meaning data flows from the master to the slave, not vice versa.



|      Tasks          |Files               |
|----------------|-------------------------------|
|0. Install MySQL||
|1. Let us in!|| 
|2. If only you could see what I've seen with your eyes|| 
|3. Quite an experience to live in fear, isn't it?|| 
|4. Setup a Primary-Replica infrastructure using MySQL|`4-mysql_configuration_primary`, `4-mysql_configuration_replica`| 
|5. MySQL backup|`5-mysql_backup`|
