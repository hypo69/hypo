# Анализ кода модуля nim.py

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, разбит на функции, что делает его читаемым и понятным.
    - Игровой процесс реализован логически правильно.
    - Есть обработка некорректного ввода пользователя (не число, неверный номер кучки или количество камней).
    - Присутствует подробное описание алгоритма и блок-схема в начале кода.
    - Код документирован с использованием docstring для функций.
- Минусы
    - Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
    - Не используется логирование ошибок через `logger.error`.
    - Не везде используется форматирование кода в соответствии с `reStructuredText`.
    - Не все комментарии соответствуют формату RST.
    - Отсутствует описание модуля в формате RST.

**Рекомендации по улучшению**
1. Добавить импорты `j_loads` и `j_loads_ns` из `src.utils.jjson` и `logger` из `src.logger.logger`.
2. Заменить `print` на `logger.info` для вывода сообщений об ошибках и для вывода текущего состояния кучек.
3. Добавить обработки исключений с логированием с помощью `logger.error` для непредвиденных ситуаций.
4. Переписать docstring в соответствии с reStructuredText (RST).
5. Добавить описание модуля в формате RST.
6. Переписать комментарии в соответствии с требованиями в RST.

**Оптимизированный код**

```python
"""
Модуль для реализации игры NIM.
=========================================================================================

Этот модуль реализует классическую игру NIM для двух игроков.
В начале игры есть несколько кучек камней, и игроки по очереди берут любое количество
камней из одной кучки. Выигрывает тот, кто возьмет последний камень.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_nim()
"""
import random
# импортируем logger
from src.logger.logger import logger

# Функция для отображения кучек камней
def display_piles(piles: list):
    """
    Выводит текущее состояние кучек камней.

    :param piles: Список, представляющий кучки камней.
    :type piles: list
    """
    logger.info("Текущее состояние кучек:")
    for i, pile in enumerate(piles):
        logger.info(f"Кучка {i + 1}: {pile} камней")


# Функция для хода игрока
def get_player_move(piles: list, player: int) -> tuple:
    """
    Запрашивает у игрока номер кучки и количество камней для удаления.

    :param piles: Список, представляющий кучки камней.
    :type piles: list
    :param player: Номер текущего игрока (1 или 2).
    :type player: int
    :return: Кортеж, содержащий номер кучки и количество камней для удаления.
    :rtype: tuple
    """
    while True:
        try:
            # Запрос ввода номера кучки от игрока
            pile_number = int(input(f"Игрок {player}, выберите номер кучки (1-{len(piles)}): ")) - 1
            # Проверка корректности номера кучки
            if 0 <= pile_number < len(piles):
                # Запрос ввода количества камней для удаления
                stones_to_remove = int(input(f"Игрок {player}, сколько камней взять из кучки {pile_number + 1}: "))
                # Проверка корректности количества камней
                if 0 < stones_to_remove <= piles[pile_number]:
                    return pile_number, stones_to_remove
                else:
                    logger.error("Недопустимое количество камней. Пожалуйста, выберите значение от 1 до текущего количества в кучке.")
            else:
                logger.error("Недопустимый номер кучки. Пожалуйста, выберите существующую кучку.")
        except ValueError:
            logger.error("Неверный ввод. Пожалуйста, введите целые числа.")
        except Exception as ex:
            logger.error(f"Произошла непредвиденная ошибка: {ex}", exc_info=True)


# Основная функция игры
def play_nim():
    """
    Реализует игру NIM.
    """
    # Инициализация кучек камней
    piles = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    current_player = 0  # 0 - игрок 1, 1 - игрок 2

    # Игровой цикл
    while sum(piles) > 0:
        display_piles(piles)
        # Ход текущего игрока
        pile_number, stones_to_remove = get_player_move(piles, current_player + 1)
        # Обновление кучи после хода игрока
        piles[pile_number] -= stones_to_remove
        # Переключение игрока
        current_player = (current_player + 1) % 2
    # Объявление победителя
    logger.info(f"Игрок {current_player + 1} победил!")


# Запуск игры
if __name__ == "__main__":
    play_nim()
```