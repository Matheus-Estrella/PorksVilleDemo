from settings import WEAPONS_LIST,MAGIC_LIST,BAG_LIST,FORMS_LIST,CHARACTER_FOLDER,ITEMS_FOLDER
from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
	terrain_map = []
	print(f'trying to open path :{path}')
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

#print(import_csv_layout(TEST_BOUNDARY)) # used to get list of elements from an csv image

#Se caso outros mapas tiverem um valor caminhável != -1, então configurar aqui as opções como "WALKING_TILES = ['-1',...]"]

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

def set_dictionary(dict_type):
    dict_images = []
    dict_list = {
        'weapon': WEAPONS_LIST,
        'magic': MAGIC_LIST,
        'bag': BAG_LIST,
        'form': FORMS_LIST,
    }

    if dict_type in dict_list:
        if dict_type == 'transformation':
            for element in dict_list[dict_type].keys():
                path = f'{CHARACTER_FOLDER}{element}/icon_form/icon.png'                
                image = pygame.image.load(path).convert_alpha()
                dict_images.append(image)
        else:
            for element in dict_list[dict_type].values():
                path = element['graphic']
                image = pygame.image.load(path).convert_alpha()
                dict_images.append(image)

    return dict_images

        # self.transformation_graphics = []
        # for form_index in FORMS_LIST.keys():
        #     path = f'{CHARACTER_FOLDER}{form_index}/icon_form/icon.png'
        #     form_image = pygame.image.load(path).convert_alpha()
        #     self.transformation_graphics.append(form_image)
