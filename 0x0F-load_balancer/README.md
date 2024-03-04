# 0x0F. Load balancer


A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase capacity (concurrent users) and reliability of applications. They improve the overall performance of applications by decreasing the burden on servers associated with managing and maintaining application and network sessions, as well as by performing application-specific tasks.
Load balancers can be based on either hardware or software, and they usually come equipped with some kind of algorithm to determine how to distribute the load. Common methods include round robin, least connections, and IP hash.
In the context of web applications, a load balancer can distribute requests to servers based on factors like the number of connections to a server, the server response time, or even the server's health status. This helps ensure that no single server becomes a bottleneck, improving overall application availability and responsiveness.


## Tasks/Files

|      Tasks          |Files               |
|----------------|-------------------------------|
|0. Double the number of webservers|`0-custom_http_response_header`|
|1. Install your load balancer|`1-install_load_balancer`|
