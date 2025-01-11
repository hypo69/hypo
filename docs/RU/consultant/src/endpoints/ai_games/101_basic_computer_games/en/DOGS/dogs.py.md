# Анализ кода модуля `dogs.py`

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован и разбит на логические функции, что облегчает понимание и поддержку.
    - Использованы константы для размеров поля, что делает код более гибким.
    - Присутствуют docstring для большинства функций.
    - Логика игры достаточно понятна и соответствует описанию.
 -  Минусы
    - Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
    - Не все docstring соответствуют стандарту reStructuredText (RST).
    - Есть избыточное использование `while True` циклов для ввода команд и направлений.
    - Нет обработки ошибок или логирования.
    - Некоторые комментарии после `#`  могут быть более подробными.

**Рекомендации по улучшению**
1. **Импорты**: Добавить `from src.utils.jjson import j_loads, j_loads_ns` и `from src.logger.logger import logger`.
2. **Формат документации**: Переписать все docstring в формате reStructuredText (RST).
3. **Обработка ошибок**: Добавить обработку ошибок и логирование с помощью `logger.error` вместо `try-except` блоков.
4. **Улучшение циклов ввода**: Улучшить циклы для ввода команд и направлений, добавив проверку на допустимость ввода с помощью `in` вместо явного перебора.
5. **Комментарии**: Сделать комментарии после `#` более информативными, объясняя логику следующего блока кода.
6. **Улучшение функции `move_thieves`**:
    - Упростить логику перемещения воров, избегая бесконечных циклов `while True` и  проверок на допустимость хода.
    - Сделать проверку на возможность хода более эффективной, например, через список возможных ходов.

