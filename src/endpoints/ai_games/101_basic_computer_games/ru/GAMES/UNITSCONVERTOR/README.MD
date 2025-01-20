
UNITS CONVERTOR:
=================
Сложность: 4
-----------------
Игра "UNITS CONVERTOR" - это игра, в которой игрок получает случайные задания на конвертацию единиц измерения и пытается дать правильный ответ.
За каждое правильное решение игрок получает очки. Игра состоит из нескольких раундов.
В конце игры выводится результат (количество набранных очков и время, затраченное на игру).

Правила игры:
1. Игрок выбирает уровень сложности (легкий, средний, сложный).
2. Игрок получает случайное задание на конвертацию единиц измерения (длина, масса, температура).
3. Игрок вводит свой ответ.
4. Если ответ правильный, игроку начисляется 1 очко.
5. Игра состоит из 5 раундов.
6. В конце игры выводится количество набранных очков и общее время, затраченное на игру.
-----------------
Алгоритм:
1. Определить функции для каждой конвертации: meters_to_kilometers, kilometers_to_meters, miles_to_kilometers, kilometers_to_miles, kilograms_to_pounds, pounds_to_kilograms, celsius_to_fahrenheit, fahrenheit_to_celsius.
2. Определить функцию get_conversion_task, которая генерирует случайное задание на конвертацию и возвращает его текст и правильный ответ.
    2.1. Выбрать случайную категорию (длина, масса или температура).
    2.2. Выбрать случайную функцию конвертации внутри этой категории.
    2.3. Сгенерировать случайное значение для конвертации.
    2.4. Сформировать текст задания и вычислить правильный ответ.
    2.5. Вернуть текст задания и правильный ответ.
3. Определить функцию play_conversion_game, которая запускает игру.
    3.1. Запросить уровень сложности (1-легкий, 2-средний, 3-сложный).
    3.2. Инициализировать счетчик очков и количество раундов.
    3.3. Запустить таймер.
    3.4. Начать цикл по количеству раундов:
        3.4.1. Получить задание и правильный ответ с помощью функции get_conversion_task.
        3.4.2. Вывести задание на экран.
        3.4.3. Запросить ввод ответа пользователя.
        3.4.4. Если ответ пользователя совпадает с правильным ответом, начислить 1 очко.
        3.4.5. Вывести сообщение о правильности ответа.
    3.5. Остановить таймер.
    3.6. Вывести общий результат (количество набранных очков и время игры).
4. Вызвать play_conversion_game в основном блоке программы.
-----------------


```python
import random
import time

def meters_to_kilometers(meters):
    """Конвертирует метры в километры."""
    return meters / 1000

def kilometers_to_meters(kilometers):
    """Конвертирует километры в метры."""
    return kilometers * 1000

def miles_to_kilometers(miles):
    """Конвертирует мили в километры."""
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    """Конвертирует километры в мили."""
    return kilometers / 1.60934

def kilograms_to_pounds(kilograms):
    """Конвертирует килограммы в фунты."""
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    """Конвертирует фунты в килограммы."""
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    """Конвертирует градусы Цельсия в градусы Фаренгейта."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертирует градусы Фаренгейта в градусы Цельсия."""
    return (fahrenheit - 32) * 5/9

def get_conversion_task(level):
    """
    Генерирует случайное задание на конвертацию.
    """
    categories = [("length", ["meters_to_kilometers", "kilometers_to_meters", "miles_to_kilometers", "kilometers_to_miles"]),
                  ("weight", ["kilograms_to_pounds", "pounds_to_kilograms"]),
                  ("temperature", ["celsius_to_fahrenheit", "fahrenheit_to_celsius"])]

    category, conversions = random.choice(categories)
    conversion = random.choice(conversions)

    if category == "length":
        value = random.randint(1, 1000) if level <= 2 else random.randint(100, 10000)
    elif category == "weight":
        value = random.randint(1, 100) if level <= 2 else random.randint(10, 1000)
    elif category == "temperature":
        value = random.randint(-50, 50) if level <= 2 else random.randint(-100, 100)

    if conversion == "meters_to_kilometers":
      task = f"Конвертируйте {value} метров в километры"
      correct_answer = meters_to_kilometers(value)
    elif conversion == "kilometers_to_meters":
      task = f"Конвертируйте {value} километров в метры"
      correct_answer = kilometers_to_meters(value)
    elif conversion == "miles_to_kilometers":
      task = f"Конвертируйте {value} миль в километры"
      correct_answer = miles_to_kilometers(value)
    elif conversion == "kilometers_to_miles":
      task = f"Конвертируйте {value} километров в мили"
      correct_answer = kilometers_to_miles(value)
    elif conversion == "kilograms_to_pounds":
      task = f"Конвертируйте {value} кг в фунты"
      correct_answer = kilograms_to_pounds(value)
    elif conversion == "pounds_to_kilograms":
      task = f"Конвертируйте {value} фунтов в кг"
      correct_answer = pounds_to_kilograms(value)
    elif conversion == "celsius_to_fahrenheit":
      task = f"Конвертируйте {value} градусов Цельсия в градусы Фаренгейта"
      correct_answer = celsius_to_fahrenheit(value)
    elif conversion == "fahrenheit_to_celsius":
      task = f"Конвертируйте {value} градусов Фаренгейта в градусы Цельсия"
      correct_answer = fahrenheit_to_celsius(value)

    return task, correct_answer

def play_conversion_game():
    """
    Основная функция игры UNITS CONVERTOR.
    """
    print("Добро пожаловать в игру по конвертации единиц измерения!")
    try:
        level = int(input("Выберите уровень сложности (1-легкий, 2-средний, 3-сложный): "))
        if level not in [1, 2, 3]:
          print("Неверный уровень сложности. Пожалуйста, выберите 1, 2 или 3.")
          return
    except ValueError:
      print("Неверный ввод. Пожалуйста, введите 1, 2 или 3 для уровня сложности.")
      return

    score = 0
    num_tasks = 5
    start_time = time.time()

    for _ in range(num_tasks):
        task, correct_answer = get_conversion_task(level)
        print("\n" + task)
        try:
          user_answer = float(input("Ваш ответ: "))
          if abs(user_answer - correct_answer) < 0.01:
            print("Правильно!")
            score += 1
          else:
            print(f"Неправильно. Правильный ответ: {correct_answer:.2f}")
        except ValueError:
            print("Неверный ввод, попробуйте снова.")
            continue


    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nИгра окончена!")
    print(f"Ваш счет: {score}/{num_tasks}")
    print(f"Время игры: {elapsed_time:.2f} секунд")


if __name__ == "__main__":
    play_conversion_game()

```

