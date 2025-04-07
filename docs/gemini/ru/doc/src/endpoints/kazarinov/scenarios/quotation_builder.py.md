# Модуль для построения коммерческих предложений
## Обзор

Модуль `quotation_builder.py` предназначен для извлечения, разбора и сохранения данных о продуктах от различных поставщиков. Он обрабатывает подготовку данных, обработку с использованием искусственного интеллекта и интеграцию с Facebook для публикации товаров.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса создания коммерческих предложений на основе данных, полученных от различных поставщиков. Он включает в себя функциональность для работы с веб-драйвером, интеграцию с AI-моделями (например, Google Gemini) и возможность публикации сгенерированных предложений в Facebook. Модуль использует различные утилиты для работы с файлами, изображениями и логированием.

## Классы

### `QuotationBuilder`

**Описание**: Класс `QuotationBuilder` отвечает за обработку данных о продуктах, их преобразование, обработку с использованием искусственного интеллекта и сохранение результатов.

**Принцип работы**:
Класс инициализируется с именем процесса (`mexiron_name`) и экземпляром веб-драйвера. Он загружает конфигурацию из JSON-файла, инициализирует AI-модель Google Gemini и подготавливает пути для экспорта данных. Основные этапы работы класса включают:

1.  Инициализация веб-драйвера для сбора данных с сайтов поставщиков.
2.  Загрузка и инициализация AI-модели для обработки и улучшения данных о продуктах.
3.  Преобразование данных о продуктах в формат, пригодный для AI-обработки.
4.  Обработка данных с использованием AI для создания описаний и других необходимых атрибутов продукта.
5.  Сохранение обработанных данных о продуктах в файлы.
6.  Публикация данных в Facebook (опционально).

**Аттрибуты**:

*   `base_path` (Path): Базовый путь к директории модуля.
*   `config` (SimpleNamespace): Конфигурация, загруженная из JSON-файла.
*   `html_path` (str | Path): Путь для сохранения HTML-отчета.
*   `pdf_path` (str | Path): Путь для сохранения PDF-отчета.
*   `docx_path` (str | Path): Путь для сохранения Docx-отчета.
*   `driver` (Driver): Экземпляр Selenium WebDriver.
*   `export_path` (Path): Путь для экспорта данных.
*   `mexiron_name` (str): Имя процесса Mexiron.
*   `price` (float): Цена продукта.
*   `timestamp` (str): Временная метка.
*   `products_list` (List): Список обработанных данных о продуктах.
*   `model` (GoogleGenerativeAI): Экземпляр AI-модели Google Gemini.
*   `translations` (SimpleNamespace): Переводы, загруженные из JSON-файла.
*   `required_fields` (tuple): Кортеж необходимых полей товара.

**Методы**:

*   `__init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None, \*\*kwards)`: Инициализирует экземпляр класса `QuotationBuilder`.
*   `convert_product_fields(self, f: ProductFields) -> dict`: Преобразует поля продукта в словарь.
*   `process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`: Обрабатывает список продуктов с использованием AI-модели.
*   `process_ai_async(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`: Асинхронно обрабатывает список продуктов с использованием AI-модели.
*   `save_product_data(self, product_data: dict) -> bool`: Сохраняет данные отдельного продукта в файл.
*   `post_facebook_async(self, mexiron: SimpleNamespace) -> bool`: Исполняет сценарий рекламного модуля `facebook`.

## Функции

### `__init__`

```python
def __init__(self, mexiron_name:Optional[str] = gs.now, driver:Optional[Firefox | Playwrid | str] = None,  **kwards):
    """
    Initializes Mexiron class with required components.

    Args:
        driver (Driver): Selenium WebDriver instance.
        mexiron_name (Optional[str]): Custom name for the Mexiron process.
        webdriver_name (Optional[str]): Name of the WebDriver to use. Defaults to 'firefox'. call to Firefox or Playwrid
        window_mode (Optional[str]): Оконный режим вебдрайвера. Может быть 'maximized', 'headless', 'minimized', 'fullscreen', 'normal', 'hidden', 'kiosk'

    """
```

**Назначение**: Инициализирует класс `QuotationBuilder` с необходимыми компонентами, такими как веб-драйвер и AI-модель.

**Параметры**:

*   `mexiron_name` (Optional[str]): Настраиваемое имя для процесса Mexiron. По умолчанию используется текущее время.
*   `driver` (Optional[Firefox | Playwrid | str]): Экземпляр Selenium WebDriver (Driver, Firefox, Playwrid или имя драйвера в виде строки). По умолчанию `None`.
*   `**kwards`: Дополнительные параметры для инициализации веб-драйвера.

**Как работает функция**:

