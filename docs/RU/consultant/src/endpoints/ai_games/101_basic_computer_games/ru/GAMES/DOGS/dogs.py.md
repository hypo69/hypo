# Анализ кода модуля `dogs.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, разбит на функции, что делает его более читаемым и понятным.
    -  Используются константы для определения размера поля, что облегчает модификацию кода.
    -  Присутствуют комментарии, объясняющие логику работы функций.
    -  Реализованы проверки ввода пользователя, что предотвращает ошибки.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST) для модуля, функций и переменных.
    -  Не используется логирование ошибок.
    -  Избыточное использование `while True` циклов.
    -  Некоторые блоки кода можно упростить и сделать более читаемыми.
    -  Нет проверки на корректность ввода направления для собак (L,R,U,D)
    -  Нет обработки исключений

**Рекомендации по улучшению**

1.  **Документирование**:
    -   Добавить docstring в формате RST для модуля, всех функций и методов для генерации документации.
2.  **Логирование**:
    -   Использовать `logger.error` для логирования ошибок вместо стандартного `try-except`, где это возможно.
3.  **Упрощение циклов**:
    -   Избегать бесконечных `while True` циклов, где это возможно, переписав логику с более явными условиями выхода.
4.  **Улучшение читаемости**:
    -  Разбить длинные блоки кода на более мелкие, чтобы улучшить читаемость.
    -   Использовать более информативные названия переменных, где это возможно.
5.  **Обработка ошибок:**
    -  Добавить обработку исключений для возможных ошибок, например, при вводе пользователя.

**Оптимизированный код**