Разбор кода:
1.  **Импорт модулей `random` и `time`**:
    -   `import random`: Импортирует модуль `random`, используемый для генерации случайных задач.
    -   `import time`: Импортирует модуль `time`, используемый для измерения времени игры.
2.  **Функции конвертации**:
    -   `meters_to_kilometers(meters)`: Конвертирует метры в километры.
    -   `kilometers_to_meters(kilometers)`: Конвертирует километры в метры.
    -   `miles_to_kilometers(miles)`: Конвертирует мили в километры.
    -   `kilometers_to_miles(kilometers)`: Конвертирует километры в мили.
    -   `kilograms_to_pounds(kilograms)`: Конвертирует килограммы в фунты.
    -   `pounds_to_kilograms(pounds)`: Конвертирует фунты в килограммы.
    -   `celsius_to_fahrenheit(celsius)`: Конвертирует градусы Цельсия в градусы Фаренгейта.
    -   `fahrenheit_to_celsius(fahrenheit)`: Конвертирует градусы Фаренгейта в градусы Цельсия.
        *   Все эти функции принимают значение для конвертации в качестве аргумента и возвращают результат.
3.  **Функция `get_conversion_task(level)`**:
    -   Принимает уровень сложности `level` в качестве аргумента.
    -   Определяет список категорий (`categories`) и доступных конвертаций.
    -   Случайно выбирает категорию и конвертацию из списка.
    -   Генерирует случайное значение для конвертации (диапазон зависит от уровня сложности).
    -   Формирует текст задания и вычисляет правильный ответ.
    -   Возвращает текст задания и правильный ответ.
4.  **Функция `play_conversion_game()`**:
    -   Выводит приветственное сообщение.
    -   Запрашивает уровень сложности у пользователя и проверяет ввод на корректность.
    -   Инициализирует счетчик очков, количество раундов и таймер.
    -   **Цикл по раундам**:
        -   Получает задание и правильный ответ с помощью функции `get_conversion_task()`.
        -   Выводит задание на экран.
        -   Запрашивает ввод ответа от пользователя.
        -   Если ответ пользователя совпадает с правильным ответом (в пределах небольшой погрешности), то начисляет 1 очко.
        -   Выводит сообщение о правильности ответа.
        -   Обрабатывает исключение ValueError, если пользователь вводит некорректное значение.
    -   Останавливает таймер.
    -   Выводит общий результат (количество набранных очков и время игры).
5.  **Основной блок (`if __name__ == "__main__":`)**:
    -   Вызывает функцию `play_conversion_game()` для запуска игры, если файл запускается напрямую.
