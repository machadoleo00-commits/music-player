# 🎵 Music Player

Um reprodutor de música simples feito em Python, usando a biblioteca `pygame.mixer` para tocar arquivos MP3 e `tkinter` (com `ttk`) para a interface gráfica.

## Funcionalidades

- ▶️ Tocar música
- ⏸️ Pausar e retomar (resume)
- ⏹️ Parar a reprodução
- 🔊 Ajustar volume (via slider)
- ⏭️ Pular para a próxima música
- 📂 Detecção automática das músicas dentro da pasta `playlist/`
- 🔁 Avanço automático para a próxima música quando a atual termina (checagem em segundo plano com threading)
- 🖥️ Interface gráfica com widgets modernos (ttk), botões organizados em grade e slider de volume
- 🎧 Exibição em tempo real do nome da música que está tocando
- 🛑 Encerramento seguro: fechar a janela para a música e finaliza o programa corretamente

## Como rodar

1. Instale a dependência:
```
pip install pygame
```

2. Coloque seus arquivos `.mp3` dentro da pasta `playlist/`.

3. Entre na pasta do projeto e rode:
```
cd music-player
python player.py
```

4. Uma janela vai abrir com os seguintes controles:
- Ligar
- Pausar
- Retomar
- Pular faixa
- Desligar
- Slider de volume
- Nome da música atual exibido na tela

## Estrutura do projeto

```
music-player/
├── playlist/       # arquivos .mp3
├── play.py         # lógica de reprodução (pygame.mixer)
├── janela.py       # interface gráfica (tkinter/ttk)
├── player.py       # arquivo principal, une thread + janela
└── README.md
```

## Tecnologias

- Python 3
- pygame (`pygame.mixer`)
- tkinter / ttk (interface gráfica)
- threading (checagem automática de fim de música)