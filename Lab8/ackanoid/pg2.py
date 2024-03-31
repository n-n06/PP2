import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
#vars related to change over time
timer1 = 0
timer2 = 0
change_period = 3


done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')
special_collision_sound = pygame.mixer.Sound('special catch.wav')
boom_collision_sound = pygame.mixer.Sound('boom.ogg')

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

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#ver for help. when the game enter a loop, the player can place the ball in the middle 
#but with the price of +2 speed for the ball
help_used = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    #drawing blocks
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

    for unbreakable_color, unbreakable_block in unbreakable_list:
        pygame.draw.rect(screen, unbreakable_color, unbreakable_block)
        pygame.draw.line(screen,
                         (255 - unbreakable_color[0], 255 - unbreakable_color[1], 255 - unbreakable_color[2]),
                         unbreakable_block.topleft,
                         unbreakable_block.bottomright,
                         width=3)
        
    #drawing paddle and ball
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    

    #2 timer for the ball's speed and paddle's size
    #ball's speed is increased over time, while the paddle's width and height is decreased
    timer1 += clock.get_rawtime() / 1000
    timer2 += clock.get_rawtime() / 1000
    change_ball_speed(change_period)
    change_paddle_size(change_period)
    

    #Ball movement
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
        #if the rect is special, we get 2 points for it, and play a different sound
        if hitRect in special_block_list:
            special_block_list.remove(hitRect)
            special_color_list.remove(hitColor)
            special_list.remove((hitColor, hitRect))
            game_score += 2
            special_collision_sound.play()
        #if the hit rect is unbreakable we do not delete it from anywhere and play another sound - vine boom
        elif hitRect in unbreakable_block_list:
            boom_collision_sound.play()
        else:
            game_score += 1
            collision_sound.play()

        dx, dy = detect_collision(dx, dy, ball, hitRect)
      
        


    
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif all(block in unbreakable_block_list for block in block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    

    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    #this setting is my solution for the problem where the ball is stuck in some closed loop and continues to move only inside of it. Basically, by pressing CTRL-H, the user can get one time help - place the ball in the center again but with the price of +2 speed
    if (key[pygame.K_LCTRL] or key[pygame.K_RCTRL]) and key[pygame.K_h] and not help_used:
        ball.x = W // 2
        ball.y = H // 2
        ballSpeed += 2
        help_used = True
        

    pygame.display.flip()
    clock.tick(FPS)


