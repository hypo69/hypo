# Модуль pricelist_generator

## Обзор

Модуль `pricelist_generator.py` предназначен для генерации HTML и PDF отчетов на основе данных из JSON файлов. Он используется для создания прайс-листов с возможностью локализации на разные языки. В частности, модуль предназначен для использования в проекте "hypotez" для нужд Казаринова.

## Подробней

Модуль предоставляет класс `ReportGenerator`, который отвечает за генерацию HTML и PDF файлов. Он использует шаблоны Jinja2 для создания HTML-контента и библиотеку `pdfkit` для преобразования HTML в PDF. Основной функционал модуля включает загрузку данных из JSON, генерацию HTML на основе этих данных и сохранение HTML и PDF файлов.

Расположение файла `/src/endpoints/kazarinov/react/pricelist_generator.py` указывает на то, что этот модуль является частью React-интерфейса для управления конечными точками Казаринова.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Методы**:
- `generate_html`: Генерирует HTML-контент на основе шаблона и данных.
- `create_report`: Полный цикл генерации отчёта.

**Параметры**:
- `env` (Environment): Окружение Jinja2 для работы с шаблонами. Инициализируется с FileSystemLoader, указывающим на текущую директорию.

**Примеры**
```python
from jinja2 import Environment, FileSystemLoader
from dataclasses import dataclass, field

@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))
```

## Функции

### `generate_html`

```python
    async def generate_html(self, data:dict, lang:str) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            data (dict): Данные для заполнения шаблона.
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
```

**Описание**: Генерирует HTML-контент на основе шаблона и данных.

**Параметры**:
- `data` (dict): Данные для заполнения шаблона.
- `lang` (str): Язык отчёта. Определяет, какой шаблон использовать (русский или иврит).

**Возвращает**:
- `str`: HTML-контент, сгенерированный на основе шаблона и данных.

**Примеры**:
```python
# Пример использования функции generate_html
# Предположим, что у нас есть экземпляр класса ReportGenerator и данные для отчета
# data = {'products': [{'name': 'Product 1', 'price': 100}, {'name': 'Product 2', 'price': 200}]}
# report_generator = ReportGenerator()
# html_content = asyncio.run(report_generator.generate_html(data, 'ru'))
# print(html_content)
```

### `create_report`

```python
    async def create_report(self, data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            data (dict): Данные для отчёта.
            lang (str): Язык отчёта.
            html_file (str | Path): Путь для сохранения HTML-файла.
            pdf_file (str | Path): Путь для сохранения PDF-файла.

        Returns:
            bool: True в случае успешной генерации, False в случае ошибки.
        """
```

**Описание**: Полный цикл генерации отчёта, включающий добавление сервисной информации, генерацию HTML, сохранение HTML в файл и преобразование HTML в PDF.

**Параметры**:
- `data` (dict): Данные для отчёта.
- `lang` (str): Язык отчёта. Используется для локализации сервисной информации и выбора шаблона.
- `html_file` (str | Path): Путь для сохранения HTML-файла.
- `pdf_file` (str | Path): Путь для сохранения PDF-файла.

**Возвращает**:
- `bool`: `True` в случае успешной генерации, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если не удалось скомпилировать PDF.

**Примеры**:
```python
# Пример использования функции create_report
# Предположим, что у нас есть экземпляр класса ReportGenerator и данные для отчета
# data = {'products': [{'name': 'Product 1', 'price': 100}, {'name': 'Product 2', 'price': 200}]}
# report_generator = ReportGenerator()
# html_file = 'report.html'
# pdf_file = 'report.pdf'
# success = asyncio.run(report_generator.create_report(data, 'ru', html_file, pdf_file))
# print(success)
```

### `main`

```python
def main(mexiron:str,lang:str) ->bool:
    """
    Основная функция для запуска процесса генерации отчёта.

    Args:
        mexiron (str): Идентификатор мехирона.
        lang (str): Язык отчёта.

    Returns:
        bool: True в случае успешной генерации, False в случае ошибки.
    """
```

**Описание**: Основная функция для запуска процесса генерации отчёта.

**Параметры**:
- `mexiron` (str): Идентификатор мехирона. Используется для определения пути к данным и файлам.
- `lang` (str): Язык отчёта.

**Возвращает**:
- `bool`: `True` в случае успешной генерации, `False` в случае ошибки.

**Примеры**:
```python
# Пример использования функции main
# success = main('24_12_01_03_18_24_269', 'ru')
# print(success)