

import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, QUIT, GAME_hard
from assets import load_assets, FEIO, LUGAR


def game_hard_intro(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Carrega o fundo da tela inicial
    inits = pygame.image.load(path.join(IMG_DIR, 'game_hard_intro.png')).convert()
    inits_rect = inits.get_rect()
    feio = True
    lugar = True
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
                if event.key == pygame.K_SPACE:
                        state = GAME_hard
                        running = False
            if feio:
                assets[FEIO].play()
                feio = False
            if lugar:
                assets[LUGAR].play()
                lugar = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(inits, inits_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
