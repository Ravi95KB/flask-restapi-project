# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:44:26 2020

@author: RAVI KANCHAN BHENGRA
"""
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'                         #Inheriting from the SQLAlchemy library to let it interact with table 'users'.
                                                
    id = db.Column(db.Integer, primary_key=True)    #Define variables according to the columns of the table and the class
    username = db.Column(db.String(80))             #attributes. Limiting the size of the username and password to 80 characters.
    password = db.Column(db.String(80))
    
    def __init__(self, username,password):
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    
    @classmethod
    def find_by_id(cls, idNum):
        return cls.query.filter_by(id=idNum).first()