import pygame
from grid import resourcePath
from grid import drawText
from button import Button
pygame.init()

def selec(window):
    bg = pygame.image.load(resourcePath("pics/menu bg.png"))
    run = True
    buttons = []
    x =48
    for i in range(10):
        x += 48
        btn1 = Button(x,324,48,48,f"{i +1}",pygame.image.load(resourcePath("buttons/blnk1.png")),pygame.image.load(resourcePath("buttons/blnk2.png"),f"1"),f"{i+1}",36)
        buttons.append(btn1)
    clock = pygame.time.Clock()

    while run:
        mousePos = pygame.mouse.get_pos()
        mousePressed = pygame.mouse.get_pressed()
        window.blit(bg,bg.get_rect())
        drawText(window,(0,2),"Turtle Wilds",162,(0,161,54))


        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return "game",1,True,False


        for btn in buttons:
            btn.draw(window)
            btn.update(mousePos)
            if(btn.is_clicked(mousePos,mousePressed)):
                    return "game",int(btn.name),True,True
        pygame.display.update()
        clock.tick(60)