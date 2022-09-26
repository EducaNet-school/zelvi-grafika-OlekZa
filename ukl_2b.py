import turtle as tr


def square():
    for i in range(4):
        tr.forward(90)
        tr.right(90)


square()
tr.penup()
tr.forward(200)
tr.pendown()
square()
