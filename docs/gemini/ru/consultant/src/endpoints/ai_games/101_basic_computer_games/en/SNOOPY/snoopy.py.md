# Анализ кода модуля `snoopy.py`

**Качество кода**
10
- Плюсы
    - Код хорошо структурирован и логически разделен на функции.
    - Присутствует подробная документация, объясняющая логику игры и алгоритм.
    - Используются понятные имена переменных и функций.
    - Код написан в соответствии с PEP 8.
    - Игра реализована в соответствии с описанными правилами и блок-схемой.
    - Имеется описание алгоритма, блок-схемы и легенда к ней.
    - Код прост для понимания и легко читается.
- Минусы
    - Отсутствует обработка ошибок и логирование.
    - Нет обработки ввода пользователя, не являющегося буквой.

**Рекомендации по улучшению**

1.  **Добавить логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок и действий пользователя.
2.  **Обработка ошибок:**  Добавить обработку исключений для пользовательского ввода (например, если введено не буквенное значение)
3.  **Комментарии в формате reStructuredText (RST)**: Описать все функции, классы и переменные в формате RST.
4.  **Унификация**: Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль игры "Снупи"
====================

Игра "Снупи" - это игра в угадывание слова, в которой компьютер выбирает
случайное слово из списка, а игрок пытается его отгадать, вводя по одной
букве за раз. После каждой попытки компьютер показывает, какие буквы
угаданы правильно и где они находятся в слове.

Правила игры:
1. Компьютер выбирает случайное слово из списка.
2. Игрок вводит одну букву.
3. Компьютер сравнивает введенную букву со словом, и если она есть, то
   показывает ее позицию.
4. Игра продолжается до тех пор, пока игрок не угадает все буквы слова.
5. Если игрок угадывает слово, игра заканчивается, и выводится сообщение
   о победе.

Алгоритм:
1. Установить список слов для выбора.
2. Выбрать случайное слово из списка.
3. Создать маску для слова (например, "----", если слово "SNOOPY")
4. Установить счетчик попыток в 0.
5. Начать цикл "пока слово не угадано":
    5.1. Вывести текущее состояние маски.
    5.2. Увеличить счетчик попыток.
    5.3. Запросить у игрока ввод буквы.
    5.4. Если введенная буква есть в слове, то:
        5.4.1. Обновить маску, показав позицию буквы.
    5.5. Если маска не содержит символов "-", то перейти к шагу 6.
6. Вывести сообщение "YOU GOT IT IN {число попыток} GUESSES!" и
   загаданное слово
7. Конец игры.

Блок-схема:

.. mermaid::
    flowchart TD
        Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:\n    <code><b>\n    wordList = ['SNOOPY', 'PEANUTS', 'CHARLIE']\n    targetWord = random_word(wordList)\n    wordMask = create_mask(targetWord)\n    numberOfGuesses = 0\n    </b></code></p>"]
        InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
        LoopStart --> OutputMask["Вывод маски слова: <code><b>wordMask</b></code>"]
        OutputMask --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
        IncreaseGuesses --> InputLetter["Ввод буквы пользователем: <code><b>userLetter</b></code>"]
        InputLetter --> CheckLetter{"Проверка: <code><b>userLetter in targetWord?</b></code>"}
        CheckLetter -- Да --> UpdateMask["<code><b>Обновить wordMask</b></code>"]
        UpdateMask --> CheckWin{"Проверка: <code><b>'-' in wordMask?</b></code>"}
        CheckWin -- Да --> LoopStart
        CheckWin -- Нет --> OutputWin["Вывод сообщения: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES! The word was <code>{targetWord}</code></b>"]
        OutputWin --> End["Конец"]
        CheckLetter -- Нет --> LoopStart

