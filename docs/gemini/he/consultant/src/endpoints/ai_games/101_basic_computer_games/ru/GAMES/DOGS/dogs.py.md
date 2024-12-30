# Анализ кода модуля `dogs.py`

**Качество кода**
-  Соответствие требованиям: 9 из 10
    - **Преимущества:**
        - Код хорошо структурирован, каждая функция выполняет определенную задачу.
        - Используются константы для размера поля, что облегчает модификацию.
        - Присутствуют docstring для функций, хотя их нужно переработать в соответствии с требованиями RST.
        - Логика игры реализована понятно и без лишних усложнений.
        - Есть комментарии, объясняющие логику работы кода, однако их необходимо переработать в RST.
    - **Недостатки:**
        - Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
        - docstring не соответствуют формату reStructuredText (RST).
        - Отсутствует обработка ошибок с использованием `logger.error`.
        - Некоторые блоки кода могут быть улучшены.

**Рекомендации по улучшению**

1.  **Импорт:** Добавить импорты для `j_loads`, `j_loads_ns` из `src.utils.jjson` и `logger` из `src.logger.logger`.
2.  **Формат docstring:** Переписать все docstring в формате reStructuredText (RST).
3.  **Обработка ошибок:** Заменить блоки `try-except` на использование `logger.error` для отслеживания ошибок.
4.  **Комментарии:** Переформатировать все комментарии в RST.
5. **Переменные:** Добавить `_` в конце имен переменных которые не меняются, на пример: `FIELD_SIZE_ = 10`.
6. **Вложенный цикл:** При `move_dogs`  и `move_thieves`  можно упростить код убрав вложенные циклы `while`.

**Улучшенный код**

```python
"""
Модуль "Собаки"
=========================

Текстовая игра, в которой игрок управляет двумя собаками,
пытаясь поймать воров.

Игрок вводит команды для перемещения собак,
а воры перемещаются случайно.

Цель игры - поймать воров за минимальное количество ходов.

Пример использования:

.. code-block:: python

    python dogs.py
"""

import random
from src.logger.logger import logger # Импортируем logger
# from src.utils.jjson import j_loads, j_loads_ns # TODO: Добавить импорт когда j_loads, j_loads_ns будут использоваться

# Константы для размеров поля
FIELD_SIZE_ = 10

def create_field() -> list[list[str]]:
    """
    Создает игровое поле размером FIELD_SIZE_ x FIELD_SIZE_,
    представляя его как список списков.

    :return: Двумерный список, представляющий игровое поле.
    :rtype: list[list[str]]
    """
    return [['.' for _ in range(FIELD_SIZE_)] for _ in range(FIELD_SIZE_)]

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
        row = random.randint(0, FIELD_SIZE_ - 1)
        col = random.randint(0, FIELD_SIZE_ - 1)
        if field[row][col] == '.': # Проверяем, что место свободно
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

def move_dogs(field: list[list[str]], dog1: tuple[int, int], dog2: tuple[int, int], command: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Перемещает собак в соответствии с командой пользователя.
    
    :param field: игровое поле
    :type field: list[list[str]]
    :param dog1: координаты первой собаки
    :type dog1: tuple[int, int]
    :param dog2: координаты второй собаки
    :type dog2: tuple[int, int]
    :param command: команда пользователя
    :type command: str
    :return: Новые координаты первой и второй собак
    :rtype: tuple[tuple[int, int], tuple[int, int]]
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2
    
    field[dog1_row][dog1_col] = '.' # Очищаем старую позицию
    field[dog2_row][dog2_col] = '.' # Очищаем старую позицию

    if command == 'L':
        if dog1_col > 0:
           dog1_col -= 1
        if dog2_col > 0:
           dog2_col -= 1
    elif command == 'R':
        if dog1_col < FIELD_SIZE_ - 1:
          dog1_col += 1
        if dog2_col < FIELD_SIZE_ - 1:
          dog2_col += 1
    elif command == 'U':
        if dog1_row > 0:
           dog1_row -= 1
        if dog2_row > 0:
           dog2_row -= 1
    elif command == 'D':
        if dog1_row < FIELD_SIZE_ - 1:
          dog1_row += 1
        if dog2_row < FIELD_SIZE_ - 1:
           dog2_row += 1
    elif command == 'F':
      while True:
        direction = input("Введите направление для первой собаки (L/R/U/D): ").upper()
        if direction in ('L', 'R', 'U', 'D'):
          break
        else:
          print("Неверное направление. Попробуйте снова.")

      if direction == 'L' and dog1_col > 0:
          dog1_col -= 1
      elif direction == 'R' and dog1_col < FIELD_SIZE_ - 1:
          dog1_col += 1
      elif direction == 'U' and dog1_row > 0:
          dog1_row -= 1
      elif direction == 'D' and dog1_row < FIELD_SIZE_ - 1:
          dog1_row += 1
    elif command == 'S':
      while True:
        direction = input("Введите направление для второй собаки (L/R/U/D): ").upper()
        if direction in ('L', 'R', 'U', 'D'):
            break
        else:
            print("Неверное направление. Попробуйте снова.")

      if direction == 'L' and dog2_col > 0:
        dog2_col -= 1
      elif direction == 'R' and dog2_col < FIELD_SIZE_ - 1:
        dog2_col += 1
      elif direction == 'U' and dog2_row > 0:
        dog2_row -= 1
      elif direction == 'D' and dog2_row < FIELD_SIZE_ - 1:
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
    
    field[thief1_row][thief1_col] = '.' # Очищаем старую позицию
    field[thief2_row][thief2_col] = '.' # Очищаем старую позицию

    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief1_row, new_thief1_col = thief1_row, thief1_col

        if direction == 'L' and thief1_col > 0:
            new_thief1_col -= 1
        elif direction == 'R' and thief1_col < FIELD_SIZE_ - 1:
            new_thief1_col += 1
        elif direction == 'U' and thief1_row > 0:
            new_thief1_row -= 1
        elif direction == 'D' and thief1_row < FIELD_SIZE_ - 1:
            new_thief1_row += 1
        if field[new_thief1_row][new_thief1_col] == '.' or (new_thief1_row, new_thief1_col) == (thief2_row, thief2_col):
            thief1_row, thief1_col = new_thief1_row, new_thief1_col
            break
    while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief2_row, new_thief2_col = thief2_row, thief2_col

        if direction == 'L' and thief2_col > 0:
            new_thief2_col -= 1
        elif direction == 'R' and thief2_col < FIELD_SIZE_ - 1:
            new_thief2_col += 1
        elif direction == 'U' and thief2_row > 0:
            new_thief2_row -= 1
        elif direction == 'D' and thief2_row < FIELD_SIZE_ - 1:
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
    return (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1)

def play_dogs_game():
    """
    Основная функция, запускающая игру "Собаки".
    """
    # Инициализация игры
    field = create_field() # Создаем пустое поле
    dog1 = place_object(field, 'D') # Размещаем первую собаку
    dog2 = place_object(field, 'D') # Размещаем вторую собаку
    thief1 = place_object(field, 'T') # Размещаем первого вора
    thief2 = place_object(field, 'T') # Размещаем второго вора
    moves = 0 # Счетчик ходов

    # Основной игровой цикл
    while True:
        moves += 1
        print(f"Ход: {moves}")
        print_field(field) # Выводим текущее состояние поля
        
        command = get_user_command()
        dog1, dog2 = move_dogs(field, dog1, dog2, command)
        thief1, thief2 = move_thieves(field, thief1, thief2)

        # Проверяем, пойманы ли воры
        if check_catch(dog1, dog2, thief1, thief2):
            print_field(field)
            print(f"ПОЗДРАВЛЯЮ! Вы поймали воров за {moves} ходов!")
            break # Завершаем игру, если воры пойманы

if __name__ == "__main__":
    play_dogs_game()

"""
Объяснение кода:
1. **Импорт модуля random и logger:**
   -   `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных перемещений.
   -   `from src.logger.logger import logger`: Импортирует logger для логирования ошибок.
