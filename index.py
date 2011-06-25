#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_jinja

import settings
from models import *

render = render_jinja(
    'templates',
    encoding='utf-8',
)
'''
render = web.template.render('templates')
'''

urls = (
    '/', 'index',
    '/home/', 'home',
    '/test/', 'test',
)

user_form = form.Form(
    form.Textbox('name', description='Username'),
    form.Textbox('fullname', description='Fullname'),
    form.Password('password', description='password'),
    form.Password('password2', description='Repeat passowrd'),
    form.Button('password2', description='Repeat passowrd')
)

app = web.application(urls, globals(), autoreload=True)

class index:

    def GET(self):
        return render.index()

class home:

    def GET(self):
        return render.home()

class test:
    
    def POST(self):
        pass
            
    def GET(self):
        f = user_form()
        return render.test(f)

if __name__ == '__main__': app.run()
