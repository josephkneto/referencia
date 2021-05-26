import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, WIN, LOSE, QUIT
from assets import load_assets, DESTROY_SOUND2, BOOM_SOUND, GAME_NORMAL, SCORE_FONT, PIZZA
from sprites import renan, cas, Bullet, Explosion, bulleta

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
                assets[DESTROY_SOUND2].play()
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
