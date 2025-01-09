# Анализ кода модуля `hurkle.py`

**Качество кода**
-   **Соответствие требованиям к формату кода (1-10):** 8
    -   **Преимущества:**
        -   Код хорошо структурирован, логика игры понятна.
        -   Используются информативные имена переменных.
        -   Функция `get_direction` четко определяет направление.
        -   Присутствует обработка исключения ValueError.
    -   **Недостатки:**
        -   Отсутствует docstring модуля.
        -   Не все функции и переменные имеют docstring.
        -   Используется стандартный `print` для вывода сообщений, что не соответствует рекомендациям по использованию логгера.
        -   В коде есть недочеты в части использования reStructuredText (RST) для docstrings и комментариев.

**Рекомендации по улучшению**

1.  Добавить docstring модуля в формате RST.
2.  Добавить docstring для всех функций и переменных в формате RST.
3.  Использовать `from src.logger.logger import logger` для регистрации ошибок и `logger.info` для сообщений.
4.  Заменить стандартный `print` на `logger.info` для информационных сообщений.
5.  Оптимизировать обработку исключений, используя `logger.error`.
6.  Пересмотреть имеющиеся комментарии и переписать их с учетом стиля RST.
7.  Улучшить форматирование кода, где это необходимо.
8.  Изменить формат docstring функции `get_direction` в соответствии с RST.

**Улучшенный код**

```python
"""
Модуль для игры HURKLE.
=========================================================================================

Эта игра представляет собой поиск "HURKLE" на карте 10x10. Игрок вводит координаты,
и игра предоставляет подсказки о направлении до HURKLE.

Описание правил:
    1. HURKLE прячется на карте 10x10, координаты выбираются случайно.
    2. Игрок делает ходы, вводя координаты X и Y.
    3. После каждого хода игрок получает подсказку о направлении (север, юг, восток, запад,
       северо-восток, юго-восток, северо-запад, юго-запад) от введенной координаты до HURKLE.
    4. Игра продолжается, пока игрок не найдет HURKLE.

Пример использования
--------------------

.. code-block:: python

    import random
    from src.logger.logger import logger

    # Код игры HURKLE
"""
import random
from src.logger.logger import logger  # Импорт логгера для регистрации событий


def get_direction(user_x: int, user_y: int, hurkle_x: int, hurkle_y: int) -> str:
    """
    Определяет направление от координат пользователя к координатам HURKLE.

    :param user_x: Координата X, введенная пользователем.
    :type user_x: int
    :param user_y: Координата Y, введенная пользователем.
    :type user_y: int
    :param hurkle_x: Координата X HURKLE.
    :type hurkle_x: int
    :param hurkle_y: Координата Y HURKLE.
    :type hurkle_y: int
    :return: Строка, представляющая направление.
    :rtype: str
    """
    if user_x < hurkle_x and user_y < hurkle_y:
        return 'СЕВЕРО-ВОСТОК'
    elif user_x < hurkle_x and user_y > hurkle_y:
        return 'ЮГО-ВОСТОК'
    elif user_x > hurkle_x and user_y < hurkle_y:
        return 'СЕВЕРО-ЗАПАД'
    elif user_x > hurkle_x and user_y > hurkle_y:
        return 'ЮГО-ЗАПАД'
    elif user_x < hurkle_x:
        return 'ВОСТОК'
    elif user_x > hurkle_x:
        return 'ЗАПАД'
    elif user_y < hurkle_y:
        return 'СЕВЕР'
    else:
        return 'ЮГ'


# Генерируем случайные координаты HURKLE
hurkle_x = random.randint(1, 10)  # Координата X HURKLE
hurkle_y = random.randint(1, 10)  # Координата Y HURKLE

# Инициализируем счетчик ходов
number_of_guesses = 0 # Количество попыток игрока

# Основной игровой цикл
while True:
    # Увеличиваем счетчик ходов
    number_of_guesses += 1 # Увеличение счетчика попыток

    # Запрашиваем ввод координат у пользователя
    try:
        user_x = int(input('Введите X координату (1-10): '))  # Запрос координаты X
        user_y = int(input('Введите Y координату (1-10): '))  # Запрос координаты Y
    except ValueError as ex: # Обработка ошибки ввода
        logger.error('Неверный ввод. Пожалуйста, введите целые числа.', exc_info=ex)  # Вывод сообщения об ошибке
        continue

    # Проверяем, угадал ли пользователь местоположение HURKLE
    if user_x == hurkle_x and user_y == hurkle_y: # Проверка, угадал ли игрок
        logger.info(f'ПОЗДРАВЛЯЮ! Вы нашли HURKLE за {number_of_guesses} ходов!') # Вывод сообщения о победе
        break

    # Вычисляем и выводим направление
    direction = get_direction(user_x, user_y, hurkle_x, hurkle_y) # Получение направления
    logger.info(direction) # Вывод направления
```