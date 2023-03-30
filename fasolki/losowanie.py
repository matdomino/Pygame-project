import random

def losowy_uklad():
    uklad = []
    zakres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(3):
        uklad_tmp = []
        for y in range(3):
            a = random.choice(zakres)
            uklad_tmp.append(a)
            zakres.remove(a)
        uklad.append(uklad_tmp)

    return uklad
