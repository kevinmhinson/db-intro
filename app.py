'''
create Flask app and configure (using config.py)
called by main.py
'''

from flask import Flask
from config import DevConfig, ProdConfig

app = Flask(__name__)
app.config.from_object(DevConfig)