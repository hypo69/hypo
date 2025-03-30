# Модуль `any`

## Обзор

Модуль `any` предоставляет утилиты для рекурсивного преобразования данных любого типа в словарь. Он предназначен для работы с различными структурами данных, включая списки, кортежи, множества, числа, строки, булевы значения и объекты, преобразуя их в словарное представление.

## Подробней

Модуль содержит функцию `any2dict`, которая рекурсивно преобразует входные данные в словарь. Это полезно, когда необходимо представить сложные структуры данных в виде словаря для дальнейшей обработки или сериализации. Функция обрабатывает базовые типы данных, такие как числа, строки и булевы значения, а также коллекции, такие как списки, множества и словари.

## Функции

### `any2dict`

```python
def any2dict(any_data: Any) -> dict | list | str | int | float | bool | None:
    """
    Args:
        any_data (Any): Любой тип данных.

    Returns:
        dict | list | str | int | float | bool | None: Словарь, представляющий входные данные, или False, если преобразование невозможно.

    Raises:
        - Ошибки не вызываются.

    Example:
        >>> data = {"name": "John", "age": 30}
        >>> any2dict(data)
        {'name': 'John', 'age': 30}
    """
    # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Рекурсивно преобразует любой тип данных в словарь.

**Параметры**:
- `any_data` (Any): Любой тип данных.

**Возвращает**:
- `dict | list | str | int | float | bool | None`: Словарь, представляющий входные данные, или `False`, если преобразование невозможно.

**Вызывает исключения**:
- Исключения не вызываются.

**Примеры**:

```python
import types

data1 = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "street": "Main St",
        "numbers":[1,2,3]
    },
   "phones": ["123-456-7890", "987-654-3210"],
   "skills": {"python", "java", "c++"}
}

print(any2dict(data1))
# Вывод: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'street': 'Main St', 'numbers': [1, 2, 3]}, 'phones': ['123-456-7890', '987-654-3210'], 'skills': ['python', 'java', 'c++']}

data2 = [1, 2, "three", {"key": "value"}]
print(any2dict(data2))
# Вывод: [1, 2, 'three', {'key': 'value'}]

data3 = 123
print(any2dict(data3))
# Вывод: 123

data4 = "string"
print(any2dict(data4))
# Вывод: string

data5 = None
print(any2dict(data5))
# Вывод: None

class MyClass:
    def __init__(self, x):
        self.x = x

data6 = MyClass(10)
print(any2dict(data6))
# Вывод: {}

# Тестируем SimpleNamespace
data7 = types.SimpleNamespace(a=1, b='hello', c=[1,2,3])
print(any2dict(data7))
# Вывод: {'a': 1, 'b': 'hello', 'c': [1, 2, 3]}

data8 = {'a':1, 'b': types.SimpleNamespace(x=2, y=3)}
print(any2dict(data8))
# Вывод: {'a': 1, 'b': {'x': 2, 'y': 3}}

data9 = [types.SimpleNamespace(x=2), 3, 'str']
print(any2dict(data9))
# Вывод: [{'x': 2}, 3, 'str']

data10 = types.SimpleNamespace(a=1, b=MyClass(3))
print(any2dict(data10))
# Вывод: {'a': 1, 'b': ''}

data11 = {"a":1, "b": MyClass(10)}
print(any2dict(data11))
# Вывод: {'a': 1, 'b': ''}