Легенда:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: wordList (список слов),
    targetWord (загаданное слово выбирается случайно), wordMask (маска слова,
    изначально заполненная дефисами), numberOfGuesses (количество попыток)
    устанавливается в 0.
    LoopStart - Начало цикла, который продолжается, пока слово не угадано.
    OutputMask - Вывод на экран текущего состояния маски слова (например,
    "S---P-").
    IncreaseGuesses - Увеличение счетчика количества попыток на 1.
    InputLetter - Запрос у пользователя ввода буквы.
    CheckLetter - Проверка, есть ли введенная буква в загаданном слове.
    UpdateMask - Обновление маски слова, заменяя дефисы на угаданные буквы.
    CheckWin - Проверка, остались ли в маске слова дефисы (-).
    OutputWin - Вывод сообщения о победе, если все буквы угаданы, с
    указанием количества попыток и загаданного слова.
    End - Конец программы.
"""
import random
from src.logger.logger import logger  # Подключаем модуль логгера

#: Список слов для игры
WORD_LIST = ["SNOOPY", "PEANUTS", "CHARLIE"]


def choose_word(word_list: list[str]) -> str:
    """Выбирает случайное слово из списка.

    :param word_list: Список слов.
    :return: Случайное слово из списка.
    """
    try:
        # Код выбирает случайное слово из списка
        return random.choice(word_list)
    except Exception as e:
        #  Логируем ошибку, если возникает исключение
        logger.error('Ошибка выбора случайного слова', exc_info=e)
        return ''


def create_mask(word: str) -> list[str]:
    """Создает маску слова, заменяя буквы на дефисы.

    :param word: Слово, для которого создается маска.
    :return: Список дефисов, длина которого равна длине слова.
    """
    # Код создает маску слова, заменяя буквы на дефисы
    return ["-" for _ in word]


def update_mask(mask: list[str], word: str, letter: str) -> list[str]:
    """Обновляет маску слова, показывая угаданные буквы.

    :param mask: Текущая маска слова.
    :param word: Исходное слово.
    :param letter: Буква, которую нужно проверить и обновить в маске.
    :return: Обновленная маска слова.
    """
    # Код обновляет маску, показывая угаданные буквы
    for i, char in enumerate(word):
        if char == letter:
            mask[i] = letter
    return mask


def play_snoopy_game():
    """Запускает игру "Снупи"."""
    # Выбираем случайное слово из списка
    target_word = choose_word(WORD_LIST).upper()
    if not target_word:
        return # Завершаем игру если слово не выбрано
    # Создаем маску для слова
    word_mask = create_mask(target_word)
    # Инициализация счетчика попыток
    number_of_guesses = 0

    # Основной цикл игры
    while True:
        # Вывод текущей маски слова
        print(" ".join(word_mask))
        # Увеличиваем счетчик попыток
        number_of_guesses += 1
        # Запрос ввода буквы у пользователя
        while True:
            try:
                user_letter = input("Введите букву: ").upper()
                if not user_letter.isalpha() or len(user_letter) != 1:
                    # Логируем ошибку, если введено не буквенное значение или больше одного символа
                    logger.error(f"Некорректный ввод пользователя: {user_letter}. Введите одну букву.")
                    print("Пожалуйста, введите одну букву.")
                    continue
                break  # Выходим из цикла если ввод корректный
            except Exception as e:
                # Логируем ошибку, если возникает исключение
                logger.error('Ошибка ввода буквы', exc_info=e)
                continue
        # Проверяем наличие введенной буквы в слове
        if user_letter in target_word:
            # Обновляем маску слова
            word_mask = update_mask(word_mask, target_word, user_letter)
        # Проверяем, угадано ли слово
        if "-" not in word_mask:
            print(
                f"ПОЗДРАВЛЯЮ! Вы угадали слово за {number_of_guesses} попыток! Слово было: {target_word}"
            )
            break


# Запускаем игру
if __name__ == "__main__":
    # Код вызывает функцию для запуска игры
    play_snoopy_game()

"""
Объяснение кода:
1.  **Импорт модуля `random`**:\n
   -  `import random`: Импортирует модуль `random`, который используется
     для генерации случайного слова из списка.\n
    -   `from src.logger.logger import logger`: импортирует модуль логгера.

2.  **Объявление константы `WORD_LIST`**:\n
   -   `WORD_LIST = ["SNOOPY", "PEANUTS", "CHARLIE"]`: Список слов, из
    которых будет выбираться загаданное слово.
