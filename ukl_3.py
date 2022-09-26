import turtle as tr


def trojuhl():
    tr.forward(100)
    tr.left(120)
    tr.forward(100)
    tr.left(120)
    tr.forward(100)


def sestiuhl():
    for i in range(6):
        trojuhl()
        tr.left(60)


sestiuhl()
