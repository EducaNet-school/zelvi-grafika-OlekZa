import turtle

t = turtle.Turtle()


def pentagon(strany, delka):
    for i in range(strany):
        t.forward(delka)
        t.right(delka)


pentagon(5, 72)
