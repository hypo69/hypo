# Модуль `report_generator`

## Обзор

Модуль `report_generator` предназначен для генерации отчетов в форматах HTML и PDF на основе данных, полученных в формате JSON. Он обеспечивает гибкую настройку генерации отчетов, поддерживая различные языки и шаблоны. Модуль является частью проекта `hypotez` и располагается в подкаталоге `src/endpoints/kazarinov/report_generator`.

## Подробней

Модуль `report_generator` предоставляет класс `ReportGenerator`, который отвечает за создание отчетов. Он использует шаблоны Jinja2 для генерации HTML-контента, который затем может быть преобразован в PDF и DOCX. Модуль интегрирован с системой логирования `logger` из `src.logger`, что позволяет отслеживать ошибки и ход выполнения операций.

Основные этапы работы модуля:

1.  Загрузка данных из JSON-файла.
2.  Генерация HTML-контента на основе шаблона Jinja2 и загруженных данных.
3.  Сохранение HTML-контента в файл.
4.  Преобразование HTML-контента в PDF-файл с использованием `pdfkit`.
5.  Создание DOCX файла из HTML.

Модуль предназначен для автоматизации процесса создания отчетов, что особенно полезно в задачах, требующих регулярной генерации документов на основе структурированных данных.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Методы**:

*   `__init__`: Инициализирует объект `ReportGenerator`, определяя форматы отчетов, которые необходимо создать.
*   `create_reports_async`: Асинхронно создает отчеты во всех поддерживаемых форматах (HTML, PDF, DOCX).
*   `service_apendix`: Возвращает словарь с информацией о сервисе.
*   `create_html_report_async`: Асинхронно генерирует HTML-контент на основе шаблона и данных.
*   `create_pdf_report_async`: Асинхронно генерирует PDF-отчет на основе HTML-контента.
*   `create_docx_report_async`: Создает DOCX файл из HTML.

**Параметры**:

*   `if_need_html` (bool): Указывает, требуется ли генерация HTML-отчета.
*   `if_need_pdf` (bool): Указывает, требуется ли генерация PDF-отчета.
*   `if_need_docx` (bool): Указывает, требуется ли генерация DOCX-отчета.
*   `storage_path` (Path): Путь к директории, где будут сохраняться отчеты.
*   `html_path` (Path | str): Путь к HTML-файлу.
*   `pdf_path` (Path | str): Путь к PDF-файлу.
*   `docs_path` (Path | str): Путь к DOCX-файлу.
*   `html_content` (str): HTML-контент отчета.
*   `data` (dict): Данные для генерации отчета.
*   `lang` (str): Язык отчета.
*   `mexiron_name` (str): Имя мехирона.
*   `env` (Environment): Окружение Jinja2 для работы с шаблонами.

**Примеры**:

```python
from src.endpoints.kazarinov.report_generator.report_generator import ReportGenerator
import asyncio

async def main():
    report_generator = ReportGenerator()
    #report_generator.create_reports_async(...)  # Пример вызова асинхронного метода
    print(report_generator)

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `main`

```python
def main(maxiron_name: str, lang: str) -> bool:
    """
    Args:
        maxiron_name (str): Имя мехирона.
        lang (str): Язык отчёта.

    Returns:
        bool: True, если отчет сгенерирован успешно.

    Raises:
        Exception: В случае ошибки при генерации отчета.

    Example:
        >>> main('250127221657987', 'ru')
        True
    """
```

**Описание**: Функция `main` является точкой входа для генерации отчетов. Она загружает данные из JSON-файла, создает экземпляры класса `ReportGenerator` и запускает процесс генерации отчетов в различных форматах.

**Параметры**:

*   `maxiron_name` (str): Имя мехирона, которое используется для формирования имени файла данных.
*   `lang` (str): Язык, на котором необходимо сгенерировать отчет.

**Возвращает**:

*   `bool`: Возвращает `True`, если отчет был успешно сгенерирован и сохранен, в противном случае возвращает `False`.

**Вызывает исключения**:

*   `FileNotFoundError`: Если не удается найти JSON-файл с данными.
*   `Exception`: В случае любой другой ошибки, возникшей в процессе генерации отчета.

**Примеры**:

```python
from src.endpoints.kazarinov.report_generator.report_generator import main

result = main(maxiron_name='250127221657987', lang='ru')
print(f"Отчет сгенерирован: {result}")