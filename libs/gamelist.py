import sdl2
import sdl2.sdlttf
from ctypes import byref, cast, POINTER, c_int

WHITE = sdl2.SDL_Color(255, 255, 255)
BLACK = sdl2.SDL_Color(0, 0, 0)
RED = sdl2.SDL_Color(255, 32, 32)

class GameList:
    def __init__(self, currentState):
        self.currentState = currentState

        sdl2.sdlttf.TTF_Init()
        self.font = sdl2.sdlttf.TTF_OpenFont(b"fonts/PTS55F.ttf", 28)

    def render(self, renderer):
        i = 0
        for game in self.currentState.roms:
            currentColor = WHITE
            if self.currentState.getCurrentRom() == game:
                currentColor = RED

            surf = sdl2.sdlttf.TTF_RenderText_Blended(self.font, game.name.encode("utf-8"), currentColor).contents
            text = sdl2.SDL_CreateTextureFromSurface(renderer, surf)
            sdl2.SDL_SetTextureBlendMode(text, sdl2.SDL_BLENDMODE_BLEND)
            sdl2.SDL_FreeSurface(surf)

            w, h = c_int(), c_int()
            sdl2.SDL_QueryTexture(text, None, None, byref(w), byref(h))
            sdl2.SDL_RenderCopy(renderer, text, None, sdl2.SDL_Rect(50, 50 + (i * 40), w, h))

            i += 1
