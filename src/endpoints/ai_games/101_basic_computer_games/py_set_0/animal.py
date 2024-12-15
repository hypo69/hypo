"""
BULL:
=================
Сложность: 4
-----------------
Игра "Быки и Коровы" - это игра-головоломка, где игрок пытается угадать секретное четырехзначное число, сгенерированное компьютером. Игрок делает предположения, и компьютер отвечает, сообщая количество "быков" (цифры, угаданные на правильном месте) и "коров" (цифры, угаданные, но не на своем месте).

Правила игры:
1. Компьютер генерирует случайное четырехзначное число, где все цифры различны.
2. Игрок вводит четырехзначное число.
3. Компьютер сравнивает число игрока с загаданным числом и сообщает:
    - Количество "быков" (BULLS) - цифры, угаданные на правильном месте.
    - Количество "коров" (COWS) - цифры, угаданные, но не на своем месте.
4. Игра продолжается, пока игрок не угадает число или не превысит лимит попыток.
-----------------
Алгоритм:
1.  Инициализация:
    - Сгенерировать случайное четырехзначное число с разными цифрами.
    - Установить количество попыток (по умолчанию 10)
2.  Игровой цикл:
    - Запросить у игрока предположение (четырехзначное число).
    - Проверить введенное число:
       - Если число не четырехзначное или не содержит разных цифр - запросить ввод заново.
    - Сравнить предположение с загаданным числом:
        - Посчитать количество "быков" (совпадения цифр на той же позиции).
        - Посчитать количество "коров" (совпадения цифр в другом положении).
    - Вывести количество "быков" и "коров".
    - Уменьшить количество оставшихся попыток.
    - Если количество "быков" равно 4, игрок выиграл - закончить игру.
    - Если количество попыток истекло, игрок проиграл - закончить игру.
3.  Конец игры:
    - Сообщить о выигрыше или проигрыше.
    - Предложить сыграть снова.
-----------------
Блок-схема:
```mermaid
graph TD
    Start(Start) --> GenerateSecretNumber(Generate Secret Number);
    GenerateSecretNumber --> SetAttempts(Set Attempts = 10);
    SetAttempts --> GameLoopStart(Game Loop Start);
    GameLoopStart --> InputGuess(Input Guess);
    InputGuess --> ValidateGuess(Validate Guess);
    ValidateGuess -- Invalid Guess --> InputGuess;
    ValidateGuess -- Valid Guess --> CalculateBullsCows(Calculate Bulls and Cows);
    CalculateBullsCows --> OutputBullsCows(Output Bulls and Cows);
    OutputBullsCows --> CheckWin(Check Win = Bulls == 4?);
    CheckWin -- Yes --> Win(Win);
    CheckWin -- No --> DecrementAttempts(Decrement Attempts);
    DecrementAttempts --> CheckAttempts(Check Attempts > 0?);
    CheckAttempts -- Yes --> GameLoopStart;
    CheckAttempts -- No --> Lose(Lose);
    Win --> PlayAgain(Play Again?);
    Lose --> PlayAgain;
    PlayAgain -- Yes --> GenerateSecretNumber;
    PlayAgain -- No --> End(End);
```
"""
import random

def generate_secret_number():
    """Генерирует случайное четырехзначное число с уникальными цифрами."""
    digits = list(range(10))
    random.shuffle(digits)
    # Убедимся, что первая цифра не ноль
    while digits[0] == 0:
        random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def validate_guess(guess):
    """Проверяет, что предположение - это четырехзначное число с уникальными цифрами."""
    if not guess.isdigit() or len(guess) != 4:
        return False, "Пожалуйста, введите четырехзначное число."
    if len(set(guess)) != 4:
        return False, "Цифры должны быть уникальными."
    return True, None

def calculate_bulls_cows(secret_number, guess):
    """Сравнивает guess с secret_number и вычисляет количество "быков" и "коров"."""
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if digit == secret_number[i]:
            bulls += 1
        elif digit in secret_number:
            cows += 1
    return bulls, cows

def play_bull_game():
    """Реализует игровую логику "Быки и Коровы"."""
    secret_number = generate_secret_number()
    attempts_left = 10 # Количество попыток
    print("Добро пожаловать в игру 'Быки и Коровы'!")
    print("Я загадал четырехзначное число с уникальными цифрами.")

    while attempts_left > 0:
        guess = input("Ваше предположение: ")
        is_valid, message = validate_guess(guess)
        if not is_valid:
            print(message)
            continue
    
        bulls, cows = calculate_bulls_cows(secret_number, guess)
        print(f"Быки: {bulls}, Коровы: {cows}")

        if bulls == 4:
            print("Вы угадали! Поздравляю!")
            break

        attempts_left -= 1
        print(f"Осталось попыток: {attempts_left}")
        
    if attempts_left == 0:
        print(f"Вы проиграли. Загаданное число было: {secret_number}")

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again == "да":
        play_bull_game()

if __name__ == "__main__":
    play_bull_game()
"""
Пояснения:
1.  Функция `generate_secret_number()`:
    -   Создает список цифр от 0 до 9.
    -   Перемешивает цифры случайным образом.
    -   Гарантирует, что первая цифра не ноль.
    -   Возвращает четырехзначное число в виде строки.
2.  Функция `validate_guess(guess)`:
    -   Проверяет, что предположение состоит из четырех цифр и все цифры уникальные.
    -   Возвращает `True` и `None`, если предположение валидно, иначе `False` и сообщение об ошибке.
3.  Функция `calculate_bulls_cows(secret_number, guess)`:
    -   Сравнивает предположение с загаданным числом и вычисляет количество "быков" и "коров".
    -   "Бык" - цифра на той же позиции.
    -   "Корова" - цифра присутствует в загаданном числе, но на другой позиции.
4.  Функция `play_bull_game()`:
    -   Запускает игровую логику "Быки и Коровы".
    -   Запрашивает у пользователя предположения.
    -   Выводит результаты (быки и коровы) или сообщение о победе/поражении.
5.  Основная часть программы:
    -   Вызывает `play_bull_game()`, чтобы начать игру.
licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'