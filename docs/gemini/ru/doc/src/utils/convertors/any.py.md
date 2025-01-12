# Модуль `any`

## Обзор

Модуль `any` содержит утилиты для рекурсивного преобразования данных любого типа в словарь, список или базовые типы данных. Он предназначен для работы со сложными структурами данных, включая объекты, списки, кортежи, множества, и базовые типы, такие как целые числа, числа с плавающей точкой, строки, булевы значения и `None`.

## Содержание

- [Функции](#Функции)
    - [`any2dict`](#any2dict)

## Функции

### `any2dict`

**Описание**: 
Рекурсивно преобразует любой тип данных в словарь. Если преобразование невозможно, возвращает `False`. Поддерживает преобразование объектов, словарей, списков, кортежей, множеств и базовых типов данных.

**Параметры**:
- `any_data` (Any): Любой тип данных.

**Возвращает**:
- `dict | list | int | float | str | bool | None | False`: Словарь, представляющий входные данные, список, базовый тип данных или `False`, если преобразование невозможно.

**Пример использования:**
```python
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

import types
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
```