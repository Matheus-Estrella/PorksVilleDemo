
# 

MAIN_SOUND_FOLDER = '../audio/main.ogg'
MAIN_SOUND_VOLUME = 0.75

# -------------------------------------------------------------------------------------------------------

# Pattern Names for variables
OBJECT_2Y = 'object'
OBJECT_2Y_FOLDER = 'objects'

GRASS_REGULAR = 'grass'
GRASS_REGULAR_FOLDER = 'grass'

ENTITIES = 'entities'
BOUNDARY = 'boundary'
INVISIBLE = 'invisible'
ENEMY = 'enemy'
SPRITE_TYPE = 'sprite_type'
WEAPON = 'weapon'

GRAPHIC = 'graphic'
GRAPHIC_FOLDER = 'graphics'

# -------------------------------------------------------------------------------------------------------
# Screen Settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': [-6,-26],
    OBJECT_2Y: [0,-40],
    GRASS_REGULAR : [0,-10],
    'invisible' : [0,0]
}

# Message Boxes colors
BACK_COLOR = 'black'
TEXT_COLOR = 'white'

# -------------------------------------------------------------------------------------------------------

# Pattern IDs for objects tiles (on Tiled)
PLAYER_ID = '394'
PLAYER = 'player'

# -------------------------------------------------------------------------------------------------------


# Ground sources
GROUNDIMAGE = ['../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png',
               '../graphics/tilemap/ground.png']

# Map sources
MAPS_BOUNDARIES = ['../map/map_FloorBlocks.csv']
MAPS_GRASSES = ['../map/map_Grass.csv']
MAPS_OBJECTS = ['../map/map_Objects.csv']
MAPS_ENTITIES =['../map/map_Entities.csv']

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

# -------------------------------------------------------------------------------------------------------
# weapons
WEAPON_1 = 'sword'
WEAPON_2 = 'lance'
WEAPON_3 = 'axe'
WEAPON_4 = 'rapier'
WEAPON_5 = 'sai'

WEAPON_ATTACK_SOUND_FOLDER = '../audio/sword.wav'
WEAPON_ATTACK_SOUND_VOLUME = 0.15

WEAPON_DATA = {
    WEAPON_1 : {'cooldown':100,'damage':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/weapons/{WEAPON_1}/full.png'},
    WEAPON_2 : {'cooldown':100,'damage':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/weapons/{WEAPON_2}/full.png'},
    WEAPON_3 : {'cooldown':100,'damage':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/weapons/{WEAPON_3}/full.png'},
    WEAPON_4 : {'cooldown':100,'damage':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/weapons/{WEAPON_4}/full.png'},
    WEAPON_5 : {'cooldown':100,'damage':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/weapons/{WEAPON_5}/full.png'}
}

# -------------------------------------------------------------------------------------------------------

# magics

MAGIC_1 = 'flame'
MAGIC_1_PARTICLE = 'fire'
MAGIC_1_SOUND_FOLDER = '../audio/Fire.wav'
MAGIC_1_SOUND_VOLUME = 0.3

MAGIC_2 = 'heal'
MAGIC_2_PARTICLE = 'heal'
MAGIC_2_SOUND_FOLDER = '../audio/heal.wav'
MAGIC_2_SOUND_VOLUME = 0.3

MAGIC_DATA = {
    MAGIC_1 : {'strength':100,'cost':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/particles/{MAGIC_1}/{MAGIC_1_PARTICLE}.png'},
    MAGIC_2 : {'strength':100,'cost':15,GRAPHIC:f'../{GRAPHIC_FOLDER}/particles/{MAGIC_2}/{MAGIC_2_PARTICLE}.png'}
}

# -------------------------------------------------------------------------------------------------------

# STATS
HEALTH = 'health'
ENERGY = 'energy'
SPEED = 'speed'
MAGIC = 'magic'

STATS = {HEALTH:100,ENERGY:60,'attack':10,MAGIC:4,SPEED:5}

UPGRADE_COST = {HEALTH:100,ENERGY:100,'attack':100,MAGIC:100,SPEED:100}

MAX_STATS = {HEALTH:300,ENERGY:140,'attack':20,MAGIC:10,SPEED:10}

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

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# item box
PADDING = 3
ITEM_BOX_POS_Y = 630
ITEM_BOX_POS_X = 10
MAGIC_BOX_POS_Y = ITEM_BOX_POS_Y
MAGIC_BOX_POS_X = ITEM_BOX_POS_X + ITEM_BOX_SIZE + PADDING

# -------------------------------------------------------------------------------------------------------

# Enemies
MONSTER_FOLDER = f'../{GRAPHIC_FOLDER}/monsters/'

ATTACK_TYPE = 'attack_type' # for animations of the attack
RESISTANCE = 'resistance' # if the player hits enemy, make a pushback
ATTACK_RADIUS = 'attack_radius' # attacking area to attack player
NOTICE_RADIUS = 'notice_radius' # chasing area to attack player

DEATH_SOUND = '../audio/death.wav'
DEATH_SOUND_VOLUME = 0.2
HIT_SOUND = '../audio/hit.wav'
HIT_SOUND_VOLUME = 0.2
MONSTER_ATTACK_SOUND_VOLUME = 0.25

MONSTER_1_NAME = 'squid'
MONSTER_1_ID = '393'
MONSTER_2_NAME = 'raccoon'
MONSTER_2_ID = '392'
MONSTER_3_NAME = 'spirit'
MONSTER_3_ID = '391'
MONSTER_4_NAME = 'bamboo'
MONSTER_4_ID = '390'

MONSTER_DATA = {
	MONSTER_1_NAME: {HEALTH: 100,'exp':100,'damage':20,ATTACK_TYPE: 'slash', 'attack_sound':'../audio/attack/slash.wav', SPEED: 3, RESISTANCE: 3, ATTACK_RADIUS: 80, NOTICE_RADIUS: 360},
	MONSTER_2_NAME: {HEALTH: 300,'exp':250,'damage':40,ATTACK_TYPE: 'claw',  'attack_sound':'../audio/attack/claw.wav',SPEED: 2, RESISTANCE: 3, ATTACK_RADIUS: 120, NOTICE_RADIUS: 400},
	MONSTER_3_NAME: {HEALTH: 100,'exp':110,'damage':8,ATTACK_TYPE: 'thunder', 'attack_sound':'../audio/attack/fireball.wav', SPEED: 4, RESISTANCE: 3, ATTACK_RADIUS: 60, NOTICE_RADIUS: 350},
	MONSTER_4_NAME: {HEALTH: 70,'exp':120,'damage':6,ATTACK_TYPE: 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', SPEED: 3, RESISTANCE: 3, ATTACK_RADIUS: 50, NOTICE_RADIUS: 300}
}

monster_data = MONSTER_DATA

# -------------------------------------------------------------------------------------------------------

# Particles
# some hardcodeds datas was kept in particles code to easier the process. For implementationa, try to transport
# this data on this section
PARTICLES_FOLDER = f'../{GRAPHIC_FOLDER}/particles/'

LEAF = 'leaf'

# -------------------------------------------------------------------------------------------------------

