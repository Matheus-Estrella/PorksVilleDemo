import pygame
from entity import Entity
from support import import_folder
from settings import MONSTER_DATA, MONSTER_SETTINGS

class Enemy(Entity):
    def __init__(self,sprite_type,monster_name,pos,sprite_id,groups,obstacle_sprites,damage_player,trigger_death_particles,add_exp,get_score):
    
        #general setup
        super().__init__(sprite_type,obstacle_sprites,pos,sprite_id,groups)
        
        # graphics setup
        self.import_graphics(monster_name)

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)

        # stats
        self.monster_name = monster_name
        self.attack_radius = self.stats['attack_radius']
        self.notice_radius = self.stats['notice_radius']
        self.attack_type = self.stats['attack_type']

        # player interaction
        self.add_exp = add_exp
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.get_score = get_score

        # sounds
        self.hit_sound = pygame.mixer.Sound(MONSTER_SETTINGS['hit_sound'])
        self.attack_sound = pygame.mixer.Sound(self.stats['attack_sound'])
        self.hit_sound.set_volume(MONSTER_SETTINGS['hit_sound_volume'])
        self.attack_sound.set_volume(MONSTER_SETTINGS['monster_attack_sound_volume'])
    

    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        main_path = f"{MONSTER_SETTINGS['folder']}{name}/"
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude() #magnitude converts vector in distance
        if distance >0:
            direction = (player_vec - enemy_vec).normalize()  # normalize to make a vector only of 1, and then, apply speed
        else: # when enemy is in the same space as the player
            direction = pygame.math.Vector2()

        return (distance,direction)

    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        # setting the animation status for enemy response
        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.base_attack_damage,self.attack_type)
            self.attack_sound.play()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()      

    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def get_damage(self,player,attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_magic_damage()
                #magic damage -- > For anothers spells attack, change here
            self.hurt_time = pygame.time.get_ticks()
            self.vulnerable = False
        
    def check_death(self): # ---------> COULD BE ON ENTITIES?
        if self.health <= 0:
            self.kill()
            self.get_score()
            self.trigger_death_particles(self.rect.center,self.monster_name)
            self.add_exp(self.exp)
            self.death_sound.play()

    def hit_reaction(self): # ---------> COULD BE ON ENTITIES or GRASSES?
        if not self.vulnerable:
            self.direction *= -self.resistance #pushback 

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldown()
        self.check_death()

    # this is like a interaction system with the player
    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)