```python
"""
Модуль "Собаки"
=====================

Модуль представляет собой текстовую игру, в которой игрок управляет двумя собаками,
пытаясь поймать воров. Игрок вводит команды для перемещения собак, а воры перемещаются
случайно. Цель игры - поймать воров за минимальное количество ходов.

:Модуль: `dogs.py`
:Версия: 1.0
"""
import random
from src.logger.logger import logger # импортируем logger

# Константы для размеров поля
FIELD_SIZE = 10

def create_field():
    """
    Создает игровое поле размером FIELD_SIZE x FIELD_SIZE, представляя его как список списков.

    :return: Двумерный список, представляющий игровое поле.
    :rtype: list[list[str]]
    """
    return [['.' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]


def place_object(field: list[list[str]], symbol: str) -> tuple[int, int]:
    """
    Размещает объект (собаку или вора) на случайной свободной позиции на поле.

    :param field: Двумерный список, представляющий игровое поле.
    :type field: list[list[str]]
    :param symbol: Символ объекта, который нужно разместить на поле.
    :type symbol: str
    :return: Кортеж с координатами (row, col) размещенного объекта.
    :rtype: tuple[int, int]
    """
    while True:
        row = random.randint(0, FIELD_SIZE - 1)
        col = random.randint(0, FIELD_SIZE - 1)
        if field[row][col] == '.':
            field[row][col] = symbol
            return row, col


def print_field(field: list[list[str]]):
    """
    Выводит текущее состояние игрового поля на экран.

    :param field: Двумерный список, представляющий игровое поле.
    :type field: list[list[str]]
    """
    for row in field:
        print(' '.join(row))


def get_user_command() -> str:
    """
    Запрашивает у пользователя команду для перемещения собак.

    Команды:
      - 'L' - переместить обеих собак влево
      - 'R' - переместить обеих собак вправо
      - 'U' - переместить обеих собак вверх
      - 'D' - переместить обеих собак вниз
      - 'F' - переместить первую собаку
      - 'S' - переместить вторую собаку

    :return: Строка - команда пользователя.
    :rtype: str
    """
    while True:
        command = input("Введите команду (L/R/U/D/F/S): ").upper()
        if command in ('L', 'R', 'U', 'D', 'F', 'S'):
            return command
        else:
            print("Неверная команда. Попробуйте снова.")


def get_direction(dog_number: int) -> str:
    """
    Запрашивает у пользователя направление для перемещения одной из собак.

    :param dog_number: Номер собаки (1 или 2).
    :type dog_number: int
    :return: Строка - направление движения собаки (L/R/U/D).
    :rtype: str
    """
    while True:
        direction = input(f"Введите направление для {dog_number}-й собаки (L/R/U/D): ").upper()
        if direction in ('L', 'R', 'U', 'D'):
            return direction
        else:
            print("Неверное направление. Попробуйте снова.")


def move_dogs(field: list[list[str]], dog1: tuple[int, int], dog2: tuple[int, int], command: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Перемещает собак в соответствии с командой пользователя.

    :param field: Игровое поле.
    :type field: list[list[str]]
    :param dog1: Координаты первой собаки (row, col).
    :type dog1: tuple[int, int]
    :param dog2: Координаты второй собаки (row, col).
    :type dog2: tuple[int, int]
    :param command: Команда пользователя.
    :type command: str
    :return: Кортеж с новыми координатами собак ((row1, col1), (row2, col2)).
    :rtype: tuple[tuple[int, int], tuple[int, int]]
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2
    
    field[dog1_row][dog1_col] = '.' # Очищаем старую позицию
    field[dog2_row][dog2_col] = '.'
    
    if command == 'L':
        if dog1_col > 0:
            dog1_col -= 1
        if dog2_col > 0:
            dog2_col -= 1
    elif command == 'R':
        if dog1_col < FIELD_SIZE - 1:
            dog1_col += 1
        if dog2_col < FIELD_SIZE - 1:
            dog2_col += 1
    elif command == 'U':
        if dog1_row > 0:
            dog1_row -= 1
        if dog2_row > 0:
            dog2_row -= 1
    elif command == 'D':
        if dog1_row < FIELD_SIZE - 1:
            dog1_row += 1
        if dog2_row < FIELD_SIZE - 1:
            dog2_row += 1
    elif command == 'F':
        direction = get_direction(1)
        if direction == 'L' and dog1_col > 0:
            dog1_col -= 1
        elif direction == 'R' and dog1_col < FIELD_SIZE - 1:
            dog1_col += 1
        elif direction == 'U' and dog1_row > 0:
            dog1_row -= 1
        elif direction == 'D' and dog1_row < FIELD_SIZE - 1:
             dog1_row += 1
    elif command == 'S':
        direction = get_direction(2)
        if direction == 'L' and dog2_col > 0:
            dog2_col -= 1
        elif direction == 'R' and dog2_col < FIELD_SIZE - 1:
            dog2_col += 1
        elif direction == 'U' and dog2_row > 0:
            dog2_row -= 1
        elif direction == 'D' and dog2_row < FIELD_SIZE - 1:
            dog2_row += 1
    
    field[dog1_row][dog1_col] = 'D'
    field[dog2_row][dog2_col] = 'D'
    return (dog1_row, dog1_col), (dog2_row, dog2_col)


def move_thieves(field: list[list[str]], thief1: tuple[int, int], thief2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Перемещает воров случайным образом на игровом поле.

    :param field: Двумерный список, представляющий игровое поле.
    :type field: list[list[str]]
    :param thief1: Координаты первого вора (row, col).
    :type thief1: tuple[int, int]
    :param thief2: Координаты второго вора (row, col).
    :type thief2: tuple[int, int]
    :return: Кортежи с новыми координатами воров ((row1, col1), (row2, col2)).
    :rtype: tuple[tuple[int, int], tuple[int, int]]
    """
    thief1_row, thief1_col = thief1
    thief2_row, thief2_col = thief2
    
    field[thief1_row][thief1_col] = '.'
    field[thief2_row][thief2_col] = '.'
    
    
    
    # Случайное перемещение первого вора
    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief1_row, new_thief1_col = thief1_row, thief1_col
        if direction == 'L' and thief1_col > 0:
            new_thief1_col -= 1
        elif direction == 'R' and thief1_col < FIELD_SIZE - 1:
            new_thief1_col += 1
        elif direction == 'U' and thief1_row > 0:
            new_thief1_row -= 1
        elif direction == 'D' and thief1_row < FIELD_SIZE - 1:
            new_thief1_row += 1
        if field[new_thief1_row][new_thief1_col] == '.' or (new_thief1_row, new_thief1_col) == (thief2_row, thief2_col):
            thief1_row, thief1_col = new_thief1_row, new_thief1_col
            break
            
    # Случайное перемещение второго вора
    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief2_row, new_thief2_col = thief2_row, thief2_col
        if direction == 'L' and thief2_col > 0:
            new_thief2_col -= 1
        elif direction == 'R' and thief2_col < FIELD_SIZE - 1:
            new_thief2_col += 1
        elif direction == 'U' and thief2_row > 0:
            new_thief2_row -= 1
        elif direction == 'D' and thief2_row < FIELD_SIZE - 1:
            new_thief2_row += 1
        if field[new_thief2_row][new_thief2_col] == '.' or (new_thief2_row, new_thief2_col) == (thief1_row, thief1_col):
            thief2_row, thief2_col = new_thief2_row, new_thief2_col
            break

    field[thief1_row][thief1_col] = 'T'
    field[thief2_row][thief2_col] = 'T'
    return (thief1_row, thief1_col), (thief2_row, thief2_col)



def check_catch(dog1: tuple[int, int], dog2: tuple[int, int], thief1: tuple[int, int], thief2: tuple[int, int]) -> bool:
    """
    Проверяет, поймали ли собаки воров.

    :param dog1: Координаты первой собаки (row, col).
    :type dog1: tuple[int, int]
    :param dog2: Координаты второй собаки (row, col).
    :type dog2: tuple[int, int]
    :param thief1: Координаты первого вора (row, col).
    :type thief1: tuple[int, int]
    :param thief2: Координаты второго вора (row, col).
    :type thief2: tuple[int, int]
    :return: True, если воры пойманы, False в противном случае.
    :rtype: bool
    """
    return (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1)


def play_dogs_game():
    """
    Основная функция, запускающая игру "Собаки".
    """
    # Инициализация игры
    field = create_field()
    dog1 = place_object(field, 'D')
    dog2 = place_object(field, 'D')
    thief1 = place_object(field, 'T')
    thief2 = place_object(field, 'T')
    moves = 0
    
    while True:
        moves += 1
        print(f"Ход: {moves}")
        print_field(field)
        
        command = get_user_command()
        dog1, dog2 = move_dogs(field, dog1, dog2, command)
        thief1, thief2 = move_thieves(field, thief1, thief2)
        
        if check_catch(dog1, dog2, thief1, thief2):
            print_field(field)
            print(f"ПОЗДРАВЛЯЮ! Вы поймали воров за {moves} ходов!")
            break


if __name__ == "__main__":
    play_dogs_game()

"""
Объяснение кода:
1. **Импорт модуля random:**
    -   `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных перемещений.
