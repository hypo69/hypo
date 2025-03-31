# Модуль `quotation_builder`

## Обзор

Модуль `quotation_builder` предназначен для извлечения, разбора и сохранения данных о продуктах от различных поставщиков. Он включает в себя функциональность подготовки данных, обработки с использованием искусственного интеллекта и интеграции с Facebook для публикации продуктов.

## Подробней

Этот модуль является ключевым компонентом системы, автоматизирующим процесс сбора и обработки информации о товарах. Он использует веб-драйвер для извлечения данных, модель Gemini AI для обработки и улучшения контента, а также Facebook API для публикации рекламных материалов. Расположение файла в структуре проекта указывает на его роль в качестве одной из конечных точек (endpoint) для обработки данных, связанных с поставщиками и рекламными кампаниями.

## Классы

### `QuotationBuilder`

**Описание**: Класс `QuotationBuilder` предназначен для обработки данных о продуктах, полученных от поставщиков, их преобразования, обработки с использованием AI и подготовки к публикации.

**Как работает класс**:

1.  **Инициализация**:
    *   При инициализации класса загружается конфигурация из JSON-файла (`kazarinov.json`).
    *   Инициализируется веб-драйвер (Firefox или Playwright) для сбора данных с веб-сайтов поставщиков.
    *   Загружается модель Gemini AI для обработки текстовых данных о продуктах.

2.  **Обработка данных**:
    *   Метод `convert_product_fields` преобразует поля продукта в формат, удобный для обработки AI.
    *   Методы `process_ai` и `process_ai_async` отправляют данные о продуктах в модель Gemini AI для получения обработанных описаний и заголовков.

3.  **Сохранение и публикация**:
    *   Метод `save_product_data` сохраняет обработанные данные о продуктах в JSON-файлы.
    *   Метод `post_facebook_async` публикует информацию о продуктах на Facebook.

**Атрибуты**:

*   `base_path` (Path): Базовый путь к каталогу `kazarinov` внутри `src/endpoints`.
*   `config` (SimpleNamespace): Объект, содержащий конфигурацию, загруженную из JSON-файла.
*   `html_path` (str | Path): Путь к HTML-файлу для отчетов.
*   `pdf_path` (str | Path): Путь к PDF-файлу для отчетов.
*   `docx_path` (str | Path): Путь к DOCX-файлу для отчетов.
*   `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с веб-страницами.
*   `export_path` (Path): Путь для экспорта данных.
*   `mexiron_name` (str): Имя процесса Mexiron.
*   `price` (float): Цена продукта.
*   `timestamp` (str): Временная метка.
*   `products_list` (List): Список данных о продуктах.
*   `model` (GoogleGenerativeAI): Экземпляр модели Google Gemini AI.
*   `translations` (SimpleNamespace): Объект, содержащий переводы, загруженные из JSON-файла.
*   `required_fields` (tuple): Кортеж необходимых полей товара.

**Методы**:

*   `__init__`: Инициализирует класс `QuotationBuilder` с необходимыми компонентами.
*   `convert_product_fields`: Преобразует поля продукта в словарь.
*   `process_ai`: Обрабатывает список продуктов с использованием AI модели (синхронно).
*   `process_ai_async`: Обрабатывает список продуктов с использованием AI модели (асинхронно).
*   `save_product_data`: Сохраняет данные продукта в файл.
*   `post_facebook_async`: Публикует данные на Facebook.

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
    ...
```

**Описание**: Инициализирует экземпляр класса `QuotationBuilder`, настраивая веб-драйвер и модель Gemini AI.

**Как работает функция**:

1.  **Инициализация пути экспорта**:
    *   Формирует путь для сохранения данных, используя `mexiron_name` для создания уникальной директории.

2.  **Инициализация веб-драйвера**:
    *   Если передан экземпляр `Driver`, использует его напрямую.
    *   Если передан класс веб-драйвера (`Firefox` или `Playwrid`), создает экземпляр `Driver` с использованием этого класса.
    *   Если передана строка `'firefox'` или `'playwright'`, создает соответствующий экземпляр `Driver`.

