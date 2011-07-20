#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, SmallInteger
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class MessageUsers(Base):
  """
  私信用户关系表
  """
  __tablename__ = 'message_users'

  message_id = Column(Integer, ForeignKey('message.id'), primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
