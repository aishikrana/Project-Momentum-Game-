#import modules

from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import pygame
from time import sleep
import csv
pygame.init()




gk=0
filename = "Extras/img/login/db.csv"
# tix=Labelop
# rix=Label
Usernaam=''

# Designing window for registration

def register():
    #global register_screen
    #register_screen = Toplevel(main_screen)
    main_screen.title("Register")
    #register_screen.geometry("300x250")

    image1 = Image.open("Extras/img/login/7f.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=-9, y=-4)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    login_font=('Bahnschrift',15)

   
    username_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=username )
    username_entry.place(x=890,y=250+200,height=30,width=250)
    username_entry.insert(0,'Enter Username:')

    username_entry.bind("<Button-1>", click_but3)
    username_entry.bind("<Leave>", leave_but3)
        
    
    password_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=password )
    password_entry.place(x=890,y=310+200,height=30,width=250)
    password_entry.insert(0,'Enter Password:')

    password_entry.bind("<Button-1>", click_but4)
    password_entry.bind("<Leave>", leave_but4)


    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 12, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])
    

    
    
    but1=ttk.Button(text="REGISTER", style="TButton", command = preregister)
    but1.place(x=940,y=370+200)
    but2=ttk.Button(text="⌂ HOME", style="TButton", command = go_home)
    but2.place(x=940,y=420+200)

   

    
    main_screen.mainloop()
    

# Designing window for login 

def login():
    global login_screen
    #login_screen = Tk()#Toplevel(main_screen)
    #main_screen.destroy()
    main_screen.title("Login")
    #login_screen.geometry("1536x800")




    

    

    # Create a photoimage object of the image in the path
    image1 = Image.open("Extras/img/login/8f.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=-9, y=-4)
    #login_screen.mainloop()
    

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    login_font=('Bahnschrift',15)

    # label2=Label(main_screen, text="Username * ")
    # label2.place(x=300, y=100)
    username_login_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font ,textvariable=username_verify)
    username_login_entry.place(x=90, y=250,height=30,width=250)
    username_login_entry.insert(0,'Enter Username:')
        
    username_login_entry.bind("<Button-1>", click_but1)
    username_login_entry.bind("<Leave>", leave_but1)
        
    
    password_login_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=password_verify, )
    password_login_entry.place(x=90,y=310,height=30,width=250)
    password_login_entry.insert(0,'Enter Password:')

    password_login_entry.bind("<Button-1>", click_but2)
    password_login_entry.bind("<Leave>", leave_but2)


    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 12, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])
    

    
    
    but1=ttk.Button(text="LOGIN", style="TButton", command = login_verify)
    but1.place(x=140,y=370)
    but2=ttk.Button(text="⌂ HOME", style="TButton", command = go_home)
    but2.place(x=140,y=420)

    
    main_screen.mainloop()

# call function when we click on entry box
def click_but1(*args):
    username_login_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but1(*args):
    # username_login_entry.delete(0, 'end')
    # username_login_entry.insert(0, 'Enter Username:',)
    xxx=10

def click_but2(*args):
    password_login_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but2(*args):
    # password_login_entry.delete(0, 'end')
    # password_login_entry.insert(0, 'Enter Password:',)
    xxx=10





  
# call function when we leave entry box
def leave_but3(*args):
    #username_entry.delete(0, 'end')
    #username_entry.insert(0, 'Enter Username:',)
    xxx=10

def click_but4(*args):
    password_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but4(*args):
    #password_entry.delete(0, 'end')
    #password_entry.insert(0, 'Enter Password:',)
    xxx=10



    
# Implementing event on register button
def preregister():
    username_info = username.get()
    password_info = password.get()
    global rix
    r = csv.reader(open(filename,newline='')) # Here your csv file
    lines = list(r)

    lnf=0
    

    col_len=len(lines)

    for ele in range(col_len):
        if username_info==lines[ele][1]:
            lnf=0
            rix=Label(main_screen, text="Username exists!", fg="red", font=("calibri", 13))
            rix.place(x=925+13,y=620+50)
            break
        else:
            lnf=1
    
    if lnf==1:
        register_user()
    



def register_user():

    username_info = username.get()
    password_info = password.get()
    global tix

      
    
    

    
    
    fields=['nmk',username_info,password_info,'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA']

    with open(filename, 'a',newline='') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
                        
        # writing the fields
        csvwriter.writerow(fields)




    username_entry.delete(0, END)
    password_entry.delete(0, END)

                    

    tix=Label(main_screen, text="Registration Success!", fg="green", font=("calibri", 13))
    tix.place(x=925,y=620+50)

    gk=1

    
    

    
    

    
    #sleeper()
    
    

