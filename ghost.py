import pygame 

class Ghost(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        file_name = "graphics/pacman clone 2/" + name + ".png"
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))