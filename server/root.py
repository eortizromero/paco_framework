
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hola Mundo"]


httpd = make_server(host='127.0.0.1', port=8080, app=application)
print("Serving on http://127.0.0.1:8080, press Ctrl+C to exit")
httpd.serve_forever()