def click_but3(*args):
    username_entry.delete(0, 'end')
    tix.destroy()
    rix.destroy()





def sleeper():
    
    sleep(4)
    tix.destroy()
    
# Implementing event on login button 

def nmkall():
    r = csv.reader(open(filename,newline='')) # Here your csv file
    lines = list(r)

    
    col_len=len(lines)
    #print (lines)


    for elen in range(col_len):
        #print(elen)
        lines[elen][0]='nmk'
    #print (lines)
    
            
        
    
    
    writer = csv.writer(open(filename, 'w', newline=''))
    writer.writerows(lines)
    


def login_verify():
    username1 = username_verify.get()
    global Usernaam
    Usernaam=username1
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    #nmkall()

    f=open(filename,newline='')

    r = csv.reader(f) # Here your csv file
    lines = list(r)
    f.close()

    unf=0
    pnf=0
    go=0

    col_len=len(lines)
    #print (lines)

    for elen in range(col_len):
        #print(elen)
        lines[elen][0]='nmk'
    #print (lines)

       
    for ele in range(col_len):
        if username1==lines[ele][1]:
            unf=3
            if password1==lines[ele][2]:
                pnf=3
                
                lines[ele][0]='mk'
                #login_sucess()
                goat=1
            else:
                if pnf!=3:
                    pnf=1
        else:
            if unf!=3:
                unf=1

    if unf==1:
        user_not_found()
    if pnf==1:
        password_not_recognised()

    f=open(filename, 'w', newline='')

    writer = csv.writer(f)
    writer.writerows(lines)
    f.close()
    # print (lines)
    # print('login verify')

    if goat==1:
        login_sucess()
        



    

    
# Designing popup for login success



def goto_lev1():
    main_screen.destroy()
    os.system('python ../Project_Momentum/Extras/maingame_lev1.py')

def goto_lev2():
    main_screen.destroy()
    os.system('python ../Project_Momentum/Extras/maingame_lev2.py')

def goto_lev3():
    main_screen.destroy()
    os.system('python ../Project_Momentum/Extras/maingame_lev3.py')

def goto_lev4():
    main_screen.destroy()
    os.system('python ../Project_Momentum/Extras/maingame_lev4.py')


