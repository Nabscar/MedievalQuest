import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('Images', 'Background_Images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        fullname = os.path.join('Images', 'Bat_Images')
        fullname = os.path.join(fullname, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            fullname = os.path.join('Images', 'Misc_Images')
            fullname = os.path.join(fullname, name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:
                fullname = os.path.join('Images', 'Shooter_Images')
                fullname = os.path.join(fullname, name)
                try:
                    image = pygame.image.load(fullname)
                except pygame.error:
                    fullname = os.path.join('Images', 'Troll_Images')
                    fullname = os.path.join(fullname, name)
                    try:
                        image = pygame.image.load(fullname)
                    except pygame.error:
                        fullname = os.path.join('Images', 'King_Images', 'King_OW')
                        fullname = os.path.join(fullname, name)
                        try:
                            image = pygame.image.load(fullname)
                        except pygame.error:
                            fullname = os.path.join('Images', 'King_Images', 'King_Cave')
                            fullname = os.path.join(fullname, name)
                            try:
                                image = pygame.image.load(fullname)
                            except pygame.error:
                                fullname = os.path.join('Images', 'Boss_Images')
                                fullname = os.path.join(fullname, name)
                                try:
                                    image = pygame.image.load(fullname)
                                except pygame.error:
                                    print('Cannot load image:' + fullname)
                                    raise SystemExit

    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    image = pygame.transform.scale(image, (64, 64))
    return image
