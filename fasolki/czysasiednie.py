def pary(lista_oczekiwana,lita_wpisana):
    pary = 0
    for x in range (len(lita_wpisana)):
        for y in range(len(lita_wpisana)-1):
            liczba1 = lita_wpisana[x][y]
            liczba2 = lita_wpisana[x][y+1]
            for a in range(len(lista_oczekiwana)):
                for b in range(len(lista_oczekiwana)-1):
                    if lista_oczekiwana[a][b] == liczba1 and lista_oczekiwana[a][b+1] == liczba2:
                        pary = pary + 1
                    elif lista_oczekiwana[a][b] == liczba2 and lista_oczekiwana[a][b+1] == liczba1:
                        pary = pary + 1
    return pary
