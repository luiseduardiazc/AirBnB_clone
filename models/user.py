#!/usr/bin/python3
''' Module that manage User
'''

# aplication imports
from models.base_model import BaseModel


class User(BaseModel):
    ''' User that inherits from BaseModel '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
