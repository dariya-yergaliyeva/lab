import pygame 
import datetime
import math
pygame.init()
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey")
clock = pygame.time.Clock()

dial_c=pygame.image.load("dial.jpg")
dial_c=pygame.transform.scale(dial_c, (600, 600))

mic=pygame.image.load("images.png")
mic=pygame.transform.scale(mic, (300, 300))

minut=pygame.image.load("min_hand.png") #hour
minut=pygame.transform.scale(minut, (350, 400))

hours=pygame.image.load("sec_hand.png") #min
hours=pygame.transform.scale(hours, (400, 400))

center=(300, 300)


shoulder_left = (center[0] +10, center[1] +0)  # Левое плечо
shoulder_right = (center[0] +10, center[1] +0)  # Правое плечо
def rot_center(image, angle, position):
    rotated_image = pygame.transform.rotate(image, -angle)
    original_rect = image.get_rect(center=position)
    rotated_rect = rotated_image.get_rect(center=original_rect.center)
    return rotated_image, rotated_rect

def movingg(image, angle, position):
    rotated_image, rotated_rect = rot_center(image, angle, position)
    screen.blit(rotated_image, rotated_rect.topleft)

running=True
while running:
    screen.fill((255, 255, 255))
    screen.blit(dial_c, (0, 0))

    mickey=mic.get_rect(center=center)
    screen.blit(mic, mickey.topleft)
    

    now=datetime.datetime.now()
    minutes=now.minute
    hourss=now.second
    min_angle=(minutes%60)*6
    h_angle=(hourss%60)*6

    movingg(minut, min_angle, shoulder_left)  # Левое плечо (часовая)
    movingg(hours, h_angle, shoulder_right) 
    

    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()
         

