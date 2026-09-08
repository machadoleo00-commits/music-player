import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load('playlist/1.mp3')
    pygame.mixer.music.play()
    print(f'Radio ligado')
def stop():
    pygame.mixer.music.stop()
    print(f'Radio desligado')
def pause():
    pygame.mixer.music.pause()
    print(f'Radio pausado')
def unpause():
    pygame.mixer.music.unpause()
    print(f'Radio retomado')
def volume():
    volume = float(input (f'escolha um volume de 0 a 10: ')) / 10
    pygame.mixer.music.set_volume(volume)
