# Модуль pricelist_generator

## Обзор

Модуль `pricelist_generator` предназначен для генерации HTML и PDF отчетов с прайс-листами, в частности для мехиронов Казаринова. Он использует шаблоны Jinja2 для создания HTML, который затем конвертируется в PDF.

## Подробней

Этот модуль предоставляет класс `ReportGenerator`, который отвечает за загрузку данных из JSON-файлов, генерацию HTML на основе этих данных и сохранение отчетов в форматах HTML и PDF. Он предназначен для автоматизации процесса создания отчетов, используя шаблоны и данные о продуктах.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Методы**:
- `generate_html`: Генерирует HTML-контент на основе шаблона и данных.
- `create_report`: Полный цикл генерации отчёта.

**Параметры**:
- `env` (Environment): Окружение Jinja2 для работы с шаблонами.

**Примеры**
```python
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from src.endpoints.kazarinov.react.pricelist_generator import ReportGenerator

# Пример создания экземпляра класса ReportGenerator
r = ReportGenerator(env=Environment(loader=FileSystemLoader('.')))
```

## Функции

### `generate_html`

```python
    async def generate_html(self, data:dict, lang:str ) -> str:
        """
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
- `lang` (str): Язык отчёта (`ru` или `he`).

**Возвращает**:
- `str`: HTML-контент, сгенерированный на основе шаблона и данных.

**Примеры**:
```python
import asyncio
from src.endpoints.kazarinov.react.pricelist_generator import ReportGenerator

async def main():
    data = {'products': [{'product_title': 'Продукт 1', 'specification': 'Описание 1', 'image_local_saved_path': 'path/to/image1.jpg'}]}
    lang = 'ru'
    r = ReportGenerator()
    html_content = await r.generate_html(data, lang)
    print(html_content[:100])  # Вывод первых 100 символов HTML

asyncio.run(main())
```

### `create_report`

```python
    async def create_report(self, data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool:
        """
        Args:
            data (dict): Данные для отчета.
            lang (str): Язык отчёта.
            html_file (str | Path): Путь для сохранения HTML-файла.
            pdf_file (str | Path): Путь для сохранения PDF-файла.

        Returns:
            bool: `True`, если отчёт успешно создан, `False` в случае ошибки.
        """
```

**Описание**: Полный цикл генерации отчёта, включающий добавление сервисной информации, генерацию HTML, сохранение HTML в файл и конвертацию в PDF.

**Параметры**:
- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчёта (`ru` или `he`).
- `html_file` (str | Path): Путь для сохранения HTML-файла.
- `pdf_file` (str | Path): Путь для сохранения PDF-файла.

**Возвращает**:
- `bool`: `True`, если отчёт успешно создан, `False` в случае ошибки.

**Примеры**:

```python
import asyncio
from pathlib import Path
from src.endpoints.kazarinov.react.pricelist_generator import ReportGenerator

async def main():
    data = {'products': [{'product_title': 'Продукт 1', 'specification': 'Описание 1', 'image_local_saved_path': 'path/to/image1.jpg'}]}
    lang = 'ru'
    html_file = Path('report.html')
    pdf_file = Path('report.pdf')
    r = ReportGenerator()
    result = await r.create_report(data, lang, html_file, pdf_file)
    print(f"Отчет создан: {result}")

asyncio.run(main())
```

### `main`

```python
def main(mexiron:str,lang:str) ->bool:
    ...
```

**Описание**: Главная функция для запуска генерации отчета.

**Параметры**:
- `mexiron` (str): Имя мехирона.
- `lang` (str): Язык отчёта.

**Возвращает**:
- `bool`: `True`, если отчёт успешно создан, `False` в случае ошибки.

**Примеры**:

```python
from src.endpoints.kazarinov.react.pricelist_generator import main

mexiron = '24_12_01_03_18_24_269'
lang = 'ru'
result = main(mexiron, lang)
print(f"Отчет создан: {result}")