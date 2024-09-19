import pygame
from random import randint
from settings import MAGIC_LIST, TILESIZE

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            MAGIC_LIST[str(0)]['magic_name'] : pygame.mixer.Sound(MAGIC_LIST[str(0)]['sound_folder']),
            MAGIC_LIST[str(1)]['magic_name']  : pygame.mixer.Sound(MAGIC_LIST[str(1)]['sound_folder'])
        }
        self.sounds[MAGIC_LIST[str(0)]['magic_name']].set_volume(MAGIC_LIST[str(0)]['volume'])
        self.sounds[MAGIC_LIST[str(1)]['magic_name']].set_volume(MAGIC_LIST[str(1)]['volume'])

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            self.sounds[MAGIC_LIST[str(1)]['magic_name']].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles(MAGIC_LIST[str(1)]['sub_magic_name'],player.rect.center,groups)
            self.animation_player.create_particles(MAGIC_LIST[str(1)]['magic_name'],player.rect.center + pygame.math.Vector2(0,-45),groups)

# TO ADD MORE MAGIC DAMAGES TYPES, SEE: https://youtu.be/QU1pPzEGrqw?t=22974

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            self.sounds[MAGIC_LIST[str(0)]['magic_name']].play()
            player.energy -= cost
            attack_direction = player.status.split('_')[0]

            if attack_direction == 'right': direction = pygame.math.Vector2(1,0)
            elif attack_direction == 'left': direction = pygame.math.Vector2(-1,0)
            elif attack_direction == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)

            
            for i in range(1,MAGIC_LIST[str(0)]['attack_amount']):
                rand_dist = TILESIZE//3
                
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-rand_dist,rand_dist)
                    y = player.rect.centery + randint(-rand_dist,rand_dist)
                    self.animation_player.create_particles(MAGIC_LIST[str(0)]['magic_name'],(x,y),groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-rand_dist,rand_dist)
                    y = player.rect.centery + offset_y + randint(-rand_dist,rand_dist)
                    self.animation_player.create_particles(MAGIC_LIST[str(0)]['magic_name'],(x,y),groups)