import pygame
pygame.init()

class Button:
    def __init__(self, x, y, width, height, name, normalS, hoverS, text=None, textSize=36):
        self.rect = pygame.Rect(x, y, width, height)
        self.normal_sprite = pygame.transform.scale(normalS, (width, height))
        self.hover_sprite = pygame.transform.scale(hoverS, (width, height))
        self.image = self.normal_sprite
        self.name = name
        self.was_clicked = False

        # Text rendering
        self.text = text
        self.text_surface = None
        if text is not None:
            font = pygame.font.Font(None, textSize)
            self.text_surface = font.render(text, True, (0, 0, 0))  # Always black

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.text_surface:
            # Center the text on the button
            text_rect = self.text_surface.get_rect(center=self.rect.center)
            screen.blit(self.text_surface, text_rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image = self.hover_sprite
        else:
            self.image = self.normal_sprite

    def is_clicked(self, mouse_pos, mouse_pressed):
        clicked_now = self.rect.collidepoint(mouse_pos) and mouse_pressed[0]
        if clicked_now and not self.was_clicked:
            self.was_clicked = True
            return True
        if not mouse_pressed[0]:
            self.was_clicked = False
        return False
