import pygame
from debug import Debug
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites, create_attack, destoy_attack,create_magic):
        super().__init__(groups)
        self.image = pygame.image.load(TEST_PLAYER).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6,HITBOX_OFFSET['player'])
        self.character_form = 0

        # graphics setup
        self.import_player_assets()
        self.status = 'down'

        # movement
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.talking = False
        self.transforming = False
        self.grabbing = False

        self.obstacle_sprites = obstacle_sprites

        # cooldown
        self.switch_duration_cooldown = 200

        # weapon
        self.create_attack = create_attack
        self.destoy_attack = destoy_attack
        self.weapon_index = 0
        self.weapon = list(WEAPON_DATA.keys())[self.weapon_index]

        self.can_switch_weapon = True
        self.weapon_switch_time = None
        
        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(MAGIC_DATA.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # stats
        self.stats = STATS
        self.max_stats = MAX_STATS
        self.upgrade_cost = UPGRADE_COST
        self.health = self.stats[HEALTH] * 0.5
        self.energy = self.stats[ENERGY] * 0.8
        self.speed = self.stats[SPEED]
        self.exp = 500
        self.energy_fill_speed = 0.01
        self.dm_energy_speed = 0.09
        self.health_fill_speed = 0.01

        # damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500
        self.dm_invulnerability = 4500 # just to easier the tests

        # import sound
        self.weapon_attack_sound = pygame.mixer.Sound(WEAPON_ATTACK_SOUND_FOLDER)
        self.weapon_attack_sound.set_volume(WEAPON_ATTACK_SOUND_VOLUME)

    def import_player_assets(self):
        self.animations = CHARACTER_ANIMATIONS
        for animation in self.animations.keys():
            full_path = CHARACTER_FOLDER + animation
            self.animations[animation] = import_folder(full_path)

    # movement
    def input(self):
        if not self.attacking: # or self.talking or self.transforming or self.grabbing):
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
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()
            
            # Magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(MAGIC_DATA.keys())[self.magic_index]
                strength = list(MAGIC_DATA.values())[self.magic_index]['strength'] + self.stats[MAGIC]
                cost = list(MAGIC_DATA.values())[self.magic_index]['cost']

                self.create_magic(style,strength,cost)

            # Switch weapon input
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(WEAPON_DATA.keys())) -1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(WEAPON_DATA.keys())[self.weapon_index]

            # Switch magic input
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(MAGIC_DATA.keys())) -1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(MAGIC_DATA.keys())[self.magic_index]
            
            # ABAIXO DESTAS LINHAS HÁ AS CONFIGURAÇÕES ADICIONAIS PARA PORKSVILLE
            # ENTRETANTO, FORAM IDENTADAS (CONTRA IDENTAR AO IMPLEMENTAR) E COMENTADAS (DESCOMENTAR AO IMPLEMENTAR)
            # POIS SUAS ANIMAÇÕES NÃO FORAM DEFINIDAS ATÉ O MOMENTO, ENTÃO, O ACIONAMENTO DESTAS TECLAS ADICIONAIS
            # CAUSAM ERRO NA ANIMAÇÃO, BLOQUEANDO OUTRAS
            # ORGANIZAR COM FRONT E TAMBÉM VERIFICAR AS POSSIBILIDADES DE IMPLEMENTAÇÃO DA ANIMAÇÃO
            # (SEJA DIRETAMENTE, COMO ATAQUE, OU INDIRETAMENTE, COMO PODER DE CURA DO TUTORIAL)

            # Eat input   ---> configure latter
            if keys[pygame.K_f]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
            
            # Grab input   ---> configure latter
            if keys[pygame.K_g]:
                self.attacking = True
                self.grabbing = True
                self.attack_time = pygame.time.get_ticks()

            # Talk input   ---> configure latter
            if keys[pygame.K_t] and not self.talking:
                self.talking = True

            # Talk input   ---> configure latter
            valid_keys = {pygame.K_0,pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4}
            if any(keys[key] for key in valid_keys) and not self.transforming:
                self.transforming = True
                # para mudanças abaixo comentadas, será necessário rearanjar a pasta do personagem para acessá-la pela indice
                # ex:  '../graphics/player/{self.character_form}'
                # adicionar efeito de transição de formas quando estado mudar
                # se for da key 0,1, 2, 3 ou 4, transformar no personagem 0,1,2,3,4
                # self.character_form deve se igualar a este valor, para baixar a imagem correta
                # após configurar recursos de comida / energia, setá-las para as formas, caso zerado o atual, retorna ao 0

    def get_status(self):
        # CONFIGURAR OUTROS STATUS QUE NÃO SEJAM O ATTACKING
        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
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
            if current_time - self.attack_time >= self.attack_cooldown + WEAPON_DATA[self.weapon]['cooldown']:
                self.attacking = False
                self.destoy_attack()

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
        base_damage = self.stats['attack']
        weapon_damage = WEAPON_DATA[self.weapon]['damage']
        return base_damage+weapon_damage
    
    def get_full_magic_damage(self):
        base_damage = self.stats['attack']
        magic_damage = MAGIC_DATA[self.magic]['strength']
        return base_damage+magic_damage

    def energy_recovery(self):
        if self.energy < self.stats[ENERGY]:
            self.energy += (self.energy_fill_speed + self.dm_energy_speed) * self.stats[MAGIC]
        else:
            self.energy = self.stats[ENERGY]

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


