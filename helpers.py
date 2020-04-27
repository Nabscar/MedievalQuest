import os, sys
import pygame
from pygame.locals import *

def load_image(name, x = 64, y = 64):
    """Although horrible this nest of try-excepts goes through all the folders of Images until it finds the intended image"""
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
                                fullname = os.path.join('Images', 'Castle_Images')
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

    """Create and return the image"""
    image = image.convert()
    image = pygame.transform.scale(image, (x, y))
    return image
