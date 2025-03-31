# Модуль `md2dict`

## Обзор

Модуль `md2dict` предназначен для конвертации текста в формате Markdown в структурированный словарь. Он включает функции для преобразования Markdown в HTML и последующего извлечения информации для формирования словарной структуры.

## Подробней

Этот модуль предоставляет возможность программно анализировать Markdown-текст, выделяя разделы и контент, что может быть полезно для автоматической обработки документации, извлечения данных из текстовых файлов и других задач, где требуется структурированное представление Markdown-контента. Расположение файла в структуре проекта `/src/utils/convertors/md2dict.py` указывает на его роль как вспомогательного инструмента преобразования данных.

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
    ...
```

**Как работает функция**:
Функция `md2html` принимает строку в формате Markdown и преобразует её в HTML. Использует библиотеку `markdown2` для выполнения преобразования. Если предоставлен список расширений (`extras`), они также применяются в процессе конвертации. В случае возникновения ошибки в процессе преобразования, она логируется, и возвращается пустая строка.

**Параметры**:
- `md_string` (str): Строка, содержащая текст в формате Markdown, который необходимо преобразовать в HTML.
- `extras` (list, optional): Список расширений для библиотеки `markdown2`, которые позволяют расширить функциональность преобразования Markdown. По умолчанию `None`.

**Возвращает**:
- `str`: Строка, содержащая HTML-представление входной Markdown-строки. В случае ошибки возвращает пустую строку.

**Вызывает исключения**:
- Отсутствуют явные исключения, но логирует ошибку с помощью `logger.error`, если преобразование не удалось.

**Примеры**:

```python
from markdown2 import markdown
from src.logger.logger import logger

def md2html(md_string: str, extras: List[str] = None) -> str:
    """
    Конвертирует строку Markdown в HTML.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2. Defaults to None.

    Returns:
        str: HTML-представление Markdown.
    """
    try:
        if extras is None:
            return markdown(md_string)
        return markdown(md_string, extras=extras)
    except Exception as ex:
        logger.error("Ошибка при преобразовании Markdown в HTML.", ex, exc_info=True)
        return ""

# Пример использования:
markdown_text = '# Заголовок'
html_text = md2html(markdown_text)
print(html_text)  # Вывод: <p><h1>Заголовок</h1></p>
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
    ...
```

**Как работает функция**:
Функция `md2dict` преобразует Markdown-текст в структурированный словарь. Сначала Markdown преобразуется в HTML с использованием функции `md2html`. Затем HTML-код анализируется построчно для извлечения заголовков и текста. Заголовки первого уровня становятся ключами словаря, а остальной текст добавляется в список значений, связанных с этими ключами.

**Параметры**:
- `md_string` (str): Строка Markdown для конвертации в словарь.
- `extras` (list, optional): Список расширений markdown2 для использования в `md2html`. По умолчанию `None`.

**Возвращает**:
- `Dict[str, list[str]]`: Словарь, где ключи — это заголовки первого уровня, а значения — списки строк, представляющие контент разделов.

**Вызывает исключения**:
- Отсутствуют явные исключения, но логирует ошибку с помощью `logger.error`, если парсинг Markdown не удался.

**Примеры**:

```python
import re
from typing import Dict, List, Any
from markdown2 import markdown
from src.logger.logger import logger


def md2html(md_string: str, extras: List[str] = None) -> str:
    """
    Конвертирует строку Markdown в HTML.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2. Defaults to None.

    Returns:
        str: HTML-представление Markdown.
    """
    try:
        if extras is None:
            return markdown(md_string)
        return markdown(md_string, extras=extras)
    except Exception as ex:
        logger.error("Ошибка при преобразовании Markdown в HTML.", ex, exc_info=True)
        return ""


def md2dict(md_string: str, extras: List[str] = None) -> Dict[str, list[str]]:
    """
    Конвертирует строку Markdown в структурированный словарь.

    Args:
        md_string (str): Строка Markdown для конвертации.
        extras (list, optional): Список расширений markdown2 для md2html. Defaults to None.

    Returns:
         Dict[str, list[str]]: Структурированное представление Markdown содержимого.
    """
    try:

        html = md2html(md_string, extras)
        sections: Dict[str, list[str]] = {}
        current_section: str | None = None

        for line in html.splitlines():
            if line.startswith('<h'):
                heading_level_match = re.search(r'h(\\d)', line)
                if heading_level_match:
                    heading_level = int(heading_level_match.group(1))
                    section_title = re.sub(r'<.*?>', '', line).strip()
                    if heading_level == 1:
                        current_section = section_title
                        sections[current_section] = []
                    elif current_section:
                        sections[current_section].append(section_title)

            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip()
                sections[current_section].append(clean_text)

        return sections

    except Exception as ex:
        logger.error("Ошибка при парсинге Markdown в структурированный словарь.", ex, exc_info=True)
        return {}

# Пример использования:
markdown_text = """
# Section 1
Content for section 1.

## Subsection
Content for subsection.

# Section 2
Content for section 2.
"""
result = md2dict(markdown_text)
print(result)
# {
#     "Section 1": ["Content for section 1.", "Subsection", "Content for subsection."],
#     "Section 2": ["Content for section 2."]
# }
```