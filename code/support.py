from settings import *
from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
	print(f'[import_csv] trying to open path :{path}')

	terrain_map = []

	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')

		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

#print(import_csv_layout(TEST_BOUNDARY)) # used to get list of elements from an csv image

#Se caso outros mapas tiverem um valor caminhável != -1, então configurar aqui as opções como "WALKING_TILES = ['-1',...]"]

def import_folder(path: pathlib.Path):
	print(f'[import_folder] trying to open path :{path}')

	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path.joinpath(image)

			image_surf = pygame.image.load(full_path).convert_alpha()

			surface_list.append(image_surf)

	return surface_list

