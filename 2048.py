import pygame
import random
import sys
import math

pygame.init()

screenHeight, screenWidth = 400, 400
screen = pygame.display.set_mode((screenWidth, screenHeight))
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

def addNum(mat, score):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = random.choice([2, 4])
        score += 1
    return mat, score

backgrounds = {
    0: pygame.image.load("assets/blue/letter.png"),
    20: pygame.image.load("assets/brown.png"),
    40: pygame.image.load("assets/wood.png"),
    60: pygame.image.load("assets/marble.png"),
    80: pygame.image.load("assets/marble.png"),
    100: pygame.image.load("assets/marble.png"),
}

def getBg(sc):
    return backgrounds[math.floor(sc / 20.0) * 20]

board = startPos()

def main():
    global board
    score = 0
    
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
                        pygame.K_a: "l"
                    }
                    dir = directions[event.key]
                    board = gravCalc(collisionCalc(gravCalc(board, dir), dir), dir)
                    board, score = addNum(board, score)
        
        screen.fill("#000000")
        for i in range(4):
            for j in range(4):
                x, y = j * 100, i * 100
                if board[i][j] > 0:
                    screen.blit(pygame.transform.scale(getBg(score), (100, 100)), (x, y))
                    text = textRender(str(board[i][j]), "#ffffff", 20)
                    text_pos = center(text, 100, 100)
                    screen.blit(text, (x + text_pos[0], y + text_pos[1]))
        
        pygame.display.flip()
        clock.tick(fps)

main()
