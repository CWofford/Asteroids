import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() 
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        asters = list(asteroids)
        for asteroid in asters:
            if asteroid.isCollision(player):
                print("Game Over!")
                return
            
            for shot in shots:
                if shot.isCollision(asteroid):
                    spawned_ast = asteroid.split() 
                    if spawned_ast != None:
                        for new_ast in spawned_ast:
                            asteroids.add(new_ast)
                            updatables.add(new_ast) 
                            drawables.add(new_ast)
                   
                    asteroids.remove(asteroid) 
                    updatables.remove(asteroid)  
                    drawables.remove(asteroid)
                    updatables.update(dt)

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
