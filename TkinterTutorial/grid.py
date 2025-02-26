from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is Yash Rana")
#create and show in one step due to object oriented programming in python
myLabel3 = Label(root, text="I study").grid(row=2,column=2)

#shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

#creating loop to continuosly execute the app
root.mainloop()
