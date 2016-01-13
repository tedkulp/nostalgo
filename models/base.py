from peewee import *
from libs.database import db

class BaseModel(Model):
    class Meta:
        database = db
