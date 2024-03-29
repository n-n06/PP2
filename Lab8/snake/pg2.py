import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

#main screen
width,height = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
loop = True

#color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,165,0)


#text handling
font= pygame.font.Font(None, 24)
message_font = pygame.font.Font(None, 36)
def print_score(score, screen):
    text = font.render(f"Score: {score}", True, orange)
    screen.blit(text, [0,0])


#snake class
class Snake():
    def __init__(self, speed):
        self.size = 20
        self.speed = speed
        self.x = width // 2
        self.y = height // 2
        self.x_speed = 0
        self.y_speed = 0
        self.body = []
        self.length = 1
        self.live = True

    def check(self):
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            self.live = False
        self.x += self.x_speed
        self.y += self.y_speed

        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]
        

        for segment in self.body[:-1]:
            if segment == [self.x,self.y]:
                self.live = False



    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, white, [segment[0], segment[1], self.size, self.size])

    def move_left(self):
        if self.x_speed == 0:
            self.x_speed = -self.speed
        self.y_speed = 0

    def move_right(self):
        if self.x_speed == 0:
            self.x_speed = self.speed
        self.y_speed = 0

    def move_up(self):
        self.x_speed = 0
        if self.y_speed == 0:
            self.y_speed = -self.speed
    
    def move_down(self):
        self.x_speed = 0
        if self.y_speed == 0:
            self.y_speed = self.speed

    def food_collision(self, food):
        if food.x - food.size // 2 <= self.x <= food.x + food.size // 2 and food.y - food.size // 2 <= self.y <= food.y + food.size // 2:
            food.__init__()
            self.length += 1
       # if self.x == food.x and self.y == food.y:
        #    food.__init__()
         #   self.length += 1

#food class
class Food():
    def __init__(self):
        self.size = 20
        self.x = round(random.randrange(0, width - snake.size) / 20.0) * 20.0
        self.y = round(random.randrange(0, height - snake.size) / 20.0) * 20.0
    def draw(self, screen):
        pygame.draw.rect(screen, orange, [self.x, self.y, self.size, self.size])
        

#main loop
snake = Snake(10)
food = Food()
while loop:
    if not snake.live:
        screen.fill(black)
        game_over_message = message_font.render("Game Over!", True, red)
        screen.blit(game_over_message, [width//2, height//2])
        pygame.display.flip()
        time.sleep(3)
        loop = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            if event.key == pygame.K_RIGHT:
                snake.move_right()
            if event.key == pygame.K_UP:
                snake.move_up()
            if event.key == pygame.K_DOWN:
                snake.move_down()

    snake.check()
    screen.fill(black)
    food.draw(screen)
    snake.draw(screen)
    print_score(snake.length - 1, screen)

    pygame.display.flip()
    clock.tick(30)
    snake.food_collision(food)
