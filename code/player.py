import pygame
from debug import Debug
from support import import_folder
from entity import Entity

from termsSettings import *
from settings import HITBOX_OFFSET,BAG_LIST,FORMS_LIST,INITIAL_IMAGE, WEAPONS_LIST,MAGIC_LIST,GAME_SOUNDS,CHARACTER_DATA,CHARACTER_ANIMATIONS,WIDTH, HEIGHT,EASTER_EGG

class Player(Entity):
    def __init__(self,sprite_type,pos,sprite_id,groups,obstacle_sprites, create_attack, destroy_attack,create_magic):

        #general setup
        super().__init__(sprite_type,obstacle_sprites,pos,sprite_id,groups)

        # graphics setup
        self.transforming = False
        self.transformation_index = 0

        # transformations
        self.form = list(FORMS_LIST.keys())[self.transformation_index]
        self.can_switch_form = True
        self.form_switch_time = None
        
        self.animations = {}

        self.image = pygame.image.load(INITIAL_IMAGE['image']).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6,HITBOX_OFFSET[PLAYER])

        self.import_player_assets()

        # dm test mode
        self.dm_mode = False
        self.dm_energy_speed = 0
        self.dm_life_regen_speed = 0
        self.dm_invulnerability = 0 

        # interactions
        self.talking = False
        self.grabbing = False

        # stats
        self.max_stats = CHARACTER_DATA['max_stats']
        self.upgrade_cost = CHARACTER_DATA['upgrade_cost']
        self.energy_fill_speed = 0.01
        self.health_fill_speed = 0.01
        
        # weapon 
        self.create_attack = create_attack
        self.destoy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(WEAPONS_LIST.keys())[self.weapon_index]

        self.can_switch_weapon = True
        self.weapon_switch_time = None
        
        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(MAGIC_LIST.keys())[self.magic_index]
        self.can_switch_magic = True

        # bag
        self.bag_index = 0
        self.bag = list(BAG_LIST.keys())[self.bag_index]
        self.can_switch_bag = True
        self.bag_switch_time = None

        # switch cooldown
        self.switch_duration_cooldown = 200
        self.magic_switch_time = None

        # import sound
        self.weapon_attack_sound = pygame.mixer.Sound(GAME_SOUNDS['weapon']['path'])
        self.weapon_attack_sound.set_volume(GAME_SOUNDS['weapon']['volume'])

        # input settings

        self.last_key_time = 0
        self.key_delay = 150
        
    def change_character_form(self, form_version):
        self.transformation_index = form_version  # '0', '1', etc.
        self.import_player_assets()

    def import_player_assets(self):
        # add puffing particles
        character_folder = f'../graphics/player/{str(self.transformation_index)}/'
        self.animations = {animat: import_folder(character_folder + animat) for animat in CHARACTER_ANIMATIONS}
    
    def detect_code_keypress(self, keys, valid_keys, addicional_time):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_key_time - addicional_time > self.key_delay:
            if all(keys[key] for key in valid_keys):
                self.last_key_time = current_time
                return True
        return False
    
    def input(self):
        if not self.can_attack: # or self.talking or self.transforming or self.grabbing):
            keys = pygame.key.get_pressed()

            # Movement Input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            # Attack input
            if keys[pygame.K_SPACE]:
                self.can_attack = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()
            
            # Magic input
            if keys[pygame.K_LCTRL]:
                self.can_attack = True
                self.attack_time = pygame.time.get_ticks()
                style = MAGIC_LIST[list(MAGIC_LIST.keys())[self.magic_index]]['magic_name']
                strength = list(MAGIC_LIST.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(MAGIC_LIST.values())[self.magic_index]['cost']

                self.create_magic(style,strength,cost)

            # Switch form input
            if keys[pygame.K_1] and self.can_switch_form:
                self.can_switch_form = False
                self.form_switch_time = pygame.time.get_ticks()

                if self.transformation_index < len(list(FORMS_LIST.keys())) -1:
                    self.transformation_index += 1
                else:
                    self.transformation_index = 0
                self.form = list(FORMS_LIST.keys())[self.transformation_index]

            # Switch bag input
            if keys[pygame.K_2] and self.can_switch_bag:
                self.can_switch_bag = False
                self.bag_switch_time = pygame.time.get_ticks()

                if self.bag_index < len(list(BAG_LIST.keys())) -1:
                    self.bag_index += 1
                else:
                    self.bag_index = 0
                self.bag = list(BAG_LIST.keys())[self.bag_index]

            # Switch weapon input
            if keys[pygame.K_3] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(WEAPONS_LIST.keys())) -1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(WEAPONS_LIST.keys())[self.weapon_index]

            # Switch magic input
            if keys[pygame.K_4] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(MAGIC_LIST.keys())) -1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(MAGIC_LIST.keys())[self.magic_index]

            
            # Master Mode On/Off
                # adjust the debug easter egg of hacker on and off to linger more on screen
            master_keys = {pygame.K_p, pygame.K_o, pygame.K_r, pygame.K_k}
            if self.detect_code_keypress(keys, master_keys,50):
                self.dm_mode = not self.dm_mode

                debug_x = WIDTH*0.5 - 64
                debug_y = HEIGHT*0.5 - 64

                if self.dm_mode:
                    self.dm_energy_speed = 0.09
                    self.dm_life_regen_speed = 0.04
                    self.dm_invulnerability = 500
                    self.exp += 500
                    Debug("HACKER ON",debug_x,debug_y,'blue')
                else:
                    self.dm_energy_speed = 0.0
                    self.dm_invulnerability = 0 
                    Debug("HACKER OFF",debug_x,debug_y,'red')              

            # -- NEW IMPLEMENTATIONS FOR THE GAMING -- #

            # bag input   ---> configure later
            if keys[pygame.K_b]:
                pass
                self.grabbing = not self.grabbing
                if self.grabbing:
                    # if is grabbing
                    self.can_attack = False
                else:
                    self.can_attack = True
                
                self.attack_time = pygame.time.get_ticks()
                pass

            # grab input   ---> configure later
            if keys[pygame.K_g]:
                pass

            # interact input   ---> configure later
            if keys[pygame.K_i]:
                pass

            # transform   ---> configure later
            if keys[pygame.K_t] and not self.transforming:
                self.transforming = True

                # adicionar efeito de transição de formas quando estado mudar
                # para isto, utilizar sistema de drop da lápide e check_death
                # se for da key 0,1, 2, 3 ou 4, transformar no personagem 0,1,2,3,4
                # self.character_form deve se igualar a este valor, para baixar a imagem correta
                # após configurar recursos de comida / energia, setá-las para as formas, caso zerado o atual, retorna ao 0

    def get_status(self):
        # CONFIGURAR OUTROS STATUS QUE NÃO SEJAM O ATTACKING
        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.can_attack:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attack_time:
            if current_time - self.attack_time >= self.attack_cooldown + WEAPONS_LIST[self.weapon]['cooldown']:
                self.can_attack = False
                self.destoy_attack()

        # switching form setups
        if not self.can_switch_form:
            if current_time - self.form_switch_time >= self.switch_duration_cooldown:
                self.can_switch_form = True

        # switching bag setups
        if not self.can_switch_bag:
            if current_time - self.bag_switch_time >= self.switch_duration_cooldown:
                self.can_switch_bag = True

        # switching weapons setups
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        # switching magic setups
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True
        
        # damaged setups
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration + self.dm_invulnerability:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]
        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index =0
        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        # add flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        weapon_damage = WEAPONS_LIST[self.weapon]['damage']
        return self.base_attack_damage+weapon_damage
    
    def get_full_magic_damage(self):
        magic_damage = MAGIC_LIST[self.magic]['strength']
        return self.base_attack_damage+magic_damage

    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += (self.energy_fill_speed + self.dm_energy_speed) * self.stats['magic']
        else:
            self.energy = self.stats['energy']

        if self.health < self.stats['health'] and self.dm_mode:
            self.health += (self.health_fill_speed + self.dm_life_regen_speed) * self.stats['magic']

    def get_value_by_index(self,index):
        return list(self.stats.values())[index]

    def get_cost_by_index(self,index):
        return list(self.upgrade_cost.values())[index]


    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()


