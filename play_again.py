import pygame
import sys
from mainloop import main


def restart(win, winWidth, winHeight, text_to_display):
    """Function to restart the game and display Winner or Looser on the screen"""
    text = text_to_display
    xTextPosition = winWidth / 2 - text.get_width() / 2
    yTextPosition = winHeight / 2 - text.get_height() / 2
    widthText = text.get_width()
    heightText = text.get_height()
    pygame.draw.rect(win, (255, 255, 255), ((xTextPosition, 520 - 5),
                                            (widthText + 10, heightText + 10)))

    win.blit(text, (xTextPosition + 5, 520))

    pygame.display.flip()
    play_again = True
    while play_again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
                if xTextPosition - 5 <= xTextPosition + widthText + 5:
                    if yTextPosition - 5 <= yTextPosition + heightText + 5:
                        play_again = False
                        break
