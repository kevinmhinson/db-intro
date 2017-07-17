'''
pass configuration details to app
called by app.py
'''

class Config(object):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  HOST = '127.0.0.1'
  PORT = 5000
  DEBUG = True