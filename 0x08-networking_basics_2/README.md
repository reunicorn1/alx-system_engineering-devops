# 0x08. Networking basics #1

In the context of networking, localhost refers to the device used to run the network service. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware, and serves as a method to connect back to the host itself. The IP address 127.0.0.1 is usually used for localhost, and it's a loopback address. In other words, if a program on your machine sends a network request to 127.0.0.1, it is routed to the network software on your own machine.

## tasks/files

|tasks            |files                         |
|----------------|-------------------------------|
|0. Change your home IP|`0-change_your_home_IP`|
|1. Show attached IPs|`1-show_attached_IPs`|
|2. Port listening on localhost|`100-port_listening_on_localhost`|
