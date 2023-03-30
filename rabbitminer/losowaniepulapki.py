import random

def losowanie_indeks():
    spot1 = []
    spot2 = []
    spot3 = []
    spot4 = []
    spot5 = []

    zakres_x = [1,2,3,4,5,6,7,8,9]
    zakres_y = [2,3,4,5,6,7,8]
    a1 = random.choice(zakres_x)
    zakres_x.remove(a1)
    b1 = random.choice(zakres_y)
    zakres_y.remove(b1)
    spot1.append(a1)
    spot1.append(b1)

    a2 = random.choice(zakres_x)
    zakres_x.remove(a2)
    b2 = random.choice(zakres_y)
    zakres_y.remove(b2)
    spot2.append(a2)
    spot2.append(b2)

    a3 = random.choice(zakres_x)
    zakres_x.remove(a3)
    b3 = random.choice(zakres_y)
    zakres_y.remove(b3)
    spot3.append(a3)
    spot3.append(b3)

    a4 = random.choice(zakres_x)
    zakres_x.remove(a4)
    b4 = random.choice(zakres_y)
    zakres_y.remove(b4)
    spot4.append(a4)
    spot4.append(b4)

    a5 = random.choice(zakres_x)
    zakres_x.remove(a5)
    b5 = random.choice(zakres_y)
    zakres_y.remove(b5)
    spot5.append(a5)
    spot5.append(b5)
    
    return [spot1,spot2,spot3,spot4,spot5]


#wyswietla liste list, np. [[6, 4], [1, 7], [7, 8], [9, 3], [5, 5]]

