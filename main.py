import os
import sys
import pygame
from typing import List
import time

from api import ImportSetting as Import
from index import Index
from event import Event
from card import Card


# Global Value Initialization
WIDTH, HEIGHT = 960, 600

START = 200
I_PRESIDENT = Index("President", START)
I_PEOPLE = Index("People", START)
I_ENVIRONMENT = Index("Environment", START)
I_TREASURY = Index("Treasury", START)

card_1_angle = 27
card_2_angle = 0
card_3_angle = 333
card_size = (200, 400)
cardColor = (250, 250, 250)

default = 400
card_1_position_x = 175
card_2_position_x = 375
card_3_position_x = 415
global card_1_position_y, card_2_position_y, card_3_position_y
card_1_position_y = default
card_2_position_y = default
card_3_position_y = default

# Game Initialization
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Our Game')
clock = pygame.time.Clock()

# Fonts
test_font = pygame.font.Font('assets/font/Abel-Regular.ttf', 50)
index_font = pygame.font.Font(os.path.join("Assets/font", "Abel-Regular.ttf"), 20)
number_font = pygame.font.Font(os.path.join("Assets/font", "Abel-Regular.ttf"), 40)
e_title_font = pygame.font.Font(os.path.join("Assets/font", "Abel-Regular.ttf"), 25)

# Sounds
start_sound = pygame.mixer.Sound('assets/sound/start.wav')
finish_sound = pygame.mixer.Sound('assets/sound/finish.wav')

# Load images
PRESIDENT_IMG = pygame.image.load(os.path.join("Assets/icon", "gov.png"))
PRESIDENT_IC = pygame.transform.scale(PRESIDENT_IMG, (48, 48))
PEOPLE_IMG = pygame.image.load(os.path.join("Assets/icon", "ppl.png"))
PEOPLE_IC = pygame.transform.scale(PEOPLE_IMG, (48, 48))
PLANT_IMG = pygame.image.load(os.path.join("Assets/icon", "plant.png"))
PLANT_IC = pygame.transform.scale(PLANT_IMG, (48, 48))
MONEY_IMG = pygame.image.load(os.path.join("Assets/icon", "money.png"))
MONEY_IC = pygame.transform.scale(MONEY_IMG, (48, 48))


# Test case for failure TODO: delete this line
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


def draw_game_intro_window():
    # Welcome page text
    welcome_text_surf = test_font.render("Welcome to Our Game!", True, 'White')
    welcome_rect = welcome_text_surf.get_rect(midtop=(500, 200))
    start_text_surf = test_font.render("Made by JAM", True, 'White')
    start_rect = start_text_surf.get_rect(midtop=(500, 250))

    # Render texts
    WIN.fill((139, 0, 18))
    WIN.blit(welcome_text_surf, welcome_rect)
    WIN.blit(start_text_surf, start_rect)

    # Render buttons
    render_button(500, 320, 125, 70, (139, 0, 18), 'White', 'Start')

    # Update display
    pygame.display.update()
    clock.tick(60)


def game_intro(plot: List[Event]):
    while True:
        draw_game_intro_window()
        start_button = press_button(500, 320, 125, 70, start_sound)
        if start_button:
            game(plot)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 214 * 235
def draw_middle_card(card: Card):

    sample_Card_Image = pygame.image.load(os.path.join('Assets/img', 'bullseye.png'))
    sample_Card_middle = pygame.transform.rotate(pygame.transform.scale(sample_Card_Image, card_size), card_2_angle)
    WIN.blit(sample_Card_middle, (card_2_position_x, card_2_position_y))


def draw_left_card(card: Card):
    sample_Card_Image = pygame.image.load(os.path.join('Assets/img', 'cardslay.png'))
    sample_Card_left = pygame.transform.rotate(pygame.transform.scale(sample_Card_Image, card_size), card_1_angle)
    WIN.blit(sample_Card_left, (card_1_position_x, card_1_position_y))


def draw_right_card(card: Card):
    sample_Card_Image = pygame.image.load(os.path.join('Assets/img', 'cardslay.png'))
    sample_Card_right = pygame.transform.rotate(pygame.transform.scale(sample_Card_Image, card_size), card_3_angle)
    WIN.blit(sample_Card_right, (card_3_position_x, card_3_position_y))


