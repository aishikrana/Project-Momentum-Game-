import pygame
import random


class rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.speedy = random.randrange(2,8)
        #self.rect.x=random.randrange(0,width)
        self.rect.x = random.randrange(-100, width)
        self.rect.y = random.randrange(-height,-5)
        #self.rect.y = random.randrange(0,height)
    def update(self):
        if self.rect.bottom > height:
            self.speedx = 1
            self.speedy = random.randrange(0,3)
            self.rect.x = random.randrange(-width,width)
            self.rect.y = random.randrange(-height,-5)
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
pygame.init()


clock = pygame.time.Clock()
fps = 60


width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Explosion Demo')
rain_img = pygame.image.load('expo_rain/explosion/snow.jfif').convert_alpha()
rain_img = pygame.transform.scale(rain_img, (5,5))
#define colours
bg = (50, 50, 50)

def draw_bg():
	screen.fill(bg)


#create Explosion class
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"expo_rain/explosion/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()


explosion_group = pygame.sprite.Group()

#create sprite group
rain_group = pygame.sprite.Group()
for i in range(200):
    Rain = rain()
    #rain_group.add(Rain)
    explosion_group.add(Rain)
run = True
while run:

	clock.tick(fps)

	#draw background
	draw_bg()

	explosion_group.draw(screen)
	explosion_group.update()
    #rain_group.update()
    #rain_group.draw(screen)

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			explosion = Explosion(pos[0], pos[1])
			explosion_group.add(explosion)


	pygame.display.update()

pygame.quit()