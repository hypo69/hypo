# Модуль `src.utils.printer`

## Обзор

Модуль `src.utils.printer` предоставляет утилиты для форматированного вывода данных и стилизации текста. Он включает функции для печати данных в удобном для чтения формате с возможностью добавления стилей текста, таких как цвет, фон и шрифт.

## Подробней

Этот модуль предназначен для улучшения читаемости выводимых данных в консоли, особенно при отладке и мониторинге работы программ. Он использует ANSI escape-коды для добавления цветов и стилей к тексту, что позволяет выделить важную информацию и сделать вывод более наглядным. Модуль содержит функции для стилизации текста и форматированного вывода различных типов данных, таких как словари, списки и строки.

## Содержание

- [Константы](#константы)
  - [RESET](#reset)
  - [TEXT_COLORS](#text_colors)
  - [BG_COLORS](#bg_colors)
  - [FONT_STYLES](#font_styles)
- [Функции](#функции)
  - [_color_text](#_color_text)
  - [pprint](#pprint)

## Константы

### `RESET`

```python
RESET = "\\033[0m"
```

Код ANSI escape для сброса всех стилей текста.

### `TEXT_COLORS`

```python
TEXT_COLORS = {
    "red": "\\033[31m",
    "green": "\\033[32m",
    "blue": "\\033[34m",
    "yellow": "\\033[33m",
    "white": "\\033[37m",
    "cyan": "\\033[36m",
    "magenta": "\\033[35m",
    "light_gray": "\\033[37m",
    "dark_gray": "\\033[90m",
    "light_red": "\\033[91m",
    "light_green": "\\033[92m",
    "light_blue": "\\033[94m",
    "light_yellow": "\\033[93m",
}
```

Словарь, содержащий коды ANSI escape для различных цветов текста.

### `BG_COLORS`

```python
BG_COLORS = {
    "bg_red": "\\033[41m",
    "bg_green": "\\033[42m",
    "bg_blue": "\\033[44m",
    "bg_yellow": "\\033[43m",
    "bg_white": "\\033[47m",
    "bg_cyan": "\\033[46m",
    "bg_magenta": "\\033[45m",
    "bg_light_gray": "\\033[47m",
    "bg_dark_gray": "\\033[100m",
    "bg_light_red": "\\033[101m",
    "bg_light_green": "\\033[102m",
    "bg_light_blue": "\\033[104m",
    "bg_light_yellow": "\\033[103m",
}
```

Словарь, содержащий коды ANSI escape для различных цветов фона.

### `FONT_STYLES`

```python
FONT_STYLES = {
    "bold": "\\033[1m",
    "underline": "\\033[4m",
}
```

Словарь, содержащий коды ANSI escape для различных стилей шрифта.

## Функции

### `_color_text`

```python
def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """Применяет цвет, фон и стиль шрифта к тексту.

    Эта вспомогательная функция применяет указанные стили цвета и шрифта к заданному тексту, используя ANSI escape-коды.

    Args:
        text (str): Текст, к которому нужно применить стили.
        text_color (str): Цвет текста. По умолчанию пустая строка, что означает отсутствие цвета.
        bg_color (str): Цвет фона. По умолчанию пустая строка, что означает отсутствие цвета фона.
        font_style (str): Стиль шрифта. По умолчанию пустая строка, что означает отсутствие стиля шрифта.

    Returns:
        str: Текст со стилями.

    Example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        '\033[1m\033[32mHello, World!\033[0m'
    """
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"
```

**Назначение**: Применение стилей (цвет текста, цвет фона, стиль шрифта) к заданной строке текста с использованием ANSI escape-кодов.

**Как работает функция**:
Функция принимает строку текста и опциональные параметры для цвета текста, цвета фона и стиля шрифта. Она формирует строку, содержащую ANSI escape-коды для указанных стилей, добавляет текст и завершает строку кодом сброса стилей. Если какой-либо стиль не указан, соответствующий ANSI escape-код не добавляется.

**Параметры**:
- `text` (str): Текст, к которому необходимо применить стили.
- `text_color` (str): Цвет текста. Значение по умолчанию - пустая строка (без цвета).
- `bg_color` (str): Цвет фона. Значение по умолчанию - пустая строка (без цвета фона).
- `font_style` (str): Стиль шрифта. Значение по умолчанию - пустая строка (без стиля шрифта).

**Возвращает**:
- `str`: Строка текста, к которой применены указанные стили.

**Примеры**:
- Пример вызова с цветом текста и стилем шрифта:

```python
_color_text("Hello, World!", text_color="green", font_style="bold")
# Возвращает: '\033[1m\033[32mHello, World!\033[0m'
```

### `pprint`

```python
def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Форматированный вывод данных с дополнительным цветом, фоном и стилем шрифта.

    Эта функция форматирует входные данные в зависимости от их типа и выводит их в консоль. Данные выводятся с дополнительным
    цветом текста, цветом фона и стилем шрифта на основе указанных параметров. Функция может обрабатывать словари,
    списки, строки и пути к файлам.

    Args:
        print_data (Any, optional): Данные для вывода. Может быть `None`, `dict`, `list`, `str` или `Path`.
        text_color (str, optional): Цвет текста. По умолчанию 'white'. См. `TEXT_COLORS`.
        bg_color (str, optional): Цвет фона. По умолчанию '' (без цвета фона). См. `BG_COLORS`.
        font_style (str, optional): Стиль шрифта. По умолчанию '' (без стиля шрифта). См. `FONT_STYLES`.

    Returns:
        None

    Raises:
        Exception: Если тип данных не поддерживается или во время вывода возникает ошибка.

    Example:
        >>> pprint({"name": "Alice", "age": 30}, text_color="green")
        \033[32m{
            "name": "Alice",
            "age": 30
        }\033[0m

        >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
        \033[34m\033[1mapple\033[0m
        \033[34m\033[1mbanana\033[0m
        \033[34m\033[1mcherry\033[0m

        >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
        \033[4m\033[33m\033[41mtext example\033[0m
    """
    if not print_data:
        return
    if isinstance(text_color, str):
        text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    if isinstance(bg_color, str):
        bg_color = BG_COLORS.get(bg_color.lower(), "")
    if isinstance(font_style, str):
        font_style = FONT_STYLES.get(font_style.lower(), "")


    try:
        if isinstance(print_data, dict):
            print(_color_text(json.dumps(print_data, indent=4), text_color))
        elif isinstance(print_data, list):
            for item in print_data:
                print(_color_text(str(item), text_color))
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            ext = Path(print_data).suffix.lower()
            if ext in ['.csv', '.xls']:
                print(_color_text("File reading supported for .csv, .xls only.", text_color))
            else:
                print(_color_text("Unsupported file type.", text_color))
        else:
            print(_color_text(str(print_data), text_color))
    except Exception as ex:
        print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"]))
```

**Назначение**: Вывод данных в консоль с применением указанных стилей текста, таких как цвет, фон и шрифт. Функция обрабатывает различные типы данных, включая словари, списки, строки и пути к файлам.

**Как работает функция**:
Функция `pprint` принимает данные для вывода и опциональные параметры для цвета текста, цвета фона и стиля шрифта. В зависимости от типа данных, она применяет соответствующее форматирование и стилизацию. Если данные являются словарем, они преобразуются в JSON-строку с отступами. Если данные являются списком, каждый элемент списка выводится отдельно. Если данные являются строкой или путем к файлу, функция проверяет расширение файла и выводит сообщение о поддержке только для `.csv` и `.xls` файлов. В случае возникновения ошибки при обработке данных, функция выводит сообщение об ошибке красным цветом.

**Параметры**:
- `print_data` (Any, optional): Данные для вывода. Может быть любого типа, но наиболее часто используются `dict`, `list`, `str` или `Path`. Значение по умолчанию - `None`.
- `text_color` (str, optional): Цвет текста. Значение по умолчанию - `"white"`.
- `bg_color` (str, optional): Цвет фона. Значение по умолчанию - `""` (без цвета фона).
- `font_style` (str, optional): Стиль шрифта. Значение по умолчанию - `""` (без стиля шрифта).

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Возникает, если тип данных не поддерживается или во время вывода возникает ошибка.

**Примеры**:
- Пример вызова с выводом словаря зеленым цветом:

```python
pprint({"name": "Alice", "age": 30}, text_color="green")
# Вывод в консоль:
# \033[32m{
#     "name": "Alice",
#     "age": 30
# }\033[0m
```

- Пример вызова с выводом списка синим цветом и жирным шрифтом:

```python
pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
# Вывод в консоль:
# \033[34m\033[1mapple\033[0m
# \033[34m\033[1mbanana\033[0m
# \033[34m\033[1mcherry\033[0m
```

- Пример вызова с выводом текста желтым цветом, красным фоном и подчеркиванием:

```python
pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
# Вывод в консоль:
# \033[4m\033[33m\033[41mtext example\033[0m
```