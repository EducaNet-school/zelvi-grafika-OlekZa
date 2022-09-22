import turtle as tr


range_c = int(input("write a number of branches of flower"))
radius = int(input("write a number of branches of flower"))


def flower(range_c, radius):
    for i in range(range_c):
        tr.circle(radius, extent=30)
        tr.left(140)
        tr.circle(radius, extent=30)


flower(range_c, radius)

tr.done()
