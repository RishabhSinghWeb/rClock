import pygame
from datetime import datetime
import math,time

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((1440, 720))
surfrect = surface.get_rect()
if surfrect.h>surfrect.w:
    q = surfrect.w // 2
    center2=q,q*3
else :
    q = surfrect.h // 2
    center2=q*3,q
center1=q,q
RADIUS = q - 50
radius_list = {'sec': RADIUS +10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
arc = RADIUS + 8
clock60 = dict(zip(range(0,60,1), range(0, 360, 6)))  # for hours, minutes and seconds
font = pygame.font.SysFont('Verdana', 60)
#img = pygame.image.load('img/2.png').convert_alpha()
#bg = pygame.image.load('img/bg4.jpg').convert()
#bg_rect = bg.get_rect()
#bg_rect.center = WIDTH, HEIGHT
#dx, dy = 1, 1

#    x = H_WIDTH  + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
#    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)

def clock_pos(center, clock_hand, key):
    x = center[0]  + radius_list[key] * math.cos(math.radians(clock_hand*6) - math.pi / 2)
    y = center[1] + radius_list[key] * math.sin(math.radians(clock_hand*6) - math.pi / 2)
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
#    dx *= -1 if bg_rect.left > 0 or bg_rect.right < WIDTH else 1
#    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < HEIGHT else 1
#    bg_rect.centerx += dx
#    bg_rect.centery += dy
#    surface.blit(bg, bg_rect)
#    surface.blit(img, (0, 0))
    surface.fill((0,0,0))
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute,    int(t.strftime("%S"))+time.time()%1 # t.second
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('#00FF00'), pygame.Color('#555555'))
    surface.blit(time_render, (q-117, q+100))
    
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), clock_pos(center1,digit, 'digit'), radius, 7)
    pygame.draw.line(surface, pygame.Color('orange'), center1, clock_pos(center1,hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), center1, clock_pos(center1,minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), center1, clock_pos(center1,second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('#FFFFFF'), center1, 8)
    sec_angle = -math.radians(second*6) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('#00FFFF'),
                    (q - arc, q - arc, 2 * arc, 2 * arc),
                    math.pi / 2, sec_angle, 8)

    h =int(datetime.now().strftime("%H")) # hours
    m = int(datetime.now().strftime("%M")) # minutes
    s = int(datetime.now().strftime("%S"))+time.time()%1 # seconds upto nano seconds
    rh = h+22 if h<2 else h-2 # r hours
    rnow = rh*4.1666666667+m*0.06944444+s*0.001157 # 100/24/60/60
    rr=str(rnow*10**10)[:6]
    rrm=(rnow%1)*60
    rrs=(rnow%0.01)*6000

    time_render = font.render(f'{rr[:2]}:{rr[2:4]}:{rr[4:6]}', True, pygame.Color('#00FF00'), pygame.Color('#555555'))
    surface.blit(time_render, (center2[0]-117, center2[1]+100))
    for digit in range(100):
        radius = 20 if not digit % 100 and not digit % 5 else 8 if not digit % 10 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), clock_pos(center2, digit*0.6, 'digit'), radius, 7)
    pygame.draw.line(surface, pygame.Color('#FF0000'), center2, clock_pos(center2,rnow*0.6, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), center2, clock_pos(center2,rrm, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), center2, clock_pos(center2,rrs, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('#FFFFFF'), center2, 8)
    sec_angle = -math.radians(rrs*6) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('#00FFFF'),
                    (center2[0] - arc, center2[1]- arc, 2 * arc, 2 * arc),
                    math.pi / 2, sec_angle, 8)

    pygame.display.flip()
    clock.tick(60)
