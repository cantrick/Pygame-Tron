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


def checkBounds():
    if player1.rect.x > rbound:
        player1.rect.x = rbound

    if player1.rect.x < lbound:
        player1.rect.x = lbound

    if player1.rect.y < ubound:
        player1.rect.y = ubound

    if player1.rect.y > dbound:
        player1.rect.y = dbound

    if player2.rect.x > rbound:
        player2.rect.x = rbound

    if player2.rect.x < lbound:
        player2.rect.x = lbound

    if player2.rect.y < ubound:
        player2.rect.y = ubound

    if player2.rect.y > dbound:
        player2.rect.y = dbound

    return False


def player1Controller(inputMap, inputMap2, score1):
    # For human input, keep moving after button is pressed
    if inputMap[0]:
        # Check if the player is out of bounds
        checkBounds()
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
                # move the player back right
                score1 += 1
                drawGameOverScreen("2")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[1]:
        checkBounds()
        player1.rect.x += 10
        createTrailP1(player1.rect.x - 10, player1.rect.y)
        blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.x == player1.rect.x:
                score1 += 1
                drawGameOverScreen("2")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[2]:
        checkBounds()
        player1.rect.y -= 10
        createTrailP1(player1.rect.x, player1.rect.y + 10)
        blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player1.rect.y:
                score1 += 1
                drawGameOverScreen("2")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[3]:
        checkBounds()
        player1.rect.y += 10
        createTrailP1(player1.rect.x, player1.rect.y - 10)
        blocks_hit_list = pygame.sprite.spritecollide(player1,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player1.rect.y:
                score1 += 1
                drawGameOverScreen("2")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    return inputMap, inputMap2, score1


def player2Controller(inputMap, inputMap2, score1):
    # For human input, keep moving after button is pressed
    if inputMap2[0]:
        # Check if the player is out of bounds
        checkBounds()
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
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[1]:
        checkBounds()
        player2.rect.x += 10
        createTrailP2(player2.rect.x - 10, player2.rect.y)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.x == player2.rect.x:
                score1 += 1
                drawGameOverScreen("1")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[2]:
        checkBounds()
        player2.rect.y -= 10
        createTrailP2(player2.rect.x, player2.rect.y + 10)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player2.rect.y:
                score1 += 1
                drawGameOverScreen("1")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap2[3]:
        checkBounds()
        player2.rect.y += 10
        createTrailP2(player2.rect.x, player2.rect.y - 10)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player2.rect.y:
                score1 += 1
                drawGameOverScreen("1")
                (inputMap, inputMap2, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    return inputMap, inputMap2, score1

#param mode for gamemode
def main(mode):
    global done, p1_x, p1_y, p2_x, p2_y
    inputMap1 = [False, True, False, False]
    inputMap2 = [True, False, False, False]

    score1 = 0
    score2 = 0

    while not done:
        randMove = random.randint(1, 4)
        pygame.display.set_caption("Tron        Player 1: " + str(score1) +
                                   "           Player 2: " + str(score2))
        # Event Processing Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if mode == 1:
                if event.type == pygame.KEYDOWN:

                    # Player 2 control handling
                    if(inputMap2 == [True, False, False, False] or
                            inputMap2 == [False, True, False, False]):
                        if event.key == pygame.K_UP:
                            inputMap2 = [False, False, True, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                        if event.key == pygame.K_DOWN:
                            inputMap2 = [False, False, False, True]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                    elif(inputMap2 == [False, False, True, False] or
                         inputMap2 == [False, False, False, True]):
                        if event.key == pygame.K_LEFT:
                            inputMap2 = [True, False, False, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                        if event.key == pygame.K_RIGHT:
                            inputMap2 = [False, True, False, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                    else:
                        if event.key == pygame.K_LEFT:
                            inputMap2 = [True, False, False, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                        if event.key == pygame.K_RIGHT:
                            inputMap2 = [False, True, False, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                        if event.key == pygame.K_UP:
                            inputMap2 = [False, False, True, False]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                        if event.key == pygame.K_DOWN:
                            inputMap2 = [False, False, False, True]
                            inputMap1, inputMap2, score1 = player2Controller(
                                inputMap1, inputMap2, score1)

                    # Player 1 control handling
                    if(inputMap1 == [True, False, False, False] or
                            inputMap1 == [False, True, False, False]):
                        if event.key == pygame.K_w:
                            inputMap1 = [False, False, True, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                        if event.key == pygame.K_s:
                            inputMap1 = [False, False, False, True]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                    elif(inputMap1 == [False, False, True, False] or
                         inputMap1 == [False, False, False, True]):
                        if event.key == pygame.K_a:
                            inputMap1 = [True, False, False, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                        if event.key == pygame.K_d:
                            inputMap1 = [False, True, False, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                    else:
                        if event.key == pygame.K_a:
                            inputMap1 = [True, False, False, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                        if event.key == pygame.K_d:
                            inputMap1 = [False, True, False, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                        if event.key == pygame.K_w:
                            inputMap1 = [False, False, True, False]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                        if event.key == pygame.K_s:
                            inputMap1 = [False, False, False, True]
                            inputMap1, inputMap2, score2 = player1Controller(
                                inputMap1, inputMap2, score2)

                    if event.key == pygame.K_r:
                        drawGameOverScreen("1")

        '''if checkBounds() == True:
            if randMove == 1:
                player1.rect.x += 10
                createTrail(player1.rect.x-10, player1.rect.y)
                checkBounds()
                blocks_hit_list = pygame.sprite.spritecollide(player1,
                                    block_list, False)
                for block in blocks_hit_list:
                    if block.rect.x == player1.rect.x:
                        player1.rect.x -= 10
            elif randMove == 2:
                player1.rect.y += 10
                createTrail(player1.rect.x, player1.rect.y-10)
                checkBounds()
                blocks_hit_list = pygame.sprite.spritecollide(player1,
                                    block_list, False)
                for block in blocks_hit_list:
                    if block.rect.y == player1.rect.y:
                        player1.rect.y -= 10
            elif randMove == 3:
                player1.rect.x -= 10
                createTrail(player1.rect.x+10, player1.rect.y)
                checkBounds()
                blocks_hit_list = pygame.sprite.spritecollide(player1,
                                    block_list, False)
                for block in blocks_hit_list:
                    if block.rect.x == player1.rect.x:
                        player1.rect.x += 10
            else:
                player1.rect.y -= 10
                createTrail(player1.rect.x, player1.rect.y+10)
                checkBounds()
                blocks_hit_list = pygame.sprite.spritecollide(player1,
                                    block_list, False)
                for block in blocks_hit_list:
                    if block.rect.y == player1.rect.y:
                        player1.rect.y += 10'''

        inputMap1, inputMap2, score2 = player1Controller(
            inputMap1, inputMap2, score2)

        inputMap1, inputMap2, score1 = player2Controller(
            inputMap1, inputMap2, score1)

        # Clear screen to white
        screen.fill(WHITE)
        drawGame()
        all_sprites_list.draw(screen)

        # Update screen with what we've drawn
        pygame.display.flip()

        # FPS
        clock.tick(11)

    if __name__ == "__main__":
        main(mode)

    pygame.quit()


''' Add modes for AI. Currently:
	1 = Player vs Player
    2 = Player vs Random AI
    3 = Player vs Wallhug AI
    4 = Player vs Good AI

    5 = Random AI vs Player
    6 = Random AI vs Random AI
    7 = Random AI vs Wallhug AI
    8 = Random AI vs Good AI

    9 = Wallhug AI vs Player
    10 = Wallhug AI vs Random AI
    11 = Wallhug AI vs Wallhug AI
    12 = Wallhug AI vs Good AI

    13 = Good AI vs Player
    14 = Good AI vs Random AI
    15 = Good AI vs Wallhug AI
    16 = Good AI vs Good AI

    ***SUBJECT TO CHANGE***
'''

#main()
