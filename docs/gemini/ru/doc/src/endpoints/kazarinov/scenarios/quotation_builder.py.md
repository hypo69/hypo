# Модуль для обработки данных о продуктах, AI-обработки и интеграции с Facebook
## Обзор

Модуль `quotation_builder.py` предназначен для извлечения, разбора и сохранения данных о продуктах от различных поставщиков. Он включает в себя функциональность для подготовки данных, обработки с использованием искусственного интеллекта и интеграции с Facebook для публикации продуктов.

## Подробнее

Модуль предоставляет класс `QuotationBuilder`, который автоматизирует процесс получения данных о продуктах, их преобразования с использованием AI-моделей и сохранения результатов. Основное назначение модуля — упростить и автоматизировать создание рекламных материалов для Facebook на основе данных, полученных от поставщиков.

## Классы

### `QuotationBuilder`

**Описание**: Класс `QuotationBuilder` предназначен для обработки данных о продуктах, полученных от поставщиков, их преобразования с использованием AI и сохранения результатов.

**Как работает класс**:

1.  **Инициализация**:
    *   При инициализации класса происходит настройка путей для хранения данных, инициализация веб-драйвера и AI-модели.
    *   Определяются необходимые поля товара (`required_fields`), которые должны быть заполнены.
    *   Загружаются переводы (`translations`) из файла `mexiron.json`.
2.  **Преобразование данных**:
    *   Метод `convert_product_fields` преобразует данные о продукте из формата `ProductFields` в словарь, пригодный для обработки AI-моделью.
    *   Внутренняя функция `escape_and_strip` используется для очистки и экранирования текстовых данных.
3.  **Обработка AI**:
    *   Методы `process_ai` и `process_ai_async` отправляют данные о продуктах в AI-модель для обработки и получения результатов.
    *   Используется файл `command_instruction_mexiron_{lang}.md` для формирования запроса к AI-модели.
4.  **Сохранение данных**:
    *   Метод `save_product_data` сохраняет обработанные данные о продукте в файл JSON.
5.  **Публикация в Facebook**:
    *   Метод `post_facebook_async` выполняет сценарий публикации рекламных материалов в Facebook, используя веб-драйвер для взаимодействия с сайтом.

**Методы**:

*   `__init__`: Инициализирует класс `QuotationBuilder` с необходимыми компонентами, такими как веб-драйвер и AI-модель.
*   `convert_product_fields`: Преобразует поля продукта в словарь.
*   `process_ai`: Обрабатывает список продуктов с использованием AI-модели (синхронно).
*   `process_ai_async`: Обрабатывает список продуктов с использованием AI-модели (асинхронно).
*   `save_product_data`: Сохраняет данные продукта в файл.
*   `post_facebook_async`: Публикует рекламные материалы в Facebook.

**Параметры**:

*   `mexiron_name` (Optional[str]): Название процесса Mexiron.
*   `driver` (Optional[Firefox | Playwrid | str]): Экземпляр веб-драйвера.
*   `kwards`: Дополнительные параметры для инициализации веб-драйвера.
*   `f` (ProductFields): Объект, содержащий данные продукта.
*   `products_list` (List[str]): Список данных о продуктах.
*   `lang` (str): Язык, на котором нужно получить ответ от AI-модели.
*   `attempts` (int): Количество попыток для получения валидного ответа от AI-модели.
*   `product_data` (dict): Данные продукта для сохранения.
*   `mexiron` (SimpleNamespace): Данные для публикации в Facebook.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
from src.webdriver.firefox import Firefox
import asyncio

# Инициализация класса QuotationBuilder
quotation_builder = QuotationBuilder(mexiron_name='test_mexiron', driver=Firefox())

# Пример вызова асинхронного метода обработки AI
async def process_data():
    product_list = [{'product_id': '123', 'name': 'Test Product'}]
    result = await quotation_builder.process_ai_async(product_list, lang='ru')
    print(result)

asyncio.run(process_data())
```

## Функции

### `convert_product_fields`

```python
def convert_product_fields(self, f: ProductFields) -> dict:
    """
    Converts product fields into a dictionary. 
    Функция конвертирует поля из объекта `ProductFields` в простой словарь для модели ии.

    Args:
        f (ProductFields): Object containing parsed product data.

    Returns:
        dict: Formatted product data dictionary.

    .. note:: Правила построения полей определяются в `ProductFields`
    """
    ...
