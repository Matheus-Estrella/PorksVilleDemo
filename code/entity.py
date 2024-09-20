import pygame
from math import sin
from termsSettings import PLAYER,ENEMY,NPC
from settings import MONSTER_SETTINGS,ENTITY_MAPPING, CHARACTER_DATA,MONSTER_DATA, CHARACTER_IMAGES,HITBOX_OFFSET

class Entity(pygame.sprite.Sprite):
    def __init__(self,sprite_type,obstacle_sprites,pos,sprite_id,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

        self.sprite_type = sprite_type
        self.sprite_id = sprite_id

        # obstacle settings
        self.obstacle_sprites = obstacle_sprites

        # --- Heir definitions --- #

        # common stats
        
        
        # entities attributes
        self.respawn,self.can_attack, self.status,self.stats,self.health,self.energy,self.speed,self.exp,self.base_attack_damage,self.resistance = self.heir_types(pos,sprite_id)

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

    def heir_types(self,pos,sprite_id):
        if self.sprite_type == PLAYER:
            can_attack = False
            status = 'down'

            # -- stats implementation -- #

            stats = CHARACTER_DATA['stats']
            health = stats['health'] * 0.5
            energy = stats['energy'] * 0.8
            speed = stats['speed']
            exp = 0
            base_attack_damage = stats['attack']
            resistance = stats['resistance']
            respawn = stats['respawn']

            return respawn,can_attack,status,stats,health,energy,speed,exp,base_attack_damage,resistance
            pass

        elif self.sprite_type == ENEMY:
            can_attack = True
            status ='idle'

            # -- stats implementation -- #

            stats = None
            for key,entity in ENTITY_MAPPING.items():
                if entity['id'] == sprite_id:
                    stats = MONSTER_DATA[entity['name']]            
            health = stats['health']
            energy = stats['energy']
            speed = stats['speed']
            exp = stats['exp']
            base_attack_damage = stats['damage']
            resistance = stats['resistance']
            respawn = stats['respawn']

            return respawn,can_attack,status,stats,health,energy,speed,exp,base_attack_damage,resistance
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