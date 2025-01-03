# Модуль `bomber.py`

## Обзор

Этот модуль реализует игру "Бомбардировщик", в которой игрок должен сбить цель, вводя начальную скорость и угол наклона снаряда. Цель расположена на фиксированном расстоянии. После каждой попытки игра вычисляет траекторию снаряда и отображает расстояние, на которое снаряд попал, и расстояние до цели. Игра продолжается, пока игрок не поразит цель или пока не будет использовано 10 попыток.

## Оглавление

1. [Константы](#константы)
2. [Функции](#функции)
    - [`play_bomber`](#play_bomber)

## Константы

### `GRAVITY`

**Описание**: Константа, представляющая ускорение свободного падения.
- Значение: `32.2`.

### `TARGET_DISTANCE`

**Описание**: Константа, представляющая расстояние до цели.
- Значение: `1000`.

## Функции

### `play_bomber`

**Описание**: Функция, содержащая основную логику игры "Бомбардировщик".

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция не возвращает никакого значения, игра завершается при попадании или по истечении количества попыток.

**Вызывает исключения**:
- `ValueError`: Возникает при вводе некорректных данных (не чисел) пользователем.

```python
def play_bomber():
    """
    Args:
        None

    Returns:
        None: Функция не возвращает никакого значения, игра завершается при попадании или по истечении количества попыток.
    
    Raises:
        ValueError: Возникает при вводе некорректных данных (не чисел) пользователем.
    """
    # Инициализация счетчика попыток
    number_of_attempts = 0

    # Основной цикл игры
    while number_of_attempts < 10:
        number_of_attempts += 1
        print(f"ניסיון {number_of_attempts}:")

        # Ввод данных от пользователя
        try:
            initial_angle = float(input("הזן זווית התחלתית (במעלות): "))
            initial_velocity = float(input("הזן מהירות התחלתית: "))
        except ValueError as ex:
            print("אנא הזן מספרים חוקיים.")
            continue
        
        # Преобразование угла в радианы
        angle_in_radians = math.radians(initial_angle)

        # Вычисление расстояния падения снаряда
        distance = (2 * initial_velocity**2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)) / GRAVITY

        # Вычисление расстояния до цели
        distance_to_target = abs(distance - TARGET_DISTANCE)

        print(f"מרחק פגיעה: {distance:.2f}")
        print(f"מרחק מהמטרה: {distance_to_target:.2f}")

        # Проверка на попадание
        if distance_to_target < 1:
            print("פגעת!")
            return  # Завершение функции при попадании

    # Сообщение о проигрыше, если не попали после 10 попыток
    print("לא פגעת!")
```