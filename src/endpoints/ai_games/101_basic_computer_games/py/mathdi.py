"""
MATHDI:
=================
Сложность: 3
-----------------
Игра "MATHDI" - это простая игра-викторина, где пользователю предлагается решить 10 математических примеров, основанных на случайных операциях сложения, вычитания, умножения и деления.
Игрок вводит ответы, и в конце игры подсчитывается количество правильных ответов.
-----------------
Правила игры:
1. Игроку предлагается 10 математических примеров.
2. Каждый пример состоит из двух случайных чисел (от 1 до 10) и случайной операции (+, -, *, /).
3. Игрок должен ввести результат вычисления с клавиатуры.
4. После 10 примеров, игра сообщает количество правильных ответов.
-----------------
Алгоритм:
1. Установить количество правильных ответов равным 0.
2. Начать цикл из 10 итераций (для 10 вопросов).
3. Внутри цикла:
    a. Сгенерировать два случайных числа в диапазоне от 1 до 10 (включительно).
    b. Выбрать случайную арифметическую операцию (+, -, *, /).
    c. Вывести на экран математическое выражение, используя сгенерированные числа и операцию.
    d. Запросить у пользователя ввод ответа.
    e. Вычислить правильный ответ.
    f. Сравнить ответ пользователя с правильным ответом.
    g. Если ответ пользователя правильный, увеличить счетчик правильных ответов.
4. После цикла, вывести общее количество правильных ответов.
-----------------
Блок-схема: 
```mermaid
graph TD
    Start(Начало) --> InitializeCorrectAnswers{Инициализировать верные ответы = 0};
    InitializeCorrectAnswers --> LoopStart{Начало цикла (10 раз)};
    LoopStart --> GenerateNumber1{Сгенерировать случайное число 1};
    GenerateNumber1 --> GenerateNumber2{Сгенерировать случайное число 2};
    GenerateNumber2 --> SelectOperation{Выбрать случайную операцию};
    SelectOperation --> DisplayExpression{Вывести выражение};
    DisplayExpression --> InputAnswer{Ввод ответа пользователя};
    InputAnswer --> CalculateCorrectAnswer{Вычислить правильный ответ};
    CalculateCorrectAnswer --> CheckAnswer{Проверить ответ пользователя};
    CheckAnswer -- Верно --> IncrementCorrectAnswers{Увеличить счетчик верных ответов};
    CheckAnswer -- Не верно --> LoopEnd{Конец цикла};
	IncrementCorrectAnswers --> LoopEnd
    LoopEnd --> ConditionLoop{Конец цикла (10 раз)?};
    ConditionLoop -- Нет --> LoopStart;
    ConditionLoop -- Да --> DisplayResult{Вывести результат};
    DisplayResult --> End(Конец);
```
"""
import random

def calculate_expression(number1, number2, operation):
    """
    Вычисляет результат выражения на основе двух чисел и операции.

    Args:
        number1 (int): Первое число.
        number2 (int): Второе число.
        operation (str): Арифметическая операция (+, -, *, /).

    Returns:
        float: Результат вычисления или None в случае деления на ноль.
    """
    if operation == '+':
        return number1 + number2
    if operation == '-':
        return number1 - number2
    if operation == '*':
        return number1 * number2
    if operation == '/':
        if number2 == 0:
            return None # Обработка деления на ноль
        return number1 / number2
    return None # в случае некорректной операции

def main():
    """
    Основная функция, реализующая игру MATHDI.
    """
    correct_answers = 0  # Инициализация счетчика правильных ответов
    number_of_questions = 10 # количество вопросов

    for _ in range(number_of_questions):  # Цикл из 10 вопросов
        number1 = random.randint(1, 10)  # Генерация первого случайного числа от 1 до 10
        number2 = random.randint(1, 10)  # Генерация второго случайного числа от 1 до 10
        operations = ['+', '-', '*', '/'] # Список возможных операций
        operation = random.choice(operations)  # Выбор случайной операции из списка

        print(f"Решите пример: {number1} {operation} {number2} = ?") # Вывод примера на экран

        try:
             user_answer = float(input("Ваш ответ: ")) # получение ввода пользователя и конвертация в float
        except ValueError:
           print("Некорректный ввод, введите число")
           continue
        correct_answer = calculate_expression(number1, number2, operation) # вычисление правильного ответа

        if correct_answer is None:
           print("Деление на ноль не допускается. Пожалуйста, попробуйте еще раз.")
           continue

        if abs(user_answer - correct_answer) < 1e-6:  # сравнение с учетом погрешности float
            print("Правильно!")
            correct_answers += 1  # Увеличение счетчика правильных ответов
        else:
            print(f"Неправильно. Правильный ответ: {correct_answer}")
    print(f"Вы ответили правильно на {correct_answers} из {number_of_questions} вопросов.")  # Вывод общего количества правильных ответов

if __name__ == "__main__":
    main()
"""
Пояснения:
1.  `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных операций.
2.  `calculate_expression(number1, number2, operation)`:
    -   Принимает два числа (`number1`, `number2`) и арифметическую операцию (`operation`).
    -   Выполняет вычисления в зависимости от операции (+, -, *, /).
    -   Возвращает результат вычисления. Если происходит деление на ноль, возвращает None.
3.  `main()`:
    -   `correct_answers = 0`: Инициализирует счетчик правильных ответов.
	- `number_of_questions = 10`: Количество вопросов в игре.
    -   Цикл `for _ in range(number_of_questions)`: Запускает цикл из 10 итераций (вопросов).
    -   `number1 = random.randint(1, 10)`: Генерирует первое случайное число от 1 до 10.
    -   `number2 = random.randint(1, 10)`: Генерирует второе случайное число от 1 до 10.
    -   `operations = ['+', '-', '*', '/']`: Создает список возможных арифметических операций.
    -   `operation = random.choice(operations)`: Выбирает случайную операцию из списка.
    -   `print(f"Решите пример: {number1} {operation} {number2} = ?")`: Выводит на экран математический пример.
    -   `user_answer = float(input("Ваш ответ: "))`: Запрашивает у пользователя ввод ответа и преобразует его во float.
	- `correct_answer = calculate_expression(number1, number2, operation)`: Вызывает функцию `calculate_expression` для вычисления правильного ответа.
	- `if correct_answer is None:`: Проверяем не произошло ли деление на ноль
    -   `if abs(user_answer - correct_answer) < 1e-6:`: Сравнивает ответ пользователя с правильным ответом, учитывая погрешности float.
    -   Если ответ пользователя правильный:
        -   Выводит "Правильно!".
        -   Увеличивает счетчик `correct_answers` на 1.
    -   Иначе:
        -   Выводит "Неправильно." и правильный ответ.
    -   `print(f"Вы ответили правильно на {correct_answers} из {number_of_questions} вопросов.")`: Выводит общее количество правильных ответов после завершения всех вопросов.
4.  `if __name__ == "__main__": main()`: Проверяет, является ли скрипт основным исполняемым файлом, и запускает функцию `main()`.

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```