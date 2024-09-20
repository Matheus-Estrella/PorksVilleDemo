import pygame
from tile import Tile
from player import Player
from debug import Debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magics import MagicPlayer
from upgrade import Upgrade

from termsSettings import *
from settings import LEVEL_IMAGES,ENTITY_MAPPING, MAGIC_LIST,INTERACTIONS_MAPPING, TILESIZE

class Level:
    def __init__(self):
        # level counter
        self.level_number = 0

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

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
        self.upgrade = Upgrade(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

    def create_map(self):
        layouts = {
            BOUNDARY: import_csv_layout(LEVEL_IMAGES[str(self.level_number)][BOUNDARY]),
            PROP : import_csv_layout(LEVEL_IMAGES[str(self.level_number)][PROP]),
            LARGE_OBJECTS : import_csv_layout(LEVEL_IMAGES[str(self.level_number)][LARGE_OBJECTS]),
            ENTITY : import_csv_layout(LEVEL_IMAGES[str(self.level_number)][ENTITY])
        }
        
        graphics = {
            PROP : import_folder(LEVEL_IMAGES[str(self.level_number)][GRAPHIC_PROP]),
            LARGE_OBJECTS : import_folder(LEVEL_IMAGES[str(self.level_number)][GRAPHIC_OBJECTS])
        }
        
        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate (row):
                    if col != INTERACTIONS_MAPPING[0]['id']:
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == INTERACTIONS_MAPPING[0]['name']:
                            Tile((x,y),col,[self.obstacles_sprites],INTERACTIONS_MAPPING[0]['name'])
                        if style == PROP:
                            random_props_image = choice(graphics[PROP])
                            Tile((x,y),col,
                                 [self.visible_sprites,self.obstacles_sprites,self.attackable_sprites],
                                 PROP,random_props_image)
                        if style == LARGE_OBJECTS:
                            surf = graphics[LARGE_OBJECTS][int(col)]
                            Tile((x,y),col,[self.visible_sprites,self.obstacles_sprites],LARGE_OBJECTS,surf)
                        if style == ENTITY:
                            # analyzing interactive column type that has a programming background
                            # if entity == player
                            if col == ENTITY_MAPPING[0]['id']:
                                self.player = Player(
                                    PLAYER,
                                    (x,y),col,
                                    [self.visible_sprites],
                                    self.obstacles_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic
                                )
                                # if entity == enemy or npc
                            else:
                                monster_name = None
                                entity_type = None
                                for index in ENTITY_MAPPING.values():
                                    if index['id'] == col:
                                        monster_name = index['name']
                                        entity_type = index['entity_type']
                                        break
                                if(entity_type == ENEMY):
                                    Enemy(
                                        ENEMY,
                                        monster_name,
                                        (x,y),col,
                                        [self.visible_sprites, self.attackable_sprites],
                                        self.obstacles_sprites,
                                        self.damage_player,
                                        self.trigger_death_particles,
                                        self.add_exp) 
                                else: 
                                    # further implementations for NPC class (or others)
                                    pass           

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        if style == MAGIC_LIST[str(0)]['magic_name']: #flame
            self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])
            pass
        if style == MAGIC_LIST[str(1)]['magic_name']: #heal
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])
            pass
        else:
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
                        if target_sprite.sprite_type == PROP:
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0,75)
                            for fading in range(randint(3,6)):
                                self.animation_player.create_fading_particles(pos - offset,[self.visible_sprites])
                            target_sprite.kill()
                        elif target_sprite.sprite_type == ENEMY:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            #spawn particles
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])
        
    def trigger_death_particles(self,pos,particle_type):
        self.animation_player.create_particles(particle_type,pos,self.visible_sprites)
        
    def add_exp(self,amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused
        pass

    def run(self):
        
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        
        if self.game_paused:
            # display upgrade menu
            self.upgrade.display()
            
        else:
            #run the game
            #update and draw the game
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()
            #Debug(self.player.direction) # enables direction print on screen
            #Debug(self.player.status) # enables status print on screen
            #Debug(self.player.weapon) 

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, level):
        # general setup 
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surface = pygame.image.load(LEVEL_IMAGES[str(level)][BACKGROUND]).convert()
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