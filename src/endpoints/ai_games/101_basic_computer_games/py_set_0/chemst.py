"""
CHEMST:
=================
Сложность: 3
-----------------
Игра "Химик" - это текстовая игра, в которой игрок пытается угадать количество атомов в химической формуле. Игрок вводит предполагаемое число атомов, и игра сообщает, является ли это число правильным или нет, и если нет, то больше или меньше загаданного числа.

Правила игры:
1. Игра загадывает случайное число атомов в диапазоне от 1 до 100.
2. Игрок вводит свою догадку о количестве атомов.
3. Игра сравнивает догадку игрока с загаданным числом.
4. Если догадка верна, игра поздравляет игрока и заканчивается.
5. Если догадка неверна, игра сообщает, было ли загаданное число больше или меньше догадки игрока.
6. Игрок может делать новые попытки, пока не угадает число.

-----------------
Алгоритм:
1. Установить константу MAX_ATOMS = 100.
2. Сгенерировать случайное число атомов atomsNumber в диапазоне от 1 до MAX_ATOMS.
3. Запросить у пользователя ввод числа атомов guessNumber.
4. Сравнить guessNumber с atomsNumber:
   - Если guessNumber равно atomsNumber, вывести сообщение о выигрыше и завершить игру.
   - Если guessNumber меньше atomsNumber, вывести сообщение "Слишком мало."
   - Если guessNumber больше atomsNumber, вывести сообщение "Слишком много."
5. Перейти к шагу 3, если guessNumber не равно atomsNumber.
-----------------
Блок-схема: 
```mermaid
graph TD
    Start(Start) --> InitMaxAtoms(Init MAX_ATOMS = 100);
    InitMaxAtoms --> GenerateRandomNumber(Generate random atomsNumber between 1 and MAX_ATOMS);
    GenerateRandomNumber --> InputGuess(Input guessNumber from user);
    InputGuess --> CompareGuess(Compare guessNumber with atomsNumber);
    CompareGuess -- guessNumber == atomsNumber --> OutputWin(Output "You got it right!");
    OutputWin --> End(End);
    CompareGuess -- guessNumber < atomsNumber --> OutputTooLow(Output "Too low.");
    OutputTooLow --> InputGuess;
    CompareGuess -- guessNumber > atomsNumber --> OutputTooHigh(Output "Too high.");
    OutputTooHigh --> InputGuess;
```
"""
import random

# Константа, определяющая максимальное количество атомов
MAX_ATOMS = 100

# Генерируем случайное число атомов от 1 до MAX_ATOMS
atoms_number = random.randint(1, MAX_ATOMS)

# Флаг для контроля цикла игры
game_over = False

# Основной цикл игры
while not game_over:
    # Запрашиваем у пользователя ввод числа атомов
    try:
        guess_number = int(input("Сколько атомов, по-твоему, в химической формуле? (от 1 до 100) "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # Сравниваем догадку пользователя с загаданным числом
    if guess_number == atoms_number:
        print("Правильно! Ты угадал количество атомов!")
        game_over = True  # Завершаем игру
    elif guess_number < atoms_number:
        print("Слишком мало.")
    else:
        print("Слишком много.")

"""
Пояснения:
1. `MAX_ATOMS = 100`: Объявляем константу для максимального количества атомов.
2. `atoms_number = random.randint(1, MAX_ATOMS)`: Генерируем случайное целое число в диапазоне от 1 до MAX_ATOMS (включительно) и сохраняем его в переменной `atoms_number`.
3. `game_over = False`: Инициализируем логическую переменную для контроля цикла игры. Она станет `True`, когда игрок угадает число.
4. `while not game_over:`: Начинаем цикл `while`, который будет выполняться до тех пор, пока `game_over` не станет `True`.
5. `try...except ValueError`: Используем обработку исключений, чтобы убедиться, что пользователь вводит целое число. Если пользователь вводит что-то, что не может быть преобразовано в целое число, выводится сообщение об ошибке, и цикл начинается заново.
6. `guess_number = int(input(...))`: Выводим сообщение с запросом ввода числа атомов, преобразуем ввод пользователя в целое число и сохраняем его в переменной `guess_number`.
7. `if guess_number == atoms_number`: Если догадка пользователя равна загаданному числу, выводим сообщение о выигрыше и устанавливаем `game_over = True`, что завершает игру.
8. `elif guess_number < atoms_number`: Если догадка пользователя меньше загаданного числа, выводим сообщение "Слишком мало."
9. `else`: Если догадка пользователя больше загаданного числа, выводим сообщение "Слишком много."
10. Цикл продолжается, пока пользователь не угадает число.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```