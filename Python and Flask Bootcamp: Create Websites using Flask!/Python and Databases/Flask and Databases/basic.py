import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)
#__file__ --> ./Python and Databases/basic.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')

db = SQLAlchemy(app)

Migrate(app,db)

########################################################################################

class Puppy(db.Model):

    #Manual table name choice!
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year's old"
