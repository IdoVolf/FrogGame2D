import pygame
pygame.init()

class Player:
    def __init__(self, pixelPos, idleFrames,moveF):
        self.frames = idleFrames
        self.idleF = idleFrames
        self.moveF = moveF
        self.currentFrame = 0
        self.animationSpeed = 200
        self.lastAnimTime = pygame.time.get_ticks()
        self.grounded = False
        self.canJump = True
        self.lookingRight = True
        self.pixelPos = pixelPos
        self.width = 48
        self.height = 48
        self.moving = False
        self.jumping = False
        self.jumpCounter = 0
        self.jumpHeight = 125  # Total pixels to jump
        self.jumpSpeed = 5  # Pixels per frame




    def getTileAt(self, typeMatrix, pixelX, pixelY):
        gridX = int(pixelX // 48)
        gridY = int(pixelY // 48)
        if 0 <= gridX < len(typeMatrix) and 0 <= gridY < len(typeMatrix[0]):
            return typeMatrix[gridX][gridY]
        return 1

    def getGridPos(self):
        return int(self.pixelPos[0] // 48), int(self.pixelPos[1] // 48)

    def draw(self, window,bool =True):
        if(bool):
            now = pygame.time.get_ticks()
            if now - self.lastAnimTime > self.animationSpeed:
                self.currentFrame = (self.currentFrame + 1) % len(self.frames)
                self.lastAnimTime = now

            frame = self.frames[self.currentFrame]
            if not self.lookingRight:
                frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, self.pixelPos)
        else:
            return

    def update(self, typeMatrix):
        keys = pygame.key.get_pressed()

        # Movement
        rightT = self.getTileAt(typeMatrix, self.pixelPos[0]+self.width, self.pixelPos[1] + self.height - 8)
        leftT = self.getTileAt(typeMatrix, self.pixelPos[0], self.pixelPos[1] + self.height - 8)

        if keys[pygame.K_a] and leftT not in [1, 0]:
            self.moving = True
            self.pixelPos = (self.pixelPos[0] - 4, self.pixelPos[1])
            self.lookingRight = False
        if keys[pygame.K_d] and rightT not in [1, 0]:
            self.moving = True
            self.pixelPos = (self.pixelPos[0] + 4, self.pixelPos[1])
            self.lookingRight = True

        # Start jump
        if keys[pygame.K_SPACE] and self.grounded and not self.jumping:
            self.jumping = True
            self.jumpCounter = 0
            self.grounded = False

        # Jumping logic
        if self.jumping:
            topLeft = self.getTileAt(typeMatrix, self.pixelPos[0] + 5, self.pixelPos[1] - self.jumpSpeed)
            topRight = self.getTileAt(typeMatrix, self.pixelPos[0] + self.width - 5, self.pixelPos[1] - self.jumpSpeed)

            if topLeft in [1, 0] or topRight in [1, 0]:
                self.jumping = False  # Bonk ceiling
            else:
                self.pixelPos = (self.pixelPos[0], self.pixelPos[1] - self.jumpSpeed)
                self.jumpCounter += self.jumpSpeed

                if self.jumpCounter >= self.jumpHeight:
                    self.jumping = False

        # Gravity (only applies when not jumping)
        if not self.jumping:
            below = self.getTileAt(typeMatrix, self.pixelPos[0] + self.width // 2, self.pixelPos[1] + self.height)

            if below not in [1, 0]:  # Air
                self.grounded = False
                self.pixelPos = (self.pixelPos[0], self.pixelPos[1] + 6)
            else:
                self.grounded = True

        # Animation
        if not any(keys):
            self.moving = False
            self.jumping = False
            self.frames = self.idleF
        elif self.moving and self.frames != self.moveF:
            self.frames = self.moveF
