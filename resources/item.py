# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:54:13 2020

@author: RAVI KANCHAN BHENGRA
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()        #To parse the request and give a check for the specific keys, in this case, 'price'
    parser.add_argument('price',             #The parser is set only for the 'price' key, so any other field that is present in the 
                            type = float,    #request will get erased.
                            required = True,
                            help = 'This field cannot be left blank'
                )
    
    parser.add_argument('store_id',                                   
                            type = int,                               
                            required = True,
                            help = 'Every item needs a store id'
    )
    
    @jwt_required()
    def get(self,name):  #name the method 'get' for GET
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
        
    def post(self,name): #name the method 'post' for POST
        if ItemModel.find_by_name(name):
            return {'message' : "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()                                                 
        item = ItemModel( name, data['price'], data['store_id'])
        
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured while inserting the item.'}, 500  #500 - internal server error
        
        return item.json() , 201                                                   #Passing 201 code for status as Created
    
    def delete(self,name): #name the method 'delete' for DELETE       
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            
        return {'message': 'Item deleted'}
    
    def put(self,name):    #name the method 'put' for PUT       
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            
        item.save_to_db()        
        return item.json()
    
    
class ItemList(Resource):
    
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} #Returning all the data in the table.