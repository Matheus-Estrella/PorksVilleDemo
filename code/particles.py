import pygame
from support import import_folder
from settings import *
from random import choice

class AnimationPlayer:
    def __init__(self):
        print("particlesFolder -> " + PARTICLES_FOLDER)
        self.frames = {
            # magic
            MAGIC_1: import_folder(f'{PARTICLES_FOLDER}/flame/frames'),
            'aura': import_folder(f'{PARTICLES_FOLDER}/aura'),
            MAGIC_2: import_folder(f'{PARTICLES_FOLDER}/heal/frames'),
            
            # attacks 
            'claw': import_folder(f'{PARTICLES_FOLDER}/claw'),
            'slash': import_folder(f'{PARTICLES_FOLDER}/slash'),
            'sparkle': import_folder(f'{PARTICLES_FOLDER}/sparkle'),
            'leaf_attack': import_folder(f'{PARTICLES_FOLDER}/leaf_attack'),
            'thunder': import_folder(f'{PARTICLES_FOLDER}/thunder'),

            # monster deaths
            MONSTER_1_NAME: import_folder(f'{PARTICLES_FOLDER}/smoke_orange'),
            MONSTER_2_NAME: import_folder(f'{PARTICLES_FOLDER}/raccoon'),
            MONSTER_3_NAME: import_folder(f'{PARTICLES_FOLDER}/nova'),
            MONSTER_4_NAME: import_folder(f'{PARTICLES_FOLDER}/bamboo'),
            
            # fading leafs 
            LEAF: (
                import_folder(f'{PARTICLES_FOLDER}/leaf1'),
                import_folder(f'{PARTICLES_FOLDER}/leaf2'),
                import_folder(f'{PARTICLES_FOLDER}/leaf3'),
                import_folder(f'{PARTICLES_FOLDER}/leaf4'),
                import_folder(f'{PARTICLES_FOLDER}/leaf5'),
                import_folder(f'{PARTICLES_FOLDER}/leaf6'),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf1')),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf2')),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf3')),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf4')),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf5')),
                self.reflect_images(import_folder(f'{PARTICLES_FOLDER}/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_fading_particles(self,pos,groups):
        animation_frames = choice(self.frames[LEAF])
        ParticleEffect(pos,animation_frames,groups)
        
    def create_particles(self,animation_type,pos,groups):
            animation_frames = self.frames[animation_type]
            ParticleEffect(pos,animation_frames,groups)
            pass

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.sprite_type = MAGIC 
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