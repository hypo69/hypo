"""
HEX:
=================
Сложность: 5
-----------------
Игра "HEX" - это игра-головоломка, в которой игрок должен угадать шестизначное шестнадцатеричное число. Компьютер генерирует случайное шестизначное шестнадцатеричное число, а игрок пытается его угадать, вводя свои варианты. 
После каждой попытки компьютер сообщает, сколько цифр в предложенном числе совпадают с загаданным числом и находятся на правильной позиции, а также сколько цифр совпадают, но находятся в неправильной позиции. 
Игра продолжается до тех пор, пока игрок не угадает число.
Правила игры:
1.  Компьютер генерирует случайное шестизначное шестнадцатеричное число.
2.  Игрок вводит шестизначное шестнадцатеричное число.
3.  После каждой попытки компьютер сообщает:
    -   Сколько цифр угадано и находятся на правильной позиции.
    -   Сколько цифр угадано, но находятся в неправильной позиции.
4.  Игра продолжается, пока игрок не угадает число полностью.
-----------------
Алгоритм:
1. Сгенерировать случайное шестизначное шестнадцатеричное число (targetNumber).
2. Начать цикл, пока игрок не угадает число:
   2.1 Запросить у игрока шестизначное шестнадцатеричное число (userGuess).
   2.2 Инициализировать переменные correctPosition и incorrectPosition значением 0.
   2.3 Пройтись по каждой цифре числа userGuess и targetNumber, сравнивая их:
      2.3.1 Если цифры совпадают и находятся на той же позиции, то увеличить correctPosition на 1.
      2.3.2 Иначе, если цифра из userGuess присутствует в targetNumber, то увеличить incorrectPosition на 1.
   2.4 Вывести количество цифр на правильной позиции (correctPosition) и количество цифр на неправильной позиции (incorrectPosition).
   2.5 Если correctPosition равно 6, вывести сообщение о победе и завершить игру.
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> GenerateTargetNumber["Генерация случайного 6-значного шестнадцатеричного числа: <code><b>targetNumber</b></code>"]
    GenerateTargetNumber --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> InputGuess["Ввод 6-значного шестнадцатеричного числа: <code><b>userGuess</b></code>"]
    InputGuess --> InitializeCounters["Инициализация: <code><b>correctPosition = 0, incorrectPosition = 0</b></code>"]
    InitializeCounters --> CheckDigitsLoopStart{"Начало цикла: по каждой цифре"}
    CheckDigitsLoopStart --> CheckPosition["Проверка: <code><b>userGuess[i] == targetNumber[i]?</b></code>"]
    CheckPosition -- Да --> IncreaseCorrectPosition["<code><b>correctPosition = correctPosition + 1</b></code>"]
    IncreaseCorrectPosition --> CheckDigitsLoopEnd{"Конец цикла по каждой цифре"}
    CheckPosition -- Нет --> CheckIncorrectPosition["Проверка: <code><b>userGuess[i] in targetNumber?</b></code>"]
    CheckIncorrectPosition -- Да --> IncreaseIncorrectPosition["<code><b>incorrectPosition = incorrectPosition + 1</b></code>"]
    IncreaseIncorrectPosition --> CheckDigitsLoopEnd
    CheckIncorrectPosition -- Нет --> CheckDigitsLoopEnd
    CheckDigitsLoopEnd --> CheckAllDigits{"Проверены все цифры?"}
    CheckAllDigits -- Нет --> CheckDigitsLoopStart
    CheckAllDigits -- Да --> OutputFeedback["Вывод: <b>Правильно на позиции: <code>{correctPosition}</code>, Правильно, но не на позиции: <code>{incorrectPosition}</code></b>"]
    OutputFeedback --> CheckWinCondition["Проверка: <code><b>correctPosition == 6?</b></code>"]
    CheckWinCondition -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    CheckWinCondition -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
Legenda:
    Start - Начало программы.
    GenerateTargetNumber - Генерация случайного 6-значного шестнадцатеричного числа и сохранение в переменной targetNumber.
    LoopStart - Начало цикла, который продолжается, пока игрок не угадает число.
    InputGuess - Запрос у пользователя ввода 6-значного шестнадцатеричного числа и сохранение его в переменной userGuess.
    InitializeCounters - Инициализация счетчиков correctPosition и incorrectPosition в 0.
     CheckDigitsLoopStart - Начало цикла для проверки каждой цифры в введенном числе.
    CheckPosition - Проверка, находится ли цифра из userGuess на правильной позиции в targetNumber.
    IncreaseCorrectPosition - Увеличение счетчика correctPosition на 1, если цифра и позиция совпадают.
    CheckDigitsLoopEnd - Конец цикла по каждой цифре.
    CheckIncorrectPosition - Проверка, присутствует ли цифра из userGuess в targetNumber, но на другой позиции.
    IncreaseIncorrectPosition - Увеличение счетчика incorrectPosition на 1, если цифра присутствует, но на неправильной позиции.
    CheckAllDigits - Проверка, все ли цифры были проверены.
    OutputFeedback - Вывод количества правильно угаданных цифр на правильных позициях и количества правильно угаданных цифр на неправильных позициях.
    CheckWinCondition - Проверка, угадано ли число (correctPosition == 6).
    OutputWin - Вывод сообщения о победе, если число угадано.
    End - Конец программы.
"""
import random

def generate_hex_number():
    """Генерирует случайное шестизначное шестнадцатеричное число."""
    return ''.join(random.choice('0123456789abcdef') for _ in range(6))


