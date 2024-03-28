import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
done = False
x = 50
y = 50
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()  
    if pressed[pygame.K_UP]:
        if y>30:
            y-= 20
    if pressed[pygame.K_DOWN]: 
        if y<370:
            y += 20
    if pressed[pygame.K_LEFT]: 
        if x>30:
                x -= 20
    if pressed[pygame.K_RIGHT]: 
        if x<470:
            x += 20

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    
    clock.tick(60)

    pygame.display.flip()