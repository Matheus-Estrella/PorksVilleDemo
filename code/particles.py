import pygame
from support import import_folder
#from settings import *
from random import choice
from settings import ENTITY_MAPPING, MAGIC_LIST,ATTACK_TYPE,ATTACK_PARTICLES

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            MAGIC_LIST[str(0)]['magic_name']: import_folder(MAGIC_LIST[str(0)]['graphic_folder']),
            MAGIC_LIST[str(1)]['magic_name']: import_folder(MAGIC_LIST[str(1)]['graphic_folder']),
            MAGIC_LIST[str(1)]['sub_magic_name']: import_folder(MAGIC_LIST[str(1)]['sub_graphic_folder']),
            
            # attacks 
            ATTACK_TYPE[0]: import_folder(ATTACK_PARTICLES[ATTACK_TYPE[0]]),
            ATTACK_TYPE[1]: import_folder(ATTACK_PARTICLES[ATTACK_TYPE[1]]),
            ATTACK_TYPE[2]: import_folder(ATTACK_PARTICLES[ATTACK_TYPE[2]]),
            ATTACK_TYPE[3]: import_folder(ATTACK_PARTICLES[ATTACK_TYPE[3]]),
            ATTACK_TYPE[4]: import_folder(ATTACK_PARTICLES[ATTACK_TYPE[4]]),

            # monster deaths
            ENTITY_MAPPING[1]['name']: import_folder(ENTITY_MAPPING[1]['dying_folder']),
            ENTITY_MAPPING[2]['name']: import_folder(ENTITY_MAPPING[2]['dying_folder']),
            ENTITY_MAPPING[3]['name']: import_folder(ENTITY_MAPPING[3]['dying_folder']),
            ENTITY_MAPPING[4]['name']: import_folder(ENTITY_MAPPING[4]['dying_folder']),
            
            # fading leafs 
            'leaf': (
                import_folder('../graphics/particles/leaf1'),
                import_folder('../graphics/particles/leaf2'),
                import_folder('../graphics/particles/leaf3'),
                import_folder('../graphics/particles/leaf4'),
                import_folder('../graphics/particles/leaf5'),
                import_folder('../graphics/particles/leaf6'),
                self.reflect_images(import_folder('../graphics/particles/leaf1')),
                self.reflect_images(import_folder('../graphics/particles/leaf2')),
                self.reflect_images(import_folder('../graphics/particles/leaf3')),
                self.reflect_images(import_folder('../graphics/particles/leaf4')),
                self.reflect_images(import_folder('../graphics/particles/leaf5')),
                self.reflect_images(import_folder('../graphics/particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_fading_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)
        
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