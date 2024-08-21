
# Screen Settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# Message Boxes colors
BACK_COLOR = 'black'
TEXT_COLOR = 'white'

# Pattern Names for variables

OBJECT_2Y = 'object'
OBJECT_2Y_FOLDER = 'objects'

GRASS_REGULAR = 'grass'
GRASS_REGULAR_FOLDER = 'grass'

# Gorund sources
GROUNDIMAGE = ['../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png']

# Map sources
MAPS_BOUNDARIES = ['../map/map_FloorBlocks.csv']
MAPS_GRASSES = ['../map/map_Grass.csv']
MAPS_OBJECTS = ['../map/map_Objects.csv']

# Character assets
CHARACTER_FOLDER = '../graphics/player/'
CHARACTER_ANIMATIONS = {
            'up':[],'down':[],'left':[],'right':[],
            'up_idle':[],'down_idle':[],'left_idle':[],'right_idle':[],
            'up_attack':[],'down_attack':[],'left_attack':[],'right_attack':[]
        }

# Components sources
TEST_PLAYER = '../graphics/test/player.png'
TEST_ROCK = '../graphics/test/rock.png'

# Background Components sources
GRAPHIC_GRASS = ['../graphics/grass']
GRAPHIC_OBJECTS = ['../graphics/objects']


# weapons
WEAPON_1 = 'sword'
WEAPON_2 = 'lance'
WEAPON_3 = 'axe'
WEAPON_4 = 'rapier'
WEAPON_5 = 'sai'

WEAPON_DATA = {
    WEAPON_1 : {'cooldown':100,'damage':15,'graphic':f'../graphics/weapons/{WEAPON_1}/full.png'},
    WEAPON_2 : {'cooldown':100,'damage':15,'graphic':f'../graphics/weapons/{WEAPON_2}/full.png'},
    WEAPON_3 : {'cooldown':100,'damage':15,'graphic':f'../graphics/weapons/{WEAPON_3}/full.png'},
    WEAPON_4 : {'cooldown':100,'damage':15,'graphic':f'../graphics/weapons/{WEAPON_4}/full.png'},
    WEAPON_5 : {'cooldown':100,'damage':15,'graphic':f'../graphics/weapons/{WEAPON_5}/full.png'}
}

# STATS
HEALTH = 'health'
ENERGY = 'energy'
SPEED = 'speed'

STATS = {HEALTH:100,ENERGY:60,'attack':10,'magic':4,SPEED:5}

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80

UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

