import time


def gettime():
    return time.ctime()


def app(environ, start_response):
    path_info = environ["file_name"]
    if path_info == "/gettime.py":
        start_response("200 OK", [("Server", "PythonWSGIServer1.0")])
        return gettime()

    else:
        start_response("404 Not Found", [("Server", "PythonWSGIServer1.0")])
        return "hello world from WSGI" + str()