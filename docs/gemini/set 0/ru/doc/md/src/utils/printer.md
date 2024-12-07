# Модуль `hypotez/src/utils/printer.py`

## Обзор

Данный модуль предоставляет функции для красивой печати данных с возможностью стилизации текста, включая цвет, фон и шрифты. Он поддерживает печать словарей, списков, строк и файлов (с расширениями .csv и .xls).

## Функции

### `_color_text`

**Описание**: Функция для применения стилей цвета, фона и шрифта к тексту. Использует ANSI escape codes для изменения отображения текста.

**Параметры**:

- `text` (str): Текст, к которому нужно применить стили.
- `text_color` (str, optional): Цвет текста. По умолчанию пустая строка (нет цвета). Допустимые значения: `red`, `green`, `blue`, `yellow`, `white`.
- `bg_color` (str, optional): Цвет фона. По умолчанию пустая строка (нет фона). Допустимые значения: `bg_red`, `bg_green`.
- `font_style` (str, optional): Стиль шрифта. По умолчанию пустая строка (нет стиля). Допустимые значения: `bold`, `underline`.

**Возвращает**:

- str: Стилизованный текст.

**Примеры**:

```python
_color_text("Hello, World!", text_color="green", font_style="bold")
```

### `pprint`

**Описание**: Функция для красивой печати данных с опциональной стилизацией. Поддерживает различные типы данных: словари, списки, строки и пути к файлам.

**Параметры**:

- `print_data` (Any, optional): Данные для печати. Может быть `None`, `dict`, `list`, `str` или `Path`.
- `text_color` (str, optional): Цвет текста. По умолчанию `white`. Доступные цвета указаны в словаре `TEXT_COLORS`.
- `bg_color` (str, optional): Цвет фона. По умолчанию пустая строка. Доступные цвета указаны в словаре `BG_COLORS`.
- `font_style` (str, optional): Стиль шрифта. По умолчанию пустая строка. Доступные стили указаны в словаре `FONT_STYLES`.

**Возвращает**:

- None

**Вызывает исключения**:

- `Exception`: Возникает при ошибках обработки данных или неподдерживаемых типах данных.


**Примеры**:

```python
pprint({"name": "Alice", "age": 30}, text_color="green")
pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
```

## Константы

- `MODE`: Строка, определяющая режим работы. В данном примере она имеет значение `'dev'`.

- `TEXT_COLORS`: Словарь, содержащий ANSI escape codes для различных цветов текста.

- `BG_COLORS`: Словарь, содержащий ANSI escape codes для различных цветов фона.

- `FONT_STYLES`: Словарь, содержащий ANSI escape codes для различных стилей шрифта.

- `RESET`: ANSI escape code для сброса стилей.


## Модули, импортированные в модуле

- `json`
- `csv`
- `pandas as pd`
- `pathlib`
- `typing`
- `pprint`


## Поддержка файлов

Функция `pprint` обрабатывает файлы с расширениями `.csv` и `.xls`. Для других типов файлов выдается сообщение об ошибке.


## Ошибки (ex)

В блоке `try...except` обрабатываются потенциальные ошибки при работе с разными типами данных. Если возникает ошибка, то выводится сообщение об ошибке с указанием цвета красного.