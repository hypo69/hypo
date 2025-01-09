# Анализ кода модуля LIFE

**Качество кода**
- Соответствие требованиям к формату кода (1-10): 8
    - Преимущества
        - Код хорошо структурирован и понятен.
        - Описание игры и алгоритма представлены в формате markdown.
        - Блок-схема в формате mermaid делает понимание логики кода наглядным.
        - Описание каждого этапа блок-схемы подробно объясняет процесс.
    - Недостатки
        - Отсутствует Python-код.
        - Нет reStructuredText (RST) комментариев и docstring.
        - Нет использования `j_loads` или `j_loads_ns` для чтения файлов (так как кода нет).
        - Отсутствует импорт необходимых библиотек (так как кода нет).
        - Не используются логирование ошибок через `logger`.
        - Не представлены примеры кода и их улучшения.

**Рекомендации по улучшению**
1. Необходимо добавить Python-код, реализующий описанный алгоритм.
2. Все комментарии и docstring должны быть переписаны в формате reStructuredText (RST).
3. При чтении файлов использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4. Добавить импорт необходимых библиотек.
5. Использовать логирование ошибок через `logger.error` вместо стандартных `try-except`.
6. Добавить примеры кода с использованием RST и TODO.
7. Необходимо добавить пояснения к коду в виде комментариев.

**Улучшенный код**

