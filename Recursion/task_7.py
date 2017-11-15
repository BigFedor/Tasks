import turtle
from math import sqrt

def dragon(n, l, angle = 45):
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.right(angle)
        dragon(n - 1, l / sqrt(2), 45)
        turtle.left(angle * 2)
        dragon(n - 1, l / sqrt(2), -45)
        turtle.right(angle)

dragon(6, 180)
