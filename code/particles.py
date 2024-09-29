import pygame
from support import import_folder
#from settings import *
from random import choice
from settings import ENTITY_MAPPING, MAGIC_LIST,ATTACK_TYPE,ATTACK_PARTICLES,FADING_PARTICLES

class AnimationPlayer:
    def __init__(self):
        
        self.frames = {}

        # magic particles
        for key in MAGIC_LIST.keys():
            self.frames[MAGIC_LIST[key]['magic_name']] = import_folder(MAGIC_LIST[key]['graphic_folder'])
            
            if MAGIC_LIST[key]['sub_magic_name'] is not None:
                self.frames[MAGIC_LIST[key]['sub_magic_name']] = import_folder(MAGIC_LIST[key]['sub_graphic_folder'])

        # attacks
        for num in range(len(ATTACK_TYPE)):
            self.frames[ATTACK_TYPE[num]] = import_folder(ATTACK_PARTICLES[ATTACK_TYPE[num]])

        # entity deaths
        for num in range(len(ENTITY_MAPPING)):
            self.frames[ENTITY_MAPPING[num]['name']] = import_folder(ENTITY_MAPPING[num]['dying_folder'])

        # fading particles
        for particle_type in FADING_PARTICLES:
            self.frames[particle_type] = []
            folder_path = FADING_PARTICLES[particle_type]['folder']
            for num in range(*FADING_PARTICLES[particle_type]['range']):
                self.frames[particle_type].append(import_folder(f'{folder_path}{num}'))
                # to mirror particles
                self.frames[particle_type].append(self.reflect_images(import_folder(f'{folder_path}{num}')))

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_fading_particles(self,pos,groups,level_number,id):
        # Apply all fading particles for the specified level numbers
        for particles in FADING_PARTICLES:
            # Check if the level is in the list of allowed level numbers
            for level_check in FADING_PARTICLES[particles]['level_numbers']:
                if level_check == level_number:
                    # Check if the id is in the list of allowed ids
                    for check_id in FADING_PARTICLES[particles]['ids']:
                        if check_id == int(id):
                            animation_frames = choice(self.frames[particles])
                            ParticleEffect(pos, animation_frames, groups)
            
    def create_particles(self,animation_type,pos,groups):
            animation_frames = self.frames[animation_type]
            ParticleEffect(pos,animation_frames,groups)
            pass

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.sprite_type = 'magic' 
        # For multiple attacks spells, change this 'magic' to correct one
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()