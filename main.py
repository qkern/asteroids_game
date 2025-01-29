import pygame
from constants import *
from player import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(PLAYER_STARTING_LOCATION_X, PLAYER_STARTING_LOCATION_Y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        player.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()