```

**Как работает функция**:

Функция `convert_product_fields` преобразует поля продукта из объекта `ProductFields` в словарь, пригодный для обработки AI-моделью.

1.  **Проверка наличия `id_product`**:
    *   Функция сначала проверяет, что поле `f.id_product` не пустое. Если оно пустое, это указывает на сбой при получении данных о товаре, и функция возвращает пустой словарь.
2.  **Экранирование и очистка строк**:
    *   Внутренняя функция `escape_and_strip` используется для очистки и экранирования текстовых данных. Она заменяет символы `\'` и `\"` на `\\\'` и `\\\"`, а также удаляет пробелы в начале и конце строки.
3.  **Извлечение данных из объекта `ProductFields`**:
    *   Функция извлекает значения полей `name`, `description`, `description_short` и `specification` из объекта `f` (типа `ProductFields`). Для каждого поля извлекается значение на нужном языке.
4.  **Формирование словаря**:
    *   Если поле `product_name` не пустое, функция формирует словарь, содержащий преобразованные данные продукта: `product_name`, `product_id`, `description_short`, `description`, `specification`, `local_image_path`.
5.  **Возврат результата**:
    *   Функция возвращает сформированный словарь с данными продукта. Если `product_name` пустое, возвращается пустой словарь.

**Внутренние функции**:

*   `escape_and_strip(text: str) -> str`:

    ```python
        def escape_and_strip(text: str) -> str:
            """
            Очищает и экранирует строку, заменяя символы "\'" и \'"\' на "\\\'" и \'\\"\',\
            удаляя пробелы в начале и конце.
            """
            ...
    ```

    **Как работает функция**:

    Функция `escape_and_strip` очищает и экранирует входную строку.

    1.  **Проверка на пустоту**:
        *   Если входная строка `text` пустая, функция возвращает пустую строку.
    2.  **Экранирование символов**:
        *   Функция использует регулярное выражение для экранирования символов `\'` и `\"`, заменяя их на `\\\'` и `\\\"` соответственно.
    3.  **Замена символа `;`**:
        *   Функция заменяет символ `;` на `<br>`.
    4.  **Удаление пробелов**:
        *   Удаляет пробелы в начале и конце строки с помощью метода `strip()`.
    5.  **Возврат результата**:
        *   Возвращает очищенную и экранированную строку.

**Параметры**:

*   `f` (ProductFields): Объект, содержащий данные продукта.
*   `text` (str): Входная строка для очистки и экранирования.

**Возвращает**:

*   `dict`: Словарь с преобразованными данными продукта.
*   `str`: Очищенная и экранированная строка.

**Примеры**:

```python
from src.endpoints.prestashop.product_fields import ProductFields
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder

# Пример объекта ProductFields (необходимо заполнить данными)
product_fields = ProductFields()
product_fields.id_product = '123'
product_fields.name = {'language': [{'value': 'Test Product'}]}
product_fields.description_short = {'language': [{'value': 'Short description'}]}
product_fields.description = {'language': [{'value': 'Long description'}]}
product_fields.specification = {'language': [{'value': 'Specification'}]}
product_fields.local_image_path = '/path/to/image.jpg'

# Инициализация класса QuotationBuilder
quotation_builder = QuotationBuilder()

# Преобразование данных продукта
product_data = quotation_builder.convert_product_fields(product_fields)
print(product_data)
# Expected output:
# {
#     'product_name': 'Test Product',
#     'product_id': '123',
#     'description_short': 'Short description',
#     'description': 'Long description',
#     'specification': 'Specification',
#     'local_image_path': '/path/to/image.jpg'
# }
```

### `process_ai`

```python
def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Processes the product list through the AI model.

    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.

    .. note::
        Модель может возвращать невалидный результат.
        В таком случае я переспрашиваю модель разумное количество раз.
    """
    ...
```

**Как работает функция**:

Функция `process_ai` обрабатывает список продуктов, отправляя его в AI-модель для получения обработанных данных.

1.  **Проверка количества попыток**:
    *   Если количество оставшихся попыток `attempts` меньше 1, функция немедленно возвращает пустой словарь, так как больше нет попыток для обработки.
2.  **Подготовка запроса к модели**:
    *   Функция считывает содержимое файла с инструкциями для модели (`command_instruction_mexiron_{lang}.md`) и добавляет к нему строковое представление списка продуктов `products_list`.
