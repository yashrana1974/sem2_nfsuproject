from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

#Root window size
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var  = IntVar()
#var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you", variable=var) #,onvalue = "Ön", offvalue = "Off"
c.deselect() #To get not selected by default by the check box
c.pack()

myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
