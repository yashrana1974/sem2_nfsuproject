from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\christmas-tree.ico")

def popupinfo():
    messagebox.showinfo("This is my Popup!", "Hello World")
    # The first "Is the titile of window" and second is "Message in the box"

def popupwarning():
    messagebox.showwarning("This is my Popup!", "Hello World!")
    
def popuperror():
    messagebox.showerror("This is my Popup!", "Hello World!")
    
def popupaskquestion():
    messagebox.askquestion("This is my Popup!", "Hello World!")    
       
def popupokcancel():
    messagebox.askokcancel("This is my Popup!", "Hello World!")    
    
def popupaskyesno():
    # Taking the value from the alert box and depending on the input performing functions.
    response = messagebox.askyesno("This is my Popup!", "Hello World!")  
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Clicked Yes!").pack()
    else:
        Label(root, text="Clicked No!").pack()
        
def popupaskretrycancel():
    messagebox.askretrycancel("This is my Popup!", "Hello World!")    
       
def popupaskyesnocancel():
    messagebox.askyesnocancel("This is my Popup!", "Hello World!")    
   
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel, askretrycancel

Button(root, text="Popupinfo", command=popupinfo).pack()
Button(root, text="Popupwarning", command=popupwarning).pack()
Button(root, text="Popuperror", command=popuperror).pack()
Button(root, text="Popupaskquestion", command=popupaskquestion).pack()
Button(root, text="Popupokcancel", command=popupokcancel).pack()
Button(root, text="Popupaskyesno", command=popupaskyesno).pack()
Button(root, text="Popupaskretrycancel", command=popupaskretrycancel).pack()
Button(root, text="Popupaskyesnocancel", command=popupaskyesnocancel).pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
