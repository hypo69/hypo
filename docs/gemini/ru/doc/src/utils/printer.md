# Модуль `hypotez/src/utils/printer.py`

## Обзор

Модуль `hypotez/src/utils/printer.py` предоставляет функции для красивого вывода данных в удобочитаемом формате с опциональным стилизованным текстом, включая цвет, фон и шрифты.  Модуль поддерживает вывод словарей, списков, строк и файлов с расширениями `.csv` и `.xls`.

## Функции

### `_color_text`

**Описание**: Функция применяет стилизацию цвета, фона и шрифта к тексту.  Использует ANSI escape коды для изменения отображения текста.

**Параметры**:
- `text` (str): Текст, которому необходимо применить стилизацию.
- `text_color` (str, опционально): Цвет текста. По умолчанию пустая строка (нет цвета).  Доступные цвета перечислены в словаре `TEXT_COLORS`.
- `bg_color` (str, опционально): Цвет фона. По умолчанию пустая строка (нет фона). Доступные цвета перечислены в словаре `BG_COLORS`.
- `font_style` (str, опционально): Стиль шрифта. По умолчанию пустая строка (нет стиля). Доступные стили перечислены в словаре `FONT_STYLES`.

**Возвращает**:
- str: Стилизованный текст.

**Пример**:
```python
>>> _color_text("Hello, World!", text_color="green", font_style="bold")
'\033[1m\033[32mHello, World!\033[0m'
```

### `pprint`

**Описание**: Красиво выводит данные с опциональной стилизацией цвета, фона и шрифта. Функция форматирует данные в зависимости от их типа и выводит их в консоль.

**Параметры**:
- `print_data` (Any, опционально): Данные для вывода. Может быть `None`, `dict`, `list`, `str` или `Path`.
- `text_color` (str, опционально): Цвет текста. По умолчанию "white". См. словарь `TEXT_COLORS`.
- `bg_color` (str, опционально): Цвет фона. По умолчанию пустая строка (нет фона). См. словарь `BG_COLORS`.
- `font_style` (str, опционально): Стиль шрифта. По умолчанию пустая строка (нет стиля). См. словарь `FONT_STYLES`.


**Возвращает**:
- None

**Вызывает исключения**:
- `Exception`: Возникает при ошибках обработки данных или при unsupported типе данных.


**Пример**:
```python
>>> pprint({"name": "Alice", "age": 30}, text_color="green")
{
    "name": "Alice",
    "age": 30
}

>>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
apple
banana
cherry

>>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
text example
```


## Словари констант

### `TEXT_COLORS`

Словарь, содержащий ANSI escape коды для различных цветов текста.

### `BG_COLORS`

Словарь, содержащий ANSI escape коды для различных цветов фона.

### `FONT_STYLES`

Словарь, содержащий ANSI escape коды для различных стилей шрифта.

### `RESET`

ANSI escape код для сброса стилей.

## Тестирование (в блоке `if __name__ == '__main__':`)

В блоке `if __name__ == '__main__':`  приведен пример использования функции `pprint` для вывода словаря с различными параметрами стилизации.
```
```