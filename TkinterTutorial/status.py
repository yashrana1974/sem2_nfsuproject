from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

def forward(image_number):
    global myLabel
    global buttonForward
    global buttonBack
    
    myLabel.grid_forget()
    myLabel = Label(image=imageList[image_number-1])
    buttonForward = Button(root, text=">>", command=lambda: forward(image_number+1))
    buttonBack = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 6:
        buttonForward = Button(root, text=">>", state=DISABLED)
    
    #Adding the status bar (Image 1 of 6)    
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonBack.grid(row=1, column=0)
    
def back(image_number):
    global myLabel
    global buttonForward
    global buttonBack
    
    myLabel.grid_forget()
    myLabel = Label(image=imageList[image_number-1])
    buttonForward = Button(root, text=">>", command=lambda: forward(image_number+1))
    buttonBack = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        buttonBack = Button(root, text="<<", state=DISABLED)
        
    #Adding the status bar (Image 1 of 6)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonBack.grid(row=1, column=0)
    

#Tkinter doesn't supports .jpg, etc. We need to add lib Pillow (PIL) to support those images Import it in top
myImage1 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo1_500.jpg"))
myImage2 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo2_500.jpg"))
myImage3 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo3_500.jpg"))
myImage4 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo4_500.jpg"))
myImage5 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo5_500.jpg"))
myImage6 = ImageTk.PhotoImage(Image.open("TkinterTutorial\\Images\\photo6_500.jpg"))

imageList = [myImage1, myImage2, myImage3, myImage4,myImage5, myImage6]

status = Label(root, text="Image 1 of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myImage1)
myLabel.grid(row=0, column=0, columnspan=3)

buttonForward = Button(root, text=">>", command=lambda: forward(2))
buttonExit = Button(root, text="Exit", command=root.quit)
buttonBack = Button(root, text="<<", command=lambda: back(), state=DISABLED)

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# #creating a quit button
# buttonQuit = Button(root, text="Exit Program", command=root.quit)
# buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
