

import pygame
import random
from os import path
from assets import load_assets, VOCE_TENTOU
from config import IMG_DIR, BLACK, FPS, GAME, QUIT


def lose_screen(screen):

    assets = load_assets()
    clock = pygame.time.Clock()
    assets[VOCE_TENTOU].play()
    # Carrega o fundo da tela de derrota
    lose = pygame.image.load(path.join(IMG_DIR, 'tela_gameover.png')).convert()
    lose_rect = lose.get_rect()

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

            if event.type == pygame.KEYUP:
                state = QUIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(lose, lose_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state