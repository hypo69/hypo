# Анализ кода модуля AMAZIN

**Качество кода**
8
- Плюсы
    - Описание игры и её логики представлено в структурированном виде.
    - Присутствует пошаговая инструкция для реализации игры.
    - Есть пример работы программы.
    - Указаны возможные ограничения.
- Минусы
    -  Отсутствует фактический код.
    -  Документация не соответствует формату reStructuredText.
    -  Нет информации о зависимостях, импортах и используемых модулях.
    -  Нет обработки ошибок.

**Рекомендации по улучшению**
1.  **Преобразовать в reStructuredText (RST)**: Переписать весь документ в формате RST, чтобы обеспечить его совместимость с инструментами генерации документации, такими как Sphinx.
2.  **Добавить код**: Предоставить фактическую реализацию игры на Python, следуя описанной логике.
3.  **Обеспечить обработку ошибок**: Реализовать обработку исключений для ввода пользователя и возможных проблем с генерацией лабиринта.
4.  **Использовать логгер**: Включить логирование ошибок с помощью `from src.logger.logger import logger`.
5.  **Импорты**: Добавить необходимые импорты в начале файла.
6. **Документация кода**: Добавить docstrings в формате reStructuredText для всех функций и классов.
7. **Стиль кода**: Использовать одинарные кавычки для строк и придерживаться стандарта PEP 8.

**Оптимизированный код**
```markdown
 """
 Модуль для генерации лабиринтов в текстовом виде.
 =====================================================

 Этот модуль содержит функции для генерации лабиринта заданного размера с использованием
 алгоритма рекурсивного поиска в глубину (DFS).

 Пример использования
 --------------------

 .. code-block:: python

    from src.logger.logger import logger
    from random import shuffle

    def generate_maze(width: int, height: int) -> list[list[str]]:
      ...

    if __name__ == "__main__":
        maze = generate_maze(10, 8)
        for row in maze:
            print(''.join(row))
 """

from src.logger.logger import logger
from random import shuffle

def generate_maze(width: int, height: int) -> list[list[str]]:
    """
    Генерирует лабиринт заданного размера.

    :param width: Ширина лабиринта.
    :type width: int
    :param height: Высота лабиринта.
    :type height: int
    :return: Список строк, представляющих лабиринт.
    :rtype: list[list[str]]
    """
    if width <= 0 or height <= 0:
        logger.error(f"Некорректные размеры лабиринта: width={width}, height={height}")
        return None

    maze = [['+' for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]
    def carve_path(x: int, y: int):
        """
        Рекурсивно прокладывает путь в лабиринте.

        :param x: Координата X текущей ячейки.
        :type x: int
        :param y: Координата Y текущей ячейки.
        :type y: int
        """
        maze[y][x] = ' '
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < 2 * width and 0 < ny < 2 * height and maze[ny][nx] == '+':
                maze[y + dy // 2][x + dx // 2] = ' '
                carve_path(nx, ny)

    carve_path(1, 1)
    return maze

if __name__ == "__main__":
    """
    Пример работы программы.
    """
    while True:
        try:
            width = int(input("Введите ширину лабиринта: "))
            height = int(input("Введите высоту лабиринта: "))
            if width <= 0 or height <= 0:
                 logger.warning(f"Некорректный размер лабиринта {width=} {height=}. Будет использован размер по умолчанию 10x10.")
                 width, height = 10, 10
            maze = generate_maze(width, height)
            if maze:
                for row in maze:
                    print(''.join(row))
            else:
                logger.error(f'Не удалось сгенерировать лабиринт с параметрами {width=}, {height=}')

        except ValueError:
            logger.error("Ошибка: Введены некорректные значения. Используются значения по умолчанию 10x10.")
            width, height = 10, 10
            maze = generate_maze(width, height)
            if maze:
                for row in maze:
                   print(''.join(row))
            else:
                logger.error(f'Не удалось сгенерировать лабиринт с параметрами {width=}, {height=}')

        new_maze = input("Сгенерировать новый лабиринт? (да/нет): ").lower()
        if new_maze != 'да':
            print('До свидания!')
            break
```