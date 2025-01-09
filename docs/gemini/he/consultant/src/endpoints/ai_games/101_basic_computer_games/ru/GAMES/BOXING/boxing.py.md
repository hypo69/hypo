# Анализ кода модуля `boxing.py`

**Качество кода**

*   **Соответствие требованиям к формату кода (1-10):** 6
    *   **Плюсы:**
        *   Код в целом соответствует логике игры "Бокс".
        *   Используется `random` для генерации случайных чисел.
        *   Есть проверка корректности ввода от пользователя.
        *   Логика смены игрока и определения победителя реализована правильно.
    *   **Минусы:**
        *   Отсутствует документация в формате reStructuredText (RST).
        *   Не используются `j_loads` или `j_loads_ns`.
        *   Нет логирования ошибок через `src.logger.logger`.
        *   Излишнее использование `try-except` без `logger.error`.
        *   Нет обработки исключений в целом и  необходимых импортов.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring в формате reStructuredText (RST) для модуля, функций и переменных.
2.  **Импорты:** Добавить все необходимые импорты.
3.  **Обработка ошибок:** Заменить `try-except` на `logger.error` для логирования ошибок.
4.  **Чтение данных:** Использовать `j_loads` или `j_loads_ns` для чтения файлов, если это необходимо.
5.  **Форматирование:** Отредактировать код для соблюдения PEP 8.
6.  **Улучшение кода:** Разделить логику игры на отдельные функции для более читаемого кода.

**Улучшенный код**

```python
"""
Модуль для текстовой игры в бокс.
=========================================================================================

Модуль имитирует боксерский поединок между двумя игроками.
Игроки по очереди наносят удары, выбирая их силу.
Игра продолжается до нокаута одного из боксеров.

Пример использования
--------------------

.. code-block:: python

    # Запуск игры
    play_boxing()
"""
import random  # Импортируем модуль random для генерации случайных чисел
from src.utils.jjson import j_loads_ns  # Импортируем j_loads_ns
from src.logger.logger import logger  # Импортируем logger


def get_player_attack_type(current_player: int) -> int:
    """
    Получение типа атаки от текущего игрока.

    :param current_player: Номер текущего игрока (1 или 2).
    :return: Тип атаки (1 - слабый, 2 - средний, 3 - сильный).
    :raises ValueError: Если ввод пользователя некорректен.
    """
    while True:
        try:
            attack_type = int(input(f'Игрок {current_player}, выберите силу удара (1-слабый, 2-средний, 3-сильный): '))
            if attack_type in [1, 2, 3]:
                return attack_type
            else:
                print('Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.')
        except ValueError:
            print('Некорректный ввод. Пожалуйста, введите число.')
            logger.error('Некорректный ввод, ожидалось число')  # Используем logger.error для логирования ошибок


def check_hit(attack_type: int) -> bool:
    """
    Проверка, достиг ли удар цели.

    :param attack_type: Тип атаки (1 - слабый, 2 - средний, 3 - сильный).
    :return: True, если удар достиг цели, False в противном случае.
    """
    random_num = random.randint(1, 100)
    if attack_type == 1 and random_num <= 80:
        return True
    if attack_type == 2 and random_num <= 60:
        return True
    if attack_type == 3 and random_num <= 40:
        return True
    return False


def play_boxing():
    """
    Основная функция игры в бокс.
    """
    player1_health = 10  # Здоровье игрока 1
    player2_health = 10  # Здоровье игрока 2
    current_player = 1  # Начинаем с первого игрока

    while player1_health > 0 and player2_health > 0:
        print(f'Здоровье игрока 1: {player1_health}, Здоровье игрока 2: {player2_health}')
        
        attack_type = get_player_attack_type(current_player)  # Получаем тип атаки от текущего игрока
        hit = check_hit(attack_type)  # Проверяем, достиг ли удар цели

        if hit:
            print('Удар достиг цели!')
            if current_player == 1:
                player2_health -= 1
            else:
                player1_health -= 1
        else:
            print('Удар не достиг цели.')

        current_player = 3 - current_player  # Переключаем ход на следующего игрока

    if player1_health <= 0:
        print('Игрок 2 победил!')
    else:
        print('Игрок 1 победил!')


if __name__ == '__main__':
    play_boxing()
```