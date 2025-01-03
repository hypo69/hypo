# Анализ кода модуля `batnum.py`

**Качество кода**

*   **Соответствие требованиям к формату кода (1-10):**

    *   **Преимущества:**
        *   Код написан на Python и логически структурирован.
        *   Присутствует базовое описание игры, алгоритма и блок-схемы в начале файла.
        *   Используются циклы `while` для основного игрового процесса и для проверки ввода пользователя.
        *   Присутствует обработка исключений `ValueError` для некорректного ввода.
        *   Код читаем и понятен для базового понимания логики игры.

    *   **Недостатки:**
        *   Отсутствует документация в формате reStructuredText (RST).
        *   Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        *   Отсутствует импорт и использование `logger` для логирования ошибок и отладки.
        *   Используются стандартные блоки `try-except`, вместо обработки ошибок через `logger.error`.
        *   Нет разделения кода на функции для лучшей читаемости и переиспользования.
        *   В коде присутствуют стандартные комментарии, вместо использования docstring.

**Рекомендации по улучшению**

1.  **Документирование:**
    *   Добавить описание модуля в формате RST в начале файла.
    *   Переписать все комментарии в формате docstring для функций и переменных.

2.  **Использование `logger`:**
    *   Импортировать `logger` из `src.logger.logger`.
    *   Заменить `print` на `logger.info` для вывода текущей суммы и сообщений о выигрыше/проигрыше.
    *   Заменить `print` в блоке `except ValueError` на `logger.error` для записи ошибок.

3.  **Разделение на функции:**
    *   Вынести логику ввода пользователя в отдельные функции для каждого игрока.
    *   Создать функцию для проверки выигрыша и вывода соответствующего сообщения.
    *   Создать функцию для основного игрового цикла.

4.  **Обработка ошибок:**
    *   Использовать `logger.error` для логирования ошибок ввода вместо `print` в блоках `except`.

5.  **Общая структура кода:**
    *   Использовать единый стиль именования переменных.
    *   Добавить пояснения к каждой функции в формате RST.
    *   Избегать избыточных блоков `try-except`.

**Улучшенный код**

```python
"""
Модуль для игры "Битва чисел"
=========================================================================================

Модуль реализует игру "Битва чисел" (BATNUM), в которой два игрока по очереди вводят числа
от 1 до 10, чтобы довести общую сумму до 100. Игрок, после ввода которого сумма достигает
100 или более, проигрывает.

Правила игры:
1. Два игрока по очереди вводят целые числа от 1 до 10.
2. Каждое введенное число прибавляется к общей сумме.
3. Игрок, после ввода которого сумма достигает 100 или более, проигрывает.
4. Начинает игру первый игрок.
"""
import logging  # импортируем модуль logging #
from src.logger.logger import logger # импортируем logger для логирования #


__author__ = 'hypo69 (hypo69@davidka.net)'


def get_player_input(player_number: int) -> int:
    """
    Запрашивает ввод числа от игрока и проверяет его корректность.

    :param player_number: Номер игрока (1 или 2).
    :return: Введенное игроком целое число от 1 до 10.
    :raises ValueError: Если ввод не является целым числом.
    """
    while True:
        try:
            player_input = int(input(f"Игрок {player_number}, введите число от 1 до 10: "))
            if 1 <= player_input <= 10:
                return player_input
            else:
                logger.info("Пожалуйста, введите число от 1 до 10.") # логируем ошибку вместо print #
        except ValueError as e:
            logger.error("Некорректный ввод, требуется целое число.", exc_info=e) # логируем ошибку вместо print #


def check_winner(total_sum: int, player_number: int) -> bool:
    """
    Проверяет, не проиграл ли игрок, и выводит сообщение о результате.

    :param total_sum: Текущая общая сумма.
    :param player_number: Номер игрока (1 или 2).
    :return: True, если игрок проиграл, False, если нет.
    """
    if total_sum >= 100:
        logger.info(f"Игрок {player_number} проиграл!") # логируем сообщение вместо print #
        return True
    return False


def play_batnum() -> None:
    """
    Основная функция для запуска игры "Битва чисел".

    Управляет игровым процессом, включая запросы ввода от игроков,
    проверку выигрыша и вывод текущей суммы.
    """
    total_sum = 0 # Инициализация суммы #
    while True: # Основной игровой цикл #
        logger.info(f"Текущая сумма: {total_sum}") # логируем текущую сумму #
        player1_input = get_player_input(1) # получение ввода от первого игрока #
        total_sum += player1_input # добавляем к общей сумме число #
        if check_winner(total_sum, 1): # проверяем, не проиграл ли первый игрок #
            break
        logger.info(f"Текущая сумма: {total_sum}") # логируем текущую сумму #
        player2_input = get_player_input(2) # получение ввода от второго игрока #
        total_sum += player2_input  # добавляем к общей сумме число #
        if check_winner(total_sum, 2): # проверяем, не проиграл ли второй игрок #
            break


if __name__ == "__main__":
    play_batnum()
```