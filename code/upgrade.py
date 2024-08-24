import pygame
from settings import *

class Upgrade():
    def __init__(self,player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.75
        self.width = (self.display_surface.get_size()[0] // 6) *0.9
        self.create_items()

        # selection box system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_number - 1:
                self.selection_index +=1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= self.attribute_number - 1:
                self.selection_index -=1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            if keys[pygame.K_SPACE]:
                pass

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.threads.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_items(self):
        self.item_list = []
        for item,index in enumerate(range(self.attribute_number)):
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_number
            left = (item * increment) + (increment - self.width) // 2

            # vertical position
            top = self.display_surface.get_size()[1] * 0.1

            # create the object
            item = Item(left,top,self.width,self.height,index,self.font)
            self.item_list.append(item)
        pass

    def display(self):
        self.display_surface.fill(BACK_COLOR)
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            # get attributes
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)

            item.display(self.display_surface,self.selection_index,name,value,max_value,cost)

class Item:
    def __init__(self,l,t,w,h,index,font):
    # def __init__(self,l,t,w,h,index,font)
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font

    def display_names(self,surface,name,cost,selected):
        # title
        title_surf = self.font.render(name,False,TEXT_COLOR)
        title_rect = title_surf.ger_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

        # cost

        # draw
        surface.blit(title_surf,title_rect)
        
    def display(self,surface,selection_number,name,value,max_value,cost):
        pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
        self.display_names(surface,name,cost,False)