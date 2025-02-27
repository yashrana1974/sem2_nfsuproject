from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=60, command=myClick, fg="blue", bg="red")
myButton1 = Button(root, text="Click Me!", state=DISABLED)
myButton.pack()
myButton1.pack()

#creating loop to continuosly execute the app
root.mainloop()
