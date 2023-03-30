import pygame

def run():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Fasolki")


    przycisk_wroc = pygame.Rect(0, 0, 90, 40)
    teskt1 = pygame.Rect(40, 100, 90, 40)
    teskt2 = pygame.Rect(40, 160, 90, 40)
    teskt3 = pygame.Rect(40, 220, 90, 40)
    teskt4 = pygame.Rect(40, 280, 90, 40)
    teskt5 = pygame.Rect(40, 340, 90, 40)



    font_text = pygame.font.Font(None, 30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_wroc.collidepoint(event.pos):
                    return


        pygame.draw.rect(screen, (255, 45, 0), przycisk_wroc)

        screen.blit(font_text.render("Wróć", True, (255, 255, 255)), (przycisk_wroc.x + 20, przycisk_wroc.y + 12))
        screen.blit(font_text.render("Cel gry: zgadnięcie ułożenia 9 cyfr od", True, (255, 255, 255)), (teskt1.x + 20, teskt1.y + 12))
        screen.blit(font_text.render("1 do 10. Po naciśnięciu \"Podaj\" wprowadź", True, (255, 255, 255)), (teskt2.x + 20, teskt2.y + 12))
        screen.blit(font_text.render("w konsoli liczby bez powtarzania. ", True, (255, 255, 255)), (teskt3.x + 20, teskt3.y + 12))
        screen.blit(font_text.render("\"Sąsiednie\" oznaczają pary które w ", True, (255, 255, 255)), (teskt4.x + 20, teskt4.y + 12))
        screen.blit(font_text.render("oczekiwanym wyniku są koło siebie.", True, (255, 255, 255)), (teskt5.x + 20, teskt5.y + 12))


        pygame.display.update()