3.  **Инициализация модели Gemini AI**:
    *   Загружает системные инструкции для модели из файла `system_instruction_mexiron.md`.
    *   Инициализирует модель `GoogleGenerativeAI` с использованием API-ключа и системных инструкций.

**Параметры**:

*   `mexiron_name` (Optional[str]): Имя процесса Mexiron. По умолчанию используется текущее время.
*   `driver` (Optional[Firefox | Playwrid | str]): Экземпляр веб-драйвера или его название (`'firefox'` или `'playwright'`). По умолчанию `None`.
*   `**kwards`: Дополнительные параметры для инициализации веб-драйвера.

**Вызывает исключения**:

*   `Exception`: Возникает при ошибке загрузки конфигурации, инициализации веб-драйвера или модели AI.

**Примеры**:

```python
quotation = QuotationBuilder(mexiron_name='test_mexiron', driver='firefox', window_mode='headless')
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
    ...
```

**Описание**: Преобразует объект `ProductFields` в словарь, пригодный для использования в запросах к AI модели.

**Как работает функция**:

1.  **Проверка наличия ID продукта**:
    *   Если `id_product` отсутствует, функция логирует ошибку и возвращает пустой словарь.

2.  **Экранирование и очистка текста**:
    *   Внутренняя функция `escape_and_strip` используется для экранирования специальных символов в текстовых полях (одинарные и двойные кавычки), замены символа `;` на `<br>`, а также для удаления лишних пробелов в начале и конце строки.

3.  **Извлечение и обработка полей**:
    *   Извлекает значения из полей `name`, `description`, `description_short` и `specification` объекта `ProductFields`, применяя функцию `escape_and_strip` для очистки и экранирования текста.

4.  **Формирование словаря**:
    *   Создает словарь, содержащий обработанные значения полей продукта, а также путь к локальному изображению.

**Параметры**:

*   `f` (ProductFields): Объект типа `ProductFields`, содержащий данные о продукте.

**Возвращает**:

*   `dict`: Словарь с данными о продукте, готовыми для отправки в AI модель. Возвращает пустой словарь, если `id_product` отсутствует или `product_name` пустой.

**Примеры**:

```python
product_fields = ProductFields(...)
product_data = quotation_builder.convert_product_fields(product_fields)
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

**Описание**: Отправляет данные о продуктах в модель Gemini AI для обработки и возвращает обработанный результат.

**Как работает функция**:

1.  **Проверка количества попыток**:
    *   Если количество попыток (`attempts`) меньше 1, функция немедленно возвращает пустой словарь.

2.  **Загрузка команды для модели**:
    *   Загружает команду (инструкцию) для модели из файла `command_instruction_mexiron_{lang}.md`.

3.  **Формирование запроса**:
    *   Объединяет команду и данные о продуктах в единый запрос `q`.

4.  **Отправка запроса в модель**:
    *   Отправляет запрос `q` в модель Gemini AI с помощью метода `self.model.ask(q)`.

5.  **Обработка ответа**:
    *   Парсит ответ модели из JSON-формата.

6.  **Повторные попытки**:
    *   Если ответ невалиден или произошла ошибка парсинга, функция повторяет запрос до тех пор, пока не будут исчерпаны все попытки (`attempts`).

**Параметры**:

*   `products_list` (List[str]): Список данных о продуктах в виде строки.
*   `lang` (str): Язык, на котором требуется получить ответ от модели.
*   `attempts` (int, optional): Количество попыток повторной отправки запроса в случае неудачи. По умолчанию равно 3.

**Возвращает**:

*   `dict`: Обработанный ответ от модели Gemini AI в виде словаря. Возвращает пустой словарь в случае неудачи после всех попыток.

**Примеры**:

```python
products = [...]
ai_response = quotation_builder.process_ai(products, lang='ru', attempts=3)
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

**Описание**: Асинхронно обрабатывает список продуктов, используя модель Gemini AI.

**Как работает функция**:

1.  **Проверка количества попыток**:
    *   Если количество попыток меньше 1, функция возвращает пустой словарь.

