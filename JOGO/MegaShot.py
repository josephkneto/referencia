# ===== Inicialização =====
# ----- Importa e inicia pacotes
 
 
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME_easy, GAME_hard, QUIT, WIN, LOSE, GAME_normal, GAME_hard_intro
from game_screen import game_hard, game_normal, game_easy, game_hard_intro, init_screen, win_screen, lose_screen
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
    elif state == GAME_hard_intro:
        state = game_hard_intro(window)
    elif state == GAME_easy:
        state = game_easy(window)
    elif state == GAME_normal:
        state = game_normal(window)
    elif state == GAME_hard:
        state = game_hard(window)
    elif state == WIN:
        state = win_screen(window)
    elif state == LOSE:
        state = lose_screen(window)
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

