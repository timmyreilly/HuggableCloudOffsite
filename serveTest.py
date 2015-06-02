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

@app.route("/data")
def data():
    """ 
    Returns a string of the current state of the cloud from stat_managed_queue
    """

    state_string = get_state_managed_queue()
    
    print state_string

    return jsonify(state=state_string, time=time.time())




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