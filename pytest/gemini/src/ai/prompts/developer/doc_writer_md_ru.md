# Модуль: `doc_writer_md`

Этот модуль содержит вспомогательные функции для генерации Markdown-документации для Python-кода.

## Примеры использования

```python
# Пример генерации документации для функции
from doc_writer_md import generate_docstring

def my_function(a, b):
    """Функция для сложения двух чисел."""
    return a + b

docstring = generate_docstring(my_function)
print(docstring)
```

## Платформы
- Python 3.8+


## Функции

### `generate_docstring(func)`

Генерирует строку документации в формате Markdown для переданной функции.

#### Параметры
- `func`: Функция, для которой требуется сгенерировать строку документации.

#### Возвращаемое значение
- Строка Markdown-документации.


### `generate_class_docstring(cls)`

Генерирует строку документации в формате Markdown для переданного класса.

#### Параметры
- `cls`: Класс, для которого требуется сгенерировать строку документации.

#### Возвращаемое значение
- Строка Markdown-документации.


```python
# Пример использования generate_class_docstring
class MyClass:
    def __init__(self, x):
        """Инициализирует объект класса."""
        self.x = x

    def my_method(self, y):
        """Вычисляет сумму x и y."""
        return self.x + y


docstring = generate_class_docstring(MyClass)
print(docstring)
```

```python
# Пример использования generate_module_docstring для модуля
import my_module

docstring = generate_module_docstring(my_module)
print(docstring)

```
```python
# Пример использования generate_function_docstring для функции
def add_numbers(x, y):
  """Складывает два числа."""
  return x + y

docstring = generate_function_docstring(add_numbers)
print(docstring)
```


```python
import pytest
from doc_writer_md import generate_docstring # Импортируем функцию для тестирования

def test_generate_docstring_valid_function():
    """Проверяет генерацию документации для корректной функции."""
    def my_func(a, b):
        """Функция, возвращающая сумму a и b."""
        return a + b

    expected_docstring = """
# Функция: my_func

Функция, возвращающая сумму a и b.


## Параметры
- a: первое число.
- b: второе число.


## Возвращаемое значение
- Сумма a и b.
"""
    actual_docstring = generate_docstring(my_func)
    assert expected_docstring in actual_docstring
```
```python
import pytest
from doc_writer_md import generate_class_docstring # Импортируем функцию для тестирования


class MyClass:
    def __init__(self, x):
        """Инициализирует объект класса."""
        self.x = x
        
    def method1(self, y):
        """Возвращает сумму x и y."""
        return self.x + y


def test_generate_class_docstring_valid_class():
    expected_docstring = """# Класс: MyClass

Класс MyClass.


## Методы
### __init__
Инициализирует объект класса.

#### Параметры
- x: Значение для атрибута x.

### method1
Возвращает сумму x и y.

#### Параметры
- y: значение для y.

#### Возвращаемое значение
Сумма x и y.
"""
    actual_docstring = generate_class_docstring(MyClass)
    assert expected_docstring in actual_docstring
```

```
```
```
```
```
```

```
```