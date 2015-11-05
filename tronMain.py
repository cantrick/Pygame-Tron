# Tron made using Pygame
import pygame
import random
from Player import Player
pygame.init()

screen_x = 500
screen_y = 500
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tron")
lbound, rbound, ubound, dbound = 0, 490, 0, 490

done = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 78, 222)
BLUE2 = (111, 151, 237)
RED = (194, 4, 36)
RED2 = (237, 111, 164)
clock = pygame.time.Clock()

# list of things the player can collide with
block_list = pygame.sprite.Group()
# list of everything, including the player
all_sprites_list = pygame.sprite.Group()

# Create both player squares with their trails

player1 = Player(BLUE, 10, 10)
all_sprites_list.add(player1)
player1.rect.x, player1.rect.y = lbound, 250

player2 = Player(RED, 10, 10)
all_sprites_list.add(player2)
player2.rect.x, player2.rect.y = rbound, 250

inputMap1 = [False, True, False, False]
inputMap2 = [True, False, False, False]


def resetBoard():
    for sprite in all_sprites_list:
        all_sprites_list.remove(sprite)

    for block in block_list:
        block_list.remove(block)

    all_sprites_list.add(player1)
    player1.rect.x, player1.rect.y = lbound, 250

    all_sprites_list.add(player2)
    player2.rect.x, player2.rect.y = rbound, 250

    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    inputMap1 = [False, True, False, False]
    inputMap2 = [True, False, False, False]

    drawGame()

    return (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
            player1.rect.x, player1.rect.y)


