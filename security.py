# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:20:58 2020

@author: RAVI KANCHAN BHENGRA
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel

def autheticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):   #safe_str_cmp is used so that there is not wrong comparison because of ASCII and unicode encoding.
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