3.  **Отправка запроса в AI-модель**:
    *   Функция отправляет запрос `q` в AI-модель с помощью метода `self.model.ask(q)` и получает ответ.
4.  **Обработка ответа**:
    *   Если ответ от модели пустой, функция логирует ошибку и возвращает пустой словарь.
    *   Функция пытается распарсить ответ модели как JSON с помощью `j_loads`. Если происходит ошибка парсинга, функция логирует ошибку и, если есть еще попытки, рекурсивно вызывает себя с уменьшенным количеством попыток.
5.  **Возврат результата**:
    *   Если ответ успешно распарсен, функция возвращает распарсенный словарь `response_dict`.

**Параметры**:

*   `products_list` (List[str]): Список данных о продуктах в виде строки.
*   `lang` (str): Язык, на котором нужно получить ответ от AI-модели.
*   `attempts` (int): Количество попыток для получения валидного ответа от AI-модели.

**Возвращает**:

*   `dict`: Распарсенный словарь с обработанными данными от AI-модели.
*   `{}`: Пустой словарь, если не удалось получить или распарсить ответ от AI-модели после всех попыток.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder

# Инициализация класса QuotationBuilder (необходимо настроить)
quotation_builder = QuotationBuilder()

# Пример списка продуктов
products_list = [{'product_id': '123', 'name': 'Test Product'}]

