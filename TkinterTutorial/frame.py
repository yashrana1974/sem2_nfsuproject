from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\christmas-tree.ico")

#Pack and Grid cannot be used in the same code, either of them can be used. But with the use of frame we can use pack or grid in it and can use grid or pack outside the frame, but the frame should be pack or either grid like the rest of the labels.

#Frames are used to create section in a window and organize them for better visual approach
Frame = LabelFrame(root, text="This is my frame........", padx=50, pady=50) #Inner padding of the label
Frame.pack(padx=100, pady=100) #Outer body of the label more like the window padding for the frame

b = Button(Frame, text="Don't click here")
b2 = Button(Frame, text="Click here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)



#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
