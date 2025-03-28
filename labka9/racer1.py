import pygame, sys
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
last_increment = 0
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

 
#Other Variables for use in the program
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 800
SPEED = 5
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

background_music = pygame.mixer.music.load('labka8/thing/background.wav')
crash_sound = pygame.mixer.Sound('labka8/thing/stukk.mp3')
#texts
font = pygame.font.Font('labka8/thing/MICKEY.TTF',60)
int_font = pygame.font.Font('labka8/thing/MICKEY.TTF',30)
win = font.render("YOU WIN!",True,BLACK)
game_over = font.render("Game Over", True, BLACK)

game_end = False


pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
#for coin
count=0
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/car.png")
        self.image=pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,SCREEN_WIDTH-100), 0)    
        self.speed=SPEED
 
      def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(100,SCREEN_WIDTH-100), 0)
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/coin.png")
        self.image=pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)
class Coin1(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/silver_coin.png")
        self.image=pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)
class Coin2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/coin2.png")
        self.image=pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)
class Coin3(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/redcoin.png")
        self.image=pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(60,SCREEN_WIDTH-60), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("labka8/thing/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 50:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH-50:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(10, 0)
 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1=Coin()
C2=Coin1()
C3=Coin2()
C4=Coin3()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)
all_sprites.add(C4)
coins=pygame.sprite.Group()
coins.add(C1)
coins2=pygame.sprite.Group()
coins2.add(C2)
coins3=pygame.sprite.Group()
coins3.add(C3)
coins4=pygame.sprite.Group()
coins4.add(C4)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

background = pygame.image.load("labka8/thing/road.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not game_end:
       
    #Cycles through all events occuring  
        
    
 
        DISPLAYSURF.blit(background, (0,0))
 
    
    #Moves and Re-draws all Sprites
    if not game_end:
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    if not game_end:
    #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollide(P1, enemies, dokill=False):
            pygame.mixer.Sound('labka8/thing/stukk.mp3').play()
            pygame.mixer.Sound('labka8/thing/lose.mp3').play()
            
            for entity in all_sprites:
                    entity.kill() 
            game_end = True
        #   time.sleep(2)
        #   pygame.quit()
        #   sys.exit()   
    #count coin 
    collect_coin= pygame.sprite.spritecollide(P1, coins, dokill=True)
    if collect_coin:
        pygame.mixer.Sound('labka8/thing/coinsound.mp3').play()
        count=count+10
        new_coin=Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)
    collect_coin2= pygame.sprite.spritecollide(P1, coins2, dokill=True)
    if collect_coin2:
        pygame.mixer.Sound('labka8/thing/coinsound.mp3').play()
        count=count+5
        new_coin1=Coin1()
        all_sprites.add(new_coin1)
        coins.add(new_coin1)
    collect_coin3= pygame.sprite.spritecollide(P1, coins3, dokill=True)
    if collect_coin3:
        pygame.mixer.Sound('labka8/thing/coinsound.mp3').play()
        count=count+1
        new_coin2=Coin2()
        all_sprites.add(new_coin2)
        coins.add(new_coin2)
    collect_coin4= pygame.sprite.spritecollide(P1, coins4, dokill=True)
    if collect_coin4:
        pygame.mixer.Sound('labka8/thing/coinsound.mp3').play()
        count=count-3
        new_coin3=Coin()
        all_sprites.add(new_coin3)
        coins.add(new_coin3)

    if not game_end:
        if count // 10 > last_increment // 10:
            last_increment = count  # Обновляем последний инкремент
            for enemy in enemies:
                enemy.speed += 2
    #winn
    if count>=100 and not game_end:
        pygame.mixer.Sound('labka8/thing/win.mp3').play()#zvuk pobedy
        game_end = True

    if game_end:
        if count >=100:
            
            DISPLAYSURF.fill(GREEN)
            pygame.draw.rect(DISPLAYSURF,BLACK,(SCREEN_WIDTH//2 -215,SCREEN_HEIGHT//2-45-40,450,150),0,20)
            pygame.draw.rect(DISPLAYSURF,WHITE,(SCREEN_WIDTH//2 -190,SCREEN_HEIGHT//2-20-40,400,100),0,10)#fon vyveski you win
            pygame.mixer.music.stop() #ostanovka zvuka mashiny
            lose_text = font.render("YOU WIN!", True, (0, 0, 0))#zagruzhaem text
            DISPLAYSURF.blit(lose_text, (SCREEN_WIDTH//2 -170, SCREEN_HEIGHT//2-40))
            
        else:
            
            #   time.sleep(1)
            DISPLAYSURF.fill(RED)
            pygame.draw.rect(DISPLAYSURF,BLACK,(SCREEN_WIDTH//2 -215,SCREEN_HEIGHT//2-45-40,450,150),0,20)
            pygame.draw.rect(DISPLAYSURF,WHITE,(SCREEN_WIDTH//2 -190,SCREEN_HEIGHT//2-20-40,400,100),0,10)#fon vyveski you win
            
            pygame.mixer.music.stop() #ostanovka zvuka mashiny
            lose_text = font.render("YOU LOSE!", True, (0, 0, 0))#zagruzhaem text
            DISPLAYSURF.blit(lose_text, (SCREEN_WIDTH//2 -170, SCREEN_HEIGHT//2-40))
            pygame.time.set_timer(INC_SPEED,0)
            

    else:
        for event in pygame.event.get():
            # if event.type == INC_SPEED:
            #     SPEED += 0.5
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            

            

            

        # time.sleep(2)
        # pygame.quit()
        # sys.exit()  
    pygame.draw.rect(DISPLAYSURF, BLACK, (SCREEN_WIDTH-160,10,120,70),0,20,20,20,20)
    pygame.draw.rect(DISPLAYSURF, WHITE, (SCREEN_WIDTH-150,20,100,50),0,10,10,10,10)
    score=int_font.render(str(count), True, BLACK)
    DISPLAYSURF.blit(score, (SCREEN_WIDTH-120, 32))
    pygame.display.update()
    FramePerSec.tick(FPS)