import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            MAGIC_1 : pygame.mixer.Sound(MAGIC_1_SOUND_FOLDER),
            MAGIC_2 : pygame.mixer.Sound(MAGIC_2_SOUND_FOLDER)
        }
        self.sounds[MAGIC_1].set_volume(MAGIC_1_SOUND_VOLUME)
        self.sounds[MAGIC_2].set_volume(MAGIC_2_SOUND_VOLUME)

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            self.sounds[MAGIC_2].play()
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats[HEALTH]:
                player.health = player.stats[HEALTH]
            self.animation_player.create_particles('aura',player.rect.center,groups)
            self.animation_player.create_particles(MAGIC_2,player.rect.center + pygame.math.Vector2(0,-45),groups)

# TO ADD MORE MAGIC DAMAGES TYPES, SEE: https://youtu.be/QU1pPzEGrqw?t=22974

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            self.sounds[MAGIC_1].play()
            player.energy -= cost
            attack_direction = player.status.split('_')[0]
        if attack_direction == 'right': direction = pygame.math.Vector2(1,0)
        elif attack_direction == 'left': direction = pygame.math.Vector2(-1,0)
        elif attack_direction == 'up': direction = pygame.math.Vector2(0,-1)
        else: direction = pygame.math.Vector2(0,1)

        for i in range(1,6):
            rand_dist = TILESIZE//3
            if direction.x: #horizontal
                offset_x = (direction.x * i) * TILESIZE
                x = player.rect.centerx + offset_x + randint(-rand_dist,rand_dist)
                y = player.rect.centery + randint(-rand_dist,rand_dist)
                self.animation_player.create_particles(MAGIC_1,(x,y),groups)
            else: #vertical
                offset_y = (direction.y * i) * TILESIZE
                x = player.rect.centerx + randint(-rand_dist,rand_dist)
                y = player.rect.centery + offset_y + randint(-rand_dist,rand_dist)
                self.animation_player.create_particles(MAGIC_1,(x,y),groups)