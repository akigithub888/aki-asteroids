import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player((SCREEN_WIDTH) / 2, (SCREEN_HEIGHT) / 2)
    asteroidfield = AsteroidField()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        updateable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                running = False
        for a in asteroids:
            for s in shots:
                if a.collision(s):
                    a.split()
                    s.kill()
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000.0

    


if __name__ == "__main__":
    main()
