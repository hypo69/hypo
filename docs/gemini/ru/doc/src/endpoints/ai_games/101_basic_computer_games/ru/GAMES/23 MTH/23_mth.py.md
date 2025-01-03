# Игра "Угадай число"

## Обзор

Игра "Угадай число" - это классическая игра, в которой компьютер выбирает случайное число в диапазоне от 1 до 100, а игрок должен угадать это число, получая подсказки "слишком низко" или "слишком высоко" после каждой попытки. Игра продолжается до тех пор, пока игрок не угадает число.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
- [Переменные](#переменные)
- [Игровой цикл](#игровой-цикл)

## Функции

В данном коде нет пользовательских функций, используется только стандартная функция `random.randint()` из модуля `random`.

## Переменные

### `numberOfGuesses`

**Описание**:
Хранит количество попыток, которые предпринял игрок, чтобы угадать число. Изначально инициализируется значением 0.
### `targetNumber`

**Описание**:
Хранит случайное целое число, сгенерированное в диапазоне от 1 до 100, которое игрок должен угадать.

## Игровой цикл

### `while True`

**Описание**:
Бесконечный цикл, который продолжается до тех пор, пока игрок не угадает загаданное число.

**Операции в цикле**:
   - `numberOfGuesses += 1`: Увеличивает количество попыток на 1 при каждой итерации цикла.

   - `try...except ValueError`:  Блок обработки исключений, используемый для обеспечения корректного ввода данных пользователем.

   - `userGuess = int(input("Угадай число от 1 до 100: "))`:
        Запрашивает у пользователя ввод числа от 1 до 100, преобразуя введенное значение в целое число.
       
   - `if userGuess == targetNumber:`:
        Проверяет, угадал ли пользователь число. Если условие верно, выводит сообщение о победе и количество попыток, после чего прерывает цикл.

   - `elif userGuess < targetNumber`:
        Если введенное число меньше загаданного, выводит сообщение "Слишком низко".

   - `else`:
        Если введенное число больше загаданного, выводит сообщение "Слишком высоко".

```python
import random

# Инициализация счетчика попыток
numberOfGuesses = 0
# Генерируем случайное число от 1 до 100
targetNumber = random.randint(1, 100)

# Основной игровой цикл
while True:
    # Увеличиваем количество попыток
    numberOfGuesses += 1
    # Запрашиваем ввод числа у пользователя
    try:
        userGuess = int(input("Угадай число от 1 до 100: "))
    except ValueError as ex:
        print("Пожалуйста, введите целое число.")
        continue

    # Проверяем, угадано ли число
    if userGuess == targetNumber:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")
        break  # Завершаем цикл, если число угадано
    elif userGuess < targetNumber:
        print("Слишком низко")  # Сообщаем, что загаданное число больше
    else:
        print("Слишком высоко")  # Сообщаем, что загаданное число меньше

```