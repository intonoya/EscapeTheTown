import pygame
import sys
from config import *

pygame.init()

button_width = 150
button_height = 50
button_spacing = 20
button_x = (screen_width - button_width) // 2
button_y = (screen_height - (5 * button_height + 4 * button_spacing)) // 2

button_texts = ["Sport", "Animals", "Music", "Random", "Hard"]

def draw_button():
    class Button:
        def __init__(self, x, y, width, height, text, text_color, color):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.text_color = text_color
            self.color = color

    def clear_screen():
        screen.blit(background_image, (0, 0))

    def open_new_window():
        new_window = pygame.Surface((200, 300))
        new_window.fill(WHITE)
        screen.blit(new_window, ((screen_width - 200) // 2, (screen_height - 300) // 2))
        pygame.display.flip()
        return new_window

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    buttons = [Button(button_x, button_y + i * (button_height + button_spacing), 
                      button_width, button_height, text, BLACK, BLUE) 
               for i, text in enumerate(button_texts)]

    while running:
        clear_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        if button.text == "New Game":
                            buttons = []
                            open_new_window()
                        elif button.text == "Exit":
                            pygame.quit()
                            sys.exit()

        for button in buttons:
            pygame.draw.rect(screen, button.color, button.rect)
            draw_text(button.text, pygame.font.Font(None, 24), BLACK, screen,
                      button.rect.x + button_width // 2, button.rect.y + button_height // 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

draw_button()
