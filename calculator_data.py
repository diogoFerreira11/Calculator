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

