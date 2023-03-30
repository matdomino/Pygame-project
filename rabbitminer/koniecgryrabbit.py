import pygame


def koniec_top(wynik):
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Rabbit Miner")

    koniec_gry = pygame.Rect(100, 150, 300, 60)
    gratulacje = pygame.Rect(107, 210, 170, 50)
    wynik_rect = pygame.Rect(107, 250, 170, 50)
    imie = pygame.Rect(107, 300, 170, 50)


    font_naglowek = pygame.font.Font(None, 45)
    font_wynik = pygame.font.Font(None, 30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        pygame.draw.rect(screen, (49, 196, 26), koniec_gry)

        screen.blit(font_wynik.render("Gratulacje jesteś w Top10", True, (255, 255, 255)), (gratulacje.x + 15, gratulacje.y + 15))
        screen.blit(font_naglowek.render("Koniec gry", True, (255, 255, 255)), (koniec_gry.x + 70, koniec_gry.y + 15))
        screen.blit(font_wynik.render("Wynik: "+str(wynik), True, (255, 255, 255)), (wynik_rect.x + 90, wynik_rect.y + 15))
        screen.blit(font_wynik.render("Podaj imie w konsoli", True, (255, 255, 255)), (imie.x + 40, imie.y + 15))


        pygame.display.update()

def koniec_zwykly(wynik):
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Rabbit Miner")

    koniec_gry = pygame.Rect(100, 150, 300, 60)
    wynik_rect = pygame.Rect(107, 250, 170, 50)


    font_naglowek = pygame.font.Font(None, 45)
    font_wynik = pygame.font.Font(None, 30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        pygame.draw.rect(screen, (49, 196, 26), koniec_gry)

        screen.blit(font_naglowek.render("Koniec gry", True, (255, 255, 255)), (koniec_gry.x + 70, koniec_gry.y + 15))
        screen.blit(font_wynik.render("Wynik: "+str(wynik), True, (255, 255, 255)), (wynik_rect.x + 90, wynik_rect.y))


        pygame.display.update()

def koniec_przegrana():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Rabbit Miner")

    koniec_gry = pygame.Rect(100, 150, 300, 60)
    powod = pygame.Rect(107, 250, 170, 50)


    font_naglowek = pygame.font.Font(None, 45)
    font_wynik = pygame.font.Font(None, 30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        pygame.draw.rect(screen, (49, 196, 26), koniec_gry)

        screen.blit(font_naglowek.render("Koniec gry", True, (255, 255, 255)), (koniec_gry.x + 70, koniec_gry.y + 15))
        screen.blit(font_wynik.render("Królik trafił na niebezpieczeństwo!", True, (255, 255, 255)), (powod.x - 28, powod.y))


        pygame.display.update()
