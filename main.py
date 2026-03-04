import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.time.Clock()
dt = 0








def main():
    print("Starting Asteroids with Pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

center_x = SCREEN_WIDTH / 2
center_y = SCREEN_HEIGHT / 2
Player = Player(center_x, center_y)




if __name__ == "__main__":
    main()


while True:
    log_state()

    for event in pygame.event.get():
        pass

    updatable.update(dt)
    screen.fill("black")
    #Player.draw(screen)
                
    pygame.display.flip()

    for obj in drawable:
        obj.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.time.Clock().tick(60)
    dt = pygame.time.Clock().tick(60) / 1000 
    

    


    print(dt)






            





