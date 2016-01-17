import logging
import sys
import sdl2
import sdl2.ext

from libs.database import db
from models.rom import Rom
from models.system import System
from models.asset import Asset

from libs.currentstate import CurrentState
from libs.backdrop import Backdrop
from libs.gamelist import GameList
from libs.emulatorrunner import EmulatorRunner

FORMAT = '%(asctime)s - %(name)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT)
logger = logging.getLogger('nostalgo')

def run():
    db.connect()
    db.create_tables([Rom, System, Asset], safe=True)

    window = sdl2.SDL_CreateWindow(b"Nostalgo", sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, 1280, 720, sdl2.SDL_WINDOW_SHOWN)
    renderer = sdl2.SDL_CreateRenderer(window, -1, sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_PRESENTVSYNC)
    sdl2.SDL_SetRenderDrawBlendMode(renderer, sdl2.SDL_BLENDMODE_BLEND)

    currentState = CurrentState(window=window, db=db)
    backdrop = Backdrop(currentState)
    gameList = GameList(currentState)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym in [sdl2.SDLK_RETURN]:
                    EmulatorRunner(currentState.getCurrentSystem(), currentState.getCurrentRom()).run()
                elif event.key.keysym.sym in [sdl2.SDLK_RIGHT, sdl2.SDLK_n]:
                    currentState.incrementSystem()
                elif event.key.keysym.sym in [sdl2.SDLK_LEFT, sdl2.SDLK_p]:
                    currentState.decrementSystem()
                elif event.key.keysym.sym in [sdl2.SDLK_UP, sdl2.SDLK_k]:
                    currentState.decrementRom()
                elif event.key.keysym.sym in [sdl2.SDLK_DOWN, sdl2.SDLK_j]:
                    currentState.incrementRom()
                elif event.key.keysym.sym in [sdl2.SDLK_ESCAPE, sdl2.SDLK_q]:
                    running = False
                    break

        sdl2.SDL_Delay(20)

        sdl2.SDL_RenderClear(renderer)
        backdrop.render(renderer)
        gameList.render(renderer)
        sdl2.SDL_RenderPresent(renderer)

if __name__ == "__main__":
    sys.exit(run())
