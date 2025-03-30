# Модуль `md2dict`

## Обзор

Модуль `md2dict` предоставляет функции для конвертации строк в формате Markdown в HTML и структурированные словари. Он использует библиотеку `markdown2` для преобразования Markdown в HTML и регулярные выражения для извлечения информации о структуре документа.

## Подробней

Модуль предназначен для обработки Markdown-текста, извлечения из него основных разделов и структурирования информации в удобном для дальнейшей обработки формате. Это может быть полезно для автоматического анализа и обработки текстовых документов, написанных с использованием Markdown. В частности, он используется для преобразования Markdown-файлов в формат, пригодный для машинной обработки, например, для создания документации или извлечения данных.

## Функции

### `md2html`

```python
def md2html(md_string: str, extras: List[str] = None) -> str:
    """
    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2. Defaults to None.

    Returns:
        str: HTML-представление Markdown.
    """
```

**Описание**: Конвертирует строку Markdown в HTML.

**Параметры**:
- `md_string` (str): Строка Markdown, которую необходимо преобразовать в HTML.
- `extras` (List[str], optional): Список расширений для библиотеки `markdown2`. По умолчанию `None`.

**Возвращает**:
- `str`: HTML-представление входной Markdown-строки.

**Вызывает исключения**:
- Возможные исключения, возникающие при преобразовании Markdown в HTML, логируются в `logger.error`.

**Примеры**:
```python
from src.utils.convertors.md2dict import md2html

markdown_text = "# Заголовок 1\nЭто параграф."
html_text = md2html(markdown_text)
print(html_text)
```

### `md2dict`

```python
def md2dict(md_string: str, extras: List[str] = None) -> Dict[str, list[str]]:
    """
    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2 для md2html. Defaults to None.

    Returns:
        Dict[str, list[str]]: Структурированное представление Markdown содержимого.
    """
```

**Описание**: Конвертирует строку Markdown в структурированный словарь, где ключами являются заголовки разделов, а значениями - список строк, составляющих содержимое раздела.

**Параметры**:
- `md_string` (str): Строка Markdown для конвертации.
- `extras` (List[str], optional): Список расширений для библиотеки `markdown2`, используемых при конвертации Markdown в HTML. По умолчанию `None`.

**Возвращает**:
- `Dict[str, list[str]]`: Структурированное представление Markdown содержимого в виде словаря. Ключи словаря - заголовки разделов, значения - список строк, составляющих содержимое раздела.

**Вызывает исключения**:
- Возможные исключения, возникающие при парсинге Markdown в словарь, логируются в `logger.error`.

**Примеры**:
```python
from src.utils.convertors.md2dict import md2dict

markdown_text = """
# Заголовок 1
Это параграф в первом разделе.
# Заголовок 2
Это параграф во втором разделе.
"""
result_dict = md2dict(markdown_text)
print(result_dict)
```