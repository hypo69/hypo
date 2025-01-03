# Анализ кода модуля `digits.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    - Используются содержательные имена переменных и функций, что делает код более понятным.
    - Присутствует подробное описание алгоритма игры и блок-схема в комментариях.
    - Имеется обработка ввода количества раундов, что предотвращает ошибки.
    - Код соответствует PEP8, за исключением отсутствия docstring в начале модуля.
- Минусы
    - Отсутствует описание модуля в формате reStructuredText (RST).
    - Отсутствует логирование ошибок.
    - Присутствует блок `try-except` для обработки ошибок ввода, который может быть заменен на логирование.

**Рекомендации по улучшению**

1. Добавить описание модуля в формате reStructuredText (RST) в начале файла.
2. Добавить логирование ошибок с использованием `from src.logger.logger import logger`.
3. Заменить обработку ошибок ввода с помощью `try-except` на логирование.
4. Добавить docstring в формате RST к каждой функции.

**Оптимизированный код**

```python
"""
Модуль для реализации игры ACE.
=========================================================================================

Этот модуль реализует игру в карты "ACE", где два игрока по очереди тянут карты из колоды,
игрок с наибольшим количеством очков за все раунды выигрывает. Туз считается за 1 очко, карты
с номерами от 2 до 10 считаются по номиналу, валет, дама и король считаются за 10 очков.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_ace_game()
"""
import random
from src.logger.logger import logger


def calculate_card_value(card: str) -> int:
    """
    Вычисляет значение карты.

    Туз ('A') равен 1, валет ('J'), дама ('Q'), король ('K') равны 10, остальные по номиналу.

    :param card: Строковое представление карты.
    :return: Числовое значение карты.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        try:
            return int(card)
        except ValueError:
            logger.error(f"Не удалось преобразовать карту '{card}' в число.", exc_info=True)
            return 0


def draw_card(deck: list) -> tuple[str, int]:
    """
    Вытягивает случайную карту из колоды.

    :param deck: Список строк, представляющих колоду карт.
    :return: Кортеж, содержащий карту (строка) и ее числовое значение (целое число).
    """
    card = random.choice(deck)
    return card, calculate_card_value(card)


def play_ace_game():
    """
    Основная функция игры ACE.

    Инициализирует игру, запрашивает количество раундов, проводит раунды,
    выводит результаты и определяет победителя.
    """
    player1_score = 0  # Инициализация счета игрока 1
    player2_score = 0  # Инициализация счета игрока 2
    
    # Создание колоды карт
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    
    try:
        number_of_rounds = int(input("Сколько раундов вы хотите сыграть? ")) # Запрос количества раундов у пользователя
        if number_of_rounds <= 0:
            print("Количество раундов должно быть положительным числом.")
            return
    except ValueError:
        logger.error("Введено некорректное значение количества раундов.", exc_info=True)
        print("Пожалуйста, введите целое число для количества раундов.")
        return

    for round_number in range(1, number_of_rounds + 1):
      print(f"\nРаунд {round_number}:")

      # Игрок 1 вытягивает карту
      card1, card1_value = draw_card(deck)
      print(f"Игрок 1 вытащил {card1} ({card1_value} очков)")
      player1_score += card1_value  # Обновление счета игрока 1

      # Игрок 2 вытягивает карту
      card2, card2_value = draw_card(deck)
      print(f"Игрок 2 вытащил {card2} ({card2_value} очков)")
      player2_score += card2_value  # Обновление счета игрока 2

      # Сравнение очков за раунд
      if card1_value > card2_value:
          print("Игрок 1 выиграл этот раунд")
      elif card2_value > card1_value:
          print("Игрок 2 выиграл этот раунд")
      else:
          print("Ничья в этом раунде")
    
    # Вывод общего счета
    print(f"\nОбщий счет:")
    print(f"Игрок 1: {player1_score} очков")
    print(f"Игрок 2: {player2_score} очков")

    # Определение победителя игры
    if player1_score > player2_score:
        print("Игрок 1 выиграл игру!")
    elif player2_score > player1_score:
        print("Игрок 2 выиграл игру!")
    else:
        print("Ничья в игре!")


if __name__ == "__main__":
    play_ace_game()
"""
Объяснение кода:
1.  **Импорт модуля `random` и `logger`**:\
    -   `import random`: Импортирует модуль `random`, который используется для генерации случайных карт.\
    -   `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок.
2.  **Функция `calculate_card_value(card)`**:\
    -   Принимает карту в качестве аргумента.\
    -   Возвращает числовое значение карты.\
        -   Для карт \'J\', \'Q\', \'K\' возвращает 10.\
        -   Для карты \'A\' возвращает 1.\
        -   Для остальных карт возвращает их номинал (преобразуя строку в целое число).\
        -   Обрабатывает ошибку ValueError, если карта не распознана, возвращает 0 и записывает ошибку в лог.\
3.  **Функция `draw_card(deck)`**:\
    -   Принимает колоду карт в качестве аргумента.\
    -   Выбирает случайную карту из колоды с помощью `random.choice()`.\
    -   Возвращает карту и ее числовое значение.\
4.  **Функция `play_ace_game()`**:\
    -   `player1_score = 0` и `player2_score = 0`: Инициализирует счетчики очков для игроков.\
    -   `deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4`: Создает стандартную колоду из 52 карт.\
    -   Запрашивает у пользователя количество раундов и проверяет ввод на корректность (чтобы было целое положительное число) и логирует ошибку, если ввод не корректен.\
    -   **Основной цикл `for round_number in range(1, number_of_rounds + 1):`**:\
        -   Цикл выполняется для каждого раунда игры.\
        -   **Карта игрока 1**:\
            -   `card1, card1_value = draw_card(deck)`: Игрок 1 вытягивает карту, и определяется её значение.\
            -   Выводится информация о карте и ее значении.\
            -   `player1_score += card1_value`: Значение карты добавляется к общему счету игрока 1.\
        -   **Карта игрока 2**:\
            -   `card2, card2_value = draw_card(deck)`: Игрок 2 вытягивает карту, и определяется её значение.\
            -   Выводится информация о карте и ее значении.\
            -   `player2_score += card2_value`: Значение карты добавляется к общему счету игрока 2.\
        -   **Сравнение очков**:\
            -   Сравниваются значения карт игроков в текущем раунде.\
            -   Выводится сообщение о победе одного из игроков или о ничьей в раунде.\
    -   **Вывод общего счета**:\
        -   Выводит общий счет каждого игрока.\
    -   **Определение победителя игры**:\
        -   Сравниваются общие очки игроков.\
        -   Выводится сообщение о победе одного из игроков или о ничьей в игре.\
5.  **Запуск игры**:\
    -   `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_ace_game()` будет запущена только если файл исполняется напрямую, а не импортируется как модуль.\
    -   `play_ace_game()`: Вызывает функцию для начала игры.
"""
```