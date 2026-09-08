from play import play 

while True:
    command = input("(P)lay or (S)top: ")
    if command.lower() == 'p':
        play()
    elif command.lower() == 's':
        break
    else:
        print(f'escolha uma opção valida: ')

