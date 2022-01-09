import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 960, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Our Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf',50)

#welcome page text
welcome_text_surf = test_font.render("Welcome to Our Game", False,'White')
welcome_rect = welcome_text_surf.get_rect(midtop = (800,300))
start_text_surf = test_font.render("Press S to Start or Q to quit", False,'White')
start_rect = start_text_surf.get_rect(midtop = (700,300))
#--------------#

def main():
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
    game_intro()
    pygame.display.update()


def game_intro():
    intro = True
    while intro:
        WIN.fill('Maroon')
        pygame.draw.rect(WIN,'White',welcome_rect)
        pygame.draw.rect(WIN,'White',start_rect)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_q:
                        pygame.quit()
                        exit()
                    if event.type == pygame.K_s:
                        intro = False



if __name__ == "__main__":
    main()

