import turtle

def koch(l, n):
    if n == 0:
        turtle.pendown()
        turtle.forward(l)
        return
    else:
        koch(l/8, n - 1)
        turtle.pendown()
        turtle.left(90)
        koch(l/8, n - 1)
        turtle.right(90)
        koch(l/8, n - 1)
        turtle.right(90)
        koch(l/8, n - 1)

        koch(l / 8, n - 1)
        turtle.left(90)
        koch(l/8, n - 1)
        turtle.left(90)
        koch(l/8, n - 1)
        turtle.right(90)
        koch(l/8, n - 1)

koch(333,3)