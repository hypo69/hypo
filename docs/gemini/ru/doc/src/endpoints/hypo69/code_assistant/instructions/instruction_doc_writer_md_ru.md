# Модуль example

## Обзор

Этот модуль предоставляет примеры функций и классов для демонстрации.

## Классы

### `ExampleClass`

**Описание**: Класс `ExampleClass` содержит методы для выполнения различных операций.

**Методы**

- `method_one(arg1: str, arg2: int = 0) -> str`: Метод `method_one` принимает строку и целое число в качестве аргументов и возвращает строку.
```python
def method_one(arg1: str, arg2: int = 0) -> str:
    """
    Args:
        arg1 (str): Первая строковый аргумент.
        arg2 (int, optional): Второе целое число. По умолчанию 0.

    Returns:
        str: Результирующая строка.
    """
    return f"Результат: {arg1} {arg2}"
```
- `method_two(data: list[int]) -> int`: Метод `method_two` принимает список целых чисел и возвращает сумму элементов.
```python
def method_two(data: list[int]) -> int:
    """
    Args:
        data (list[int]): Список целых чисел.

    Returns:
        int: Сумма элементов списка.
    """
    return sum(data)
```


## Функции

### `calculate_sum(numbers: list[int]) -> int`

**Описание**: Функция `calculate_sum` вычисляет сумму чисел в списке.

**Параметры**
- `numbers` (list[int]): Список чисел для суммирования.

**Возвращает**
- `int`: Сумма чисел в списке.

```python
def calculate_sum(numbers: list[int]) -> int:
    """
    Args:
        numbers (list[int]): Список чисел для суммирования.

    Returns:
        int: Сумма чисел в списке.
    """
    return sum(numbers)
```

### `greet(name: str) -> str`

**Описание**: Функция `greet` приветствует человека по имени.

**Параметры**
- `name` (str): Имя человека.

**Возвращает**
- `str`: Приветственное сообщение.

```python
def greet(name: str) -> str:
    """
    Args:
        name (str): Имя человека.

    Returns:
        str: Приветственное сообщение.
    """
    return f"Привет, {name}!"
```