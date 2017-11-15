import turtle

def cantor(n, l):
    if n == 0:
        turtle.pendown()
        turtle.forward(l)
        return
    else:
        turtle.pendown()
        turtle.forward(l)
        turtle.penup()

        turtle.backward(l)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)

        cantor(n - 1, l/3)

        turtle.penup()
        turtle.forward(l/3)
        cantor(n - 1, l/3)

        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)


cantor(3,180)