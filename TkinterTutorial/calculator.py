from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    return

def buttonEqual():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))
    return

button1 = Button(root, text="1", padx=40, pady=40, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=40, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=40, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=40, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=40, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=40, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=40, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=40, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=40, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=40, command=lambda: buttonClick(0))
buttonadd = Button(root, text="+", padx=40, pady=40, command=buttonAdd)
buttonequal = Button(root, text="=", padx=40, pady=40, command=buttonEqual)
buttonclear = Button(root, text="Clear", padx=127, pady=30, command=buttonClear)

# Put the buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=4, column=1)
buttonequal.grid(row=4, column=2)

buttonclear.grid(row=5, column=0, columnspan=3)
#creating loop to continuosly execute the app
root.mainloop()
