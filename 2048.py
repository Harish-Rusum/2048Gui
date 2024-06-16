import pygame
import random
import sys

pygame.init()

screenHeight, screenWidth = 460, 410
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()
fps = 60

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


def displayScore(surf, sc):
    scoreText = textRender(str(sc), "#ffffff", 25)
    textPos = center(scoreText, 410, 50)
    surf.blit(scoreText, textPos)


def addNum(mat, score):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = random.choice([2, 4])
        score += 1
    return mat, score


def getBg(sc):
    return pygame.transform.scale(
        pygame.image.load(f"assets/{sc}.png").convert_alpha(), (90, 90)
    )


board = startPos()


def main():
    global board, running
    score = 0
    yOffset = 50
    bg = pygame.transform.scale(
        pygame.image.load("assets/bg.png").convert_alpha(), (410, 410)
    )

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                dir = ""
                if event.key in [pygame.K_w, pygame.K_UP]:
                    dir = "u"
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    dir = "d"
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    dir = "r"
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    dir = "l"

                if event.key in [
                    pygame.K_w,
                    pygame.K_UP,
                    pygame.K_s,
                    pygame.K_DOWN,
                    pygame.K_d,
                    pygame.K_RIGHT,
                    pygame.K_a,
                    pygame.K_LEFT,
                ]:
                    addPreBoard = list(board)
                    board = gravCalc(collisionCalc(gravCalc(board, dir), dir), dir)
                    if addPreBoard != board:
                        board, score = addNum(board, score)

        screen.fill("#000000")
        screen.blit(bg, (0, 50))
        for i in range(4):
            for j in range(4):
                x, y = j * 100, i * 100 + yOffset
                if board[i][j] > 0:
                    screen.blit(getBg(board[i][j]), (x + 10, y + 10))
                    text = textRender(str(board[i][j]), "#000000", 20)
                    textPos = center(text, 90, 90)
                    screen.blit(text, (x + 10 + textPos[0], y + 10 + textPos[1]))
        displayScore(screen, score)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


main()
