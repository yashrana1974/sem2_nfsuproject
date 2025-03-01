from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

# Databases

# Create a databse or connct to one
conn = sqlite3.connect('address_book.db')

# Create cursor
# cursor is little thing that goes with query and fetchs data for use
c = conn.cursor()

# datatype in sqllite3 Text, integer, decimal, null and blob
# Create table
c.execute("""CREATE TABLE addressess (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
          
          """)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
