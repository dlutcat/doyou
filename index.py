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

urls = (
    '/', 'index',
    '/home/', 'home',
    '/test/', 'test',
)

app = web.application(urls, globals(), autoreload=True)

class index:

    def GET(self):
        return render.index()

class home:

    def GET(self):
        return render.home()

class test:
    
    def GET(self):
        return render.test(name='hello')

d

if __name__ == '__main__': app.run()
