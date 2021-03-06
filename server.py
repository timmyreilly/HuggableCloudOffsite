#!/usr/bin/env python

from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import gevent

from helperFUNctions import *

from flask import Flask, jsonify, request, render_template, send_from_directory
import time, threading, random, webbrowser, os, platform

start_local_browser = platform.system() == 'Windows'


app = Flask(__name__)
    
if start_local_browser:
    PORT = 5000 + random.randint(0, 999)
else:
    PORT = 5000
MIN_DELAY, MAX_DELAY = 0, 1

# for testing
PORT = 5000

@app.route("/data", methods=['GET'])
def data():
    state_string = get_state_managed_queue()
    print state_string
    return jsonify(state=state_string, time=time.time())

@app.route("/updated")
def updated():
    """
    Update the client that an update is ready. Contracted by the client to subscribe to the notification service
    """
    ws = request.environ.get('wsgi.websocket', None)
    print "Web Socket RETRIEVED"
    if ws:
        while True:
            delay = random.randint(MIN_DELAY, MAX_DELAY)
            gevent.sleep(delay)
            ws.send('ready')
    else:
        raise RuntimeError("Environment lacks WSGI WebSocket support")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def main():
    return render_template("base.html", port=PORT)

if __name__ == "__main__":
    
    if start_local_browser:
        # start server and web page pointing to it
        url = "http://127.0.0.1:{}".format(PORT)
        wb = webbrowser.WindowsDefault()  # Using Windows Default instead
        threading.Timer(1.00, lambda: wb.open(url) ).start()
    
    print 'Port: ' , PORT 
    http_server = WSGIServer(('', PORT), app, handler_class=WebSocketHandler)

    http_server.serve_forever()
    #app.run(port=port, debug=False)