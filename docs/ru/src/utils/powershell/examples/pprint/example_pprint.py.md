# Документация для модуля `example_pprint.py`

## Обзор

Модуль `example_pprint.py` демонстрирует использование различных функций pretty print для форматирования вывода данных. Включает примеры использования как стандартной библиотеки `pprint`, так и кастомной функции `pprint` из модуля `src.printer`.

## Подробней

Этот модуль предназначен для демонстрации возможностей форматированного вывода данных в Python. Он импортирует стандартную библиотеку `pprint` как `pretty_print` и кастомную функцию `pprint` из `src.printer`. Затем используется кастомная функция `pprint` для вывода строки "Hello, world!".

## Функции

### `pprint` (из модуля `src.printer`)

```python
def pprint(obj: object, stream: Optional[typing.TextIO] = None, indent: int = 1, width: int = 80, depth: Optional[int] = None, *, compact: bool = False, sort_dicts: bool = False, underscore_numbers: bool = False) -> None:
    """
    Форматированный вывод объекта на экран или в поток.

    Args:
        obj (object): Объект для вывода.
        stream (Optional[typing.TextIO], optional): Поток для вывода. По умолчанию `None` (стандартный вывод).
        indent (int, optional): Отступ для форматирования. По умолчанию 1.
        width (int, optional): Максимальная ширина строки. По умолчанию 80.
        depth (Optional[int], optional): Максимальная глубина для рекурсивного вывода. По умолчанию `None` (без ограничений).
        compact (bool, optional): Компактный вывод. По умолчанию `False`.
        sort_dicts (bool, optional): Сортировать словари по ключам. По умолчанию `False`.
        underscore_numbers (bool, optional): Подчеркивать числа. По умолчанию `False`.

    Returns:
        None

    Как работает функция:
     1. Функция принимает объект `obj` для форматированного вывода.
     2. Использует модуль `pprint` для форматирования объекта в соответствии с заданными параметрами, такими как отступ, ширина, глубина и т.д.
     3. Выводит отформатированный объект в указанный поток (по умолчанию, стандартный вывод).

    ASCII flowchart:
    Объект -> [pprint.pprint] -> Вывод в поток

    Примеры:
        >>> pprint("Hello, world!")
        Hello, world!
    """
    ...
```
**Методы**:
- Нет

**Параметры**:
- `obj` (object): Объект для вывода.
- `stream` (Optional[typing.TextIO], optional): Поток для вывода. По умолчанию `None` (стандартный вывод).
- `indent` (int, optional): Отступ для форматирования. По умолчанию 1.
- `width` (int, optional): Максимальная ширина строки. По умолчанию 80.
- `depth` (Optional[int], optional): Максимальная глубина для рекурсивного вывода. По умолчанию `None` (без ограничений).
- `compact` (bool, optional): Компактный вывод. По умолчанию `False`.
- `sort_dicts` (bool, optional): Сортировать словари по ключам. По умолчанию `False`.
- `underscore_numbers` (bool, optional): Подчеркивать числа. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет

**Примеры**:

```python
pprint("Hello, world!")
```
```