 
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, WIN, LOSE, QUIT, GAME_hard, IMG_DIR, GAME_easy, GAME_hard_intro, GAME_normal
from assets import load_sounds, load_images, DESTROY_SOUND, SCORE_FONT, MATEI_TRES, DESTROY_SOUND2, DESTROY_SOUND3, FEIO, LUGAR, VOCE_PERDEU, VOCE_TENTOU

from sprites import renan, cas, Bullet, Explosion, bulleta
import random
from os import path
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
 
def game_screens(window, image, som, vida, ganhou):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
 
    sounds = load_sounds()
    images = load_images()
 
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_cas = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cas'] = all_cas
    groups['all_bullets'] = all_bullets
 
    # Criando o jogador
    player = renan(groups, images)
    all_sprites.add(player)
    castilho = cas(images)
    all_sprites.add(castilho)
    all_cas.add(castilho)
 
 
    PLAYING = 1
    run = True
    state = PLAYING
    keys_down = {}
    score = 0
    soundplay = True
    # ===== Loop principal =====
    sounds[som].play(loops=-1)
    while run: #rodando
        clock.tick(FPS)
 
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT #rodando = False
                run = False
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
 
 
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()
 
        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_cas, all_bullets, True, True, pygame.sprite.collide_mask)
            for mcas in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                x = random.randint(0, 2)
                if x == 0:
                    sounds[DESTROY_SOUND].play()
                elif x == 1:
                    sounds[DESTROY_SOUND2].play()
                elif x == 2:
                    sounds[DESTROY_SOUND3].play()
                m = cas(images)
                all_sprites.add(m)
                all_cas.add(m)
 
                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(mcas.rect.center, images)
                all_sprites.add(explosao)
 
                # Ganhou pontos!
                score += 100
                if score == ganhou:
                    state = WIN
                    run = False
            #game_easy
            if len(bulleta) == 1 and vida == 5:
                vida = 4
            if len(bulleta) == 2 and vida == 4:
                vida = 3
            if len(bulleta) == 3 and vida == 3:
                vida = 2
                if soundplay:
                    sounds[MATEI_TRES].play()
                    soundplay = False
            if len(bulleta) == 4 and vida == 2:
                vida = 1
            if len(bulleta) == 5 and vida == 1:
                vida = 0
            #game_normal
            if len(bulleta) == 1 and vida == 3:
                vida = 2
            if len(bulleta) == 2 and vida == 2:
                vida = 1
            if len(bulleta) == 3 and vida == 1:
                vida = 0
            #game_hard
            if len(bulleta) == 1 and vida == 1:
                vida = 0
    
            if vida == 0:
                state = LOSE
                run = False
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(images[image], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
 
        # Desenhando o score
        text_surface = images[SCORE_FONT].render("{:08d}".format(score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
 
        # Desenhando as vidas
        text_surface = images[SCORE_FONT].render(chr(9829) * vida, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
 
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state
 
def game_hard_intro(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    sounds = load_sounds()
    images = load_images()
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
                    sounds[FEIO].stop()
                    sounds[LUGAR].stop()
                    state = GAME_hard
                    running = False
            if feio:
                sounds[FEIO].play()
                feio = False
            if lugar:
                sounds[LUGAR].play()
                lugar = False
 
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(inits, inits_rect)
 
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
 
    return state
 
def winORlose_screen(screen, imagem, som):
    sounds = load_sounds()
    images = load_images()
    clock = pygame.time.Clock()
    sounds[som].play()
 
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
        screen.blit(images[imagem], (0, 0))
 
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
 
    return state