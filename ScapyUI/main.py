from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("ScapyUI")

#Image icon for tool icon
root.iconbitmap("ScapyUI\\res\\logo.ico")

# Geometry of the window
root.geometry("400x500")


myMenu = Menu(root)
root.config(menu=myMenu)

# Create a menu time
navigate = Menu(myMenu)
myMenu.add_cascade(label="Navigate", menu=navigate)
navigate.add_command(label="New..")
navigate.add_command(label="Exit", command=root.quit)
# naivgate.add_separator()


#creating loop to continuosly execute the app
root.mainloop()