def drawGameOverScreen(pWin):
    done = False
    diff = 0
    font = pygame.font.SysFont(None, 50)
    screen.fill(WHITE)
    win = "Player " + pWin + " wins!"
    items = ("GAME OVER", win, "Press Enter to continue...")
    for item in items:
        text = font.render(item, True, (0, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        pos_x = 250
        pos_y = 100 + diff
        textrect.centerx, textrect.centery = pos_x, pos_y
        screen.blit(text, textrect)
        diff += 100

    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


def drawGame():
    # Draw game board grid
    for y_offset in range(0, 500, 10):
        pygame.draw.line(screen, BLACK, [0, 0 + y_offset], [500, 0 + y_offset])
        pygame.draw.line(screen, BLACK, [0 + y_offset, 0], [0 + y_offset, 500])


def createTrailP1(px, py):
    p1Trail = Player(BLUE2, 10, 10)
    p1Trail.rect.x, p1Trail.rect.y = px, py
    all_sprites_list.add(p1Trail)
    block_list.add(p1Trail)


def createTrailP2(px, py):
    p2Trail = Player(RED2, 10, 10)
    p2Trail.rect.x, p2Trail.rect.y = px, py
    print("PTX:", p2Trail.rect.x, "PTY:", p2Trail.rect.y)
    all_sprites_list.add(p2Trail)
    block_list.add(p2Trail)


def checkBounds(player):
    if player.rect.x > rbound:
        player.rect.x = rbound
        return True

    if player.rect.x < lbound:
        player.rect.x = lbound
        return True

    if player.rect.y < ubound:
        player.rect.y = ubound
        return True

    if player.rect.y > dbound:
        player.rect.y = dbound
        return True

    return False


def player1Controller(score1):
    global inputMap1, inputMap2

    # For human input, keep moving after button is pressed
    if inputMap1[0]:
        # Check if the player is out of bounds
        if checkBounds(player1):
            score1 += 1
            drawGameOverScreen("2")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:
            # move player left
            player1.rect.x -= 10
            # create a trail behind where player was
            createTrailP1(player1.rect.x + 10, player1.rect.y)
            # check if there are collisions
            blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                          block_list, False)
            for block in blocks_hit_list:
                # if there is a collision after going LEFT
                if block.rect.x == player1.rect.x:
                    # give opposite player some points
                    score1 += 1
                    # show the game over screen
                    drawGameOverScreen("2")
                    # reset the board
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap1[1]:

        if checkBounds(player1):
            score1 += 1
            drawGameOverScreen("2")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player1.rect.x += 10
            createTrailP1(player1.rect.x - 10, player1.rect.y)
            blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.x == player1.rect.x:
                    score1 += 1
                    drawGameOverScreen("2")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap1[2]:

        if checkBounds(player1):
            score1 += 1
            drawGameOverScreen("2")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player1.rect.y -= 10
            createTrailP1(player1.rect.x, player1.rect.y + 10)
            blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.y == player1.rect.y:
                    score1 += 1
                    drawGameOverScreen("2")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap1[3]:

        if checkBounds(player1):
            score1 += 1
            drawGameOverScreen("2")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player1.rect.y += 10
            createTrailP1(player1.rect.x, player1.rect.y - 10)
            blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.y == player1.rect.y:
                    score1 += 1
                    drawGameOverScreen("2")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    return score1


def player2Controller(score1):
    global inputMap1, inputMap2

    # For human input, keep moving after button is pressed
    if inputMap2[0]:
        # Check if the player is out of bounds
        if checkBounds(player2):
            score1 += 1
            drawGameOverScreen("1")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:
            # move player left
            player2.rect.x -= 10
            # create a trail behind where player was
            createTrailP2(player2.rect.x + 10, player2.rect.y)
            # check if there are collisions
            blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                          block_list, False)
            for block in blocks_hit_list:
                # if there is a collision after going LEFT
                if block.rect.x == player2.rect.x:
                    # move the player back right
                    score1 += 1
                    drawGameOverScreen("1")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[1]:

        if checkBounds(player2):
            score1 += 1
            drawGameOverScreen("1")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player2.rect.x += 10
            createTrailP2(player2.rect.x - 10, player2.rect.y)
            blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.x == player2.rect.x:
                    score1 += 1
                    drawGameOverScreen("1")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[2]:

        if checkBounds(player2):
            score1 += 1
            drawGameOverScreen("1")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player2.rect.y -= 10
            createTrailP2(player2.rect.x, player2.rect.y + 10)
            blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.y == player2.rect.y:
                    score1 += 1
                    drawGameOverScreen("1")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[3]:

        if checkBounds(player2):
            score1 += 1
            drawGameOverScreen("1")
            (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
             player1.rect.x, player1.rect.y) = resetBoard()
        else:

            player2.rect.y += 10
            createTrailP2(player2.rect.x, player2.rect.y - 10)
            blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                          block_list, False)
            for block in blocks_hit_list:
                if block.rect.y == player2.rect.y:
                    score1 += 1
                    drawGameOverScreen("1")
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                     player1.rect.x, player1.rect.y) = resetBoard()

    return score1


def gameMode(score, p1mode, p2mode):
    global inputMap1, inputMap2

    if p1mode == 2:
        randMove = random.randint(1, 4)

        if randMove == 1:
            if (inputMap1 == [True, False, False, False] or
                    inputMap1 == [False, True, False, False]):
                pass
            else:
                inputMap1 = [True, False, False, False]

        elif randMove == 2:
            if (inputMap1 == [True, False, False, False] or
                    inputMap1 == [False, True, False, False]):
                pass
            else:
                inputMap1 = [False, True, False, False]

        elif randMove == 3:
            if (inputMap1 == [False, False, True, False] or
                    inputMap1 == [False, False, False, True]):
                pass
            else:
                inputMap1 = [False, False, True, False]

        elif randMove == 4:
            if (inputMap1 == [False, False, True, False] or
                    inputMap1 == [False, False, False, True]):
                pass
            else:
                inputMap1 = [False, False, False, True]

    if p2mode == 2:
        randMove = random.randint(1, 4)

        if randMove == 1:
            if (inputMap2 == [True, False, False, False] or
                    inputMap2 == [False, True, False, False]):
                pass
            else:
                inputMap2 = [True, False, False, False]

        elif randMove == 2:
            if (inputMap2 == [True, False, False, False] or
                    inputMap2 == [False, True, False, False]):
                pass
            else:
                inputMap2 = [False, True, False, False]

        elif randMove == 3:
            if (inputMap2 == [False, False, True, False] or
                    inputMap2 == [False, False, False, True]):
                pass
            else:
                inputMap2 = [False, False, True, False]

        elif randMove == 4:
            if (inputMap2 == [False, False, True, False] or
                    inputMap2 == [False, False, False, True]):
                pass
            else:
                inputMap2 = [False, False, False, True]

    return score

