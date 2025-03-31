# Модуль для конвертации HTML в DOCX с использованием LibreOffice

## Обзор

Модуль предоставляет функцию `html_to_docx`, которая конвертирует HTML-файл в документ Word (.docx) с использованием LibreOffice. Этот модуль позволяет автоматизировать процесс преобразования HTML-контента в формат DOCX, что может быть полезно для создания отчетов, документов и других целей.

## Подробней

Этот модуль использует библиотеку `subprocess` для вызова LibreOffice из Python. Функция `html_to_docx` принимает путь к HTML-файлу и путь к выходному DOCX-файлу в качестве аргументов. Она проверяет наличие HTML-файла, создает выходной каталог, если он не существует, и выполняет команду LibreOffice для преобразования файла. В случае успеха возвращает `True`, в противном случае - `False`. Логи записываются с помощью модуля `logger` из `src.logger`.

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

**Назначение**: Преобразует HTML-файл в документ Word (.docx) с использованием LibreOffice.

**Как работает функция**:
1. Функция проверяет существование входного HTML-файла. Если файл не найден, регистрируется ошибка и возвращается `False`.
2. Функция проверяет наличие родительского каталога для выходного DOCX-файла и создает его, если он не существует.
3. Функция формирует команду для вызова LibreOffice в режиме headless (без графического интерфейса) с параметрами для конвертации HTML в DOCX.
4. Функция выполняет команду LibreOffice с помощью `subprocess.run`, перехватывая стандартный вывод и стандартную ошибку.
5. Функция проверяет наличие ошибок в стандартном выводе LibreOffice и регистрирует их, если они есть.
6. В случае успешного выполнения возвращает `True`, в противном случае - `False`.
7. Функция обрабатывает исключения `subprocess.CalledProcessError` (ошибка выполнения команды LibreOffice), `FileNotFoundError` (LibreOffice не найден) и `Exception` (любая другая ошибка). В каждом случае регистрируется ошибка и возвращается `False`.

**Параметры**:
- `html_file` (str): Путь к входному HTML-файлу в виде строки.
- `output_docx` (Path | str): Путь к выходному DOCX-файлу.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Вызывает исключения**:
- `subprocess.CalledProcessError`: Возникает, если LibreOffice не удалось выполнить преобразование.
- `FileNotFoundError`: Возникает, если не удается найти исполняемый файл LibreOffice (soffice).
- `Exception`: Возникает при любой другой непредвиденной ошибке.

**Примеры**:

```python
from pathlib import Path

html_file = "template.html"  # Replace with your HTML file (as string)
output_docx = Path("output_libreoffice.docx")  # Replace with your desired output file

if html_to_docx(html_file, output_docx):
    print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
else:
    print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")