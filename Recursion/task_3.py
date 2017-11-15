import turtle

def koch(l, n):
    if n == 0:
        turtle.pendown()
        turtle.forward(l)
        return
    else:
        koch(l/3, n - 1)
        turtle.pendown()
        turtle.left(60)
        koch(l/3, n - 1)
        turtle.right(120)
        koch(l/3, n - 1)
        turtle.left(60)
        koch(l/3, n - 1)

koch(180,3)
#print("hello")