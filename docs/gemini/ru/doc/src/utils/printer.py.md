# src.utils.printer

## Обзор

Модуль `src.utils.printer` предоставляет утилиты для красивого вывода данных с возможностью стилизации текста, включая цвет, фон и стиль шрифта.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Функции](#функции)
    - [`_color_text`](#_color_text)
    - [`pprint`](#pprint)

## Константы

### `RESET`
Сброс ANSI escape кодов.

### `TEXT_COLORS`
Словарь, содержащий ANSI escape коды для различных цветов текста.

### `BG_COLORS`
Словарь, содержащий ANSI escape коды для различных фоновых цветов.

### `FONT_STYLES`
Словарь, содержащий ANSI escape коды для различных стилей шрифта (например, жирный, подчеркнутый).

## Функции

### `_color_text`

**Описание**:
Применяет цвет, фон и стиль шрифта к тексту.

**Параметры**:
- `text` (str): Текст, к которому применяется стиль.
- `text_color` (str, optional): Цвет текста. По умолчанию пустая строка (без цвета).
- `bg_color` (str, optional): Цвет фона. По умолчанию пустая строка (без фона).
- `font_style` (str, optional): Стиль шрифта. По умолчанию пустая строка (без стиля).

**Возвращает**:
- `str`: Стилизованный текст.

**Пример**:
```python
_color_text("Hello, World!", text_color="green", font_style="bold")
# => '\033[1m\033[32mHello, World!\033[0m'
```

### `pprint`

**Описание**:
Красиво выводит данные с возможностью применения цвета, фона и стиля шрифта.

**Параметры**:
- `print_data` (Any, optional): Данные для вывода. Может быть `None`, `dict`, `list`, `str` или `Path`. По умолчанию `None`.
- `text_color` (str, optional): Цвет текста. По умолчанию `white`. См. `TEXT_COLORS`.
- `bg_color` (str, optional): Цвет фона. По умолчанию пустая строка (без фона). См. `BG_COLORS`.
- `font_style` (str, optional): Стиль шрифта. По умолчанию пустая строка (без стиля). См. `FONT_STYLES`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если тип данных не поддерживается или происходит ошибка при выводе.

**Пример**:
```python
pprint({"name": "Alice", "age": 30}, text_color="green")
# Выведет: \033[32m{
#             "name": "Alice",
#             "age": 30
#         }\033[0m

pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
# Выведет: \033[34m\033[1mapple\033[0m
#          \033[34m\033[1mbanana\033[0m
#          \033[34m\033[1mcherry\033[0m

pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
# Выведет: \033[4m\033[33m\033[41mtext example\033[0m
```