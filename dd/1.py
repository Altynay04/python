import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill((250, 0, 0))
    pygame.display.flip()