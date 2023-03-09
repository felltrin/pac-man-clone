import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/pac-man clone/board-layout-trans.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (600,600))
        self.rect = self.image.get_rect(topleft=(0,0))

