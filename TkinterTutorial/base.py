from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

def open():
    global myImage
    top = Toplevel()
    top.title("My Second Window")
    top.iconbitmap("TkinterTutorial\\christmas-tree.ico")
    label = Label(top, text="Hello World").pack()
    myImage = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo1_500.jpg"))
    label2 = Label(top, image=myImage).pack() 
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
