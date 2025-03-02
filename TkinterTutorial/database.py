from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

root.geometry("400x600")

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

def saverecord():
    # Create a databse or connct to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    # cursor is little thing that goes with query and fetchs data for use
    c = conn.cursor()
    
    record_id = update_box.get()
    c.execute("""UPDATE addressess SET 
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid
              """,
              {
                  'first' : f_name_editor.get(),
                  'last' : l_name_editor.get(),
                  'address' : address_editor.get(),
                  'city' : city_editor.get(),
                  'state' : state_editor.get(),
                  'zipcode' : zipcode_editor.get(),
                  
                  'oid' : record_id
              }
              )
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    
    editor.destroy()
    

# Create a fucntion to edit/update the record
def update():
    global editor
    editor = Tk()
    #Title for the window
    editor.title("Update A Record")

    #Image icon for tool icon
    editor.iconbitmap("TkinterTutorial\\christmas-tree.ico")

    editor.geometry("400x300")
    
    # Create a databse or connct to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    # cursor is little thing that goes with query and fetchs data for use
    c = conn.cursor()
    
    record_id = update_box.get()
    # Query the database (sqlite3 automatically create the primary key for the databse table so if we explicitly select it, it will be shown [oid])
    c.execute("SELECT * FROM addressess WHERE oid = " + record_id)
    # c.fetchmany(number)
    # c.fetchone()
    records = c.fetchall()
    # print(records)

    # Create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Creaate Text Box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0)) #This will just add padding to the top only and not below it.

    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)
    
    # for loop through the records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    # Create a Update Button
    updateBtn = Button(editor, text="Save Record", command=saverecord)
    updateBtn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=137)
    
    #creating a quit button
    buttonQuit = Button(editor, text="Exit Program", command=editor.quit)
    buttonQuit.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
    return

# Create a function to delete the record
def delete():
    # Create a databse or connct to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    # cursor is little thing that goes with query and fetchs data for use
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addressess WHERE oid= " + delete_box.get())

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()    
    
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
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + '\n'
    
    queryLabel = Label(root, text=print_records)
    queryLabel.grid(row=14, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

update_box = Entry(root, width=30)
update_box.grid(row=11, column=1)

# Creaate Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0)) #This will just add padding to the top only and not below it.

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

delete_label = Label(root, text="Delete ID")
delete_label.grid(row=9, column=0)

update_label = Label(root, text="Select ID")
update_label.grid(row=11, column=0)

# Create Submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=110)

# Create a Query Button
queryBtn = Button(root, text="Show Records", command=query)
queryBtn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Delete Button
deleteBtn = Button(root, text="Delete Record", command=delete)
deleteBtn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Update Button
updateBtn = Button(root, text="Update Record", command=update)
updateBtn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#creating loop to continuosly execute the app
root.mainloop()
