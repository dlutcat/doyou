#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class User(Base):
  """
  用户信息
  """
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  nickname = Column(String(30),nullable=False)
  email = Column(String(120), index=True)
  gender = Column(Integer, nullable=False)
  location_id = Column(Integer, ForeignKey('location.id'), nullable=False) 
  location = relationship('Location', backref='users')
  password = Column(String(64), nullable=False)
  avatar = Column(String(1024))
  profile = Column(Text)
  shorturl = Column(String(8))
  create_time = Column(TIMESTAMP, nullable=False)

  def __init__(self, nickname, email, gender, password, avatar, profile, shorturl, create_time):
    self.nickname = nickname
    self.email = email 
    self.gender = gender
    self.password = password
    self.avatar = avatar
    self.profile = profile
    self.shorturl = shorturl
    self.create_time = create_time

  def __repr__(self):
    return "<User('%s', '%s', '%s')>" % (str(self.id), self.nickname, self.email)
