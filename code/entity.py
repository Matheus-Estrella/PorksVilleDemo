import pygame
from math import sin
from termsSettings import PLAYER,ENEMY,NPC
from settings import MONSTER_SETTINGS, CHARACTER_IMAGES,HITBOX_OFFSET

class Entity(pygame.sprite.Sprite):
    def __init__(self,sprite_type,obstacle_sprites,pos,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

        self.sprite_type = sprite_type

        # obstacle settings
        self.obstacle_sprites = obstacle_sprites

        # --- Heir definitions --- #
        
        #graphics
        self.can_attack, self.status = self.heir_types(pos)

        # attacking
        self.attack_cooldown = 400
        self.attack_time = None

        # sounds
        self.death_sound = pygame.mixer.Sound(MONSTER_SETTINGS['death_sound'])
        self.death_sound.set_volume(MONSTER_SETTINGS['death_sound_volume'])

        # damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

    def heir_types(self,pos):
        if self.sprite_type == PLAYER:
            can_attack = False
            status = 'down'
            return can_attack,status
            pass

        elif self.sprite_type == ENEMY:
            can_attack = True
            status ='idle'
            return can_attack,status
            pass

        elif self.sprite_type == NPC:
            pass
        else:
            pass

        
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() #diagonal vector as 1 move
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction): #for static collisions
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x <0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y <0:
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: 
            return 255
        else: 
            return 0