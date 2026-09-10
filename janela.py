import tkinter as tk
from tkinter import ttk
import play



def criar_janela():
    global janela_principal
    janela_principal = tk.Tk()
    janela_principal.title('Rádio')
    janela_principal.geometry('600x400')
    frame_botoes = ttk.Frame(janela_principal)
    frame_botoes.pack(pady=10)

    global label_musica_atual
    label_musica_atual = ttk.Label(janela_principal, text="Nenhuma música tocando")
    label_musica_atual.pack(pady=10)
    

    botao_play = ttk.Button(frame_botoes, text="Ligar", command=play.play)
    botao_play.grid(row=1, column=1, padx=5)
    botao_stop = ttk.Button(frame_botoes, text="desligar", command=play.stop)
    botao_stop.grid(row=1, column=5, padx=5)
    botao_pause = ttk.Button(frame_botoes, text="pausar", command=play.pause)
    botao_pause.grid(row=4, column=2, padx=5)
    botao_unpause = ttk.Button(frame_botoes, text="retomar", command=play.unpause)
    botao_unpause.grid(row=4, column=3, padx=5)
    botao_proxima_musica = ttk.Button(frame_botoes, text="pular faixa", command=play.proxima_musica)
    botao_proxima_musica.grid(row=4, column=4, padx=5)
    botao_volume = ttk.Scale(janela_principal,from_=0, to=10, orient='horizontal', command=play.volume)
    botao_volume.pack(pady=5)
    janela_principal.protocol("WM_DELETE_WINDOW", play.fechar_programa)

    janela_principal.mainloop()


