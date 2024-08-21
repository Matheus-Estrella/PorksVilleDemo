import pygame
from settings import *
from tile import Tile
from player import Player
from debug import Debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy

class Level:
    def __init__(self):
        # level counter
        self.level_number = 0

        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup(self.level_number)
        self.obstacles_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None

        #sprite setup
        self.create_map()

        #user interface
        self.ui = UI()

    def create_map(self):
        level = self.level_number
        layouts = {
            'boundary': import_csv_layout(MAPS_BOUNDARIES[level]),
            'grass' : import_csv_layout(MAPS_GRASSES[level]),
            'object' : import_csv_layout(MAPS_OBJECTS[level]),
            'entities' : import_csv_layout(MAPS_ENTITIES[level])
        }
        
        graphics = {
            'grass' : import_folder(GRAPHIC_GRASS[level]),
            'objects' : import_folder(GRAPHIC_OBJECTS[level])
        }
        
        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate (row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacles_sprites],'invisible')
                        if style == GRASS_REGULAR:
                            random_grass_image = choice(graphics[GRASS_REGULAR_FOLDER])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],GRASS_REGULAR,random_grass_image)
                        if style == OBJECT_2Y:
                            surf = graphics[OBJECT_2Y_FOLDER][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],OBJECT_2Y,surf)
                        if style == ENTITIES:
                            if col == PLAYER_ID:
                                self.player = Player( # adding player on map with its level functions
                                    (x,y),
                                    [self.visible_sprites],
                                    self.obstacles_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic
                                )
                            else:
                                if col == MONSTER_1_ID: monster_name = MONSTER_1_NAME
                                elif col == MONSTER_2_ID: monster_name = MONSTER_2_NAME
                                elif col == MONSTER_3_ID: monster_name = MONSTER_3_NAME
                                else: monster_name = MONSTER_4_NAME
                                Enemy(monster_name,(x,y),[self.visible_sprites],self.obstacles_sprites)            

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])

    def create_magic(self,style,strength,cost):
        pass

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)
        #Debug(self.player.direction) # enables direction print on screen
        #Debug(self.player.status) # enables status print on screen
        #Debug(self.player.weapon) 

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, level_number):
        # general setup 
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surface = pygame.image.load(GROUNDIMAGE[level_number]).convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset 
        self.offset.x = player.rect.centerx - self.half_width 
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
