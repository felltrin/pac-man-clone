import pygame 


class Player(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load('graphics/pac-man-player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect(midbottom = (300, 470))
        self.speed = 0
        self.x_speed = speed

    def get_input(self):
        self.rect.x += self.x_speed
        self.rect.y += self.speed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x_speed = 3
            self.speed = 0
            self.load_image(1)
        elif keys[pygame.K_LEFT]:
            self.x_speed = -3
            self.speed = 0
            self.load_image(2)
        elif keys[pygame.K_UP]:
            self.x_speed = 0
            self.speed = -3
            self.load_image(3)
        elif keys[pygame.K_DOWN]:
            self.x_speed = 0
            self.speed = 3
            self.load_image(4)
            
    def load_image(self, num):
        default_dictionary = {
            1 : pygame.image.load('graphics/pac-man-player.png').convert_alpha(),
            2 : pygame.image.load('graphics/pac-man-player-left.png').convert_alpha(),
            3 : pygame.image.load('graphics/pac-man-player-up.png').convert_alpha(),
            4 : pygame.image.load('graphics/pac-man-player-down.png').convert_alpha()
        }
        self.image = default_dictionary[num]
        self.image = pygame.transform.scale(self.image, (32,32))

    # fix bug next time
    def board_loop(self):
        if(self.rect.right <= 0 and self.x_speed == -3):
            self.rect.left = 650
        if(self.rect.right >= 650 and self.x_speed == 3):
            self.rect.left = -50

    def update(self):
        self.get_input()
        self.board_loop()
        