```markdown
"""
Модуль, реализующий игру "Жизнь" Конвея.
=========================================================================================

Этот модуль содержит функции для создания, отображения и симуляции клеточного автомата "Жизнь".
Игровое поле представляет собой сетку клеток, каждая из которых может быть "живой" или "мертвой".
Состояние каждой клетки в следующем поколении определяется состоянием ее соседей в текущем поколении.

Пример использования:
--------------------

.. code-block:: python

    from src.utils.jjson import j_loads_ns
    from src.logger.logger import logger
    import random

    def main():
       rows = 20
       cols = 20
       generations = 10
       initial_config = None
       game_of_life(rows, cols, generations, initial_config)

    if __name__ == "__main__":
        main()

"""
from src.utils.jjson import j_loads_ns  # Импорт j_loads_ns для чтения файлов
from src.logger.logger import logger  # Импорт logger для логирования ошибок
import random # Импорт модуля random для генерации случайной начальной конфигурации

def create_initial_grid(rows: int, cols: int, initial_config: list = None) -> list:
    """
    Создает начальную сетку игрового поля.

    :param rows: Количество строк в сетке.
    :param cols: Количество столбцов в сетке.
    :param initial_config: Начальная конфигурация сетки (список строк, где '*' - живая клетка, ' ' - мертвая клетка). Если None, генерируется случайная конфигурация.
    :return: Начальная сетка игрового поля.
    """
    if initial_config: # Проверка наличия начальной конфигурации
       try: # Блок try-except для отлова ошибок
            # Проверка, что начальная конфигурация соответствует заданным размерам
            if len(initial_config) != rows or any(len(row) != cols for row in initial_config):
                logger.error(f'Неверная начальная конфигурация. Требуется сетка {rows}x{cols}, а получена сетка {len(initial_config)}x{[len(row) for row in initial_config]}') # Логирование ошибки, если размеры сетки не совпадают
                return [[random.choice(['*', ' ']) for _ in range(cols)] for _ in range(rows)] # Возврат случайной сетки в случае ошибки
            return initial_config
       except Exception as e:  # Обработка исключений при чтении конфига
           logger.error('Произошла ошибка при использовании начальной конфигурации.', exc_info=True) # Логирование ошибки при обработке исключения
           return [[random.choice(['*', ' ']) for _ in range(cols)] for _ in range(rows)] # Возврат случайной сетки в случае ошибки
    else: # Если начальная конфигурация не задана
        # Генерация случайной конфигурации
        return [[random.choice(['*', ' ']) for _ in range(cols)] for _ in range(rows)] # Возврат случайной сетки

def print_grid(grid: list) -> None:
    """
    Выводит на экран текущее состояние сетки.

    :param grid: Сетка игрового поля.
    """
    for row in grid:  # Проход по строкам сетки
        print(''.join(row))  # Вывод строки
    print("-" * len(grid[0])) # Вывод разделительной линии

def count_live_neighbours(grid: list, row: int, col: int) -> int:
    """
    Подсчитывает количество живых соседей для заданной клетки.

    :param grid: Сетка игрового поля.
    :param row: Индекс строки клетки.
    :param col: Индекс столбца клетки.
    :return: Количество живых соседей клетки.
    """
    rows = len(grid) # Получение количества строк сетки
    cols = len(grid[0]) # Получение количества столбцов сетки
    live_neighbours = 0 # Инициализация количества живых соседей
    for i in range(max(0, row - 1), min(rows, row + 2)):  # Проход по соседним строкам
        for j in range(max(0, col - 1), min(cols, col + 2)): # Проход по соседним столбцам
            if (i, j) != (row, col) and grid[i][j] == '*':  # Проверка, что это не сама клетка и она жива
                live_neighbours += 1  # Увеличение счетчика живых соседей
    return live_neighbours # Возврат количества живых соседей

def apply_rules(grid: list, row: int, col: int) -> str:
    """
    Применяет правила игры для определения состояния клетки в следующем поколении.

    :param grid: Текущая сетка игрового поля.
    :param row: Индекс строки клетки.
    :param col: Индекс столбца клетки.
    :return: Состояние клетки в следующем поколении ('*' - живая, ' ' - мертвая).
    """
    live_neighbours = count_live_neighbours(grid, row, col) # Подсчет живых соседей
    if grid[row][col] == '*': # Если клетка жива
        if live_neighbours < 2 or live_neighbours > 3: # Если соседей меньше 2 или больше 3
           return ' '  # Клетка умирает от одиночества или перенаселения
        else: # Если 2 или 3 соседа
            return '*' # Клетка выживает
    else:  # Если клетка мертва
        if live_neighbours == 3:  # Если ровно 3 соседа
            return '*'  # Клетка оживает
        else:  # Если другое количество соседей
            return ' '  # Клетка остается мертвой

def create_next_generation_grid(grid: list) -> list:
    """
    Создает новую сетку (следующее поколение) на основе правил игры.

    :param grid: Текущая сетка игрового поля.
    :return: Новая сетка (следующее поколение).
    """
    rows = len(grid) # Получение количества строк сетки
    cols = len(grid[0]) # Получение количества столбцов сетки
    next_grid = [[' ' for _ in range(cols)] for _ in range(rows)] # Инициализация новой сетки мертвыми клетками
    for row in range(rows): # Проход по всем строкам
        for col in range(cols):  # Проход по всем столбцам
            next_grid[row][col] = apply_rules(grid, row, col) # Определение состояния клетки в следующем поколении
    return next_grid # Возврат новой сетки

def game_of_life(rows: int, cols: int, generations: int, initial_config: list = None) -> None:
    """
    Запускает симуляцию игры "Жизнь".

    :param rows: Количество строк в сетке.
    :param cols: Количество столбцов в сетке.
    :param generations: Количество поколений для симуляции.
    :param initial_config: Начальная конфигурация сетки (список строк, где '*' - живая клетка, ' ' - мертвая клетка). Если None, генерируется случайная конфигурация.
    """
    grid = create_initial_grid(rows, cols, initial_config) # Создание начальной сетки
    for generation in range(generations): # Проход по всем поколениям
        print(f"Поколение {generation + 1}:")  # Вывод номера текущего поколения
        print_grid(grid) # Вывод текущей сетки
        grid = create_next_generation_grid(grid) # Создание новой сетки для следующего поколения
    print("Финальное состояние:")  # Вывод заключительного состояния
    print_grid(grid) # Вывод финальной сетки

def main():
    """
    Главная функция для запуска игры.
    """
    rows = 20 # Количество строк
    cols = 20 # Количество столбцов
    generations = 10 # Количество поколений
    initial_config = None # Начальная конфигурация
    game_of_life(rows, cols, generations, initial_config) # Запуск игры

if __name__ == "__main__":
    main() # Запуск main функции, если скрипт запущен напрямую
```