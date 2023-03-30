import pygame
import koniecgryrabbit
import losowaniepulapki
from Dane import wyniki

def run():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("Rabbit Miner")

    przycisk_wroc = pygame.Rect(0, 0, 90, 40)
    liczba_ruchow = pygame.Rect(350, 0, 150, 40)
    uwaga = pygame.Rect(420, 220, 60, 60) #######################################

    
    pygame.draw.circle(screen, (95, 47, 42), (420,65), 15)

    pole1 = pygame.Rect(50, 430, 30, 30)
    pole2 = pygame.Rect(90, 430, 30, 30)
    pole3 = pygame.Rect(130, 430, 30, 30)
    pole4 = pygame.Rect(170, 430, 30, 30)
    pole5 = pygame.Rect(210, 430, 30, 30)
    pole6 = pygame.Rect(250, 430, 30, 30)
    pole7 = pygame.Rect(290, 430, 30, 30)
    pole8 = pygame.Rect(330, 430, 30, 30)
    pole9 = pygame.Rect(370, 430, 30, 30)
    pole10 = pygame.Rect(50, 430, 30, 30)
    pole11 = pygame.Rect(90, 390, 30, 30)
    pole12 = pygame.Rect(130, 390, 30, 30)
    pole13 = pygame.Rect(170, 390, 30, 30)
    pole14 = pygame.Rect(210, 390, 30, 30)
    pole15 = pygame.Rect(250, 390, 30, 30)
    pole16 = pygame.Rect(290, 390, 30, 30)
    pole17 = pygame.Rect(330, 390, 30, 30)
    pole18 = pygame.Rect(370, 390, 30, 30)
    pole19 = pygame.Rect(50, 390, 30, 30)
    pole20 = pygame.Rect(90, 350, 30, 30)
    pole21 = pygame.Rect(130, 350, 30, 30)
    pole22 = pygame.Rect(170, 350, 30, 30)
    pole23 = pygame.Rect(210, 350, 30, 30)
    pole24 = pygame.Rect(250, 350, 30, 30)
    pole25 = pygame.Rect(290, 350, 30, 30)
    pole26 = pygame.Rect(330, 350, 30, 30)
    pole27 = pygame.Rect(370, 350, 30, 30)
    pole28 = pygame.Rect(50, 350, 30, 30)
    pole29 = pygame.Rect(90, 350, 30, 30)
    pole30 = pygame.Rect(130, 310, 30, 30)
    pole31 = pygame.Rect(170, 310, 30, 30)
    pole32 = pygame.Rect(210, 310, 30, 30)
    pole33 = pygame.Rect(250, 310, 30, 30)
    pole34 = pygame.Rect(290, 310, 30, 30)
    pole35 = pygame.Rect(330, 310, 30, 30)
    pole36 = pygame.Rect(370, 310, 30, 30)
    pole37 = pygame.Rect(50, 310, 30, 30)
    pole38 = pygame.Rect(90, 310, 30, 30)
    pole39 = pygame.Rect(130, 310, 30, 30)
    pole40 = pygame.Rect(170, 270, 30, 30)
    pole41 = pygame.Rect(210, 270, 30, 30)
    pole42 = pygame.Rect(250, 270, 30, 30)
    pole43 = pygame.Rect(290, 270, 30, 30)
    pole44 = pygame.Rect(330, 270, 30, 30)
    pole45 = pygame.Rect(370, 270, 30, 30)
    pole46 = pygame.Rect(50, 270, 30, 30)
    pole47 = pygame.Rect(90, 270, 30, 30)
    pole48 = pygame.Rect(130, 270, 30, 30)
    pole49 = pygame.Rect(170, 270, 30, 30)
    pole50 = pygame.Rect(210, 230, 30, 30)
    pole51 = pygame.Rect(250, 230, 30, 30)
    pole52 = pygame.Rect(290, 230, 30, 30)
    pole53 = pygame.Rect(330, 230, 30, 30)
    pole54 = pygame.Rect(370, 230, 30, 30)
    pole55 = pygame.Rect(50, 230, 30, 30)
    pole56 = pygame.Rect(90, 230, 30, 30)
    pole57 = pygame.Rect(130, 230, 30, 30)
    pole58 = pygame.Rect(170, 230, 30, 30)
    pole59 = pygame.Rect(210, 230, 30, 30)
    pole60 = pygame.Rect(250, 230, 30, 30)
    pole61 = pygame.Rect(290, 190, 30, 30)
    pole62 = pygame.Rect(330, 190, 30, 30)
    pole63 = pygame.Rect(370, 190, 30, 30)
    pole64 = pygame.Rect(50, 190, 30, 30)
    pole65 = pygame.Rect(90, 190, 30, 30)
    pole66 = pygame.Rect(130, 190, 30, 30)
    pole67 = pygame.Rect(170, 190, 30, 30)
    pole68 = pygame.Rect(210, 190, 30, 30)
    pole69 = pygame.Rect(250, 190, 30, 30)
    pole70 = pygame.Rect(290, 150, 30, 30)
    pole71 = pygame.Rect(330, 150, 30, 30)
    pole72 = pygame.Rect(370, 150, 30, 30)
    pole73 = pygame.Rect(50, 150, 30, 30)
    pole74 = pygame.Rect(90, 150, 30, 30)
    pole75 = pygame.Rect(130, 150, 30, 30)
    pole76 = pygame.Rect(170, 150, 30, 30)
    pole77 = pygame.Rect(210, 150, 30, 30)
    pole78 = pygame.Rect(250, 150, 30, 30)
    pole79 = pygame.Rect(290, 150, 30, 30)
    pole80 = pygame.Rect(330, 110, 30, 30)
    pole81 = pygame.Rect(370, 110, 30, 30)
    pole82 = pygame.Rect(50, 110, 30, 30)
    pole83 = pygame.Rect(90, 110, 30, 30)
    pole84 = pygame.Rect(130, 110, 30, 30)
    pole85 = pygame.Rect(170, 110, 30, 30)
    pole86 = pygame.Rect(210, 110, 30, 30)
    pole87 = pygame.Rect(250, 110, 30, 30)
    pole88 = pygame.Rect(290, 110, 30, 30)
    pole89 = pygame.Rect(330, 110, 30, 30)
    pole90 = pygame.Rect(370, 70, 30, 30)
    pole91 = pygame.Rect(370, 70, 30, 30)
    pole92 = pygame.Rect(50, 70, 30, 30)
    pole93 = pygame.Rect(90, 70, 30, 30)
    pole94 = pygame.Rect(130, 70, 30, 30)
    pole95 = pygame.Rect(170, 70, 30, 30)
    pole96 = pygame.Rect(210, 70, 30, 30)
    pole97 = pygame.Rect(250, 70, 30, 30)
    pole98 = pygame.Rect(290, 70, 30, 30)
    pole99 = pygame.Rect(330, 70, 30, 30)
    pole100 = pygame.Rect(370, 70, 30, 30)

    font_uwaga = pygame.font.Font(None, 50)
    font_text = pygame.font.Font(None, 30)
    font_krolik = pygame.font.Font(None, 15)


    running = True

    x = 55
    y = 435

    index_x = 0
    index_y = 0

    ruchy = 0

    pulapki = losowaniepulapki.losowanie_indeks()
    print(pulapki)

    current = [0,0]
    
    topka = wyniki.top10

    left_pressed = False
    right_pressed = False
    up_pressed = False
    down_pressed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_wroc.collidepoint(event.pos):
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                elif event.key == pygame.K_RIGHT:
                    right_pressed = True
                elif event.key == pygame.K_UP:
                    up_pressed = True
                elif event.key == pygame.K_DOWN:
                    down_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                elif event.key == pygame.K_RIGHT:
                    right_pressed = False
                elif event.key == pygame.K_UP:
                    up_pressed = False
                elif event.key == pygame.K_DOWN:
                    down_pressed = False

        pygame.draw.rect(screen, (255, 45, 0), uwaga)
        pygame.draw.rect(screen, (255, 45, 0), przycisk_wroc)
        pygame.draw.rect(screen, (118, 226, 96), liczba_ruchow)
        pygame.draw.rect(screen, (208, 197, 96), pole1)
        pygame.draw.rect(screen, (208, 197, 96), pole2)
        pygame.draw.rect(screen, (208, 197, 96), pole3)
        pygame.draw.rect(screen, (208, 197, 96), pole4)
        pygame.draw.rect(screen, (208, 197, 96), pole5)
        pygame.draw.rect(screen, (208, 197, 96), pole6)
        pygame.draw.rect(screen, (208, 197, 96), pole7)
        pygame.draw.rect(screen, (208, 197, 96), pole8)
        pygame.draw.rect(screen, (208, 197, 96), pole9)
        pygame.draw.rect(screen, (208, 197, 96), pole10)
        pygame.draw.rect(screen, (208, 197, 96), pole11)
        pygame.draw.rect(screen, (208, 197, 96), pole12)
        pygame.draw.rect(screen, (208, 197, 96), pole13)
        pygame.draw.rect(screen, (208, 197, 96), pole14)
        pygame.draw.rect(screen, (208, 197, 96), pole15)
        pygame.draw.rect(screen, (208, 197, 96), pole16)
        pygame.draw.rect(screen, (208, 197, 96), pole17)
        pygame.draw.rect(screen, (208, 197, 96), pole18)
        pygame.draw.rect(screen, (208, 197, 96), pole19)
        pygame.draw.rect(screen, (208, 197, 96), pole20)
        pygame.draw.rect(screen, (208, 197, 96), pole21)
        pygame.draw.rect(screen, (208, 197, 96), pole22)
        pygame.draw.rect(screen, (208, 197, 96), pole23)
        pygame.draw.rect(screen, (208, 197, 96), pole24)
        pygame.draw.rect(screen, (208, 197, 96), pole25)
        pygame.draw.rect(screen, (208, 197, 96), pole26)
        pygame.draw.rect(screen, (208, 197, 96), pole27)
        pygame.draw.rect(screen, (208, 197, 96), pole28)
        pygame.draw.rect(screen, (208, 197, 96), pole29)
        pygame.draw.rect(screen, (208, 197, 96), pole30)
        pygame.draw.rect(screen, (208, 197, 96), pole31)
        pygame.draw.rect(screen, (208, 197, 96), pole32)
        pygame.draw.rect(screen, (208, 197, 96), pole33)
        pygame.draw.rect(screen, (208, 197, 96), pole34)
        pygame.draw.rect(screen, (208, 197, 96), pole35)
        pygame.draw.rect(screen, (208, 197, 96), pole36)
        pygame.draw.rect(screen, (208, 197, 96), pole37)
        pygame.draw.rect(screen, (208, 197, 96), pole38)
        pygame.draw.rect(screen, (208, 197, 96), pole39)
        pygame.draw.rect(screen, (208, 197, 96), pole40)
        pygame.draw.rect(screen, (208, 197, 96), pole41)
        pygame.draw.rect(screen, (208, 197, 96), pole42)
        pygame.draw.rect(screen, (208, 197, 96), pole43)
        pygame.draw.rect(screen, (208, 197, 96), pole44)
        pygame.draw.rect(screen, (208, 197, 96), pole45)
        pygame.draw.rect(screen, (208, 197, 96), pole46)
        pygame.draw.rect(screen, (208, 197, 96), pole47)
        pygame.draw.rect(screen, (208, 197, 96), pole48)
        pygame.draw.rect(screen, (208, 197, 96), pole49)
        pygame.draw.rect(screen, (208, 197, 96), pole50)
        pygame.draw.rect(screen, (208, 197, 96), pole51)
        pygame.draw.rect(screen, (208, 197, 96), pole52)
        pygame.draw.rect(screen, (208, 197, 96), pole53)
        pygame.draw.rect(screen, (208, 197, 96), pole54)
        pygame.draw.rect(screen, (208, 197, 96), pole55)
        pygame.draw.rect(screen, (208, 197, 96), pole56)
        pygame.draw.rect(screen, (208, 197, 96), pole57)
        pygame.draw.rect(screen, (208, 197, 96), pole58)
        pygame.draw.rect(screen, (208, 197, 96), pole59)
        pygame.draw.rect(screen, (208, 197, 96), pole60)
        pygame.draw.rect(screen, (208, 197, 96), pole61)
        pygame.draw.rect(screen, (208, 197, 96), pole62)
        pygame.draw.rect(screen, (208, 197, 96), pole63)
        pygame.draw.rect(screen, (208, 197, 96), pole64)
        pygame.draw.rect(screen, (208, 197, 96), pole65)
        pygame.draw.rect(screen, (208, 197, 96), pole66)
        pygame.draw.rect(screen, (208, 197, 96), pole67)
        pygame.draw.rect(screen, (208, 197, 96), pole68)
        pygame.draw.rect(screen, (208, 197, 96), pole69)
        pygame.draw.rect(screen, (208, 197, 96), pole70)
        pygame.draw.rect(screen, (208, 197, 96), pole71)
        pygame.draw.rect(screen, (208, 197, 96), pole72)
        pygame.draw.rect(screen, (208, 197, 96), pole73)
        pygame.draw.rect(screen, (208, 197, 96), pole74)
        pygame.draw.rect(screen, (208, 197, 96), pole75)
        pygame.draw.rect(screen, (208, 197, 96), pole76)
        pygame.draw.rect(screen, (208, 197, 96), pole77)
        pygame.draw.rect(screen, (208, 197, 96), pole78)
        pygame.draw.rect(screen, (208, 197, 96), pole79)
        pygame.draw.rect(screen, (208, 197, 96), pole80)
        pygame.draw.rect(screen, (208, 197, 96), pole81)
        pygame.draw.rect(screen, (208, 197, 96), pole82)
        pygame.draw.rect(screen, (208, 197, 96), pole83)
        pygame.draw.rect(screen, (208, 197, 96), pole84)
        pygame.draw.rect(screen, (208, 197, 96), pole85)
        pygame.draw.rect(screen, (208, 197, 96), pole86)
        pygame.draw.rect(screen, (208, 197, 96), pole87)
        pygame.draw.rect(screen, (208, 197, 96), pole88)
        pygame.draw.rect(screen, (208, 197, 96), pole89)
        pygame.draw.rect(screen, (208, 197, 96), pole90)
        pygame.draw.rect(screen, (208, 197, 96), pole91)
        pygame.draw.rect(screen, (208, 197, 96), pole92)
        pygame.draw.rect(screen, (208, 197, 96), pole93)
        pygame.draw.rect(screen, (208, 197, 96), pole94)
        pygame.draw.rect(screen, (208, 197, 96), pole95)
        pygame.draw.rect(screen, (208, 197, 96), pole96)
        pygame.draw.rect(screen, (208, 197, 96), pole97)
        pygame.draw.rect(screen, (208, 197, 96), pole98)
        pygame.draw.rect(screen, (208, 197, 96), pole99)
        pygame.draw.rect(screen, (208, 197, 96), pole100)


        keys = pygame.key.get_pressed()

        if left_pressed:
            ruchy = ruchy + 1
            x -= 40
            if index_x != 0: 
                index_x = index_x - 1
                current=[index_x,index_y]
            left_pressed = False
        if right_pressed:
            ruchy = ruchy + 1
            x += 40
            if index_x != 8:
                index_x = index_x + 1
                current=[index_x,index_y]
            right_pressed = False
        if up_pressed:
            ruchy = ruchy + 1
            y -= 40
            if index_y != 9:
                index_y = index_y + 1
                current=[index_x,index_y]
            up_pressed = False
        if down_pressed:
            ruchy = ruchy + 1
            y += 40
            if index_y != 0:
                index_y = index_y - 1
                current=[index_x,index_y]
            down_pressed = False

        if x < 40:
            x = 55
        if x > 380:
            x = 375
        if y < 70:
            y = 75
        if y > 440:
            y = 435

        if current in pulapki:
            koniecgryrabbit.koniec_przegrana()
            return


        pygame.draw.rect(screen, (0, 0, 0), uwaga)

        if [index_x - 1, index_y]  in pulapki:             
            pygame.draw.rect(screen, (255, 45, 0), uwaga)
        if [index_x + 1, index_y]  in pulapki:
            pygame.draw.rect(screen, (255, 45, 0), uwaga)
        if [index_x, index_y - 1]  in pulapki:
            pygame.draw.rect(screen, (255, 45, 0), uwaga)
        if [index_x, index_y + 1]  in pulapki:
            pygame.draw.rect(screen, (255, 45, 0), uwaga)


        if index_x == 8 and index_y == 9:
            if ruchy < topka[9]['wynik']:
                koniecgryrabbit.koniec_top(ruchy)
                return
            else:
                koniecgryrabbit.koniec_zwykly(ruchy)
                return

        krolik = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(screen, (255, 255, 255), krolik)
        screen.blit(font_krolik.render("^..^", True, (0, 0, 0)), (krolik.x + 2, krolik.y + 2))


        screen.blit(font_text.render("Wróć", True, (255, 255, 255)), (przycisk_wroc.x + 20, przycisk_wroc.y + 12))
        screen.blit(font_text.render("Ruchy: "+str(ruchy), True, (255, 255, 255)), (liczba_ruchow.x + 20, liczba_ruchow.y + 12))
        screen.blit(font_uwaga.render(" ! ", True, (0, 0, 0)), (uwaga.x + 15, uwaga.y + 12))


        pygame.display.update()
