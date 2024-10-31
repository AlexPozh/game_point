import pygame

from main_menu import main_menu
from constants import *


pygame.display.set_caption("Circle.io")

def main() -> None:
    """Точка входа в игру Circle.io"""
    main_menu()


if __name__ == "__main__":
    main()
