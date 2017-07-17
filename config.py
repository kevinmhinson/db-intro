'''
pass configuration details to app
called by app.py
'''
import os

class Config(object):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

  HOST = '127.0.0.1'
  PORT = 5000
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
  SQLALCHEMY_TRACK_MODIFICATIONS = False # reduce overhead