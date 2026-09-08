import play 
import threading

play.pygame.mixer.init()
thread = threading.Thread(target=play.verificar_fim_da_musica)
thread.start()

while True:    
    command = input("selecione a opção desejada:"
    "(L)igar, (P)ausar, (R)etomar, ajustar (V)olume, (S)altar a musica ou (D)esligar: ")
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
    elif command.lower() == 's':
        play.proxima_musica()
    else:
        print(f'escolha uma opção valida: ')

