# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:18:32 2020

@author: RAVI KANCHAN BHENGRA
"""

from flask_restful import Resource, reqparse
from models.user import UserModel
    
class UserRegister(Resource):    #Creating a resource (an endpoint) for registering users.    
    parser = reqparse.RequestParser()
    
    parser.add_argument('username',
            type = str,
            required = True,
            help = "This field cannot be left blank."
            )
    
    parser.add_argument('password',
            type = str,
            required = True,
            help = "This field cannot be left blank."
            )
    
    def post(self):       
        data = UserRegister.parser.parse_args()       #The json message sent from the Postman or normaly from the web as post request 
                                                      #is received in the parser in the form of dictionary.
        if UserModel.find_by_username(data["username"]):
            return {"Message": "User already exists!"}
        
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        
        return {"Message": "User created successfully!"}, 201