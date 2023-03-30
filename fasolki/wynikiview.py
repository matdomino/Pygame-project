import pygame
from Dane import wyniki

def run():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Fasolki")

    najlepsze = pygame.Rect(100, 90, 300, 60)
    przycisk_wroc = pygame.Rect(0, 0, 90, 40)

    najlepszy_1 = pygame.Rect(107, 160, 170, 50)
    najlepszy_2 = pygame.Rect(107, 185, 170, 50)
    najlepszy_3 = pygame.Rect(107, 210, 170, 50)
    najlepszy_4 = pygame.Rect(107, 235, 170, 50)
    najlepszy_5 = pygame.Rect(107, 260, 170, 50)
    najlepszy_6 = pygame.Rect(107, 285, 170, 50)
    najlepszy_7 = pygame.Rect(107, 310, 170, 50)
    najlepszy_8 = pygame.Rect(107, 335, 170, 50)
    najlepszy_9 = pygame.Rect(107, 360, 170, 50)
    najlepszy_10 = pygame.Rect(107, 385, 170, 50)

    top1 = wyniki.top10[0]["nazwa"] + ": " + str(wyniki.top10[0]["wynik"])
    top2 = wyniki.top10[1]["nazwa"] + ": " + str(wyniki.top10[1]["wynik"])
    top3 = wyniki.top10[2]["nazwa"] + ": " + str(wyniki.top10[2]["wynik"])
    top4 = wyniki.top10[3]["nazwa"] + ": " + str(wyniki.top10[3]["wynik"])
    top5 = wyniki.top10[4]["nazwa"] + ": " + str(wyniki.top10[4]["wynik"])
    top6 = wyniki.top10[5]["nazwa"] + ": " + str(wyniki.top10[5]["wynik"])
    top7 = wyniki.top10[6]["nazwa"] + ": " + str(wyniki.top10[6]["wynik"])
    top8 = wyniki.top10[7]["nazwa"] + ": " + str(wyniki.top10[7]["wynik"])
    top9 = wyniki.top10[8]["nazwa"] + ": " + str(wyniki.top10[8]["wynik"])
    top10 = wyniki.top10[9]["nazwa"] + ": " + str(wyniki.top10[9]["wynik"])


    font_naglowek = pygame.font.Font(None, 45)
    font_wynik = pygame.font.Font(None, 30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_wroc.collidepoint(event.pos):
                    return

        pygame.draw.rect(screen, (116, 35, 233), najlepsze)
        pygame.draw.rect(screen, (255, 45, 0), przycisk_wroc)

        screen.blit(font_naglowek.render("Najlepsze wyniki:", True, (255, 255, 255)), (najlepsze.x + 20, najlepsze.y + 15))
        screen.blit(font_wynik.render("Wróć", True, (255, 255, 255)), (przycisk_wroc.x + 20, przycisk_wroc.y + 12))
        screen.blit(font_wynik.render(top1, True, (255, 255, 255)), (najlepszy_1.x + 15, najlepszy_1.y + 15))
        screen.blit(font_wynik.render(top2, True, (255, 255, 255)), (najlepszy_2.x + 15, najlepszy_2.y + 15))
        screen.blit(font_wynik.render(top3, True, (255, 255, 255)), (najlepszy_3.x + 15, najlepszy_3.y + 15))
        screen.blit(font_wynik.render(top4, True, (255, 255, 255)), (najlepszy_4.x + 15, najlepszy_4.y + 15))
        screen.blit(font_wynik.render(top5, True, (255, 255, 255)), (najlepszy_5.x + 15, najlepszy_5.y + 15))
        screen.blit(font_wynik.render(top6, True, (255, 255, 255)), (najlepszy_6.x + 15, najlepszy_6.y + 15))
        screen.blit(font_wynik.render(top7, True, (255, 255, 255)), (najlepszy_7.x + 15, najlepszy_7.y + 15))
        screen.blit(font_wynik.render(top8, True, (255, 255, 255)), (najlepszy_8.x + 15, najlepszy_8.y + 15))
        screen.blit(font_wynik.render(top9, True, (255, 255, 255)), (najlepszy_9.x + 15, najlepszy_9.y + 15))
        screen.blit(font_wynik.render(top10, True, (255, 255, 255)), (najlepszy_10.x + 15, najlepszy_10.y + 15))


        pygame.display.update()


