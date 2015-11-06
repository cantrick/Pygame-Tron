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

    items = ("Player", "Random", "Ordered Selection", "WallHug", "Good")
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
                    elif (item.is_mouse_selection(mpos) and
                            item.text == "Ordered Selection"):
                        done = True
                        screen2(5)

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

    items = ("Player", "Random", "Ordered Selection", "WallHug", "Good")
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
                        tronMain.main(firstOp, 1)

                    elif (item.is_mouse_selection(mpos)
                          and item.text == "Random"):
                        done = True
                        tronMain.main(firstOp, 2)

                    elif (item.is_mouse_selection(mpos)
                          and item.text == "WallHug"):
                        done = True
                        tronMain.main(firstOp, 3)

                    elif item.is_mouse_selection(mpos) and item.text == "Good":
                        done = True
                        tronMain.main(firstOp, 4)

                    elif (item.is_mouse_selection(mpos) and
                            item.text == "Ordered Selection"):
                        done = True
                        tronMain.main(firstOp, 5)

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
    1,1 = Player vs Player
    1,2 = Player vs Random AI
    1,3 = Player vs Wallhug AI
    1,4 = Player vs Good AI
    1,5 = Player vs Ordered Selection AI

    2,1 = Random AI vs Player
    2,2 = Random AI vs Random AI
    2,3 = Random AI vs Wallhug AI
    2,4 = Random AI vs Good AI
    2,5 = Random AI vs Ordered Selection AI

    3,1 = Wallhug AI vs Player
    3,2 = Wallhug AI vs Random AI
    3,3 = Wallhug AI vs Wallhug AI
    3,4 = Wallhug AI vs Good AI
    3,5 = Wallhug AI vs Ordered Selection AI

    4,1 = Good AI vs Player
    4,2 = Good AI vs Random AI
    4,3 = Good AI vs Wallhug AI
    4,4 = Good AI vs Good AI
    4,5 = Good AI vs Ordered Selection AI

    5,1 = Ordered Selection AI vs Player
    5,2 = Ordered Selection AI vs Random AI
    5,3 = Ordered Selection AI vs Wallhug AI
    5,4 = Ordered Selection AI vs Good AI
    5,5 = Ordered Selection AI vs Ordered Selection AI

    ***SUBJECT TO CHANGE***
'''

pygame.quit()
