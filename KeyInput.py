import pygame, sys
from pygame.locals import *

class KeyInput():
    def __init__(self, nm):
        self.name = nm
    def getKeyValue(self, k):
        if k[K_a]:
            return 'a'
        elif k[K_b]:
            return 'b'
        elif k[K_c]:
            return 'c'
        elif k[K_d]:
            return 'd'
        elif k[K_e]:
            return 'e'
        elif k[K_f]:
            return 'f'
        elif k[K_g]:
            return 'g'
        elif k[K_h]:
            return 'h'
        elif k[K_i]:
            return 'i'
        elif k[K_j]:
            return 'j'
        elif k[K_k]:
            return 'k'
        elif k[K_l]:
            return 'l'
        elif k[K_m]:
            return 'm'
        elif k[K_n]:
            return 'n'
        elif k[K_o]:
            return 'o'
        elif k[K_p]:
            return 'p'
        elif k[K_q]:
            return 'q'
        elif k[K_r]:
            return 'r'
        elif k[K_s]:
            return 's'
        elif k[K_t]:
            return 't'
        elif k[K_u]:
            return 'u'
        elif k[K_v]:
            return 'v'
        elif k[K_w]:
            return 'w'
        elif k[K_x]:
            return 'x'
        elif k[K_y]:
            return 'y'
        elif k[K_z]:
            return 'z'
        elif k[K_0]:
            return '0'
        elif k[K_1]:
            return '1'
        elif k[K_2]:
            return '2'
        elif k[K_3]:
            return '3'
        elif k[K_4]:
            return '4'
        elif k[K_5]:
            return '5'
        elif k[K_6]:
            return '6'
        elif k[K_7]:
            return '7'
        elif k[K_8]:
            return '8'
        elif k[K_9]:
            return '9'
        else:
            return 'none'
  
  
