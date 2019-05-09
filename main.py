import sys
from constants import *
from player_class import Macgyver
from maze_class import MazeCreation


def restart(win, winWidth, winHeight, text_to_display):
    """Function to restart the game and display Winner or Looser on the screen"""
    text = text_to_display
    xTextPosition = winWidth / 2 - text.get_width() / 2
    yTextPosition = winHeight / 2 - text.get_height() / 2
    widthText = text.get_width()
    heightText = text.get_height()
    pygame.draw.rect(win, (255, 255, 255), ((xTextPosition / 2 - text.get_width() / 2, 520 - 5),
                                            (widthText + 10, heightText + 10)))

    win.blit(text, (xTextPosition / 2 - text.get_width() / 2, 520))

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


def main():
    """Main Loop of the game"""
    win = pygame.display.set_mode((winWidth, winHeight))
    score = 0
    pygame.display.set_caption('Macgyver')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('helvetica', 30)

    all_sprites = pygame.sprite.Group()
    walls_sprites = pygame.sprite.Group()
    floor_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    pick_sprites = pygame.sprite.Group()

    maze = MazeCreation(all_sprites, walls_sprites, floor_sprites, enemy_sprites, pick_sprites)
    maze.draw()

    player = Macgyver(45, 45, walls_sprites)
    all_sprites.add(player)

    game = False
    while not game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.macgyverVelocity.y = -3
        elif keys[pygame.K_DOWN]:
            player.macgyverVelocity.y = 3
        else:
            player.macgyverVelocity.y = 0

        if keys[pygame.K_LEFT]:
            player.macgyverVelocity.x = -3
        elif keys[pygame.K_RIGHT]:
            player.macgyverVelocity.x = 3
        else:
            player.macgyverVelocity.x = 0

        pick_objects = pygame.sprite.spritecollide(player, pick_sprites, True)

        if pick_objects:
            pick_sprites.clear(win, back)
            score += 1

        if score != 3 and pygame.sprite.spritecollideany(player, enemy_sprites):
            pygame.sprite.spritecollide(player, enemy_sprites, False)
            text = font.render('Looser ! Play again ?', 13, (0, 0, 0))
            restart(win, winWidth, winHeight, text)
        elif score == 3 and pygame.sprite.spritecollide(player, enemy_sprites, True):
            text = font.render('Winner ! Play again ?', 13, (0, 0, 0))
            restart(win, winWidth, winHeight, text)


        win.blit(back, (0, 0))
        text = font.render('Score : ' + str(score), 1, (255, 255, 255))
        win.blit(text, (winWidth / 2 - text.get_width() / 2, 520))
        all_sprites.update()
        all_sprites.draw(win)

        pygame.display.flip()
        clock.tick(27)


if __name__ == "__main__":
    main()
