from config import *

def ft_menuM():
    pygame.mixer.music.load("../other/menu.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def ft_gameplayM():
    pygame.mixer.music.load("../other/gameplay.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def ft_winM():
    pygame.mixer.music.load("../other/win.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def ft_loseM():
    pygame.mixer.music.load("../other/lose.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def ft_button():
    pygame.mixer.music.load("../other/button.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0)