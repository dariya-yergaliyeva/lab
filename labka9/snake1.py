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

font = pygame.font.Font('labka8/thing/MICKEY.TTF',30)
int_font = pygame.font.Font('labka8/thing/MICKEY.TTF',30)

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
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # snake's body
        self.dx = 1  # direction of movement
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):  # each segment moves to the place of the previous one
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx  # direction 
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL), 0, 5)  # head color
        for segment in self.body[1:]:
            pygame.draw.rect(screen, ORANGE, (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 5)  # body color

    def check_collision(self, food):
        global score, level, speed
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:  # check if snake eats the food
            score += food.points 
            score = max(score, 0) # Add food points to score
            if food.color==RED:
                if score // 10 < level: # Ensure score doesn't go below 0 # Decrease level based on score
                    level -= 1
                    print(level)
                    screen.fill(RED)
                    pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                    pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)
                    level_down = font.render("LEVEL DOWN!", True, (0, 0, 0))
                    screen.blit(level_down, (Width // 2 - 110, Height // 2 - 30))
                    pygame.display.flip()
                    pygame.time.delay(500) 
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  # increase snake by 1 segment
            food.update_food(self)  # Update food with new random properties

            if score // 10 > level:
                level += 1
                speed += 2
                # Green screen flash for 0.5 seconds
                screen.fill(GREEN)
                pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)  # next level background
                next_level_text = font.render("NEXT LEVEL!", True, (0, 0, 0))
                screen.blit(next_level_text, (Width // 2 - 110, Height // 2 - 30))
                pygame.display.flip()
                pygame.time.delay(500)  # Pause before continuing the game

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= Width // CELL or head.y < 0 or head.y >= Height // CELL

    def check_self_collision(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

                
                
    def check_wall_collision(self):
        head=self.body[0]
        return head.x<0 or head.x>=Width//CELL or head.y<0 or head.y>=Height//CELL
    def check_self_collision(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

class Food:
    def __init__(self):
        self.pos = Point(0, 0)
        
        self.points, self.color = self.random_food_properties()  # Присваиваем случайные баллы и цвет еды
        self.spawn_time = None  # Обновляем время появления еды
        self.spawn(None)  # Генерируем первую еду
    def random_food_properties(self):
        # Генерация случайного цвета и баллов при каждом спавне еды
        food_type = random.choice(["green", "red", "yellow"])
        if food_type == "green":
            return 5, GREEN  # 5 points for green food
        elif food_type == "red":
            return -2, RED  # -2 points for red food
        elif food_type == "yellow":
            return 5, YELLOW  # 1 point for yellow food

    def spawn(self, snake):
        while True:
            new_x = random.randint(0, Width // CELL - 3)
            new_y = random.randint(0, Height // CELL - 3)
            
            if snake and any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                
                continue
            self.pos = Point(new_x, new_y)
            self.spawn_time = pygame.time.get_ticks()
            break

    def draw(self):
        # Отрисовка еды с текущим цветом
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 0, 20)
    
    def update_food(self, snake):
        # Эта функция будет вызываться каждый раз, когда змейка съедает еду
        self.points, self.color = self.random_food_properties()  # Генерируем новый цвет и баллы для еды
        self.spawn(snake)  # Перегенерируем позицию еды
    
        
    # def chwck_expressionself(self):
    #     if pygame.time.get_ticks() - self.spawn_time >5000:
    #         print("serdar")
    #         return True
    #     return False




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
            if event.key == pygame.K_ESCAPE:
                running=False
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
    # food.chwck_expressionself()
    if pygame.time.get_ticks() - food.spawn_time > 5000:
        food.update_food(snake)

    # Отрисовка
    snake.draw()
    food.draw()
    draw_text()

    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
sys.exit()