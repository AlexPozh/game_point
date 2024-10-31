import sys
import webbrowser

import pygame
from pygame import Rect

from constants import *
from utills import draw_text, draw_text_split, click_sound, manage_music


def draw_settings_header(
                        text: str, 
                        x: float = 155, 
                        y: float = 50,
                        width: int = 300,
                        height: int = 66,
                        text_x: float = 495, 
                        text_y: float = 88
) -> None:
    """Ф-ция рисует шапку настроек"""
    # Объект для логотипа
    logo_rect = pygame.Rect(WINDOW_SIZE[0] // 2 - x, y, width, height)  
    pygame.draw.rect(screen, BLUE, logo_rect, border_radius=25)

    # Отрисовка текста "Настройки"
    draw_text(text, FONT_LOGO, BLACK, screen, text_x, text_y)


def draw_back_button() -> Rect:
    """Ф-ция рисует кнопку назад"""
    # Отрисовка кнопки назад
    back_button_rect = BACK.get_rect(topleft=(130, 57))
    screen.blit(BACK, back_button_rect)
    
    return back_button_rect


def rules() -> None:
    """Ф-ция рисует правила игры"""
    click = False
    while True:
        # Рисуем наш фон меню
        screen.blit(BACKGROUND, (0, 0))

        # Шапка настроек
        draw_settings_header('Правила')

         # Кнопка "Назад"
        back_button_rect = draw_back_button()

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()
        
        rule_text_1 = pygame.Rect(WINDOW_SIZE[0] // 2 - 400, 160, 800, 120)
        rule_text_2 = pygame.Rect(WINDOW_SIZE[0] // 2 - 400, 300, 800, 225)
        rule_text_3 = pygame.Rect(WINDOW_SIZE[0] // 2 - 400, 560, 800, 70)
        rule_text_4 = pygame.Rect(WINDOW_SIZE[0] // 2 - 400, 650, 800, 90)

        # Проверяем нажатие кнопок
        if back_button_rect.collidepoint((mx, my)):
            if click:
                click_sound()
                return  # Выходим из ф-ции
        # Рисуем прямоугольнкии с правилами
        pygame.draw.rect(screen, PINK, rule_text_1, border_radius=40)
        pygame.draw.rect(screen, PINK, rule_text_2, border_radius=40)
        pygame.draw.rect(screen, PINK, rule_text_3, border_radius=40)
        pygame.draw.rect(screen, PINK, rule_text_4, border_radius=40)

        # Отрисовка текста кнопок меню
        draw_text_split('1. Игровое поле и точки. Игра ведётся на клетчатом поле, игроки поочерёдно ходят в точки пересечения клеток. Пункт, в который поставлена точка, остаётся занятым до конца игры, перемещать ранее поставленные точки или снимать их с поля нельзя.', 
                FONT_RULES, BLACK, screen, rule_text_1, padding_left=14)
        draw_text_split('2. Окружение. Цель игры — окружить точки соперника. Окружение — это создание на определённом участке игрового поля области, замкнутой внутри непрерывной непересекающейся цепи точек одного цвета, отстоящих друг от друга не более, чем на одну клетку по горизонтали, вертикали или диагонали. При этом в данной области в момент замыкания обязательно должны находиться точки другого цвета (одна или более). В таком случае область закрашивается в цвет создавших окружение точек, а точки соперника внутри неё выключаются из дальнейшей игры, считаясь захваченными, и идут в зачёт окружившему.', 
                FONT_RULES, BLACK, screen, rule_text_2)
        draw_text_split('3. Стартовая позиция. Игра начинается с пустого поля. В этом случае точек на поле нет, и оба игрока делают ходы в любые пункты.', 
                FONT_RULES, BLACK, screen, rule_text_3)
        draw_text_split('4. Подсчет очков. По окончании игры производится подсчет окружённых точек. Победителем считается игрок, захвативший хотя бы на одну точку больше, чем соперник. При равенстве по этому показателю объявляется ничья.', 
                FONT_RULES, BLACK, screen, rule_text_4)

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


def sounds() -> None:
    """Ф-ция рисует настройки звука"""
    global SOUND_ACTIVE, MUSIC_ACTIVE
    click = False
    while True:
        # Проверка настроек музыки
        manage_music()

        # Рисуем наш фон меню
        screen.blit(BACKGROUND, (0, 0))

        # Шапка настроек
        draw_settings_header('Звук', text_y=84)

        # Кнопка "Назад"
        back_button_rect = draw_back_button()

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Объекты кнопок
        button_music = pygame.Rect(WINDOW_SIZE[0] // 2 - 170, 200, 350, 56)
        button_sounds = pygame.Rect(WINDOW_SIZE[0] // 2 - 170, 300, 350, 56)

        pygame.draw.rect(screen, PINK, button_music, border_radius=15)
        pygame.draw.rect(screen, PINK, button_sounds, border_radius=15)

        # Проверяем нажатие кнопок
        if back_button_rect.collidepoint((mx, my)):
            if click:
                click_sound()
                return  # Выходим из ф-ции
        if button_music.collidepoint((mx, my)):
            if click:
                if MUSIC_ACTIVE[0]:
                    MUSIC_ACTIVE[0] = False
                else:
                    MUSIC_ACTIVE[0] = True

        if button_sounds.collidepoint((mx, my)):
            if click:
                if SOUND_ACTIVE[0]:
                    SOUND_ACTIVE[0] = False
                else:
                    SOUND_ACTIVE[0] = True
        
         # Значки у кнопок
        screen.blit(SWITCH_ON if MUSIC_ACTIVE[0] else SWITCH_OFF, (587, 196))
        screen.blit(SWITCH_ON if SOUND_ACTIVE[0] else SWITCH_OFF, (587, 296))

        # Отрисовка текста кнопок меню
        draw_text('Музыка', FONT, BLACK, screen, WINDOW_SIZE[0] // 2 - 110, 230)
        draw_text('Звук в игре', FONT, BLACK, screen, WINDOW_SIZE[0] // 2 - 90, 330)

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

def about_us() -> None:
    """Ф-ция рисует информацию об игре"""
    click = False
    while True:
        # Рисуем наш фон меню
        screen.blit(BACKGROUND, (0, 0))

        # Шапка настроек
        draw_settings_header('О приложении', width=400, x=180, text_x=517)

        # Кнопка "Назад"
        back_button_rect = draw_back_button()

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()
 
        # Объекты кнопок
        button_rate_us = pygame.Rect(WINDOW_SIZE[0] // 2 - 170, 200, 360, 56)
        button_link_tg = pygame.Rect(WINDOW_SIZE[0] // 2 - 170, 300, 360, 56)

        # Проверяем нажатие кнопок
        if back_button_rect.collidepoint((mx, my)):
            if click:
                click_sound()
                return  # Выходим из ф-ции
            
        if button_rate_us.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_rate_us, border_radius=15)
            if click:
                click_sound()
                webbrowser.get(using='google-chrome').open_new_tab(POLL_LINK)
        else:
            pygame.draw.rect(screen, PINK, button_rate_us, border_radius=15)

        if button_link_tg.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_link_tg, border_radius=15)
            if click:
                click_sound()
                webbrowser.get(using='google-chrome').open_new_tab(CHANNEL_LINK)
        else:
            pygame.draw.rect(screen, PINK, button_link_tg, border_radius=15)

        # Значки у кнопок
        screen.blit(STAR, (337, 213))
        screen.blit(TG, (337, 313))

        # Отрисовка текста кнопок меню
        draw_text('Оцените наше приложение', FONT, BLACK, screen, WINDOW_SIZE[0] // 2 + 24, 230)
        draw_text('@CirCle', FONT, BLACK, screen, WINDOW_SIZE[0] // 2 - 74, 330)

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


def settings() -> None:
    """Ф-ция по игровым настройкам"""
    click = False
    while True:
        # Рисуем наш фон меню
        screen.blit(BACKGROUND, (0, 0))

        # Шапка настроек (текст "Настройки")
        draw_settings_header('Настройки')

        # Кнопка "Назад"
        back_button_rect = draw_back_button()

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Объекты кнопок настроек
        button_rules = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 200, 200, 56)
        button_sounds = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 300, 200, 56)
        button_about_us = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 400, 200, 56)

        # Проверяем нажатие кнопок
        if back_button_rect.collidepoint((mx, my)):
            if click:
                click_sound()
                return  # Выходим из ф-ции настроек

        if button_rules.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_rules, border_radius=15)
            if click:
                click_sound()
                rules()
        else:
            pygame.draw.rect(screen, PINK, button_rules, border_radius=15)

        if button_sounds.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_sounds, border_radius=15)
            if click:
                click_sound()
                sounds()
        else:
            pygame.draw.rect(screen, PINK, button_sounds, border_radius=15)

        if button_about_us.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_about_us, border_radius=15)
            if click:
                click_sound()
                about_us()
        else:
            pygame.draw.rect(screen, PINK, button_about_us, border_radius=15)

        # Отрисовка текста кнопок меню
        draw_text('Правила', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 230)
        draw_text('Звук', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 330)
        draw_text('О приложении', FONT, BLACK, screen, WINDOW_SIZE[0] // 2, 430)

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