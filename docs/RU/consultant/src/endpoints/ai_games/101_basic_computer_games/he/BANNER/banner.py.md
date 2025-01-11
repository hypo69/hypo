# Анализ кода модуля `banner.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и логически понятен.
    - Используются функции для разделения логики игры, что повышает читаемость и возможность повторного использования кода.
    - Наличие подробного описания алгоритма и блок-схемы в начале кода.
    - Код соответствует основным требованиям (написан на Python, имеет комментарии)
    - Проверка на корректность ввода пользователя.
-  Минусы
    - Отсутствует использование reStructuredText (RST) для docstring и комментариев.
    - Не используется `src.utils.jjson` для загрузки данных из JSON. (нет json)
    - Отсутствует логирование ошибок с помощью `src.logger.logger` .
    - Не все комментарии содержат подробные объяснения к коду.
    - Использованы длинные комментарии после #, которые не подходят под reStructuredText (RST)
    - Не хватает docstring к функциям.

**Рекомендации по улучшению**

1. **Перевести комментарии в reStructuredText (RST)**: Перевести все комментарии и docstring в формат RST.
2. **Добавить логирование**: Добавить логирование ошибок с помощью `src.logger.logger`.
3. **Улучшить docstring**: Добавить docstring к функциям для более ясного описания их назначения, параметров и возвращаемых значений.
4. **Разделить блок проверок ввода:** Блок проверок ввода и логику игры можно разделить для лучшей читаемости.

**Оптимизированный код**

```python
"""
Модуль для реализации игры "Бейглс".
=========================================================================================

Этот модуль реализует игру "Бейглс", в которой игрок должен угадать
секретное число, состоящее из трех уникальных цифр.

Игра предоставляет подсказки в виде "Fermi" (цифра угадана и находится на правильной позиции),
"Pico" (цифра угадана, но не на правильной позиции) и "Bagels" (нет совпадений).

Пример использования
--------------------

.. code-block:: python

    play_bagels()
"""
import random
from src.logger.logger import logger

def generate_secret_number() -> str:
    """
    Генерирует случайное секретное число из трех уникальных цифр.

    :return: Строка, представляющая секретное число.
    :rtype: str
    """
    try:
        digits = list(range(10))
        random.shuffle(digits)
        secret_number = digits[:3]
        return "".join(map(str, secret_number))
    except Exception as ex:
        logger.error('Ошибка при генерации секретного числа', ex)
        return None


def get_clues(user_guess: str, secret_number: str) -> str:
    """
    Предоставляет подсказки на основе предположения игрока и секретного числа.

    :param user_guess: Предположение игрока.
    :type user_guess: str
    :param secret_number: Секретное число.
    :type secret_number: str
    :return: Подсказка для игрока ("Fermi", "Pico", "Bagels").
    :rtype: str
    """
    clue = ""
    try:
        for i in range(len(user_guess)):
            if user_guess[i] == secret_number[i]:
                clue += "Fermi "
            elif user_guess[i] in secret_number:
                clue += "Pico "
        if not clue:
             clue = "Bagels"
        return clue.strip()
    except Exception as ex:
        logger.error('Ошибка при формировании подсказки', ex)
        return 'Bagels'


def play_bagels() -> None:
    """
    Запускает игровой процесс "Бейглс".

    Игроку предлагается угадать число, состоящее из трех уникальных цифр.
    Игра предоставляет подсказки до тех пор, пока игрок не угадает число.
    """
    try:
        secret_number = generate_secret_number()
        if secret_number is None:
            print("Не удалось сгенерировать секретное число.")
            return
        number_of_guesses = 0

        print("Бейглс: Попробуйте угадать число из 3 разных цифр.")

        while True:
            number_of_guesses += 1
            user_guess = input("Введите вашу догадку: ")

            if not user_guess.isdigit() or len(user_guess) != 3:
                print("Некорректный ввод. Пожалуйста, введите число из 3 цифр.")
                continue
            
            if user_guess == secret_number:
                print(f"Поздравляем! Вы угадали число {secret_number} за {number_of_guesses} попыток.")
                break
            else:
                clue = get_clues(user_guess, secret_number)
                print(clue)
    except Exception as ex:
        logger.error('Неизвестная ошибка во время игры.', ex)

if __name__ == "__main__":
    play_bagels() # запуск игры
```