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
player1.rect.x, player1.rect.y = lbound, ubound
p1Trail = Player(BLUE2, 10, 10)
block_list.add(p1Trail)
all_sprites_list.add(p1Trail)

player2 = Player(RED, 10, 10)
all_sprites_list.add(player2)
player2.rect.x, player2.rect.y = rbound, dbound
p2Trail = Player(RED2, 10, 10)
block_list.add(p2Trail)
all_sprites_list.add(p2Trail)


def resetBoard():
    for sprite in all_sprites_list:
        all_sprites_list.remove(sprite)

    for block in block_list:
        block_list.remove(block)

    all_sprites_list.add(player1)
    player1.rect.x, player1.rect.y = lbound, ubound
    p1Trail = Player(BLUE2, 10, 10)
    block_list.add(p1Trail)
    all_sprites_list.add(p1Trail)

    all_sprites_list.add(player2)
    player2.rect.x, player2.rect.y = rbound, dbound
    p2Trail = Player(RED2, 10, 10)
    block_list.add(p2Trail)
    all_sprites_list.add(p2Trail)

    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    inputMap1 = [False, False, False, False]
    inputMap2 = [False, False, False, False]

    return (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
            player1.rect.x, player1.rect.y)


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


def player1Controller(inputMap, score1):
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
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
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
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
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
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
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
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    return score1


def player2Controller(inputMap, score1):
        # For human input, keep moving after button is pressed
    if inputMap[0]:
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
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[1]:
        checkBounds()
        player2.rect.x += 10
        createTrailP2(player2.rect.x - 10, player2.rect.y)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.x == player2.rect.x:
                score1 += 1
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[2]:
        checkBounds()
        player2.rect.y -= 10
        createTrailP2(player2.rect.x, player2.rect.y + 10)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player2.rect.y:
                score1 += 1
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    elif inputMap[3]:
        checkBounds()
        player2.rect.y += 10
        createTrailP2(player2.rect.x, player2.rect.y - 10)
        blocks_hit_list = pygame.sprite.spritecollide(player2,
                                                      block_list, False)
        for block in blocks_hit_list:
            if block.rect.y == player2.rect.y:
                score1 += 1
                (inputMap, inputMap, player2.rect.x, player2.rect.y,
                 player1.rect.x, player1.rect.y) = resetBoard()

    return score1


def main():
    global done, p1_x, p1_y, p2_x, p2_y
    inputMap1 = [False, False, False, False]
    inputMap2 = [False, False, False, False]

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    inputMap2 = [True, False, False, False]
                    score1 = player2Controller(inputMap2, score1)

                if event.key == pygame.K_RIGHT:
                    inputMap2 = [False, True, False, False]
                    score1 = player2Controller(inputMap2, score1)

                if event.key == pygame.K_UP:
                    inputMap2 = [False, False, True, False]
                    score1 = player2Controller(inputMap2, score1)

                if event.key == pygame.K_DOWN:
                    inputMap2 = [False, False, False, True]
                    score1 = player2Controller(inputMap2, score1)

                if event.key == pygame.K_a:
                    inputMap1 = [True, False, False, True]
                    score2 = player1Controller(inputMap1, score2)

                if event.key == pygame.K_d:
                    inputMap1 = [False, True, False, True]
                    score2 = player1Controller(inputMap1, score2)

                if event.key == pygame.K_w:
                    inputMap1 = [False, False, True, False]
                    score2 = player1Controller(inputMap1, score2)

                if event.key == pygame.K_s:
                    inputMap1 = [False, False, False, True]
                    score2 = player1Controller(inputMap1, score2)

                if event.key == pygame.K_r:
                    (inputMap1, inputMap2, player2.rect.x, player2.rect.y,
                        player1.rect.x, player1.rect.y) = resetBoard()

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

        score2 = player1Controller(inputMap1, score2)
        score1 = player2Controller(inputMap2, score1)

        # Clear screen to white
        screen.fill(WHITE)
        drawGame()
        all_sprites_list.draw(screen)

        # Update screen with what we've drawn
        pygame.display.flip()

        # FPS
        clock.tick(11)

    '''if __name__ == "__main__":
        main()'''

    pygame.quit()


''' Add modes for AI. Currently:
    1 = Player vs Random AI
    2 = Player vs Wallhug AI
    3 = Player vs Good AI

    4 = Random AI vs Random AI
    5 = Random AI vs Wallhug AI
    6 = Random AI vs Good AI

    7 = Wallhug AI vs Wallhug AI
    8 = Wallhug AI vs Good AI
    9 = Good AI vs Good AI

    ***SUBJECT TO CHANGE***
'''


def gameModes(modeNum):
    if modeNum == 1:
        qq = 1
    elif modeNum == 2:
        qq = 2
    else:
        qq = 3

    main()

main()
