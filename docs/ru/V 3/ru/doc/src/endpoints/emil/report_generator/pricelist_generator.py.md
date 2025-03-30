# Модуль pricelist_generator

## Обзор

Модуль предназначен для генерации HTML и PDF отчетов на основе данных из JSON для мехиронов Казаринова. Он использует шаблоны Jinja2 для создания HTML и библиотеку pdfkit для преобразования HTML в PDF.

## Подробней

Этот модуль предоставляет класс `ReportGenerator`, который отвечает за загрузку данных, генерацию HTML-контента на основе этих данных и сохранение сгенерированного HTML в PDF-файл.

Модуль выполняет следующие шаги:
1. Загружает данные из JSON-файла, используя функцию `j_loads`.
2. Генерирует HTML-контент на основе шаблона Jinja2 и загруженных данных. Шаблон выбирается в зависимости от языка отчета.
3. Сохраняет сгенерированный HTML-контент в файл.
4. Преобразует HTML-файл в PDF-файл с использованием библиотеки `pdfkit`.

Пример использования:
Сначала необходимо создать экземпляр класса `ReportGenerator`, затем вызвать метод `create_report` с необходимыми параметрами (данные, язык, пути к HTML и PDF файлам).

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
from pathlib import Path
import asyncio
from src.endpoints.emil.report_generator.pricelist_generator import ReportGenerator
from src.utils.jjson import j_loads
from src import gs

#Путь к файлу
mexiron:str = '24_12_01_03_18_24_269'
lang:str = 'ru'
base_path:Path =  gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
data:dict = j_loads(base_path / f'{lang}.json')
html_file:Path =  base_path / f'{mexiron}_{lang}.html' 
pdf_file:Path = base_path / f'{mexiron}_{lang}.pdf'

#Инициализация класса
r = ReportGenerator()
asyncio.run( r.create_report(data, lang, html_file, pdf_file)   )
```

## Функции

### `generate_html`

```python
    async def generate_html(self, data:dict, lang:str ) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
```

**Описание**: Генерирует HTML-контент на основе шаблона и данных.

**Параметры**:
- `data` (dict): Данные для заполнения шаблона.
- `lang` (str): Язык отчёта ('ru' или 'he').

**Возвращает**:
- `str`: Сгенерированный HTML-контент.

**Примеры**:
```python
import asyncio
from pathlib import Path
from src.endpoints.emil.report_generator.pricelist_generator import ReportGenerator
from src.utils.jjson import j_loads
from src import gs

#  Пример вызова функции generate_html

mexiron:str = '24_12_01_03_18_24_269'
lang:str = 'ru'
base_path:Path =  gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
data:dict = j_loads(base_path / f'{lang}.json')

r = ReportGenerator()
html_content = asyncio.run(r.generate_html(data, lang))
print(html_content[:100])
```

### `create_report`

```python
    async def create_report(self, data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
```

**Описание**: Полный цикл генерации отчёта.

**Параметры**:
- `data` (dict): Данные для отчёта.
- `lang` (str): Язык отчёта.
- `html_file` (str | Path): Путь к файлу для сохранения HTML.
- `pdf_file` (str | Path): Путь к файлу для сохранения PDF.

**Возвращает**:
- `bool`: `True`, если отчёт успешно сгенерирован, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если возникла ошибка при сохранении PDF.

**Примеры**:
```python
import asyncio
from pathlib import Path
from src.endpoints.emil.report_generator.pricelist_generator import ReportGenerator
from src.utils.jjson import j_loads
from src import gs

#  Пример вызова функции create_report

mexiron:str = '24_12_01_03_18_24_269'
lang:str = 'ru'
base_path:Path =  gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
data:dict = j_loads(base_path / f'{lang}.json')
html_file:Path =  base_path / f'{mexiron}_{lang}.html' 
pdf_file:Path = base_path / f'{mexiron}_{lang}.pdf'

r = ReportGenerator()
result = asyncio.run(r.create_report(data, lang, html_file, pdf_file))
print(result)
```

### `main`

```python
def main(mexiron:str,lang:str) ->bool:
    ...
```

**Описание**: Главная функция для запуска генерации отчёта.

**Параметры**:
- `mexiron` (str): Имя мехирона.
- `lang` (str): Язык отчёта.

**Возвращает**:
- `bool`: `True`, если отчёт успешно сгенерирован.

**Примеры**:
```python
from src.endpoints.emil.report_generator.pricelist_generator import main

# Пример вызова функции main
mexiron:str = '24_12_01_03_18_24_269'
lang:str = 'ru'
main(mexiron,lang)
```