# Обработка списка продуктов с помощью AI-модели
result = quotation_builder.process_ai(products_list, lang='ru', attempts=3)
print(result)
```

### `process_ai_async`

```python
async def process_ai_async(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Processes the product list through the AI model.

    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.

    .. note::
        Модель может возвращать невалидный результат.
        В таком случае я переспрашиваю модель разумное количество раз.
    """
    ...
```

**Как работает функция**:

Функция `process_ai_async` асинхронно обрабатывает список продуктов, отправляя его в AI-модель для получения обработанных данных.

1.  **Проверка количества попыток**:
    *   Если количество оставшихся попыток `attempts` меньше 1, функция немедленно возвращает пустой словарь, так как больше нет попыток для обработки.
2.  **Подготовка запроса к модели**:
    *   Функция считывает содержимое файла с инструкциями для модели (`command_instruction_mexiron_{lang}.md`) и добавляет к нему строковое представление списка продуктов `products_list`.
3.  **Отправка запроса в AI-модель**:
    *   Функция отправляет запрос `q` в AI-модель асинхронно с помощью метода `self.model.ask_async(q)` и получает ответ.
4.  **Обработка ответа**:
    *   Если ответ от модели пустой, функция логирует ошибку и возвращает пустой словарь.
    *   Функция пытается распарсить ответ модели как JSON с помощью `j_loads`. Если происходит ошибка парсинга, функция логирует ошибку и, если есть еще попытки, рекурсивно вызывает себя с уменьшенным количеством попыток.
5.  **Возврат результата**:
    *   Если ответ успешно распарсен, функция возвращает распарсенный словарь `response_dict`.

**Параметры**:

*   `products_list` (List[str]): Список данных о продуктах в виде строки.
*   `lang` (str): Язык, на котором нужно получить ответ от AI-модели.
*   `attempts` (int): Количество попыток для получения валидного ответа от AI-модели.

**Возвращает**:

*   `dict`: Распарсенный словарь с обработанными данными от AI-модели.
*   `{}`: Пустой словарь, если не удалось получить или распарсить ответ от AI-модели после всех попыток.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
import asyncio

# Инициализация класса QuotationBuilder (необходимо настроить)
quotation_builder = QuotationBuilder()

# Пример списка продуктов
products_list = [{'product_id': '123', 'name': 'Test Product'}]

# Асинхронная обработка списка продуктов с помощью AI-модели
async def main():
    result = await quotation_builder.process_ai_async(products_list, lang='ru', attempts=3)
    print(result)

asyncio.run(main())
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> bool:
    """
    Saves individual product data to a file.

    Args:
        product_data (dict): Formatted product data.
    """
    ...
```

**Как работает функция**:

Функция `save_product_data` сохраняет данные о продукте в формате JSON в файл.

1.  **Определение пути к файлу**:
    *   Функция определяет путь к файлу, в котором будут сохранены данные продукта. Путь формируется на основе `export_path` и `product_id` из `product_data`.
2.  **Сохранение данных в файл**:
    *   Функция использует `j_dumps` для сохранения данных продукта в файл в формате JSON. Параметр `ensure_ascii=False` позволяет сохранять не-ASCII символы.
3.  **Обработка ошибок**:
    *   Если `j_dumps` возвращает `False`, значит, произошла ошибка при сохранении данных. В этом случае функция логирует ошибку и возвращает `None`.
4.  **Возврат результата**:
    *   Если данные успешно сохранены, функция возвращает `True`.

**Параметры**:

*   `product_data` (dict): Словарь с данными продукта, которые нужно сохранить.

**Возвращает**:

*   `bool`: `True`, если данные успешно сохранены, и `None` в случае ошибки.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
import asyncio

# Инициализация класса QuotationBuilder (необходимо настроить)
quotation_builder = QuotationBuilder()

# Пример данных продукта
product_data = {'product_id': '123', 'name': 'Test Product'}

# Асинхронное сохранение данных продукта
async def main():
    result = await quotation_builder.save_product_data(product_data)
    print(result)

asyncio.run(main())
```

### `post_facebook_async`

```python
async def post_facebook_async(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
    ...
```

**Как работает функция**:

Функция `post_facebook_async` выполняет сценарий публикации рекламного сообщения в Facebook.

1.  **Переход на страницу Facebook**:
    *   Функция открывает указанную страницу Facebook с использованием веб-драйвера.
2.  **Формирование текста сообщения**:
    *   Формируется текст сообщения, включающий заголовок, описание и цену продукта.
3.  **Публикация сообщения**:
    *   Функция вызывает ряд других функций (`post_message_title`, `upload_post_media`, `message_publish`) для публикации сообщения, загрузки медиафайлов и подтверждения публикации.
4.  **Обработка ошибок**:
    *   Если какая-либо из функций возвращает `False`, функция логирует предупреждение и возвращает `None`.
5.  **Возврат результата**:
    *   Если все шаги выполнены успешно, функция возвращает `True`.

**Параметры**:

*   `mexiron` (SimpleNamespace): Объект, содержащий данные для публикации в Facebook.

**Возвращает**:

*   `bool`: `True`, если сообщение успешно опубликовано, и `None` в случае ошибки.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
import asyncio
from types import SimpleNamespace

# Инициализация класса QuotationBuilder (необходимо настроить)
quotation_builder = QuotationBuilder()

# Пример данных для публикации в Facebook
mexiron_data = SimpleNamespace(
    title='Test Product',
    description='Test Description',
    price='100',
    products=['/path/to/image.jpg']
)

# Асинхронная публикация сообщения в Facebook
async def main():
    result = await quotation_builder.post_facebook_async(mexiron_data)
    print(result)

asyncio.run(main())
```

### `main`

```python
def main():
    """"""
    ...
```

**Как работает функция**:

Функция `main` является точкой входа для запуска процесса создания отчетов.

1.  **Определение параметров**:
    *   Функция задает значения параметров, таких как язык (`lang`), название Mexiron (`mexiron_name`), пути к файлам (`html_path`, `pdf_path`, `docx_path`) и загружает данные из JSON-файла.
2.  **Инициализация `QuotationBuilder`**:
    *   Создается экземпляр класса `QuotationBuilder` с указанным именем Mexiron.
3.  **Создание отчетов**:
    *   Асинхронно вызывается метод `create_reports` экземпляра `QuotationBuilder` для создания отчетов на основе загруженных данных и указанных параметров.

**Параметры**:

*   Нет явных параметров, но функция использует жестко закодированные значения для демонстрации.

**Примеры**:

```python
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
import asyncio
from pathlib import Path

# Пример вызова функции main
def main():
    lang: str = 'he'

    mexiron_name: str = '250203025325520'
    base_path: Path = Path('/path/to/external_storage')  # Замените на фактический путь
    export_path = base_path / 'kazarinov' / 'mexironim' / mexiron_name
    html_path: Path = export_path / f'{mexiron_name}_{lang}.html'
    pdf_path: Path = export_path / f'{mexiron_name}_{lang}.pdf'
    docx_path: Path = export_path / f'{mexiron_name}_{lang}.doc'
    # Создайте фиктивный файл JSON для примера
    data = {'he': [{'product_id': '123', 'name': 'Test Product'}]}

    quotation = QuotationBuilder(mexiron_name)
    asyncio.run(quotation.create_reports(data[lang], mexiron_name, lang, html_path, pdf_path, docx_path))

if __name__ == '__main__':
    main()
```