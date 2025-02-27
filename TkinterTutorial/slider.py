from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

# Sets the size of the window to 400 by 400
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
# Don't use .pack() with directly with vertical (above) it or else it gets worst while compiling/interpreating
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

# myLabel = Label(root, horizontal.get()).pack()

def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    
myButton = Button(root, text="Click Me!", command=slide).pack()


#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
