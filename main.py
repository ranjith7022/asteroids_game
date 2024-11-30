import pygame
from constants import *
from player import *
def main():
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    updateable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updateable,drawable)


    while running:
        
        
        screen.fill("black")
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # player.update(dt)
        for obj in updateable:
            obj.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()
