# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, WIN, LOSE
from init_screen import init_screen
from game_screen import game_screen
import os

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mega Shot')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == WIN:
        state == QUIT
    elif state == LOSE:
        state == QUIT
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