2.  **Импорт модуля logger:**
    -    `from src.logger.logger import logger`: Импортирует logger для логирования ошибок.
3. **Константа `FIELD_SIZE`**:\
    -   `FIELD_SIZE = 10`: Определяет размер игрового поля.
4. **Функция `create_field()`**:\
    -   Создает игровое поле размером `FIELD_SIZE x FIELD_SIZE` и возвращает его в виде списка списков, заполненных точками, представляющими пустые клетки.
5. **Функция `place_object(field, symbol)`**:\
    -   Размещает объект (`symbol`) на случайной свободной позиции в `field`.\
    -   Возвращает координаты размещенного объекта.
6. **Функция `print_field(field)`**:\
    -   Выводит текущее состояние игрового поля `field` на экран.
7. **Функция `get_user_command()`**:\
    -   Запрашивает у пользователя команду для управления собаками (L, R, U, D, F, S).\
    -   Проверяет корректность ввода и возвращает команду в верхнем регистре.
8. **Функция `get_direction(dog_number)`**:\
    -   Запрашивает у пользователя направление для перемещения одной из собак (L, R, U, D).
9.  **Функция `move_dogs(field, dog1, dog2, command)`**:\
    -   Перемещает собак в соответствии с введенной командой:\
        -   `L`, `R`, `U`, `D` - перемещают обеих собак.\
        -   `F` - перемещает первую собаку в соответствии с дополнительным вводом направления (L, R, U, D).\
        -   `S` - перемещает вторую собаку в соответствии с дополнительным вводом направления (L, R, U, D).\
    -   Обновляет позиции собак на поле и возвращает новые координаты.
10. **Функция `move_thieves(field, thief1, thief2)`**:\
    -   Перемещает воров на случайную свободную позицию.\
    -   Обновляет позиции воров на поле и возвращает их новые координаты.
11. **Функция `check_catch(dog1, dog2, thief1, thief2)`**:\
    -   Проверяет, пойманы ли воры. Возвращает `True`, если первая собака находится в той же позиции, что и первый вор, а вторая собака находится в той же позиции, что и второй вор, или наоборот, иначе возвращает `False`.
12. **Функция `play_dogs_game()`**:\
    -   Основная функция игры:\
        -   Создает поле, размещает собак и воров.\
        -   Запускает игровой цикл, который продолжается, пока воры не будут пойманы.\
        -   Выводит текущее состояние поля и запрашивает команду пользователя.\
        -   Перемещает собак и воров.\
        -   Проверяет, пойманы ли воры, и выводит сообщение о победе, если это так.
13. **Условие `if __name__ == "__main__":`**:\
    -   Гарантирует, что игра будет запущена только при запуске файла напрямую, а не при импорте его как модуля.\
    -   Вызывает функцию `play_dogs_game()` для начала игры.
"""
```