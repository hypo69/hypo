# Игра "Херкл"

## Обзор

Этот модуль реализует игру "Херкл", в которой игрок должен найти Херкла, перемещаясь по числовой оси. Компьютер случайным образом выбирает позицию Херкла, а игрок вводит свои координаты. Компьютер сообщает направление (запад или восток) и расстояние до Херкла. Цель игры — найти Херкла за минимальное количество шагов.

## Содержание
1. [Функции](#Функции)
    - [`main`](#main)

## Функции

### `main`

**Описание**: 
Основная функция, реализующая логику игры "Херкл".

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Возникает, если пользователь вводит не целое число при запросе позиции.
```python
def main():
    """
    Основная функция, реализующая логику игры "Херкл".
    """
    numberOfSteps = 0
    hurklePosition = random.randint(1, 1000)

    while True:
        numberOfSteps += 1
        try:
            userPosition = int(input("Введите вашу позицию (от 1 до 1000): "))
        except ValueError as ex:
            print("Пожалуйста, введите целое число.")
            continue

        if userPosition == hurklePosition:
            print(f"ПОЗДРАВЛЯЮ! Вы нашли его за {numberOfSteps} шагов!")
            break
        elif userPosition < hurklePosition:
            distance = hurklePosition - userPosition
            print(f"EAST {distance}")
        else:
            distance = userPosition - hurklePosition
            print(f"WEST {distance}")
```