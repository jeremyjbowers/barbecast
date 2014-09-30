#!/usr/bin/env python

import json

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('payload.json', 'r') as readfile:
        return render_template('index.html', objs=list(json.loads(readfile.read())))

if __name__ == '__main__':
    app.run(port=8000, debug=True)