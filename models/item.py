# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:54:12 2020

@author: RAVI KANCHAN BHENGRA
"""

from db import db                                   #SQLAlchemy class is defined in this file

class ItemModel(db.Model):
    __tablename__ = 'items'                         #Inheriting from the SQLAlchemy library to let it interact with table 'items'.
                                                
    id = db.Column(db.Integer, primary_key=True)    #Define variables according to the columns of the table and the class
    name = db.Column(db.String(80))                 #attributes. Limiting the size of the username and password to 80 characters.
    price = db.Column(db.Float(precision = 2))      #Keeping the precision of the float for two decimal points.
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')           #Kind of SQL join between 'items' and 'stores'
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #Replacing the SELECT query and getting the first row with simple SQLAlchemy methods.
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()