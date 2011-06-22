#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form

import settings

render = web.template.render(settings.TEMPLATE_DIR)

urls = (
    '/', 'index',
)

app = web.application(urls, globals())

class index:

    def GET(self):
        return render.index()

if __name__ == '__main__': app.run()
