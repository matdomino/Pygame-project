import pygame

def run():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Rabbit Miner")


    przycisk_wroc = pygame.Rect(0, 0, 90, 40)
    tekst1 = pygame.Rect(40, 100, 90, 40)
    tekst2 = pygame.Rect(40, 160, 90, 40)
    tekst3 = pygame.Rect(40, 220, 90, 40)
    tekst4 = pygame.Rect(40, 280, 90, 40)
    tekst5 = pygame.Rect(40, 340, 90, 40)



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
        screen.blit(font_text.render("Cel gry: poprowadzenie królika do", True, (255, 255, 255)), (tekst1.x + 20, tekst1.y + 12))
        screen.blit(font_text.render("schronienia używając strzałek.", True, (255, 255, 255)), (tekst2.x + 20, tekst2.y + 12))
        screen.blit(font_text.render("Królik słyszy, ale nie widzi", True, (255, 255, 255)), (tekst3.x + 20, tekst3.y + 12))
        screen.blit(font_text.render("niebezpieczeństw, co sygnalizuje", True, (255, 255, 255)), (tekst4.x + 20, tekst4.y + 12))
        screen.blit(font_text.render("czerwona ikonka z wykrzyknikiem", True, (255, 255, 255)), (tekst5.x + 20, tekst5.y + 12))
        


        pygame.display.update()


