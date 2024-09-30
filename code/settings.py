import os
from termsSettings import *

# -------------------------------------------------| CONSTANTS |-------------------------------------------------
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'code')  # directory base

# -------------------------------------------------| MAPPING TERMS |-------------------------------------------------
from termsSettings import *

# -------------------------------------------------| SCREEN SETTINGS |-------------------------------------------------

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

HITBOX_OFFSET = {
    PLAYER: -26,
    LARGE_OBJECTS: -40,
    'leaf' : -10,
    'snow' : -10,
    BOUNDARY : 0
}

# -------------------------------------------------| GAME SOUNDS |-------------------------------------------------

GENERAL_SOUND_ADJUST = 0.4
GAME_SOUNDS = {
    'main' : {'path':os.path.join(BASE_DIR, 'audio', 'forest.ogg'),'volume':0.75*GENERAL_SOUND_ADJUST},
    'weapon':{'path': os.path.join(BASE_DIR, 'audio', 'sword.wav'),'volume':0.25*GENERAL_SOUND_ADJUST},
}

# -------------------------------------------------| MAPPING IMAGES |-------------------------------------------------

# Level Images and  Map sources
LEVEL_IMAGES = { # 'level' : {level images}
    '0':{
        BACKGROUND: os.path.join(BASE_DIR, 'graphics', 'tilemap', 'ground.png'),
        BOUNDARY: os.path.join(BASE_DIR, 'map', 'map_FloorBlocks.csv'),
        LARGE_OBJECTS: os.path.join(BASE_DIR, 'map', 'map_Objects.csv'),
        ENTITY: os.path.join(BASE_DIR, 'map', 'map_Entities.csv'),
        GRAPHIC_OBJECTS: os.path.join(BASE_DIR, 'graphics', 'objects')
        },
    '1':{
        BACKGROUND: os.path.join(BASE_DIR, 'graphics', 'tilemap', 'ground.png'),
        BOUNDARY: os.path.join(BASE_DIR, 'map', 'map_FloorBlocks.csv'),
        LARGE_OBJECTS: os.path.join(BASE_DIR, 'map', 'map_Objects.csv'),
        ENTITY: os.path.join(BASE_DIR, 'map', 'map_Entities.csv'),
        GRAPHIC_OBJECTS: os.path.join(BASE_DIR, 'graphics', 'objects')
        },
    }
# -------------------------------------------------| CHARACTER SETTINGS |-------------------------------------------------

FADING_PARTICLES = {
    'leaf': {
        'folder': os.path.join(BASE_DIR, 'graphics', 'particles', 'leaf'),
        'graphic_prop': os.path.join(BASE_DIR, 'graphics', 'Grass'),
        'csv_folder': os.path.join(BASE_DIR, 'map', 'map_Grass.csv'),
        'range': [1, 7],
        'level_numbers': [0],
        'ids': [8, 9, 10]
    },
}

# -------------------------------------------------| CHARACTER SETTINGS |-------------------------------------------------

# character images

FORMS_LIST = { # {} are further implementations of differents settings for each form, if necessary
    0 : {},
    1 : {},
    2 : {},
    3 : {},
}

INITIAL_IMAGE = {'image': os.path.join(BASE_DIR, 'graphics', 'test', 'rock.png')}
CHARACTER_FOLDER = '../code/graphics/player/'

RESOURCES_TYPES = ['weapon', 'magic', 'bag', 'transformation']


CHARACTER_ANIMATIONS = ['up', 'down', 'left', 'right', 
                        'up_idle', 'down_idle', 'left_idle', 'right_idle',
                        'up_attack', 'down_attack', 'left_attack', 'right_attack']

EXCLUDED_STATS = {'respawn'}  # used for future stats that isn't on upgrade section
CHARACTER_DATA = {
    'stats':{'health':100,'energy':60,'attack':10,'magic':4,'resistance':5,'speed':5,'respawn':3},
    'max_stats':{'health':300,'energy':140,'attack':20,'magic':10,'resistance':10,'speed':10,'respawn':3},
    'upgrade_cost':{'health':100,'energy':100,'attack':100,'magic':100,'resistance':100,'speed':100,'respawn':3},
}

