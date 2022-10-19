a = 1
b = 2
sez = [1, 2]

count = int(input('Write count of numbers'))
rng = count // 2

for i in range(rng):
    a += b
    sez.append(a)
    b += a
    sez.append(b)

print(sez)
