"""
MNOPLY:
=================
Сложность: 4
-----------------
Игра MNOPLY - это простая игра в угадывание числа. Компьютер выбирает случайное число от 1 до 100, а игрок пытается его угадать. После каждой попытки компьютер сообщает, больше или меньше загаданное число, чем введенное игроком.
Правила игры:
-----------------
1. Компьютер загадывает случайное целое число в диапазоне от 1 до 100.
2. Игрок вводит число в качестве предположения.
3. Компьютер сообщает, было ли предположение больше, меньше или равно загаданному числу.
4. Игра продолжается, пока игрок не угадает число.
5. После угадывания числа игра выводит сообщение о победе и количество попыток.
-----------------
Алгоритм:
1. Инициализировать счетчик попыток (attemptsCount) нулем.
2. Сгенерировать случайное целое число (randomNumber) в диапазоне от 1 до 100.
3. Начать цикл угадывания:
   a. Увеличить счетчик попыток на 1.
   b. Запросить у пользователя ввод числа (userGuess).
   c. Сравнить введенное число с загаданным числом:
      i. Если введенное число меньше загаданного, вывести сообщение "TOO LOW".
      ii. Если введенное число больше загаданного, вывести сообщение "TOO HIGH".
      iii. Если введенное число равно загаданному, вывести сообщение "YOU GOT IT IN [attemptsCount] TRIES" и закончить игру.
4. Вернуться к началу цикла угадывания.
-----------------
Блок-схема: 
```mermaid
graph TD
    Start(Start) --> InitializeAttemptsCount(Инициализация attemptsCount = 0);
    InitializeAttemptsCount --> GenerateRandomNumber(Сгенерировать randomNumber (1-100));
    GenerateRandomNumber --> GuessingLoopStart(Начало цикла угадывания);
    GuessingLoopStart --> IncrementAttemptsCount(Увеличить attemptsCount на 1);
    IncrementAttemptsCount --> InputUserGuess(Ввод userGuess);
    InputUserGuess --> CheckGuess(Сравнить userGuess с randomNumber);
    CheckGuess -- userGuess < randomNumber --> OutputTooLow(Вывести "TOO LOW");
    OutputTooLow --> GuessingLoopStart;
    CheckGuess -- userGuess > randomNumber --> OutputTooHigh(Вывести "TOO HIGH");
    OutputTooHigh --> GuessingLoopStart;
    CheckGuess -- userGuess == randomNumber --> OutputWin(Вывести "YOU GOT IT IN [attemptsCount] TRIES");
    OutputWin --> End(End);
```
"""
import random

def play_mnoply():
    """
    Запускает игру MNOPLY.
    """

    # Инициализация счетчика попыток
    attempts_count = 0

    # Генерация случайного числа от 1 до 100
    random_number = random.randint(1, 100)

    # Начало цикла угадывания
    while True:
        # Увеличиваем счетчик попыток на 1
        attempts_count += 1

        # Запрашиваем у пользователя ввод числа
        try:
            user_guess = int(input("Введите ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue # Если введено не число, пропускаем итерацию и повторяем запрос

        # Сравниваем введенное число с загаданным числом
        if user_guess < random_number:
            print("TOO LOW") # Выводим "Слишком мало"
        elif user_guess > random_number:
             print("TOO HIGH") # Выводим "Слишком много"
        else:
            # Если число угадано, выводим сообщение о победе и количестве попыток
            print(f"YOU GOT IT IN {attempts_count} TRIES")
            break # Завершаем цикл, так как число угадано

"""
Пояснения:
    `import random`: Импортирует модуль `random` для генерации случайных чисел.
    `play_mnoply()`: Функция, которая содержит основную логику игры.
    `attempts_count = 0`: Инициализирует счетчик попыток в ноль.
    `random_number = random.randint(1, 100)`: Генерирует случайное целое число в диапазоне от 1 до 100.
    `while True:`: Бесконечный цикл, который продолжается до тех пор, пока игрок не угадает число.
    `attempts_count += 1`: Увеличивает счетчик попыток на 1 при каждой новой попытке.
    `user_guess = int(input("Введите ваше предположение: "))`: Запрашивает у пользователя ввод числа и преобразует ввод в целое число.
    `if user_guess < random_number:`: Сравнивает предположение пользователя с загаданным числом.
    `print("TOO LOW")`: Выводит сообщение, если предположение пользователя меньше загаданного числа.
    `print("TOO HIGH")`: Выводит сообщение, если предположение пользователя больше загаданного числа.
    `print(f"YOU GOT IT IN {attempts_count} TRIES")`: Выводит сообщение о победе и количестве попыток, если пользователь угадал число.
    `break`: Прерывает цикл `while`, когда число угадано.
    `try ... except ValueError`: обрабатывает исключение если пользователь вводит не целое число, и сообщает об ошибке
    `continue` - пропускает текущую итерацию цикла, и запрашивает новое число

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'

# Запускаем игру
if __name__ == "__main__":
    play_mnoply()
```