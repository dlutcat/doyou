#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from doyou.database import Base

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
