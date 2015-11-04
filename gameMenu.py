import pygame
import tronMain
pygame.init()


class MenuItem(pygame.font.Font):

    def __init__(self, text, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x=0, pos_y=0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, color):
        self.font_color = color
        self.label = self.render(self.text, 1, self.font_color)

    def is_mouse_selection(self, pos):
        if ((pos[0] >= self.pos_x and pos[0] <= self.pos_x + self.width)
            and (pos[1] >= self.pos_y
                 and pos[1] <= self.pos_y + self.height)):
            return True
        return False


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font2 = pygame.font.SysFont(None, 30)


def initScreen():
    screen_x = 500
    screen_y = 500
    size = (screen_x, screen_y)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tron Main Menu")

    return screen


def screen1():
    screen = initScreen()

    # Loop until the user clicks the close button.
    done = False

    items = ("Player", "Random", "WallHug", "Good")
    menuItems = []
    diff = 0
    # Create Menu items
    for item in items:
        mItem = MenuItem(item)
        pos_x = 210
        pos_y = 100 + diff
        mItem.set_position(pos_x, pos_y)
        diff += 50
        menuItems.append(mItem)

    while not done:
        mpos = pygame.mouse.get_pos()
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in menuItems:
                    if item.is_mouse_selection(mpos) and item.text == "Player":
                        done = True
                        screen2(1)
                    elif (item.is_mouse_selection(mpos)
                          and item.text == "Random"):
                        done = True
                        screen2(2)
                    elif (item.is_mouse_selection(mpos)
                          and item.text == "WallHug"):
                        done = True
                        screen2(3)
                    elif item.is_mouse_selection(mpos) and item.text == "Good":
                        done = True
                        screen2(4)

        screen.fill(WHITE)

        for item in menuItems:
            if item.is_mouse_selection(pygame.mouse.get_pos()):
                item.set_font_color(RED)
                item.set_italic(True)
            else:
                item.set_font_color(BLACK)
                item.set_italic(False)
            screen.blit(item.label, item.position)

        screen.blit(
            font2.render("Select who will play as Player 1:",
                         1, BLACK), (80, 10))
        pygame.display.flip()
        clock.tick(30)


def screen2(firstOp):
    screen = initScreen()
    # Loop until the user clicks the close button.
    done = False

    items = ("Player", "Random", "WallHug", "Good")
    menuItems = []
    diff = 0
    # Create Menu items
    for item in items:
        mItem = MenuItem(item)
        pos_x = 210
        pos_y = 100 + diff
        mItem.set_position(pos_x, pos_y)
        diff += 50
        menuItems.append(mItem)

    while not done:
        mpos = pygame.mouse.get_pos()
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in menuItems:
                    if item.is_mouse_selection(mpos) and item.text == "Player":
                        if firstOp == 1:
                            done = True
                            tronMain.main(1)
                        elif firstOp == 2:
                            done = True
                            tronMain.main(2)
                    elif (item.is_mouse_selection(mpos)
                          and item.text == "Random"):
                        if firstOp == 1:
                            done = True
                            tronMain.main(3)
                        done = True
                        screen2(2)
                    elif (item.is_mouse_selection(mpos)
                          and item.text == "WallHug"):
                        done = True
                        screen2(3)
                    elif item.is_mouse_selection(mpos) and item.text == "Good":
                        done = True
                        screen2(4)

        screen.fill(WHITE)

        for item in menuItems:
            if item.is_mouse_selection(pygame.mouse.get_pos()):
                item.set_font_color(RED)
                item.set_italic(True)
            else:
                item.set_font_color(BLACK)
                item.set_italic(False)
            screen.blit(item.label, item.position)

        screen.blit(
            font2.render("Select who will play as Player 2:",
                         1, BLACK), (80, 10))
        pygame.display.flip()
        clock.tick(30)

screen1()


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

pygame.quit()