# -------------------------------------------------| ATTACKS SETTINGS |-------------------------------------------------

# magics

MAGIC_LIST = {
    '0':{'magic_name':'flame',
         'sub_magic_name':None,
         'magic_particle':'fire',
         'strength':50,
         'cost':25,
         'attack_amount':6,
         'graphic':'../code/graphics/particles/flame/fire.png',
         'graphic_folder':'../code/graphics/particles/flame/frames',
         'sub_graphic_folder':None,
         'sound_folder':'../code/audio/Fire.wav',
         'volume':0.3*GENERAL_SOUND_ADJUST
         },
    '1':{'magic_name':'heal',
         'sub_magic_name':'aura',
         'magic_particle':'heal',
         'strength':10,
         'cost':5,
         'attack_amount':1,
         'graphic':'../code/graphics/particles/heal/heal.png',
         'graphic_folder':'../code/graphics/particles/heal/frames',
         'sub_graphic_folder':'../code/graphics/particles/aura',
         'sound_folder':'../code/audio/heal.wav',
         'volume':0.3*GENERAL_SOUND_ADJUST
         }
}

# weapons
WEAPONS_FOLDER = '../code/graphics/weapons/'
WEAPONS_LIST = {
    # 'sword':{'cooldown':100,'damage':15,'graphic':'../code/graphics/weapons/sword/full.png','accessible':True},
    # 'lance' : {'cooldown':100,'damage':15,'graphic':'../code/graphics/weapons/lance/full.png','accessible':True},
    # 'axe' : {'cooldown':100,'damage':15,'graphic':'../code/graphics/weapons/axe/full.png','accessible':True},
    # 'rapier' : {'cooldown':100,'damage':15,'graphic':'../code/graphics/weapons/rapier/full.png','accessible':True},
    # 'sai': {'cooldown':100,'damage':15,'graphic':'../code/graphics/weapons/sai/full.png','accessible':True},
    'borduna':{'cooldown':100,'damage':10,'graphic':'../code/graphics/weapons/borduna/full.png','accessible':True},
    'coronha' : {'cooldown':100,'damage':10,'graphic':'../code/graphics/weapons/coronha/full.png','accessible':True},
    'lanca' : {'cooldown':100,'damage':10,'graphic':'../code/graphics/weapons/lanca/full.png','accessible':True},
    'tacape' : {'cooldown':100,'damage':10,'graphic':'../code/graphics/weapons/tacape/full.png','accessible':True},
}

WEAPONS_DISPLAY_ADJUST = {
    # 'sword':{'left':{'x':0,'y':0},'right':{'x':0,'y':0},'down':{'x':0,'y':0},'up':{'x':0,'y':0},},
    # 'lance' : {'left':{'x':0,'y':0},'right':{'x':0,'y':0},'down':{'x':0,'y':0},'up':{'x':0,'y':0},},
    # 'axe' : {'left':{'x':0,'y':0},'right':{'x':0,'y':0},'down':{'x':0,'y':0},'up':{'x':0,'y':0},},
    # 'rapier' : {'left':{'x':0,'y':0},'right':{'x':0,'y':0},'down':{'x':0,'y':0},'up':{'x':0,'y':0},},
    # 'sai': {'left':{'x':0,'y':0},'right':{'x':0,'y':0},'down':{'x':0,'y':0},'up':{'x':0,'y':0},},
    'borduna':{'left':{'x':10,'y':-2},'right':{'x':-10,'y':-2},'down':{'x':31,'y':-19},'up':{'x':31,'y':10},},
    'coronha' : {'left':{'x':7,'y':-10},'right':{'x':-7,'y':-10},'down':{'x':31,'y':-19},'up':{'x':31,'y':10},},
    'lanca' : {'left':{'x':7,'y':-10},'right':{'x':-7,'y':-10},'down':{'x':31,'y':-19},'up':{'x':31,'y':10},},
    'tacape' : {'left':{'x':7,'y':-10},'right':{'x':-7,'y':-10},'down':{'x':31,'y':-19},'up':{'x':31,'y':10},},
}

# -------------------------------------------------| INTERACTIONS AND ITEMS SETTINGS |-------------------------------------------------

