#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, Table, Column, 
                        Integer, String, MetaData, ForeignKey)
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

from python.settings

engine = create_engine('mysql://%s:%s@%s/%s' % (settings.USER, settings.PASSWORD, settings.HOST, settings.DBNAME)
metadata = MetaData()
Base = declarative_base()

users_table = Table('users', metadata,
  Column('id', Integer, primary_key=True),
  Column('name', String(30)),
  Column('fullname', String(50)),
  Column('password', String(30))
)

metadata.create_all(engine)

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
'''
class User(Object):
  def __init__(self, name, fullname, password):
    self.name = name
    self.fullname = fullname
    self.password = password
  def __repr__(self):
    return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

mapper(User, users_table)

ed_user = User('patto', 'patto cheng', 'xxxxx')
print ed_user.name
print ed_user.id
