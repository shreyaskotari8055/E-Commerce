from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime

class User(Model):
    id =  fields.IntField(pk= True, index= True)
    username = fields.CharField(max_length= 20,null= False,unique= True)
    email = fields.CharField(max_length= 200,null= False, unique= True)
    password = fields.CharField(max_length= 16, null= False)
    is_verified = fields.BooleanField(default= False)
    join_date = fields.DateField(default= datetime.utcnow)


class Business(Model):
    id = fields.IntField(pk= True, index= True)