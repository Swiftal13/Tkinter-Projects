#password generator

#imports
from tkinter import * 
from datetime import date 
import tkinter.font as font
import tkinter.messagebox as box
import string
import random
import time

root = Tk()
date = date.today()
root.title(f"Password generator!                                             {date}")
root.geometry("470x180")
root.configure(bg = "#bcc3c4")    

#all letters and numbers
char = string.ascii_letters + string.digits

#label widgets and placement  
label_1 = Label(root, text = "Pick: Easy - Medium - Hard", bg = "#756f6f",fg = "white", borderwidth=2, relief="ridge")
label_1.pack(side = TOP)

stringvar_generating = StringVar()
label_generating = Label(root, textvariable = stringvar_generating, bg = "#bcc3c4")
label_generating.pack()

stringvar_password = StringVar()
label_password = Label(root, textvariable=stringvar_password, bg = "#bcc3c4")
label_password.pack(side=BOTTOM)



#functions
def easy():
    stringvar_generating.set("Password generating...")
    root.after(1300)
    sample1 = random.sample(char,6)
    def b(lost):
            lost = lost.replace("[", "")
            lost = lost.replace("]", "")
            lost = lost.replace("'", "")
            lost = lost.replace(",", "")
            return lost
    stringvar_password.set(f"Password: {b(str(sample1))}")
    
    
def medium():
    stringvar_generating.set("Password generating...")
    root.after(1300)
    sample1 = random.sample(char,10)
    def b(lost):
            lost = lost.replace("[", "")
            lost = lost.replace("]", "")
            lost = lost.replace("'", "")
            lost = lost.replace(",", "")
            return lost
    stringvar_password.set(f"Password: {b(str(sample1))}")
        
def hard():
    stringvar_generating.set("Password generating...")
    root.after(1300)
    sample1 = random.sample(char,14)
    def b(lost):
            lost = lost.replace("[", "")
            lost = lost.replace("]", "")
            lost = lost.replace("'", "")
            lost = lost.replace(",", "")
            return lost
    stringvar_password.set(f"Password: {b(str(sample1))}")
    
def custom():
    root2 = Tk()
    root2.geometry("250x90")
    root2.title("digit of char: ")
    root2.configure(bg = "#bcc3c4")
    entry = Entry(root2)
    entry.pack(side = TOP)
    def b(lost):
            lost = lost.replace("[", "")
            lost = lost.replace("]", "")
            lost = lost.replace("'", "")
            lost = lost.replace(",", "")
            return lost
    stringvar_custompassword = StringVar(root2)
    label_custom_password = Label(root2, textvariable = stringvar_custompassword, bg = "#bcc3c4")
    def emilian():
        leans = int(entry.get())
        sample1 = random.sample(char, leans)
        root2.after(1300)
        stringvar_custompassword.set(f"Password: {b(str(sample1))}")
    label_custom_password.pack(side = BOTTOM)
    button_cc = Button(root2, text = "Enter", command = emilian, fg = "white", bg = "#756f6f")
    button_cc.place(x = 109, y = 20)
    
   
#buttons
button_easy = Button(root, text = "Easy", width=6, height=1, command = easy, fg = "#8fff57", bg = "#756f6f")
button_easy.place(x = 80, y = 60)
    
button_medium = Button(root, text = "Medium", width=6, height=1, command = medium, fg = "#ff9757", bg = "#756f6f")
button_medium.place(x = 168, y = 60)
    
button_hard = Button(root, text = "Hard", width = 6, height = 1, command = hard, fg = "#ff3d3d", bg = "#756f6f")
button_hard.place(x = 255, y = 60)

button_custom = Button(root, text = "Custom", width = 6, height = 1, command = custom, fg = "white", bg = "#756f6f")
button_custom.place(x = 340, y = 60)
    
mainloop()


        
        
        
        
        
        
        
        
        

    
    

    
    
    

