# Анализ кода модуля hang.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, разбит на функции, что облегчает чтение и понимание.
    - Логика игры "Виселица" реализована правильно.
    - Используются понятные имена переменных и функций.
    - Присутствуют docstring, описывающие назначение функций.
    - Есть блок-схема, описывающая работу программы.
- Минусы
    - Отсутствует обработка исключений.
    - Нет логирования ошибок.
    - Комментарии не соответствуют формату RST.
    - Используются магические числа (например, 6 для максимального числа ошибок).
    - Жестко задан список слов, можно добавить возможность загрузки из файла.

**Рекомендации по улучшению**
1.  **Форматирование документации**:
    - Привести все комментарии и docstring к формату reStructuredText (RST).
2.  **Обработка ошибок**:
    -   Использовать `try-except` блоки для обработки возможных ошибок при вводе данных от пользователя.
    -   Внедрить логирование ошибок с помощью `from src.logger.logger import logger`.
3.  **Константы**:
    -   Вынести максимальное количество ошибок в константу (например, `MAX_ERRORS = 6`).
4.  **Загрузка слов**:
    -   Реализовать возможность загрузки списка слов из файла, например JSON, с использованием `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  **Улучшение читаемости**:
    -   Разделить функцию `play_hangman` на более мелкие, чтобы улучшить читаемость и возможность повторного использования кода.

**Оптимизированный код**
```python
"""
Модуль для реализации игры "Виселица"
====================================

Этот модуль содержит функции для игры в "Виселицу", включая отображение виселицы и логику игры.

.. note::
    Игра основана на выборе случайного слова из списка.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_hangman()
"""
import random
# TODO: добавить импорт j_loads или j_loads_ns из src.utils.jjson
from src.logger.logger import logger

# Максимальное количество ошибок
MAX_ERRORS = 6

# Список слов для игры
# TODO: заменить на загрузку из файла
WORDS = ["python", "java", "kotlin", "javascript", "swift", "ruby", "csharp"]


def draw_hangman(errors: int) -> None:
    """
    Отображает виселицу в зависимости от количества ошибок.

    :param errors: Количество ошибок, совершенных игроком.
    :type errors: int
    :raises IndexError: Если `errors` выходит за пределы допустимого диапазона.
    """
    hangman_stages = [
        """
          ________
         |        |
         |
         |
         |
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |
         |
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |        |
         |
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |       /|
         |
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |       /|\\
         |
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |       /|\\
         |       /
         |
        ---
        """,
        """
          ________
         |        |
         |        O
         |       /|\\
         |       / \\
         |
        ---
        """
    ]
    try:
        print(hangman_stages[errors])
    except IndexError as e:
        logger.error(f"Недопустимое количество ошибок: {errors}", exc_info=True)
        raise  # Перевыбрасываем исключение после логирования


def choose_word() -> str:
    """
    Выбирает случайное слово из списка.

    :return: Случайно выбранное слово в верхнем регистре.
    :rtype: str
    """
    return random.choice(WORDS).upper()


def create_guess_string(word: str) -> str:
    """
    Создает строку из прочерков, соответствующую длине слова.

    :param word: Слово для создания строки прочерков.
    :type word: str
    :return: Строка из прочерков.
    :rtype: str
    """
    return "_" * len(word)


def update_guess_string(guess_string: str, target_word: str, user_letter: str) -> str:
    """
    Обновляет строку отгадываемого слова, показывая угаданные буквы.

    :param guess_string: Текущая строка отгадываемого слова.
    :type guess_string: str
    :param target_word: Загаданное слово.
    :type target_word: str
    :param user_letter: Буква, введенная пользователем.
    :type user_letter: str
    :return: Обновленная строка отгадываемого слова.
    :rtype: str
    """
    new_guess_string = ""
    for i in range(len(target_word)):
        if target_word[i] == user_letter:
            new_guess_string += user_letter
        else:
            new_guess_string += guess_string[i]
    return new_guess_string


def check_win(guess_string: str, target_word: str) -> bool:
    """
    Проверяет, угадано ли слово.

    :param guess_string: Текущая строка отгадываемого слова.
    :type guess_string: str
    :param target_word: Загаданное слово.
    :type target_word: str
    :return: `True`, если слово угадано, `False` в противном случае.
    :rtype: bool
    """
    return guess_string == target_word


