import pygame
from settings import *
from debug import Debug

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)

