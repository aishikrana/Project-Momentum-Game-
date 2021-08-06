import pygame
import random
import math

pygame.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ritik Snow')
#define colours
BLACK = (0,0,0)
WHITE = (169,169, 169)

def draw_bg():
	window.fill(BLACK)

class Snowball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.x = 0
        # self.y = 0
        self.x = random.randrange(SCREEN_WIDTH)
        self.y = random.randrange(-SCREEN_HEIGHT, 0)
        #  other variables for the snowflake
        self.size = random.randrange(4)
        self.speed = random.randrange(20, 40)
        self.angle = random.uniform(math.pi, math.pi * 2)

    def update(self, delta_time):
        if self.y > SCREEN_HEIGHT:
            self.x = random.randrange(0, SCREEN_WIDTH)
            self.y = random.randrange(-SCREEN_HEIGHT, 0)
        self.y += self.speed * delta_time
        # Some math to make the snowflakes move side to side
        self.x += self.speed * math.cos(self.angle) * delta_time
        self.angle += 1 * delta_time


# class Snowfall:
#     def __init__(self):
#         # self.n = n
#         self.snow_list  = []
#     def start_snowfall(self):
#         self.snow_list = []
#         for i in range(150):
#             snow = Snowball()
#             snow.x = random.randrange(SCREEN_WIDTH)
#             snow.y = random.randrange(SCREEN_HEIGHT + 200)
#             # Set other variables for the snowflake
#             snow.size = random.randrange(4)
#             snow.speed = random.randrange(20, 40)
#             snow.angle = random.uniform(math.pi, math.pi * 2)

#             # Add snowflake to snowflake list
#             self.snow_list.append(snow)

#     def draw(self):
#         for snowflake in self.snow_list:
#             pygame.draw.circle(window, WHITE, (snowflake.x, snowflake.y), snowflake.size)
    
#     def update(self, delta_time):
#          for snowflake in self.snow_list:
#             snowflake.y -= snowflake.speed * delta_time

#             # Check if snowflake has fallen below screen
#             if snowflake.y < 0:
#                 snowflake.update()

#             # Some math to make the snowflakes move side to side
#             snowflake.x += snowflake.speed * math.cos(snowflake.angle) * delta_time
#             snowflake.angle += 1 * delta_time


snow_list = pygame.sprite.Group()
for i in range(200):
    Rain = Snowball()
    snow_list.add(Rain)

run = True
while run:
    clock.tick(fps)
    draw_bg()

    # snowfall = Snowfall()
    # snowfall.start_snowfall()
    # snowfall.update(1)
    # snowfall.draw()
    for snow in snow_list:
        snow.update(0.02)
        pygame.draw.circle(window, WHITE, (snow.x, snow.y), snow.size)
	#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()