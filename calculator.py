#calculator

#imports
from tkinter import * 
from tkinter import Entry

#window
root = Tk()
root.geometry("304x370")
root.title("Calculator")
root.configure(bg = "#5c5d5e")

#entry
entry = Entry(root,width = 30,font = 50)
entry.config(disabledbackground ="white",state="normal")
entry.place(x = 12, y = 10, height = 45)

#text show
Stringvar = StringVar()

#functions

def one():
    entry.insert(END,"1")

def two():
    entry.insert(END,"2")

def three():
    entry.insert(END,"3")

def four():
    entry.insert(END,"4")

def five():
    entry.insert(END,"5")

def six():
    entry.insert(END,"6")

def seven():
    entry.insert(END,"7")

def eight():
    entry.insert(END,"8")

def nine():
    entry.insert(END,"9")

def zero():
    entry.insert(END,"0")

def delete():
    entry.delete(0)

def equal():
    entryget = entry.get()
    evaluate = eval(entryget)
    entry.delete(0, "end")
    entry.insert(0, int(evaluate))

def plus():
    entry.insert(END,"+")

def minus():
    entry.insert(END,"-")
    
def times():
    entry.insert(END,"*")
    
def divide():
    entry.insert(END,"/")






#buttons
button_1 = Button(root, text = "1", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = one, bg = "#403e3e", fg = "WHITE")
button_1.place(x = 12, y = 70)

button_2 = Button(root, text = "2", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = two, bg = "#403e3e", fg = "WHITE")
button_2.place(x = 82, y = 70)

button_3 = Button(root, text = "3", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = three, bg = "#403e3e", fg = "WHITE")
button_3.place(x = 152, y = 70)

button_4 = Button(root, text = "4", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = four, bg = "#403e3e", fg = "WHITE")
button_4.place(x = 12, y = 144)

button_5 = Button(root, text = "5", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = five, bg = "#403e3e", fg = "WHITE")
button_5.place(x = 82, y = 144)

button_6 = Button(root, text = "6", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = six, bg = "#403e3e", fg = "WHITE")
button_6.place(x = 152, y = 144)

button_7 = Button(root, text = "7", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = seven, bg = "#403e3e", fg = "WHITE")
button_7.place(x = 12, y = 218)

button_8 = Button(root, text = "8", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = eight, bg = "#403e3e", fg = "WHITE")
button_8.place(x = 82, y = 218)

button_9 = Button(root, text = "9", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = nine, bg = "#403e3e", fg = "WHITE")
button_9.place(x = 152, y = 218)

button_0 = Button(root, text = "0", width = 8, height = 4, borderwidth = 1, relief = "ridge", command = zero, bg = "#403e3e", fg = "WHITE")
button_0.place(x = 12, y = 292)

button_delete = Button(root, text = "Delete", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#ffb536", fg = "WHITE", command = delete)
button_delete.place(x = 82, y = 292)

button_equal = Button(root, text = "=", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#18181a", fg = "WHITE", command = equal)
button_equal.place(x = 152, y = 292)

button_plus = Button(root, text = "+", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#ffb536", fg = "WHITE", command = plus)
button_plus.place(x = 223, y = 70)

button_minus = Button(root, text = "-", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#ffb536", fg = "WHITE", command = minus)
button_minus.place(x = 223, y = 144)

button_times = Button(root, text = "x", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#ffb536", fg = "WHITE", command = times)
button_times.place(x = 223, y = 218)

button_divide = Button(root, text = "/", width = 8, height = 4, borderwidth = 1, relief = "ridge", bg = "#ffb536", fg = "WHITE", command = divide)
button_divide.place(x = 223, y = 292)

mainloop()


    
