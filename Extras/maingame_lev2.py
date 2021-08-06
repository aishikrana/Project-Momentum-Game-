import pygame
import os  # for finding number of images in folder
import random  # for randomly choose a number in range
import csv
import math
import time
#added
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk



# Initializing Pygame
pygame.init()


#csv file info
filename = "Extras/img/login/db.csv"

# set frame rate
clock = pygame.time.Clock()
FPS = 60


SCREEN_WIDTH = 1536

SCREEN_HEIGHT = 800

# Create and Name window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MY GAME')


# define player action variables
moving_left = False
moving_right = False


## For Pause Button 
color_light = (240,151,7)
color_white = (255,255,255)
color_dark = (240,116,7)
width_pause = window.get_width()
height_pause = window.get_height()
smallfont_pause = pygame.font.SysFont('Arial Black',25)
text_pause = smallfont_pause.render(' | | ' , True , color_white)
pbx=-300-425
pby=-300-80
lenp=70*2/3
brep=65*2/3





#Login Credentials and loading from csv

#global Usernaam

fopen=open(filename,newline='')
r_list = csv.reader(fopen) # Here your csv file
lines = list(r_list)
col_len=len(lines)
fopen.close()
#print(lines)

chk=0
Usernaam=''


for ele in range(col_len):
	if lines[ele][0]=='mk':
		Usernaam=lines[ele][1]
		#print(Usernaam+'\n')
		#lines[ele][0]='nmk'
		chk=1
if chk==0:
	print('Rogue User Detected!')

#print(lines)
	
fopen=open(filename, 'w', newline='')
writer = csv.writer(fopen)
writer.writerows(lines)
fopen.close()

def mktonmk():
	r_list = csv.reader(open(filename,newline='')) # Here your csv file
	lines = list(r_list)
	col_len=len(lines)

	chk=0

	for ele in range(col_len):
		if lines[ele][0]=='mk':
			Usernaam=lines[ele][1]
			#print(Usernaam+'\n')
			#lines[ele][0]='nmk'
			chk=1
	if chk==0:
		print('Rogue User Detected!')
	
	# writer = csv.writer(open(filename, 'w', newline=''))
	# writer.writerows(lines)
    
#mktonmk()

def nmktomk():
	r_list_loc = csv.reader(open(filename,newline='')) # Here your csv file
	lines_loc = list(r_list_loc)
	col_len_loc=len(lines)

	chk_loc=0
	#print(lines)

	


	for ele_loc in range(col_len_loc):
		if Usernaam==lines[ele_loc][1]:
			lines[ele_loc][0]='mk'
			#lines[ele_loc][2]='trialmode'
			chk_loc=1
	if chk_loc==0:
		print('User Undetected!!')
	
	global writer
	writer = csv.writer(open(filename, 'w', newline=''))
	writer.writerows(lines)
	#print(lines)
	
	#Implement a score storing system




def back_levels():
	pause_screen.destroy()
	pause_pressed()

def resume_pressed():
	pause_screen.destroy()


