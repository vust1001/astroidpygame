import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    x = int(SCREEN_WIDTH / 2)
    y = int(SCREEN_HEIGHT / 2)
    newPlayer = Player(x, y)
    #newPlayer.update(dt)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    gameClock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        tick = gameClock.tick(60)
        dt = tick / 1000
        updatable.update(dt)

        asteroids_to_kill = []
        bullets_to_kill = []
        for asteroid in asteroids:
            if newPlayer.is_collided(asteroid):
                print("Game over!")
                sys.exit() 
            for bullet in shots:
                if bullet.is_collided(asteroid):
                    asteroids_to_kill.append(asteroid)
                    bullets_to_kill.append(bullet)
        convert_To_Set_asteroids = set(asteroids_to_kill)
        convert_To_Set_bullets = set(bullets_to_kill)
        for i in convert_To_Set_asteroids:
            i.kill()
        for i in convert_To_Set_bullets:
            i.kill()

if __name__ == "__main__":
    main()
