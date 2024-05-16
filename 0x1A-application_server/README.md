## Application Server vs Web Server
An application server and a web server both are servers used to host applications. However, they serve different purposes:

- **Web Server**: It's designed to serve HTTP content. It's mostly designed to serve static content, though most Web Servers have plugins to support scripting languages like Perl, PHP, ASP, JSP etc. through which these servers can generate dynamic HTTP content¹².

- **Application Server**: It can also serve HTTP Content but is not limited to just HTTP. It can provide other protocol support such as RMI/RPC¹. Application servers have components and features to support Application level services such as Connection Pooling, Object Pooling, Transaction Support, Messaging services etc¹.

## Serving a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
Here are the steps to serve a Flask application with Gunicorn and Nginx on Ubuntu 16.04⁹:

1. **Install the Components from the Ubuntu Repositories**: This includes pip, the Python package manager, which will manage the Python components. You will also get the Python development files necessary to build some of the Gunicorn components⁹.

2. **Create a Python Virtual Environment**: Set up a virtual environment in order to isolate the Flask application from the other Python files on your system⁹.

3. **Set Up a Flask Application**: Build a Python application using the Flask microframework⁹.

4. **Create a systemd Unit File**: This will allow Ubuntu's init system to automatically start Gunicorn and serve the Flask application whenever the server boots⁹.

5. **Configuring Nginx to Proxy Requests**: Nginx will be set up to forward requests to the Gunicorn server⁹.

## Running Gunicorn
After installing Gunicorn, you will have access to the command line script `gunicorn`. The basic usage is `$ gunicorn [OPTIONS] [WSGI_APP]`¹¹. Here, `WSGI_APP` is of the pattern `$(MODULE_NAME):$(VARIABLE_NAME)`. The module name can be a full dotted path. The variable name refers to a WSGI callable that should be found in the specified module¹¹.

## Flask and strict_slashes
In Flask, the use of a trailing slash in the URL definition has significance. If the canonical URL for the endpoint has a trailing slash, it is similar to a folder on a filesystem. Accessing it without a trailing slash will cause Flask to redirect to the canonical URL with the trailing slash⁴. If you want to change this behavior, you can set `strict_slashes=False` on the route⁴.

## Upstart Documentation
Upstart is an event-based replacement for the traditional init daemon – the method by which several Unix-like computer operating systems perform tasks when the computer is started. It was written by Scott James Remnant, a former employee of Canonical Ltd¹⁶.
