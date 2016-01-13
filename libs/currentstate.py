import logging

import sdl2
import sdl2.ext

from models.system import System

logger = logging.getLogger('nostalgo.libs')

class CurrentState:
    def __init__(self, **kargs):
        self.window = kargs.get("window", None)
        self.db = kargs.get("db", None)

        self.systems = []
        self.systemIdx = kargs.get("currentSystem", self.getDefaultSystem())
        self.roms = []
        self.romIdx = kargs.get("currentRom", self.getDefaultRom())

        logger.debug("Current System: %s", self.getCurrentSystem())
        logger.debug("Current Rom: %s", self.getCurrentRom())

    def getDefaultSystem(self):
        self.loadSystems()
        return 1;

    def getDefaultRom(self):
        self.loadRoms()
        return 0;

    def getCurrentSystem(self):
        if len(self.systems) > self.systemIdx:
            return self.systems[self.systemIdx];
        else:
            return None

    def incrementSystem(self):
        self.systemIdx += 1
        if (self.systemIdx >= len(self.systems)):
            self.systemIdx = 0;

        self.loadRoms()

        logger.debug("Current System: %s", self.getCurrentSystem())

    def decrementSystem(self):
        self.systemIdx -= 1
        if (self.systemIdx < 0):
            if len(self.systems) > 0:
                self.systemIdx = len(self.systems) - 1;
            else:
                self.systemIdx = 0

        self.loadRoms()

        logger.debug("Current System: %s", self.getCurrentSystem())

    def getCurrentRom(self):
        if len(self.roms) > self.romIdx:
            return self.roms[self.romIdx];
        else:
            return None

    def incrementRom(self):
        self.romIdx += 1
        if (self.romIdx >= len(self.roms)):
            self.romIdx = 0;

        logger.debug("Current Rom: %s", self.getCurrentRom())

    def decrementRom(self):
        self.romIdx -= 1
        if (self.romIdx < 0):
            if len(self.roms) > 0:
                self.romIdx = len(self.roms) - 1;
            else:
                self.romIdx = 0

        logger.debug("Current Rom: %s", self.getCurrentRom())

    def loadSystems(self):
        self.systems = System.select()

    def loadRoms(self):
        if self.getCurrentSystem():
            self.roms = self.getCurrentSystem().roms.select()