# for further implementations of interactible objects on map to check isn't interaction type
INTERACTIONS_MAPPING = {
    0:{'id':'-1','name':'boundary'},
    #1:{'id':'?','name':'respwan_spot'}
}

# sprite_types for itens and interactions
'''

'totem' = for itens that affects special characteristics of the player (as new magics or their improovement, or even life chances for the gaming)
'food' = for itens that improove the stats upgrades (exp,health, energy and etc)
'money' = for itens that grants money
'weapon' = for itens that grants a new weapon on list
'magic' = for itens that can cast a magic on it
'scenario' = for itens that can't be stored but can be interactible by other ways

'''
ITEMS_FOLDER = '../code/graphics/items/'
OBJECTS_LIST = {
    0:{'id':'1000','name':'dying_totem','quantity':3,'sprite_type':'totem',
       'talkable': False,'grabbable': False,'consumable': True,
       'collectable': True,'equippable':False,
       'sellable': False, 'value': 'The life has not a price',
       'life_time':60,'health':100,
       'fading':4,
       'can_shift': False,
       'upgrade':'respawn','reward':1
       }
}
'''
obects list index = used for references directly the item that should appear

'id': the same id from tiled
'name': name of the image.png that should be loaded
'quantity': avaliable amount of the item for bag sistem controll
'sprite_type': used for ocasional special interactions and animations or references for the item type
    should also be used for references the images folder as: graphics->special_objects->{sprite_type}

INTERACTIONS_TYPES = 'talkable','collectable','grabbable','equippable','consumable', 'sellable' and etc
    define the kinds of interactions that that object can provide

'life_time': seconds that the item lingers on the map
    after the life_time, the object should start fading
'upgrade' : kind of upgrade that affect the character (None,health,respawn,energy,money,new magic and etc)
    this feat allow the development of differents applyications on  the character, filtered by the sprite_type
    references, that should distinguish the nature of the interaction 
'reward': amount of the upgrade, if item can be used for it.
'fading' : used for fading the item from screen, when it can't be interactible any more and desapear from the screen
    this number is the number of images that represents the fading object, cuz their saving name patterns sould be
    like the example: for 'name' = dying_totem, their 4 range means dying_totem_0,dying_totem_1,dying_totem_2 and dying_totem_3
'can_shift' : used for objects that can shift its image, or by sequence (changing the sequence of the images)
or by interaction (for itens that can manifest and animation on interactions)

'''
# -------------------------------------------------| BAG SETTINGS |-------------------------------------------------

BAG_LIST = {
    0:{'id':'1000','name':'dying_totem','quantity':3,'sprite_type':'totem',
        'graphic': '../code/graphics/items/dying_totem/dying_totem.png',
       'talkable': False,'grabbable': False,'consumable': True,
       'collectable': True,'equippable':False,
       'sellable': False, 'value': 'The life has not a price',
       'life_time':60,'health':100,
       'fading':4,
       'can_shift': False,
       'upgrade':'respawn','reward':1
       },
    1:{'id':'1000','name':'test1','quantity':3,'sprite_type':'totem',
        'graphic': '../code/graphics/items/test1/test1.png',
       'talkable': False,'grabbable': False,'consumable': True,
       'collectable': True,'equippable':False,
       'sellable': False, 'value': 'The life has not a price',
       'life_time':60,'health':100,
       'fading':4,
       'can_shift': False,
       'upgrade':'respawn','reward':1
       },
    2:{'id':'1000','name':'test2','quantity':3,'sprite_type':'totem',
        'graphic': '../code/graphics/items/test2/test2.png',
       'talkable': False,'grabbable': False,'consumable': True,
       'collectable': True,'equippable':False,
       'sellable': False, 'value': 'The life has not a price',
       'life_time':60,'health':100,
       'fading':4,
       'can_shift': False,
       'upgrade':'respawn','reward':1
       },
    3:{'id':'1000','name':'test3','quantity':3,'sprite_type':'totem',
        'graphic': '../code/graphics/items/test3/test3.png',
       'talkable': False,'grabbable': False,'consumable': True,
       'collectable': True,'equippable':False,
       'sellable': False, 'value': 'The life has not a price',
       'life_time':60,'health':100,
       'fading':4,
       'can_shift': False,
       'upgrade':'respawn','reward':1
       }
       
       }


