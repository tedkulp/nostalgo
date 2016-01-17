import logging
import subprocess

logger = logging.getLogger('nostalgo.libs')

class EmulatorRunner:
    def __init__(self, system, rom):
        self.system = system
        self.rom = rom

    def run(self):
        logger.info("Run '%s' '%s'", self.system, self.rom)
        if self.system.name == 'nes':
            ret = subprocess.call(['fceux', self.rom.fullFilename])
        elif self.system.name == 'snes':
            ret = subprocess.call(['open', '-Wa', '/opt/homebrew-cask/Caskroom/snes9x/1.53/Snes9x.app', self.rom.fullFilename])
        logger.info('Return %s', ret)
