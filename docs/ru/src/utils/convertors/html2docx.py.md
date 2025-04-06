# Модуль для конвертации HTML в DOCX с использованием LibreOffice
=================================================================

Модуль содержит функцию `html_to_docx`, которая преобразует HTML-файл в документ Word (.docx) с использованием LibreOffice.

## Обзор

Этот модуль предоставляет функцию для автоматического преобразования HTML-файлов в формат DOCX с использованием LibreOffice. Он использует подпроцесс для вызова LibreOffice в режиме headless, что позволяет выполнять преобразование в фоновом режиме без графического интерфейса.

## Подробней

Модуль использует функцию `html_to_docx` для конвертации HTML в DOCX.  Для этого вызывается системная утилита `soffice` (LibreOffice) через модуль `subprocess`. Важно, чтобы LibreOffice был установлен в системе и команда `soffice` была доступна в PATH. Если в процессе конвертации возникают ошибки, они логируются с использованием модуля `logger`.

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

**Параметры**:
- `html_file` (str): Путь к входному HTML-файлу в виде строки.
- `output_docx` (Path | str): Путь к выходному DOCX-файлу.

**Возвращает**:
- `bool`: `True`, если преобразование выполнено успешно, `False` в противном случае.

**Вызывает исключения**:
- `subprocess.CalledProcessError`: Если LibreOffice не смог выполнить преобразование.
- `FileNotFoundError`: Если исполняемый файл LibreOffice (soffice) не найден.
- `Exception`: При возникновении неожиданной ошибки во время преобразования.

**Как работает функция**:

1.  **Проверка наличия HTML-файла**: Проверяет, существует ли HTML-файл по указанному пути. Если файл не найден, функция логирует ошибку и возвращает `False`.
2.  **Создание выходного каталога**: Обеспечивает существование каталога, в котором должен быть создан DOCX-файл. Если каталог не существует, он создается.
3.  **Формирование команды для LibreOffice**: Формирует команду для вызова LibreOffice с необходимыми параметрами, такими как запуск в режиме headless, указание формата преобразования (HTML в DOCX), путь к входному HTML-файлу и путь к выходному каталогу.
4.  **Выполнение команды LibreOffice**: Выполняет команду LibreOffice с использованием `subprocess.run`. Проверяет наличие ошибок в процессе выполнения.
5.  **Обработка ошибок**: Если во время выполнения команды возникают ошибки (например, LibreOffice возвращает ненулевой код возврата), функция логирует ошибку и возвращает `False`.
6.  **Логирование и возврат результата**: В случае успешного выполнения функция возвращает `True`.

```
Проверка существования HTML-файла
    |
    Нет --> Логирование ошибки и возврат False
    |
    Да
    |
    Создание выходного каталога (если не существует)
    |
    Формирование команды для LibreOffice
    |
    Выполнение команды LibreOffice
    |
    Проверка наличия ошибок в процессе выполнения
    |
    Ошибка --> Логирование ошибки и возврат False
    |
    Успех --> Возврат True
```

**Примеры**:

```python
from pathlib import Path
import os

# Пример использования
html_file = "template.html"  # Замените на ваш HTML-файл
output_docx = Path("output_libreoffice.docx")  # Замените на желаемый выходной файл

# Создаем фиктивный html файл, если его нет
if not os.path.exists(html_file):
    with open(html_file, "w") as f:
        f.write("<html><body><h1>Пример HTML</h1></body></html>")

if html_to_docx(html_file, output_docx):
    print(f"Успешно преобразовано {html_file} в {output_docx} с использованием LibreOffice!")
else:
    print(f"Не удалось преобразовать {html_file} в {output_docx} с использованием LibreOffice.")

```

## Main
Если скрипт запускается напрямую (а не импортируется как модуль), выполняется следующий код:

- Определяются пути к входному HTML-файлу и выходному DOCX-файлу.
- Вызывается функция `html_to_docx` для преобразования HTML в DOCX.
- Выводится сообщение об успехе или неудаче в зависимости от результата преобразования.
```python
if __name__ == '__main__':
    # Example usage
    html_file = "template.html"  # Replace with your HTML file (as string)
    output_docx = Path("output_libreoffice.docx")  # Replace with your desired output file

    if html_to_docx(html_file, output_docx):
        print(f"Successfully converted {html_file} to {output_docx} using LibreOffice!")
    else:
        print(f"Failed to convert {html_file} to {output_docx} using LibreOffice.")