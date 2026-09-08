# 🎵 Music Player

Um reprodutor de música simples feito em Python, usando a biblioteca `pygame.mixer` para tocar arquivos MP3 via terminal.

## Funcionalidades

- ▶️ Tocar música
- ⏸️ Pausar e retomar (resume)
- ⏹️ Parar a reprodução
- 🔊 Ajustar volume
- 📂 Detecção automática das músicas dentro da pasta `playlist/`
- 🔁 Avanço automático para a próxima música quando a atual termina

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

4. Use o menu no terminal para controlar a reprodução:
- `L` — tocar (play)
- `P` — pausar
- `R` — retomar
- `V` — ajustar volume
- `D` — desligar (stop)

## Estrutura do projeto

```
music-player/
├── playlist/       # arquivos .mp3
├── play.py         # lógica de reprodução (pygame.mixer)
├── player.py       # menu/interface via terminal
└── README.md
```

## Tecnologias

- Python 3
- pygame (`pygame.mixer`)

## Próximos passos

- Interface gráfica (tkinter)