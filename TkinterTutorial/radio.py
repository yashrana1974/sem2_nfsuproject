from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\christmas-tree.ico")

#Tkinter varible are bit different form the python varibale

#Need to create integer because the value is, they can also be used with different classes. Like r.get()
r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack() 

Radiobutton(root, text="Option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command= lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack() 

myButton = Button(root, text="Click Me!", command= lambda: clicked(r.get()))
myButton.pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
