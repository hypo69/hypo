# Анализ кода модуля `spacwrd.py`

**Качество кода**
*   **Соответствие требованиям к формату кода (1-10):** 8
    *   **Преимущества:**
        *   Код написан на языке Python.
        *   Реализована основная логика игры "Космическое слово".
        *   Используются функции для разделения логики, что улучшает читаемость кода.
        *   Имеется документация в виде комментариев.
        *   Присутствует блок-схема в формате mermaid.
    *   **Недостатки:**
        *   Отсутствует reStructuredText (RST) для документации.
        *   Не используются `j_loads` или `j_loads_ns`.
        *   Отсутствует обработка ошибок с использованием `logger.error`.
        *   Некоторые функции не имеют подробных docstring.
        *   Код можно улучшить, сделав его более модульным.
        *   Не используется импорт `logger` для записи ошибок.
        *   Некоторые переменные можно переименовать для лучшей читаемости.
        *   Документация не соответствует стандарту RST.

**Рекомендации по улучшению**

1.  **Формат документации:**
    *   Заменить все обычные комментарии на reStructuredText (RST) в docstring.
    *   Использовать `:param:` и `:return:` для описания параметров и возвращаемых значений функций.

2.  **Использование `j_loads`:**
    *   В данном коде нет чтения файлов, поэтому это требование не применяется.

3.  **Импорты:**
    *   Добавить импорт `from src.logger.logger import logger` для логирования ошибок.

4.  **Обработка ошибок:**
    *   Заменить блоки `try-except` на использование `logger.error` для записи ошибок.

5.  **Наименование переменных и функций:**
    *   Переименовать `user_letter` в `guessed_letter` для большей ясности.
    *   Уточнить имена переменных, чтобы они были более информативными.

6.  **Дополнительные улучшения:**
    *   Переписать комментарии в формате RST.
    *   Добавить docstring к каждой функции, методу и классу.
    *   Добавить проверки на ввод пользователя (например, что введена одна буква).
    *   Возможно, добавить возможность выбора уровня сложности (длины слова).

