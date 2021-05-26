

import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME_easy, QUIT, GAME_hard_intro, GAME_normal


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    inits = pygame.image.load(path.join(IMG_DIR, 'init.jpg')).convert()
    inits_rect = inits.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        state = GAME_easy
                        running = False
                    if event.key == pygame.K_2:
                        state = GAME_normal
                        running = False
                    if event.key == pygame.K_3:
                        state = GAME_hard_intro
                        running = False


        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(inits, inits_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
