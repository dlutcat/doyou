#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from doyou.database import db_session

app = Flask(__name__)
app.config.from_envvar('DOYOU_SETTINGS', silent=True)

import doyou.views

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

"""
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
"""
