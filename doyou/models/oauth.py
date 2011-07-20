#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, SmallInteger
from sqlalchemy.orm import relationship, backref
from doyou.database import Base

class Oauth(Base):
  """
  Oauth信息
  """
  __tablename__ = 'oauth'

  id = Column(Integer, primary_key=True)
  oauth_type = Column(SmallInteger,nullable=False)
  oauth_id = Column(String(120))
  oauth_homepage = Column(String(1024))
  tokenkey = Column(String(128), nullable=False)
  tokensecret = Column(String(128), nullable=False)
  create_time = Column(TIMESTAMP, nullable=False)

  def __init__(self, oauth_type, oauth_id, oauth_homepage, tokenkey, tokensecret):

    self.oauth_type = oauth_type
    self.oauth_id = oauth_id
    self.oauth_homepage = oauth_homepage
    self.tokenkey = tokenkey
    self.tokensecret = tokensecret

  def __repr__(self):
    return "<Oauth('%s', '%s', '%s')>" % (str(self.id), self.oauth_type, self.oauth_id)
