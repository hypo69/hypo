# Модуль `md2dict`

## Обзор

Модуль `md2dict` предназначен для конвертации Markdown-текста в HTML и структурированные словари. Он позволяет извлекать информацию из Markdown-форматированного текста, делая его удобным для дальнейшей обработки и анализа.

## Подробней

Этот модуль предоставляет функции для преобразования Markdown-строк в HTML и структурированные словари. Он использует библиотеку `markdown2` для конвертации Markdown в HTML и регулярные выражения для извлечения структуры и содержимого. Модуль полезен для разбора Markdown-файлов, извлечения данных и представления их в удобном для программной обработки виде.

## Функции

### `md2html`

```python
def md2html(md_string: str, extras: List[str] = None) -> str:
    """
    Конвертирует строку Markdown в HTML.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2. Defaults to None.

    Returns:
        str: HTML-представление Markdown.
    """
```

**Как работает функция**:
Функция `md2html` принимает Markdown-строку и опциональный список расширений для `markdown2`. Она пытается преобразовать входную строку в HTML с использованием библиотеки `markdown2`. В случае успеха возвращает HTML-представление Markdown, а в случае ошибки логирует ошибку и возвращает пустую строку.

**Параметры**:
- `md_string` (str): Строка Markdown, которую необходимо преобразовать в HTML.
- `extras` (List[str], optional): Список расширений для markdown2. По умолчанию `None`.

**Возвращает**:
- `str`: HTML-представление Markdown-строки. В случае ошибки возвращает пустую строку.

**Вызывает исключения**:
- `Exception`: Логируется в случае ошибки при преобразовании Markdown в HTML.

**Примеры**:

```python
from src.utils.convertors.md import md2html

markdown_text = "# Hello, world!"
html_output = md2html(markdown_text)
print(html_output)  # Вывод: <h1 id="hello-world">Hello, world!</h1>
```

### `md2dict`

```python
def md2dict(md_string: str, extras: List[str] = None) -> Dict[str, list[str]]:
    """
    Конвертирует строку Markdown в структурированный словарь.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2 для md2html. Defaults to None.

    Returns:
         Dict[str, list[str]]: Структурированное представление Markdown содержимого.
    """
```

**Как работает функция**:

Функция `md2dict` конвертирует Markdown-строку в структурированный словарь, где ключами являются заголовки разделов, а значениями — списки строк, относящихся к этим разделам.

1.  Сначала Markdown преобразуется в HTML с помощью функции `md2html`.
2.  Затем HTML разбивается на строки.
3.  Функция итерируется по строкам, определяя заголовки (теги `<h`) и текст.
4.  При обнаружении заголовка первого уровня (`<h1>`), он становится текущим разделом, и для него создается новая запись в словаре `sections`.
5.  Заголовки других уровней и остальной текст добавляются в список текущего раздела.
6.  В конечном итоге возвращается словарь, представляющий структурированное содержимое Markdown.

**Параметры**:
- `md_string` (str): Строка Markdown, которую необходимо преобразовать в словарь.
- `extras` (List[str], optional): Список расширений для `markdown2`, используемый в `md2html`. По умолчанию `None`.

**Возвращает**:
- `Dict[str, list[str]]`: Структурированный словарь, где ключи — заголовки разделов, а значения — списки строк.

**Вызывает исключения**:
- `Exception`: Логируется в случае ошибки при парсинге Markdown в структурированный словарь.

**Примеры**:

```python
from src.utils.convertors.md import md2dict

markdown_text = """
# Section 1
This is the first section.
## Subsection 1.1
Some text in the subsection.
# Section 2
This is the second section.
"""

result = md2dict(markdown_text)
print(result)
# Вывод:
# {
#     'Section 1': ['This is the first section.', 'Subsection 1.1', 'Some text in the subsection.'],
#     'Section 2': ['This is the second section.']
# }
```