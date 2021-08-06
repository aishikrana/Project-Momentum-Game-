import pygame
from pygame.constants import GL_CONTEXT_RELEASE_BEHAVIOR
import button
import csv
import os           #for getting length of folder
import random



#tempprary background

class rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 2
        self.speedy = random.randrange(2,8)
        #self.rect.x=random.randrange(0,width)
        self.rect.x = random.randrange(-600+scroll, width + scroll)
        self.rect.y = random.randrange(2,8)
        #self.rect.y = random.randrange(0,height)

    def update(self):
        if self.rect.bottom>height:
            self.speedx = 1
            self.speedy = random.randrange(2,8)
            self.rect.x = random.randrange(-width,width+scroll)
            self.rect.y=random.randrange(-height,-5)
        self.rect.x=self.rect.x+self.speedx
        self.rect.y= self.rect.y+self.speedy
pygame.init()


# clock = pygame.time.Clock()
# fps = 60

# width = 800
# height = 600

# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Explosion Demo')

#define colours
# bg = (50, 50, 50)

# def draw_bg():
# 	screen.fill(bg)


#create Explosion class
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"Extras/expo_rain/explosion/exp{num}.png")
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














# pygame.init()

#FPS
clock = pygame.time.Clock()
FPS = 60


#game WINDOW
TOTAL_WIDTH = 1900
TOTAL_HEIGHT = 1000
SCREEN_WIDTH = 1536
width = SCREEN_WIDTH
SCREEN_HEIGHT = 800
height = SCREEN_HEIGHT
LOWER_MARGIN = TOTAL_HEIGHT - SCREEN_HEIGHT
SIDE_MARGIN = TOTAL_WIDTH - SCREEN_WIDTH


#display on WINDOW
window = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


#DEFINE GAME VARIABLES
ROWS = 50
TILE_SIZE = SCREEN_HEIGHT // ROWS
MAX_COLUMNS = (1920 * 4) // TILE_SIZE
BG_SMALL_TYPES = len(os.listdir('Extras/img/tile')) - 2
BG_MAIN_TYPES = 5
current_bg = -1
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1
level = 0
bg_count = 0
bg_pressed = 0
tile_flag = 0
death_tile_flag = 0
load_button_press = 0
bg_flag = [-1, -1, -1, -1]
bg_layer_speed = [0.5, 0.6, 0.8, 1]



#LOAD BACKGROUND IMAGES
bg_list = []
j = 1
while j <= 4:
    num_of_images = len(os.listdir(f'Extras/img/background/layer{j}')) 
    x_list = []
    for i in range(num_of_images):
        img = pygame.image.load(f'Extras/img/background/layer{j}/{i}.png').convert_alpha()
        img = pygame.transform.scale(img,(1920,800))
        x_list.append(img)
    j += 1
    bg_list.append(x_list)


