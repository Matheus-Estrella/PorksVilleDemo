import pygame
from settings import WEAPONS_FOLDER, WEAPONS_LIST, WEAPONS_DISPLAY_ADJUST
from debug import Debug

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]  # dividindo a palavra pelo _idle, _attack e etc.

        # graphic
        full_path = f'{WEAPONS_FOLDER}{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement adjust
        pos_adj = self.get_weapon_position_adjust(player.weapon, direction)  # Chamada do método

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0 + pos_adj[0], 16 + pos_adj[1]))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0 + pos_adj[0], 16 + pos_adj[1]))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10 + pos_adj[0], 0 + pos_adj[1]))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10 + pos_adj[0], 0 + pos_adj[1]))

        '''para refinar as posições de armas em função do sprite confirmado no frontend para testes de ajustes
        Alterá-las em WEAPONS_DISPLAY_ADJUST para cada arma'''
        
    def get_weapon_position_adjust(self, weapon, direction): 
        if weapon in WEAPONS_DISPLAY_ADJUST and direction in WEAPONS_DISPLAY_ADJUST[weapon]:
            adj = WEAPONS_DISPLAY_ADJUST[weapon][direction]
            return [adj['x'], adj['y']]



