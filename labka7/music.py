import pygame
import time
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("music controler")
playlist=['first.mp3', 'second.mp3', 'third.mp3']
current=0
imgs=[pygame.transform.scale(pygame.image.load("lock.jpg"), (600, 600)), pygame.transform.scale(pygame.image.load("perfect.jpg"), (600, 600)), pygame.transform.scale(pygame.image.load("dietmountaindew.jpg"), (600, 600))]
def first_play():
    pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play(0)
def stopm():
    pygame.mixer.music.stop()
def nextm():
    global current
    current=(current+1)%3
    first_play()
def prev():
    global current
    current=(current-1)%3
    first_play()
first_play()
running=True
while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # if event.type==pygame.KEYDOWN:
        #     if event.type==pygame.K_SPACE:
        #         if pygame.mixer.music.get_busy():
        #             pygame.mixer.music.pause()
        #         elif pygame.mixer.music.get_pos()>0:
        #             pygame.mixer.music.unpause()
        #         else:
        #             first_play()
        #     elif event.type==pygame.K_s:
        #         stopm()
        #     elif event.type==pygame.K_RIGHT:
        #         nextm()
        #     elif event.type==pygame.K_LEFT:
        #         prev()
    
    key = pygame.key.get_pressed()
    screen.blit(imgs[current], (0,0))
    if key[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        elif pygame.mixer.music.get_pos()>0:
            pygame.mixer.music.unpause()
        else:
            first_play()
        time.sleep(0.5)
    elif key[pygame.K_LEFT]:
        prev()
        time.sleep(0.5)
    elif key[pygame.K_RIGHT]:
        nextm()
        time.sleep(0.5)
    elif key[pygame.K_s]:
        stopm()
        time.sleep(0.5)

    pygame.display.flip()
pygame.quit()