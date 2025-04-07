# Модуль для конвертации HTML в DOCX с использованием LibreOffice
==================================================================

Модуль предоставляет функциональность для конвертации HTML-файлов в формат DOCX с использованием LibreOffice.

## Обзор

Этот модуль содержит функцию `html_to_docx`, которая использует LibreOffice для преобразования HTML-файла в документ Word (DOCX). Модуль предназначен для автоматизации процесса конвертации файлов, что может быть полезно в различных задачах, таких как создание отчетов, архивирование веб-страниц или преобразование контента для редактирования в Word.

## Подробней

Модуль `html2docx.py` предназначен для преобразования HTML файлов в формат DOCX с использованием LibreOffice. Он обеспечивает надежный способ конвертации, обрабатывая ошибки и логируя их для облегчения отладки. Этот модуль важен в проекте `hypotez`, поскольку позволяет преобразовывать HTML-шаблоны, сгенерированные системой, в редактируемые документы Word.

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

**Назначение**:
Конвертирует HTML файл в документ Word (DOCX) с использованием LibreOffice.

**Параметры**:
- `html_file` (str): Путь к входному HTML файлу в виде строки.
- `output_docx` (Path | str): Путь к выходному DOCX файлу.

**Возвращает**:
- `bool`: `True`, если конвертация выполнена успешно, `False` в противном случае.

**Вызывает исключения**:
- `subprocess.CalledProcessError`: Если LibreOffice не смог выполнить конвертацию.
- `FileNotFoundError`: Если исполняемый файл LibreOffice (soffice) не найден.
- `Exception`: Если произошла непредвиденная ошибка во время конвертации.

**Как работает функция**:

1. **Проверка наличия HTML-файла**: Функция проверяет, существует ли входной HTML-файл по указанному пути. Если файл не найден, функция логирует ошибку и возвращает `False`.
2. **Создание выходной директории**: Функция проверяет, существует ли директория для выходного DOCX-файла. Если директория не существует, она создает её.
3. **Формирование команды для LibreOffice**: Функция формирует команду для вызова LibreOffice в режиме headless (без графического интерфейса) с параметрами для конвертации HTML в DOCX.
4. **Выполнение команды LibreOffice**: Функция выполняет сформированную команду с помощью `subprocess.run`. При этом перехватываются стандартный вывод и стандартный вывод ошибок.
5. **Проверка ошибок**: Функция проверяет наличие ошибок в стандартном выводе ошибок процесса LibreOffice. Если ошибки обнаружены, они логируются.
6. **Обработка исключений**:
   - Если процесс LibreOffice завершается с ошибкой, перехватывается исключение `subprocess.CalledProcessError`, логируется сообщение об ошибке с указанием входного и выходного файлов, а также текста ошибки, и возвращается `False`.
   - Если исполняемый файл LibreOffice не найден, перехватывается исключение `FileNotFoundError`, логируется сообщение об ошибке и возвращается `False`.
   - В случае любой другой непредвиденной ошибки перехватывается общее исключение `Exception`, логируется сообщение об ошибке и возвращается `False`.

**Внутренние функции**:
Внутри данной функции нет внутренних функций.

**Пример**:

```python
from pathlib import Path
from src.utils.convertors.html2docx import html_to_docx

html_file = "template.html"  # Укажите путь к вашему HTML файлу
output_docx = Path("output.docx")  # Укажите желаемый путь для выходного DOCX файла

if html_to_docx(html_file, output_docx):
    print(f"Успешно конвертировано {html_file} в {output_docx} с использованием LibreOffice!")
else:
    print(f"Не удалось конвертировать {html_file} в {output_docx} с использованием LibreOffice.")
```
ASCII схема работы функции

```
A: Проверка наличия HTML файла
|
B: Создание выходной директории
|
C: Формирование команды LibreOffice
|
D: Выполнение команды LibreOffice
|
E: Проверка ошибок
|
F: Обработка исключений
|
G: Возврат результата
```

## Примеры использования

В основной части модуля (`if __name__ == '__main__'`) представлен пример использования функции `html_to_docx`. В этом примере задаются пути к входному HTML-файлу и выходному DOCX-файлу, затем вызывается функция `html_to_docx` для выполнения конвертации. В зависимости от результата конвертации выводится соответствующее сообщение.
```python
if __name__ == '__main__':
    # Example usage
    html_file = "template.html"  # Replace with your HTML file (as string)
    output_docx = Path("output_libreoffice.docx")  # Replace with your desired output file

    if html_to_docx(html_file, output_docx):
        print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
    else:
        print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")