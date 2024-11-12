import sys
from datetime import timedelta

import pygame

from constants import *
from utills import draw_text, click_sound
from game_settings import settings

def draw_grid() -> None:
    """Ф-ция рисует игровую сетку"""
    # Рисуем сетку и координаты
    for i in range(GRID_SIZE + 1):
        # Рисуем горизонтальные линии сетки
        pygame.draw.line(screen, BLACK, (250, 200 + i * CELL_SIZE), (250 + GRID_SIZE * CELL_SIZE, 200 + i * CELL_SIZE))
        
        # Рисуем вертикальные линии сетки
        pygame.draw.line(screen, BLACK, (250 + i * CELL_SIZE, 200), (250 + i * CELL_SIZE, 200 + GRID_SIZE * CELL_SIZE))
        if i < GRID_SIZE:
            # Рисуем цифры (1-20)
            number = FONT_GAME_GRID.render(str(i + 1), True, BLACK)
            screen.blit(number, (225, 200 + i * CELL_SIZE + CELL_SIZE // 4))
            # Рисуем буквы (a-u)
            letter = FONT_GAME_GRID.render(chr(97 + i), True, BLACK)
            screen.blit(letter, (255 + i * CELL_SIZE + CELL_SIZE // 4, 182))


def draw_timer(time_left: int) -> None:
    """Ф-ция рисует таймер"""
    # Отображение таймера
    time = str(timedelta(seconds=time_left))
    timer_text = FONT.render("0" + time if int(time[0]) <= 9 else time, True, BLACK)
    #pygame.draw.rect(screen, GRAY, (350, 10, 115, 30), border_radius=25)
    #screen.blit(timer_text, (360, 15))
    pygame.draw.rect(screen, GRAY, (450, 145, 115, 30), border_radius=25)
    screen.blit(timer_text, (460, 150))

def draw_players(
                player1_name: str,
                player2_name: str,
                player_turn: int, 
                player1_score: int = 0, 
                player2_score: int = 0
) -> None:
    """Ф-ция рисует иконки игроков, их счет и имена"""
    # Отображение имени игрока
    pygame.draw.rect(screen, BLUE if player_turn == 1 else GRAY, (315, 65, 110, 35), border_radius=20)
    pygame.draw.rect(screen, LIGHT_RED if player_turn == 2 else GRAY, (575, 65, 110, 35), border_radius=20)
    
    # Красный и синий фон за иконкой игрока
    pygame.draw.rect(screen, DARK_BLUE, (430, 50, 60, 60), border_radius=12)
    pygame.draw.rect(screen, RED, (510, 50, 60, 60), border_radius=12)
    
    # Серый фон для счета игрока
    pygame.draw.rect(screen, GRAY, (335, 110, 60, 35), border_radius=12)
    pygame.draw.rect(screen, GRAY, (595, 110, 60, 35), border_radius=12)

    # Отображание иконок
    screen.blit(PLAYER_ICON, (440, 60))
    screen.blit(PLAYER_ICON, (520, 60))

    # Имя игрока 1 и его счет
    player1_name = FONT.render(player1_name, True, BLACK)
    screen.blit(player1_name, (328, 73))
    player1_score_text = FONT.render(str(player1_score), True, BLACK)
    screen.blit(player1_score_text, (350, 118))

    # Имя игрока 2 и его счет
    player2_name = FONT.render(player2_name, True, BLACK)
    screen.blit(player2_name, (588, 73))
    player2_score_text = FONT.render(str(player2_score), True, BLACK)
    screen.blit(player2_score_text, (615, 118))

def draw_menu_header(
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


def draw_menu() -> None | bool:
    """Ф-ция отображает меню в игрвом поле"""
    click = False
    while True:
        screen.blit(BACKGROUND, (0, 0))
        
        # Отображение шапки меню
        draw_menu_header("Меню")
        
        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Кнопки меню
        button_settings = pygame.Rect(400, 200, 200, 50)
        button_exit = pygame.Rect(400, 270, 200, 50)
        button_resume = pygame.Rect(400, 340, 200, 50)
        
        if button_settings.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_settings, border_radius=15)
            if click:
                click_sound()
                settings()
        else:
            pygame.draw.rect(screen, PINK, button_settings, border_radius=15)

        if button_exit.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_exit, border_radius=15)
            if click:
                click_sound()
                return True
        else:
            pygame.draw.rect(screen, PINK, button_exit, border_radius=15)

        if button_resume.collidepoint((mx, my)):
            pygame.draw.rect(screen, WHITE, button_resume, border_radius=15)
            if click:
                click_sound()
                return
        else:
            pygame.draw.rect(screen, PINK, button_resume, border_radius=15)
        
        # Отрисовка текста на кнопках
        draw_text("Настройки", FONT, BLACK, screen, 500, 225)
        draw_text("Выйти из игры", FONT, BLACK, screen, 500, 295)
        draw_text("Вернуться в игру", FONT, BLACK, screen, 500, 365)

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


def draw_moves(board: list[list[int]], last_move: tuple[int, int]) -> None:
    """Ф-ция рисует ходы игроков"""
    for y in range(19):
        for x in range(19):
            if board[y][x] == 1:  # Синий игрок
                pygame.draw.circle(screen, DARK_BLUE, (GRID_OFFSET_X + x * CELL_SIZE, GRID_OFFSET_Y + y * CELL_SIZE), 10)
            elif board[y][x] == 2:  # Красный игрок
                pygame.draw.circle(screen, RED, (GRID_OFFSET_X + x * CELL_SIZE, GRID_OFFSET_Y + y * CELL_SIZE), 10)

def is_fully_surrounded(x: int, y: int, board: list[list[int]], player: int) -> bool:
    """Проверяет, окружена ли группа точек со всех сторон."""
    visited = set()
    stack = [(x, y)]
    surrounded = True

    while stack:
        cx, cy = stack.pop()
        visited.add((cx, cy))

        # Проверяем все направления
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 19 and 0 <= ny < 19:
                if board[ny][nx] == 0:  # Если есть пустая клетка, группа не окружена
                    surrounded = False
                elif board[ny][nx] == player and (nx, ny) not in visited:
                    stack.append((nx, ny))
            else:
                # Если клетка выходит за пределы поля, группа не окружена
                surrounded = False

    return surrounded, visited


def capture_group(points: set[tuple[int, int]], board: list[list[int]], player: int) -> int:
    """Захватывает группу точек и возвращает количество захваченных очков."""
    for (x, y) in points:
        board[y][x] = player
    return len(points)


def capture_points(x: int, y: int, player_turn: int, board: list[list[int]]) -> int:
    """Подсчитывает и захватывает окруженные группы точек противника."""
    captured_points = 0
    opponent = 3 - player_turn

    # Проверка всех соседей для возможного захвата групп
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 19 and 0 <= ny < 19 and board[ny][nx] == opponent:
            surrounded, points_to_capture = is_fully_surrounded(nx, ny, board, opponent)
            if surrounded:
                captured_points += capture_group(points_to_capture, board, player_turn)

    return captured_points

def draw_winner(text: str) -> None:
    """Ф-ция рисует табличку победителя"""
    winner_rect = pygame.Rect(200, 300, 600, 300)
    pygame.draw.rect(screen, BLUE, winner_rect, border_radius=25)
    draw_text(text, FONT_LOGO, RED, screen,  500, 440)
    
    return_menu_button = pygame.Rect(450, 500, 100, 40)
    pygame.draw.rect(screen, PINK, return_menu_button, border_radius=25)
    draw_text("OK", FONT, BLACK, screen,  500, 520)
    
    click = False

    while True:
        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Проверяем нажатие кнопок
        if return_menu_button.collidepoint((mx, my)):
            if click:
                click_sound()
                return  # Выходим из ф-ции
        
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


def check_name(name: str) -> bool:
    """Ф-ция проверяет введенное имя на соответствие правилам"""
    if len(name) == 1 or len(name) > 7 or any([letter in "«,.:@$;\~`”»/<>+-=»" for letter in name]):
        return False
    return True

def ask_name(player_num: int) -> str:
    """Функция для ввода имени игрока"""
    input_box = pygame.Rect(450, 250, 300, 50)
    color_active = pygame.Color('dodgerblue')
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    active = False
    text = ""
    done = False
    is_correct_name = True

    while not done:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Если игрок нажимает на поле ввода
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Нажатие Enter завершает ввод
                        if len(text) == 0:
                            text = f"Игрок {player_num}"        
                            done = True
                        elif check_name(text):
                            done = True
                        else:
                            is_correct_name = False
                            
                    elif event.key == pygame.K_BACKSPACE:
                        # Удаление символа
                        text = text[:-1]
                    else:
                        # Добавление нового символа
                        text += event.unicode

        # Отрисовка на экране
        if  not is_correct_name:
            txt_error = FONT.render(f"Нельзя использовать символы «,.:@$;\~`”»/<>+-=». Попробуй еще раз!»", True, BLACK)
            screen.blit(txt_error, (input_box.x - 350, input_box.y + 70))
        txt_surface = FONT.render(f"Введите имя для игрока {player_num}: " + text, True, BLACK)
        screen.blit(txt_surface, (input_box.x - 300, input_box.y + 15))
        pygame.draw.rect(screen, color, input_box, 2)
        
        # Обновление экрана
        pygame.display.flip()

    return text

def game() -> None:
    """Ф-ция для игры"""
    player1_name = ask_name(1)
    player2_name = ask_name(2)

    clock = pygame.time.Clock()
    
    player_turn = 1
    
    player1_score, player2_score = 0, 0
    
    time_left = TIMER_START

    pause_ticks = 0 

    start_ticks = pygame.time.get_ticks()

    menu_button = pygame.Rect(450, 725, 100, 40)

    timer_paused = False
    
    # Сетка для отслеживания ходов игроков (0 - пустая клетка, 1 - синий, 2 - красный)
    board = [[0] * 20 for _ in range(20)]
    
    # Координаты последнего хода
    last_move = None  
    
    while True:
        # Заполняем фон белым цветом
        screen.fill(WHITE)

        # Текущие координаты мыши
        mx, my = pygame.mouse.get_pos()

        # Обработка событий
        for event in pygame.event.get():
            # Закрытие окна игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Нажатие кнопки Меню
                if menu_button.collidepoint((mx, my)):
                    click_sound()

                    # Таймер ставится на паузу
                    timer_paused = not timer_paused
                    if timer_paused:
                        pause_ticks = pygame.time.get_ticks()
                        if draw_menu():
                            return

                        # Таймер продолжает отсчет
                        else:
                            timer_paused = not timer_paused
                            start_ticks += pygame.time.get_ticks() - pause_ticks
                # Ход игроков
                else:
                    # Обработка хода игрока на поле
                    grid_x, grid_y = (mx - GRID_OFFSET_X) // CELL_SIZE, (my - GRID_OFFSET_Y) // CELL_SIZE
                    print(f"Координаты мыши по X - {mx} и Y - {my}.\nВычисленные координаты X - {grid_x} и  Y - {grid_y} для точки.")
                    if 0 <= grid_x < 19 and 0 <= grid_y < 19 and board[grid_y][grid_x] == 0:
                        # Устанавливаем точку текущего игрока
                        board[grid_y][grid_x] = player_turn
                        # Захват очков
                        points = capture_points(grid_x, grid_y, player_turn, board)
                        if player_turn == 1:
                            player1_score += points
                        else:
                            player2_score += points

                        # Передача хода
                        player_turn = 3 - player_turn

        # Проверка на наведение на кнопку Меню
        if menu_button.collidepoint((mx, my)):
            # Увеличение на 5%
            enlarged_rect = menu_button.inflate(10, 5)  
            pygame.draw.rect(screen, PINK, enlarged_rect, border_radius=15)
        else:
            pygame.draw.rect(screen, PINK, menu_button, border_radius=15)
        
        # Отрисовка текста кнпоки меню
        draw_text("Меню", FONT, BLACK, screen, 500, 745)
        # Отрисовка доски
        draw_grid()

        # Отрисовка последнего хода игрока
        draw_moves(board, last_move)
                
        # Отрисовка таймера
        draw_timer(time_left)
       
        # Отрисовка иконок игроков
        draw_players(player1_name, player2_name, player_turn, player1_score, player2_score)


        if not timer_paused:
            # Проверка таймера игры
            second_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        
            time_left = TIMER_START - second_passed
        
            if time_left <= 0:
                if player1_score > player2_score:
                    draw_winner(f"{player1_name} победил!")
                    return

                elif player2_score > player1_score:
                    draw_winner(f"{player2_name} победил!")
                    return
                else:
                    draw_winner("Ничья!")
                    return

        if player1_score > player2_score and player1_score >= POINTS:
                draw_winner(f"{player1_name} победил!")
                return
        
        if player2_score > player1_score and player2_score >= POINTS:
                draw_winner(f"{player2_name} победил!")
                return
        
        # Обновление отображения на экране
        pygame.display.flip()
        
        # Кол-во fps
        clock.tick(60)