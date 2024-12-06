import tkinter
import numpy as np

sqrt_symbol = "\u221A"

# Button data: text, value, x, y position
button_normal = [
    ("ⁿ√x", "ⁿ√x", 100, 160),  # nth root button
    ("√x", "sqrt", 170, 160),   # square root button
    ("x²", "x²", 240, 160),     # square button
    ("1", "1", 100, 230),
    ("2", "2", 170, 230),
    ("3", "3", 240, 230),
    ("4", "4", 100, 300),
    ("5", "5", 170, 300),
    ("6", "6", 240, 300),
    ("7", "7", 100, 370),
    ("8", "8", 170, 370),
    ("9", "9", 240, 370),
    ("0", "0", 100, 440),
    (".", ".", 240, 440),
    ("/", "/", 310, 160),
    ("*", "*", 310, 230),
    ("-", "-", 310, 300),
    ("+", "+", 310, 370),
    ("=", "=", 310, 440),
    ("Ans", "Ans", 10, 370),
    ("C", "C", 10, 440),
    ("Scientific", "Scientific", 10, 160),
    ("Graphical", "Graphical", 10, 230),
]




""" 
# Button for n-th root
B_nr = Button(top, text = f"ⁿ{sqrt_symbol}x", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B_nr.place(x=100,y=160)

# Button for square root
B_sqr = Button(top, text = f"{sqrt_symbol}x", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B_sqr.place(x=170,y=160)

# Button for exponential
B_pow = Button(top, text = "x²", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B_pow.place(x=240,y=160)  

# Button for number 1
B1 = Button(top, text = "1", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B1.place(x=100,y=230)
print(B1)

# Button for number 2
B2 = Button(top, text = "2", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B2.place(x=170,y=230)

# Button for number 3
B3 = Button(top, text = "3", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B3.place(x=240,y=230)    

# Button for number 4
B4 = Button(top, text = "4", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B4.place(x=100,y=300)

# Button for number 5
B5 = Button(top, text = "5", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B5.place(x=170,y=300)

# Button for number 6
B6 = Button(top, text = "6", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B6.place(x=240,y=300)        

# Button for number 7
B7 = Button(top, text = "7", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B7.place(x=100,y=370)

# Button for number 8
B8 = Button(top, text = "8", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B8.place(x=170,y=370)

# Button for number 9
B9 = Button(top, text = "9", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B9.place(x=240,y=370)

# Button for number 0
B0 = Button(top, text = "0", command = sqr(1), width=20, height=4, bg="gray", fg="black")
B0.place(x=100,y=440)

# Button for decimal place
B_dot = Button(top, text = ".", command = sqr(1), width=9, height=4, bg="gray", fg="black")
B_dot.place(x=240,y=440)        

# Button for division operation
B_div = Button(top, text = "/", command = sqr(1), width=6, height=4, bg="gray", fg="black")
B_div.place(x=310,y=160)    

# Button for multiplication operation
B_mul = Button(top, text = "*", command = sqr(1), width=6, height=4, bg="gray", fg="black")
B_mul.place(x=310,y=230)

# Button for sum operation
B_sum = Button(top, text = "+", command = sqr(1), width=6, height=4, bg="gray", fg="black")
B_sum.place(x=310,y=300)    

# Button for subtraction operation
B_sub = Button(top, text = "-", command = sqr(1), width=6, height=4, bg="gray", fg="black")
B_sub.place(x=310,y=370)  

# Button for result
B_res = Button(top, text = "=", command = sqr(1), width=6, height=4, bg="gray", fg="black")
B_res.place(x=310,y=440)  

#label = Label(top, textvariable=var, relief=RAISED, justify=RIGHT)
"""

    