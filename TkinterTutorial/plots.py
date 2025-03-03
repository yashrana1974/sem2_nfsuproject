from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
    plt.polar(house_prices)
    plt.show()
    
myButton = Button(root, text="Graph It!", command=graph)
myButton.pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
