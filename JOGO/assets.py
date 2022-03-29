
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
SOUND_EASY = 'sound_easy'
def load_images():
    images = {}
    images[BACKGROUND] = fetch_image('background.png').convert()
    images[cas_IMG] = fetch_image('castilho.png').convert_alpha()
    images[cas_IMG] = pygame.transform.scale(images['cas_img'], (cas_WIDTH, cas_HEIGHT))
    images[renan_IMG] = fetch_image('renan2.png').convert_alpha()
    images[renan_IMG] = pygame.transform.scale(images['renan_img'], (renan_WIDTH, renan_HEIGHT))
    images[BULLET_IMG] = fetch_image('laserRed16.png').convert_alpha()
    images[YOU_LOSE] = fetch_image('tela_gameover.png').convert()
    images[VOCE_GANHOU] = fetch_image('tela_win.png').convert()
    images[GAME_HARD] = fetch_image('GAME_HARD.jpeg').convert()
    images[GAME_NORMAL] = fetch_image('GAME_normal.png').convert()
    explosion_anim = []
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    images[EXPLOSION_ANIM] = explosion_anim
    images[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
def load_sounds():
    sounds = {}
    sounds[DESTROY_SOUND] = fetch_sound('casM.wav')
    sounds[DESTROY_SOUND2] = fetch_sound('casM2.wav')
    sounds[DESTROY_SOUND3] = fetch_sound('casM3.wav')
    sounds[PEW_SOUND] = fetch_sound('tome.wav')
    sounds[VOCE_TENTOU] = fetch_sound('vocetentou.wav')
    sounds[VOCE_PERDEU] = fetch_sound('voceperdeu.wav')
    sounds[VOCE_PERDEU].set_volume(200.0)
    sounds[MATEI_TRES] = fetch_sound('mateitres.wav')
    sounds[SOUND_EASY] = fetch_sound('musicafundo.wav')
    sounds[SOUND_EASY].set_volume(0.4)
    sounds[PIZZA] = fetch_sound('pizza.wav')
    sounds[PIZZA].set_volume(0.6)
    sounds[EPICO] = fetch_sound('epic.wav')
    sounds[EPICO].set_volume(0.4)
    sounds[LUGAR] = fetch_sound('lugar.wav')
    sounds[FEIO] = fetch_sound('feio.wav')
    return sounds

def fetch_sound(name):
    return pygame.mixer.Sound(os.path.join(SND_DIR, name))

def fetch_image(name):
    return pygame.image.load(os.path.join(IMG_DIR,name))
