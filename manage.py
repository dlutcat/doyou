#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from flaskext.script import Manager
from doyou import app
from doyou.models import Location
from doyou.database import db_session

manager = Manager(app)

@manager.command
def syncdb():
    from doyou import database
    database.init_db()

@manager.command
def init_location():
    cities = pickle.load(open('data/location.txt', 'r'))
    for i, v in enumerate(cities):
        province = Location((i+1)*1000, v['name'])
        db_session.add(province)
        for j, c in enumerate(v['cities']):
            city = Location((i+1)*1000 + j+1, c['name'])
            db_session.add(city)
    db_session.commit()


if __name__ == "__main__":
    manager.run()
