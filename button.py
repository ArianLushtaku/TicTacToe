import pygame

pygame.font.init()


class Button:
    def __init__(self, x, y, width, height, text, bg_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.highlighted = False
        self.font = pygame.font.Font("freesansbold.ttf", 24)

    def draw(self, surface):
        button_color = self.bg_color
        outline_color = pygame.Color('black')
        outline_thickness = 3 if self.highlighted else 1

        pygame.draw.rect(surface, button_color, self.rect)
        pygame.draw.rect(surface, outline_color, self.rect, outline_thickness)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)