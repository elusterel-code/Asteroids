import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys











def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    



    print("Starting Asteroids with Pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    


    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    player = Player(center_x, center_y)
    asteroid_field = AsteroidField()




   
    dt = 0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                pygame.quit()
                sys.exit()


        screen.fill("black")
    
                
    

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        
        
        dt = clock.tick(60) / 1000 
        #print(dt)
    

    

if __name__ == "__main__":
        main()

    






            





