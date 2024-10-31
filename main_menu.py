import sys
from time import sleep

import pygame

from utills import draw_text, play_music, click_sound
from game_settings import settings
from game import game
from constants import *


def draw_game_logo() -> None:
    # Объект для логотипа
    logo_rect = pygame.Rect(WINDOW_SIZE[0] // 2 - 140, 50, 275, 66)  
    pygame.draw.rect(screen, BLUE, logo_rect, border_radius=25)

    # Отрисовка изображения логотипа (картинки)
    screen.blit(LOGO, (365, 50))
    
    # Отрисовка текста "Circle.io"
    draw_text('Circle.io', FONT_LOGO, BLACK, screen, 528, 88)


def main_menu() -> None:
    """Главное меню игры"""
    # Запуск музыки
    play_music()

    click = False
    while True:
        # Рисуем наш фон меню
        screen.blit(BACKGROUND, (0, 0))

        # Отрисовка логотипа игры
        draw_game_logo()

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Объекты кнопок главного меню
        button_start_game = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 200, 200, 56)
        button_settings = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 300, 200, 56)
        button_quit = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 400, 200, 56)

        # Проверяем нажатие кнопок
        if button_start_game.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_start_game, border_radius=15)
            if click:
                click_sound()
                game()
        else:
            pygame.draw.rect(screen, PINK, button_start_game, border_radius=15)

        if button_settings.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_settings, border_radius=15)
            if click:
                click_sound()
                settings()
        else:
            pygame.draw.rect(screen, PINK, button_settings, border_radius=15)

        if button_quit.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_quit, border_radius=15)
            if click:
                click_sound()
                sleep(0.6)
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, PINK, button_quit, border_radius=15)

        # Отрисовка текста кнопок меню
        draw_text('Играть', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 230)
        draw_text('Настройки', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 330)
        draw_text('Выход', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 430)

        # Получение событий игры
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    click = True

        pygame.display.update()
