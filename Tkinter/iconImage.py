from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\christmas-tree.ico")

#Tkinter doesn't supports .jpg, etc. We need to add lib Pillow (PIL) to support those images Import it in top
myImage = ImageTk.PhotoImage(Image.open("TkinterTutorial\photo.jpg"))
myLabel = Label(image=myImage)
myLabel.pack()


#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
