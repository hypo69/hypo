# Анализ кода модуля `pdf2html.py`

**Качество кода**
6
-  Плюсы
    - Код выполняет заявленную функцию конвертации PDF в HTML.
    - Используется `PDFUtils` для конвертации.
-  Минусы
    - Отсутствует импорт `logger`.
    - Отсутствует описание модуля и документация к функции.
    - Использование глобальных переменных `pdf_file`, `html_file` для путей к файлам.
    - Не указан импорт `Path` из `pathlib`.
    - Используется `header` как импорт, что не соответствует PEP8 и не понятно, что это за модуль.
    - Не используется обработка ошибок.
    - Нет проверки существования файлов `pdf_file` и родительской директории для `html_file`.

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить документацию к функции `pdf2html` в формате RST.
3. Заменить глобальные переменные на параметры в функции `pdf2html`.
4. Добавить проверку существования `pdf_file` и `html_file`.
5. Добавить обработку ошибок с помощью `logger.error`.
6. Устранить импорт `header`, так как не ясно, что это за модуль. 
7. Добавить импорт `Path` из `pathlib` и `logger` из `src.logger.logger`.

**Оптимизированный код**
```python
"""
Модуль для конвертации PDF в HTML.
=========================================================================================

Этот модуль предоставляет функцию для преобразования PDF файлов в HTML формат с использованием
класса PDFUtils.

Пример использования
--------------------

Пример использования функции `pdf2html`:

.. code-block:: python

    from pathlib import Path
    from src.utils.pdf import PDFUtils
    from src.logger.logger import logger
    
    pdf_file = Path('assets/materials/example.pdf')
    html_file = Path('assets/materials/example.html')
    
    pdf2html(pdf_file, html_file)
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
from pathlib import Path
from src.utils.pdf import PDFUtils
from src.logger.logger import logger

def pdf2html(pdf_file: Path, html_file: Path) -> bool:
    """Конвертирует PDF файл в HTML формат.

    Args:
        pdf_file (Path): Путь к PDF файлу.
        html_file (Path): Путь к HTML файлу.

    Returns:
        bool: `True`, если конвертация прошла успешно, `False` в противном случае.
           
    Raises:
        FileNotFoundError: Если PDF файл не существует.
        Exception: При возникновении любой другой ошибки в процессе конвертации.
    """
    # Проверка существования файла PDF
    if not pdf_file.exists():
        logger.error(f'Файл {pdf_file} не найден.')
        return False
    
    # Код исполняет конвертацию PDF в HTML
    try:
        PDFUtils.pdf_to_html(str(pdf_file), str(html_file))
        return True
    except Exception as e:
         # Код логгирует ошибку в случае сбоя конвертации
        logger.error(f'Ошибка при конвертации {pdf_file} в {html_file}: {e}')
        return False

if __name__ == '__main__':
    # Пример использования функции pdf2html
    pdf_file = Path('assets/materials/101_BASIC_Computer_Games_Mar75.pdf')
    html_file = Path('assets/materials/101_BASIC_Computer_Games_Mar75.html')

    # Код исполняет конвертацию PDF в HTML и логирует результат
    if pdf2html(pdf_file, html_file):
        print(f'PDF файл {pdf_file} успешно конвертирован в {html_file}')
    else:
        print(f'Не удалось конвертировать {pdf_file} в {html_file}')
```