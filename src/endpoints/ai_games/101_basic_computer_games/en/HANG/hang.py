"""
<HANG>:
=================
Сложность: 7
-----------------
Игра "Виселица" - это игра в слова, где один игрок (или компьютер) загадывает слово, а другой игрок пытается его отгадать по буквам.
За каждую неправильную букву игрок получает штраф, обычно в виде части рисунка виселицы. Если рисунок завершен, игрок проигрывает.

Правила игры:
1. Компьютер выбирает случайное слово из заранее определенного списка.
2. Игрок видит слово, представленное прочерками (по одной на каждую букву).
3. Игрок пытается отгадать слово, вводя буквы.
4. Если введенная буква есть в слове, она отображается на своих местах.
5. Если введенной буквы нет в слове, игрок получает штраф.
6. Игра продолжается до тех пор, пока игрок не угадает слово или не исчерпает лимит штрафов.
-----------------
Алгоритм:
1.  Инициализировать массив слов, которые может загадать компьютер.
2.  Выбрать случайное слово из массива.
3.  Создать строку `GUESS$` , состоящую из прочерков, по длине загаданного слова.
4.  Инициализировать число ошибок, равное 0.
5.  Начать цикл "пока слово не отгадано и количество ошибок меньше 6":
  5.1 Запросить ввод буквы от игрока.
  5.2 Если введенная буква есть в загаданном слове:
    5.2.1 Обновить строку `GUESS$` , показав букву на всех ее позициях в слове.
    5.2.2 Если все буквы отгаданы, перейти к шагу 6.
  5.3 Иначе:
    5.3.1 Увеличить число ошибок на 1.
    5.3.2 Показать изображение виселицы, соответствующее текущему количеству ошибок.
  5.4 Если число ошибок равно 6, перейти к шагу 7.
6. Вывести сообщение "YOU GOT IT!", затем загаданное слово, и перейти к шагу 8.
7. Вывести сообщение "SORRY, YOU DIDN'T GET IT.", затем загаданное слово, и перейти к шагу 8.
8. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeWords["<p align='left'>Инициализация:
    <code><b>
    words = ['слово1', 'слово2', ...]
    </b></code></p>"]
    InitializeWords --> ChooseWord["<p align='left'>Выбор случайного слова:
    <code><b>
    targetWord = random(words)
    </b></code></p>"]
    ChooseWord --> CreateGuessString["<p align='left'>Создание строки GUESS$:
    <code><b>
    guessString = '______'
    </b></code></p>"]
    CreateGuessString --> InitializeErrors["<p align='left'>Инициализация счетчика ошибок:
    <code><b>
    numberOfErrors = 0
    </b></code></p>"]
    InitializeErrors --> LoopStart{"Начало цикла: пока слово не угадано и ошибок < 6"}
    LoopStart -- Да --> InputLetter["Ввод буквы пользователем: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"Проверка: <code><b>userLetter in targetWord?</b></code>"}
    CheckLetter -- Да --> UpdateGuessString["<p align='left'>Обновление GUESS$:
    <code><b>
    guessString = replace(guessString, userLetter)
    </b></code></p>"]
    UpdateGuessString --> CheckWin{"Проверка: <code><b>guessString == targetWord?</b></code>"}
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b> и <b>targetWord</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    CheckLetter -- Нет --> IncreaseErrors["<code><b>numberOfErrors = numberOfErrors + 1</b></code>"]
    IncreaseErrors --> DrawHangman["Вывод виселицы: <code><b>drawHangman(numberOfErrors)</b></code>"]
    DrawHangman --> CheckLose{"Проверка: <code><b>numberOfErrors == 6?</b></code>"}
    CheckLose -- Да --> OutputLose["Вывод сообщения: <b>SORRY, YOU DIDN'T GET IT.</b> и <b>targetWord</b>"]
    OutputLose --> End
    CheckLose -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
Legenda:
  Start - Начало игры.
  InitializeWords - Инициализация списка слов для выбора.
  ChooseWord - Выбор случайного слова из списка.
  CreateGuessString - Создание строки `guessString` из прочерков, соответствующей длине загаданного слова.
  InitializeErrors - Инициализация счетчика ошибок `numberOfErrors` в 0.
  LoopStart - Начало цикла, который продолжается, пока слово не угадано и количество ошибок меньше 6.
  InputLetter - Запрос у пользователя ввода буквы и сохранение ее в `userLetter`.
  CheckLetter - Проверка, есть ли введенная буква `userLetter` в загаданном слове `targetWord`.
  UpdateGuessString - Обновление строки `guessString`, показывая введенную букву на ее местах.
  CheckWin - Проверка, угадано ли слово (т.е. `guessString` равен `targetWord`).
  OutputWin - Вывод сообщения о победе "YOU GOT IT!" и загаданного слова.
  End - Конец игры.
  IncreaseErrors - Увеличение счетчика ошибок `numberOfErrors` на 1.
  DrawHangman - Отображение текущего состояния виселицы в зависимости от количества ошибок.
  CheckLose - Проверка, достигло ли количество ошибок `numberOfErrors` значения 6.
  OutputLose - Вывод сообщения о проигрыше "SORRY, YOU DIDN'T GET IT." и загаданного слова.
"""
import random

