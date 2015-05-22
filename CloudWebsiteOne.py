import time

from tokens import *
from helperFUNctions import *

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return get_state_managed_queue()

if __name__ == "__main__":
    app.run()
