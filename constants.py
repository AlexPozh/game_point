import pygame

# Инициализация Pygame
pygame.init()

GRID_SIZE = 20   # Размер игральной доски 20x20
CELL_SIZE = 25   # Размер одной клетки
GRID_OFFSET_X = 250
GRID_OFFSET_Y = 200

# Время игры
TIMER_START = 600 # 10 минут

# Кол-во очков для выигрыша
POINTS = 10

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (205, 92, 92)
BLUE = (149, 210, 254)
DARK_BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (225, 139, 255)
BG_COLOR = (255, 255, 255)

# Размер окна
WINDOW_SIZE = (1000, 800)

# Объект окна
screen = pygame.display.set_mode(WINDOW_SIZE)

# Загрузка фонового изображения
BACKGROUND = pygame.image.load("templates/background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, WINDOW_SIZE)

SHORT_BACKGROUND = pygame.transform.scale(BACKGROUND, (500, 700))
# Логотип игры
LOGO = pygame.image.load("templates/Logo_2.png")
LOGO = pygame.transform.scale(LOGO, (60, 60))

# Кнопка назад
BACK = pygame.image.load("templates/back.png")
BACK = pygame.transform.scale(BACK, (45, 45))

# Значок телеграм и звезда
TG = pygame.image.load("templates/telegram.png")
TG = pygame.transform.scale(TG, (30, 30))

STAR = pygame.image.load("templates/star.png")
STAR = pygame.transform.scale(STAR, (30, 30))

# Значок игрока
PLAYER_ICON = pygame.image.load("templates/user_icon.png")
PLAYER_ICON = pygame.transform.scale(PLAYER_ICON, (40, 40))

# Кнопки вкл и выключить
SWITCH_OFF = pygame.image.load("templates/switch-off.png")
SWITCH_OFF = pygame.transform.scale(SWITCH_OFF, (53, 66))

SWITCH_ON = pygame.image.load("templates/switch_on.png")
SWITCH_ON = pygame.transform.scale(SWITCH_ON, (53, 66))

# URL на пост и группу в телеграм
POLL_LINK = "https://web.telegram.org/a/#-4566839864"
CHANNEL_LINK = "https://web.telegram.org/a/#-4566839864"

# Шрифты
pygame.font.init()
FONT = pygame.font.SysFont('arial', 25)
FONT_GAME_GRID = pygame.font.SysFont('arial', 15)
FONT_RULES = pygame.font.SysFont('arial', 20)
FONT_LOGO = pygame.font.SysFont('arial', 55)

# Музыка
BUTTON_CLICK_SOUND = pygame.mixer.Sound("music/a.wav")

# Настройки музыки
SOUND_ACTIVE = [True]
MUSIC_ACTIVE = [True]

