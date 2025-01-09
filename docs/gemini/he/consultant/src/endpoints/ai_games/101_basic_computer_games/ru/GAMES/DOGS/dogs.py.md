# Анализ кода модуля `dogs.py`

**Качество кода**

-   **Соблюдение требований к формату кода (1-10):**
    -   **Преимущества:**
        -   Код написан на языке Python и в целом соответствует основным принципам чистого кода.
        -   Присутствуют docstring для большинства функций.
        -   Используются константы для размера поля.
        -   Логика игры хорошо структурирована и разделена на отдельные функции.
        -   Код содержит блок-схему в формате mermaid.
    -   **Недостатки:**
        -   Не все функции имеют docstring в формате reStructuredText (RST).
        -   В коде отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
        -   Не используются `j_loads` и `j_loads_ns` из `src.utils.jjson`.
        -   Вместо обработки ошибок через `logger.error` используются `print`.
        -   Комментарии не всегда соответствуют стандарту RST.
        -   Много повторяющегося кода в функциях `move_dogs` и `move_thieves`.

**Рекомендации по улучшению**

1.  **Использовать reStructuredText (RST) для всех docstring и комментариев:**
    -   Привести все docstring к формату RST.
    -   Все комментарии должны соответствовать стандарту RST.
2.  **Импортировать и использовать `j_loads` и `j_loads_ns`:**
    -   Импортировать необходимые функции из `src.utils.jjson`.
    -   Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` при работе с файлами JSON (в данном коде файлов JSON нет, но если они появятся в будущем).
3.  **Использовать логгер для обработки ошибок:**
    -   Импортировать `logger` из `src.logger.logger`.
    -   Заменить `print` на `logger.error` для вывода сообщений об ошибках.
4.  **Упростить и рефакторить код:**
    -   Избавиться от повторяющегося кода в функциях `move_dogs` и `move_thieves` с помощью создания отдельных функций для проверки и перемещения.
    -   Улучшить читаемость кода, разбив длинные блоки кода на более мелкие функции.
5.  **Улучшить обработку ввода пользователя:**
    -   Использовать более строгую проверку ввода пользователя, чтобы избежать ошибок.
6.  **Добавить пояснения в комментариях:**
    -   Комментарии должны пояснять логику и назначение частей кода.
7.  **Улучшить формат вывода:**
    -   Использовать f-строки для более удобного форматирования вывода.
8.  **Добавить примеры в документацию (docstring)**

**Улучшенный код**

```python
"""
Модуль для текстовой игры "Собаки"
=========================================================================================

Модуль реализует текстовую игру, в которой игрок управляет двумя собаками и пытается поймать воров.
Игрок вводит команды для перемещения собак, воры перемещаются случайно. Цель игры - поймать воров за минимальное количество ходов.

Примеры использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_dogs_game()
"""

import random
from src.logger.logger import logger # импортируем logger из src.logger.logger

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
        if field[row][col] == '.':  # Проверяем, что место свободно
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

def _move_object(field: list[list[str]], row: int, col: int, direction: str) -> tuple[int, int]:
    """
    Вспомогательная функция для перемещения объекта (собаки или вора) в заданном направлении.
    
    :param field: Игровое поле.
    :type field: list[list[str]]
    :param row: Текущая строка объекта.
    :type row: int
    :param col: Текущий столбец объекта.
    :type col: int
    :param direction: Направление перемещения ('L', 'R', 'U', 'D').
    :type direction: str
    :return: Новые координаты объекта (строка, столбец).
    :rtype: tuple[int, int]
    """
    field[row][col] = '.' # Очищаем старую позицию
    if direction == 'L' and col > 0:
        col -= 1
    elif direction == 'R' and col < FIELD_SIZE - 1:
        col += 1
    elif direction == 'U' and row > 0:
        row -= 1
    elif direction == 'D' and row < FIELD_SIZE - 1:
        row += 1
    return row, col