# param mode for game mode
def main(p1mode, p2mode):
    global done, p1_x, p1_y, p2_x, p2_y, inputMap1, inputMap2

    score1 = 0
    score2 = 0

    while not done:
        pygame.display.set_caption("Tron        Player 1: " + str(score1) +
                                   "           Player 2: " + str(score2))
        # Event Processing Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if p2mode == 1:

                # Player 2 control handling
                    if(inputMap2 == [True, False, False, False] or
                            inputMap2 == [False, True, False, False]):
                        if event.key == pygame.K_UP:
                            inputMap2 = [False, False, True, False]
                            score1 = player2Controller(score1)

                        if event.key == pygame.K_DOWN:
                            inputMap2 = [False, False, False, True]
                            score1 = player2Controller(score1)

                    elif(inputMap2 == [False, False, True, False] or
                         inputMap2 == [False, False, False, True]):
                        if event.key == pygame.K_LEFT:
                            inputMap2 = [True, False, False, False]
                            score1 = player2Controller(score1)

                        if event.key == pygame.K_RIGHT:
                            inputMap2 = [False, True, False, False]
                            score1 = player2Controller(score1)

                    else:
                        if event.key == pygame.K_LEFT:
                            inputMap2 = [True, False, False, False]
                            score1 = player2Controller(score1)

                        if event.key == pygame.K_RIGHT:
                            inputMap2 = [False, True, False, False]
                            score1 = player2Controller(score1)

                        if event.key == pygame.K_UP:
                            inputMap2 = [False, False, True, False]
                            score1 = player2Controller(score1)

                        if event.key == pygame.K_DOWN:
                            inputMap2 = [False, False, False, True]
                            score1 = player2Controller(score1)

                if p1mode == 1:
                    # Player 1 control handling
                    if(inputMap1 == [True, False, False, False] or
                            inputMap1 == [False, True, False, False]):
                        if event.key == pygame.K_w:
                            inputMap1 = [False, False, True, False]
                            score2 = player1Controller(score2)

                        if event.key == pygame.K_s:
                            inputMap1 = [False, False, False, True]
                            score2 = player1Controller(score2)

                    elif(inputMap1 == [False, False, True, False] or
                         inputMap1 == [False, False, False, True]):
                        if event.key == pygame.K_a:
                            inputMap1 = [True, False, False, False]
                            score2 = player1Controller(score2)

                        if event.key == pygame.K_d:
                            inputMap1 = [False, True, False, False]
                            score2 = player1Controller(score2)

                    else:
                        if event.key == pygame.K_a:
                            inputMap1 = [True, False, False, False]
                            score2 = player1Controller(score2)

                        if event.key == pygame.K_d:
                            inputMap1 = [False, True, False, False]
                            score2 = player1Controller(score2)

                        if event.key == pygame.K_w:
                            inputMap1 = [False, False, True, False]
                            score2 = player1Controller(score2)

                        if event.key == pygame.K_s:
                            inputMap1 = [False, False, False, True]
                            score2 = player1Controller(score2)

                    if event.key == pygame.K_r:
                        drawGameOverScreen("1")

        if p1mode != 1:
        	score2 = gameMode(score2, p1mode, 0)

        if p2mode != 1:
        	score1 = gameMode(score1, 0, p2mode)

        score2 = player1Controller(score2)
        score1 = player2Controller(score1)

        # Clear screen to white
        screen.fill(WHITE)
        drawGame()
        all_sprites_list.draw(screen)

        # Update screen with what we've drawn
        pygame.display.flip()

        # FPS
        clock.tick(11)

    if __name__ == "__main__":
        main(p1mode, p2mode)

    pygame.quit()

# main()
