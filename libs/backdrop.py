import logging

import sdl2
import sdl2.sdlimage
from ctypes import byref, cast, POINTER, c_int, c_uint8

logger = logging.getLogger('nostalgo.libs')

class Backdrop:
    def __init__(self, currentState):
        self.currentState = currentState
        self.currentSystem = None
        self.text = None
        self.imageWidth = c_int()
        self.imageHeight = c_int()

        sdl2.sdlimage.IMG_Init(sdl2.sdlimage.IMG_INIT_JPG | sdl2.sdlimage.IMG_INIT_PNG)

    def render(self, renderer):
        if self.currentSystem != self.currentState.getCurrentSystem().name:
            image = sdl2.sdlimage.IMG_Load(b"images/backdrops/" + self.currentState.getCurrentSystem().name.encode('utf-8') + b".jpg")
            self.text = sdl2.SDL_CreateTextureFromSurface(renderer, image)
            sdl2.SDL_FreeSurface(image)

            sdl2.SDL_SetTextureBlendMode(self.text, sdl2.SDL_BLENDMODE_BLEND)
            sdl2.SDL_SetTextureAlphaMod(self.text, c_uint8(48))
            sdl2.SDL_QueryTexture(self.text, None, None, byref(self.imageWidth), byref(self.imageHeight))

            self.currentSystem = self.currentState.getCurrentSystem().name

        percent = 720 / self.imageHeight.value
        sdl2.SDL_RenderCopy(renderer, self.text, None, sdl2.SDL_Rect(0, 0, int(self.imageWidth.value * percent), int(self.imageHeight.value * percent)))
