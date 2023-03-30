import pygame
import importlib
import sys


sys.path.append("fasolki")
sys.path.append("fasolki/Dane")
sys.path.append("rabbitminer")
sys.path.append("rabbitminer/Dane")


pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Menu")

wybierz_gre = pygame.Rect(88, 100, 300, 80)
przycisk_gra1 = pygame.Rect(165, 200, 170, 50)
przycisk_gra2 = pygame.Rect(165, 270, 170, 50)
imie_nazwisko = pygame.Rect(300, 450, 200, 50)

font_naglowek = pygame.font.Font(None, 50)
font_gra = pygame.font.Font(None, 30)
font_naziwsko = pygame.font.Font(None, 20)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if przycisk_gra1.collidepoint(event.pos):
                fasolki = importlib.import_module("fasolki.fasolkimenu.py")
                fasolki.run()
            if przycisk_gra2.collidepoint(event.pos):
                imported = importlib.import_module("rabitmenu.py")
                imported.run()


    pygame.draw.rect(screen, (137, 196, 220), przycisk_gra1)
    pygame.draw.rect(screen, (137, 196, 220), przycisk_gra2)


    screen.blit(font_naglowek.render("Wybierz grę:", True, (65, 200, 85)), (wybierz_gre.x + 60, wybierz_gre.y + 30))
    screen.blit(font_gra.render("Fasolki", True, (255, 255, 255)), (przycisk_gra1.x + 50, przycisk_gra1.y + 18))
    screen.blit(font_gra.render("Rabbit Miner", True, (255, 255, 255)), (przycisk_gra2.x + 22, przycisk_gra2.y + 15))
    screen.blit(font_naziwsko.render("Mateusz Domino 2023", True, (76, 82, 82)), (imie_nazwisko.x + 50, imie_nazwisko.y + 30))
    pygame.display.update()

pygame.quit()
