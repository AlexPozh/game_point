from pygame.font import Font
from pygame.surface import Surface
from pygame import Rect
import pygame

from constants import *

def draw_text(
        text: str, 
        font: Font, 
        color: tuple, 
        surface: Surface, 
        x: int, 
        y: int
) -> None:
    """Ф-ция для отрисовки текста"""
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def draw_text_split(
        text: str, 
        font: Font, 
        color: tuple, 
        surface: Surface,
        rect: Rect, 
        line_spacing=5,
        padding_left: int = 10,
        padding_top: int = 10
) -> None:
    """Ф-ция отображает разбитый текст."""
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] < rect.width - padding_left * 2:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    
    if current_line:
        lines.append(current_line)

    # Начальная позиция с учетом отступа сверху
    y = rect.top + padding_top
    for line in lines:
        if y + font.get_height() > rect.bottom:
            break
        # Отрисовка текста с учетом отступа слева
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (rect.left + padding_left, y))
        y += font.get_height() + line_spacing


def play_music() -> None:
    """Ф-ция для проигрывания фоновой музыки"""
    pygame.mixer.music.load("music/dr-livesey.mp3")
    # Запуск музыки (-1 для зацикливания)
    pygame.mixer.music.play(-1)


def click_sound() -> None:
    """Ф-ция воспроизводит звук при нажатии на кнопку"""
    global SOUND_ACTIVE
    if SOUND_ACTIVE[0]:
        BUTTON_CLICK_SOUND.play()
    else:
        pass


def manage_music() -> None:
    """Ф-ция по управлению музыкой"""
    global MUSIC_ACTIVE
    try:
        if MUSIC_ACTIVE[0]:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    except Exception as error:
        print(error)