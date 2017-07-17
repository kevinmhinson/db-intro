'''
routing info applied to app
called (run) by main.py
'''

from app import app

@app.route('/')
def homepage():
  return 'Home page'