# Модуль `src.utils.printer`

## Обзор

Модуль `src.utils.printer` предоставляет утилиты для форматированного вывода данных в консоль, включая стилизацию текста с использованием цветов, фона и шрифтов.

## Подробней

Модуль содержит функции для красивого и структурированного вывода информации, что может быть полезно для отладки, логирования и представления данных в удобном для восприятия виде.  Функция `pprint` позволяет выводить различные типы данных (словари, списки, строки) с применением цветового оформления и стилей. Цветовые коды и стили задаются через ANSI escape-последовательности.

## Константы

### `RESET`
```python
RESET = "\\033[0m"
```
Код ANSI escape, используемый для сброса всех стилей текста к значениям по умолчанию.

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
Словарь, содержащий ANSI escape-коды для различных цветов текста.  Ключи словаря - названия цветов (например, `"red"`, `"green"`), значения - соответствующие ANSI escape-коды.

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
Словарь, содержащий ANSI escape-коды для различных цветов фона. Ключи словаря - названия цветов фона (например, `"bg_red"`, `"bg_green"`), значения - соответствующие ANSI escape-коды.

### `FONT_STYLES`
```python
FONT_STYLES = {
    "bold": "\\033[1m",
    "underline": "\\033[4m",
}
```
Словарь, содержащий ANSI escape-коды для различных стилей шрифта. Ключи словаря - названия стилей (например, `"bold"`, `"underline"`), значения - соответствующие ANSI escape-коды.

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
    ...
```

**Назначение**: Применяет цвет, фон и стиль шрифта к заданному тексту с использованием ANSI escape-кодов.

**Параметры**:
- `text` (str): Текст, к которому необходимо применить стили.
- `text_color` (str, optional): Цвет текста. По умолчанию пустая строка (без цвета).
- `bg_color` (str, optional): Цвет фона. По умолчанию пустая строка (без фона).
- `font_style` (str, optional): Стиль шрифта. По умолчанию пустая строка (без стиля).

**Возвращает**:
- `str`: Строка с примененными стилями.

**Как работает функция**:

Функция `_color_text` принимает текст и опциональные параметры для цвета текста, цвета фона и стиля шрифта.  Она формирует строку, добавляя в начало и конец текста соответствующие ANSI escape-коды для установки и сброса стилей. Если какой-либо из параметров стиля не указан, он не включается в результирующую строку.

1. **Сборка стилей**: Функция получает значения стилей (`font_style`, `text_color`, `bg_color`).
2. **Формирование строки**: Функция объединяет стили с текстом, добавляя в начало строки коды стилей, а в конец - код сброса стилей (`RESET`).
3. **Возврат результата**: Функция возвращает строку с примененными стилями.

**Примеры**:

```python
_color_text("Hello, World!", text_color="green", font_style="bold")
# Результат: '\033[1m\033[32mHello, World!\033[0m'
```

### `pprint`

```python
def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Pretty prints the given data with optional color, background, and font style.

    This function formats the input data based on its type and prints it to the console. The data is printed with optional 
    text color, background color, and font style based on the specified parameters. The function can handle dictionaries, 
    lists, strings, and file paths.

    :param print_data: The data to be printed. Can be of type ``None``, ``dict``, ``list``, ``str``, or ``Path``.\n
    :param text_color: The color to apply to the text. Default is \'white\'. See :ref:`TEXT_COLORS`.\n
    :param bg_color: The background color to apply to the text. Default is \'\' (no background color). See :ref:`BG_COLORS`.\n
    :param font_style: The font style to apply to the text. Default is \'\' (no font style). See :ref:`FONT_STYLES`.\n
    :return: None

    :raises: Exception if the data type is unsupported or an error occurs during printing.

    :example:\n
        >>> pprint({"name": "Alice", "age": 30}, text_color="green")\n
        \\033[32m{\n
            "name": "Alice",\n
            "age": 30\n
        }\\033[0m\n

        >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")\n
        \\033[34m\\033[1mapple\\033[0m\n
        \\033[34m\\033[1mbanana\\033[0m\n
        \\033[34m\\033[1mcherry\\033[0m\n

        >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")\n
        \\033[4m\\033[33m\\033[41mtext example\\033[0m\n
    """
    ...
```

**Назначение**:  Форматированный вывод данных в консоль с возможностью стилизации текста.

**Параметры**:
- `print_data` (Any, optional): Данные для вывода. Может быть `None`, словарем, списком, строкой или путем к файлу. По умолчанию `None`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"white"`. См. `TEXT_COLORS`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""` (без фона). См. `BG_COLORS`.
- `font_style` (str, optional): Стиль шрифта. По умолчанию `""` (без стиля). См. `FONT_STYLES`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если тип данных не поддерживается или произошла ошибка при выводе.

**Как работает функция**:

Функция `pprint` принимает данные различных типов и выводит их в консоль с применением опционального форматирования (цвет, фон, стиль шрифта). Она определяет тип входных данных и применяет соответствующую обработку для форматированного вывода.

```
A: Проверка print_data на None
|
B: Обработка text_color, bg_color, font_style
|
C: Проверка типа print_data
|
+- D1: print_data - словарь -> Форматирование JSON и вывод
|
+- D2: print_data - список -> Вывод каждого элемента с применением стилей
|
+- D3: print_data - строка или Path -> Проверка на файл и его расширение
|  |
|  +- E1: Файл CSV/XLS -> Вывод предупреждения о поддержке только для чтения
|  |
|  +- E2: Другой тип файла -> Вывод предупреждения о неподдерживаемом типе
|
+- D4: print_data - другой тип -> Преобразование в строку и вывод
|
F: Обработка исключений -> Вывод сообщения об ошибке
```

**Примеры**:

```python
pprint({"name": "Alice", "age": 30}, text_color="green")
# Результат: 
# \033[32m{
#     "name": "Alice",
#     "age": 30
# }\033[0m

pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
# Результат:
# \033[34m\033[1mapple\033[0m
# \033[34m\033[1mbanana\033[0m
# \033[34m\033[1mcherry\033[0m

pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
# Результат: \033[4m\033[33m\033[41mtext example\033[0m