import pygame
import math
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
fill_shape=False
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
            
            if event.key==pygame.K_2:
                shape='line'
            if event.key==pygame.K_1:
                shape='circle'
            if event.key==pygame.K_5:
                shape='rectangle'
            if event.key==pygame.K_0:
                shape='eraser'
            if event.key==pygame.K_6:
                shape='rhomb'
            if event.key==pygame.K_4:
                shape='square'
            if event.key==pygame.K_3:
                shape='etriangle'
            if event.key==pygame.K_9:
                shape='rtriangle'
            if event.key == pygame.K_z:  # Переключение между закрашенной и незакрашенной фигурой
                fill_shape = not fill_shape
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                if shape == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

            elif event.button == 3:
                radius = max(1, radius - 1)

        # draw while mouse moves and button is held down
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
                shapes_list.append(('rectangle', mode, (start_pos[0], start_pos[1], width, height), 4 if not fill_shape else 0))
            elif shape=='circle' and start_pos:
                rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
                shapes_list.append(('circle', mode, start_pos, rad, 4 if not fill_shape else 0))
            elif shape=='eraser' and start_pos:
                rad=int(((pygame.mouse.get_pos()[0]-start_pos[0])**2 + (pygame.mouse.get_pos()[1]-start_pos[1])**2)**0.5)
                shapes_list.append(('eraser', (0, 0, 0), start_pos, rad, 0))
            elif shape == 'rhomb' and start_pos:
                
                # dx = (pygame.mouse.get_pos()[0] - start_pos[0]) // 2
                # dy = (pygame.mouse.get_pos()[1] - start_pos[1]) // 2
                rhomb_points = [(start_pos[0] + (pygame.mouse.get_pos()[0] - start_pos[0]) // 2, start_pos[1]), (pygame.mouse.get_pos()[0], start_pos[1] + (pygame.mouse.get_pos()[1] - start_pos[1]) // 2), (start_pos[0] + (pygame.mouse.get_pos()[0] - start_pos[0]) // 2, pygame.mouse.get_pos()[1]), (start_pos[0], start_pos[1] + (pygame.mouse.get_pos()[1] - start_pos[1]) // 2)]
                shapes_list.append(('rhomb', mode, rhomb_points, 4 if not fill_shape else 0))

            elif shape == 'square' and start_pos:
                size = min(abs(pygame.mouse.get_pos()[0] - start_pos[0]), abs(pygame.mouse.get_pos()[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
                shapes_list.append(('square', mode, rect, 4 if not fill_shape else 0))

            elif shape == 'etriangle' and start_pos:
                # mid_x = (start_pos[0] + pygame.mouse.get_pos()[0]) // 2
                triangle_points = [((start_pos[0] + pygame.mouse.get_pos()[0]) // 2, start_pos[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), (start_pos[0], pygame.mouse.get_pos()[1])]
                shapes_list.append(('etriangle', mode, triangle_points, 4 if not fill_shape else 0))

            elif shape == 'rtriangle' and start_pos:
                
                triangle_points1 = [(start_pos[0], start_pos[1]), (start_pos[0], pygame.mouse.get_pos()[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])]
                shapes_list.append(('rtriangle', mode, triangle_points1, 4 if not fill_shape else 0))

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
        elif i[0]=='rhomb':
            pygame.draw.polygon(screen, i[1], i[2], i[3])
        elif i[0]=='square':
            pygame.draw.rect(screen, i[1], i[2], i[3])
        elif i[0]=='etriangle':
            pygame.draw.polygon(screen, i[1], i[2], i[3])
        elif i[0]=='rtriangle':
            pygame.draw.polygon(screen, i[1], i[2], i[3])

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
        if shape=='rhomb':
            rhomb_points=[(start_pos[0] + (pygame.mouse.get_pos()[0] - start_pos[0]) // 2, start_pos[1]), (pygame.mouse.get_pos()[0], start_pos[1] + (pygame.mouse.get_pos()[1] - start_pos[1]) // 2), (start_pos[0] + (pygame.mouse.get_pos()[0] - start_pos[0]) // 2, pygame.mouse.get_pos()[1]), (start_pos[0], start_pos[1] + (pygame.mouse.get_pos()[1] - start_pos[1]) // 2)]
            pygame.draw.polygon(screen, mode, rhomb_points, 4)
        if shape=='square':
            size=min(abs(pygame.mouse.get_pos()[0]-start_pos[0]), abs(pygame.mouse.get_pos()[1]-start_pos[1]))
            rect=pygame.Rect(start_pos[0], start_pos[1], size, size)
            pygame.draw.rect(screen, mode, rect, 4)
        if shape=='etriangle':
            triangle_points=triangle_points = [((start_pos[0] + pygame.mouse.get_pos()[0]) // 2, start_pos[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), (start_pos[0], pygame.mouse.get_pos()[1])]
            pygame.draw.polygon(screen, mode, triangle_points, 4)
        if shape=='rtriangle':
            triangle_points1=[(start_pos[0], start_pos[1]), (start_pos[0], pygame.mouse.get_pos()[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])]
            pygame.draw.polygon(screen, mode, triangle_points1, 4)
    pygame.display.flip()
    clock.tick(60)

