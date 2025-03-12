import pygame
pygame.init()
HEGHT=600
WIDTH=600
screen=pygame.display.set_mode((HEGHT, WIDTH))
pygame.display.set_caption("ball")
clock=pygame.time.Clock()
radius=25
coor_x=WIDTH//2
coor_y=HEGHT//2
speedb=20
FPS=60
running =True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (coor_x, coor_y), radius)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    key=pygame.key.get_pressed()
    if key[pygame.K_UP] and coor_y - radius - speedb >= 0:
        coor_y-=speedb
    if key[pygame.K_DOWN] and coor_y + radius + speedb <= HEGHT:
        coor_y+=speedb
    if key[pygame.K_RIGHT] and coor_x+radius+speedb<=WIDTH:
        coor_x+=speedb
    if key[pygame.K_LEFT] and coor_x -radius-speedb>=0:
        coor_x-=speedb
    clock.tick(FPS)
pygame.quit()