def level_pressed():
    global pause_screen
    #pause_screen=Tk()
    pause_screen.geometry("670x400")
    pause_screen.title("Level Screen")
    image1 = Image.open("Extras/img/login/lgm.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

    label1.place(x=-9, y=-4)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 10,),borderwidth = '2')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')]) 


    but2=ttk.Button(text="Back", style="TButton", command = back_levels)
    but2.place(x=10,y=360)

    high=Label(pause_screen, text="HIGHSCORE", fg="white",bg="black", font=("century gothic", 20, 'bold'),borderwidth=4)
    high.place(x=250,y=10)  
    #level details
    levx=150
    levy=95
    dy=60   
    lev1=Label(pause_screen, text="Level 1 :", fg="white",bg="black", font=("century gothic", 14),borderwidth=2)
    lev1.place(x=levx,y=levy+dy*0)  
    lev2=Label(pause_screen, text="Level 2 :", fg="white",bg="black", font=("century gothic", 14),borderwidth=2)
    lev2.place(x=levx,y=levy+dy*1)  
    lev3=Label(pause_screen, text="Level 3 :", fg="white",bg="black", font=("century gothic", 14),borderwidth=2)
    lev3.place(x=levx,y=levy+dy*2)  
    lev4=Label(pause_screen, text="Level 4 :", fg="white",bg="black", font=("century gothic", 14),borderwidth=2)
    lev4.place(x=levx,y=levy+dy*3)  

    #score details
    skx=levx+160    
    #scoreloads
    skmin_1=''
    skmin_2=''
    skmin_3=''
    skmin_4=''
    sksec_1=''
    sksec_2=''
    sksec_3=''
    sksec_4=''
    skms_1=''
    skms_2=''
    skms_3=''
    skms_4=''
    score_1=''
    score_2=''
    score_3=''
    score_4=''

    f=open(filename,newline='')
    r_list_loc = csv.reader(f) # Here your csv file
    lines_loc = list(r_list_loc)
    col_len_loc=len(lines_loc)
    f.close()
    print(lines_loc)
    print('level_pressed')
    

    chk_loc=0
    

	#print (Usernaam+' Usernaam'+ '\n')


    for ele_loc in range(col_len_loc):
        #print (lines_loc[ele_loc][1]+'\n')
        if lines_loc[ele_loc][1]==Usernaam:
            skmin_1=lines_loc[ele][3]
            sksec_1=lines_loc[ele][4]
            skms_1=lines_loc[ele][5]
            skmin_2=lines_loc[ele][6]
            sksec_2=lines_loc[ele][7]
            skms_2=lines_loc[ele][8]
            skmin_3=lines_loc[ele][9]
            sksec_3=lines_loc[ele][10]
            skms_3=lines_loc[ele][11]
            skmin_4=lines_loc[ele][12]
            sksec_4=lines_loc[ele][13]
            skms_4=lines_loc[ele][14]

			
            chk_loc=1
    if chk_loc==0:
        print('User Undetected!! score load')
	
	#Concatenate
	
    score_1=skmin_1+':'+sksec_1+':'+skms_1
    score_2=skmin_2+':'+sksec_2+':'+skms_2
    score_3=skmin_3+':'+sksec_3+':'+skms_3
    score_4=skmin_4+':'+sksec_4+':'+skms_4


	#score_1='1'+' s'
    if skmin_1=='NA':
        sk_1=Label(pause_screen, text=skmin_1, fg="red",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_1.place(x=skx,y=levy+dy*0)
    else:
        #score_1+=' s'
        sk_1=Label(pause_screen, text=score_1, fg="green",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_1.place(x=skx,y=levy+dy*0)
	
    if skmin_2=='NA':
        sk_2=Label(pause_screen, text=skmin_2, fg="red",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_2.place(x=skx,y=levy+dy*1)
    else:
        #score_2+=' s'
        sk_2=Label(pause_screen, text=score_2, fg="green",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_2.place(x=skx,y=levy+dy*1)
	
    if skmin_3=='NA':
        sk_3=Label(pause_screen, text=skmin_3, fg="red",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_3.place(x=skx,y=levy+dy*2)
    else:
        #score_3+=' s'
        sk_3=Label(pause_screen, text=score_3, fg="green",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_3.place(x=skx,y=levy+dy*2)
	
    if skmin_4=='NA':
        sk_4=Label(pause_screen, text=skmin_4, fg="red",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_4.place(x=skx,y=levy+dy*3)
    else:
        #score_4+=' s'
        sk_4=Label(pause_screen, text=score_4, fg="green",bg="black", font=("banschrift", 14,'bold' ),borderwidth=2)
        sk_4.place(x=skx,y=levy+dy*3)











	
    pause_screen.mainloop()

def restart_pressed():
	
    #nmktomk()
    pause_screen.destroy()
    pygame.quit()
    os.system("python ../Project_Momentum/Extras/maingame_lev2.py")
    #os._exit(0)
    





def pause_pressed():

    global pause_screen
    pause_screen=Tk()
    pause_screen.geometry("670x400")
    pause_screen.title("Pause Screen")
    image1 = Image.open("Extras/img/login/lg1m.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

    label1.place(x=-9, y=-4)

    #Button Dealings
    b1x=300-50# X co-ordinate of b1
    b1y=70#y coordinate of b1
    b2x=b1x+0
    b2y=b1y+100
    b3x=b1x+0
    b3y=b1y+100*2

    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 20, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])

    but1=ttk.Button(text="Resume", style="TButton", command = resume_pressed)
    but1.place(x=b1x,y=b1y)
    but2=ttk.Button(text="Restart", style="TButton", command = restart_pressed)
    but2.place(x=b2x,y=b2y)
    but3=ttk.Button(text="Level History", style="TButton", command = level_pressed)
    but3.place(x=b3x,y=b3y)

	
    pause_screen.mainloop()








#When the level ends

def play_again():
    #nmktomk()
    end_screen.destroy()
    pygame.quit()
    os.system("python ../Project_Momentum/Extras/maingame_lev2.py")

def next_level():
    #nmktomk()
    end_screen.destroy()
    pygame.quit()
    os.system("python ../Project_Momentum/Extras/maingame_lev3.py")

def on_closing():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    end_screen.destroy()
    pygame.quit()

def EndGame(mini,sec,milisec):
    global end_screen
    end_screen=Tk()
    end_screen.geometry("730x460")
    end_screen.title("Level Completed!")
    image1 = Image.open("Extras/img/login/im1f.png")
    end_screen.title("Level Completed!")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

    label1.place(x=-2, y=-4)

    m=str(mini)
    s=str(sec)
    ms=str(milisec)

    tame=m+':'+s+':'+ms

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 11,),borderwidth = '2')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])

    but1=ttk.Button(text="Play Again", style="TButton", command = play_again)
    but1.place(x=10,y=420)

    but2=ttk.Button(text="Next Level", style="TButton", command = next_level)
    but2.place(x=620,y=420)

    msgdis='New Highscore!'

    #tame details
    tmx=240
    tmy=120

    tam1=Label(end_screen, text=tame, fg="red",bg="black", font=("century gothic", 50,'bold','italic'),borderwidth=2)
    tam1.place(x=tmx,y=tmy)

    

    tam0=Label(end_screen, text="TIME :", fg="white",bg="black", font=("century gothic", 28,),borderwidth=3)
    tam0.place(x=tmx+60,y=tmy-110)



    #Score Stroing System

    f=open(filename,newline='')
    r_list_loc = csv.reader(f) # Here your csv file
    lines_loc = list(r_list_loc)
    #global lines
    col_len_loc=len(lines_loc)
    f.close()
    # print(lines_loc)
    # print('endgame')

    chk_loc=0

    for ele_loc in range(col_len_loc):
        if lines_loc[ele_loc][1]==Usernaam:
            #global level
            rand=level+0
            if(lines_loc[ele_loc][rand*3]!='NA'):
                tempm=int(lines_loc[ele_loc][rand*3])
                temps=int(lines_loc[ele_loc][rand*3+1])
                tempms=int(lines_loc[ele_loc][rand*3+2])

                curt=mini*60000+sec*1000+milisec
                lurt=tempm*60000+temps*1000+tempms

                if(curt<lurt):
                    print(curt)
                    print('\n')
                    print(lurt)
                    tam2=Label(end_screen, text=msgdis, fg="light green",bg="black", font=("century gothic", 30,),borderwidth=2)
                    tam2.place(x=tmx-30,y=tmy+110)

                    lines_loc[ele_loc][rand*3]=m
                    lines_loc[ele_loc][rand*3+1]=s
                    lines_loc[ele_loc][rand*3+2]=ms
                
            elif(lines_loc[ele_loc][rand*3]=='NA'):
                tam2=Label(end_screen, text=msgdis, fg="light green",bg="black", font=("century gothic", 30,),borderwidth=2)
                tam2.place(x=tmx-30,y=tmy+110)

                lines_loc[ele_loc][rand*3]=m
                lines_loc[ele_loc][rand*3+1]=s
                lines_loc[ele_loc][rand*3+2]=ms
            
        chk_loc=1
    if chk_loc==0:
        print('User Undetected!! end game load')

    # print(lines_loc)
    # print('after endgame')

    f=open(filename, 'w', newline='')
    writer_loc= csv.writer(f)
    writer_loc.writerows(lines_loc)
    f.close()

    


     




    end_screen.mainloop()






# define game variables
timer = 0
GRAVITY = 0.5
ROWS = 50
TILE_SIZE = SCREEN_HEIGHT // ROWS
COLS = (1920 * 4) // TILE_SIZE
BG_SMALL_TYPES = len(os.listdir('Extras/img/tile')) - 2
BG_MAIN_TYPES = 5
level = 2
SCROLL_THRESH = 800  # distance player get before starting scroll #can move left or right by 200, and after that screen start scroll
scroll = 0
bg_scroll = 0
bg_layer_speed = [0.5, 0.6, 0.8, 1]
starting_time = pygame.time.get_ticks()
climb = 0


# load Images
# LOAD BACKGROUND IMAGES
bg_list = []
j = 1
while j <= 4:
    num_of_images = len(os.listdir(f'Extras/img/background/layer{j}'))
    x_list = []
    for i in range(num_of_images):
        img = pygame.image.load(
            f'Extras/img/background/layer{j}/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (1920, 800))
        x_list.append(img)
    j += 1
    bg_list.append(x_list)


#TILE
red_tile = pygame.image.load('Extras/img/tile/red_tile.jpg').convert_alpha()
red_tile = pygame.transform.scale(red_tile,(TILE_SIZE,TILE_SIZE))
#DEATH TILE
death_tile = pygame.image.load('Extras/img/tile/death_tile.png').convert_alpha()
death_tile = pygame.transform.scale(death_tile,(TILE_SIZE,TILE_SIZE))

# store b-small images in a list
img_list = []
for i in range(BG_SMALL_TYPES):
    img = pygame.image.load(f'Extras/img/tile/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

#load rain image
rain_img = pygame.image.load('Extras/img/rain.png')
rain_img = pygame.transform.scale(rain_img, (5, 10))


#load music
#running music
run_sound = pygame.mixer.Sound('Extras/img/music/sanhok running.mp3')
# jump music
jump_sound = pygame.mixer.Sound('Extras/img/music/idle jump.mp3')

# background
music = pygame.mixer.music.load('Extras/img/music/background map/sanhok background.mp3')
pygame.mixer.music.play(-1)

#rain
rain_sound = pygame.mixer.Sound('Extras/img/music/rain.mp3')
rain_sound.play()
#death music
death_sound = pygame.mixer.Sound('Extras/img/music/death music.mp3')

# define colors
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
DARK_GRAY = (15, 15, 15)

# define font
font = pygame.font.SysFont('Futura', 30)  # predefined function for fonts

# text on screen


def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    window.blit(img, (x, y))


# create function for drawing background
def draw_background():
    # window.fill(DARK_GREEN)
    width = 1920
    for x in range(4):
        for i in range(4):
             #rain
            if i == 2:
                for rain in rain_group:
                    if x==0:
                        rain.update()
                    window.blit(rain.image, (rain.rect.x + (x * SCREEN_WIDTH) - bg_scroll * bg_layer_speed[i], rain.rect.y, rain.rect.width, rain.rect.height))
                    
            if bg_data[i][x] >= 0:
                window.blit(bg_list[i][bg_data[i][x]], ((x * width) - bg_scroll * bg_layer_speed[i], 0))


class Snowball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.x = 0
        # self.y = 0
        self.x = random.randrange(SCREEN_WIDTH + 200)
        self.y = random.randrange(-50, SCREEN_HEIGHT)
        #  other variables for the snowflake
        self.size = random.randrange(30)/6
        self.speed = random.randrange(20, 40)
        self.angle = random.uniform(math.pi, math.pi * 2)

    def update(self, delta_time):
        if self.y > SCREEN_HEIGHT:
            self.x = random.randrange(0, SCREEN_WIDTH + 200)
            self.y = random.randrange(-SCREEN_HEIGHT, 0)
        self.y += self.speed * delta_time
        # Some math to make the snowflakes move side to side
        self.x += self.speed * math.cos(self.angle) * delta_time
        self.angle += 1 * delta_time


class rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = random.randrange(3,5)
        self.speedy = random.randrange(4,6)
        #self.rect.x=random.randrange(0,width)
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT)
        #self.rect.y = random.randrange(0,height)
    def update(self):
        if self.rect.bottom > SCREEN_HEIGHT:
            self.speedx = random.randrange(3,5)
            self.speedy = random.randrange(4,6)
            self.rect.x = random.randrange(-700, SCREEN_WIDTH)
            self.rect.y=random.randrange(0, 10)
        self.rect.x=self.rect.x+self.speedx
        self.rect.y= self.rect.y+self.speedy

# define class for instances of background images
class Background_image(pygame.sprite.Sprite):
    def __init__(self, type, x, y, distance):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.rect = img_list[type].get_rect()
        self.rect.topleft = (x, y)
        self.temp_x = x
        self.temp_y = y
        self.distance = distance  # actual distance from starting

    def draw(self):
        if scroll > 0 and bg_scroll > 0:
            self.rect.x += 5
        if scroll < 0 and bg_scroll < (COLS * TILE_SIZE) - SCREEN_WIDTH:
            self.rect.x -= 5
        window.blit(img_list[self.type], self.rect)


class World():
    def __init__(self):
        self.obstacle_list = []
        self.death_tile_list = []

    def process_data(self, data):
        self.level_length = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile == 1:
                    img = red_tile
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                elif tile == 2:
                    img = death_tile
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.death_tile_list.append(tile_data)

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += scroll
            # window.blit(tile[0], tile[1])
        for tile in self.death_tile_list:
            tile[1][0] += scroll
            # window.blit(tile[0], tile[1])


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.climbed = 0
        self.climb_activation = 0
        self.update_time = pygame.time.get_ticks()
        self.z = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump_run', 'Jump_Idle', 'climb']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(
                f'Extras/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(
                    f'Extras/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (100, 150))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self, moving_left, moving_right):
        screen_scroll = 0
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            if not(self.action == "Jump_idle" and (self.frame_index == 0 or self.frame_index == 2 or self.frame_index == 3)):
                self.vel_y = -11
                self.jump = False
                self.in_air = True
            # else:
            # 	self.vel_y = -11
            # 	self.jump = False
            # 	self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        global climb
        # check for collision with tiles
         #check with death tiles
        for tile in world.death_tile_list:
            # in x-direction
            if tile[1].colliderect(self.rect.x + 25 + dx, self.rect.y, 50, self.height):
                dx = 0
                self.alive = False
            # in y-direction
            if tile[1].colliderect(self.rect.x + 25, self.rect.y + dy, 50, self.height - 40):
                self.alive = False
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom
                    self.in_air = False


        #check with obstacle tiles
        for tile in world.obstacle_list:
            # check collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y - TILE_SIZE, self.width, self.height):
                if self.climbed == 0 and tile[1].colliderect(self.rect.x + dx, self.rect.y - 100, self.width, self.height):
                    # dx = tile[1].left - self.rect.right
                    dx = 0
                    self.climbed = 1
                    self.climb_activation = 1
                    if climb and self.climb_activation:
                        dy = -3
                        self.in_air = True
                    self.z = 1

                elif self.climbed == 1 and tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height - 120):
                    # dx = tile[1].left - self.rect.right
                    self.climb_activation = 1
                    dx = 0
                    if climb and self.climb_activation:
                        dy = -2
                        self.jump = True
                        self.in_air = False
                    self.z = 1

                else:
                    self.climbed = 0
                    dx = 0
                    # self.climb_activation = 0
            else:
                # 	self.climbed = 0
                self.climb_activation = 0
                # climb = 0

            # check collision in y-direction
            if climb and self.climb_activation:
                if self.vel_y >= 0:
                    self.vel_y = 0
            else:
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground, i.e. jumping
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile[1].bottom - self.rect.top
                    # check if above the ground, i.e falling
                    elif self.vel_y >= 0:
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom
                        self.in_air = False
                    self.z = 0

        # check if going off the edges of the screen
        if self.char_type == 'player':
            if self.rect.left + dx < 0:
                dx = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        global bg_scroll
    # update scroll based on player position
        if self.char_type == 'player':
            # self.rect.right > (SCREEN_WIDTH - SCROLL_THRESH) and
            # self.rect.left < SCROLL_THRESH  and bg_scroll > abs(dx)
            if dx > 0 and bg_scroll < (7660) - SCREEN_WIDTH and self.rect.right > (SCREEN_WIDTH - SCROLL_THRESH):
                self.rect.x -= dx  # make position of player back to its previous position
                screen_scroll = -dx  # screen start move in opposite direction
            elif dx < 0 and self.rect.left < 300:
                if bg_scroll > 0:
                    self.rect.x -= dx  # make position of player back to its previous position
                    screen_scroll = -dx  # screen start move in opposite direction
                else:
                    bg_scroll = 0

        return screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 300  # cooldown for idle
        if(self.action == 1):
            ANIMATION_COOLDOWN = 30  # cooldown for run
        elif(self.action == 2):
            ANIMATION_COOLDOWN = 100  # cooldown for run and jump
        elif(self.action == 3):
            if self.frame_index == 0 or self.frame_index == 2 or self.frame_index == 3:
                ANIMATION_COOLDOWN = 200  # cooldown for idlejump
            else:
                ANIMATION_COOLDOWN = 500
        elif self.action == 4:
            ANIMATION_COOLDOWN = 500
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        # flip funtion in pygame   Image        flip            x-axis Y-axis
        window.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)


# create group for background images
bg_group = pygame.sprite.Group()

# sprite group for rain
rain_group = pygame.sprite.Group()


for i in range(100):
    Rain = rain()
    rain_group.add(Rain)

dust_snow_data = [0, 0, 0]

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)

