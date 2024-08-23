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
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

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

        BOUNDARY = 'boundary'
        GRASS_REGULAR = 'grass_regular'
        OBJECT_2Y = 'object_2y'
        ENTITIES = 'entities'
        
        for style, layout in layouts.items():
            total_elements = len(layout) * len(layout[0])

            for index in range(total_elements):
                row_index = index // len(layout[0])
                col_index = index % len(layout[0])
                col = layout[row_index][col_index]

                if col == '-1':
                    continue

                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if style == BOUNDARY:
                    Tile((x, y), [self.obstacles_sprites], 'invisible')
                elif style == GRASS_REGULAR:
                    random_grass_image = choice(graphics[GRASS_REGULAR_FOLDER])
                    
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites, self.attackable_sprites], GRASS_REGULAR, random_grass_image)
                elif style == OBJECT_2Y:
                    surf = graphics[OBJECT_2Y_FOLDER][int(col)]

                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites], OBJECT_2Y, surf)
                elif style == ENTITIES:
                    if col == PLAYER_ID:
                        self.player = Player(
                            (x, y),
                            [self.visible_sprites],
                            self.obstacles_sprites,
                            self.create_attack,
                            self.destroy_attack,
                            self.create_magic
                        )
                    else:
                        monster_name = {
                            MONSTER_1_ID: MONSTER_1_NAME,
                            MONSTER_2_ID: MONSTER_2_NAME,
                            MONSTER_3_ID: MONSTER_3_NAME
                        }.get(col, MONSTER_4_NAME)
                        Enemy(
                            monster_name,
                            (x, y),
                            [self.visible_sprites, self.attackable_sprites],
                            self.obstacles_sprites,
                            self.damage_player
                        )            

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        pass

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == GRASS_REGULAR:
                            target_sprite.kill()
                        elif target_sprite.sprite_type == 'enemy':
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)

        pass

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            #spawn particles
        pass

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
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
