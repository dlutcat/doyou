#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#from settings

#engine = create_engine('mysql://%s:%s@%s/%s' % (settings.USER, settings.PASSWORD, settings.HOST, settings.DBNAME)
engine = create_engine('mysql://root:deadbeef@localhost/doyou')
Base = declarative_base()

'''
metadata = MetaData()
users_table = Table('users', metadata,
  Column('id', Integer, primary_key=True),
  Column('name', String(30)),
  Column('fullname', String(50)),
  Column('password', String(30))
)

metadata.create_all(engine)

class User(object):
  def __init__(self, name, fullname, password):
    self.name = name
    self.fullname = fullname
    self.password = password
  def __repr__(self):
    return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

mapper(User, users_table)
'''

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String(30))
  fullname = Column(String(50))
  password = Column(String(30))

  def __init__(self, name, fullname, password):
    self.name = name
    self.fullname = fullname
    self.password = password

  def __repr__(self):
    return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

users_table = User.__table__
metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
