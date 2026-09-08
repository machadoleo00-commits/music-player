import play 
import threading
import janela

play.pygame.mixer.init()
thread = threading.Thread(target=play.verificar_fim_da_musica)
thread.start()

janela.criar_janela()
