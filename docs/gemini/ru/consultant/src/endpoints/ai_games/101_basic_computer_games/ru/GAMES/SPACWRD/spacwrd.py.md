# Анализ кода модуля `spacwrd.py`

**Качество кода: 7/10**

-   **Плюсы:**
    -   Код логически структурирован и понятен.
    -   Разделение на функции облегчает чтение и понимание.
    -   Используются описательные имена переменных и функций.
    -   Присутствует подробная документация в виде комментариев, включая блок-схему.
-   **Минусы:**
    -   Отсутствует явное указание кодировки в начале файла.
    -   Не используется `j_loads` или `j_loads_ns` для загрузки данных, хотя это не требуется для данного кода.
    -   Не используется логирование ошибок с помощью `logger.error`.
    -   Не все комментарии соответствуют формату reStructuredText (RST).
    -   Избыточное использование `if ... else` в функции `display_word`.
    -   Функция `correct_guesses` может быть упрощена.
    -   В цикле `while` функции `play_spaceword_game` есть лишние проверки и ветвления.

**Рекомендации по улучшению:**

1.  **Добавить Docstring для модуля:**
    -   В начало файла добавить docstring в формате RST, описывающий модуль и его назначение.
2.  **Использовать RST для всех комментариев:**
    -   Преобразовать все комментарии в формат RST, включая docstring функций.
3.  **Улучшить функцию `display_word`:**
    -   Избавиться от лишнего `if-else`, можно использовать тернарный оператор.
4.  **Улучшить функцию `correct_guesses`:**
    -   Упростить логику подсчета угаданных букв. Можно использовать `sum()` с генератором.
5.  **Улучшить цикл `while`:**
    -   Убрать избыточную проверку условия завершения цикла.
6.  **Добавить логирование ошибок:**
    -   Использовать `logger.error` для отслеживания ошибок в коде.
7.  **Использовать f-строки:**
    -   Использовать f-строки для форматирования вывода, когда это возможно.

**Оптимизированный код**

```python
"""
Модуль для игры "Космическое слово"
=========================================================================================

Этот модуль реализует текстовую игру, в которой игрок угадывает слово, вводя по одной букве.
Компьютер выбирает случайное слово из списка, и игрок пытается его угадать.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_spaceword_game()
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
import random
#  Импорт модуля random для выбора случайного слова
from src.logger.logger import logger

def choose_word(word_list: list) -> str:
    """
    Выбирает случайное слово из списка.

    :param word_list: Список слов.
    :return: Случайное слово из списка.
    """
    return random.choice(word_list)

def display_word(word: str, guessed_letters: list) -> str:
  """
    Отображает слово, скрывая неугаданные буквы.

    :param word: Слово для отображения.
    :param guessed_letters: Список угаданных букв.
    :return: Отображаемое слово с открытыми буквами и пробелами.
  """
  return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def update_word(word: str, guessed_word: str, user_letter: str) -> str:
    """
    Обновляет отображаемое слово, открывая угаданные буквы.

    :param word: Загаданное слово.
    :param guessed_word: Текущее отображение слова с пробелами.
    :param user_letter: Буква, введенная пользователем.
    :return: Обновленное слово с открытыми буквами.
    """
    updated_word = ""
    for i, letter in enumerate(word):
        updated_word += f'{user_letter} ' if letter == user_letter else f'{guessed_word[i*2]} '
    return updated_word.strip()

def correct_guesses(guessed_letters: list, target_word: str) -> int:
    """
    Подсчитывает количество правильно угаданных букв в слове.

    :param guessed_letters: Список угаданных букв.
    :param target_word: Загаданное слово.
    :return: Количество правильно угаданных букв.
    """
    unique_letters = set(target_word)
    return sum(1 for letter in guessed_letters if letter in unique_letters and unique_letters.discard(letter) is None)

def play_spaceword_game():
    """
    Основная логика игры "Космическое слово".
    """
    word_list = [
        "APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
        "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    target_word = choose_word(word_list)
    guessed_word = "_ " * len(target_word)
    guessed_letters = []
    correct_guesses_count = 0

    print("Добро пожаловать в игру 'Космическое слово'!")
    print("Я загадал слово. Попробуй его угадать, вводя по одной букве.")
    
    while correct_guesses_count < len(target_word):
        print(f"\nСлово: {guessed_word}")
        user_letter = input("Введите букву: ").upper()

        if user_letter in target_word:
            guessed_letters.append(user_letter)
            guessed_word = update_word(target_word, guessed_word, user_letter)
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("Такой буквы нет в слове.")


        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()

"""
Объяснение кода:
1. **Импорт модуля `random`**:
   - `import random`: Импортирует модуль `random` для выбора случайного слова.
   - `from src.logger.logger import logger`: Импортирует модуль `logger` для логирования ошибок.

2. **Функция `choose_word(word_list)`**:
   - Принимает список слов `word_list` в качестве аргумента.
   - `return random.choice(word_list)`: Возвращает случайное слово из списка.

3. **Функция `display_word(word, guessed_letters)`**:
   - Принимает слово `word` и список угаданных букв `guessed_letters`.
   - Использует генератор списков для создания строки `display`, в которой отображает буквы из `word`, если они есть в `guessed_letters`, иначе `_`.
   - Возвращает отображаемое слово.

4. **Функция `update_word(word, guessed_word, user_letter)`**:
    - Принимает загаданное слово `word`, текущее отображение слова `guessed_word` и введенную пользователем букву `user_letter`.
    - Использует `enumerate` для перебора слова с индексами.
    - Формирует обновленную строку `updated_word` с помощью f-строк, подставляя угаданные буквы или символы из `guessed_word`.
    - Возвращает обновленную строку с открытыми буквами.

5. **Функция `correct_guesses(guessed_letters, target_word)`**:
    - Принимает список угаданных букв `guessed_letters` и загаданное слово `target_word`.
    - Создает множество `unique_letters` из букв слова `target_word` для отслеживания уникальных букв.
    - Использует `sum` с генератором для подсчета количества угаданных букв. Если буква угадана, она удаляется из `unique_letters`.
    - Возвращает количество угаданных букв.

6. **Функция `play_spaceword_game()`**:
   - Основная функция игры.
   - `word_list`: Список слов для игры.
   - `target_word = choose_word(word_list)`: Выбирает случайное слово.
    - `guessed_word = "_ " * len(target_word)`: Создает строку, представляющую слово, в котором все буквы заменены пробелами.
   - `guessed_letters = []`: Создает пустой список для хранения угаданных букв.
   - Выводит приветствие и описание игры.
   - **Основной игровой цикл `while correct_guesses_count < len(target_word)`**:
      - `print(f"\\nСлово: {guessed_word}")`: Выводит текущее состояние слова.
      - `user_letter = input("Введите букву: ").upper()`: Запрашивает ввод буквы и переводит ее в верхний регистр.
      - **Проверка введенной буквы:**
        - `if user_letter in target_word:`: Если буква есть в загаданном слове, то добавляем ее в список угаданных, обновляем слово и счётчик.
        - `else:`: Если буквы нет в слове, то выводим сообщение об ошибке.
        - Условие выхода из цикла проверяется в самом цикле `while correct_guesses_count < len(target_word)`.

7. **Запуск игры**:
   - `if __name__ == "__main__":`: Запускает функцию `play_spaceword_game()`, если скрипт запущен напрямую.
   - `play_spaceword_game()`: Вызов функции для начала игры.
"""
```