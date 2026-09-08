from play import * 

while True:
    command = input("selecione a opção desejada:"
    "(L)igar, (P)ausar, (R)etomar, ajustar (V)olume ou (D)esligar: ")
    if command.lower() == 'l':
        play()
    elif command.lower() == 'p':
        pause()
    elif command.lower() == 'd':
        stop()
        break
    elif command.lower() == 'r':
        unpause()
    elif command.lower() == 'v':
        volume()
    else:
        print(f'escolha uma opção valida: ')

