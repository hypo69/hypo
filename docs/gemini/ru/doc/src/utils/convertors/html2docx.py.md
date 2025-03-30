# Модуль конвертации HTML в DOCX

## Обзор

Модуль `html2docx` предоставляет функцию для конвертации HTML-файлов в документы Word (`.docx`) с использованием LibreOffice. Он использует подпроцесс для вызова LibreOffice в headless-режиме, что позволяет выполнять конвертацию без графического интерфейса.

## Подробней

Этот модуль предназначен для автоматизированной конвертации HTML-контента в формат DOCX. Он особенно полезен в приложениях, где требуется генерация документов Word из HTML-шаблонов или веб-страниц.

## Функции

### `html_to_docx`

```python
def html_to_docx(html_file: str, output_docx: Path | str) -> bool:
    """
    Args:
        html_file (str): Путь к входному HTML-файлу в виде строки.
        output_docx (Path | str): Путь к выходному DOCX-файлу.

    Returns:
        bool: `True`, если конвертация выполнена успешно, `False` в противном случае.

    Raises:
        subprocess.CalledProcessError: Если LibreOffice не смог выполнить конвертацию.
        FileNotFoundError: Если исполняемый файл LibreOffice (`soffice`) не найден.
        Exception: При возникновении неожиданной ошибки во время конвертации.

    Example:
        >>> from pathlib import Path
        >>> html_file = "template.html"
        >>> output_docx = Path("output.docx")
        >>> if html_to_docx(html_file, output_docx):
        ...     print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
        ... else:
        ...     print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")
    """
```

**Описание**: Конвертирует HTML-файл в документ Word с использованием LibreOffice.

**Параметры**:
- `html_file` (str): Путь к входному HTML-файлу.
- `output_docx` (Path | str): Путь к выходному DOCX-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `subprocess.CalledProcessError`: Если команда LibreOffice завершилась с ошибкой.
- `FileNotFoundError`: Если исполняемый файл `soffice` не найден.
- `Exception`: При возникновении любой другой ошибки.

**Примеры**:

1.  Успешная конвертация HTML-файла в DOCX:

```python
from pathlib import Path
from src.utils.convertors.html2docx import html_to_docx

html_file = "template.html"  # Укажите путь к вашему HTML-файлу
output_docx = Path("output.docx")  # Укажите желаемый путь для выходного DOCX-файла

if html_to_docx(html_file, output_docx):
    print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
else:
    print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")
```

2.  Обработка ошибки, если HTML-файл не найден:

```python
from pathlib import Path
from src.utils.convertors.html2docx import html_to_docx

html_file = "non_existent_template.html"  # Укажите путь к несуществующему HTML-файлу
output_docx = Path("output.docx")

if html_to_docx(html_file, output_docx):
    print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
else:
    print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")
```

3.  Обработка ошибки, если LibreOffice не установлен или не находится в системном PATH:

```python
from pathlib import Path
from src.utils.convertors.html2docx import html_to_docx

html_file = "template.html"
output_docx = Path("output.docx")

if html_to_docx(html_file, output_docx):
    print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
else:
    print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")
```