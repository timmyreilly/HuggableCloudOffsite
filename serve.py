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
MIN_DELAY, MAX_DELAY = 5, 20

time_format = {
    'one': "%H:%M:%S",
    'best': "%a, %d %b %Y %H:%M:%S +0000",
    'other': "%a, %H:%M",
}

@app.route("/data", methods=['GET'])
def data():
    """
    Provides the server's current timestamp, formatted in several different
    ways, across a WebSocket connection. NB While other Python JSON emitters
    will directly encode arrays and other data types, Flask.jsonify() appears to
    require a dict.
    """
    
    fmt    = request.args.get('format', 'best')  # gets query parameter here; default 'best'
    
    now    = time.time()
    nowstr = time.strftime(time_format[fmt])

    other = get_state_managed_queue()

    info = { 'value':    other,
             'contents': "The time is now <b>{0}</b> (format = '{1}')".format(nowstr, fmt),
             'format':   fmt,
             'other': other
            }
    return jsonify(info)


@app.route("/updated")
def updated():
    """
    Notify the client that an update is ready. Contacted by the client to
    'subscribe' to the notification service. 
    """
    ws = request.environ.get('wsgi.websocket', None)
    print "web socket retrieved"
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
    return render_template("index.html", port=PORT)
    

if __name__ == "__main__":
    
    if start_local_browser:
        # start server and web page pointing to it
        url = "http://127.0.0.1:{}".format(PORT)
        wb = webbrowser.WindowsDefault()  # Using Windows Default instead
        threading.Timer(1.25, lambda: wb.open(url) ).start()
    
    print 'Port: ' , PORT 
    http_server = WSGIServer(('', PORT), app, handler_class=WebSocketHandler)

    http_server.serve_forever()
    #app.run(port=port, debug=False)
