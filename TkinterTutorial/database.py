from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

root.geometry("400x400")

# Databases

# Create a databse or connct to one
conn = sqlite3.connect('address_book.db')

# Create cursor
# cursor is little thing that goes with query and fetchs data for use
c = conn.cursor()

# datatype in sqllite3 Text, integer, decimal, null and blob
# Create table
# c.execute("""CREATE TABLE addressess (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
          
#           """)

def submit():
    # Create a databse or connct to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    # cursor is little thing that goes with query and fetchs data for use
    c = conn.cursor()
    
    # Insert Into Table
    c.execute("INSERT INTO addressess VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
              {
                  'f_name': f_name.get(),
                  'l_name' : l_name.get(),
                  'address' : address.get(),
                  'city' : city.get(),
                  'state' : state.get(),
                  'zipcode' : zipcode.get()
              })
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    
    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
# Query function 
def query():
    # Create a databse or connct to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    # cursor is little thing that goes with query and fetchs data for use
    c = conn.cursor()
    
    # Query the database (sqlite3 automatically create the primary key for the databse table so if we explicitly select it, it will be shown [oid])
    c.execute("SELECT *, oid FROM addressess")
    # c.fetchmany(number)
    # c.fetchone()
    records = c.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + '\n'
    
    queryLabel = Label(root, text=print_records)
    queryLabel.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Creaate Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# Create Submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
queryBtn = Button(root, text="Show Records", command=query)
queryBtn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#creating loop to continuosly execute the app
root.mainloop()
