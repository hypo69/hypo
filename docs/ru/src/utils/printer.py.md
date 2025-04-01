# Модуль `src.utils.printer`

## Обзор

Модуль `src.utils.printer` предоставляет утилиты для форматирования и стилизации текста при выводе в консоль. Он позволяет применять различные цвета, фоны и стили шрифтов к тексту, делая вывод более читаемым и информативным. Модуль включает функции для обработки различных типов данных, таких как словари, списки и строки, а также для чтения данных из файлов.

## Подробнее

Модуль содержит функции для стилизации текста с использованием ANSI escape-кодов, что позволяет изменять цвет текста, фона и стиль шрифта. Это полезно для выделения важной информации или разделения различных типов сообщений в консоли.

## Содержание

1.  [Переменные](#Переменные)
2.  [Функции](#Функции)
    *   [`_color_text`](#_color_text)
    *   [`pprint`](#pprint)

## Переменные

### `RESET`

```python
RESET = "\\033[0m"
```

Код ANSI escape для сброса всех стилей текста. Используется для возврата к стандартному стилю консоли после применения стилей.

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

Словарь, содержащий коды ANSI escape для различных цветов текста. Ключи словаря — названия цветов, значения — соответствующие коды.

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

Словарь, содержащий коды ANSI escape для различных цветов фона. Ключи словаря — названия цветов фона, значения — соответствующие коды.

### `FONT_STYLES`

```python
FONT_STYLES = {
    "bold": "\\033[1m",
    "underline": "\\033[4m",
}
```

Словарь, содержащий коды ANSI escape для различных стилей шрифта. Ключи словаря — названия стилей шрифта, значения — соответствующие коды.

## Функции

### `_color_text`

```python
def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """Apply color, background, and font styling to the text.

    This helper function applies the provided color and font styles to the given text using ANSI escape codes.

    :param text: The text to be styled.
    :param text_color: The color to apply to the text. Default is an empty string, meaning no color.
    :param bg_color: The background color to apply. Default is an empty string, meaning no background color.
    :param font_style: The font style to apply to the text. Default is an empty string, meaning no font style.
    :return: The styled text as a string.

    :example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        \'\\033[1m\\033[32mHello, World!\\033[0m\'
    """
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"
```

Применяет цвет, фон и стиль шрифта к тексту.

**Параметры**:

*   `text` (str): Текст, к которому необходимо применить стили.
*   `text_color` (str, optional): Цвет текста. По умолчанию "".
*   `bg_color` (str, optional): Цвет фона. По умолчанию "".
*   `font_style` (str, optional): Стиль шрифта. По умолчанию "".

**Возвращает**:

*   str: Стилизованный текст.

**Как работает функция**:

1.  Функция принимает текст и опциональные параметры для цвета текста, цвета фона и стиля шрифта.
2.  Формирует строку, включающую ANSI escape-коды для указанных стилей, текст и код сброса стилей (`RESET`).
3.  Возвращает стилизованную строку.

**ASCII Flowchart**:

```
    Начало
     ↓
  Применение стилей (цвет, фон, шрифт)
     ↓
  Формирование стилизованной строки
     ↓
    Возврат стилизованной строки
     ↓
    Конец
```

**Примеры**:

```python
_color_text("Hello, World!", text_color="green", font_style="bold")
# Возвращает: '\033[1m\033[32mHello, World!\033[0m'

_color_text("Example", text_color="red")
# Возвращает: '\033[31mExample\033[0m'

_color_text("Text with background", bg_color="bg_yellow")
# Возвращает: '\033[43mText with background\033[0m'
```

### `pprint`

```python
def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Pretty prints the given data with optional color, background, and font style.

    This function formats the input data based on its type and prints it to the console. The data is printed with optional 
    text color, background color, and font style based on the specified parameters. The function can handle dictionaries, 
    lists, strings, and file paths.

    :param print_data: The data to be printed. Can be of type ``None``, ``dict``, ``list``, ``str``, or ``Path``.\n
    :param text_color: The color to apply to the text. Default is \'white\'. See :ref:`TEXT_COLORS`.
    :param bg_color: The background color to apply to the text. Default is \'\' (no background color). See :ref:`BG_COLORS`.
    :param font_style: The font style to apply to the text. Default is \'\' (no font style). See :ref:`FONT_STYLES`.
    :return: None

    :raises: Exception if the data type is unsupported or an error occurs during printing.

    :example:
        >>> pprint({"name": "Alice", "age": 30}, text_color="green")
        \\033[32m{\n
            "name": "Alice",\n
            "age": 30\n
        }\\033[0m

        >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
        \\033[34m\\033[1mapple\\033[0m
        \\033[34m\\033[1mbanana\\033[0m
        \\033[34m\\033[1mcherry\\033[0m

        >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
        \\033[4m\\033[33m\\033[41mtext example\\033[0m
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

Выводит данные в консоль с применением стилизации.

**Параметры**:

*   `print_data` (Any, optional): Данные для вывода. Может быть `None`, `dict`, `list`, `str` или `Path`. По умолчанию `None`.
*   `text_color` (str, optional): Цвет текста. По умолчанию "white".
*   `bg_color` (str, optional): Цвет фона. По умолчанию "".
*   `font_style` (str, optional): Стиль шрифта. По умолчанию "".

**Возвращает**:

*   None

**Как работает функция**:

1.  Функция принимает данные для вывода и опциональные параметры для цвета текста, цвета фона и стиля шрифта.
2.  Если `print_data` равно `None`, функция завершается.
3.  Преобразует строковые значения `text_color`, `bg_color` и `font_style` в соответствующие ANSI escape-коды, используя словари `TEXT_COLORS`, `BG_COLORS` и `FONT_STYLES`.
4.  В зависимости от типа данных `print_data` выполняет следующие действия:
    *   Если это словарь, преобразует его в строку JSON с отступами и применяет стилизацию.
    *   Если это список, выводит каждый элемент списка с применением стилизации.
    *   Если это строка или путь к файлу, проверяет расширение файла и выводит сообщение о поддержке только для `.csv` и `.xls`, либо сообщает о неподдерживаемом типе файла.
    *   В остальных случаях преобразует данные в строку и применяет стилизацию.
5.  Обрабатывает исключения, которые могут возникнуть в процессе вывода, и выводит сообщение об ошибке красным цветом.

**ASCII Flowchart**:

```
    Начало
     ↓
  Проверка print_data на None
     ↓
  Преобразование text_color, bg_color, font_style в ANSI escape-коды
     ↓
  Определение типа данных print_data
     ├── dict: Преобразование в JSON и стилизация
     ├── list: Вывод каждого элемента с стилизацией
     ├── str/Path: Проверка расширения файла и вывод сообщения
     └── Другое: Преобразование в строку и стилизация
     ↓
  Обработка исключений
     ↓
    Конец
```

**Примеры**:

```python
pprint({"name": "Alice", "age": 30}, text_color="green")
# Выводит:
# \033[32m{
#     "name": "Alice",
#     "age": 30
# }\033[0m

pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
# Выводит:
# \033[34m\033[1mapple\033[0m
# \033[34m\033[1mbanana\033[0m
# \033[34m\033[1mcherry\033[0m

pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
# Выводит: \033[4m\033[33m\033[41mtext example\033[0m