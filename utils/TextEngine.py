import pygame


def textRender(textString, textColor,size):
    font = pygame.font.Font("assets/fonts/kaph-regular.ttf", size)
    text = font.render(textString, True, textColor)
    return text
