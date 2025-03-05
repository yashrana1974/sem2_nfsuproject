from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
# root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

root.geometry("400x400")

myMenu = Menu(root)
root.config(menu=myMenu)

# Click command
def our_command():
    pass

# Create a menu time
file_menu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New..", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Edit", command=our_command)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=root.quit)

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
