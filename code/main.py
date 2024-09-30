import time 
import pygame, sys, os
from debug import Debug
from level import Level
from settings import GAME_SOUNDS, FPS, WIDTH, HEIGHT, COLORS_SETTINGS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PorksVille')
        self.clock = pygame.time.Clock()
        self.level = Level()

        self.font = pygame.font.Font(None, 36)

        main_sound = pygame.mixer.Sound(GAME_SOUNDS['main']['path'])
        main_sound.set_volume(GAME_SOUNDS['main']['volume'])
        main_sound.play(loops=-1)

        # Outros atributos
        self.end_game_active = False
        self.end_game_start_time = None
        self.end_game_cooldown = 2000  # Tempo em milissegundos para aguardar
        self.end_game_cooldown_start = None
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.pause_game_menu()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL] and keys[pygame.K_w]:
                pygame.quit()
                sys.exit()
                
            if self.level.get_end_game():
                if not self.end_game_active:
                    self.end_game_active = True
                    self.end_game_start_time = time.time()

            self.screen.fill(COLORS_SETTINGS['water_color'])
            self.level.run()
            self.end_game_prompt()
            pygame.display.update()
            self.clock.tick(FPS)

    def end_game_prompt(self):
        if self.end_game_active:
            elapsed_time = time.time() - self.end_game_start_time
            if elapsed_time < 5:
                text_surf = self.font.render(f'PARABÉNS, VOCÊ SALVOU A NATUREZA HOJE (FECHANDO EM {round(5 - elapsed_time)}...)', True, COLORS_SETTINGS['text_color'])
                screen_width = 1280
                screen_height = 720
                text_rect = text_surf.get_rect(center=(screen_width // 2, screen_height // 2))
                box_width = text_rect.width + 20
                box_height = text_rect.height + 20
                box_rect = pygame.Rect((screen_width // 2) - (box_width // 2), (screen_height // 2) - (box_height // 2), box_width, box_height)

                pygame.draw.rect(self.screen, (255, 255, 255), box_rect)
                pygame.draw.rect(self.screen, (140, 132, 255), text_rect.inflate(40, 40))
                pygame.draw.rect(self.screen, (200, 200, 200), text_rect.inflate(40, 40), 3)
                self.screen.blit(text_surf, text_rect)
            else:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
