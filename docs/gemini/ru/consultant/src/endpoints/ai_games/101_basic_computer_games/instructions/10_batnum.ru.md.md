# Анализ кода модуля `10_batnum.ru.md`

**Качество кода**

- **Соответствие требованиям по оформлению кода:** 8/10
    -   **Плюсы**
        -   Документ содержит подробное описание игры, пошаговую инструкцию, пример работы и возможные ограничения.
        -   Структура документа логична и понятна.
        -   Присутствует описание стратегии победы.
    -   **Минусы**
        -   Отсутствуют docstring в стиле reStructuredText (RST).
        -   Не используется логирование ошибок.
        -   Код представлен в виде инструкций, а не в виде исполняемого кода.
        -   Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код:**
    -   Необходимо преобразовать пошаговые инструкции в исполняемый код на Python.
2.  **Использование reStructuredText (RST):**
    -   Добавить docstring для модуля, функций и переменных в формате RST.
3.  **Логирование ошибок:**
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  **Обработка ошибок:**
    -   Избегать избыточного использования `try-except`, предпочитать логирование с помощью `logger.error`.
5.  **Использование `j_loads`:**
    -   Если предполагается чтение данных из файла, использовать `j_loads` или `j_loads_ns`.
6.  **Комментарии в коде:**
    -   Добавить комментарии к коду, объясняющие каждый блок.

**Оптимизированный код**

```python
"""
Модуль для реализации игры "Битва чисел" (Butnum)
==================================================

Этот модуль содержит функции для инициализации, управления ходами и определения победителя в игре "Битва чисел".
В игре участвуют игрок и компьютер, поочередно убирающие объекты из кучки.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.instructions.batnum import play_game

    play_game()
"""
import random
from src.logger.logger import logger # импортируем logger для логирования ошибок

def get_player_choice(min_take: int, max_take: int, remaining_objects: int) -> int:
    """
    Получает ввод от игрока о количестве объектов для забора.

    :param min_take: Минимальное количество объектов для забора.
    :param max_take: Максимальное количество объектов для забора.
    :param remaining_objects: Количество оставшихся объектов.
    :return: Количество объектов, которое игрок хочет забрать.
    :raises ValueError: Если ввод игрока не является целым числом или выходит за допустимые границы.
    """
    while True:
        try:
            choice = int(input(f'Ваш ход: Сколько объектов вы хотите забрать? ({min_take}, ..., {max_take})\n> '))
            if min_take <= choice <= max_take and choice <= remaining_objects:
                 # Проверка корректности ввода
                return choice
            else:
                logger.error(f'Неверный ввод: выберите от {min_take} до {max_take} или меньше {remaining_objects}')
        except ValueError as e:
            logger.error(f'Неверный ввод, введите целое число {e}') # логируем ошибку ввода
            continue


def get_computer_choice(min_take: int, max_take: int, remaining_objects: int) -> int:
    """
    Вычисляет оптимальный ход для компьютера.

    :param min_take: Минимальное количество объектов для забора.
    :param max_take: Максимальное количество объектов для забора.
    :param remaining_objects: Количество оставшихся объектов.
    :return: Количество объектов, которое компьютер забирает.
    """
    if remaining_objects == 1:
        return 1  # Если остался один объект, компьютер забирает его
    if (remaining_objects - 1) % (max_take + 1) == 0:
         # Если количество объектов - 1 кратно max_take + 1, компьютер забирает случайное число
        return random.randint(min_take, max_take)
    else:
         # Иначе компьютер делает ход, чтобы оставить количество объектов - 1 кратным max_take + 1
        return (remaining_objects - 1) % (max_take + 1)


def play_game():
    """
    Запускает основной цикл игры "Битва чисел".
    
    Функция отвечает за инициализацию игры, управление ходами игрока и компьютера,
    а также за определение победителя.
    """
    try:
        while True: # Бесконечный цикл для возможности повторной игры
            objects = 20 # Начальное количество объектов
            min_take = int(input('Введите минимальное количество объектов для забора (например, 1):\n> '))
            max_take = int(input('Введите максимальное количество объектов для забора (например, 3):\n> '))
            first_move = input('Кто ходит первым? (игрок или компьютер):\n> ').strip().lower()
             # запрос кто ходит первым

            if first_move == 'игрок':
                player_turn = True
            elif first_move == 'компьютер':
                player_turn = False
            else:
                 # обработка некорректного ввода
                logger.error('Некорректный ввод, введите "игрок" или "компьютер"')
                continue

            print(f'Игра начинается с {objects} объектов.')

            while objects > 0:
                if player_turn:
                    # Ход игрока
                    take_objects = get_player_choice(min_take, max_take, objects)
                    objects -= take_objects
                    print(f'Оставшиеся объекты: {objects}')
                    if objects <= 0:
                         # Проверка условия победы игрока
                        print('Поздравляем! Вы выиграли!' if objects == 0 else 'Жаль, вы проиграли!')
                        break
                    player_turn = False
                else:
                     # Ход компьютера
                    take_objects = get_computer_choice(min_take, max_take, objects)
                    objects -= take_objects
                    print(f'Компьютер забрал {take_objects} объект(а).')
                    print(f'Оставшиеся объекты: {objects}')
                    if objects <= 0:
                         # Проверка условия победы компьютера
                        print('Жаль, вы проиграли!' if objects == 0 else 'Поздравляем! Вы выиграли!')
                        break
                    player_turn = True
            
            play_again = input('Хотите сыграть снова? (да/нет)\n> ').strip().lower()
            if play_again != 'да':
                break  # Выход из цикла, если игрок не хочет играть снова
    except Exception as e:
        logger.error(f'Произошла ошибка во время игры: {e}') # Логирование общей ошибки
        ...
```