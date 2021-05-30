 
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, WIN, LOSE, QUIT, GAME_hard, IMG_DIR, GAME_easy, GAME_hard_intro, GAME_normal
from assets import load_assets, DESTROY_SOUND, BACKGROUND, SCORE_FONT, MATEI_TRES, DESTROY_SOUND2, DESTROY_SOUND3,BOOM_SOUND, GAME_HARD, EPICO, GAME_NORMAL, PIZZA, FEIO, LUGAR, VOCE_PERDEU, VOCE_TENTOU
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
 
def game_easy(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
 
    assets = load_assets()
 
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_cas = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cas'] = all_cas
    groups['all_bullets'] = all_bullets
 
    # Criando o jogador
    player = renan(groups, assets)
    all_sprites.add(player)
    castilho = cas(assets)
    all_sprites.add(castilho)
    all_cas.add(castilho)
 
 
    PLAYING = 1
    run = True
    state = PLAYING
    keys_down = {}
    score = 0
    lives = 5
    soundplay = True
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
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
                    assets[DESTROY_SOUND].play()
                elif x == 1:
                    assets[DESTROY_SOUND2].play()
                elif x == 2:
                    assets[DESTROY_SOUND3].play()
                m = cas(assets)
                all_sprites.add(m)
                all_cas.add(m)
 
                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(mcas.rect.center, assets)
                all_sprites.add(explosao)
 
                # Ganhou pontos!
                score += 100
                if score == 1000:
                    state = WIN
                    run = False
            if len(bulleta) == 1:
                lives = 4
            if len(bulleta) == 2:
                lives = 3
            if len(bulleta) == 3:
                lives = 2
                if soundplay:
                    assets[MATEI_TRES].play()
                    soundplay = False
            if len(bulleta) == 4:
                lives = 1
            if len(bulleta) == 5:
                lives = 0
    
            if lives == 0:
                state = LOSE
                run = False
 
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
 
        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
 
        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
 
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state
 
def game_hard(window):
 
    clock = pygame.time.Clock()
 
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_cas = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cas'] = all_cas
    groups['all_bullets'] = all_bullets
 
    # Criando o jogador
    player = renan(groups, assets)
    all_sprites.add(player)
    castilho = cas(assets)
    all_sprites.add(castilho)
    all_cas.add(castilho)
 
 
    PLAYING = 1
    run = True
    state = PLAYING
    keys_down = {}
    score = 0
    lives = 1
 
    # ===== Loop principal =====
    assets[EPICO].play(loops=-1)
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
                    assets[DESTROY_SOUND].play()
                elif x == 1:
                    assets[DESTROY_SOUND2].play()
                elif x == 2:
                    assets[DESTROY_SOUND3].play()
                m = cas(assets)
                all_sprites.add(m)
                all_cas.add(m)
 
                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(mcas.rect.center, assets)
                all_sprites.add(explosao)
 
                # Ganhou pontos!
                score += 100
                if score == 2000:
                    state = WIN
                    run = False
            if len(bulleta) == 1:
                lives = 0
    
            if lives == 0:
                state = LOSE
                run = False
 
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[GAME_HARD], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
 
        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
 
        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
 
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state
 
def game_normal(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
 
    assets = load_assets()
 
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_cas = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cas'] = all_cas
    groups['all_bullets'] = all_bullets
 
    # Criando o jogador
    player = renan(groups, assets)
    all_sprites.add(player)
    castilho = cas(assets)
    all_sprites.add(castilho)
    all_cas.add(castilho)
 
 
    PLAYING = 1
    run = True
    state = PLAYING
    keys_down = {}
    score = 0
    lives = 3
 
    # ===== Loop principal =====
    assets[PIZZA].play(loops=-1)
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
                    assets[DESTROY_SOUND].play()
                elif x == 1:
                    assets[DESTROY_SOUND2].play()
                elif x == 2:
                    assets[DESTROY_SOUND3].play()
                m = cas(assets)
                all_sprites.add(m)
                all_cas.add(m)
 
                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(mcas.rect.center, assets)
                all_sprites.add(explosao)
 
                # Ganhou pontos!
                score += 100
                if score == 1500:
                    state = WIN
                    run = False
            if len(bulleta) == 1:
                lives = 2
            if len(bulleta) == 2:
                lives = 1
            if len(bulleta) == 3:
                lives = 0
    
            if lives == 0:
                state = LOSE
                run = False
 
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[GAME_NORMAL], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
 
        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
 
        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
 
        pygame.display.update()  # Mostra o novo frame para o jogador
    return state
 
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