#store b-small images in a list
img_list = []
for i in range(BG_SMALL_TYPES):
    img = pygame.image.load(f'Extras/img/tile/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (125, 125))
    img_list.append(img)

#TILE
red_tile = pygame.image.load('Extras/img/tile/red_tile.jpg').convert_alpha()
red_tile = pygame.transform.scale(red_tile,(TILE_SIZE,TILE_SIZE))
#DEATH TILE
death_tile = pygame.image.load('Extras/img/tile/death_tile.png').convert_alpha()
death_tile = pygame.transform.scale(death_tile,(TILE_SIZE,TILE_SIZE))


#image for clear button
clear_image = pygame.image.load('Extras/img/background/clear.png').convert_alpha()

# images of load and save button
load_image = pygame.image.load('Extras/img/load_btn.png').convert_alpha()
save_image = pygame.image.load('Extras/img/save_btn.png').convert_alpha()



#DEFINE COLORS
GREEN = (144, 201,120)
WHITE = (255 , 255 , 255)
RED = (200 , 25, 25 )
BLACK = (0 , 0, 0)
DARK_GREEN = (0, 51, 51)
DARK_KHAKI = (189,183,107)
GRAY = (119,136,153)
CORNSILK = (255, 248, 220)
BLUE = (61, 183, 228)


#define font
font  = pygame.font.SysFont('Futura', 30)

#Create Empty Tile List
world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COLUMNS
    world_data.append(r)


#function for outputtng text onto the screen
# so we have to convert our text to image and then blit it
def draw_text(text, font, text_color, x , y):
    img = font.render(text, True, text_color)    #convert text to image
    window.blit(img , (x, y))




#define class for instances of background images
class Background_image(pygame.sprite.Sprite):
    def __init__(self, type, x, y, distance):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.rect = img_list[type].get_rect()
        self.rect.topleft = (x, y)
        self.temp_x = x
        self.temp_y = y
        self.distance = distance            #actual distance from starting
    
    def draw(self):
        if scroll_left and scroll > 0 :
            self.rect.x += 5 * scroll_speed
        if scroll_right and scroll < ( MAX_COLUMNS * TILE_SIZE ) - SCREEN_WIDTH :
            self.rect.x -= 5 * scroll_speed
        window.blit(img_list[self.type], self.rect)

    def draw_load(self):
        self.rect.x = self.distance + self.temp_x

    def check(self):
        #check if mouse right click over it
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[2]==1:
                self.kill()



#create function for drawing background
def draw_bg():
    window.fill(DARK_GREEN)
    width = 1920
    for x in range(4):
        for i in range(4):
            # if x==0 and i==1:
                #temp background
                # explosion_group.draw(window)
                # explosion_group.update()
            if bg_data[i][x] >= 0:
                window.blit(bg_list[i][bg_data[i][x]],(( x * width) -scroll* bg_layer_speed[i]  ,0))


#draw grid
def draw_grid():
    #vertical lines
    for i in range(MAX_COLUMNS + 1):
        pygame.draw.line(window, BLUE, (i * TILE_SIZE - scroll , 0) , (i * TILE_SIZE - scroll, SCREEN_HEIGHT))
    #horizontal lines
    for i in range(ROWS + 1):
            pygame.draw.line(window, BLUE, (0 , i * TILE_SIZE) , (SCREEN_WIDTH,i * TILE_SIZE))


#function for drawing the world tiles
def draw_world():
    for i in range(ROWS):
        for j in range(MAX_COLUMNS):
            if world_data[i][j] == 1:       #check if tile is present
                window.blit(red_tile, (j * TILE_SIZE - scroll, i * TILE_SIZE))
            elif world_data[i][j] == 2:       #check if tile is present
                window.blit(death_tile, (j * TILE_SIZE - scroll, i * TILE_SIZE))



#function for screen resize
def window_resize(width, height,button_list):
    window = pygame.display.set_mode((width, height),pygame.RESIZABLE)
    global SCREEN_HEIGHT
    global LOWER_MARGIN
    global SCREEN_WIDTH
    global SIDE_MARGIN
    global TILE_SIZE
    SCREEN_HEIGHT = int(height*(64/74))
    LOWER_MARGIN = int(height*(10/74))
    SCREEN_WIDTH = int((8/11)*width)
    SIDE_MARGIN = int((3/11)*width)
    TILE_SIZE = SCREEN_HEIGHT // ROWS
    #creating instance of buttons
    create_buttons(button_list)

def create_buttons(button_list):
    #create buttons
    button_row = 0
    button_column = 0
    
    for j in range(4):
        temp = []
        button_row = j*5
        if j==3:
            button_row = (j-1)*4
        button_column = 0
        for i in range(len(bg_list[j])):
            new_button = button.Button(SCREEN_WIDTH + (button_column * 150) + 50, (button_row * 60) + 60, bg_list[j][i], 120 , 40)
            temp.append(new_button)
            button_column += 1
            if button_column == 2:
                button_row += 1
                button_column = 0
        if(j!=2):
            new_button = button.Button(SCREEN_WIDTH + (button_column * 150) + 50, (button_row * 60) + 60, clear_image, 120 , 40)
            temp.append(new_button)
        Bg_ButtonList.append(temp)
    button_row = 0
    button_column = 0

    for i in range(len(img_list)):
        new_button = button.Button(1100 + (button_column * 60), 750 + (button_row * 60) + 60, img_list[i], 40 , 40)
        button_list.append(new_button)
        button_column += 1
        if button_column == 7:
            button_row += 1
            button_column = 0
    button_row += 2
    #button for red tile
    global red_tile_button
    red_tile_button = button.Button( 850 , SCREEN_HEIGHT + 20, red_tile, 40, 40 )
     #button for death tile
    global death_tile_button
    death_tile_button = button.Button( 850 , SCREEN_HEIGHT + 90, death_tile, 40, 40 )
    #button for save and load 
    global save_button
    global load_button
    save_button = button.Button(300 , SCREEN_HEIGHT + int(LOWER_MARGIN/2) + 30, save_image, save_image.get_width(), save_image.get_height())
    load_button = button.Button(500, SCREEN_HEIGHT + int(LOWER_MARGIN/2) + 30, load_image, load_image.get_width(), load_image.get_height())
    #dust button



#create group for background images
bg_group = pygame.sprite.Group()


#make a button list by creating instance of buttons
button_list = []
Bg_ButtonList = []
save_button = 0
load_button = 0
red_tile_button = 0
death_tile_button = 0
create_buttons(button_list)



#background layers data
bg_data = [[-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1]]



#temp bg


rain_img = pygame.image.load("Extras/expo_rain/explosion/rain1.png").convert_alpha()
rain_img = pygame.transform.scale(rain_img, (10,10))


explosion_group = pygame.sprite.Group()



#create sprite group
rain_group = pygame.sprite.Group()
for i in range(200):
    Rain = rain()
    #rain_group.add(Rain)
    explosion_group.add(Rain)

dust_snow_data = [0,0,0]




run = True
while run:

    clock.tick(FPS)

     #scroll the map
    if scroll_left:
        if scroll > 0:
            scroll -= 5 * scroll_speed
        else:
            scroll = 0
    if scroll_right and scroll < 7660 - SCREEN_WIDTH:
        scroll += 5 * scroll_speed
        
    draw_bg()

    #for sprite group of background
    for bg in bg_group:
        bg.draw()
        bg.check()
        if load_button_press:
            bg.draw_load()
    draw_world()
    draw_grid()


    #draw tile panels and tiles (buttons of tiles)
    pygame.draw.rect(window, GRAY, (SCREEN_WIDTH, 0 , SIDE_MARGIN, TOTAL_HEIGHT))

    #drawing text
    draw_text('Select First Layer Background:', font, WHITE, SCREEN_WIDTH + 10, 15)
    draw_text('Select Second Layer Background:', font, WHITE, SCREEN_WIDTH + 10, 330)
    # draw_text('Select Third Layer Background:', font, WHITE, SCREEN_WIDTH + 10, 500)
    draw_text('Select Base Layer:', font, WHITE, SCREEN_WIDTH + 10, 540)
    draw_text('Main Tile:', font, WHITE, 710 , SCREEN_HEIGHT +20)
    draw_text('Death Tile:', font, WHITE, 710 , SCREEN_HEIGHT +100)
    draw_text('Press UP or DOWN to change level', font, WHITE, 10, SCREEN_HEIGHT + (4/10)*LOWER_MARGIN)
    draw_text(f'Level: {level}', font, WHITE, 10, SCREEN_HEIGHT + (1/10)*LOWER_MARGIN)
    
    

    # Save and Load data
    if save_button.draw(window):
        #highlight button while clicked
        pygame.draw.rect(window, WHITE, save_button.rect, 3)  #3 is for border line
        #background data is in bacground sprite group
        #save level data
        #           name of file            write
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile:      #It opens the file
            writer = csv.writer(csvfile, delimiter = ',')                     #delimiter refers to character that separates the value from each other
            for row in world_data:
                writer.writerow(row)
            for row in bg_data:
                writer.writerow(row)
            for bg in bg_group:           #background sprite group
                writer.writerow([bg.type, bg.temp_x, bg.temp_y, bg.distance])

    if load_button.draw(window):
        #load in level data
        #highlight button while clicked
        pygame.draw.rect(window, WHITE, load_button.rect, 3)  #3 is for border line
        #reset scroll back to the start of the level
        scroll = 0
        with open(f'Extras/level{level}_data.csv', 'r', newline='') as csvfile:      #It opens the file
            reader = csv.reader(csvfile, delimiter = ',')                     #delimiter refers to character that separates the value from each other
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    if x < ROWS:                             #TILE DATA    
                        world_data[x][y] = int(tile)         #since data stored in csv file in strings so for storing it back to world data, convert values to integer
                if x >= ROWS and x< ROWS + 4:
                    for i in range(4):
                        bg_data[x-ROWS][i] = int(row[i])
                if x >= ROWS + 4 and x < ROWS + 7:
                    dust_snow_data[x - ROWS - 4] = int(row[0])
                if x >= ROWS + 7:
                    new_bg = Background_image(int(row[0]), int(row[1]), int(row[2]), int(row[3]))       #since data store in csv is in strings, so convert them first to int
                    bg_group.add(new_bg)
        #set load_button_press variable to 1
        load_button_press = 1
    else:
        load_button_press = 0


    #check if red tile been pressed
    if red_tile_button.draw(window):
        tile_flag = 1
        current_bg = -1
    #check if death tile been pressed
    if death_tile_button.draw(window):
        tile_flag = 2
        current_bg = -1

    #highlight tile with boundry
    if(tile_flag==1):
        pygame.draw.rect(window, WHITE, red_tile_button.rect, 3)  #3 is for border line
    elif(tile_flag==2):
        pygame.draw.rect(window, RED, death_tile_button.rect, 3)  #3 is for border line


    #choose layers background which are being clicked
    for j, row in enumerate(Bg_ButtonList):
        for i, x in enumerate(row):
            if x.draw(window):
                bg_flag[j] = i
                if i==len(bg_list[j]):
                    bg_data[j][int((scroll * bg_layer_speed[j] + SCREEN_WIDTH )) // 1920] = -1
                else:
                    bg_data[j][int((scroll * bg_layer_speed[j] + SCREEN_WIDTH )) // 1920] = i
                    
        if bg_flag[j]>=0:
            pygame.draw.rect(window, RED, row[bg_flag[j]].rect, 3)  #3 is for border line

    #choose background which is being clicked
    button_count = 0
    for i in button_list:
        if i.draw(window):
            current_bg = button_count
            bg_pressed = 1
            tile_flag = 0
        button_count += 1
    
        
    #highlight the selected tile with red boundry
    if(current_bg != -1):
        pygame.draw.rect(window, RED, button_list[current_bg].rect, 3)  #3 is for border line


    #add new tiles to the screen
    #get current mouse position
    if tile_flag:
        mouse_position = pygame.mouse.get_pos()
        x = (mouse_position[0] + scroll) // TILE_SIZE      #0 for x, and 1 for y. This calculates the index of world_data.
        y = (mouse_position[1]) // TILE_SIZE

        #check that the coordinates are within the tile area
        if mouse_position[0] < SCREEN_WIDTH and mouse_position[1] < SCREEN_HEIGHT:
            #update tile value
            if pygame.mouse.get_pressed()[0] == 1 :        #if left mouse clicked
                if world_data[y][x] == -1:
                    if tile_flag == 1:
                        world_data[y][x] = 1
                    else:
                        world_data[y][x] = 2
            if pygame.mouse.get_pressed()[2] == 1:          #right click deletes tile from that position
                world_data[y][x] = -1
                
    elif current_bg != -1:
        #add new background images to the screen
        #get current mouse position
        mouse_position = pygame.mouse.get_pos()
        x = (mouse_position[0])
        y = (mouse_position[1])
        if x < SCREEN_WIDTH and y < SCREEN_HEIGHT: 
            # if bg_pressed==1:
            window.blit(img_list[current_bg],(x,y))
            if pygame.mouse.get_pressed()[0] == 1 and bg_pressed == 0 :
                bg_pressed = 1
                new_bg = Background_image(current_bg, x , y, scroll)
                bg_group.add(new_bg)
        if pygame.mouse.get_pressed()[0] == 0:
            bg_pressed = 0


    # #temp background
    # explosion_group.draw(window)
    # explosion_group.update()






    #EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True 
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1
            if event.key == pygame.K_ESCAPE:
                run = False
        
        #keyboard unpresses
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            explosion = Explosion(pos[0], pos[1])
            explosion_group.add(explosion)

        #for window resize
        if event.type == pygame.VIDEORESIZE:
            # window_resize()
            button_list = []
            window_resize(event.w, event.h,button_list)
    pygame.display.update()

pygame.quit()