import pygame 
import random
import json
import os
from menu import * # <- this module was made by me and contains most of the Lab9's functionality

#changing the working dir to resources where all of the stuff like imgs, audio and json files are stored
pygame.init()
os.chdir("resources")

'''
Main window parameters
'''
W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()

#vars related to change over time
global timer1, timer2
timer1 = 0
timer2 = 0
change_period = 3

done = False
bg = (0,0,0)


'''
Paddle parameters
'''
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle_color = (255,255,255)
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


'''
Ball parameters
'''
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(W // 2, H // 2, ball_rect, ball_rect)
dx, dy = 1, -1


'''
Text and Font handling
'''
main_font = pygame.font.Font(None, 40)

#game score
game_score = 0
game_score_font = game_score_text = main_font.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Game over Screen
losetext = main_font.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
wintext = main_font.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Record Text
record = main_font.render("You have set a new record!", True, (255,255,255)) 
recordRect = record.get_rect(center = (600,500))


'''
Audio handling
'''
#Creating separate audio channels for sound effects and background music
bgm_channel = pygame.mixer.Channel(0)
bgm_channel.set_volume(0.5)
bgm_channel.play(pygame.mixer.Sound("bgm.wav"), -1)

sfx_channel = pygame.mixer.Channel(1)
sfx_channel.set_volume(0.5)

collision_sound = pygame.mixer.Sound('catch.mp3')
special_collision_sound = pygame.mixer.Sound('special catch.wav')
boom_collision_sound = pygame.mixer.Sound('boom.ogg')


'''
Functions for collision and change over time
'''
#detection of collision
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

#functions that change ball's speed and paddle' size over time
def change_ball_speed(change_period):
    global ballSpeed, timer1
    if timer1 >= change_period:
        timer1 = 0
        ballSpeed += 3

def change_paddle_size(change_period):
    global paddle, timer2
    if timer2 >= change_period:
        timer2 = 0
        #keeping the aspect ration of the paddle
        aspect_ratio = paddle.width / paddle.height
        width = paddle.width - 15
        height = width / aspect_ratio
        paddle = pygame.Rect(paddle.left, paddle.top, width, height)


'''
Block creation
'''
#block setting
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#selecting special blocks from block_list and color_list
num_special = num_unbreakable = random.randint(4,7)
special_list = [(color_list[i], block_list[i]) for i in (random.randrange(0,40) for j in range(num_special))]
special_color_list = [pair[0] for pair in special_list]
special_block_list = [pair[1] for pair in special_list]

#selecting the same number of unbreakable blocks as the number of special blocks
#not exactly the same - the number can be less if the selected rect has already been assigned to the special group)
unbreakable_list = [(color_list[i], block_list[i]) for i in (random.randrange(0,40) for j in range(num_unbreakable)) if block_list[i] not in special_block_list]
unbreakable_color_list = [pair[0] for pair in unbreakable_list]
unbreakable_block_list = [pair[1] for pair in unbreakable_list]


#ver for help. when the game enter a loop, the player can place the ball in the middle 
#but with the price of +2 speed for the ball
help_used = False


'''
Working with files
'''
#stats json
with open("stats.json", "r") as stats_r:
    stats_dict = json.load(stats_r)


'''
Stats 
'''
blocks_destroyed = 0
special_blocks_destroyed = 0
win = lose = 0

'''
Main Menu
'''
#game_menu is a function from my module that does all of the usual menu stuff and returns a color
#this color is the color of the player and is selected in the settings. If the color was not selected, return white
paddle_color = game_menu(stats_dict, bgm_channel, sfx_channel, menu_type="main")
if not paddle_color:
    done = True
timer1 = timer2 = 0
started = False


'''
Game loop
'''
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #checking if a player has pressed pause - ESC button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paddle_color = game_menu(stats_dict, bgm_channel, sfx_channel, menu_type="pause")
            if not paddle_color:
                done = True
            started = False

    screen.fill(bg)
    
    #drawing regular blocks
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)
     if (color_list[color], block) not in special_list and (color_list[color], block) not in unbreakable_list]
    
    #drawing special blocks
    for special_color, special_block in special_list:
        pygame.draw.rect(screen, special_color, special_block)
        pygame.draw.circle(screen,
                           (255-special_color[0], 255-special_color[1], 255 - special_color[2]),
                           special_block.center, 
                           radius=10
                            )

    #drawing unbreakable blocks
    for unbreakable_color, unbreakable_block in unbreakable_list:
        pygame.draw.rect(screen, unbreakable_color, unbreakable_block)
        pygame.draw.line(screen,
                         (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                         unbreakable_block.topleft,
                         unbreakable_block.bottomright,
                         width=3)
        
    #drawing paddle and ball
    pygame.draw.rect(screen, paddle_color, paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    

    #Ball movement
    if started:
        #2 timer for the ball's speed and paddle's size
        #ball's speed is increased over time, while the paddle's width and height is decreased
        timer1 += clock.get_rawtime() / 1000
        timer2 += clock.get_rawtime() / 1000
    
        change_ball_speed(change_period)
        change_paddle_size(change_period)

        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy
         

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    

    #Collision blocks
    hitIndex = ball.collidelist(block_list)


    if hitIndex != -1:
        if block_list[hitIndex] not in unbreakable_block_list:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
        else:
            hitRect = block_list[hitIndex]
            hitColor = color_list[hitIndex]

        #if the rect is special, we get 2 points for it, increase player's speed and play a different sound
        if hitRect in special_block_list:
            special_blocks_destroyed += 1
            blocks_destroyed += 1
            stats_dict["Total blocks destroyed: "] = blocks_destroyed

            special_block_list.remove(hitRect)
            special_color_list.remove(hitColor)
            special_list.remove((hitColor, hitRect))

            game_score += 2
            paddleSpeed += 1
            sfx_channel.play(special_collision_sound)

        #if the hit rect is unbreakable we do not delete it from anywhere and play another sound - vine boom ;)
        elif hitRect in unbreakable_block_list:
            sfx_channel.play(boom_collision_sound)
        else:
            blocks_destroyed += 1
            game_score += 1
            sfx_channel.play(collision_sound)

       
        stats_dict["Total blocks destroyed: "] = blocks_destroyed


        dx, dy = detect_collision(dx, dy, ball, hitRect)
      

    #Game score
    game_score_text = main_font.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    

    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        #checking if a player has set a record
        lose = 1
        win = 0
        if game_score > stats_dict["Max score: "]:
            screen.blit(record, recordRect)

    elif all(block in unbreakable_block_list for block in block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
        #checking if a player has set a record
        lose = 0
        win = 1
        if game_score > stats_dict["Max score: "]:
            screen.blit(record, recordRect)
    

    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
        started = True
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
        started = True

    #this setting is my solution for the problem where the ball is stuck in some closed loop and continues to move only inside of it. 
    #Basically, by pressing CTRL-H, the user can get one time help - place the ball in the center again but with the price of +2 speed
    if (key[pygame.K_LCTRL] or key[pygame.K_RCTRL]) and key[pygame.K_h] and not help_used:
        ball.x = W // 2
        ball.y = H // 2
        ballSpeed += 2
        help_used = True
     

    #refreshing the screen
    pygame.display.flip()
    clock.tick(FPS)


'''
Writing all of the stats of the current game to the json file 
'''
stats_dict["Max score: "] = max(stats_dict["Max score: "], game_score)
stats_dict["Number of victories: "] += win
stats_dict["Number of defeats: "] += lose

with open("stats.json", "w") as stats_w:
    json.dump(stats_dict, stats_w, indent=4)


