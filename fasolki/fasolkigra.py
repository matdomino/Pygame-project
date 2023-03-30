import pygame
import wpisywanie
import sprawdzanie
import losowanie
import czysasiednie
import koniecgry
from Dane import wyniki

def run():
    oczekiwany = losowanie.losowy_uklad()
    print(oczekiwany)
    wynik = 0
    zgodne = 0
    sasiednie = 0
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Fasolki")

    przycisk_wroc = pygame.Rect(0, 0, 90, 40)
    liczba_prob = pygame.Rect(350, 0, 150, 40)
    podaj_cyrfy = pygame.Rect(30, 120, 250, 250)
    poprzednia_proba = pygame.Rect(320, 170, 150, 150)
    liczba_poprawnych = pygame.Rect(0, 460, 150, 40)
    liczba_sasiadow = pygame.Rect(350, 460, 150, 40)
    sprawdz = pygame.Rect(335, 330, 120, 40)
    podaj = pygame.Rect(30, 370, 120, 40)


    obecna_1 = pygame.Rect(50, 170, 40, 40)
    obecna_2 = pygame.Rect(110, 170, 40, 40)
    obecna_3 = pygame.Rect(170, 170, 40, 40)
    obecna_4 = pygame.Rect(50, 230, 40, 40)
    obecna_5 = pygame.Rect(110, 230, 40, 40)
    obecna_6 = pygame.Rect(170, 230, 40, 40)
    obecna_7 = pygame.Rect(50, 290, 40, 40)
    obecna_8 = pygame.Rect(110, 290, 40, 40)
    obecna_9 = pygame.Rect(170, 290, 40, 40)


    poprzednia_1 = pygame.Rect(340, 200, 30, 30)
    poprzednia_2 = pygame.Rect(380, 200, 30, 30)
    poprzednia_3 = pygame.Rect(420, 200, 30, 30)
    poprzednia_4 = pygame.Rect(340, 240, 30, 30)
    poprzednia_5 = pygame.Rect(380, 240, 30, 30)
    poprzednia_6 = pygame.Rect(420, 240, 30, 30)
    poprzednia_7 = pygame.Rect(340, 280, 30, 30)
    poprzednia_8 = pygame.Rect(380, 280, 30, 30)
    poprzednia_9 = pygame.Rect(420, 280, 30, 30)


    font_podaj = pygame.font.Font(None, 40)
    font_text = pygame.font.Font(None, 30)
    font_liczbaobecna = pygame.font.Font(None, 50)


    obec1 = ""
    obec2 = ""
    obec3 = ""
    obec4 = ""
    obec5 = ""
    obec6 = ""
    obec7 = ""
    obec8 = ""
    obec9 = ""

    poprzed1 = ""
    poprzed2 = ""
    poprzed3 = ""
    poprzed4 = ""
    poprzed5 = ""
    poprzed6 = ""
    poprzed7 = ""
    poprzed8 = ""
    poprzed9 = ""


    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_wroc.collidepoint(event.pos):
                    return

                if podaj.collidepoint(event.pos):
                    lista = wpisywanie.wpisany_rzad()
                    obec1 = str(lista[0][0])
                    obec2 = str(lista[0][1])
                    obec3 = str(lista[0][2])
                    obec4 = str(lista[1][0])
                    obec5 = str(lista[1][1])
                    obec6 = str(lista[1][2])
                    obec7 = str(lista[2][0])
                    obec8 = str(lista[2][1])
                    obec9 = str(lista[2][2])

                if sprawdz.collidepoint(event.pos):
                    wynik = wynik + 1
                    zgodne = sprawdzanie.sprawdzanie(oczekiwany,lista)
                    if zgodne == 9:
                        topka = wyniki.top10
                        if wynik < topka[9]['wynik']:
                            koniecgry.koniec_top(wynik)
                            return
                        else:
                            koniecgry.koniec_zwykly(wynik)
                            return

                        pygame.quit()
                    else:
                        sasiednie = czysasiednie.pary(oczekiwany,lista)

                        poprzed1 = obec1
                        poprzed2 = obec2
                        poprzed3 = obec3
                        poprzed4 = obec4
                        poprzed5 = obec5
                        poprzed6 = obec6
                        poprzed7 = obec7
                        poprzed8 = obec8
                        poprzed9 = obec9

                        obec1 = ""
                        obec2 = ""
                        obec3 = ""
                        obec4 = ""
                        obec5 = ""
                        obec6 = ""
                        obec7 = ""
                        obec8 = ""
                        obec9 = ""


        pygame.display.flip()
        clock.tick(60)


        pygame.draw.rect(screen, (255, 45, 0), przycisk_wroc)
        pygame.draw.rect(screen, (118, 226, 89), liczba_prob)
        pygame.draw.rect(screen, (118, 226, 89), liczba_poprawnych)
        pygame.draw.rect(screen, (118, 226, 89), liczba_sasiadow)
        pygame.draw.rect(screen, (137, 196, 220), podaj_cyrfy)
        pygame.draw.rect(screen, (137, 196, 220), sprawdz)
        pygame.draw.rect(screen, (118, 226, 89), podaj)


        pygame.draw.rect(screen, (255, 255, 255), obecna_1)
        pygame.draw.rect(screen, (255, 255, 255), obecna_2)
        pygame.draw.rect(screen, (255, 255, 255), obecna_3)
        pygame.draw.rect(screen, (255, 255, 255), obecna_4)
        pygame.draw.rect(screen, (255, 255, 255), obecna_5)
        pygame.draw.rect(screen, (255, 255, 255), obecna_6)
        pygame.draw.rect(screen, (255, 255, 255), obecna_7)
        pygame.draw.rect(screen, (255, 255, 255), obecna_8)
        pygame.draw.rect(screen, (255, 255, 255), obecna_9)


        pygame.draw.rect(screen, (255, 255, 255), poprzednia_1)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_2)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_3)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_4)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_5)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_6)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_7)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_8)
        pygame.draw.rect(screen, (255, 255, 255), poprzednia_9)


        screen.blit(font_text.render("Wróć", True, (255, 255, 255)), (przycisk_wroc.x + 20, przycisk_wroc.y + 12))
        screen.blit(font_text.render("Wynik: "+str(wynik), True, (255, 255, 255)), (liczba_prob.x + 20, liczba_prob.y + 12))
        screen.blit(font_text.render("Poprawne: "+str(zgodne), True, (255, 255, 255)), (liczba_poprawnych.x + 18, liczba_poprawnych.y + 12))
        screen.blit(font_text.render("Sąsiednie: "+str(sasiednie), True, (255, 255, 255)), (liczba_sasiadow.x + 18, liczba_sasiadow.y + 12))
        screen.blit(font_podaj.render("Podaj cyfry:", True, (255, 255, 255)), (podaj_cyrfy.x + 18, podaj_cyrfy.y + 12))
        screen.blit(font_text.render("Ostatnia próba:", True, (255, 255, 255)), (poprzednia_proba.x + 2, poprzednia_proba.y))
        screen.blit(font_text.render("Sprawdz", True, (118, 226, 89)), (sprawdz.x + 17, sprawdz.y + 10))
        screen.blit(font_text.render("Podaj", True, (255, 255, 255)), (podaj.x + 30, podaj.y + 10))


        screen.blit(font_liczbaobecna.render(obec1, True, (0, 0, 0)), (obecna_1.x + 10, poprzednia_1.y - 25))
        screen.blit(font_liczbaobecna.render(obec2, True, (0, 0, 0)), (obecna_2.x + 10, poprzednia_2.y - 25))
        screen.blit(font_liczbaobecna.render(obec3, True, (0, 0, 0)), (obecna_3.x + 10, poprzednia_3.y - 25))
        screen.blit(font_liczbaobecna.render(obec4, True, (0, 0, 0)), (obecna_4.x + 10, poprzednia_4.y - 5))
        screen.blit(font_liczbaobecna.render(obec5, True, (0, 0, 0)), (obecna_5.x + 10, poprzednia_5.y - 5))
        screen.blit(font_liczbaobecna.render(obec6, True, (0, 0, 0)), (obecna_6.x + 10, poprzednia_6.y - 5))
        screen.blit(font_liczbaobecna.render(obec7, True, (0, 0, 0)), (obecna_7.x + 10, poprzednia_7.y + 14))
        screen.blit(font_liczbaobecna.render(obec8, True, (0, 0, 0)), (obecna_8.x + 10, poprzednia_8.y + 14))
        screen.blit(font_liczbaobecna.render(obec9, True, (0, 0, 0)), (obecna_9.x + 10, poprzednia_9.y + 14))


        screen.blit(font_podaj.render(poprzed1, True, (0, 0, 0)), (poprzednia_1.x + 7, poprzednia_1.y + 3))
        screen.blit(font_podaj.render(poprzed2, True, (0, 0, 0)), (poprzednia_2.x + 7, poprzednia_2.y + 3))
        screen.blit(font_podaj.render(poprzed3, True, (0, 0, 0)), (poprzednia_3.x + 7, poprzednia_3.y + 3))
        screen.blit(font_podaj.render(poprzed4, True, (0, 0, 0)), (poprzednia_4.x + 7, poprzednia_4.y + 3))
        screen.blit(font_podaj.render(poprzed5, True, (0, 0, 0)), (poprzednia_5.x + 7, poprzednia_5.y + 3))
        screen.blit(font_podaj.render(poprzed6, True, (0, 0, 0)), (poprzednia_6.x + 7, poprzednia_6.y + 3))
        screen.blit(font_podaj.render(poprzed7, True, (0, 0, 0)), (poprzednia_7.x + 7, poprzednia_7.y + 3))
        screen.blit(font_podaj.render(poprzed8, True, (0, 0, 0)), (poprzednia_8.x + 7, poprzednia_8.y + 3))
        screen.blit(font_podaj.render(poprzed9, True, (0, 0, 0)), (poprzednia_9.x + 7, poprzednia_9.y + 3))


        pygame.display.update()
