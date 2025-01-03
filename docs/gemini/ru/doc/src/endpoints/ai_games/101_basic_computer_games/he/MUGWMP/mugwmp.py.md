# MUGWMP

## Обзор

Этот модуль реализует игру "MUGWMP", в которой игрок пытается угадать последовательность из четырех цифр, каждая из которых находится в диапазоне от 1 до 6. После каждой попытки компьютер предоставляет подсказки о количестве правильных цифр на правильном месте (Mugs) и количестве правильных цифр на неправильном месте (Wumps).

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`create_target_sequence`](#create_target_sequence)
  - [`calculate_mugs_wumps`](#calculate_mugs_wumps)
  - [`play_mugwmp`](#play_mugwmp)

## Функции

### `create_target_sequence`

**Описание**:
Создает случайную последовательность из 4 цифр, каждая из которых находится в диапазоне от 1 до 6.

**Возвращает**:
- `list`: Случайная последовательность из 4 цифр.

### `calculate_mugs_wumps`

**Описание**:
Вычисляет количество "Mugs" (правильные цифры на правильном месте) и "Wumps" (правильные цифры на неправильном месте).

**Параметры**:
- `target_sequence` (list): Исходная последовательность, которую пытается угадать пользователь.
- `user_sequence` (list): Последовательность, введенная пользователем в качестве предположения.

**Возвращает**:
- `tuple`: Количество mugs и wumps.

### `play_mugwmp`

**Описание**:
Управляет игровым процессом MUGWMP.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- `ValueError`: Вызывается, если пользователь вводит не числовую последовательность.