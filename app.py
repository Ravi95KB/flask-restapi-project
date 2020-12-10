# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:45:54 2020

@author: RAVI KANCHAN BHENGRA
"""

'''We are using flask_restful instead of normal flask library, so the syntax is gonna be different'''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from security import autheticate, identity
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #To turn off the Flask tracking
app.secret_key = 'ravi'
api = Api(app)

@app.before_first_request                      #This method will create the table in data.db before any API request is sent.
def create_tables():
    db.create_all()

#creates another endpoint with /auth
jwt = JWT(app, autheticate, identity) 

api.add_resource(Store,'/store/<string:name>')          
api.add_resource(Item,'/item/<string:name>')    #Sort of the endpoint which can be accessed by http://127.0.0.1:5000
api.add_resource(StoreList,'/stores')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')     #Endpoint for registering users

if __name__ == '__main__':                      #Will run only when app.py is made to run, not when app module is imported from some other file
    db.init_app(app)                            
    app.run(port=5000, debug=True)              #Not really necessary as the default 5000. Add Debug parameter for getting error traceback.