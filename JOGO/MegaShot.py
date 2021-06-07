# ===== Inicialização =====
# ----- Importa e inicia pacotes
 
 
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME_easy, GAME_hard, QUIT, WIN, LOSE, GAME_normal, GAME_hard_intro
from assets import BACKGROUND, GAME_NORMAL, GAME_HARD, SOUND_EASY, PIZZA, EPICO, VOCE_GANHOU, VOCE_PERDEU, YOU_LOSE, VOCE_TENTOU
from game_screen import game_screens, game_hard_intro, init_screen, winORlose_screen
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
        state = game_screens(window, BACKGROUND, SOUND_EASY, 5, 1000)
    elif state == GAME_normal:
        state = game_screens(window, GAME_NORMAL, PIZZA,3, 1500)
    elif state == GAME_hard:
        state = game_screens(window, GAME_HARD, EPICO,1, 2000)
    elif state == WIN:
        state = winORlose_screen(window, VOCE_GANHOU, VOCE_PERDEU)
    elif state == LOSE:
        state = winORlose_screen(window, YOU_LOSE, VOCE_TENTOU)
 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