# -------------------------------------------------| ENEMIES AND NPCS SETTINGS |-------------------------------------------------

MONSTER_SETTINGS = {'folder':'../code/graphics/monsters/',
                    'hit_sound':'../code/audio/hit.wav',
                    'hit_sound_volume':0.35*GENERAL_SOUND_ADJUST,
                    'monster_attack_sound_volume': 0.30*GENERAL_SOUND_ADJUST,
                    'death_sound':'../code/audio/death.wav',
                    'death_sound_volume':0.30*GENERAL_SOUND_ADJUST}

ENTITY_MAPPING = {
    0:{'id':'394','name':'player','entity_type':PLAYER,'dying_folder':'../code/graphics/particles/smoke_orange'},
    1:{'id':'392','name':'raccoon','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/raccoon'},
    # 2:{'id':'393','name':'squid','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/smoke_orange'},
    # 3:{'id':'391','name':'spirit','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/nova'},
    # 4:{'id':'390','name':'bamboo','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/smoke_orange'},
    2:{'id':'393','name':'pork','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/smoke_orange'},
    3:{'id':'391','name':'pork','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/smoke_orange'},
    4:{'id':'390','name':'pork','entity_type':ENEMY,'dying_folder':'../code/graphics/particles/smoke_orange'},
}

ATTACK_TYPE = ['slash','claw','thunder','leaf_attack','sparkle']

ATTACK_SOUND = {
    ATTACK_TYPE[0] :'../code/audio/attack/slash.wav',
    ATTACK_TYPE[1] :'../code/audio/attack/claw.wav',
    ATTACK_TYPE[2] :'../code/audio/attack/fireball.wav',
    ATTACK_TYPE[3] :'../code/audio/attack/slash.wav',
}

ATTACK_PARTICLES = {
    ATTACK_TYPE[0] :'../code/graphics/particles/slash',
    ATTACK_TYPE[1] :'../code/graphics/particles/claw',
    ATTACK_TYPE[2] :'../code/graphics/particles/thunder',
    ATTACK_TYPE[3] :'../code/graphics/particles/leaf_attack',
    ATTACK_TYPE[4] :'../code/graphics/particles/sparkle',
}

MONSTER_DATA = {
	ENTITY_MAPPING[1]['name']: {'health': 100,'exp':150,'damage':20,'attack_type': ATTACK_TYPE[0], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[0]], 'speed': 3, 'resistance': 3, 'attack_radius' : 80, 'notice_radius' : 360, 'energy' : 100,'respawn':0},
	ENTITY_MAPPING[2]['name']: {'health': 300,'exp':300,'damage':40,'attack_type': ATTACK_TYPE[1],  'attack_sound':ATTACK_SOUND[ATTACK_TYPE[1]],'speed': 2, 'resistance': 3, 'attack_radius' : 120, 'notice_radius' : 400, 'energy' : 100,'respawn':0},
	ENTITY_MAPPING[3]['name']: {'health': 100,'exp':160,'damage':8,'attack_type': ATTACK_TYPE[2], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[2]], 'speed': 4, 'resistance': 3, 'attack_radius' : 60, 'notice_radius' : 350, 'energy' : 100,'respawn':0},
	ENTITY_MAPPING[4]['name']: {'health': 70,'exp':170,'damage':6,'attack_type': ATTACK_TYPE[3], 'attack_sound':ATTACK_SOUND[ATTACK_TYPE[3]], 'speed': 3, 'resistance': 3, 'attack_radius' : 50, 'notice_radius' : 300, 'energy' : 100,'respawn':0}
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
    'energy_bar_width': 150,
    # fonts
    'ui_font' :'../code/graphics/font/joystix.ttf',
    'ui_font_size':18,
    'ui_bg_color' : '#222222',
    'ui_border_color' : '#111111',
    'ui_border_color_active' : 'gold',
    'upgrade_bg_color_selected' : '#EEEEEE',
    # item box positions
    'item_box_size' : 80,
    'padding' : 5,
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