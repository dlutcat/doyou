#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class Location(Base):
  """
  地域字典表
  """
  __tablename__ = 'location'

  id = Column(Integer, nullable=False, primary_key=True)
  name = Column(String(128), nullable=False)

  def __init__(self, id=None, name=None):
    self.id = id
    self.name = name

  def __repr__(self):
    return "<Location('%s', '%s')>" % (str(self.id), self.name)
