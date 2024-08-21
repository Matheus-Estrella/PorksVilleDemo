import pygame
from debug import Debug
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites, create_attack, destoy_attack):
        super().__init__(groups)
        self.image = pygame.image.load(TEST_PLAYER).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.character_form = 0

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.talking = False
        self.transforming = False
        self.grabbing = False

        self.obstacle_sprites = obstacle_sprites

        # weapon
        self.create_attack = create_attack
        self.destoy_attack = destoy_attack
        self.weapon_index = 0
        self.weapon = list(WEAPON_DATA.keys())[self.weapon_index]

        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_duration_cooldown = 200
        
        # stats
        self.stats = STATS
        self.health = self.stats[HEALTH] * 0.5
        self.energy = self.stats[ENERGY] * 0.8
        self.speed = self.stats[SPEED]
        self.exp = 0

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
            
            # Power input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()

            # Switch weapon input
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(WEAPON_DATA.keys())) -1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(WEAPON_DATA.keys())[self.weapon_index]
            
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


    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() #diagonal vector as 1 move
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        #self.rect.center += self.direction * speed

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

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attack_time:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destoy_attack()
        #switching weapons setups
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.weapon_switch_duration_cooldown:
                self.can_switch_weapon = True

    def animate(self):
        animation = self.animations[self.status]
        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index =0
        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)


