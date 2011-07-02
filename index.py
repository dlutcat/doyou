#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_envvar('DOYOU_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    if 'POST' == request.method:
        pass
    else:
        return render_template('register.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
