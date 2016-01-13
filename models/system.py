import datetime

from peewee import *

from .base import BaseModel

class System(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    logo = CharField()
    pathToRomFiles = CharField()
    extensions = CharField()
    createdAt = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id) + ": " + self.name

