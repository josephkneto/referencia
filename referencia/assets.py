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
PEW_SOUND = 'pew_sound'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert()
    assets[cas_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'castilho.png')).convert_alpha()
    assets[cas_IMG] = pygame.transform.scale(assets['cas_img'], (cas_WIDTH, cas_HEIGHT))
    assets[renan_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'renan.png')).convert_alpha()
    assets[renan_IMG] = pygame.transform.scale(assets['renan_img'], (renan_WIDTH, renan_HEIGHT))
    assets[BULLET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
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
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets