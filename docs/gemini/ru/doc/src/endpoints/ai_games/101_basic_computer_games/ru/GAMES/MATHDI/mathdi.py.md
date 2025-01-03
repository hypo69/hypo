# MATHDI

## Обзор

Игра "Математические задачи" предлагает пользователю решить простую математическую задачу (сложение, вычитание, умножение или деление) и проверяет правильность ответа. Игра генерирует случайные числа и операцию.

## Оглавление
1. [Функции](#Функции)

## Функции

### `main_loop`
**Описание**:
Основной игровой цикл, генерирует математическое выражение, запрашивает ответ у пользователя и проверяет его.
        
**Параметры**:
    - `isGameOver` (bool): Флаг для управления циклом игры, инициализируется как `False`.

**Возвращает**:
  - `None`

**Вызывает исключения**:
 -   `ValueError`: Возникает, если пользователь вводит некорректное значение, которое не может быть преобразовано в число с плавающей точкой.
 -   `ZeroDivisionError`: Возникает, при деление на ноль.

```python
import random

# Флаг для управления циклом игры
isGameOver = False

# Основной игровой цикл
while not isGameOver:
    # Генерируем два случайных числа от 1 до 10
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    
    # Выбираем случайную операцию
    operations = ["+", "-", "*", "/"]
    operation = random.choice(operations)
    
    # Формируем математическое выражение в виде строки
    expression = f"{number1} {operation} {number2}"
    
    # Выводим выражение пользователю
    print(f"Решите: {expression} = ?")
    
    # Получаем ответ от пользователя
    try:
        userAnswer = float(input("Ваш ответ: "))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
        continue
    
    # Вычисляем правильный ответ
    try:
      correctResult = eval(expression)
    except ZeroDivisionError:
      print("Деление на ноль невозможно. Попробуйте еще раз.")
      continue

    # Проверяем ответ
    if userAnswer == correctResult:
        print("CORRECT")
        isGameOver = True  # Завершаем игру, если ответ правильный
    else:
        print("INCORRECT. TRY AGAIN.")
```
## Описание кода

1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел и выбора случайной операции.
2. **Инициализация переменной**
   - `isGameOver = False`: Инициализируется флаг isGameOver как False. Этот флаг будет использоваться для контроля цикла игры.
3.  **Основной цикл игры `while not isGameOver:`**:
    -   Этот цикл выполняется, пока флаг `isGameOver` остается `False`. Как только ответ пользователя будет правильным, флаг будет установлен в `True`, и цикл завершится.
4.  **Генерация случайных чисел и операции**:
    -   `number1 = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и сохраняет его в `number1`.
    -   `number2 = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и сохраняет его в `number2`.
    -   `operations = ["+", "-", "*", "/"]`: Создает список допустимых математических операций.
    -   `operation = random.choice(operations)`: Выбирает случайную операцию из списка и сохраняет её в `operation`.
5.  **Формирование выражения**:
    -   `expression = f"{number1} {operation} {number2}"`: Формирует строку, представляющую математическое выражение, используя f-строку для вставки значений чисел и операции.
6.  **Вывод выражения пользователю**:
    -   `print(f"Решите: {expression} = ?")`: Выводит на экран математическое выражение для решения пользователем.
7.  **Получение ответа от пользователя**:
    -   `try...except ValueError`: Обрабатывает возможную ошибку ввода, если пользователь введет не число.
    -   `userAnswer = float(input("Ваш ответ: "))`: Запрашивает у пользователя ответ, преобразуя ввод в число с плавающей точкой (для возможности ввода не целых чисел).
8.  **Вычисление правильного ответа**:
      -  `try...except ZeroDivisionError`: Обрабатывает возможную ошибку деления на ноль
      -   `correctResult = eval(expression)`: Вычисляет правильный результат, используя функцию eval(). Она выполняет вычисление выражения, которое хранится в виде строки.
9.  **Проверка ответа пользователя**:
    -   `if userAnswer == correctResult:`: Проверяет, является ли введенный ответ пользователя правильным.
    -   `print("CORRECT")`: Выводит сообщение о правильном ответе.
    -   `isGameOver = True`: Устанавливает флаг `isGameOver` в `True`, что приводит к завершению основного цикла игры.
    -   `else:`: Если ответ неправильный.
    -   `print("INCORRECT. TRY AGAIN.")`: Выводит сообщение о неправильном ответе и предлагает попробовать снова.