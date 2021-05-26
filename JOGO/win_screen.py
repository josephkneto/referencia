import pygame
import random
from os import path
from assets import load_assets, VOCE_PERDEU
from config import IMG_DIR, BLACK, FPS, QUIT


def win_screen(screen):
    assets = load_assets()
    clock = pygame.time.Clock()
    assets[VOCE_PERDEU].play()
    inits = pygame.image.load(path.join(IMG_DIR, 'tela_win.png')).convert()
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

            if event.type == pygame.KEYUP:
                state = QUIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(inits, inits_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state