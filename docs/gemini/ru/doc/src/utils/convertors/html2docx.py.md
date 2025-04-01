# Модуль для конвертации HTML в DOCX с использованием LibreOffice
==============================================================

Модуль содержит функцию `html_to_docx`, которая конвертирует HTML-файл в документ Word (`.docx`) с использованием LibreOffice.

## Обзор

Этот модуль предоставляет функцию `html_to_docx` для автоматической конвертации HTML-файлов в формат DOCX с использованием LibreOffice. Он обрабатывает исключения, проверяет наличие необходимых файлов и директорий, а также логирует ошибки для облегчения отладки.

## Подробней

Модуль использует библиотеку `subprocess` для вызова LibreOffice в headless-режиме. Это позволяет выполнять конвертацию файлов без необходимости отображения графического интерфейса LibreOffice. Функция проверяет наличие входного HTML-файла, создаёт выходную директорию, если она не существует, и обрабатывает возможные ошибки во время выполнения конвертации.

## Функции

### `html_to_docx`

```python
def html_to_docx(html_file: str, output_docx: Path | str) -> bool:
    """Converts an HTML file to a Word document using LibreOffice.

    Args:
        html_file (str): Path to the input HTML file as a string.
        output_docx (Path | str): Path to the output DOCX file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
```

**Назначение**: Конвертирует HTML-файл в документ Word (`.docx`) с использованием LibreOffice.

**Параметры**:
- `html_file` (str): Путь к входному HTML-файлу.
- `output_docx` (Path | str): Путь к выходному DOCX-файлу.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Вызывает исключения**:
- `subprocess.CalledProcessError`: Если LibreOffice не смог выполнить конвертацию.
- `FileNotFoundError`: Если исполняемый файл LibreOffice (`soffice`) не найден.
- `Exception`: При возникновении любой другой непредвиденной ошибки.

**Как работает функция**:

1. **Проверка наличия HTML-файла**: Проверяет, существует ли файл, указанный в `html_file`. Если файл не найден, функция логирует ошибку и возвращает `False`.
2. **Проверка и создание выходной директории**: Извлекает родительскую директорию из `output_docx` и проверяет, существует ли она. Если директория не существует, она создаётся.
3. **Формирование команды для LibreOffice**: Создаёт список аргументов для вызова LibreOffice через командную строку.
4. **Выполнение команды LibreOffice**: Выполняет команду с использованием `subprocess.run`. Параметр `check=True` вызывает исключение `subprocess.CalledProcessError`, если команда завершается с ненулевым кодом возврата.
5. **Обработка ошибок**: Если во время выполнения команды возникают ошибки, они логируются.
6. **Логирование и возврат результата**: В случае успеха функция возвращает `True`. При возникновении исключений логируются соответствующие ошибки и возвращается `False`.

```
A: Проверка наличия HTML-файла
│
├── Нет: Логирование ошибки, возврат False
│
B: Проверка наличия выходной директории и её создание при необходимости
│
C: Формирование команды для LibreOffice
│
D: Выполнение команды LibreOffice
│
├── Ошибка выполнения команды: Логирование ошибки, возврат False
│
E: Возврат True в случае успеха
```

**Примеры**:

```python
from pathlib import Path
from src.utils.convertors.html2docx import html_to_docx

html_file = "template.html"
output_docx = Path("output_libreoffice.docx")

if html_to_docx(html_file, output_docx):
    print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
else:
    print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")