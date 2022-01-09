import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 960, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Our Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf',50)

def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(WIN, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(WIN, defaultcolor, (x, y, width, height))

def game_intro():
    #welcome page text
    welcome_text_surf = test_font.render("Welcome to Our Game!", True,'White')
    welcome_rect = welcome_text_surf.get_rect(midtop = (500,200))
    start_text_surf = test_font.render("Made by JAMA", True,'White')
    start_rect = start_text_surf.get_rect(midtop = (500,250))
    #--------------#
    while True:
        WIN.fill((139,0,18))
        WIN.blit(welcome_text_surf,welcome_rect)
        WIN.blit(start_text_surf,start_rect)
        start_button = create_button(500, 300, 125, 26, 'Gold', 'White')
        if start_button:
            game()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(15)
        return True

def game():
    game_text_surf = test_font.render("Here to Code the Game", True,'White')
    while True:
        WIN.fill((0,0,0))
        WIN.blit(game_text_surf,(500,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)

#Game loop
while True:
    game_intro()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)