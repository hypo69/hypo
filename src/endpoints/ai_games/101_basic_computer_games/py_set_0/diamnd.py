"""
DIAMND:
=================
Сложность: 4
-----------------
Игра "Бриллиант" представляет собой простую текстовую игру, в которой игрок пытается угадать загаданное компьютером число, представляющее размер "бриллианта". 
Размер бриллианта варьируется от 1 до 10.  
После каждой попытки компьютер сообщает, является ли введенное число больше или меньше загаданного. Игрок продолжает угадывать, пока не назовет правильное число.

Правила игры:
1. Компьютер случайным образом выбирает целое число от 1 до 10, представляющее размер бриллианта.
2. Игрок вводит число, которое, по его мнению, является размером бриллианта.
3. Компьютер сравнивает введенное число с загаданным и сообщает, больше ли оно, меньше или равно загаданному числу.
4. Если введенное число не равно загаданному, игрок повторяет шаг 2.
5. Если введенное число равно загаданному, игра заканчивается, и игрок побеждает.
-----------------
Алгоритм:
1. Присвоить переменной `diamondSize` случайное целое число от 1 до 10.
2. Вывести на экран сообщение "I AM THINKING OF A DIAMOND".
3. Вывести на экран сообщение "OF WHAT SIZE (1 TO 10)".
4. Ввести с клавиатуры число в переменную `playerGuess`.
5. Если `playerGuess` < `diamondSize`, то вывести на экран сообщение "TOO SMALL, TRY AGAIN". и перейти к шагу 4.
6. Если `playerGuess` > `diamondSize`, то вывести на экран сообщение "TOO BIG, TRY AGAIN". и перейти к шагу 4.
7. Если `playerGuess` = `diamondSize`, то вывести на экран сообщение "YOU GOT IT!".
8. Конец игры.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Начало) --> GenerateDiamondSize(Сгенерировать diamondSize случайное число от 1 до 10);
    GenerateDiamondSize --> OutputPrompt1(Вывести "I AM THINKING OF A DIAMOND");
    OutputPrompt1 --> OutputPrompt2(Вывести "OF WHAT SIZE (1 TO 10)");
    OutputPrompt2 --> InputPlayerGuess(Ввод playerGuess);
    InputPlayerGuess --> CompareGuess(Сравнить playerGuess и diamondSize);
    CompareGuess -- playerGuess < diamondSize --> OutputTooSmall(Вывести "TOO SMALL, TRY AGAIN");
    OutputTooSmall --> InputPlayerGuess;
    CompareGuess -- playerGuess > diamondSize --> OutputTooBig(Вывести "TOO BIG, TRY AGAIN");
    OutputTooBig --> InputPlayerGuess;
    CompareGuess -- playerGuess = diamondSize --> OutputWin(Вывести "YOU GOT IT!");
    OutputWin --> End(Конец);
```
"""
import random

def play_diamond_game():
    """
    Функция, реализующая игру "Бриллиант".
    """

    # 1. Присваиваем переменной diamondSize случайное целое число от 1 до 10.
    diamond_size = random.randint(1, 10)

    # 2. Выводим на экран сообщение "I AM THINKING OF A DIAMOND".
    print("I AM THINKING OF A DIAMOND")

    # 3. Выводим на экран сообщение "OF WHAT SIZE (1 TO 10)".
    print("OF WHAT SIZE (1 TO 10)")

    while True:
       # 4. Вводим с клавиатуры число в переменную playerGuess.
        try:
            player_guess = int(input("Ваш вариант: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        # 5. Если playerGuess < diamondSize, выводим "TOO SMALL, TRY AGAIN"
        if player_guess < diamond_size:
            print("TOO SMALL, TRY AGAIN")
            continue

        # 6. Если playerGuess > diamondSize, выводим "TOO BIG, TRY AGAIN"
        elif player_guess > diamond_size:
            print("TOO BIG, TRY AGAIN")
            continue
        
        # 7. Если playerGuess = diamondSize, выводим "YOU GOT IT!"
        else:
            print("YOU GOT IT!")
            break  # 8. Конец игры

# Запускаем игру
if __name__ == "__main__":
    play_diamond_game()
"""
Пояснения:
1.  `import random`: Импортируем модуль random для генерации случайных чисел.

2.  `def play_diamond_game():`:  Объявляем функцию `play_diamond_game`, в которой будет реализована логика игры.

3.  `diamond_size = random.randint(1, 10)`: Генерируем случайное целое число от 1 до 10 (включительно) и присваиваем его переменной `diamond_size`. Это размер бриллианта, который нужно угадать.

4.  `print("I AM THINKING OF A DIAMOND")`: Выводим сообщение о том, что компьютер задумал бриллиант.

5.  `print("OF WHAT SIZE (1 TO 10)")`: Выводим сообщение о том, что нужно угадать его размер.

6. `while True:`: Создаем бесконечный цикл, который будет продолжаться, пока игрок не угадает размер бриллианта.

7.  `try... except...`:  Обрабатываем возможные ошибки при вводе данных от пользователя. Если пользователь введет не число, то программа выведет сообщение и перейдет к следующей итерации цикла.

8.  `player_guess = int(input("Ваш вариант: "))`: Запрашиваем у пользователя ввод числа и преобразуем его в целое число. Это число - попытка угадать размер бриллианта.

9. `if player_guess < diamond_size: `:  Сравниваем введенное число с загаданным размером бриллианта. Если введенное число меньше, выводим сообщение "TOO SMALL, TRY AGAIN" и переходим к следующей итерации цикла, чтобы получить еще одну попытку.

10. `elif player_guess > diamond_size:`: Если введенное число больше, выводим сообщение "TOO BIG, TRY AGAIN" и переходим к следующей итерации цикла.

11. `else:`: Если введенное число не меньше и не больше загаданного, значит оно равно ему. 

12. `print("YOU GOT IT!")`: Выводим сообщение о победе, если игрок угадал размер бриллианта.

13. `break`: Завершаем цикл и игра заканчивается.

14. `if __name__ == "__main__":`: Проверяем, является ли скрипт запущенным напрямую. Если это так, вызываем функцию `play_diamond_game()` для начала игры.

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```