#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class Question(Base):
  """
  问题信息
  """
  __tablename__ = 'question'

  id = Column(Integer, primary_key=True)
  content = Column(String(1024),nullable=False)
  asker_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  asker = relationship('User', backref="questions")
  category = Column(Integer, nullable=False, default=0)
  create_time = Column(TIMESTAMP, nullable=False)

  

  def __init__(self, content, category, create_time):
    self.content = content
    self.category = category
    self.create_time = create_time

  def __repr__(self):
    return "<Question('%s', '%s', '%s')>" % (str(self.id), self.content, str(self.asker_id))
