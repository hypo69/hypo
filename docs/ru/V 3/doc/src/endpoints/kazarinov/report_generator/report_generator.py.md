# Модуль `report_generator.py`

## Обзор

Модуль `report_generator.py` предназначен для генерации отчетов в форматах HTML, PDF и DOCX на основе данных, полученных из JSON-файлов. Он использует шаблонизатор Jinja2 для создания HTML-контента и библиотеки pdfkit и python-docx для преобразования HTML в PDF и DOCX соответственно.

## Подробней

Модуль предоставляет класс `ReportGenerator`, который отвечает за загрузку данных, генерацию HTML, сохранение HTML в файл, преобразование HTML в PDF и DOCX, а также за запуск полного цикла генерации отчёта. Он предназначен для использования в проекте `hypotez` для создания отчетов по данным, связанным с мехиронами Казаринова.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Методы**:
- `__init__`: Определяет, какие форматы данных требуется вернуть.
- `create_reports_async`: Создает отчеты во всех форматах: HTML, PDF, DOCX.
- `service_apendix`: подготавливает данные для сервисного приложения на основе языка.
- `create_html_report_async`: Генерирует HTML-контент на основе шаблона и данных.
- `create_pdf_report_async`: Полный цикл генерации отчёта в PDF.
- `create_docx_report_async`: Создает docx файл.

**Параметры**:
- `if_need_html` (bool): Флаг, указывающий на необходимость генерации HTML-отчета.
- `if_need_pdf` (bool): Флаг, указывающий на необходимость генерации PDF-отчета.
- `if_need_docx` (bool): Флаг, указывающий на необходимость генерации DOCX-отчета.
- `storage_path` (Path): Путь к хранилищу отчетов. По умолчанию `Path(gs.path.external_storage, ENDPOINT)`.
- `html_path` (Path | str): Путь к HTML-файлу.
- `pdf_path` (Path | str): Путь к PDF-файлу.
- `docs_path` (Path | str): Путь к DOCX-файлу.
- `html_content` (str): HTML-контент отчета.
- `data` (dict): Данные для генерации отчета.
- `lang` (str): Язык отчета.
- `mexiron_name` (str): Имя мехирона.
- `env` (Environment): Окружение Jinja2. По умолчанию `Environment(loader=FileSystemLoader('.'))`.

**Примеры**

```python
from pathlib import Path
from src.endpoints.kazarinov.report_generator.report_generator import ReportGenerator

# Пример создания экземпляра класса ReportGenerator
report_generator = ReportGenerator(if_need_pdf = True, if_need_docx = True)

# Пример вызова метода create_reports_async (требуется асинхронный контекст)
# asyncio.run(report_generator.create_reports_async(bot, chat_id, data, lang, mexiron_name))

# Пример вызова метода service_apendix
# service_data = report_generator.service_apendix(lang='ru')
# print(service_data)

# Пример вызова метода create_html_report_async (требуется асинхронный контекст)
# asyncio.run(report_generator.create_html_report_async(data, lang, 'report.html'))

# Пример вызова метода create_pdf_report_async (требуется асинхронный контекст)
# asyncio.run(report_generator.create_pdf_report_async(data, lang, 'report.pdf'))

# Пример вызова метода create_docx_report_async (требуется асинхронный контекст)
# asyncio.run(report_generator.create_docx_report_async('report.html', 'report.docx'))
```

## Функции

### `main`

```python
def main(maxiron_name:str, lang:str) ->bool:
    """ This if example function
    Args:
        maxiron_name (str): имя мехирона.
        lang (str): Язык отчёта.
    Returns:
        bool: Описание возвращаемого значения. Возвращает `True` или `False`.

     Raises:
          Ошибка выполнение

     Example:
         Примеры вызовов

    """
    ...
```

**Описание**: Главная функция для запуска процесса генерации отчетов.

**Параметры**:
- `maxiron_name` (str): Имя мехирона.
- `lang` (str): Язык отчета.

**Возвращает**:
- `bool`: Возвращает `True`, если процесс завершился успешно.

**Вызывает исключения**:
- Отсутствуют явно обработанные исключения.

**Примеры**:

```python
from src.endpoints.kazarinov.report_generator.report_generator import main

# Пример вызова функции main
# result = main(maxiron_name='250127221657987', lang='ru')
# print(result)
```