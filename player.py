import play 

play.pygame.mixer.init()
while True:
    print(f"get_busy: {play.pygame.mixer.music.get_busy()} | tocando_algo: {play.tocando_algo}")
    if play.pygame.mixer.music.get_busy() == False and play.tocando_algo:
        play.indice_atual += 1
        if play.indice_atual >= len(play.playlist):
            play.indice_atual = 0
        play.play()
    command = input("selecione a opção desejada:"
    "(L)igar, (P)ausar, (R)etomar, ajustar (V)olume ou (D)esligar: ")
    if command.lower() == 'l':
        play.play()
    elif command.lower() == 'p':
        play.pause()
    elif command.lower() == 'd':
        play.stop()
        break
    elif command.lower() == 'r':
        play.unpause()
    elif command.lower() == 'v':
        play.volume()
    else:
        print(f'escolha uma opção valida: ')

