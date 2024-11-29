import numpy as np 
import math
import math3d
import tkinter
from tkinter import *
from calculator_data import *



#SUM operation
def sum(a, b):
    result = a+b
    return result

#SUB operation
def sub(a, b):
    result = a-b
    return result

#MUL operation
def mul(a, b):
    result = a*b
    return result

#DIV operation
def div(a, b):
    result = a/b
    return result

#Exponential operation
def pow(a,b):
    result = math.pow(a,b)
    return result

#Square root operation
def sqr(a):
    result = math.sqrt(a)
    return result

#Nth-root operation 
def sqr_n(a,b):
    result = math.pow(a,(1/b))
    return result

def read_values(value, var):
    current = var.get()  # Get the current value in the display
    var.set(current + str(value))  # Append the clicked button's value to the display

def clear_display(var):
    var.set("")

def operation(var):

    try:
        current = var.get()  # Get the current expression
        print(current)

        result = eval(current)  # Safely evaluate the expression
        var.set(str(result))  # Display the result
    except Exception as e:
        var.set("Error")  # Handle any errors in the expression


def main():

    top = tkinter.Tk()
    top.geometry("368x528")
    top.title("Calculator")

    # Variable to store the current text in the display
    var = tkinter.StringVar()
    label = tkinter.Label(top, textvariable=var, justify="right", anchor="e", width=31, height=6, bg="light gray", font=("Arial", 15))
    label.place(x=10, y=10)

    for text, value, x, y in button_normal:

        if value == "=":
             b = Button(top, text = text, command=lambda v=value: operation(var), width=6, height=4, bg="gray", fg="black")

        elif value in ['+', '-', '*', '/']:
            b = Button(top, text = text, command=lambda v=value: read_values(v, var), width=6, height=4, bg="gray", fg="black")

        elif value == "0":
            b = Button(top, text = text, command=lambda v=value: read_values(v, var), width=20, height=4, bg="gray", fg="black")

        elif value in ["Ans", "Scientific", "Graphical"]:
            b = Button(top, text = text, command = sqr(1), width=10, height=4, bg="gray", fg="black")
        
        elif value == "C":
            b = Button(top, text = text, command=lambda: clear_display(var), width=10, height=4, bg="gray", fg="black")

        else:
            b = Button(top, text = text,  command=lambda v=value: read_values(v, var), width=9, height=4, bg="gray", fg="black")

        b.place(x=x, y=y)

    expression = input()
    var.set(expression)
    
    top.mainloop()    


if __name__ == "__main__":
    main()