**Улучшенный код**
```python
"""
Модуль для игры "Космическое слово".
=========================================================================================

Этот модуль реализует текстовую игру, в которой игрок должен угадать загаданное компьютером слово, вводя буквы.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    play_spaceword_game()
"""

__author__ = 'hypo69 (hypo69@davidka.net)'
import random
from src.logger.logger import logger # Импорт logger для записи ошибок

def choose_word(word_list: list) -> str:
    """
    Выбирает случайное слово из списка.

    :param word_list: Список слов для выбора.
    :return: Случайно выбранное слово.
    """
    return random.choice(word_list) # Выбирает случайное слово из списка

def display_word(word: str, guessed_letters: list) -> str:
    """
    Отображает слово, скрывая неугаданные буквы.

    :param word: Загаданное слово.
    :param guessed_letters: Список угаданных букв.
    :return: Строка, представляющая слово с открытыми и скрытыми буквами.
    """
    display = "" # Инициализация пустой строки для отображения
    for letter in word:
      if letter in guessed_letters:
        display += letter + " " # Если буква угадана, добавляем её
      else:
        display += "_ " # Если не угадана, добавляем символ "_"
    return display.strip() # Возвращаем строку, убрав лишние пробелы

def update_word(word: str, guessed_word: str, guessed_letter: str) -> str:
    """
    Обновляет отображаемое слово, открывая угаданные буквы.

    :param word: Загаданное слово.
    :param guessed_word: Текущее отображение слова с пробелами.
    :param guessed_letter: Угаданная буква.
    :return: Обновленное отображение слова с открытыми буквами.
    """
    updated_word = "" # Инициализация пустой строки для обновления слова
    for i in range(len(word)):
        if word[i] == guessed_letter:
          updated_word += guessed_letter + " " # Если буква угадана, добавляем её
        else:
            updated_word += guessed_word[i*2] + " " # Если нет, добавляем символ с текущего отображения
    return updated_word.strip() # Возвращаем обновленную строку, убрав лишние пробелы

def correct_guesses(guessed_letters: list, target_word: str) -> int:
    """
    Считает количество правильно угаданных букв в слове.

    :param guessed_letters: Список угаданных букв.
    :param target_word: Загаданное слово.
    :return: Количество правильно угаданных букв.
    """
    count = 0 # Инициализируем счетчик угаданных букв
    unique_letters = set(target_word) # Создаем множество уникальных букв из загаданного слова
    for letter in guessed_letters:
        if letter in unique_letters:
            count += 1 # Увеличиваем счетчик, если буква есть в уникальных
            unique_letters.remove(letter) # Удаляем букву из множества уникальных
    return len(set(target_word)) - len(unique_letters) # Возвращаем количество угаданных букв

def play_spaceword_game():
    """
    Основная логика игры "Космическое слово".
    """
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ] # Список слов для игры
    target_word = choose_word(word_list) # Выбираем случайное слово
    guessed_word = "_ " * len(target_word) # Создаем закрытое слово
    guessed_letters = []  # Список угаданных букв
    correct_guesses_count = 0 # Счетчик правильно угаданных букв
    
    print("Добро пожаловать в игру \'Космическое слово\'!")
    print("Я загадал слово. Попробуй его угадать, вводя по одной букве.")
    
    while correct_guesses_count < len(target_word):
        print("\\nСлово:", guessed_word)
        try:
          guessed_letter = input("Введите букву: ").upper() # Запрашиваем букву и преобразуем в верхний регистр
          if not guessed_letter.isalpha() or len(guessed_letter) != 1: # Проверка ввода пользователя
              print("Пожалуйста, введите одну букву.")
              continue
        except Exception as e:
            logger.error(f'Ошибка при вводе буквы: {e}') # Логирование ошибки ввода
            continue
        
        if guessed_letter in target_word:
            guessed_letters.append(guessed_letter) # Добавляем угаданную букву в список
            guessed_word = update_word(target_word, guessed_word, guessed_letter) # Обновляем отображение слова
            correct_guesses_count = correct_guesses(guessed_letters, target_word) # Обновляем счетчик угаданных букв
        else:
            print("Такой буквы нет в слове.")

        
        if correct_guesses_count == len(target_word):
           print("\\nYOU GOT IT!") # Вывод сообщения о победе
           break

if __name__ == "__main__":
    play_spaceword_game() # Запуск игры
"""
Объяснение кода:
1. **Импорт модуля `random` и `logger`**:\n
   - `import random`: Импортирует модуль `random` для выбора случайного слова.\n
   - `from src.logger.logger import logger`: Импортирует модуль `logger` для записи ошибок.
2. **Функция `choose_word(word_list)`**:\n
   - Принимает список слов `word_list` в качестве аргумента.\n
   - `return random.choice(word_list)`: Возвращает случайное слово из списка.
3. **Функция `display_word(word, guessed_letters)`**:\n
   - Принимает слово `word` и список угаданных букв `guessed_letters`.\n
   - Создает строку `display`, в которой отображает буквы из `word` если они есть в `guessed_letters` или знак `_`.\n
   - Возвращает отображаемое слово.
4. **Функция `update_word(word, guessed_word, guessed_letter)`**:\n
    -   Принимает загаданное слово `word`, текущее отображение слова `guessed_word`, и введенную пользователем букву `guessed_letter`.\n
    -   Создает строку `updated_word`, которая сначала пустая.\n
    -   Циклом `for` проверяет каждую букву в слове `word`.\n
    -   Если текущая буква равна `guessed_letter`, то добавляет ее в `updated_word` c пробелом.\n
    -   В противном случае добавляет символ из `guessed_word`.\n
    -   Возвращает обновленную строку с открытыми буквами.
5. **Функция `correct_guesses(guessed_letters, target_word)`**:\n
    -  Принимает список угаданных букв `guessed_letters` и загаданное слово `target_word`.\n
    -  Создаёт множество `unique_letters` из букв слова `target_word` для отслеживания уникальных букв.\n
    -  Циклом `for` считает сколько букв из `guessed_letters` есть в слове.\n
    -  Исключает уже подсчитанные буквы из `unique_letters`.\n
    -  Возвращает количество угаданных букв, которое равно разнице длинны множества уникальных букв и длинны остатка множества.
6. **Функция `play_spaceword_game()`**:\n
   - Основная функция игры.\n
   - `word_list`: Список слов для игры.\n
   - `target_word = choose_word(word_list)`: Выбирает случайное слово.\n
   - `guessed_word = "_ " * len(target_word)`: Создает строку, представляющую слово, в котором все буквы заменены пробелами.\n
   - `guessed_letters = []`: Создает пустой список для хранения угаданных букв.\n
   - Выводит приветствие и описание игры.\n
   - **Основной игровой цикл `while correct_guesses_count < len(target_word)`**:\n
      - `print("\\nСлово:", guessed_word)`: Выводит текущее состояние слова.\n
      -   `guessed_letter = input("Введите букву: ").upper()`: Запрашивает ввод буквы и переводит ее в верхний регистр.\n
      -   **Проверка введенной буквы:**\n
        - `if guessed_letter in target_word:`: Если буква есть в загаданном слове, то добавляем ее в список угаданных, обновляем слово и счётчик.\n
        - `else:`: Если буквы нет в слове, то выводим сообщение об ошибке.\n
        - Если угаданных букв столько же, сколько букв в слове, то выводится сообщение о победе и цикл завершается.
7. **Запуск игры**:\n
   - `if __name__ == "__main__":`: Запускает функцию `play_spaceword_game()`, если скрипт запущен напрямую.\n
   - `play_spaceword_game()`: Вызов функции для начала игры.
"""
```