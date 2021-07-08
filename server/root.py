
from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple


def application(environ, start_response):
    request = Request(environ)
    response = Response("Hola Mundo", mimetype="text/plain")
    return response(environ, start_response)

if __name__ == "__main__":
    run_simple('127.0.0.1', 8080, application, use_debugger=True, use_reloader=True)

