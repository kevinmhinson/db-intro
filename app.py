'''
create Flask app and configure (using config.py)
called by main.py
'''

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy  # deprecated, replaced with following...
from flask_sqlalchemy import SQLAlchemy 

from config import DevConfig, ProdConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db =  SQLAlchemy(app)