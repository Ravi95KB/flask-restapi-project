# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:35:16 2020

@author: RAVI KANCHAN BHENGRA
"""

from app import app
from db import db

db.init_app(app)

@app.before_first_request                      #This method will create the table in data.db before any API request is sent.
def create_tables():
    db.create_all()