def play_hangman() -> None:
    """
    Основная функция игры в виселицу.
    
    Содержит основной игровой цикл и логику игры.
    """
    target_word = choose_word()
    guess_string = create_guess_string(target_word)
    number_of_errors = 0

    while number_of_errors < MAX_ERRORS and "_" in guess_string:
        print("Слово:", guess_string)
        try:
            user_letter = input("Введите букву: ").upper()
        except Exception as e:
             logger.error(f"Ошибка ввода от пользователя: {e}", exc_info=True)
             return

        if user_letter in target_word:
            guess_string = update_guess_string(guess_string, target_word, user_letter)
            if check_win(guess_string, target_word):
                print("ПОЗДРАВЛЯЮ! Вы угадали слово:", target_word)
                return
        else:
            number_of_errors += 1
            draw_hangman(number_of_errors)

    if number_of_errors == MAX_ERRORS:
        print("СОЖАЛЕЮ, вы не отгадали слово. Загаданное слово:", target_word)


if __name__ == "__main__":
    play_hangman()
"""
Объяснение кода:

1.  **Импорт модулей:**
    -   `import random`: Импортирует модуль random для случайного выбора слова.
    -   `from src.logger.logger import logger`: Импортирует логгер для обработки ошибок.
   
2. **Константа `MAX_ERRORS`:**
    - `MAX_ERRORS = 6`: Определяет максимальное количество ошибок, которое может совершить игрок.
    
3.  **Список слов `WORDS`:**
    -   `WORDS = ["python", "java", "kotlin", "javascript", "swift", "ruby", "csharp"]`: Список, содержащий слова, из которых компьютер выбирает слово для игры.
    - TODO: Заменить на загрузку из файла.

4. **Функция `draw_hangman(errors)`:**
    -   Отображает состояние виселицы в зависимости от количества ошибок, используя ASCII-арт.
    -   `hangman_stages` - массив строк, представляющих стадии виселицы.
    -   `print(hangman_stages[errors])` - выводит на экран соответсвующую строку.
    -   Обработка `IndexError` для логирования ошибки, если `errors` выходит за пределы списка.
  
5. **Функция `choose_word()`:**
   - Случайно выбирает слово из списка `WORDS` и возвращает его в верхнем регистре.

6.  **Функция `create_guess_string(word)`:**
    -   Создает строку из прочерков, длина которой соответствует длине загаданного слова.

7.  **Функция `update_guess_string(guess_string, target_word, user_letter)`:**
    -   Обновляет строку `guess_string`, показывая угаданные буквы на их местах.
  
8.  **Функция `check_win(guess_string, target_word)`:**
    -  Проверяет, угадано ли слово.

9.  **Функция `play_hangman()`:**
    -   **Выбор слова:**
        -   `target_word = choose_word()`: Случайно выбирает слово, используя функцию `choose_word`.
    -   **Создание строки для отгадывания:**
        -   `guess_string = create_guess_string(target_word)`: Создает строку из прочерков.
    -   **Инициализация счетчика ошибок:**
        -   `number_of_errors = 0`: Устанавливает начальное количество ошибок в 0.
    -   **Основной цикл игры `while number_of_errors < MAX_ERRORS and "_" in guess_string:`**
        -   Цикл продолжается, пока количество ошибок меньше `MAX_ERRORS` и в строке `guess_string` есть прочерки (т.е. пока слово не угадано и не исчерпан лимит ошибок).
        -   `print("Слово:", guess_string)`: Выводит текущее состояние слова с угаданными буквами и прочерками.
        -   `user_letter = input("Введите букву: ").upper()`: Запрашивает у пользователя ввод буквы и переводит ее в верхний регистр.
        -  Обработка возможных ошибок ввода с помощью `try-except`.
        -   **Проверка наличия буквы в слове:**
            -   `if user_letter in target_word:`: Проверяет, есть ли введенная буква в загаданном слове.
            -   Если буква есть:
                -   `guess_string = update_guess_string(guess_string, target_word, user_letter)`: Обновляет `guess_string` с помощью функции `update_guess_string`.
                -  `if check_win(guess_string, target_word):`: Проверяет, угадано ли слово с помощью функции `check_win`.
                -   `print("ПОЗДРАВЛЯЮ! Вы угадали слово:", target_word)`: Выводит поздравление и загаданное слово.
                -   `return`: Завершает функцию (игру).
            -   **Если буквы нет в слове:**
                -   `number_of_errors += 1`: Увеличивает счетчик ошибок на 1.
                -   `draw_hangman(number_of_errors)`: Вызывает функцию `draw_hangman` для отображения виселицы.
    -   **Проверка на проигрыш:**
        -   `if number_of_errors == MAX_ERRORS:`: Проверяет, равно ли количество ошибок `MAX_ERRORS`.
        -   `print("СОЖАЛЕЮ, вы не отгадали слово. Загаданное слово:", target_word)`: Выводит сообщение о проигрыше и загаданное слово.

10. **Запуск игры:**
    -   `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_hangman()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    -   `play_hangman()`: Вызывает функцию для начала игры.
"""
```