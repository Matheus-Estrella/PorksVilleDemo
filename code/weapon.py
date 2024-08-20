import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__()
        direction = player.status.split('_')[0] #dividindo a palavra pelo _idle, _attack e etc
        self.image = pygame.Surface((40,40))
        self.rect = self.image.get_rect(center = player.rect.center)


        

        #ORIGINAL, QUE PODE ESTAR CAUSANDO ERRO

        # # graphics
        # full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
        # self.image = pygame.image.load(full_path).convert_alpha()

        # # placement
        # if direction == 'right':
        #     self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        # elif direction == 'left':
        #     self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
        # elif direction == 'down':
        #     self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
        # else:
        #     self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))

