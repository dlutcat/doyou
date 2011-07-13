#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request
from doyou import app
from doyou.database import db_session

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

#@app.teardown_request
#def shutdown_session(exception=None):
#    db_session.remove()

"""
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
"""
