from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=12)
e.pack()
e.get()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get() 
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=20, pady=20, command=myClick, fg="blue", bg="red")
myButton1 = Button(root, text="Click Me!", state=DISABLED)
myButton.pack()
myButton1.pack()

#creating loop to continuosly execute the app
root.mainloop()
