import pygame
import datetime
import math

pygame.init()
screen = pygame.display.set_mode((1200, 800))
width, height = 1200 // 2, 800 // 2
done = False
image = pygame.image.load('back.jpg')
sec = pygame.image.load('seconds.png')
mik_sec = sec.get_rect(center=(width, height))
minute=pygame.image.load('minutes.png')
mik_min=minute.get_rect(center=(width, height))
mik_rec = image.get_rect(center=(width, height))
font = pygame.font.SysFont('Micky', 100)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 128, 128))
    time = datetime.datetime.now()
    time_render = font.render(time.strftime("%H:%M:%S"), True, pygame.Color('black'), pygame.Color('grey'))
    screen.blit(image, mik_rec)
    screen.blit(time_render, (10, 10))
    
    # здесь рассчитала угол секундной стрелки
    angle = (time.second / 60) * 360
    
    # вращение картинки секундной стрекли 
    rotated_image = pygame.transform.rotate(sec, -angle)
    
    # отцентрировала остальную часть повернутой картиники
    rotated_rect = rotated_image.get_rect(center=mik_sec.center)
    
    # Вывела повернутую картинку на экран
    screen.blit(rotated_image, rotated_rect)
    minute_angle = ((time.minute + time.second / 60) / 60) * 360
    rotated_minute = pygame.transform.rotate(minute, -minute_angle)
    
    # Получила остальную часть повернутой кратинки минутной стрелки и отцентрировала её
    rotated_minute_rect = rotated_minute.get_rect(center=mik_min.center)
    
    # Вывела на экран картинку повернутой минутной стрелки
    screen.blit(rotated_minute, rotated_minute_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()