# Анализ кода модуля boat.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и логически понятен.
    - Присутствует подробное описание алгоритма игры и ее правил в начале файла.
    - Используются комментарии для пояснения основных блоков кода.
    - Игровой процесс реализован корректно, включая проверку попаданий, промахов и потопления корабля.
    - Присутствует проверка на ввод некорректных данных.
- Минусы
    - Комментарии не соответствуют стандарту reStructuredText (RST).
    - Нет логирования ошибок, что затрудняет отладку.
    - Используется стандартный try-except, хотя можно обрабатывать ошибки через логгер.
    - Не хватает docstring для функций.
    - Используется прямой вывод в консоль через `print`, что затрудняет тестирование и использование кода в других контекстах.

**Рекомендации по улучшению**
1. **Комментарии в формате RST**: Переписать все комментарии в формате RST, включая описание модуля, функций, и переменных.
2. **Логирование ошибок**: Использовать `from src.logger.logger import logger` для логирования ошибок вместо `print`.
3. **Docstring**: Добавить docstring для функции `place_ship`.
4. **Обработка исключений**: Заменить `try-except` на использование логгера для отслеживания ошибок.
5. **Унифицировать код**: Использовать одинарные кавычки в коде.

**Оптимизированный код**
```python
"""
Модуль игры "Морской бой"
=========================

Этот модуль реализует текстовую версию классической игры "Морской бой".
Игрок должен потопить корабль компьютера, угадывая координаты его расположения на игровом поле размером 8x8.

Правила игры:
    1. Игровое поле представляет собой квадратную сетку 8x8.
    2. Компьютер размещает свой корабль на поле случайным образом, занимая 3 последовательные клетки по горизонтали или вертикали.
    3. Игрок вводит координаты выстрела в формате "ряд, столбец" (например, "1,2").
    4. Если выстрел попадает в корабль, компьютер сообщает "Попал".
    5. Если выстрел промахивается, компьютер сообщает "Мимо".
    6. Игра продолжается до тех пор, пока игрок не потопит корабль.

Пример использования
--------------------

.. code-block:: python

    python boat.py
"""
import random
from src.logger.logger import logger # импортируем logger

# Инициализация игрового поля 8x8
board = [[0 for _ in range(8)] for _ in range(8)]

def place_ship():
    """
    Размещает корабль на игровом поле случайным образом.

    Корабль имеет длину 3 клетки и может быть размещен либо горизонтально, либо вертикально.
    """
    # Выбираем случайное направление (0 - горизонтальное, 1 - вертикальное)
    direction = random.randint(0, 1)
    if direction == 0:  # Горизонтальное направление
        row = random.randint(0, 7)
        col = random.randint(0, 4) # Чтобы корабль не выходил за границы
        for i in range(3):
            board[row][col + i] = 1
    else: # Вертикальное направление
        row = random.randint(0, 4) # Чтобы корабль не выходил за границы
        col = random.randint(0, 7)
        for i in range(3):
            board[row + i][col] = 1

# Размещаем корабль на поле
place_ship()

# Основной игровой цикл
while True:
    # Выводим поле в консоль для пользователя
    for row in board:
        print(' '.join(map(str, row)))

    # Запрашиваем ввод координат у пользователя
    try:
        coordinates = input('Введите координаты выстрела (ряд, столбец): ')
        row, col = map(int, coordinates.split(','))
        # Проверяем допустимость координат
        if not (0 <= row <= 7 and 0 <= col <= 7):
            print('Неверные координаты. Введите числа от 0 до 7')
            continue
    except ValueError as e:
        # логируем ошибку
        logger.error('Неверный формат ввода. Введите ряд и столбец через запятую, например: 1,2', exc_info=True)
        continue

    # Проверяем, был ли выстрел попаданием
    if board[row][col] == 1:
        print('Попал!')
        board[row][col] = 2  # Меняем значение, чтобы не учитывать повторные попадания
        # Проверяем, остались ли еще части корабля
        ship_sunk = True
        for row_b in board:
            if 1 in row_b:
                ship_sunk = False
                break
        if ship_sunk:
            print('Корабль потоплен! Вы выиграли!')
            break

    elif board[row][col] == 0:
        print('Мимо!')

    elif board[row][col] == 2:
         print('Вы уже стреляли в эту клетку. Попробуйте другую.')


"""
Объяснение кода:
1.  **Импорт модуля `random`**::
    - `import random`:  Импортирует модуль `random`, который используется для генерации случайных чисел.
    - `from src.logger.logger import logger`: Импортирует логгер для отслеживания ошибок.
2.  **Инициализация игрового поля**::
    - `board = [[0 for _ in range(8)] for _ in range(8)]`: Создает двумерный список (матрицу) размером 8x8, представляющий игровое поле, и заполняет его нулями.
3.  **Функция `place_ship()`**::
    - `direction = random.randint(0, 1)`: Случайно выбирает направление корабля: 0 - горизонтальное, 1 - вертикальное.
    -  **Горизонтальное размещение**::
        - `row = random.randint(0, 7)`: Выбирает случайный ряд для начала корабля.
        -  `col = random.randint(0, 4)`: Выбирает случайный столбец для начала корабля, учитывая длину корабля, чтобы он не выходил за границы.
        -  `for i in range(3): board[row][col + i] = 1`: Размещает корабль, присваивая значение 1 трем клеткам в выбранном ряду.
    -  **Вертикальное размещение**::
        - `row = random.randint(0, 4)`: Выбирает случайный ряд для начала корабля, учитывая длину корабля, чтобы он не выходил за границы.
        -  `col = random.randint(0, 7)`: Выбирает случайный столбец для начала корабля.
        -  `for i in range(3): board[row + i][col] = 1`: Размещает корабль, присваивая значение 1 трем клеткам в выбранном столбце.
4.  **Вызов функции `place_ship()`**::
    - `place_ship()`: Вызывает функцию для размещения корабля на поле.
5.  **Основной игровой цикл `while True:`**::
    - Бесконечный цикл, который продолжается до тех пор, пока корабль не будет потоплен.
    - **Вывод игрового поля**::
        - `for row in board: print(' '.join(map(str, row)))`: Выводит текущее состояние игрового поля в консоль.
    - **Ввод координат**::
      - `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет неверный формат, код записывает ошибку в лог.
      - `coordinates = input('Введите координаты выстрела (ряд, столбец): ')`: Запрашивает ввод координат у игрока в формате "ряд,столбец".
      - `row, col = map(int, coordinates.split(','))`: Разделяет введенную строку на ряд и столбец и преобразует их в целые числа.
      - `if not (0 <= row <= 7 and 0 <= col <= 7):`: Проверяет, находятся ли введенные координаты в допустимых пределах игрового поля.
    - **Проверка попадания**::
        - `if board[row][col] == 1:`: Проверяет, есть ли корабль в клетке, в которую стрелял игрок.
        - `print('Попал!')`: Выводит сообщение о попадании.
        - `board[row][col] = 2`: Отмечает клетку как "попал", чтобы не учитывать повторные попадания.
        - **Проверка, потоплен ли корабль:**:
           - `ship_sunk = True`:  Устанавливает флаг `ship_sunk` в `True`, предполагая, что корабль потоплен.
           - `for row_b in board:`:  Проходит по всем строкам игрового поля.
           - `if 1 in row_b:`: Если в какой-либо строке есть клетка со значением `1`, то корабль еще не потоплен.
           - `ship_sunk = False`: В этом случае флаг `ship_sunk` сбрасывается в `False`.
           - `if ship_sunk: print('Корабль потоплен! Вы выиграли!'); break`: Если флаг остается `True`, то корабль потоплен, и выводится сообщение о победе и игра завершается.
    -  **Проверка промаха**::
        - `elif board[row][col] == 0:`: Проверяет, является ли выстрел промахом.
        - `print('Мимо!')`: Выводит сообщение о промахе.
    -   **Обработка повторного попадания**::
        - `elif board[row][col] == 2:`: Проверяет, стрелял ли игрок ранее в эту клетку.
        - `print('Вы уже стреляли в эту клетку. Попробуйте другую.')`: Выводит сообщение о том, что игрок уже стрелял в эту клетку.
"""