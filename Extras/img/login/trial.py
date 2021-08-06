from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
  
# Create Tkinter Object
root = Tk()
  
# Set geometry
root.geometry('400x400')
login_font=('Bahnschrift',)
  
# call function when we click on entry box
def click(*args):
    playlist_url.delete(0, 'end')
  
# call function when we leave entry box
def leave(*args):
    playlist_url.delete(0, 'end')
    playlist_url.insert(0, 'Enter Text:- ',font=login_font,fg='dark grey')
    root.focus()
  
  
# Add Entry Box
playlist_url = Entry(root, width=60)
  
# Add text in Entry box
playlist_url.insert(0, 'Enter Text:- ')
playlist_url.pack(pady=10)
  
# Use bind method
playlist_url.bind("<Button-1>", click)
playlist_url.bind("<Leave>", leave)
  
# Execute Tkinter
root.mainloop()