# 0x1A. Application server

An application server is a server that hosts and operates applications. It provides the necessary infrastructure to create web applications and services.
WSGI, or Web Server Gateway Interface, is a standard interface between web servers and web applications in Python. It's a protocol for Python web applications to communicate with web servers, and it allows for flexibility in choosing between different web servers and web applications.
Gunicorn, or 'Green Unicorn', is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model, which means it forks multiple worker processes to handle requests. Gunicorn is often used to serve Python web applications from a web server.
In a typical setup, you might have a web server like Nginx that receives client requests. This server then passes appropriate requests to Gunicorn via the WSGI protocol. Gunicorn, acting as an application server, runs your web application and returns responses to the web server, which then sends these responses to the client.


## Tasks/Files

|      Tasks          |Files               |
|----------------|-------------------------------|
|0. Set up development with Python|`README.md`| 
|1. Set up production with Gunicorn|| 
|2. Serve a page with Nginx|`2-app_server-nginx_config`|
|3. Add a route with query parameters|`3-app_server-nginx_config`|
|4. Let's do this for your API|`4-app_server-nginx_config`|
|5. Serve your AirBnB clone|`5-app_server-nginx_config`|

