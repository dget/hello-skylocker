#!/usr/bin/env python

import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h2>Hello, Skylocker!</h2>"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))