2.  **Константа `FIELD_SIZE_`**:
    -   `FIELD_SIZE_ = 10`: Определяет размер игрового поля.
3. **Функция `create_field()`**:
    -   Создает игровое поле размером `FIELD_SIZE_ x FIELD_SIZE_` и возвращает его в виде списка списков, заполненных точками, представляющими пустые клетки.
4. **Функция `place_object(field, symbol)`**:
    -   Размещает объект (`symbol`) на случайной свободной позиции в `field`.
    -   Возвращает координаты размещенного объекта.
5. **Функция `print_field(field)`**:
    -   Выводит текущее состояние игрового поля `field` на экран.
6. **Функция `get_user_command()`**:
    -   Запрашивает у пользователя команду для управления собаками (L, R, U, D, F, S).
    -   Проверяет корректность ввода и возвращает команду в верхнем регистре.
7. **Функция `move_dogs(field, dog1, dog2, command)`**:
    -   Перемещает собак в соответствии с введенной командой:
        -   `L`, `R`, `U`, `D` - перемещают обеих собак.
        -   `F` - перемещает первую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
        -   `S` - перемещает вторую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
    -   Обновляет позиции собак на поле и возвращает новые координаты.
8. **Функция `move_thieves(field, thief1, thief2)`**:
    -   Перемещает воров на случайную свободную позицию.
    -   Обновляет позиции воров на поле и возвращает их новые координаты.
9. **Функция `check_catch(dog1, dog2, thief1, thief2)`**:
    -   Проверяет, пойманы ли воры. Возвращает `True`, если первая собака находится в той же позиции, что и первый вор, а вторая собака находится в той же позиции, что и второй вор, или наоборот, иначе возвращает `False`.
10. **Функция `play_dogs_game()`**:
    -   Основная функция игры:
        -   Создает поле, размещает собак и воров.
        -   Запускает игровой цикл, который продолжается, пока воры не будут пойманы.
        -   Выводит текущее состояние поля и запрашивает команду пользователя.
        -   Перемещает собак и воров.
        -   Проверяет, пойманы ли воры, и выводит сообщение о победе, если это так.
11. **Условие `if __name__ == "__main__":`**:
    -   Гарантирует, что игра будет запущена только при запуске файла напрямую, а не при импорте его как модуля.
    -   Вызывает функцию `play_dogs_game()` для начала игры.
"""
```