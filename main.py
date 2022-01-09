import os
import sys
import pygame
from typing import List
from api import ImportSetting as Import
from index import Index
from event import Event
from card import Card
import time

pygame.init()
WIDTH, HEIGHT = 960, 600
I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY = 100, 100, 100, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Our Game')
clock = pygame.time.Clock()

# Fonts
test_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 50)
index_font = pygame.font.Font(os.path.join("Assets/font", "Abel-Regular.ttf"), 20)
number_font = pygame.font.Font(os.path.join("Assets/font", "Abel-Regular.ttf"), 40)

# Sounds
start_sound = pygame.mixer.Sound('assets/sound/start.wav')
finish_sound = pygame.mixer.Sound('assets/sound/finish.wav')

# Load images
PRESIDENT_IMG = pygame.image.load(os.path.join("Assets/icon", "gov.png"))
PEOPLE_IMG = pygame.image.load(os.path.join("Assets/icon", "ppl.png"))
PLANT_IMG = pygame.image.load(os.path.join("Assets/icon", "plant.png"))
MONEY_IMG = pygame.image.load(os.path.join("Assets/icon", "money.png"))

# Scale images
PRESIDENT_IC = pygame.transform.scale(PRESIDENT_IMG, (48, 48))
PEOPLE_IC = pygame.transform.scale(PEOPLE_IMG, (48, 48))
PLANT_IC = pygame.transform.scale(PLANT_IMG, (48, 48))
MONEY_IC = pygame.transform.scale(MONEY_IMG, (48, 48))

# Test case for failure
fail_id = 3


def render_button(x, y, width, height, hovercolor, defaultcolor, message):
    mouse = pygame.mouse.get_pos()
    btn_text_surf = test_font.render(message, True, hovercolor)
    btn_text_surf_hover = test_font.render(message, True, defaultcolor)
    btn_text_rect = btn_text_surf.get_rect(midtop=(x + width / 2, y))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(WIN, hovercolor, (x, y, width, height))
        WIN.blit(btn_text_surf_hover, btn_text_rect)
    else:
        pygame.draw.rect(WIN, defaultcolor, (x, y, width, height))
        WIN.blit(btn_text_surf, btn_text_rect)


def press_button(x, y, width, height, sound):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y and click[0] == 1:
        pygame.mixer.Sound.play(sound)
        return True
    return False


def game_intro():
    # welcome page text
    welcome_text_surf = test_font.render("Welcome to Our Game!", True, 'White')
    welcome_rect = welcome_text_surf.get_rect(midtop=(500, 200))
    start_text_surf = test_font.render("Made by JAM", True, 'White')
    start_rect = start_text_surf.get_rect(midtop=(500, 250))

    while True:
        WIN.fill((139, 0, 18))
        WIN.blit(welcome_text_surf, welcome_rect)
        WIN.blit(start_text_surf, start_rect)
        render_button(500, 320, 125, 70, (139, 0, 18), 'White', 'Start')
        start_button = press_button(500, 320, 125, 70, start_sound)
        if start_button:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)
        return True


def draw_game_window(indices: List[Index]):
    game_text_surf = test_font.render("Here to Code the Game", True, 'Black')
    names = [index_font.render(index.id_str, True, 'Black') for index in indices]
    values = [number_font.render(str(index.value), True, 'Black') for index in indices]

    WIN.fill((255, 255, 255))  # WHITE
    WIN.blit(game_text_surf, (500, 300))

    # President Index
    WIN.blit(PRESIDENT_IC, (100, 25))
    WIN.blit(names[0], (90, 78))
    WIN.blit(values[0], (170, 30))

    # People Index
    WIN.blit(PEOPLE_IC, (300, 25))
    WIN.blit(names[1], (300, 78))
    WIN.blit(values[1], (370, 30))

    # Environment Index
    WIN.blit(PLANT_IC, (500, 25))
    WIN.blit(names[2], (480, 78))
    WIN.blit(values[2], (570, 30))

    # Treasury Index
    WIN.blit(MONEY_IC, (700, 25))
    WIN.blit(names[3], (690, 78))
    WIN.blit(values[3], (770, 30))

    # Render buttons
    render_button(100, 320, 125, 70, (139, 0, 18), 'White', 'End')

    # Update
    pygame.display.update()
    clock.tick(60)


def game():
    president = Index("President", 100)
    people = Index("People", 100)
    environment = Index("Environment", 100)
    treasury = Index("Treasury", 100)
    time.sleep(0.5)
    pygame.mixer.music.load('assets/sound/background.wav')
    pygame.mixer.music.play(-1)
    while True:
        draw_game_window([president, people, environment, treasury])
        button_pressed = press_button(100, 320, 125, 70, finish_sound)
        if button_pressed:
            pygame.mixer.music.stop()
            finish(fail_id)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            president.value = -5


def finish(id):
    if id == 0:
        end_text_surf = test_font.render("The president FIRED you!", True, 'White')
    elif id == 1:
        end_text_surf = test_font.render("Your people REVOLT against you!", True, 'White')
    elif id == 2:
        end_text_surf = test_font.render("Mother earth is DYING!!", True, 'White')
    else:
        end_text_surf = test_font.render("Your office runs our of money!", True, 'White')

    while True:
        WIN.fill((139, 0, 18))
        WIN.blit(end_text_surf, (280, 200))
        render_button(350, 320, 170, 70, (139, 0, 18), 'White', 'Re-Play')
        restart_button = press_button(350, 320, 170, 70, start_sound)
        if restart_button:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    config_file = "plot.json"
    events = Import(config_file).read_plot()

    while True:
        game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


# TODO: integration
# TODO: event
# TODO: game over, restart
# TODO: after effects (sound, animation, etc.)
# TODO: documentation video