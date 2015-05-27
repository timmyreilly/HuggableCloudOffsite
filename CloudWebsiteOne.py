import time

from tokens import *
from helperFUNctions import *

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return get_state_managed_queue()

@app.route("/publish")
def publish():
    def notify():
        msg = str(time.time())
        for sub in subscriptions[:]


if __name__ == "__main__":
    app.run()