1.  Устанавливает имя процесса `mexiron_name`.
2.  Формирует путь для экспорта данных, используя имя процесса.
3.  Инициализирует веб-драйвер:
    *   Если передан экземпляр `Driver`, использует его напрямую.
    *   Если передан `Firefox` или `Playwrid`, создает экземпляр `Driver` с указанным драйвером.
    *   Если передана строка (например, 'firefox' или 'playwright'), создает экземпляр `Driver` с соответствующим драйвером.
    *   Если драйвер не передан, использует `Firefox` по умолчанию.
4.  Инициализирует AI-модель Google Gemini:
    *   Загружает системные инструкции из файла `system_instruction_mexiron.md`.
    *   Получает API-ключ из `gs.credentials.gemini.kazarinov`.
    *   Создает экземпляр `GoogleGenerativeAI` с указанными параметрами.

**Внутренние функции**: Отсутствуют

**Примеры**:

```python
quotation = QuotationBuilder(mexiron_name='test_mexiron', driver=Firefox())
quotation = QuotationBuilder(mexiron_name='test_mexiron', driver='playwright', window_mode='headless')
```

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
```

**Назначение**: Преобразует поля продукта из объекта `ProductFields` в словарь.

**Параметры**:

*   `f` (ProductFields): Объект, содержащий распарсенные данные о продукте.

**Возвращает**:

*   `dict`: Отформатированный словарь с данными о продукте.

**Как работает функция**:

1.  Проверяет наличие `id_product` в данных продукта. Если `id_product` отсутствует, функция логирует ошибку и возвращает пустой словарь.
2.  Определяет внутреннюю функцию `escape_and_strip(text: str) -> str`, которая очищает и экранирует строку, заменяя символы `"` и `'` на `\"` и `\'`, а также удаляет пробелы в начале и конце строки.
3.  Извлекает значения полей `name`, `description`, `description_short` и `specification` из объекта `ProductFields`, используя функцию `escape_and_strip` для очистки и экранирования данных.
4.  Проверяет наличие имени продукта (`product_name`). Если имя продукта отсутствует, возвращает пустой словарь.
5.  Создает и возвращает словарь, содержащий следующие поля:
    *   `product_name`: Имя продукта.
    *   `product_id`: ID продукта.
    *   `description_short`: Краткое описание продукта.
    *   `description`: Полное описание продукта.
    *   `specification`: Спецификация продукта.
    *   `local_image_path`: Путь к локальному изображению продукта.

**Внутренние функции**:

*   `escape_and_strip(text: str) -> str`: Очищает и экранирует строку.

**Примеры**:

```python
product_fields = ProductFields(...)  # Создание объекта ProductFields с данными
product_data = quotation.convert_product_fields(product_fields)
print(product_data)
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
```

**Назначение**: Обрабатывает список продуктов с использованием AI-модели для получения улучшенных описаний и других атрибутов.

**Параметры**:

*   `products_list` (List[str]): Список данных о продуктах в виде строки.
*   `lang` (str): Язык, на котором нужно получить ответ от AI-модели.
*   `attempts` (int, optional): Количество попыток повторной отправки запроса в случае неудачи. По умолчанию 3.

**Возвращает**:

*   `dict`: Обработанный ответ от AI-модели в виде словаря.
*   `{}`: Пустой словарь, если не удалось получить валидный ответ после всех попыток.

**Как работает функция**:

