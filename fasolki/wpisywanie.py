def wpisany_rzad():
    lista_wpisana = []
    zakres_dopuszczalny = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Podaj pierwszy rząd:")

    for z in range(3):
        lista_tmp = []
        for x in range(3):
            status = False
            while status == False:
                y = input()
                if y.isdigit():
                    y = int(y)
                    if y in zakres_dopuszczalny:
                        lista_tmp.append(y)
                        zakres_dopuszczalny.remove(y)
                        status = True
                    else:
                        print("Podaj liczbę całkowitą od 1 do 9, bez powtórzeń")
                else:
                    print("Podaj liczbę całkowitą od 1 do 9, bez powtórzeń")
        lista_wpisana.append(lista_tmp)
        if z != 2:
            print("Podaj kolejny rząd")
    print("--------------------")
    return lista_wpisana
