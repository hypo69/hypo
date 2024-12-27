# Анализ кода модуля spacwrd.py

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разделен на функции, что делает его читаемым и поддерживаемым.
    - Логика игры реализована корректно, игра работает согласно описанию.
    - Используются информативные названия переменных и функций.
    - Присутствует подробная документация в формате reStructuredText (RST).
    - Алгоритм и блок-схема в описании соответствует логике игры
-  Минусы
    - Отсутствует обработка ошибок, таких как некорректный ввод пользователя (не буква, несколько букв).
    - Нет логирования событий, что затрудняет отладку и мониторинг.
    -   Используется стандартный `print` для вывода информации пользователю, который следует заменить на более гибкий механизм логирования.
    -  Имеется избыточное использование пробелов в строках, например `updated_word += user_letter + " "` и `display += letter + " "`, которые можно оптимизировать.
    - Отсутствует импорт `logger`.
    -   В функциях `display_word` и `update_word` используется добавление пробелов после каждой буквы. Что выглядит странно, можно использовать `join`.

**Рекомендации по улучшению**

1.  **Обработка ошибок**:
    -   Добавить проверку ввода пользователя, чтобы убедиться, что введена только одна буква.
    -   Обрабатывать исключения при вводе пользователя.
2.  **Логирование**:
    -   Использовать `logger` для записи информации о ходе игры, ошибках и действиях пользователя.
3.  **Улучшение вывода**:
    -   Избегать избыточных пробелов при выводе слова. Использовать `join`.
4.  **Общая оптимизация**:
    -    Удалить избыточные пробелы при конкатенации строк.

**Оптимизированный код**

```python
"""
Модуль реализует текстовую игру "Космическое слово".
=========================================================================================

Игра "Космическое слово" - это текстовая игра, в которой игрок пытается угадать
загаданное компьютером слово, вводя буквы. Компьютер отображает слово с пробелами
вместо неугаданных букв. После каждой попытки игрок получает информацию о том,
сколько букв он угадал, и может продолжать угадывать оставшиеся. Игра заканчивается,
когда игрок угадывает все буквы слова.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == "__main__":
        play_spaceword_game()
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
import random
from src.logger.logger import logger

def choose_word(word_list: list[str]) -> str:
    """
    Выбирает случайное слово из списка.

    :param word_list: Список слов, из которого нужно выбрать слово.
    :return: Случайно выбранное слово.
    """
    return random.choice(word_list)

def display_word(word: str, guessed_letters: list[str]) -> str:
    """
    Отображает слово, скрывая неугаданные буквы.

    :param word: Загаданное слово.
    :param guessed_letters: Список угаданных букв.
    :return: Строка, представляющая слово с открытыми и скрытыми буквами.
    """
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)


def update_word(word: str, guessed_word: str, user_letter: str) -> str:
    """
    Обновляет отображаемое слово, открывая угаданные буквы.

    :param word: Загаданное слово.
    :param guessed_word: Текущее состояние слова с открытыми и скрытыми буквами.
    :param user_letter: Буква, введенная пользователем.
    :return: Обновленная строка слова с открытыми буквами.
    """
    updated_word = [user_letter if word[i] == user_letter else guessed_word[i*2] for i in range(len(word))]
    return " ".join(updated_word)


def correct_guesses(guessed_letters: list[str], target_word: str) -> int:
    """
    Считает количество правильно угаданных букв в слове.

    :param guessed_letters: Список угаданных букв.
    :param target_word: Загаданное слово.
    :return: Количество правильно угаданных букв.
    """
    count = 0
    unique_letters = set(target_word)
    for letter in guessed_letters:
        if letter in unique_letters:
            count += 1
            unique_letters.remove(letter)
    return len(set(target_word)) - len(unique_letters)


def play_spaceword_game():
    """
    Основная логика игры "Космическое слово".
    """
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    # Код исполняет выбор случайного слова из списка
    target_word = choose_word(word_list)
    # Код создаёт закрытое слово, состоящее из символов "_"
    guessed_word = "_ " * len(target_word)
    # Код создаёт список для хранения угаданных букв
    guessed_letters = []
    correct_guesses_count = 0

    print("Добро пожаловать в игру \'Космическое слово\'!")
    print("Я загадал слово. Попробуй его угадать, вводя по одной букве.")

    while correct_guesses_count < len(target_word):
        print("\nСлово:", guessed_word)
        # Код запрашивает у пользователя ввод буквы и переводит её в верхний регистр
        user_letter = input("Введите букву: ").upper()

        if not user_letter.isalpha() or len(user_letter) != 1:
            logger.error(f"Некорректный ввод: {user_letter}. Введите одну букву.")
            continue

        # Код проверяет, есть ли введенная буква в загаданном слове
        if user_letter in target_word:
            guessed_letters.append(user_letter)
            # Код обновляет отображаемое слово с открытой буквой
            guessed_word = update_word(target_word, guessed_word, user_letter)
            # Код считает количество правильно угаданных букв
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("Такой буквы нет в слове.")

        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()
```