import pygame
from settings import *
from tile import Tile
from player import Player
from debug import Debug

class Level:
    def __init__(self):
        # level counter
        self.level_number = 1

        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        if self.level_number in WORLD_MAPS:
            current_map = WORLD_MAPS[self.level_number]
            for row_index,row in enumerate(current_map):
                for col_index,col in enumerate(row):
                    x = TEILESIZE * col_index
                    y = TEILESIZE * row_index
                    if col == 'x':
                        Tile((x,y),[self.visible_sprites, self.obstacles_sprites])
                    if col == 'p': 
                        self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)


    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        Debug(self.player.direction) # enables direction print on screen

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width 
		self.offset.y = player.rect.centery - self.half_height

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)