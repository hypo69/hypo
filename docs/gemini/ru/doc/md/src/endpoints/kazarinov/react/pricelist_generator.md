# Модуль pricelist_generator

## Обзор

Модуль `pricelist_generator` предназначен для генерации HTML и PDF отчетов для мехиронов Казаринова. Он использует Jinja2 для рендеринга HTML шаблонов и библиотеку `pdfkit` для преобразования HTML в PDF.  Модуль загружает данные из JSON-файла, генерирует HTML-отчет на основе шаблона и сохраняет его в файл, а затем преобразует его в PDF и сохраняет.

## Классы

### `ReportGenerator`

**Описание**: Класс `ReportGenerator` предназначен для генерации HTML и PDF отчетов. Он предоставляет методы для загрузки данных, рендеринга HTML, сохранения HTML и PDF файлов, и запуска полного цикла генерации отчета.

**Атрибуты**:

- `template_path` (str): Путь к файлу шаблона HTML. По умолчанию `gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'`.
- `env` (Environment): Объект Jinja2 для работы с шаблонами.

**Методы**:

#### `generate_html(self, data: dict) -> str`

**Описание**: Генерирует HTML-контент на основе шаблона и переданных данных.

**Параметры**:

- `data` (dict): Словарь с данными для рендеринга шаблона.

**Возвращает**:

- str: сгенерированный HTML-код.

#### `create_report(self, data: dict, html_file: str | Path, pdf_file: str | Path) -> None`

**Описание**: Запускает полный цикл генерации отчета, включая генерацию HTML, сохранение HTML в файл, преобразование HTML в PDF и сохранение PDF в файл.

**Параметры**:

- `data` (dict): Словарь с данными для генерации отчета.
- `html_file` (str | Path): Путь к файлу для сохранения HTML отчета.
- `pdf_file` (str | Path): Путь к файлу для сохранения PDF отчета.

**Возвращает**:

- `None`


## Функции

(Нет функций в этом модуле)


## Использование (пример)

```python
import gs
from pathlib import Path
from .pricelist_generator import ReportGenerator

# ... (получение данных data)

base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326'
html_file: Path = base_path / '202410262326_ru.html'
pdf_file: Path = base_path / '202410262326_ru.pdf'

r = ReportGenerator()
r.create_report(data, html_file, pdf_file)
```

Этот пример демонстрирует создание объекта `ReportGenerator`, получение данных, передачу их в метод `create_report`, для генерации HTML и PDF отчетов.


```
```
```