import pygame
import random
import sys

pygame.init()

screenHeight, screenWidth = 460, 410
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()
fps = 60
running = True

from scripts.gravity import gravCalc
from scripts.collision import collisionCalc
from utils.CenteringEngine import center
from utils.TextEngine import textRender

def startPos():
    mat = [[0 for _ in range(4)] for _ in range(4)]
    for _ in range(2):
        while True:
            i, j = random.choice(range(4)), random.choice(range(4))
            if mat[i][j] == 0:
                mat[i][j] = random.choice([2, 4])
                break
    return mat

def displayLevelup(sc, surf, pos):
    for i in range(sc):
        pygame.draw.circle(surf, (255, 255, 255), (pos[0] + (i // 2), pos[1]), 10)
    if sc == 0:
        pygame.draw.circle(surf, (255, 255, 255), pos, 10)

def addNum(mat, score):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = random.choice([2, 4, 8])
        score += 1
    return mat, score

def getBg(sc):
    return pygame.transform.scale(
            pygame.image.load(f"assets/{sc}.png").convert_alpha(), (90, 90)
    )

board = startPos()

def main():
    global board
    score = 0
    yOffset = 50
    bg = pygame.transform.scale(
            pygame.image.load("assets/bg.png").convert_alpha(), (410,410)
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key in (pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a):
                    directions = {
                        pygame.K_w: "u",
                        pygame.K_s: "d",
                        pygame.K_d: "r",
                        pygame.K_a: "l",
                    }
                    dir = directions[event.key]
                    board = gravCalc(collisionCalc(gravCalc(board, dir), dir), dir)
                    board, score = addNum(board, score)

        screen.fill("#000000")
        screen.blit(bg, (0,50))
        for i in range(4):
            for j in range(4):
                x, y = j * 100, i * 100 + yOffset
                if board[i][j] > 0:
                    screen.blit(getBg(board[i][j]), (x + 10, y + 10))
                    text = textRender(str(board[i][j]), "#000000", 20)
                    textPos = center(text, 90, 90)
                    screen.blit(text, (x + 10 + textPos[0], y + 10 + textPos[1]))
        
        displayLevelup(score, screen, (20, 25))
        pygame.display.flip()
        clock.tick(fps)

main()
