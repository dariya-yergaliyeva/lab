import pygame
import random
import time
import sys
pygame.init()
Width=600
Height=600
screen=pygame.display.set_mode((Width, Height))

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE=(255, 128, 0)
CELL=15
DARGDRAY=(10, 10, 10)
score=0
level=1
speed=5

font = pygame.font.Font('thing/MICKEY.TTF',30)
int_font = pygame.font.Font('thing/MICKEY.TTF',30)

#draw grid
def grid():
    for i in range(Height//2):
        for j in range(Width//2):
            pygame.draw.rect(screen, DARGDRAY, (i * CELL, j * CELL, CELL, CELL), 1)
#draw chess grid
def chess_grid():
    colors=[DARGDRAY, BLACK]
    for i in range(Height//2):
        for j in range(Width//2):
            pygame.draw.rect(screen, colors[(i+j)%2], (i*CELL, j*CELL, CELL, CELL))
def draw_text():
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
#представляет точку на игровом поле с координатами (x, y)
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # def __str__(self):
    #     return f"{self.x}, {self.y}"
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)] #snake's body
        self.dx = 1 #аправление движения
        self.dy = 0
    def move(self):
        for i in range(len(self.body)-1, 0, -1): #каждый сегмент змейки становится на место предыдущего
            self.body[i].x=self.body[i-1].x
            self.body[i].y=self.body[i-1].y
        self.body[0].x += self.dx #направление 
        self.body[0].y += self.dy
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL), 0, 5) #head color
        for segment in self.body[1:]:
            pygame.draw.rect(screen, ORANGE, (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 5) #body color
    def check_collision(self, food):
        global score, level, speed
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y: #проверяет, съела ли змейка еду.
            score += 1
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            food.spawn(self)  #если координаты головы совпадают с координатами еды, змейка увеличивается на 1 сегмент.
            if score % 3 == 0 and score!=0:
                level += 1
                speed += 5
                # Вспышка зеленого экрана на 0.5 секунды
                screen.fill(GREEN)
                pygame.draw.rect(screen,BLACK,(Width//2 -215,Height//2-45-40,450,150),0,20)
                pygame.draw.rect(screen,WHITE,(Width//2 -190,Height//2-20-40,400,100),0,10)#fon vyveski you win
        
                next_level_text = font.render("NEXT LEVEL!", True, (0, 0, 0))#zagruzhaem text
                screen.blit(next_level_text, (Width//2 -110, Height//2-30))
                pygame.display.flip()
                pygame.time.delay(500)  # Пауза перед продолжением игры


                
                
    def check_wall_collision(self):
        head=self.body[0]
        return head.x<0 or head.x>=Width//CELL or head.y<0 or head.y>=Height//CELL
    def check_self_collision(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

class Food:
    def __init__(self):
        self.pos = Point(0, 0)
        self.spawn(None)  # Генерируем первую еду

    def spawn(self, snake):
        while True:
            new_x = random.randint(0, Width//CELL - 3)
            new_y = random.randint(0, Height//CELL - 3)
            new_pos = Point(new_x, new_y)

            # Проверяем, чтобы еда не попала на тело змейки
            if snake and any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                continue
            self.pos = new_pos
            break

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x *CELL, self.pos.y * CELL , CELL, CELL), 0, 20) #food drawing


clock = pygame.time.Clock()
food = Food()
snake = Snake()
nup=False
ndown=False
nright=True
nleft=False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not nleft:
                nright=True
                snake.dx = 1
                nup=False
                ndown=False
                nleft=False
                snake.dy = 0
            elif event.key == pygame.K_LEFT and not nright:
                nleft=True
                nup=False
                ndown=False
                nright=False
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and not nup:
                nleft=False
                nup=False
                ndown=True
                nright=False
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and not ndown:
                nleft=False
                nup=True
                ndown=False
                nright=False
                snake.dx = 0
                snake.dy = -1
    chess_grid()
    snake.move()
    if snake.check_wall_collision() or snake.check_self_collision():
        screen.fill(RED)
        pygame.draw.rect(screen,BLACK,(Width//2 -215,Height//2-45-40,450,150),0,20)
        pygame.draw.rect(screen,WHITE,(Width//2 -190,Height//2-20-40,400,100),0,10)#fon vyveski you lose
        
        lose_text = font.render("YOU LOSE!", True, (0, 0, 0))#zagruzhaem text
        screen.blit(lose_text, (Width//2 -110, Height//2-30))
        pygame.display.update()
          
        time.sleep(3)
        pygame.quit() 
        sys.exit()
    snake.check_collision(food)

    # Отрисовка
    snake.draw()
    food.draw()
    draw_text()

    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
sys.exit()