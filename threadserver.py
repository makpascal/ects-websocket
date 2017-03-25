from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)

def main():
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('127.0.0.1', 9999), app, handler_class=WebSocketHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
