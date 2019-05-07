import random

from constants import *
from player_class import Macgyver
from visuals_class import Walls, PickSafe, PickCoin, PickPotion, Floor, End


def restart(win, winWidth, winHeight, text_to_display):
    text = text_to_display
    textx = winWidth / 2 - text.get_width() / 2
    texty = winHeight / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(win, (255, 255, 255), ((textx - 5, texty - 5),
                                            (textx_size + 10, texty_size + 10)))

    win.blit(text, (winWidth / 2 - text.get_width() / 2,
                    winHeight / 2 - text.get_height() / 2))

    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                main()
                if x >= textx - 5 and x <= textx + textx_size + 5:
                    if y >= texty - 5 and y <= texty + texty_size + 5:
                        in_main_menu = False
                        break

def main():
    win = pygame.display.set_mode((winWidth, winHeight))
    score = 0
    pygame.display.set_caption('Macgyver')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsans', 30)

    all_sprites = pygame.sprite.Group()
    walls_sprites = pygame.sprite.Group()
    floor_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    pick_sprites = pygame.sprite.Group()

    maze_list = [maze_1, maze_2]
    maze_choice = random.choice(maze_list)
    mazing = []
    for line in maze_choice.split('\n'):
        line = list(line)
        mazing.append(line)

    y = 0
    objects_to_display = 0
    counting_sprites = 0
    for line in mazing:
        x = 0
        for sprite in line:
            if sprite == '0':
                aSprite = Floor(x * number_of_sprite, y * number_of_sprite)
                floor_sprites.add(aSprite)
                all_sprites.add(aSprite)

                if counting_sprites > 60 and objects_to_display <= 2:
                    x_pick = x * number_of_sprite
                    y_pick = y * number_of_sprite
                    list_toBePicked = [PickPotion(x_pick, y_pick),
                                       PickCoin(x_pick, y_pick),
                                       PickSafe(x_pick, y_pick)]
                    choose_toBePicked = random.choice(list_toBePicked)
                    pick_sprites.add(choose_toBePicked)
                    all_sprites.add(choose_toBePicked)
                    objects_to_display += 1
                counting_sprites += 1

            elif sprite == 'm':
                aSprite = Walls(x * number_of_sprite, y * number_of_sprite)
                walls_sprites.add(aSprite)
                all_sprites.add(aSprite)
            elif sprite == 'a':
                aSprite = End(x * number_of_sprite, y * number_of_sprite)
                backgroundSprite = Floor(x * number_of_sprite, y * number_of_sprite)
                enemy_sprites.add(aSprite)
                all_sprites.add(backgroundSprite, aSprite)
            x += 1
        y += 1

    player = Macgyver(45, 45, walls_sprites)
    all_sprites.add(player)

    game = False

    while not game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True

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
        end_game = pygame.sprite.spritecollide(player, enemy_sprites, True) and score == 3

        if pick_objects:
            pick_sprites.clear(win, back)
            score += 1

        if end_game:
            enemy_sprites.clear(win, back)
            text = font.render('Winner ! Play again ?', 13, (0, 0, 0))
            restart(win, winWidth, winHeight, text)
        # elif :
        #     text = font.render('Looser ! Play again ?', 13, (0, 0, 0))
        #     play_again(win, winWidth, winHeight, text)

        win.blit(back, (0, 0))
        text = font.render('Score : ' + str(score), 1, (255, 255, 0))
        win.blit(text, (15, 550))
        all_sprites.update()
        all_sprites.draw(win)

        pygame.display.flip()
        clock.tick(27)


if __name__ == "__main__":
    main()