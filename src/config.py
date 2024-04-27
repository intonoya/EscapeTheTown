import random
import pygame
import sys


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

word_dictionary = ["queer", "music","python", "cat", "basketball", "football", "radio", "pizza", "sushi", "anime", "car", "capibara", "cherry"]
word_sport = ["football", "baseball", "golf", "basketball", "volleyball", "rugby", "tennis", "chess", "cricket", "hockey"]
word_animals = ["cat", "dog", "capibara", "lion", "bober", "lion", "fox", "shark", "dolphin", "elephant", "whale", "wolf"]
word_music = ["piano", "violin", "guitar", "radio", "vinyl", "microphone", "cello", "duduk", "saxophone", "ukulele"]
word_random = ["queer", "python", "cat", "radiohead", "icon", "memes", "zombie", "terminal", "samsung", "anime", "porsche", "cherry", "friend", "github"]
word_hard = ["rendezvous", "application", "honeymoon", "strawberry", "motorcycle", "astronaut", "genderfluid", "crescendo", "paparazzi", "bangladesh"]

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape The Town")

background_image = pygame.image.load("../other/menu.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (30, 144, 255)

font_color=(255, 255, 255)
font_size=36
background_color=(0, 0, 0)