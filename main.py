import sys
import pygame
from api import ImportSetting as Import

pygame.init()
WIDTH, HEIGHT = 960, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Our Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Abel-Regular.ttf',50)

#dummy arg, changes required
fail_id = 3

#sounds
start_sound = pygame.mixer.Sound('assets/sound/start.wav')
#--------


def create_button(x, y, width, height, hovercolor, defaultcolor, message, sound):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    btn_text_surf = test_font.render(message, True, hovercolor)
    btn_text_surf_hover = test_font.render(message, True, defaultcolor)
    btn_text_rect = btn_text_surf.get_rect(midtop=(x + width/2, y))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(WIN, hovercolor, (x, y, width, height))
        WIN.blit(btn_text_surf_hover, btn_text_rect)
        if click[0] == 1:
            pygame.mixer.Sound.play(sound)
            return True
    else:
        pygame.draw.rect(WIN, defaultcolor, (x, y, width, height))
        WIN.blit(btn_text_surf, btn_text_rect)


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
        start_button = create_button(500, 320, 125, 70, (139, 0, 18), 'White', 'Start', start_sound)
        if start_button:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)
        return True

def finish(id):
    if id == 0:
        end_text_surf = test_font.render("The president FIRED you!", True, 'White')
    elif id == 1:
        end_text_surf = test_font.render("Your people REVOLT against you!", True, 'White')
    elif id == 2:
        end_text_surf = test_font.render("Mother earth is DYING!\n EVERYONE IS DOOMED!", True, 'White')
    else:
        end_text_surf = test_font.render("Your office runs our of money!", True, 'White')
    
    while True:
        WIN.fill((139, 0, 18))
        WIN.blit(end_text_surf, (280, 200))
        restart_button = create_button(350, 320, 170, 70, (139, 0, 18), 'White', 'Re-Play', start_sound)
        if restart_button:
            game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def game():
    game_text_surf = test_font.render("Here to Code the Game", True, 'White')
    
    while True:
        WIN.fill((0, 0, 0))
        WIN.blit(game_text_surf, (500, 300))
        end_button = create_button(100, 320, 125, 70, (139, 0, 18), 'White', 'End', start_sound)
        if end_button:
            finish(fail_id)
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
