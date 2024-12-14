"""
LIT QZ:
=================
Сложность: 2
-----------------
Игра "LIT QZ" - это простая викторина, где пользователю предлагается угадать букву, загаданную компьютером. Компьютер генерирует случайную букву алфавита, а игрок пытается ее отгадать, вводя свои предположения. После каждого предположения игроку сообщается, является ли загаданная буква больше или меньше введенной.

Правила игры:
1. Компьютер случайно выбирает букву из алфавита.
2. Игрок вводит букву в качестве предположения.
3. Компьютер сравнивает введенную букву с загаданной и сообщает, была ли загаданная буква больше, меньше или равна введенной.
4. Если буквы равны, игра завершается и игрок побеждает.
5. Иначе, игра продолжается с шага 2.

-----------------
Алгоритм:
1. Инициализация: Задать начальное значение переменной случайного числа `randomNumber`, переменной счетчика попыток `numberOfGuesses`  в 0
2. Сгенерировать случайное число `randomNumber` в диапазоне от 1 до 26.
3. Перевести полученное число  `randomNumber` в соответствующую букву  `secretLetter`, где 1 = "A", 2 = "B" ... 26 = "Z".
4. Увеличить счетчик попыток `numberOfGuesses` на 1.
5. Вывести сообщение "WHAT LETTER AM I THINKING OF?".
6. Получить ввод от пользователя `guessLetter`.
7. Сравнить `guessLetter` с загаданной буквой `secretLetter`.
8. Если `guessLetter` больше чем `secretLetter`, то вывести "TOO HIGH, TRY A LOWER LETTER".
9. Если `guessLetter` меньше чем `secretLetter`, то вывести "TOO LOW, TRY A HIGHER LETTER".
10. Если `guessLetter` равно `secretLetter`, то вывести "YOU GOT IT IN `numberOfGuesses` GUESSES!". и перейти к шагу 12
11. Вернуться к шагу 4.
12. Конец игры.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Start) --> Initialize(Initialize variables: numberOfGuesses = 0);
    Initialize --> GenerateRandomNumber(Generate random number 1-26 randomNumber);
    GenerateRandomNumber --> ConvertToLetter(Convert randomNumber to secretLetter);
    ConvertToLetter --> IncrementGuesses(Increment numberOfGuesses);
    IncrementGuesses --> Input(Output "WHAT LETTER AM I THINKING OF?"\n Input guessLetter);
    Input --> CompareLetters(Compare guessLetter with secretLetter);
    CompareLetters --> TooHigh{guessLetter > secretLetter?};
    TooHigh -- Yes --> OutputTooHigh(Output "TOO HIGH, TRY A LOWER LETTER");
    OutputTooHigh --> IncrementGuesses;
    TooHigh -- No --> TooLow{guessLetter < secretLetter?};
    TooLow -- Yes --> OutputTooLow(Output "TOO LOW, TRY A HIGHER LETTER");
    OutputTooLow --> IncrementGuesses;
    TooLow -- No --> CorrectGuess{guessLetter == secretLetter?};
    CorrectGuess -- Yes --> OutputCorrect(Output "YOU GOT IT IN numberOfGuesses GUESSES!");
    OutputCorrect --> End(End);
    CorrectGuess -- No --> IncrementGuesses;
```
"""
import random

# Начало игры
def play_lit_qz():
    """
    Функция, реализующая игру LIT QZ.
    """
    # Инициализация счетчика попыток
    number_of_guesses = 0 

    # Генерируем случайное число от 1 до 26
    random_number = random.randint(1, 26)
    
    # Преобразуем число в букву (1 = A, 2 = B, ..., 26 = Z)
    secret_letter = chr(random_number + 64)  # 65 - код 'A' в таблице ASCII

    # Основной цикл игры
    while True:
        number_of_guesses += 1  # Увеличиваем счетчик попыток
        print("WHAT LETTER AM I THINKING OF?")
        guess_letter = input().upper() # Получаем ввод пользователя и переводим в верхний регистр

        # Сравниваем введенную букву с загаданной
        if guess_letter > secret_letter:
            print("TOO HIGH, TRY A LOWER LETTER") # если буква больше
        elif guess_letter < secret_letter:
            print("TOO LOW, TRY A HIGHER LETTER") # если буква меньше
        else:
            print(f"YOU GOT IT IN {number_of_guesses} GUESSES!") # если буква угадана
            break # игра закончена
# Запуск игры
play_lit_qz()
"""
Пояснения:
1. `import random`: импортирует модуль random, необходимый для генерации случайных чисел.

2. `number_of_guesses = 0`:  инициализирует переменную `number_of_guesses` для отслеживания количества попыток пользователя.

3. `random_number = random.randint(1, 26)`: генерирует случайное целое число в диапазоне от 1 до 26 включительно и сохраняет его в переменной `random_number`.

4. `secret_letter = chr(random_number + 64)`: преобразует случайное число в соответствующую букву. 65 соответствует ASCII коду буквы 'A', поэтому мы прибавляем 64 к числу `random_number`, чтобы получить код нужной буквы. Функция `chr()` преобразует ASCII код в символ.

5. `while True:`: запускает бесконечный цикл, который будет продолжаться до тех пор, пока пользователь не угадает букву.

6. `number_of_guesses += 1`:  увеличивает счетчик попыток на 1 перед каждым новым предположением.

7. `print("WHAT LETTER AM I THINKING OF?")`: выводит сообщение с запросом на ввод буквы.

8. `guess_letter = input().upper()`: получает ввод от пользователя, переводит его в верхний регистр с помощью `.upper()` и сохраняет в `guess_letter`.

9. `if guess_letter > secret_letter: ... elif guess_letter < secret_letter: ... else:`: сравнивает введенную букву с загаданной и выводит подсказки пользователю.

10. `print(f"YOU GOT IT IN {number_of_guesses} GUESSES!")`: выводит сообщение о победе и количестве попыток, если пользователь угадал букву.

11. `break`:  выход из цикла, что завершает игру.

12. `play_lit_qz()`:  вызывает функцию, чтобы начать игру.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```