import pygame
from constants import *
from player import *
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit
def main():
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shotable = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shotable, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    Player.containers = (updateable,drawable)
    
    
    
    
    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    Shot.containers = (shotable, updateable, drawable)
    


    while running:
        
        
        
        # player.draw(screen)
        
        
        # player.update(dt)
        for obj in updateable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if CircleShape.check_collisions(player,obj):
                print("Game over!")
                exit()
            for shot in shotable:
                if obj.check_collisions(shot):
                    shot.kill()
                    obj.split()
        

        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()