2.  **Загрузка инструкции для модели**:
    *   Загружает инструкцию для модели из файла `command_instruction_mexiron_{lang}.md`.

3.  **Формирование запроса**:
    *   Формирует запрос, объединяя инструкцию и список продуктов.

4.  **Отправка запроса в модель**:
    *   Отправляет запрос в модель Gemini AI асинхронно с помощью `self.model.ask_async(q)`.

5.  **Обработка ответа**:
    *   Парсит полученный ответ из JSON в словарь.

6.  **Повторные попытки**:
    *   Если ответ не получен или произошла ошибка парсинга, функция повторяет запрос асинхронно, пока не будут исчерпаны все попытки.

**Параметры**:

*   `products_list` (List[str]): Список продуктов для обработки.
*   `lang` (str): Язык, на котором требуется получить ответ от модели.
*   `attempts` (int, optional): Количество попыток повторной отправки запроса в случае неудачи. По умолчанию равно 3.

**Возвращает**:

*   `dict`: Обработанный ответ от модели Gemini AI в виде словаря. Возвращает пустой словарь в случае неудачи после всех попыток.

**Примеры**:

```python
products = [...]
ai_response = await quotation_builder.process_ai_async(products, lang='ru', attempts=3)
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

**Описание**: Асинхронно сохраняет данные о продукте в JSON-файл.

**Как работает функция**:

1.  **Формирование пути к файлу**:
    *   Формирует путь к файлу, используя `export_path` и `product_id` для создания уникального имени файла.

2.  **Сохранение данных в файл**:
    *   Сохраняет `product_data` в JSON-файл с помощью функции `j_dumps`, отключая экранирование ASCII символов.

3.  **Обработка ошибок**:
    *   В случае ошибки сохранения, функция логирует сообщение об ошибке.

**Параметры**:

*   `product_data` (dict): Словарь с данными о продукте.

**Возвращает**:

*   `bool`: `True`, если данные успешно сохранены, иначе `None`.

**Примеры**:

```python
product_data = {...}
await quotation_builder.save_product_data(product_data)
```

### `post_facebook_async`

```python
async def post_facebook_async(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
    ...
```

**Описание**: Асинхронно публикует рекламное сообщение на Facebook, используя данные из объекта `mexiron`.

**Как работает функция**:

1.  **Переход на страницу Facebook**:
    *   Открывает указанную страницу Facebook в браузере, управляемом веб-драйвером.

2.  **Формирование текста сообщения**:
    *   Формирует текст сообщения, объединяя заголовок, описание и цену продукта из объекта `mexiron`.

3.  **Публикация сообщения**:
    *   Использует функции `post_message_title`, `upload_post_media` и `message_publish` для публикации сообщения и медиафайлов на Facebook.

4.  **Обработка ошибок**:
    *   В случае ошибки при публикации сообщения или загрузке медиафайлов, функция логирует предупреждение.

**Параметры**:

*   `mexiron` (SimpleNamespace): Объект, содержащий данные для публикации на Facebook (заголовок, описание, цена, медиафайлы).

**Возвращает**:

*   `bool`: `True`, если публикация прошла успешно, иначе `None`.

**Примеры**:

```python
mexiron_data = SimpleNamespace(title='Заголовок', description='Описание', price=100, products=['image1.jpg', 'image2.jpg'])
await quotation_builder.post_facebook_async(mexiron_data)
```

## Функции

### `main`

```python
def main():
    """"""
    ...
```

**Описание**: Главная функция, выполняющая основной сценарий формирования отчетов.

**Как работает функция**:

1.  **Определение параметров**:
    *   Устанавливает язык (`lang`), имя мехирона (`mexiron_name`) и базовый путь.

2.  **Формирование путей к файлам**:
    *   Определяет пути к HTML, PDF и DOCX файлам для отчетов.

3.  **Загрузка данных**:
    *   Загружает данные из JSON файла.

4.  **Создание и запуск отчетов**:
    *   Инициализирует класс `QuotationBuilder` и запускает асинхронное создание отчетов.

**Примеры**:

```python
if __name__ == '__main__':
    main()