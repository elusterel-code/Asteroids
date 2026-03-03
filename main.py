import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.time.Clock()
dt = 0





def main():
    print("Starting Asteroids with Pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()


while True:
    log_state()

    for event in pygame.event.get():
        pass

    screen.fill("black")
                
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.time.Clock().tick(60)
        


    dt = pygame.time.Clock().tick(60) / 1000 

    print(dt)






            





