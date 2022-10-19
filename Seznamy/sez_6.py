
action = 0
sez = []
while action != 'exit':
    action = str(input('napiste co chcete delat: prid_jmen, vyp_sez, vym_jmen, vyp_poc, vyp_sort_sez'))
    if action == 'prid_jmen':
        jmen = str(input('Napis jmeno jake chces pritat'))
        sez.append(jmen)

    elif action == 'vyp_sez':
        print(sez)

    elif action == 'vym_jmen':
        jmen = str(input('Napis jmeno jake chces vymazat'))
        if jmen in sez:
            sez.remove("jmen")
        else:
            print('jmeno neni v seznamu')

    elif action == 'vyp_poc':
        print(len(sez))

    elif action == 'vyp_sort_sez':
        print(sorted(sez))
