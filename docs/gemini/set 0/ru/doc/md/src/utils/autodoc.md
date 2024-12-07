# Модуль hypotez/src/utils/autodoc.py

## Обзор

Этот модуль содержит декоратор `autodoc`, который обновляет строку документации функции с добавлением времени последнего вызова функции. Декоратор используется для автоматического обновления docstring функции при ее вызове.  Декоратор оборачивает функцию, обновляя ее docstring перед вызовом, добавляя в него строку с текущим временем.

## Функции

### `autodoc`

**Описание**: Декоратор для автоматического обновления docstring функции.

**Параметры**:
- Нет

**Возвращает**:
- Функцию, обернутую декоратором.


**Подробное описание**: Декоратор `autodoc` принимает функцию в качестве аргумента и возвращает обернутую функцию `wrapper`.  Функция `wrapper` обновляет docstring исходной функции перед ее вызовом, добавляя в него строку с текущим временем.

### `update_docstring`

**Описание**: Обновляет docstring функции, добавляя информацию о времени последнего вызова.

**Параметры**:
- `func` (функция): Функция, чья строка документации должна быть обновлена.

**Возвращает**:
- Нет (None)


**Подробное описание**: Функция `update_docstring` обновляет docstring функции `func`, добавляя строку с текущим временем в формате "YYYY-MM-DD HH:MM:SS". Если у функции не было docstring, функция создает новый с текущим временем.

### `example_function`

**Описание**: Пример функции, использующей декоратор `autodoc`.

**Параметры**:
- `param1` (int): Первое значение.
- `param2` (str): Второе значение.

**Возвращает**:
- None

**Подробное описание**: Функция `example_function` печатает сообщение с параметрами `param1` и `param2`. При каждом вызове ее docstring обновляется, содержа в себе информацию о времени последнего вызова.

## Использование

Для использования декоратора `autodoc` необходимо импортировать его и поместить перед функцией, которую требуется документировать. При вызове функции `example_function` ее docstring будет автоматически обновляться, содержа в себе информацию о времени последнего вызова.

```python
@autodoc
def example_function(param1: int, param2: str) -> None:
    """Пример функции.

    Args:
        param1 (int): Первое значение.
        param2 (str): Второе значение.
    """
    print(f"Processing {param1} and {param2}")

example_function(1, "test")
print(example_function.__doc__)  # Вывод обновленного docstring
example_function(2, "another test")
print(example_function.__doc__)  # Вывод обновленного docstring
```

##  Примечания

- Модуль использует библиотеку `time` для получения текущего времени.
- Декоратор `functools.wraps` используется для сохранения метаданных оригинальной функции.
- Пример использования декоратора и вывод обновленного docstring демонстрирует работу декоратора `autodoc`.


```
```
```python