# Модуль example_module

## Обзор

Этот модуль предоставляет функции для работы с числами.

## Функции

### `add_numbers`

**Описание**: Функция суммирует два числа.

**Параметры**:
- `num1` (int): Первое слагаемое.
- `num2` (int): Второе слагаемое.

**Возвращает**:
- `int`: Сумма `num1` и `num2`.

**Вызывает исключения**:
- `TypeError`: Если входные значения не являются числами.


```python
def add_numbers(num1: int, num2: int) -> int:
    """
    Args:
        num1 (int): First addend.
        num2 (int): Second addend.

    Returns:
        int: The sum of num1 and num2.

    Raises:
        TypeError: If input values are not numbers.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Input values must be integers.")
    return num1 + num2
```

### `subtract_numbers`

**Описание**: Функция вычитает из первого числа второе.

**Параметры**:
- `num1` (int): Уменьшаемое.
- `num2` (int): Вычитаемое.

**Возвращает**:
- `int`: Разность `num1` и `num2`.

**Вызывает исключения**:
- `TypeError`: Если входные значения не являются числами.


```python
def subtract_numbers(num1: int, num2: int) -> int:
    """
    Args:
        num1 (int): Minuend.
        num2 (int): Subtrahend.

    Returns:
        int: Difference between num1 and num2.

    Raises:
        TypeError: If input values are not numbers.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Input values must be integers.")
    return num1 - num2