1.  Проверяет количество оставшихся попыток (`attempts`). Если `attempts` меньше 1, функция возвращает пустой словарь.
2.  Формирует команду для AI-модели, загружая текст команды из файла `command_instruction_mexiron_{lang}.md`.
3.  Формирует запрос (`q`), объединяя команду и список продуктов.
4.  Отправляет запрос в AI-модель с помощью метода `self.model.ask(q)`.
5.  Проверяет наличие ответа от AI-модели. Если ответ отсутствует, логирует ошибку и возвращает пустой словарь.
6.  Парсит ответ AI-модели с использованием `j_loads` для преобразования JSON-строки в словарь.
7.  Проверяет, удалось ли распарсить ответ. Если при парсинге произошла ошибка, логирует ошибку и, если остались попытки, рекурсивно вызывает `self.process_ai` с уменьшенным количеством попыток.
8.  Возвращает полученный словарь с обработанными данными.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
products = [{'product_name': 'Шкаф', 'description': 'Простой шкаф'}]
processed_data = quotation.process_ai(products, lang='ru')
print(processed_data)
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
```

**Назначение**: Асинхронно обрабатывает список продуктов с использованием AI-модели для получения улучшенных описаний и других атрибутов.

**Параметры**:

*   `products_list` (List[str]): Список данных о продуктах в виде строки.
*   `lang` (str): Язык, на котором нужно получить ответ от AI-модели.
*   `attempts` (int, optional): Количество попыток повторной отправки запроса в случае неудачи. По умолчанию 3.

**Возвращает**:

*   `dict`: Обработанный ответ от AI-модели в виде словаря.
*   `{}`: Пустой словарь, если не удалось получить валидный ответ после всех попыток.

**Как работает функция**:

1.  Проверяет количество оставшихся попыток (`attempts`). Если `attempts` меньше 1, функция возвращает пустой словарь.
2.  Формирует команду для AI-модели, загружая текст команды из файла `command_instruction_mexiron_{lang}.md`.
3.  Формирует запрос (`q`), объединяя команду и список продуктов.
4.  Отправляет асинхронный запрос в AI-модель с помощью метода `self.model.ask_async(q)`.
5.  Проверяет наличие ответа от AI-модели. Если ответ отсутствует, логирует ошибку и возвращает пустой словарь.
6.  Парсит ответ AI-модели с использованием `j_loads` для преобразования JSON-строки в словарь.
7.  Проверяет, удалось ли распарсить ответ. Если при парсинге произошла ошибка, логирует ошибку и, если остались попытки, рекурсивно вызывает `self.process_ai_async` с уменьшенным количеством попыток.
8.  Возвращает полученный словарь с обработанными данными.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
products = [{'product_name': 'Шкаф', 'description': 'Простой шкаф'}]
processed_data = await quotation.process_ai_async(products, lang='ru')
print(processed_data)
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> bool:
    """
    Saves individual product data to a file.

    Args:
        product_data (dict): Formatted product data.
    """
```

**Назначение**: Сохраняет данные отдельного продукта в файл в формате JSON.

**Параметры**:

*   `product_data` (dict): Словарь с данными продукта.

**Возвращает**:

*   `True`: Если данные успешно сохранены.
*   `False`: Если произошла ошибка при сохранении данных.

**Как работает функция**:

1.  Формирует путь к файлу, используя `export_path` и `product_id` из `product_data`.
2.  Сохраняет данные в файл с использованием `j_dumps`, указывая `ensure_ascii=False` для поддержки Unicode.
3.  Если при сохранении произошла ошибка, логирует её и возвращает `None`.
4.  Возвращает `True` в случае успешного сохранения.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
product_data = {'product_id': '123', 'product_name': 'Шкаф'}
result = await quotation.save_product_data(product_data)
print(result)
```

### `post_facebook_async`

```python
async def post_facebook_async(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
```

**Назначение**: Публикует сообщение с информацией о продукте на странице Facebook.

**Параметры**:

*   `mexiron` (SimpleNamespace): Объект, содержащий данные для публикации в Facebook (заголовок, описание, цену и медиафайлы).

**Возвращает**:

*   `True`: Если публикация прошла успешно.
*   `False`: Если произошла ошибка в процессе публикации.

**Как работает функция**:

1.  Переходит по указанному URL страницы Facebook.
2.  Формирует заголовок сообщения, объединяя заголовок, описание и цену продукта.
3.  Публикует заголовок сообщения, используя функцию `post_message_title`. Если публикация заголовка не удалась, логирует предупреждение и возвращает `None`.
4.  Загружает медиафайлы (изображения), используя функцию `upload_post_media`. Если загрузка медиафайлов не удалась, логирует предупреждение и возвращает `None`.
5.  Публикует сообщение, используя функцию `message_publish`. Если публикация сообщения не удалась, логирует предупреждение и возвращает `None`.
6.  Возвращает `True` в случае успешной публикации.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
mexiron_data = SimpleNamespace(
    title='Новый шкаф',
    description='Отличное качество',
    price=1000,
    products=['image1.jpg', 'image2.jpg']
)
result = await quotation.post_facebook_async(mexiron_data)
print(result)
```

### `main`

```python
def main():
    """"""
```

**Назначение**: Главная функция для запуска процесса создания отчетов.

**Как работает функция**:

1.  Определяет язык (`lang`) как `'he'`.
2.  Устанавливает имя процесса `mexiron_name` как `'250203025325520'`.
3.  Формирует пути к файлам для экспорта:
    *   `export_path`: Путь к директории экспорта.
    *   `html_path`: Путь к HTML-файлу отчета.
    *   `pdf_path`: Путь к PDF-файлу отчета.
    *   `docx_path`: Путь к Docx-файлу отчета.
4.  Загружает данные из JSON-файла, используя `j_loads`.
5.  Создает экземпляр класса `QuotationBuilder` с указанным именем процесса.
6.  Запускает асинхронную функцию `quotation.create_reports` для создания отчетов.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
main()