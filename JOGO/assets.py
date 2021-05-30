
import pygame
import os
from config import cas_WIDTH, cas_HEIGHT, renan_WIDTH, renan_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
cas_IMG = 'cas_img'
cas_IMG = 'cas_img'
renan_IMG = 'renan_img'
renan_IMG = 'renan_img'
BULLET_IMG = 'bullet_img'
EXPLOSION_ANIM = 'explosion_anim'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'
DESTROY_SOUND2 = 'destroy_sound2'
DESTROY_SOUND3 = 'destroy_sound3'
PEW_SOUND = 'pew_sound'
VOCE_TENTOU = 'voce_tentou'
YOU_LOSE = 'YOU_LOSE'
VOCE_PERDEU = 'voce_perdeu'
VOCE_GANHOU = 'voce_ganhou'
GAME_HARD = 'game_hard'
GAME_NORMAL = 'game_normal'
MATEI_TRES = 'matei_tres'
PIZZA = 'pizza'
EPICO = 'epico'
LUGAR = 'lugar'
FEIO = 'feio'
def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert()
    assets[cas_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'castilho.png')).convert_alpha()
    assets[cas_IMG] = pygame.transform.scale(assets['cas_img'], (cas_WIDTH, cas_HEIGHT))
    assets[renan_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'renan2.png')).convert_alpha()
    assets[renan_IMG] = pygame.transform.scale(assets['renan_img'], (renan_WIDTH, renan_HEIGHT))
    assets[BULLET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[YOU_LOSE] = pygame.image.load(os.path.join(IMG_DIR, 'tela_gameover.png')).convert()
    assets[VOCE_GANHOU] = pygame.image.load(os.path.join(IMG_DIR, 'tela_win.png')).convert()
    assets[GAME_HARD] = pygame.image.load(os.path.join(IMG_DIR, 'GAME_HARD.jpeg')).convert()
    assets[GAME_NORMAL] = pygame.image.load(os.path.join(IMG_DIR, 'GAME_normal.png')).convert()
    explosion_anim = []
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSION_ANIM] = explosion_anim
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musicafundo.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'casM.wav'))
    assets[DESTROY_SOUND2] = pygame.mixer.Sound(os.path.join(SND_DIR, 'casM2.wav'))
    assets[DESTROY_SOUND3] = pygame.mixer.Sound(os.path.join(SND_DIR, 'casM3.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'tome.wav'))
    assets[VOCE_TENTOU] = pygame.mixer.Sound(os.path.join(SND_DIR, 'vocetentou.wav'))
    assets[VOCE_PERDEU] = pygame.mixer.Sound(os.path.join(SND_DIR, 'voceperdeu.wav'))
    assets[VOCE_PERDEU].set_volume(200.0)
    assets[MATEI_TRES] = pygame.mixer.Sound(os.path.join(SND_DIR, 'mateitres.wav'))
    assets[PIZZA] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pizza.wav'))
    assets[PIZZA].set_volume(0.6)
    assets[EPICO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'epic.wav'))
    assets[EPICO].set_volume(0.4)
    assets[LUGAR] = pygame.mixer.Sound(os.path.join(SND_DIR, 'lugar.wav'))
    assets[FEIO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'feio.wav'))
    return assets