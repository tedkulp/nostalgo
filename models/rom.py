import datetime

from peewee import *

from . import logger
from .base import BaseModel
from .system import System

class Rom(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    filename = CharField()
    fullFilename = CharField()
    description = TextField()
    system = ForeignKeyField(System, related_name="roms")
    timesPlayed = IntegerField()
    gamesDbId = IntegerField()
    createdAt = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id) + ": " + self.name