def login_sucess():

    #main_screen.destroy()
    username2 = username_verify.get()
    
    global main_screen
    #main_screen=Tk()
    main_screen.geometry("1536x800")
    main_screen.title("Let's Go")
    image1 = Image.open("Extras/img/login/6fs.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

    label1.place(x=-3, y=-1.5)

    high=Label(main_screen, text="HIGHSCORE", fg="white",bg="black", font=("century gothic", 30, 'bold'),borderwidth=4)
    high.place(x=620,y=20)

    #level details
    levx=320
    levy=300
    dy=120
    bwb=5

    lev1=Label(main_screen, text="Level 1 :", fg="white",bg="black", font=("century gothic", 20),borderwidth=bwb)
    lev1.place(x=levx,y=levy+dy*0)

    lev2=Label(main_screen, text="Level 2 :", fg="white",bg="black", font=("century gothic", 20),borderwidth=bwb)
    lev2.place(x=levx,y=levy+dy*1)

    lev3=Label(main_screen, text="Level 3 :", fg="white",bg="black", font=("century gothic", 20),borderwidth=bwb)
    lev3.place(x=levx,y=levy+dy*2)

    lev4=Label(main_screen, text="Level 4 :", fg="white",bg="black", font=("century gothic", 20),borderwidth=bwb)
    lev4.place(x=levx,y=levy+dy*3)


    #score details
    skx=levx+415
    skf=20
    bwb=6
    

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


    
	
    f=open(filename, 'r',newline='')
    r_list = csv.reader(f) # Here your csv file
    lines = list(r_list)
    f.close()
    #print(lines)
    col_len_loc=len(lines)
    # print('login_success')
    # print(Usernaam)

    chk_loc=0

    for ele in range(col_len_loc):
        #print (lines_loc[ele_loc][1]+'\n')
        if lines[ele][1]==Usernaam:
            skmin_1=lines[ele][3]
            sksec_1=lines[ele][4]
            skms_1=lines[ele][5]
            skmin_2=lines[ele][6]
            sksec_2=lines[ele][7]
            skms_2=lines[ele][8]
            skmin_3=lines[ele][9]
            sksec_3=lines[ele][10]
            skms_3=lines[ele][11]
            skmin_4=lines[ele][12]
            sksec_4=lines[ele][13]
            skms_4=lines[ele][14]
            
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
        sk_1=Label(main_screen, text=skmin_1, fg="red",bg="black", font=("banschrift", skf,'bold' ),borderwidth=bwb)
        sk_1.place(x=skx,y=levy+dy*0)
    
    else:
        #score_1+=' s'
        sk_1=Label(main_screen, text=score_1, fg="light green",bg="black", font=("banschrift", skf,'bold','italic' ),borderwidth=5)
        sk_1.place(x=skx,y=levy+dy*0)

    if skmin_2=='NA':
        sk_2=Label(main_screen, text=skmin_2, fg="red",bg="black", font=("banschrift", skf,'bold' ),borderwidth=bwb)
        sk_2.place(x=skx,y=levy+dy*1)
    else:
        #score_2+=' s'
        sk_2=Label(main_screen, text=score_2, fg="light green",bg="black", font=("banschrift", skf,'bold' ,'italic'),borderwidth=bwb)
        sk_2.place(x=skx,y=levy+dy*1)

    if skmin_3=='NA':
        sk_3=Label(main_screen, text=skmin_3, fg="red",bg="black", font=("banschrift", skf,'bold' ),borderwidth=bwb)
        sk_3.place(x=skx,y=levy+dy*2)
    else:
        #score_3+=' s'
        sk_3=Label(main_screen, text=score_3, fg="light green",bg="black", font=("banschrift", skf,'bold' ,'italic'),borderwidth=bwb)
        sk_3.place(x=skx,y=levy+dy*2)

    if skmin_4=='NA':
        sk_4=Label(main_screen, text=skmin_4, fg="red",bg="black", font=("banschrift", skf,'bold' ),borderwidth=bwb)
        sk_4.place(x=skx,y=levy+dy*3)
    else:
        #score_4+=' s'
        sk_4=Label(main_screen, text=score_4, fg="light green",bg="black", font=("banschrift", skf,'bold' ,'italic'),borderwidth=bwb)
        sk_4.place(x=skx,y=levy+dy*3)

    
    #Button Dealings

    butwid=3
    butx=levx+800
    butfont=24

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 15,),borderwidth = '2')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])


    but1=ttk.Button(text="Play", style="TButton", command = goto_lev1)
    but1.place(x=butx,y=levy+dy*0)

    if skmin_1!='NA':
        but2=ttk.Button(text="Play", style="TButton", command = goto_lev2)
        but2.place(x=butx,y=levy+dy*1)

    if skmin_2!='NA':
        but3=ttk.Button(text="Play", style="TButton", command = goto_lev3)
        but3.place(x=butx,y=levy+dy*2)
    
    if skmin_3!='NA':
        but4=ttk.Button(text="Play", style="TButton", command = goto_lev4)
        but4.place(x=butx,y=levy+dy*3)


    
    
    

    main_screen.mainloop()


    # global login_success_screen
    # login_success_screen = Toplevel(main_screen)
    # login_success_screen.title("Success")
    # login_success_screen.geometry("150x100")
    # Label(login_success_screen, text="Login Success").pack()
    # Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
###################################################################################




def delete_login_success():

    #login_success_screen.destroy()
    main_screen.destroy()
    
    os.system('python ../Project_Momentum/Extras/maingame_lev1.py')
    #execfile('Extras/maingame_lev1.py')
    
    



######################################################################################
def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def go_home():
    main_screen.destroy()
    main_account_screen()

# Designing Main(first) window


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1536x800")
    main_screen.title("Account Login")
    
    bgrnd = PhotoImage(file="Extras/img/login/1bg.png")

    #creating canvas
    canva = Canvas(main_screen, width=1536, height=800)
    
    canva.pack(fill="both", expand=True)

    canva.create_image(-9,-4,image=bgrnd,anchor="nw")

    
    

    #STyle Buttons
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 20, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])

    # Create Buttons
   
   # Label(text="").pack()
    but1=ttk.Button(text="LOGIN", style="TButton", command = login)
    but2=ttk.Button(text="REGISTER", style="TButton", command = register)
    
    


    # Display Buttons
    button1_canvas = canva.create_window( 570, 150,anchor = "nw", window = but1)
    button2_canvas = canva.create_window( 870, 150,anchor = "nw", window = but2)
    
    
    main_screen.mainloop()

main_account_screen()