def get_feedback(target, guess):
    """Сравнивает введенное число с загаданным и выдает обратную связь."""
    correct_position = 0 # Счетчик цифр на правильной позиции
    incorrect_position = 0 # Счетчик цифр на неправильной позиции
    
    for i in range(len(guess)):
        if guess[i] == target[i]:
            correct_position += 1 # Если цифра на правильной позиции - увеличиваем счетчик
        elif guess[i] in target:
            incorrect_position += 1 # Если цифра есть в загаданном числе, но не на той позиции - увеличиваем счетчик
    return correct_position, incorrect_position


def play_hex_game():
    """Основная функция игры."""
    target_number = generate_hex_number() # Генерируем загаданное число
    print("Добро пожаловать в игру HEX!")

    while True: # Запускаем бесконечный цикл, который будет работать пока игрок не угадает число
        user_guess = input("Введите шестизначное шестнадцатеричное число: ").lower() # Запрашиваем ввод пользователя и приводим к нижнему регистру
        
        # Проверяем, что ввод пользователя корректен
        if not all(c in '0123456789abcdef' for c in user_guess) or len(user_guess) != 6:
            print("Некорректный ввод. Пожалуйста, введите 6-значное шестнадцатеричное число.")
            continue  # Если ввод не корректен - переходим на начало цикла
        
        correct_pos, incorrect_pos = get_feedback(target_number, user_guess) # Получаем обратную связь
        print(f"Правильно на позиции: {correct_pos}, Правильно, но не на позиции: {incorrect_pos}")
        
        if correct_pos == 6: # Если все цифры угаданы на правильной позиции - поздравляем пользователя и выходим из цикла
            print("ПОЗДРАВЛЯЮ! Вы угадали число!")
            break

if __name__ == "__main__":
    play_hex_game()
"""
Пояснения:
1. **Импорт модуля `random`**:
   - `import random`: Импортирует модуль `random`, который используется для генерации случайного числа.

2. **Функция `generate_hex_number()`**:
   - `def generate_hex_number():`: Определяет функцию для генерации случайного шестизначного шестнадцатеричного числа.
   - `return ''.join(random.choice('0123456789abcdef') for _ in range(6))`: Использует генератор списков для создания шести случайных шестнадцатеричных символов и объединяет их в строку.

3. **Функция `get_feedback(target, guess)`**:
   - `def get_feedback(target, guess):`: Определяет функцию, которая сравнивает введенное число с загаданным и выдает обратную связь.
   - `correct_position = 0`: Инициализирует счетчик `correct_position` для отслеживания количества правильно угаданных цифр на правильных позициях.
   - `incorrect_position = 0`: Инициализирует счетчик `incorrect_position` для отслеживания количества правильно угаданных цифр, но на неправильных позициях.
   - `for i in range(len(guess)):`: Запускает цикл для прохода по каждой цифре в введенном числе.
   - `if guess[i] == target[i]:`: Проверяет, совпадает ли цифра на i-ой позиции в `guess` с цифрой на i-ой позиции в `target`.
     - `correct_position += 1`: Если цифры совпадают и находятся на той же позиции, то увеличивает `correct_position` на 1.
   - `elif guess[i] in target:`: Проверяет, есть ли цифра из `guess` в `target`, но не на той же позиции.
     - `incorrect_position += 1`: Если цифра есть в `target`, но не на той же позиции, то увеличивает `incorrect_position` на 1.
   - `return correct_position, incorrect_position`: Возвращает количество цифр на правильной позиции и количество цифр на неправильной позиции.

4. **Функция `play_hex_game()`**:
   - `def play_hex_game():`: Определяет основную функцию игры.
   - `target_number = generate_hex_number()`: Генерирует случайное шестизначное шестнадцатеричное число, используя `generate_hex_number()`.
   - `print("Добро пожаловать в игру HEX!")`: Выводит приветствие в начале игры.
   - `while True:`: Запускает бесконечный цикл, который продолжается до тех пор, пока игрок не угадает число.
   - `user_guess = input("Введите шестизначное шестнадцатеричное число: ").lower()`: Запрашивает ввод пользователя, приводит его к нижнему регистру для удобства сравнения и сохраняет в `user_guess`.
   - `if not all(c in '0123456789abcdef' for c in user_guess) or len(user_guess) != 6:`: Проверяет, является ли ввод пользователя корректным, то есть состоит ли из 6 шестнадцатеричных символов.
     - `print("Некорректный ввод. Пожалуйста, введите 6-значное шестнадцатеричное число.")`: Выводит сообщение об ошибке, если ввод некорректен.
     - `continue`: Если ввод некорректен, то переходит к следующей итерации цикла.
   - `correct_pos, incorrect_pos = get_feedback(target_number, user_guess)`: Вызывает функцию `get_feedback()` для получения обратной связи.
   - `print(f"Правильно на позиции: {correct_pos}, Правильно, но не на позиции: {incorrect_pos}")`: Выводит обратную связь для пользователя.
   - `if correct_pos == 6:`: Проверяет, угадал ли игрок число полностью.
     - `print("ПОЗДРАВЛЯЮ! Вы угадали число!")`: Выводит сообщение о победе.
     - `break`: Выходит из цикла, завершая игру.

5. **Запуск игры**:
   - `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_hex_game()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
   - `play_hex_game()`: Вызывает функцию для начала игры.
"""
