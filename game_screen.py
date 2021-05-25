import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('assets/img/background.jpg').convert()
image2 = pygame.image.load('assets/img/renan.png').convert()
image2 = pygame.transform.scale(image2, (70, 70))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))
    window.blit(image2, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados