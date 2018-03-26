# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


def main():
    (w, h) = (640, 480)  # 画面サイズ
    (x, y) = (w/2, h/2)
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(("NEKO GAME"))
    font = pygame.font.Font(None, 55)

    backimg = pygame.image.load("bg.png").convert()
    playerimg = pygame.image.load("player.png").convert_alpha()
    neko = 0

    screen.blit(backimg, (0, 0))

    while 1:
        pygame.display.update()
        pygame.time.delay(30)
        # screen.blit(playerimg, (x, y))
        screen.blit(playerimg, (random.randint(0, w), random.randint(0, h)))
        text = font.render("NEKO: " + str(neko), True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # pygame.draw.circle(screen, (255, 51, 51), (random.randint(0, h), random.randint(0, h)), 15, 0)
        neko += 1
        # screen.blit(text, [10, 10])
        print('NEKO: ' + str(neko))

        for event in pygame.event.get():
            '''if event.type == MOUSEMOTION:
                x, y = event.pos
                x -= playerimg.get_width() / 2
                y -= playerimg.get_height() / 2'''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
