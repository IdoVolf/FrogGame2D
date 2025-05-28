import pygame
pygame.init()
from grid import drawScreen
from grid import loadLevel
from grid import getIndex
from grid import resourcePath
from grid import screenToIndexed
from grid import mouseGridLoc
from menu import menu
from trt import Player
from levs import selec
windowSize = (624,624)
window = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()
run = True
level = loadLevel(1)
currentScreen = 0
idleF = [pygame.image.load("idleCycle/pixil-layer-0.png"),pygame.image.load("idleCycle/pixil-layer-1.png"),
         pygame.image.load("idleCycle/pixil-layer-2.png"),pygame.image.load("idleCycle/pixil-layer-3.png")]

moveF = [pygame.image.load(resourcePath("moveCycle/pixil-layer-0.png")),pygame.image.load(resourcePath("moveCycle/pixil-layer-1.png")),
         pygame.image.load(resourcePath("moveCycle/pixil-layer-2.png")),pygame.image.load(resourcePath("moveCycle/pixil-layer-3.png"))]

trt = Player((0,0),idleF,idleF)
gameState = "menu"
drawP = True

def checkScreenTransition(player, levelList, currentScreen):
    screenWidth = 624

    # Right edge
    if player.pixelPos[0] + 48 >= screenWidth:
        if currentScreen + 1 < len(levelList):
            currentScreen += 1
            player.pixelPos = (0, player.pixelPos[1])
        else:
            player.pixelPos = (screenWidth - player.width, player.pixelPos[1])

    # Left edge
    elif player.pixelPos[0] < 0:
        if currentScreen - 1 >= 0:
            currentScreen -= 1
            newWidth = len(levelList[currentScreen][0]) * 48
            player.pixelPos = (newWidth - player.width, player.pixelPos[1])
        else:
            player.pixelPos = (0, player.pixelPos[1])

    return currentScreen




while run:
    if(gameState == "menu"):
        gameState,run = menu(window)
    elif gameState == "selection":
        gameState,level,drawP,run = selec(window)
        level = loadLevel(level)
    elif(gameState == "game"):
        mousePos = pygame.mouse.get_pos()
        typeMatrixs = screenToIndexed(level[currentScreen])
        typeMatrixs1 = typeMatrixs[0]

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                currentScreen =0
                trt.pixelPos = (0,0)
                drawP = False
                gameState = "menu"
            


        for  screen in level[currentScreen]:
            drawScreen(window,screen)

        trt.draw(window,drawP)
        trt.update(typeMatrixs1)
        if(trt.pixelPos[1] >=576):
            trt.pixelPos = (0,0)
        currentScreen = checkScreenTransition(trt, level, currentScreen)


        pygame.display.update()
        clock.tick(60)  