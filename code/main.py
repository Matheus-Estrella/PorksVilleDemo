import pygame,sys
from debug import Debug
from level import Level
from settings import GAME_SOUNDS,FPS,WIDTH,HEIGHT,COLORS_SETTINGS

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('PorksVille')
        self.clock = pygame.time.Clock()
        self.level = Level()

        #sound
        main_sound = pygame.mixer.Sound(GAME_SOUNDS['main']['path'])
        main_sound.set_volume(GAME_SOUNDS['main']['volume'])
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(COLORS_SETTINGS['water_color'])
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
