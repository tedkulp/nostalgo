import datetime

from peewee import *

from . import logger
from .base import BaseModel
from .rom import Rom

class Asset(BaseModel):
    id = PrimaryKeyField()
    type = CharField(default="image")
    width = IntegerField(null=True)
    height = IntegerField(null=True)
    fullFilename = CharField()
    rom = ForeignKeyField(Rom, related_name="assets")
    createdAt = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id) + ": " + self.fullFilename
