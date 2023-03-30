import pygame
import fasolkijakgrac
import wynikiview
import fasolkigra

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Fasolki")

naglowekfasolki = pygame.Rect(90, 80, 300, 80)
przycisk_graj = pygame.Rect(165, 190, 170, 50)
przycisk_wyniki = pygame.Rect(175, 260, 150, 40)
jak_grac = pygame.Rect(175, 310, 150, 40)

font_naglowek = pygame.font.Font(None, 80)
font_stnd = pygame.font.Font(None, 30)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if przycisk_graj.collidepoint(event.pos):
                fasolkigra.run()
                screen.fill((0, 0, 0))

            if przycisk_wyniki.collidepoint(event.pos):
                wynikiview.run()
                screen.fill((0, 0, 0))

            if jak_grac.collidepoint(event.pos):
                fasolkijakgrac.run()
                screen.fill((0, 0, 0))


    pygame.draw.rect(screen, (16, 146, 226), przycisk_graj)
    pygame.draw.rect(screen, (137, 196, 220), przycisk_wyniki)
    pygame.draw.rect(screen, (137, 196, 220), jak_grac)


    screen.blit(font_naglowek.render("Fasolki", True, (116, 35, 233)), (naglowekfasolki.x + 62, naglowekfasolki.y + 30))
    screen.blit(font_stnd.render("Graj", True, (255, 255, 255)), (przycisk_graj.x + 63, przycisk_graj.y + 18))
    screen.blit(font_stnd.render("Wyniki", True, (255, 255, 255)), (przycisk_wyniki.x + 40, przycisk_wyniki.y + 12))
    screen.blit(font_stnd.render("Jak grać?", True, (255, 255, 255)), (jak_grac.x + 26, jak_grac.y + 12))
    pygame.display.update()

pygame.quit()
