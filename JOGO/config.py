from os import path
 
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')
 
# Dados gerais do jogo.
WIDTH = 700
HEIGHT = 400
FPS = 60 # Frames por segundo
 
# Define tamanhos
cas_WIDTH = 80
cas_HEIGHT = 60
renan_WIDTH = 90
renan_HEIGHT = 68
 
# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
 
# Estados para controle do fluxo da aplicação
INIT = 0
GAME_easy = 1
WIN = 2
QUIT = 3
LOSE = 4
GAME_hard = 5
GAME_normal = 6
GAME_hard_intro = 7
