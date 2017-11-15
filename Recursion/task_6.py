import turtle

def levi(l, n):
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.left(45)
        levi(l/2, n - 1)
        turtle.right(90)
        levi(l/2, n - 1)
        turtle.left(45)

levi(180,5)