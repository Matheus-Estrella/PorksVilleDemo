# -------------------------------------------------| MAPPING TERMS |-------------------------------------------------
from termsSettings import *

# -------------------------------------------------| SCREEN SETTINGS |-------------------------------------------------

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

HITBOX_OFFSET = {
    PLAYER: -26,
    OBJECTS: -40,
    PROP : -10,
    BOUNDARY : 0
}

# -------------------------------------------------| GAME SOUNDS |-------------------------------------------------

GENERAL_SOUND_ADJUST = 0.1
GAME_SOUNDS = {
    'main' : {'path':'../audio/main.ogg','volume':0.75*GENERAL_SOUND_ADJUST},
    'weapon':{'path':'../audio/sword.wav','volume':0.8*GENERAL_SOUND_ADJUST}
}

# -------------------------------------------------| MAPPING IMAGES |-------------------------------------------------

# Level Images and  Map sources
LEVEL_IMAGES = { # 'level' : {level images}
    '0':{
        BACKGROUND:'../graphics/tilemap/ground.png',
        BOUNDARY:'../map/map_FloorBlocks.csv',
        PROP:'../map/map_Grass.csv',
        OBJECTS:'../map/map_Objects.csv',
        ENTITY:'../map/map_Entities.csv',
        # Background Components sources
        GRAPHIC_PROP:'../graphics/grass',
        GRAPHIC_OBJECTS:'../graphics/objects'
        },
    '1':{
        BACKGROUND:'../graphics/tilemap/ground.png',
        BOUNDARY:'../map/map_FloorBlocks.csv',
        PROP:'../map/map_Grass.csv',
        OBJECTS:'../map/map_Objects.csv',
        ENTITY:'../map/map_Entities.csv',
        # Background Components sources
        GRAPHIC_PROP:'../graphics/grass',
        GRAPHIC_OBJECTS:'../graphics/objects'
        },
    }

# -------------------------------------------------| CHARACTER SETTINGS |-------------------------------------------------

# character images

CHARACTER_IMAGES = { # 'character form' : {character image and folder}
    '0':{'image':'../graphics/test/player.png','folder':'../graphics/player/'},
    }

CHARACTER_ANIMATIONS = {
            'up':[],'down':[],'left':[],'right':[],
            'up_idle':[],'down_idle':[],'left_idle':[],'right_idle':[],
            'up_attack':[],'down_attack':[],'left_attack':[],'right_attack':[]
        }

CHARACTER_DATA = {
    'stats':{'health':100,'energy':60,'attack':10,'magic':4,'speed':5},
    'max_stats':{'health':300,'energy':140,'attack':20,'magic':10,'speed':10},
    'upgrade_cost':{'health':100,'energy':100,'attack':100,'magic':100,'speed':100},
}

# -------------------------------------------------| ATTACKS SETTINGS |-------------------------------------------------

# magics

MAGIC_LIST = {
    '0':{'magic_name':'flame',
         'sub_magic_name':None,
         'magic_particle':'fire',
         'strength':100,
         'cost':15,
         'graphic':'../graphics/particles/flame/fire.png',
         'graphic_folder':'../graphics/particles/flame/frames',
         'sub_graphic_folder':None,
         'sound_folder':'../audio/Fire.wav',
         'volume':0.3*GENERAL_SOUND_ADJUST
         },
    '1':{'magic_name':'heal',
         'sub_magic_name':'aura',
         'magic_particle':'heal',
         'strength':100,
         'cost':15,
         'graphic':'../graphics/particles/heal/heal.png',
         'graphic_folder':'../graphics/particles/heal/frames',
         'sub_graphic_folder':'../graphics/particles/aura',
         'sound_folder':'../audio/heal.wav',
         'volume':0.3*GENERAL_SOUND_ADJUST
         }
}

# weapons

WEAPONS_LIST = {
    'sword':{'cooldown':100,'damage':15,'graphic':'../graphics/weapons/sword/full.png'},
    'lance' : {'cooldown':100,'damage':15,'graphic':'../graphics/weapons/lance/full.png'},
    'axe' : {'cooldown':100,'damage':15,'graphic':'../graphics/weapons/axe/full.png'},
    'rapier' : {'cooldown':100,'damage':15,'graphic':'../graphics/weapons/rapier/full.png'},
    'sai': {'cooldown':100,'damage':15,'graphic':'../graphics/weapons/sai/full.png'}
}

# -------------------------------------------------| INTERACTIONS SETTINGS |-------------------------------------------------

# for further implementations of interactible objects to check ist interaction type
INTERACTIONS_MAPPING = {
    0:{'id':'-1','name':'boundary','interaction_type':INTERACTION[0]}
}

# -------------------------------------------------| ENEMIES AND NPCS SETTINGS |-------------------------------------------------