def draw_game_window(indices: List[Index], e: Event, card_pos: int):
    # Value initialization
    title = e_title_font.render(e.title, True, 'Black')
    desc = index_font.render(e.desc, True, 'Black')
    names = [index_font.render(index.id_str, True, 'Black') for index in indices]
    values = [number_font.render(str(index.value), True, 'Black') for index in indices]
    cards = e.cards

    WIN.fill((255, 255, 255))

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

    # Description Box
    pygame.draw.rect(WIN, "Black", (120, 125, 710, 260))
    pygame.draw.rect(WIN, "White", (125, 130, 700, 250))
    WIN.blit(title, (375, 150))
    WIN.blit(desc, (225, 250))

    # Cards
    if card_pos == 1:  # hover left
        draw_middle_card(cards[1])
        draw_right_card(cards[0])
        draw_left_card(cards[2])
    elif card_pos == 2:  # hover middle
        draw_left_card(cards[0])
        draw_right_card(cards[2])
        draw_middle_card(cards[1])
    else:  # hover right
        draw_left_card(cards[0])
        draw_middle_card(cards[1])
        draw_right_card(cards[2])

    # Update
    pygame.display.update()
    clock.tick(60)


def check_game_ended(i_event, plot):
    # Game over conditions
    if I_PRESIDENT.destroy():
        pygame.mixer.music.stop()
        finish(0, plot)
    elif I_PEOPLE.destroy():
        pygame.mixer.music.stop()
        finish(1, plot)
    elif I_ENVIRONMENT.destroy():
        pygame.mixer.music.stop()
        finish(2, plot)
    elif I_TREASURY.destroy():
        pygame.mixer.music.stop()
        finish(3, plot)
    elif i_event >= len(plot):
        pygame.mixer.music.stop()
        finish(4, plot)  # success


def game(plot: List[Event]):
    time.sleep(0.5)
    pygame.mixer.music.load('assets/sound/background.wav')
    pygame.mixer.music.play(-1)

    global card_1_position_y, card_2_position_y, card_3_position_y
    i_event = 0
    while True:
        draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cards = plot[i_event].cards
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and card_1_position_y > 200:
            card_1_position_y -= 10
            card_2_position_y = default
            card_3_position_y = default
            if card_1_position_y <= 200:
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 1)

                I_PRESIDENT.value = cards[0].effects[0]
                I_PEOPLE.value = cards[0].effects[1]
                I_ENVIRONMENT.value = cards[0].effects[2]
                I_TREASURY.value = cards[0].effects[3]
                i_event += 1

                card_1_position_y = default
                card_2_position_y = default
                card_3_position_y = default

                check_game_ended(i_event, plot)
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 1)

        elif keys[pygame.K_w] and card_2_position_y > 200:
            card_1_position_y = default
            card_2_position_y -= 10
            card_3_position_y = default

            if card_2_position_y <= 200:
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 2)

                I_PRESIDENT.value = cards[1].effects[0]
                I_PEOPLE.value = cards[1].effects[1]
                I_ENVIRONMENT.value = cards[1].effects[2]
                I_TREASURY.value = cards[1].effects[3]
                i_event += 1

                card_1_position_y = default
                card_2_position_y = default
                card_3_position_y = default

                check_game_ended(i_event, plot)
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 2)

        elif keys[pygame.K_e] and card_3_position_y > 200:
            card_1_position_y = default
            card_2_position_y = default
            card_3_position_y -= 10

            if card_3_position_y <= 200:
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 3)

                I_PRESIDENT.value = cards[2].effects[0]
                I_PEOPLE.value = cards[2].effects[1]
                I_ENVIRONMENT.value = cards[2].effects[2]
                I_TREASURY.value = cards[2].effects[3]
                i_event += 1

                card_1_position_y = default
                card_2_position_y = default
                card_3_position_y = default

                check_game_ended(i_event, plot)
                draw_game_window([I_PRESIDENT, I_PEOPLE, I_ENVIRONMENT, I_TREASURY], plot[i_event], 3)


def draw_finish_window(reason: int) -> None:
    if reason == 0:
        end_text_surf = test_font.render("The president FIRED you!", True, 'White')
    elif reason == 1:
        end_text_surf = test_font.render("Your people REVOLT against you!", True, 'White')
    elif reason == 2:
        end_text_surf = test_font.render("Mother earth is DYING!!", True, 'White')
    elif reason == 3:
        end_text_surf = test_font.render("Your office runs our of money!", True, 'White')
    else:
        end_text_surf = test_font.render("You well completed your job as a mayor!", True, 'White')

    WIN.fill((139, 0, 18))
    WIN.blit(end_text_surf, (220, 200))

    # Render buttons
    render_button(350, 320, 170, 70, (139, 0, 18), 'White', 'Re-Play')

    # Update
    pygame.display.update()
    # clock.tick(60)


def finish(reason: int, orig_plot: List[Event]):
    while True:
        draw_finish_window(reason)
        restart_button = press_button(350, 320, 170, 70, start_sound)
        if restart_button:
            I_PRESIDENT.reset(START)
            I_PEOPLE.reset(START)
            I_ENVIRONMENT.reset(START)
            I_TREASURY.reset(START)
            game(orig_plot)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    config_file = "plot.json"
    plots = Import(config_file).read_plots()

    while True:
        game_intro(plots[0])

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
