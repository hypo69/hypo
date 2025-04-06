# Модуль `pricelist_generator`

## Обзор

Модуль `pricelist_generator` предназначен для генерации HTML и PDF отчетов для мехиронов Казаринова. Он включает в себя классы и функции для загрузки данных из JSON, создания HTML на основе шаблонов Jinja2 и преобразования HTML в PDF.

## Подробней

Этот модуль играет важную роль в создании отчетов на основе данных, хранящихся в формате JSON. Он использует шаблоны Jinja2 для генерации HTML, а затем преобразует этот HTML в PDF с использованием утилит `pdfkit` и `PDFUtils`. Модуль обеспечивает гибкость в создании отчетов на разных языках.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Принцип работы**: Класс `ReportGenerator` содержит методы для генерации HTML-контента на основе шаблонов Jinja2 и данных, а также для создания PDF-отчетов из сгенерированного HTML.

**Аттрибуты**:

- `env` (Environment): Окружение Jinja2, используемое для загрузки и рендеринга шаблонов. По умолчанию создает новое окружение с загрузчиком файловой системы, указывающим на текущую директорию.

**Методы**:

- `generate_html(data:dict, lang:str) -> str`: Генерирует HTML-контент на основе шаблона и данных.
- `create_report(data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool`: Полный цикл генерации отчёта.

### `ReportGenerator.generate_html`

```python
    async def generate_html(self, data:dict, lang:str ) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        ...
```

**Назначение**: Генерирует HTML-контент на основе шаблона и данных.

**Параметры**:

- `data` (dict): Словарь с данными для заполнения шаблона.
- `lang` (str): Язык отчёта.

**Возвращает**:

- `str`: HTML-контент.

**Как работает функция**:

1. Определяется имя шаблона в зависимости от языка отчёта (`template_table_he.html` для иврита и `template_table_ru.html` для русского).
2. Формируется полный путь к файлу шаблона.
3. Читается содержимое файла шаблона.
4. Создается объект шаблона Jinja2 из прочитанной строки.
5. Выполняется рендеринг шаблона с использованием переданных данных.
6. Возвращается сгенерированный HTML-контент.

**ASCII flowchart**:

```
A[Определение имени шаблона по языку]
|
B[Формирование пути к шаблону]
|
C[Чтение содержимого шаблона]
|
D[Создание объекта шаблона Jinja2]
|
E[Рендеринг шаблона с данными]
|
F[Возврат HTML-контента]
```

**Примеры**:

```python
from pathlib import Path
import asyncio
from src.endpoints.emil.report_generator.pricelist_generator import ReportGenerator

# Пример использования
async def main():
    data = {"products": [{"product_title": "Товар 1", "specification": "Описание 1"}, {"product_title": "Товар 2", "specification": "Описание 2"}]}
    lang = "ru"
    generator = ReportGenerator()
    html_content = await generator.generate_html(data, lang)
    print(html_content)
    assert isinstance(html_content, str)

if __name__ == "__main__":
    asyncio.run(main())
```

### `ReportGenerator.create_report`

```python
    async def create_report(self, data: dict, lang:str, html_file:str| Path, pdf_file:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
        ...
```

**Назначение**: Полный цикл генерации отчёта, включающий добавление сервисной информации, генерацию HTML, сохранение HTML в файл и преобразование HTML в PDF.

**Параметры**:

- `data` (dict): Словарь с данными для отчёта.
- `lang` (str): Язык отчёта.
- `html_file` (str | Path): Путь к файлу для сохранения HTML.
- `pdf_file` (str | Path): Путь к файлу для сохранения PDF.

**Возвращает**:

- `bool`: `True`, если отчёт успешно сгенерирован, `False` в случае ошибки.

**Как работает функция**:

1. Формируется словарь `service_dict` с информацией об услуге, включающей заголовок продукта, спецификацию и путь к изображению.
2. Добавляется `service_dict` в список продуктов в `data`.
3. Генерируется HTML-контент с использованием метода `generate_html`.
4. HTML-контент сохраняется в файл.
5. Создается экземпляр класса `PDFUtils`.
6. HTML-контент преобразуется в PDF с использованием метода `save_pdf_pdfkit` из `PDFUtils`.
7. Логируется ошибка, если PDF не был скомпилирован.
8. Возвращается `True`, если PDF успешно создан, и `False` в противном случае.

**ASCII flowchart**:

```
A[Формирование service_dict]
|
B[Добавление service_dict в data['products']]
|
C[Генерация HTML-контента]
|
D[Сохранение HTML-контента в файл]
|
E[Создание экземпляра PDFUtils]
|
F[Преобразование HTML в PDF]
|
G[Проверка успешности создания PDF]
|
H[Логирование ошибки (если PDF не создан)]
|
I[Возврат результата]
```

**Примеры**:

```python
import asyncio
from pathlib import Path
from src.endpoints.emil.report_generator.pricelist_generator import ReportGenerator
from src import gs

# Пример использования
async def main():
    data = {"products": [{"product_title": "Товар 1", "specification": "Описание 1"}, {"product_title": "Товар 2", "specification": "Описание 2"}]}
    lang = "ru"
    html_file = Path("report.html")
    pdf_file = Path("report.pdf")
    generator = ReportGenerator()
    result = await generator.create_report(data, lang, html_file, pdf_file)
    print(f"Отчет создан: {result}")
    assert result == True

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `main`

```python
def main(mexiron:str,lang:str) ->bool:
    ...
```

**Назначение**: Главная функция, выполняющая загрузку данных, генерацию отчёта и сохранение результатов в файлы HTML и PDF.

**Параметры**:

- `mexiron` (str): Имя директории mexiron.
- `lang` (str): Язык отчёта.

**Возвращает**:

- `bool`: `True`, если отчёт успешно сгенерирован, `False` в случае ошибки.

**Как работает функция**:

1. Формируется базовый путь к директории mexiron.
2. Загружаются данные из JSON-файла.
3. Определяются пути к файлам HTML и PDF.
4. Создается экземпляр класса `ReportGenerator`.
5. Запускается асинхронная генерация отчёта с использованием `asyncio.run`.

**ASCII flowchart**:

```
A[Формирование базового пути]
|
B[Загрузка данных из JSON]
|
C[Определение путей к HTML и PDF файлам]
|
D[Создание экземпляра ReportGenerator]
|
E[Запуск асинхронной генерации отчёта]
```

**Примеры**:

```python
from src.endpoints.emil.report_generator.pricelist_generator import main

# Пример использования
mexiron = '24_12_01_03_18_24_269'
lang = 'ru'
result = main(mexiron, lang)
print(f"Отчет создан: {result}")
assert result == None