# background layers data
bg_data = [[-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1]]

# load in level data and create world
def load_data(level):
    with open(f'Extras/level{level}_data.csv', 'r', newline='') as csvfile:  # It opens the file
        # delimiter refers to character that separates the value from each other
        reader = csv.reader(csvfile, delimiter=',')
        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                if x < ROWS:  # TILE DATA
                    # since data stored in csv file in strings so for storing it back to world data, convert values to integer
                    world_data[x][y] = int(tile)
            if x >= ROWS and x < ROWS + 4:
                for i in range(4):
                    bg_data[x-ROWS][i] = int(row[i])
            if x >= ROWS + 4 and x < ROWS + 7:
                dust_snow_data[x - ROWS - 4] = int(row[0])
            if x >= ROWS + 7:
                # since data store in csv is in strings, so convert them first to int
                new = Background_image(int(row[0]), int(
                    row[1]), int(row[2]), int(row[3]))
                bg_group.add(new)
    return world_data

world_data = load_data(level)
world = World()
world.process_data(world_data)

player = Soldier('player', 200, 500, 1.65, 4)

#####
#pause time
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

#####
#timer variable
start_ticks =pygame.time.get_ticks()
start_run = pygame.time.get_ticks()
RUN_COOLDOWN = 1400
e=0
s=0

