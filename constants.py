import pygame

pygame.init()
spriteSize = 30
winWidth, winHeight = 510, 550
back = pygame.Surface((winWidth, winHeight))
music = pygame.mixer.music.load("music/soundbay_Epic_Movie.wav")

maze_1 = ("mmmmmmmmmmmmmmmmm\n"
          "m0000mmm0000mm0mm\n"
          "mmmm0m000mm0mm0mm\n"
          "mm0m0mmm0mm0m000m\n"
          "mm0000000mm0m0m0m\n"
          "mmmmmmmmmmm0m0m0m\n"
          "m000mm000000m0m0m\n"
          "m0m0m00mmmmmm0m0m\n"
          "mm00mm0mm00000m0m\n"
          "mm0mmm0m00mmmmm0m\n"
          "mm00000m0mm00000m\n"
          "mmmm0mmm0mm0m00mm\n"
          "mmmm0m000m00mm0mm\n"
          "m0000m0mmmm0mm0mm\n"
          "m0mm0000mmm000mmm\n"
          "mmmmmmmmmmmmm00am\n"
          "mmmmmmmmmmmmmmmmm")

maze_2 = ("mmmmmmmmmmmmmmmmm\n"
          "m0mmmmmmmmm0mmmmm\n"
          "m00000000mm0000mm\n"
          "mm0m0mmm0mm0m000m\n"
          "m00000000mm0m0m0m\n"
          "mmmmmm0mmmm0m0m0m\n"
          "m000mm000000m0m0m\n"
          "m0m0m00mmmmmm0m0m\n"
          "mm00mm0mm00000m0m\n"
          "mm0mmm0000mmmmm0m\n"
          "mm00000m0mm00000m\n"
          "mmmm0mmm0000m00mm\n"
          "mmmm0m000m00mm0mm\n"
          "m0000m0mmmm0mm0mm\n"
          "m0mm0000mmmmm0mmm\n"
          "mmmmm0000000000am\n"
          "mmmmmmmmmmmmmmmmm")
