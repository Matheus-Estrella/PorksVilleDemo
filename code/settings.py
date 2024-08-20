
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

#Components sources
TEST_PLAYER = '../graphics/test/player.png'
TEST_ROCK = '../graphics/test/rock.png'

#Background Components sources
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


