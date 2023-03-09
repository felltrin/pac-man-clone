import pygame, sys
from player import Player
from board import Board
from ghost import Ghost


class Game:
    def __init__(self):
        # player setup
        player_sprite = Player(3)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        # board setup
        board_sprite = Board()
        self.board = pygame.sprite.GroupSingle(board_sprite)
        # ghost setup
        self.ghosts = pygame.sprite.Group()
        self.ghost_setup()

    def ghost_setup(self):
        pass
    
    def run(self):
        self.player.update()

        self.board.draw(screen)
        self.player.draw(screen)
        # update all sprite groups
        # draw all sprite groups


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
