#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, SmallInteger
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class Message(Base):
  """
  私信
  """
  __tablename__ = 'message'

  id = Column(Integer, primary_key=True)
  title = Column(String(256),nullable=False)
  content = Column(Text)
  mtype = Column(SmallInteger, nullable=False, default=0)
  create_time = Column(TIMESTAMP, nullable=False)

  def __init__(self, title, content, mtype):
    self.title = title
    self.content = content
    self.mtype = mtype

  def __repr__(self):
    return "<Message('%s', '%s')>" % (str(self.id), self.title)
