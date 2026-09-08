import pygame
import os
import time


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
    global tocando_algo
    pygame.mixer.music.stop()
    tocando_algo = False
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

def proxima_musica():
    global indice_atual
    indice_atual += 1
    if indice_atual >= len(playlist):
        indice_atual = 0
    play()
def verificar_fim_da_musica():
    while True:
        time.sleep(0.5) 
        if pygame.mixer.music.get_busy() == False and tocando_algo:
            proxima_musica()

