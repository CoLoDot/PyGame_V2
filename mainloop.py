import sys
from constants import *
from player_class import Macgyver
from maze_class import MazeCreation
import play_again


def main():
    """Main Loop of the game"""
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
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
            pygame.mixer.Sound.play(pickingMusic).set_volume(0.2)
            pick_sprites.clear(win, back)
            score += 1

        if score != 3 and pygame.sprite.spritecollideany(player, enemy_sprites):
            pygame.sprite.spritecollide(player, enemy_sprites, False)
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(loosingMusic).set_volume(0.5)
            text = font.render('Looser ! Play again ?', 13, (0, 0, 0))
            play_again.restart(win, winWidth, winHeight, text)
        elif score == 3 and pygame.sprite.spritecollide(player, enemy_sprites, True):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winningMusic).set_volume(0.5)
            text = font.render('Winner ! Play again ?', 13, (0, 0, 0))
            play_again.restart(win, winWidth, winHeight, text)

        win.blit(back, (0, 0))
        text = font.render('Score : ' + str(score) + ' / 3', 1, (255, 255, 255))
        win.blit(text, (winWidth / 2 - text.get_width() / 2, 520))
        all_sprites.update()
        all_sprites.draw(win)

        pygame.display.flip()
        clock.tick(27)


if __name__ == "__main__":
    main()
