# Модуль для конвертации HTML в DOCX с использованием LibreOffice

## Обзор

Этот модуль содержит функцию `html_to_docx`, которая конвертирует HTML-файл в документ Word (.docx) с использованием LibreOffice в headless режиме. Он предназначен для автоматизации процесса конвертации файлов HTML в формат DOCX, что может быть полезно для создания отчетов, документов или других целей, где требуется преобразование веб-контента в редактируемый формат.

## Подробней

Модуль использует библиотеку `subprocess` для запуска LibreOffice из Python. Это позволяет автоматизировать конвертацию HTML в DOCX, не требуя ручного вмешательства. Функция проверяет наличие входного HTML-файла, создает выходной каталог, если он не существует, и обрабатывает любые ошибки, возникающие в процессе конвертации. Логи записываются с использованием модуля `logger` из `src.logger`.

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

    **Как работает функция**:
    Функция `html_to_docx` конвертирует HTML файл в Word документ (.docx) используя LibreOffice.
    Она принимает путь к HTML файлу (`html_file`) и желаемый путь для выходного DOCX файла (`output_docx`).
    Функция сначала проверяет существование входного HTML файла. Если файл не найден, функция записывает ошибку в лог и возвращает `False`.
    Затем, функция проверяет, существует ли директория для выходного файла и, если нет, создает её.
    После этого, функция создает команду для запуска LibreOffice в headless режиме, указывая на необходимость конвертации HTML файла в DOCX формат.
    Команда выполняется с использованием `subprocess.run`, и функция проверяет наличие ошибок в процессе конвертации, записывая их в лог при необходимости.
    Если конвертация прошла успешно, функция возвращает `True`, в противном случае - `False`.
    В случае возникновения исключений, таких как `subprocess.CalledProcessError`, `FileNotFoundError` или других, функция также записывает ошибки в лог.

    """
    ...
```

**Описание**: Конвертирует HTML-файл в документ Word, используя LibreOffice.

**Параметры**:

-   `html_file` (str): Путь к входному HTML-файлу.
-   `output_docx` (Path | str): Путь к выходному DOCX-файлу.

**Возвращает**:

-   `bool`: `True`, если конвертация прошла успешно, `False` в противном случае.

**Вызывает исключения**:

-   `subprocess.CalledProcessError`: Если LibreOffice не смог конвертировать HTML-файл.
-   `FileNotFoundError`: Если LibreOffice не найден.
-   `Exception`: Если произошла непредвиденная ошибка во время конвертации.

**Примеры**:

```python
from pathlib import Path

html_file = "template.html"  # Укажите путь к вашему HTML-файлу
output_docx = Path("output_libreoffice.docx")  # Укажите желаемый путь для выходного файла

if html_to_docx(html_file, output_docx):
    print(f"Успешно преобразован {html_file} в {output_docx} с использованием LibreOffice!")
else:
    print(f"Не удалось преобразовать {html_file} в {output_docx} с использованием LibreOffice.")
```