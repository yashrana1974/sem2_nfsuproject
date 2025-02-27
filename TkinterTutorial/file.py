from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

# The filedailog box returns the path of the image and we use that path to open the file (can be done with any file)

def open():
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\ranay\\OneDrive\\Documents\\GitHub\\sem2_nfsuproject", title="Select A File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    myLabel = Label(root, text=root.filename).pack()
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    imageLabel = Label(root, image=myImage).pack()

myButton = Button(root, text="Open File", command=open).pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
