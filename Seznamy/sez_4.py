
sez = [1, 4, 5, 6, 7, 334]  # pro seznam


def greater_than_all(seznam, n):
    nejv = True
    for i in seznam:
        if i > n:
            nejv = False
            print(f'{n} neni nejventsi element')
            break

    if nejv is not False:
        print(f'{n} je nejvetsi element')


greater_than_all(sez, 600)

#snaz se psat funkce, ktere nemaji uzivatelsky vstup
#nebo vystup. Funkce Greater by mela vrazet true, false,
# ty printy by mely byt mimo ni
