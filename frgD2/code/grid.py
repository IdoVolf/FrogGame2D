import pygame
import json
import os
import sys
pygame.init()
windowSize = (624,624)

def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        basePath = sys._MEIPASS  
    except AttributeError:
        basePath = os.path.abspath(".")  

    return os.path.join(basePath, relativePath)

tiles = [pygame.image.load(resourcePath("tiles/dirt grass.png")),#0
         pygame.image.load(resourcePath("tiles/dirt.png")),#1
         pygame.image.load(resourcePath("tiles/sky.png")),#2
         pygame.image.load(resourcePath("tiles/lackOf2.png")),#3
         pygame.image.load(resourcePath("tiles/leaf.png")),#4
         pygame.image.load(resourcePath("tiles/bran.png")),#5
         pygame.image.load(resourcePath("tiles/sun.png")),#6
         pygame.image.load(resourcePath("tiles/clouds2.png")),#7
         pygame.image.load(resourcePath("tiles/stoneWall.png"))]#8

def getIndex(img):
    return tiles.index(img)

def getTile(i):
    return tiles[i]

def drawTile(window,tile,gLoc):
    window.blit(tile,(gLoc[0] * 48,gLoc[1] * 48))

def drawScreen(window,screen):
    for i in range(len(screen)):
        for j in range(len(screen[i])):
            drawTile(window,screen[i][j],(i,j))


def saveScreen(screen,counter):
    counter +=1
    save_path = f'screens/level{counter}.json'
    folder = os.path.dirname(save_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(save_path,"w") as f:
        json.dump(screen,f)
    return counter


def initBlank():
    screen = []
    tile = getTile(3)
    for i in range(13):
        newRow = []
        for j in range(13):
            newRow.append(tile)
        screen.append(newRow)
    return screen

def screenToIndexed(screens):
    newScreens = []
    for screen in screens:
        newList = []
        for i in screen:
            newRow = []
            for j in i:
                newRow.append(tiles.index(j))
            newList.append(newRow)
        newScreens.append(newList)
    return newScreens

def indexesToScreen(indexScreens):
    newScreens = []
    for indexScreen in indexScreens:
        screen = []
        for i in indexScreen:
            newRow = []
            for j in i:
                newRow.append(getTile(j))
            screen.append(newRow)
        newScreens.append(screen)
    return newScreens   

def mouseGridLoc():
    mousePos = pygame.mouse.get_pos()
    return(mousePos[0] //48,mousePos[1] // 48)

def drawText(window, gridLoc, text, size, color):
    font = pygame.font.SysFont(None, size)
    textSurface = font.render(text, True, color)
    x, y = gridLoc
    tileSize = 48  
    pos = (x * tileSize, y * tileSize)
    window.blit(textSurface, pos)



def loadLevel(levelNum):
    level = []
    levelPath = f"levels/level{levelNum}"
    for filename in os.listdir(levelPath):
        if filename.endswith(".json"):
            with open(os.path.join(levelPath, filename), "r") as f:
                indexScreens = json.load(f)
                level.append(indexesToScreen(indexScreens))
    return level
