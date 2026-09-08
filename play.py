import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load('playlist/1.mp3')
    pygame.mixer.music.play()