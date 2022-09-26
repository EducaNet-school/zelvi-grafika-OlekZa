import turtle


def square(a):
    for i in range(4):
        turtle.fd(a)
        turtle.rt(90)


square(80)
turtle.rt(135)
square(80)
turtle.rt(180)
square(80)
