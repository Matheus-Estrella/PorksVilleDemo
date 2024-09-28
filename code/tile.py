import pygame

from settings import HITBOX_OFFSET,TILESIZE
from termsSettings import LARGE_OBJECTS


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,sprite_id,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == LARGE_OBJECTS: #ajusting large objects
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,y_offset)