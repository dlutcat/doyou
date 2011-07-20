#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flaskext.script import Manager
from doyou import app

manager = Manager(app)

@manager.command
def syncdb():
    from doyou import database
    database.init_db()


if __name__ == "__main__":
    manager.run()
