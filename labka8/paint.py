import pygame
pygame.init()
screen=pygame.display.set_mode((600, 600))
clock=pygame.time.Clock()
mode=(255, 255, 255)
points=[]
shape=None
start_pos=None
radius=15
shapes_list=[]
running =True
while running:
    keys=pygame.key.get_pressed()
    alt_held = keys[pygame.K_LALT] or keys[pygame.K_RALT]
    ctrl_held = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                pygame.quit()
                exit()
            if event.key == pygame.K_F4 and alt_held:
                pygame.quit()
                exit()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key==pygame.K_r:
                mode=(255, 0, 0)
            if event.key==pygame.K_b:
                mode=(0, 0, 255)
            if event.key==pygame.K_g:
                mode=(0, 255, 0)
            if event.key==pygame.K_y:
                mode=(255, 255, 0)
            if event.key==pygame.K_o:
                mode=(255, 165, 0)
            if event.key==pygame.K_p:
                mode=(128, 0, 128)
            
            if event.key==pygame.K_l:
                shape='line'
            if event.key==pygame.K_c:
                shape='circle'
            if event.key==pygame.K_s:
                shape='rectangle'
            if event.key==pygame.K_e:
                shape='eraser'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                if shape == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

            elif event.button == 3:
                radius = max(1, radius - 1)

        # Eraser - draw while mouse moves and button is held down
        if event.type == pygame.MOUSEMOTION:
            if shape == 'eraser' and pygame.mouse.get_pressed()[0]:  # Left mouse button held
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        if event.type==pygame.MOUSEBUTTONDOWN:
            position=event.pos
            points.append(position)
            points = points[-256:]

            if shape=='eraser':
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)    

        if event.type==pygame.MOUSEBUTTONUP:
            end_pos=event.pos
            if shape=='line':
                shapes_list.append(('line', mode, start_pos, end_pos))
            elif shape=='rectangle' and start_pos:
                width=pygame.mouse.get_pos()[0]-start_pos[0]
                height=pygame.mouse.get_pos()[1]-start_pos[1]
                shapes_list.append(('rectangle', mode, (start_pos[0], start_pos[1], width, height), 4))
            elif shape=='circle' and start_pos:
                rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
                shapes_list.append(('circle', mode, start_pos, rad, 4))
            elif shape=='eraser' and start_pos:
                rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
                shapes_list.append(('eraser', (0, 0, 0), start_pos, rad, 0))
            start_pos=None

    screen.fill((0, 0, 0))
    for i in shapes_list:
        if i[0]=='rectangle':
            pygame.draw.rect(screen, i[1], i[2], 4)
        elif i[0]=='circle':
            pygame.draw.circle(screen, i[1], i[2], i[3], 4)
        elif i[0]=='line':
            pygame.draw.line(screen, i[1], i[2], i[3], 4)
        elif i[0]=='eraser':
            pygame.draw.circle(screen, i[1], i[2], i[3], 0)
    if start_pos:
        if shape=='rectangle':
            width=pygame.mouse.get_pos()[0]-start_pos[0]
            height=pygame.mouse.get_pos()[1]-start_pos[1]
            pygame.draw.rect(screen, mode, (start_pos[0], start_pos[1], width, height), 4)
        if shape=='line':
            pygame.draw.line(screen, mode, start_pos, pygame.mouse.get_pos(), 4)
        if shape=='circle':
            rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, mode, start_pos, rad, 4)
        if shape=='eraser':
            rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, (0, 0, 0), start_pos, rad, 0)

    pygame.display.flip()
    clock.tick(60)

