import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(PLAYER_STARTING_LOCATION_X, PLAYER_STARTING_LOCATION_Y, shots)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        new_asteroids = []
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collision_check(shot):
                    split_asteroids = asteroid.split()
                    new_asteroids.extend(split_asteroids)
                    shot.kill()
        for new_asteroid in new_asteroids:
            asteroids.add(new_asteroid)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()