def move_dogs(field: list[list[str]], dog1: tuple[int, int], dog2: tuple[int, int], command: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Перемещает собак в соответствии с командой пользователя.

    :param field: Игровое поле.
    :type field: list[list[str]]
    :param dog1: Координаты первой собаки (row, col).
    :type dog1: tuple[int, int]
    :param dog2: Координаты второй собаки (row, col).
    :type dog2: tuple[int, int]
    :param command: Команда пользователя ('L', 'R', 'U', 'D', 'F', 'S').
    :type command: str
    :return: Кортеж с новыми координатами собак ((row1, col1), (row2, col2)).
    :rtype: tuple[tuple[int, int], tuple[int, int]]
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2

    if command in ('L', 'R', 'U', 'D'):
      # Перемещение обеих собак
        dog1_row, dog1_col = _move_object(field, dog1_row, dog1_col, command)
        dog2_row, dog2_col = _move_object(field, dog2_row, dog2_col, command)

    elif command == 'F':
      # Перемещение первой собаки
        while True:
            direction = input("Введите направление для первой собаки (L/R/U/D): ").upper()
            if direction in ('L', 'R', 'U', 'D'):
                break
            else:
                print("Неверное направление. Попробуйте снова.")
        dog1_row, dog1_col = _move_object(field, dog1_row, dog1_col, direction)

    elif command == 'S':
      # Перемещение второй собаки
        while True:
            direction = input("Введите направление для второй собаки (L/R/U/D): ").upper()
            if direction in ('L', 'R', 'U', 'D'):
                break
            else:
                print("Неверное направление. Попробуйте снова.")
        dog2_row, dog2_col = _move_object(field, dog2_row, dog2_col, direction)

    field[dog1_row][dog1_col] = 'D' # Обновляем позицию собаки
    field[dog2_row][dog2_col] = 'D' # Обновляем позицию собаки
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

    field[thief1_row][thief1_col] = '.' # Очищаем старую позицию
    field[thief2_row][thief2_col] = '.' # Очищаем старую позицию

    # Случайное перемещение первого вора
    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief1_row, new_thief1_col = thief1_row, thief1_col
        new_thief1_row, new_thief1_col = _move_object(field, new_thief1_row, new_thief1_col, direction)
        if field[new_thief1_row][new_thief1_col] == '.' or (new_thief1_row, new_thief1_col) == (thief2_row, thief2_col):
            thief1_row, thief1_col = new_thief1_row, new_thief1_col
            break

    # Случайное перемещение второго вора
    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief2_row, new_thief2_col = thief2_row, thief2_col
        new_thief2_row, new_thief2_col = _move_object(field, new_thief2_row, new_thief2_col, direction)
        if field[new_thief2_row][new_thief2_col] == '.' or (new_thief2_row, new_thief2_col) == (thief1_row, thief1_col):
            thief2_row, thief2_col = new_thief2_row, new_thief2_col
            break

    field[thief1_row][thief1_col] = 'T'  # Обновляем позицию вора
    field[thief2_row][thief2_col] = 'T' # Обновляем позицию вора
    return (thief1_row, thief1_col), (thief2_row, thief2_col)

def check_catch(dog1: tuple[int, int], dog2: tuple[int, int], thief1: tuple[int, int], thief2: tuple[int, int]) -> bool:
    """
    Проверяет, поймали ли собаки воров. Возвращает True, если пойманы, False - в противном случае.

    :param dog1: Кортеж с координатами первой собаки (row, col).
    :type dog1: tuple[int, int]
    :param dog2: Кортеж с координатами второй собаки (row, col).
    :type dog2: tuple[int, int]
    :param thief1: Кортеж с координатами первого вора (row, col).
    :type thief1: tuple[int, int]
    :param thief2: Кортеж с координатами второго вора (row, col).
    :type thief2: tuple[int, int]
    :return: True, если воры пойманы, False в противном случае.
    :rtype: bool
    """
    if (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1):
        return True
    return False

def play_dogs_game():
    """
    Основная функция, запускающая игру "Собаки".
    """
    # Инициализация игры
    field = create_field()  # Создаем пустое поле
    dog1 = place_object(field, 'D') # Размещаем первую собаку
    dog2 = place_object(field, 'D') # Размещаем вторую собаку
    thief1 = place_object(field, 'T') # Размещаем первого вора
    thief2 = place_object(field, 'T') # Размещаем второго вора
    moves = 0 # Счетчик ходов

    # Основной игровой цикл
    while True:
        moves += 1
        print(f"Ход: {moves}") # Выводим номер хода
        print_field(field) # Выводим текущее состояние поля

        command = get_user_command() # Получаем команду от пользователя
        dog1, dog2 = move_dogs(field, dog1, dog2, command) # Перемещаем собак
        thief1, thief2 = move_thieves(field, thief1, thief2) # Перемещаем воров

        # Проверяем, пойманы ли воры
        if check_catch(dog1, dog2, thief1, thief2):
            print_field(field) # Выводим финальное состояние поля
            print(f"ПОЗДРАВЛЯЮ! Вы поймали воров за {moves} ходов!") # Сообщение о победе
            break # Завершаем игру, если воры пойманы

# Запускаем игру, если скрипт запущен как основной
if __name__ == "__main__":
    play_dogs_game()

"""
Объяснение кода:
1. **Импорт модуля random и logger:**
    -  `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных перемещений.
    -  `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок.
2.  **Константа `FIELD_SIZE`**:
    -   `FIELD_SIZE = 10`: Определяет размер игрового поля.
3.  **Функция `create_field()`**:
    -   Создает игровое поле размером `FIELD_SIZE x FIELD_SIZE` и возвращает его в виде списка списков, заполненных точками, представляющими пустые клетки.
4.  **Функция `place_object(field, symbol)`**:
    -   Размещает объект (`symbol`) на случайной свободной позиции в `field`.
    -   Возвращает координаты размещенного объекта.
5.  **Функция `print_field(field)`**:
    -   Выводит текущее состояние игрового поля `field` на экран.
6.  **Функция `get_user_command()`**:
    -   Запрашивает у пользователя команду для управления собаками (L, R, U, D, F, S).
    -   Проверяет корректность ввода и возвращает команду в верхнем регистре.
7.  **Функция `_move_object(field, row, col, direction)`**:
    -   Вспомогательная функция для перемещения объекта (собаки или вора) в заданном направлении.
8.  **Функция `move_dogs(field, dog1, dog2, command)`**:
    -   Перемещает собак в соответствии с введенной командой:
        -   `L`, `R`, `U`, `D` - перемещают обеих собак.
        -   `F` - перемещает первую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
        -   `S` - перемещает вторую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
    -   Обновляет позиции собак на поле и возвращает новые координаты.
9.  **Функция `move_thieves(field, thief1, thief2)`**:
    -   Перемещает воров на случайную свободную позицию.
    -   Обновляет позиции воров на поле и возвращает их новые координаты.
10. **Функция `check_catch(dog1, dog2, thief1, thief2)`**:
    -   Проверяет, пойманы ли воры. Возвращает `True`, если первая собака находится в той же позиции, что и первый вор, а вторая собака находится в той же позиции, что и второй вор, или наоборот, иначе возвращает `False`.
11. **Функция `play_dogs_game()`**:
    -   Основная функция игры:
        -   Создает поле, размещает собак и воров.
        -   Запускает игровой цикл, который продолжается, пока воры не будут пойманы.
        -   Выводит текущее состояние поля и запрашивает команду пользователя.
        -   Перемещает собак и воров.
        -   Проверяет, пойманы ли воры, и выводит сообщение о победе, если это так.
12. **Условие `if __name__ == "__main__":`**:
    -   Гарантирует, что игра будет запущена только при запуске файла напрямую, а не при импорте его как модуля.
    -   Вызывает функцию `play_dogs_game()` для начала игры.
"""