from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# utility functions

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClearClick():
    e.delete(0, END)

def buttonAdditionClick():
    firstNumber = e.get()
    global fNum
    global math 
    math = "addition"
    fNum = int(firstNumber)
    e.delete(0, END)

def buttonEqualClick():
    secondNumber = e.get()
    e.delete(0, END)

    #e.insert(0, fNum + int(secondNumber))
    if math == "addition":
        e.insert(0, fNum + int(secondNumber))
    elif math == "subtraction":
        e.insert(0, fNum - int(secondNumber))
    elif math == "multiplication":
        e.insert(0, fNum * int(secondNumber))
    else:
        e.insert(0, fNum / int(secondNumber))

def buttonSubtractionClick():
    firstNumber = e.get()
    global fNum
    global math 
    math = "subtraction"
    fNum = int(firstNumber)
    e.delete(0, END)

def buttonMultiplicationClick():
    firstNumber = e.get()
    global fNum
    global math 
    math = "multiplication"
    fNum = int(firstNumber)
    e.delete(0, END)

def buttonDivisionClick():
    firstNumber = e.get()
    global fNum
    global math 
    math = "division"
    fNum = int(firstNumber)
    e.delete(0, END)

# Define/Create [0,9]-numbers buttons
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: buttonClick(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: buttonClick(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: buttonClick(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: buttonClick(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: buttonClick(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: buttonClick(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: buttonClick(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: buttonClick(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: buttonClick(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: buttonClick(0))

# Define/Create + , = and clear buttons
button_addition = Button(root, text = "+", padx = 39, pady = 20, command = buttonAdditionClick)
button_equal = Button(root, text = "=", padx = 91, pady = 20, command = buttonEqualClick)
button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = buttonClearClick)

# Define/Create - , * and / buttons
button_subtraction = Button(root, text = "-", padx = 41, pady = 20, command = buttonSubtractionClick)
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = buttonMultiplicationClick)
button_division = Button(root, text = "/", padx = 41, pady = 20, command = buttonDivisionClick)

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
button_addition.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtraction.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_division.grid(row=6, column=2)

root.mainloop()