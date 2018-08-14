import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except (pygame.error, message):
        print ('Cannot load image:', name)
        raise (SystemExit, message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def distancia_objetos(obj1,obj2):
    pass


def iniciar():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Proyecto')
    pygame.mouse.set_visible(0)

def exit():
    sys.exit()


