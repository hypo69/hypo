# DIAMND

## Обзор

Этот модуль реализует игру "DIAMND", которая выводит на экран ромб из звездочек. Пользователь задает высоту ромба (количество строк в верхней половине), которая должна быть нечетным и положительным числом.

## Содержание

1. [Функции](#Функции)
   - [`print_diamond`](#print_diamond)

## Функции

### `print_diamond`

**Описание**:
Функция печатает ромб на экране, основываясь на высоте, введенной пользователем. Высота должна быть нечетным и положительным числом.

**Параметры**:
- Нет параметров

**Возвращает**:
- `None`: Функция не возвращает значения, а выводит результат на экран.

**Вызывает исключения**:
- `ValueError`: Возникает, если пользователь вводит не целое число.
```python
    def print_diamond():
        """
        הפונקציה מדפיסה יהלום על המסך, בהתאם לגובה שהמשתמש מכניס.
        הגובה חייב להיות מספר אי-זוגי וחיובי.
        """
```