import pygame
import random
import sys

pygame.init()

screenHeight,screenWidth = 400,400
screen = pygame.display.set_mode((screenWidth,screenHeight))
running = True


from scripts.gravity import gravCalc
from scripts.collision import collisionCalc
from utils.CenteringEngine import center
from utils.TextEngine import textRender


def startPos():
    mat = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    mat[random.choice([0,1,2,3])][random.choice([0,1,2,3])] = random.choice([2,4])
    
    i,j = 0,0
    while mat[i][j] != 0:
        i,j = random.choice([0,1,2,3]),random.choice([0,1,2,3])
    mat[i][j] = random.choice([2,4])
    return mat

def addNum(mat):
    i,j = 0,0
    while mat[i][j] != 0:
        i,j = random.choice([0,1,2,3]),random.choice([0,1,2,3])
    mat[i][j] = random.choice([2,4])
    return mat

board = startPos()
def main():
    global board
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_w:
                    board = gravCalc(collisionCalc(gravCalc(board, "u"),"u"),"u")
                    board = addNum(board)
                if event.key == pygame.K_s:
                    board = gravCalc(collisionCalc(gravCalc(board, "d"),"d"),"d")
                    board = addNum(board)
                if event.key == pygame.K_d:
                    board = gravCalc(collisionCalc(gravCalc(board, "r"),"r"),"r")
                    board = addNum(board)
                if event.key == pygame.K_a:
                    board = gravCalc(collisionCalc(gravCalc(board, "l"),"l"),"l")
                    board = addNum(board)
        
            screen.fill("#000000")
            x,y = 0,0
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[j][i] > 0:
                        screen.blit(pygame.transform.scale(pygame.image.load("assets/wood.png").convert_alpha(),(100,100)),(x,y))
                        text = textRender(str(board[j][i]),"#ffffff",40)
                        screen.blit(text, (center(text,100, 100)[0]+x,center(text, 100, 100)[1]+y))
                    y += 100
                x += 100
                y = 0
        pygame.display.flip()
main()