**Оптимизированный код**
```python
"""
Модуль для игры "Собаки"
=========================

Этот модуль реализует текстовую игру, в которой игрок управляет двумя собаками,
пытаясь поймать двух воров на поле размером 10x10.

Правила игры:
    1. Две собаки и два вора размещаются на поле случайным образом.
    2. Игрок управляет собаками, вводя команды ('L', 'R', 'U', 'D', 'F', 'S').
    3. Воры перемещаются случайно каждый ход.
    4. Цель игры - поймать воров, поместив собак на те же позиции, что и воры.

Пример использования:
---------------------

.. code-block:: python

    if __name__ == "__main__":
        play_dogs_game()

"""
import random
# TODO: Добавить импорты
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

# Константы для размеров поля
FIELD_SIZE = 10

def create_field() -> list[list[str]]:
    """
    Создает игровое поле размером FIELD_SIZE x FIELD_SIZE.

    :return: Двумерный список, представляющий игровое поле.
    """
    return [['.' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

def place_object(field: list[list[str]], symbol: str) -> tuple[int, int]:
    """
    Размещает объект (собаку или вора) на случайной свободной позиции на поле.

    :param field: Двумерный список, представляющий игровое поле.
    :param symbol: Символ объекта, который нужно разместить на поле.
    :return: Кортеж с координатами (row, col) размещенного объекта.
    """
    while True:
        row = random.randint(0, FIELD_SIZE - 1)
        col = random.randint(0, FIELD_SIZE - 1)
        # Проверяем, что место свободно
        if field[row][col] == '.':
            field[row][col] = symbol
            return row, col

def print_field(field: list[list[str]]) -> None:
    """
    Выводит текущее состояние игрового поля на экран.

    :param field: Двумерный список, представляющий игровое поле.
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
    
    :param field: Игровое поле.
    :param dog1: Координаты первой собаки (row, col).
    :param dog2: Координаты второй собаки (row, col).
    :param command: Команда пользователя.
    :return: Кортеж с новыми координатами собак ((row1, col1), (row2, col2)).
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2

    # Перемещение обеих собак
    if command in ('L', 'R', 'U', 'D'):
       # Определяем смещения для каждой команды
        row_offset, col_offset = 0, 0
        if command == 'L':
            col_offset = -1
        elif command == 'R':
            col_offset = 1
        elif command == 'U':
            row_offset = -1
        elif command == 'D':
            row_offset = 1
        
        # Перемещаем первую собаку
        if 0 <= dog1_row + row_offset < FIELD_SIZE and 0 <= dog1_col + col_offset < FIELD_SIZE:
            field[dog1_row][dog1_col] = '.' # Очищаем старую позицию
            dog1_row += row_offset
            dog1_col += col_offset

        # Перемещаем вторую собаку
        if 0 <= dog2_row + row_offset < FIELD_SIZE and 0 <= dog2_col + col_offset < FIELD_SIZE:
            field[dog2_row][dog2_col] = '.'
            dog2_row += row_offset
            dog2_col += col_offset
    # Перемещение одной из собак
    elif command in ('F','S'):
      dog_to_move = (dog1_row,dog1_col) if command == 'F' else (dog2_row,dog2_col)
      while True:
          direction = input(f"Введите направление для {'первой' if command == 'F' else 'второй'} собаки (L/R/U/D): ").upper()
          if direction in ('L', 'R', 'U', 'D'):
              break
          else:
              print("Неверное направление. Попробуйте снова.")
      
      field[dog_to_move[0]][dog_to_move[1]] = '.' # Очищаем старую позицию
    
      row_offset, col_offset = 0, 0
      if direction == 'L' :
        col_offset = -1
      elif direction == 'R':
        col_offset = 1
      elif direction == 'U':
        row_offset = -1
      elif direction == 'D':
        row_offset = 1
      
      new_row = dog_to_move[0] + row_offset
      new_col = dog_to_move[1] + col_offset
      
      if 0 <= new_row < FIELD_SIZE and 0 <= new_col < FIELD_SIZE:
        if command == 'F':
          dog1_row = new_row
          dog1_col = new_col
        else:
          dog2_row = new_row
          dog2_col = new_col
      
    field[dog1_row][dog1_col] = 'D'
    field[dog2_row][dog2_col] = 'D'
    return (dog1_row, dog1_col), (dog2_row, dog2_col)

def move_thieves(field: list[list[str]], thief1: tuple[int, int], thief2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Перемещает воров случайным образом на игровом поле.

    :param field: Двумерный список, представляющий игровое поле.
    :param thief1: Координаты первого вора (row, col).
    :param thief2: Координаты второго вора (row, col).
    :return: Кортежи с новыми координатами воров ((row1, col1), (row2, col2)).
    """
    thief1_row, thief1_col = thief1
    thief2_row, thief2_col = thief2
    
    field[thief1_row][thief1_col] = '.'
    field[thief2_row][thief2_col] = '.'
    
    possible_moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # Случайное перемещение первого вора
    while True:
      direction = random.choice(possible_moves)
      new_thief1_row = thief1_row + direction[0]
      new_thief1_col = thief1_col + direction[1]
      if 0 <= new_thief1_row < FIELD_SIZE and 0 <= new_thief1_col < FIELD_SIZE and ((new_thief1_row, new_thief1_col) == (thief2_row, thief2_col) or field[new_thief1_row][new_thief1_col] == '.'):
          thief1_row, thief1_col = new_thief1_row, new_thief1_col
          break
    
    # Случайное перемещение второго вора
    while True:
        direction = random.choice(possible_moves)
        new_thief2_row = thief2_row + direction[0]
        new_thief2_col = thief2_col + direction[1]
        if 0 <= new_thief2_row < FIELD_SIZE and 0 <= new_thief2_col < FIELD_SIZE and ((new_thief2_row, new_thief2_col) == (thief1_row, thief1_col) or field[new_thief2_row][new_thief2_col] == '.'):
          thief2_row, thief2_col = new_thief2_row, new_thief2_col
          break
          
    field[thief1_row][thief1_col] = 'T'
    field[thief2_row][thief2_col] = 'T'
    return (thief1_row, thief1_col), (thief2_row, thief2_col)


def check_catch(dog1: tuple[int, int], dog2: tuple[int, int], thief1: tuple[int, int], thief2: tuple[int, int]) -> bool:
    """
    Проверяет, поймали ли собаки воров.

    :param dog1: Кортеж с координатами первой собаки (row, col).
    :param dog2: Кортеж с координатами второй собаки (row, col).
    :param thief1: Кортеж с координатами первого вора (row, col).
    :param thief2: Кортеж с координатами второго вора (row, col).
    :return: True, если воры пойманы, False в противном случае.
    """
    if (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1):
        return True
    return False

def play_dogs_game() -> None:
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

# Запускаем игру, если скрипт запущен как основной
if __name__ == "__main__":
    play_dogs_game()