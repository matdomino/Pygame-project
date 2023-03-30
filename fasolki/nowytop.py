from Dane import wyniki

def nowy_top(wynik):
    print("Podaj nazwe:") 
    nazwa = input()
    nowy = {"nazwa": nazwa, "wynik": wynik}

    slownik = wyniki.top10

    if wynik < slownik[9]["wynik"]: 
        slownik[9] = nowy
        
    sorted_slownik = sorted(slownik, key=lambda x: x["wynik"], reverse=False)
    return sorted_slownik
    