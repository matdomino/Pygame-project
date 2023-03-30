def sprawdzanie(lista_oczekiwana,lita_wpisana):
    poprawne = 0
    for x in range(len(lista_oczekiwana)):
        for y in range(len(lista_oczekiwana)):
            if lista_oczekiwana[x][y] == lita_wpisana[x][y]:
                poprawne = poprawne + 1
    
    return poprawne