MONSTER_SETTINGS = {'folder':'../graphics/monsters/',
                    'hit_sound':'../audio/hit.wav',
                    'hit_sound_volume':0.2*GENERAL_SOUND_ADJUST,
                    'monster_attack_sound_volume': 0.25*GENERAL_SOUND_ADJUST,
                    'death_sound':'../audio/death.wav',
                    'death_sound_volume':0.25*GENERAL_SOUND_ADJUST}

ENTITY_MAPPING = {
    0:{'id':'394','name':'player','entity_type':PLAYER,'dying_folder':'../graphics/particles/smoke_orange'},
    1:{'id':'393','name':'squid','entity_type':ENEMY,'dying_folder':'../graphics/particles/smoke_orange'},
    2:{'id':'392','name':'raccoon','entity_type':ENEMY,'dying_folder':'../graphics/particles/raccoon'},
    3:{'id':'391','name':'spirit','entity_type':ENEMY,'dying_folder':'../graphics/particles/nova'},
    4:{'id':'390','name':'bamboo','entity_type':ENEMY,'dying_folder':'../graphics/particles/bamboo'}
}

ATTACK_TYPE = ['slash','claw','thunder','leaf_attack','sparkle']

ATTACK_SOUND = {
    ATTACK_TYPE[0] :'../audio/attack/slash.wav',
    ATTACK_TYPE[1] :'../audio/attack/claw.wav',
    ATTACK_TYPE[2] :'../audio/attack/fireball.wav',
    ATTACK_TYPE[3] :'../audio/attack/slash.wav',
}

ATTACK_PARTICLES = {
    ATTACK_TYPE[0] :'../graphics/particles/slash',
    ATTACK_TYPE[1] :'../graphics/particles/claw',
    ATTACK_TYPE[2] :'../graphics/particles/thunder',
    ATTACK_TYPE[3] :'../graphics/particles/leaf_attack',
    ATTACK_TYPE[4] :'../graphics/particles/sparkle',
}

MONSTER_DATA = {
	ENTITY_MAPPING[1]['name']: {'health': 100,'exp':100,'damage':20,'attack_type': ATTACK_TYPE[0], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[0]], 'speed': 3, 'resistance': 3, 'attack_radius' : 80, 'notice_radius' : 360},
	ENTITY_MAPPING[2]['name']: {'health': 300,'exp':250,'damage':40,'attack_type': ATTACK_TYPE[1],  'attack_sound':ATTACK_SOUND[ATTACK_TYPE[1]],'speed': 2, 'resistance': 3, 'attack_radius' : 120, 'notice_radius' : 400},
	ENTITY_MAPPING[3]['name']: {'health': 100,'exp':110,'damage':8,'attack_type': ATTACK_TYPE[2], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[2]], 'speed': 4, 'resistance': 3, 'attack_radius' : 60, 'notice_radius' : 350},
	ENTITY_MAPPING[4]['name']: {'health': 70,'exp':120,'damage':6,'attack_type': ATTACK_TYPE[3], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[3]], 'speed': 3, 'resistance': 3, 'attack_radius' : 50, 'notice_radius' : 300}
}

# -------------------------------------------------| UI AND COLORS SETTINGS |-------------------------------------------------

COLORS_SETTINGS = {
    'back_color' : 'black',
    'text_color' : '#EEEEEE',
    'text_color_selected' : '#111111',
    'bar_color' : '#EEEEEE',
    'bar_color_selected' : '#111111',
    'water_color' : '#71ddee',
    # stats colors
    'health_color' : 'red',
    'energy_color' : 'blue',
}

UI_SETTINGS = {
    # dimensions
    'bar_height':20,
    'health_bar_width': 200,
    'energy_bar_width': 140,
    # fonts
    'ui_font' :'../graphics/font/joystix.ttf',
    'ui_font_size':18,
    'ui_bg_color' : '#222222',
    'ui_border_color' : '#111111',
    'ui_border_color_active' : 'gold',
    'upgrade_bg_color_selected' : '#EEEEEE',
    # item box positions
    'item_box_size' : 80,
    'padding' : 3,
    'box_pos_y' : 630,
    'box_pos_x' : 10,
}





EASTER_EGG = '''                                                                                                      
      :--::::--:                    :-------:       
      -:::::::::--                -:::::::::-       
      -:::::::::::-   :::::::   ::::::::::::-       
       -::::::::---:::::::::::::---::::::::-        
        -::::--:::::::::::::::::::::--::::-         
         :---:::::::::::::::::::::::::---:          
          -:::::::::::::::::::::::::::::-           
         =:::::::::::::::::::::::::::::::-          
        -:::::::::::::::::::::::::::::::::-         
        -:::::::::::::::---:::::::::::::::=         
       :::::::::-:::----:::---::::-::::::::-        
       :::::::=@*+:--::-::::::---%#+-::::::-        
        -:::::-##*:=:-=%+:=%=::=:#%#-::::::-        
        -::::::::::=::-#=:=#-::=::::::::::-         
         -::::::::::=:::::::::=::::::::::-:         
          -:::::::::::--==---:::::::::::=           
           :-:::::::::::::::::::::::::=:            
              :::::---:::::-----:::::    '''