#imports and init
import pygame
import random
import time
from itertools import chain

pygame.init()

#Colors
black = pygame.Color((0,0,0))
white = pygame.Color((255,255,255))
red = pygame.Color((255,0,0))
blue = pygame.Color((0,0,255))
green = pygame.Color((0,255,0))

#Some game variables
screen_width = 400
screen_height = 600
speed = 5
#scores
score = 0
coin_score = 0

#fonts and game over text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)


#bg image
background = pygame.image.load("AnimatedStreet.png")
#file paths
coin_img = "coin.png"
coin_sfx = "getcoin.mp3"
diamond_img = "diamond.png"
diamond_sfx = "getdiamond.mp3"
emerald_img = "emerald.png"
emerald_sfx = "getemerald.mp3"

#screen and frame counter
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
loop = True

#Enemy and Player classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), -20)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > screen_height):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), -20)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        self.speed = 5
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-self.speed,0)
        if self.rect.right < screen_width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(self.speed,0)

#coin class
class Coin(pygame.sprite.Sprite):
    coin_count = 0
    group = pygame.sprite.Group()
    def __init__(self, image, sfx, tier):
        #init with image, sound effect and tier - the value of a coin
        super().__init__()
        self.image = pygame.image.load(image)
        self.sfx = pygame.mixer.Sound(sfx)
        self.rect = self.image.get_rect()
        self.tier = tier
        self.generated = False



    def invalid_collision(self):
        #if a coin collides with an enemy it is considered as not generated, and thus 
        #we generate it again with different coords
        if pygame.sprite.spritecollideany(self, enemies):
            self.generated = False
        #here we copy the sprite group, delete the current sprite from it
        Coin_group_copy = Coin.group.copy()
        Coin_group_copy.remove(self)
        #then we check if the current sprite collides with any of the other Coin sprites
        #if it does, we consider it as not generated and generate again
        if pygame.sprite.spritecollideany(self, Coin_group_copy):
            self.generated = False
    
    def gen_rect(self, enemy):
        #if the rect was already generated, there is nothing to go here
        if self.generated:
            return

        #we select a range of numbers that specifically excludes the coords of the enemy's rect object
        coord_range = list(chain(range(22, enemy.rect.center[0] - 50), range(enemy.rect.center[0] + 50, screen_width - 22)))
        #we select a center for our coin sprite from this range and mark it as generated
        self.rect.center = (random.choice(coord_range), 0)
        self.generated = True
    

    def move(self, enemy):  #moving the coin just like the enemies
        self.rect.move_ip(0,speed)
        if self.rect.top > screen_height:
            #if the coin has passed the bottom, we generate it again 
            self.generated = False
            self.gen_rect(enemy)
            self.rect.top = 0



#instances of player and enemy
P1 = Player()
E1 = Enemy()
#instances of 3 types of coins
coin = Coin(coin_img, coin_sfx, tier = 1)
diamond = Coin(diamond_img, diamond_sfx, tier = 2)
emerald = Coin(emerald_img, emerald_sfx, tier = 3)

#Sprite group for enemies
enemies = pygame.sprite.Group()
enemies.add(E1)

#Sprite group for Coins
Coin.group.add(coin)
Coin.group.add(diamond)
Coin.group.add(emerald)

#Sprite group for cars specifically
car_sprites = pygame.sprite.Group()
car_sprites.add(P1, E1)

#all sprties group (needed when exiting he game on failure)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, coin)

#New User event
inc_speed = pygame.USEREVENT + 1


while loop:
    for event in pygame.event.get():
        #custom event that increases speed
        if event.type == inc_speed:
            speed += 1

        if event.type == pygame.QUIT:
            loop = False
    

    #screen and the scores
    screen.blit(background, (0,0))


    #blits and moves all car sprites
    for entity in car_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #moving coin sprites
    for obj in Coin.group:
        #checking for invalid collisions
        obj.invalid_collision()
        obj.gen_rect(E1)
        #then drawing the coins if their rect objects were created
        if obj.generated:
            screen.blit(obj.image, obj.rect)
            obj.move(E1)


    #game over screen
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(5)
        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        screen.fill((255,0,0))
        loop = False

    
    #collision with the coins
    #we get the list of collided coins
    collidelist = pygame.sprite.spritecollide(P1, Coin.group, dokill=True)
    #if it is not empty
    if collidelist:
        #we iterate over it and reinit the correspoding coins and play their sound and add their values to the score
        for obj in collidelist:
            obj.sfx.play()
            coin_score += obj.tier

            if obj.tier == 1:
                coin = Coin(coin_img, coin_sfx, tier = 1)
                Coin.group.add(coin)
                all_sprites.add(coin)

            elif obj.tier == 2:
                diamond = Coin(diamond_img, diamond_sfx, tier = 2)
                Coin.group.add(diamond)
                all_sprites.add(diamond)

            else:
                emerald = Coin(emerald_img, emerald_sfx, tier = 3)
                Coin.group.add(emerald)
                all_sprites.add(emerald)
            #counting the coins 
            Coin.coin_count += 1
    
    #when the coint count reaches 5 we add our custom event that increases the enemy speed to the event queue
    #and we also drop the count back to 0
    if Coin.coin_count == 5:
        Coin.coin_count = 0
        pygame.event.post(pygame.event.Event(inc_speed))
    
    #printing out the scores
    scores = font_small.render(str(score), True, black)
    coin_scores = font_small.render(f"Coins: {coin_score}", True, black)

    screen.blit(scores, (10,10))
    screen.blit(coin_scores, (280, 10))
    
    pygame.display.flip()
    clock.tick(60)


