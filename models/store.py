# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:39:01 2020

@author: RAVI KANCHAN BHENGRA
"""

from db import db                                   #SQLAlchemy class is defined in this file

class StoreModel(db.Model):
    __tablename__ = 'stores'                         #Inheriting from the SQLAlchemy library to let it interact with table 'items'.
                                                
    id = db.Column(db.Integer, primary_key=True)    #Define variables according to the columns of the table and the class
    name = db.Column(db.String(80))                 #attributes. Limiting the size of the username and password to 80 characters.
    
    items = db.relationship('ItemModel', lazy = 'dynamic') #So that SQLAlchemy doesn't create item object for each item.
     
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name': self.name, 'price': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #Replacing the SELECT query and getting the first row with simple SQLAlchemy methods.
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()