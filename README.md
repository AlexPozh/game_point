# Circle.io
Игра *"Точки"*

Чтобы запустить проект у себя:
1) Скачиваем `python 3.11.8` - [ТЫК](https://www.python.org/downloads/release/python-3118/)
2) Создаем новую папку.
3) Открываем папку с помощью редактора кода.
4) Клониуруем репозиторий через терминал командой `git clone https://github.com/AlexPozh/game_point.git`
5) Скачиваем все необходимые пакеты командой `pip install -r requirements.txt`
6) Запускаем проект командой `python3 main.py` или `python main.py` (Нужно находиться внутри папки `src/`, в терминале смотрите внимательнее!!!)


При разработке нужно создать **ОТДЕЛЬНУЮ ВЕТКУ!**
1) Склонировали проект (пункт *4* выше).
2) Проверяем, в какой ветке находимся: в консоли `git branch` и должно выглядеть как на скрине ниже.

![image](https://github.com/user-attachments/assets/15c039e1-2811-4cd4-98db-bf31b53d9f64)
4) Создаем новую ветку и сразу переключаемся на нее: `git checkout -b имя_ветки`
5) Можно проверить командой `git branch`.
6) Делаем свою работу...
7) Подготавливаем изменения для коммита командой `git add .`
8) Делаем коммит `git commit -m "какое-то_сообщение"`
9) Пушим изменения, создавая pull request командой `git push origin название_новой_ветки`
