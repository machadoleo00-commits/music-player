import pygame
import os

indice_atual = 0
playlist = []
tocando_algo = False

for mp3 in os.listdir('playlist'):
    if os.path.isfile('playlist/' + mp3) and mp3.endswith('.mp3'):
        playlist.append('playlist/' + mp3)



def play():
    global tocando_algo
    pygame.mixer.music.load(playlist[indice_atual])
    pygame.mixer.music.play()
    tocando_algo = True
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