# Список слов для игры
WORDS = ["python", "java", "kotlin", "javascript", "swift", "ruby", "csharp"]

def draw_hangman(errors):
    """
    Функция для отображения виселицы в зависимости от количества ошибок.
    
    Args:
      errors: Количество ошибок, совершенных игроком.
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
    print(hangman_stages[errors])

def play_hangman():
    """Основная функция игры в виселицу"""
    # Выбираем случайное слово из списка
    target_word = random.choice(WORDS).upper()
    # Создаем строку из прочерков, соответствующую длине слова
    guess_string = "_" * len(target_word)
    # Инициализируем счетчик ошибок
    number_of_errors = 0
    
    # Основной игровой цикл
    while number_of_errors < 6 and "_" in guess_string:
        print("Слово:", guess_string)
        # Запрашиваем у пользователя ввод буквы
        user_letter = input("Введите букву: ").upper()
        
        # Проверяем, есть ли буква в слове
        if user_letter in target_word:
            # Обновляем guess_string, показывая букву на ее местах
            new_guess_string = ""
            for i in range(len(target_word)):
                if target_word[i] == user_letter:
                    new_guess_string += user_letter
                else:
                    new_guess_string += guess_string[i]
            guess_string = new_guess_string
            
            # Проверяем, угадано ли слово
            if guess_string == target_word:
                print("ПОЗДРАВЛЯЮ! Вы угадали слово:", target_word)
                return  # Завершаем игру
            
        else:
            # Увеличиваем число ошибок и рисуем виселицу
            number_of_errors += 1
            draw_hangman(number_of_errors)
    
    # Проверка на проигрыш
    if number_of_errors == 6:
        print("СОЖАЛЕЮ, вы не отгадали слово. Загаданное слово:", target_word)
    
if __name__ == "__main__":
    play_hangman()
"""
Объяснение кода:

1.  **Импорт модуля `random`:**
    -   `import random`: Импортирует модуль random для случайного выбора слова.

2.  **Список слов `WORDS`:**
    -   `WORDS = ["python", "java", "kotlin", "javascript", "swift", "ruby", "csharp"]`: Список, содержащий слова, из которых компьютер выбирает слово для игры.
    
3. **Функция `draw_hangman(errors)`:**
    -   Отображает состояние виселицы в зависимости от количества ошибок, используя ASCII-арт.
    -  `hangman_stages` - массив строк, представляющих стадии виселицы.
    -  `print(hangman_stages[errors])` - выводит на экран соответсвующую строку.

4.  **Функция `play_hangman()`:**
    -   **Выбор слова:**
        -  `target_word = random.choice(WORDS).upper()`: Случайно выбирает слово из списка `WORDS` и переводит его в верхний регистр.
    -   **Создание строки для отгадывания:**
        -   `guess_string = "_" * len(target_word)`: Создает строку, состоящую из прочерков, длина которой соответствует длине загаданного слова.
    -   **Инициализация счетчика ошибок:**
        -   `number_of_errors = 0`: Устанавливает начальное количество ошибок в 0.
    -   **Основной цикл игры `while number_of_errors < 6 and "_" in guess_string:`**:
        -   Цикл продолжается, пока количество ошибок меньше 6 и в строке `guess_string` есть прочерки (т.е. пока слово не угадано и не исчерпан лимит ошибок).
        -   `print("Слово:", guess_string)`: Выводит текущее состояние слова с угаданными буквами и прочерками.
        -   `user_letter = input("Введите букву: ").upper()`: Запрашивает у пользователя ввод буквы и переводит ее в верхний регистр.
        -   **Проверка наличия буквы в слове:**
            -   `if user_letter in target_word:`: Проверяет, есть ли введенная буква в загаданном слове.
            -   Если буква есть:
                -  `new_guess_string = ""`: Создает пустую строку `new_guess_string` для сборки нового варианта отгадываемого слова.
                -  Цикл `for i in range(len(target_word))` перебирает все символы в загаданном слове.
                -  Если текущая буква в загаданном слове совпадает с введенной буквой `user_letter`, то добавляет ее в `new_guess_string`, иначе, добавляет символ с текущей позиции из `guess_string`.
                - `guess_string = new_guess_string`: Обновляет `guess_string` новым вариантом с угаданными буквами.
                -  `if guess_string == target_word:`: Проверяет, угадано ли слово.
                -  `print("ПОЗДРАВЛЯЮ! Вы угадали слово:", target_word)`: Выводит поздравление и загаданное слово.
                -  `return`: Завершает функцию (игру).
            -   **Если буквы нет в слове:**
                -   `number_of_errors += 1`: Увеличивает счетчик ошибок на 1.
                -   `draw_hangman(number_of_errors)`: Вызывает функцию `draw_hangman` для отображения виселицы.
    -   **Проверка на проигрыш:**
        -   `if number_of_errors == 6:`: Проверяет, равно ли количество ошибок 6.
        -   `print("СОЖАЛЕЮ, вы не отгадали слово. Загаданное слово:", target_word)`: Выводит сообщение о проигрыше и загаданное слово.

5. **Запуск игры:**
    -  `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_hangman()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    -  `play_hangman()`: Вызывает функцию для начала игры.
"""
