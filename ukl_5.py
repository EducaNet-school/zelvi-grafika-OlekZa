import turtle as tr


def spr(q):
    tr.forward(q)
    tr.rt(90)
    tr.forward(q)


q = 5

while q != 150:
    spr(q)
    q += 5
