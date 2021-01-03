from tkinter import * 

root = Tk()
root.title("Who is the smarter brother?")
root.geometry("400x200")
root.configure(bg = "#cedbdb")



label_1 = Label(root, text = "Who is smarter Daniel or Elyas:", bg = "#cedbdb" )
label_1.place(x = 120, y = 25)


stringvar = StringVar()
displaylabel = Label(root, textvariable = stringvar)
displaylabel.pack()

#functions
def eod():
    stringvar.set("You are wrong!") 
    root.configure(bg = "#f23838")   


def doe():
    stringvar.set("You are correct!")
    root.configure(bg = "#4af74d")   

#buttons
button_daniel = Button(root, text="Daniel", width=7, height=2, command = eod, fg = "#c19df2", bg = "#756f6f")
button_daniel.place(x = 126, y = 105)

button_elyas = Button(root, text="Elyas", width=7, height=2, command = doe, fg = "#c19df2", bg = "#756f6f")
button_elyas.place(x = 220, y = 105)

mainloop()