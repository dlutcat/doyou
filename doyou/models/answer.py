#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, SmallInteger
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class Answer(Base):
  """
  回答信息
  """
  __tablename__ = 'answer'

  id = Column(Integer, primary_key=True)
  question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
  question = relationship('Question', backref="answers")
  flag = Column(SmallInteger, nullable=False)
  comment = Column(String(1024))
  creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  creator = relationship('User', backref="answers")
  create_time = Column(TIMESTAMP, nullable=False)

  def __init__(self, flag, comment):
    self.flag = flag
    self.comment = comment

  def __repr__(self):
    return "<Question('%s', '%s', '%s')>" % (str(self.id), self.comment, str(self.flag))
