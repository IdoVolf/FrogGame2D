import pygame
from grid import resourcePath
from grid import drawText
from button import Button
pygame.init()

def menu(window):
    playB = Button(264,252,48,48,"play",pygame.image.load(resourcePath("buttons/btn play.png")),pygame.image.load(resourcePath("buttons/btn play2.png")))
    bg = pygame.image.load(resourcePath("pics/menu bg.png"))
    run = True
    buttons = [playB]
    clock = pygame.time.Clock()

    while run:
        mousePos = pygame.mouse.get_pos()
        mousePressed = pygame.mouse.get_pressed()
        window.blit(bg,bg.get_rect())
        drawText(window,(0,2),"Turtle Wilds",162,(0,161,54))


        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return "game",False


        for btn in buttons:
            btn.draw(window)
            btn.update(mousePos)
            if(btn.is_clicked(mousePos,mousePressed)):
                if(btn.name == "play"):
                    return "selection",True
        pygame.display.update()
        clock.tick(60)