run = True
while run:

    clock.tick(FPS)

    # update background
    draw_background()
    # for sprite group of background
    for bg in bg_group:
        bg.draw()
        bg.check()
    # draw world map
    world.draw()

    player.update_animation()
    player.draw()

    # update player actions
    if player.alive:
        if player.z and (moving_left or moving_right) and climb:
            run_sound.stop()
            x = 0
            player.update_action(4)  # 4: climb
        elif player.in_air:
            run_sound.stop()
            x = 0
            if moving_left or moving_right:
                player.update_action(2)  # 2 jump + run
            else:
                player.update_action(3)  # 3 jump idle

        elif moving_left or moving_right:
            if x == 0 and (pygame.time.get_ticks() - start_run) < RUN_COOLDOWN:
                run_sound.stop()
                run_sound.play()
                x = 1
            if pygame.time.get_ticks() - start_run >= RUN_COOLDOWN:
                run_sound.stop()
                start_run = pygame.time.get_ticks()
                run_sound.play()

            player.update_action(1)  # 1: run
        else:
            run_sound.stop()
            x = 0
            player.update_action(0)  # 0: idle
        scroll = player.move(moving_left, moving_right)
        bg_scroll -= scroll


    # timer
    # pygame.time.get_ticks() give current time from starting in milliseconds
    milisec = (int((pygame.time.get_ticks() - start_ticks) / 10)) % 100
    seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
    sec = seconds % 60
    mins = seconds // 60
    text = font.render(("Time: " + str(mins).zfill(2) + ":" + str(sec).zfill(2)) + ":" + str(milisec), True,(255, 255, 255))
    window.blit(text, (1380, 20))
    

    #player dead
    if player.rect.top > SCREEN_HEIGHT + 30 or player.alive == False:
        run_sound.stop()
        jump_sound.stop()
        death_sound.play()
        player.rect.center = (200, 500)
        scroll = 0
        bg_scroll = 0
        world = World()
        world.process_data(world_data)
        player.alive = False
        start_ticks += 3000
        pygame.time.delay(3000)
    else:
        player.alive = True
    
    #level clear
    if player.rect.left >= SCREEN_WIDTH:
        run_sound.stop()
        jump_sound.stop()
        player.alive = False
        #pygame.quit()
        EndGame(mins,sec,milisec)
        player.alive = False
    else:
        player.alive = True


    # EVENT KEYPRESSING
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player.alive:
                if climb==0:
                    jump_sound.play()
                player.jump = True
            if event.key == pygame.K_w:
                climb = 1
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RSHIFT:
                player.speed = 30


        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                climb = 0
            if event.key == pygame.K_RSHIFT:
                player.speed = 4

        #Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width_pause/2+pbx <= mouse[0] <= width_pause/2+pbx+lenp and height_pause/2+pby <= mouse[1] <= height_pause/2+brep+pby:
                s = time.time()
                pause_pressed()
                e = time.time()
                start_ticks = start_ticks + int((e-s)* 1000)
                	
		
	#Mouse Button Dealings
    mouse = pygame.mouse.get_pos()
    #for hover effect
    if width_pause/2+pbx <= mouse[0] <= width_pause/2+pbx+lenp and height_pause/2+pby <= mouse[1] <= height_pause/2+brep+pby:
        pygame.draw.rect(window,color_light,[width_pause/2+pbx,height_pause/2+pby,lenp,brep])

    else:
        pygame.draw.rect(window,color_dark,[width_pause/2+pbx,height_pause/2+pby,lenp,brep])

    
    window.blit(text_pause , (width_pause/2+5+pbx,height_pause/2+pby))

        

    pygame.display.update()
    # making the time interval of the loop 1sec
pygame.quit()