3.  **Функция `choose_word(word_list)`**:\n
    -   `def choose_word(word_list: list[str]) -> str:`: Определяет функцию,
        которая принимает список слов `word_list`.\n
    -   `return random.choice(word_list)`: Возвращает случайное слово из
        переданного списка, используя метод `random.choice()`.\n
    -   `try except`: Блок try except обрабатывает возможные ошибки при выборе слова.
    -    `logger.error('Ошибка выбора случайного слова', exc_info=e)`: Логирует ошибку, если возникает исключение.

4.  **Функция `create_mask(word)`**:\n
    -   `def create_mask(word: str) -> list[str]:`: Определяет функцию,
        которая принимает слово `word`.\n
    -   `return ["-" for _ in word]`: Возвращает список, где количество
        дефисов равно длине слова, создавая маску.\n

5.  **Функция `update_mask(mask, word, letter)`**:\n
    -   `def update_mask(mask: list[str], word: str, letter: str) -> list[str]:`:
        Определяет функцию, которая принимает маску слова `mask`, исходное
        слово `word` и введенную букву `letter`.\n
    -   `for i, char in enumerate(word):`: Итерирует по символам слова с
        их индексами, используя функцию `enumerate`.\n
    -   `if char == letter:`: Проверяет, равен ли текущий символ слова
        введенной букве.\n
    -   `mask[i] = letter`: Если символ равен введенной букве, то обновляет
        маску, заменяя дефис на букву.\n
    -   `return mask`: Возвращает обновленную маску.\n

6.  **Функция `play_snoopy_game()`**:\n
    -   `def play_snoopy_game():`: Определяет функцию, которая содержит
        логику игры "Снупи".\n
    -   `target_word = choose_word(WORD_LIST).upper()`: Выбирает случайное
        слово из списка и преобразует его в верхний регистр.\n
    -   `if not target_word: return`: Проверка на пустое слово.
    -   `word_mask = create_mask(target_word)`: Создает маску для выбранного
        слова, используя функцию `create_mask()`.\n
    -   `number_of_guesses = 0`: Инициализирует счетчик попыток.\n
    -   `while True:`: Запускает бесконечный цикл, который продолжается,
        пока игрок не угадает слово.\n
    -   `print(" ".join(word_mask))`: Выводит текущее состояние маски слова
        на экран. `join` преобразует список букв в строку, разделенную
        пробелами.\n
    -   `number_of_guesses += 1`: Увеличивает счетчик попыток на 1.\n
    -   `while True:`: Запускается бесконечный цикл для обработки ввода
    -    `try except`: Блок try except обрабатывает ошибки ввода
    -   `user_letter = input("Введите букву: ").upper()`: Запрашивает ввод
        буквы у пользователя и преобразует ее в верхний регистр.\n
    -   `if not user_letter.isalpha() or len(user_letter) != 1`: проверяет на корректность ввода.
    -   `logger.error(f"Некорректный ввод пользователя: {user_letter}. Введите одну букву.")`: Логирует ошибку если ввод некорректен
    -   `if user_letter in target_word:`: Проверяет, есть ли введенная
        буква в загаданном слове.\n
    -   `word_mask = update_mask(word_mask, target_word, user_letter)`:
        Обновляет маску, показывая угаданную букву на ее позиции, используя
        функцию `update_mask()`.\n
    -   `if "-" not in word_mask:`: Проверяет, есть ли в маске еще не
        угаданные буквы, представленные дефисами.\n
    -   `print(f"ПОЗДРАВЛЯЮ! Вы угадали слово за {number_of_guesses} попыток!
        Слово было: {target_word}")`: Выводит сообщение о победе с
        количеством попыток и загаданным словом.\n
    -   `break`: Выход из цикла.\n

7.  **Запуск игры**:\n
   -   `if __name__ == "__main__":`: Этот блок гарантирует, что функция
        `play_snoopy_game()` будет запущена, только если файл исполняется
        напрямую, а не импортируется как модуль.\n
   -   `play_snoopy_game()`: Вызывает функцию для начала игры.\n
"""
```