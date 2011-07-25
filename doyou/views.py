#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for, abort
from doyou import app
from doyou.database import db_session
from doyou.libs.tools import get_param
from doyou.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    error = None
    if 'POST' == request.method:
      email = get_param(request, 'email')
      gender = get_param(request, 'gender')
      nickname = get_param(request, 'nickname')
      passwd = get_param(request, 'password')
  
      user = User(nickname, email, int(gender), passwd)
      db_session.add(user)
      #try:
      db_session.commit()
      session['user'] = user
      return redirect(url_for('index'))
      """
      except:
        print 'User signup error'
        abort(500)
      """
    else:
        return render_template('signup.html')

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
