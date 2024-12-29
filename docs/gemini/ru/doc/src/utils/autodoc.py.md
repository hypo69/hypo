# Модуль `src.utils.autodoc`

## Обзор

Модуль `src.utils.autodoc` предоставляет функциональность для автоматического обновления строк документации (`docstring`) функций с использованием декоратора `autodoc`. Это позволяет добавлять информацию о времени последнего вызова функции в её документацию.

## Оглавление
  
- [Обзор](#обзор)
- [Функции](#функции)
  - [`autodoc`](#autodoc)
  - [`update_docstring`](#update_docstring)
- [Пример использования](#пример-использования)

## Функции

### `autodoc`

**Описание**: Декоратор для автоматического обновления docstring функции.

**Параметры**:
- `func` (function): Функция, для которой необходимо обновить docstring.

**Возвращает**:
- `function`: Обернутая функция с обновленным docstring.

### `update_docstring`

**Описание**: Обновляет docstring функции, добавляя информацию о времени последнего вызова.

**Параметры**:
- `func` (function): Функция, docstring которой нужно обновить.

**Возвращает**:
- `None`: Функция не возвращает значение, она изменяет docstring переданной функции.

## Пример использования

```python
@autodoc
def example_function(param1: int, param2: str) -> None:
    """Пример функции.

    Args:
        param1 (int): Первое значение.
        param2 (str): Второе значение.
    """
    print(f"Processing {param1} and {param2}")

# Тестирование функции
example_function(1, "test")
print(example_function.__doc__)
example_function(2, "another test")
print(example_function.__doc__)
```