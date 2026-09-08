import tkinter as tk
import play

def criar_janela():
    janela = tk.Tk()

    botao_play = tk.Button(janela, text="Ligar", command=play.play)
    botao_play.pack()
    botao_stop = tk.Button(janela, text="desligar", command=play.stop)
    botao_stop.pack()
    botao_pause = tk.Button(janela, text="pausar", command=play.pause)
    botao_pause.pack()
    botao_unpause = tk.Button(janela, text="retomar", command=play.unpause)
    botao_unpause.pack()
    botao_proxima_musica = tk.Button(janela, text="pular faixa", command=play.proxima_musica)
    botao_proxima_musica.pack()
    botao_volume = tk.Scale(janela,from_=0, to=10, orient='horizontal', command=play.volume)
    botao_volume.pack()

    janela.mainloop()