import pygame
from math import sin
from settings import PLAYER,ENEMY

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups,sprite_type,pos,obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

        #graphics setup
        self.status = self.set_attributes()['status']

        # movement
        self.obstacle_sprites = obstacle_sprites

    def set_attributes(self):
        if self.sprite_type == PLAYER:
            return {'status':'down'}
        elif self.sprite_type == ENEMY:
            return {'status':'idle'}
        
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