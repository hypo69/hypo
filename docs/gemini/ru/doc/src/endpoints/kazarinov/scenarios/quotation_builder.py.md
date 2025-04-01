# Модуль для подготовки данных, обработки AI и интеграции с Facebook для публикации товаров
## Обзор

Модуль `quotation_builder.py` предназначен для извлечения, разбора и обработки данных о продуктах из различных источников. Он включает в себя функциональность для подготовки данных, обработки с использованием AI и интеграции с Facebook для публикации товаров.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за автоматизацию процесса создания и публикации рекламных материалов для товаров. Он использует различные инструменты, такие как Selenium WebDriver для взаимодействия с веб-сайтами поставщиков, Google Gemini AI для обработки текста и изображений, а также API Facebook для публикации рекламных постов.

## Классы

### `QuotationBuilder`

**Описание**: Класс `QuotationBuilder` обрабатывает извлечение, разбор и сохранение данных о продуктах от поставщиков.

**Принцип работы**:
Класс инициализируется с именем процесса `mexiron_name`, создает пути для экспорта данных, инициализирует веб-драйвер и модель Gemini AI. Он предоставляет методы для преобразования данных о продуктах, обработки с использованием AI, сохранения данных и публикации в Facebook.

**Атрибуты**:
- `base_path` (Path): Базовый путь к каталогу модуля.
- `config` (SimpleNamespace): Конфигурация, загруженная из JSON-файла.
- `html_path` (str | Path): Путь к HTML-файлу.
- `pdf_path` (str | Path): Путь к PDF-файлу.
- `docx_path` (str | Path): Путь к DOCX-файлу.
- `driver` (Driver): Экземпляр Selenium WebDriver.
- `export_path` (Path): Путь для экспорта данных.
- `mexiron_name` (str): Имя процесса Mexiron.
- `price` (float): Цена.
- `timestamp` (str): Временная метка.
- `products_list` (List[dict]): Список обработанных данных о продуктах.
- `model` (GoogleGenerativeAI): Экземпляр модели Google Gemini AI.
- `translations` (SimpleNamespace): Переводы, загруженные из JSON-файла.
- `required_fields` (tuple): Кортеж необходимых полей товара.

**Методы**:
- `__init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None,  **kwards)`: Инициализирует класс `QuotationBuilder`.
- `convert_product_fields(self, f: ProductFields) -> dict`: Преобразует поля продукта в словарь.
- `process_ai(self, products_list: List[str], lang: str,  attempts: int = 3) -> tuple | bool`: Обрабатывает список продуктов с использованием AI модели.
- `process_ai_async(self, products_list: List[str], lang: str,  attempts: int = 3) -> tuple | bool`: Асинхронно обрабатывает список продуктов с использованием AI модели.
- `save_product_data(self, product_data: dict) -> bool`: Сохраняет данные о продукте в файл.
- `post_facebook_async(self, mexiron: SimpleNamespace) -> bool`: Исполняет сценарий рекламного модуля `facebook`.

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
    self.mexiron_name = mexiron_name
    try:
        self.export_path = gs.path.external_storage / ENDPOINT / 'mexironim' / self.mexiron_name
    except Exception as ex:
        logger.error(f"Error constructing export path:",ex)
        ...
        return

    # 1. Initialize webdriver

    if driver:

       if isinstance(driver, Driver):
            self.driver = driver

       elif isinstance(driver, (Firefox, Playwrid, )):  # Chrome, Edge
            self.driver = Driver(driver, **kwards)

       elif isinstance(driver, str):
           if driver.lower() == 'firefox':
                self.driver = Driver(Firefox, **kwards)

           elif driver.lower() == 'playwright':
                self.driver = Driver(Playwrid, **kwards)

    else:
        self.driver = Driver(Firefox, **kwards)

            
    # 2. Initialize Gemini model

    try:
        system_instruction:str = (gs.path.endpoints / ENDPOINT / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
        api_key:str = gs.credentials.gemini.kazarinov
        self.model = GoogleGenerativeAI(
            api_key=api_key,
            system_instruction=system_instruction,
            generation_config={'response_mime_type': 'application/json'}
        )
    except Exception as ex:
        logger.error(f"Error loading model, or instructions or API key:", ex)
        ...
```

**Назначение**: Инициализирует класс `QuotationBuilder` с необходимыми компонентами, такими как веб-драйвер и модель Gemini AI.

**Параметры**:
- `mexiron_name` (Optional[str]): Пользовательское имя для процесса Mexiron. По умолчанию используется текущая дата и время.
- `driver` (Optional[Firefox | Playwrid | str]): Экземпляр Selenium WebDriver. Может быть передан как объект `Driver`, `Firefox`, `Playwrid` или как строка `'firefox'` или `'playwright'`. По умолчанию используется `Firefox`.
- `**kwards`: Дополнительные параметры, передаваемые в конструктор драйвера.

**Как работает функция**:

1. **Инициализация имени и путей**: Устанавливает имя процесса `mexiron_name` и пытается создать путь для экспорта данных. Если происходит ошибка при создании пути, она логируется, и функция завершается.
2. **Инициализация веб-драйвера**:
   - Если передан объект `Driver`, он используется напрямую.
   - Если передан объект `Firefox` или `Playwrid`, создается новый экземпляр `Driver` с переданным драйвером.
   - Если передана строка `'firefox'` или `'playwright'`, создается новый экземпляр `Driver` с соответствующим драйвером.
   - Если драйвер не передан, используется `Firefox` по умолчанию.
3. **Инициализация модели Gemini AI**: Пытается загрузить системные инструкции и API-ключ, а затем инициализировать модель `GoogleGenerativeAI`. Если происходит ошибка при загрузке модели, инструкций или API-ключа, она логируется, и функция завершается.

**Примеры**:

```python
# Инициализация с именем процесса и драйвером Firefox по умолчанию
quotation = QuotationBuilder(mexiron_name='my_mexiron')

# Инициализация с именем процесса и драйвером Playwright
quotation = QuotationBuilder(mexiron_name='my_mexiron', driver='playwright')

# Инициализация с именем процесса и пользовательскими параметрами для драйвера Firefox
quotation = QuotationBuilder(mexiron_name='my_mexiron', driver=Firefox, headless=True)
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
    if not f.id_product:
        logger.error(f"Сбой при получении полей товара. ")
        return {} # <- сбой при получении полей товара. Такое может произойти если вместо страницы товара попалась страница категории, при невнимательном составлении мехирона из комплектующих
    ...

    def escape_and_strip(text: str) -> str:
        """
        Очищает и экранирует строку, заменяя символы "\'" и \'"\' на "\\\'" и '\',
        удаляя пробелы в начале и конце.
        """
        if not text:
            return ''
        # Экранируем "\'" и '"', заменяем ";" на "<br>", удаляем лишние пробелы
        escaped_text = re.sub(r"['\"]", lambda match: '\\' + match.group(0), text.strip()).replace(';', '<br>')
        return escaped_text

    product_name = escape_and_strip(f.name['language'][0]['value']) if f.name and f.name['language'] and len(f.name['language']) > 0 and 'value' in f.name['language'][0] else ''
    description = escape_and_strip(f.description['language'][0]['value']) if f.description and f.description['language'] and len(f.description['language']) > 0 and 'value' in f.description['language'][0] else ''
    description_short = escape_and_strip(f.description_short['language'][0]['value']) if f.description_short and f.description_short['language'] and len(f.description_short['language']) > 0 and 'value' in f.description_short['language'][0] else ''
    specification = escape_and_strip(f.specification['language'][0]['value']) if f.specification and f.specification['language'] and len(f.specification['language']) > 0 and 'value' in f.specification['language'][0] else ''
    
    if not product_name:
        return {}
    return {
        'product_name':product_name,
        'product_id': f.id_product,
        'description_short':description_short,
        'description': description,
        'specification': specification,
        'local_image_path': str(f.local_image_path),
    }
```

**Назначение**: Преобразует поля продукта из объекта `ProductFields` в словарь, пригодный для использования в AI-модели.

**Параметры**:
- `f` (ProductFields): Объект, содержащий распарсенные данные о продукте.

**Возвращает**:
- `dict`: Форматированный словарь с данными о продукте.

**Внутренние функции**:

- `escape_and_strip(text: str) -> str`: Очищает и экранирует строку, заменяя символы `\'` и `"` на `\\'` и `\\"`, а также удаляет пробелы в начале и конце строки.
    - **Параметры**:
        - `text` (str): Строка для обработки.
    - **Возвращает**:
        - `str`: Очищенная и экранированная строка.

**Как работает функция**:

1. **Проверка наличия `id_product`**: Проверяет, существует ли `id_product` в объекте `ProductFields`. Если его нет, функция логирует ошибку и возвращает пустой словарь.
2. **Экранирование и очистка текста**: Определяет внутреннюю функцию `escape_and_strip`, которая используется для очистки и экранирования текстовых полей продукта.
3. **Извлечение данных о продукте**: Извлекает значения для `product_name`, `description`, `description_short` и `specification` из объекта `ProductFields`, используя функцию `escape_and_strip` для очистки и экранирования.
4. **Создание словаря продукта**: Если `product_name` не пустое, функция создает и возвращает словарь, содержащий поля `product_name`, `product_id`, `description_short`, `description`, `specification` и `local_image_path`.

**Примеры**:

```python
# Пример использования функции с объектом ProductFields
product_fields = ProductFields(...)  # Объект ProductFields с данными
product_data = quotation_builder.convert_product_fields(product_fields)
print(product_data)
```

### `process_ai`

```python
def process_ai(self, products_list: List[str], lang: str,  attempts: int = 3) -> tuple | bool:
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
    if attempts < 1:
        ...
        return {}  # return early if no attempts are left

    model_command = Path(gs.path.endpoints / ENDPOINT / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
    # Request response from the AI model
    q = model_command + '\n' + str(products_list)
    response = self.model.ask(q)
    if not response:
        logger.error(f"Нет ответа от модели")
        ...
        return {}

    response_dict:dict = j_loads(response) # <- если будет ошибка , то вернется пустой словарь

    if not response_dict:
        logger.error(f"Ошибка парсинга ответа модели", None, False)
        if attempts > 1:
            ...
            self.process_ai(products_list, lang, attempts -1 )
        return {}
    return  response_dict
```

**Назначение**: Обрабатывает список продуктов с использованием AI-модели, при необходимости повторяя попытки.

**Параметры**:
- `products_list` (List[str]): Список словарей с данными о продуктах в виде строки.
- `lang` (str): Язык, на котором запрашивается ответ от модели.
- `attempts` (int, optional): Количество попыток повтора в случае неудачи. По умолчанию 3.

**Возвращает**:
- `dict`: Обработанный ответ от модели в виде словаря.
- `dict`: Пустой словарь, если не удалось получить валидный ответ после всех попыток.

**Как работает функция**:

1. **Проверка количества попыток**: Если количество попыток (`attempts`) меньше 1, функция возвращает пустой словарь.
2. **Чтение команды для модели**: Читает команду для AI-модели из файла, путь к которому формируется на основе языка (`lang`).
3. **Запрос к AI-модели**: Формирует запрос (`q`), объединяя команду для модели и список продуктов, затем отправляет запрос в модель с помощью метода `self.model.ask(q)`.
4. **Обработка ответа**:
   - Если ответ от модели пустой, функция логирует ошибку и возвращает пустой словарь.
   - Пытается распарсить ответ модели с использованием `j_loads`. Если происходит ошибка парсинга, функция логирует ошибку и, если остались попытки, рекурсивно вызывает себя для повторной обработки.
5. **Возврат результата**: Если ответ успешно распарсен, функция возвращает полученный словарь.

**Примеры**:

```python
# Пример использования функции с списком продуктов на русском языке
products = [...]  # Список продуктов
result = quotation_builder.process_ai(products, lang='ru')
print(result)

# Пример использования функции с списком продуктов и указанием количества попыток
products = [...]  # Список продуктов
result = quotation_builder.process_ai(products, lang='ru', attempts=5)
print(result)
```

### `process_ai_async`

```python
async def process_ai_async(self, products_list: List[str], lang: str,  attempts: int = 3) -> tuple | bool:
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
    if attempts < 1:
        ...
        return {}  # return early if no attempts are left

    model_command = Path(gs.path.endpoints / ENDPOINT / 'instructions' / f'command_instruction_mexiron_{lang}.md').read_text(encoding='UTF-8')
    # Request response from the AI model
    q = model_command + '\n' + str(products_list)

    response = await self.model.ask_async(q) # CORRECT

    if not response:
        logger.error(f"Нет ответа от модели")
        ...
        return {}

    response_dict:dict = j_loads(response) # <- если будет ошибка , то вернется пустой словарь

    if not response_dict:
        logger.error(f'Ошибка {attempts} парсинга ответа модели', None, False)
        if attempts > 1:
            ...
            return await self.process_ai_async(products_list, lang, attempts - 1) 
        return {}
    return  response_dict
```

**Назначение**: Асинхронно обрабатывает список продуктов с использованием AI-модели, при необходимости повторяя попытки.

**Параметры**:
- `products_list` (List[str]): Список словарей с данными о продуктах в виде строки.
- `lang` (str): Язык, на котором запрашивается ответ от модели.
- `attempts` (int, optional): Количество попыток повтора в случае неудачи. По умолчанию 3.

**Возвращает**:
- `dict`: Обработанный ответ от модели в виде словаря.
- `dict`: Пустой словарь, если не удалось получить валидный ответ после всех попыток.

**Как работает функция**:

1. **Проверка количества попыток**: Если количество попыток (`attempts`) меньше 1, функция возвращает пустой словарь.
2. **Чтение команды для модели**: Читает команду для AI-модели из файла, путь к которому формируется на основе языка (`lang`).
3. **Запрос к AI-модели**: Формирует запрос (`q`), объединяя команду для модели и список продуктов, затем асинхронно отправляет запрос в модель с помощью метода `self.model.ask_async(q)`.
4. **Обработка ответа**:
   - Если ответ от модели пустой, функция логирует ошибку и возвращает пустой словарь.
   - Пытается распарсить ответ модели с использованием `j_loads`. Если происходит ошибка парсинга, функция логирует ошибку и, если остались попытки, рекурсивно вызывает себя для повторной обработки.
5. **Возврат результата**: Если ответ успешно распарсен, функция возвращает полученный словарь.

**Примеры**:

```python
# Пример использования функции с списком продуктов на русском языке
products = [...]  # Список продуктов
result = await quotation_builder.process_ai_async(products, lang='ru')
print(result)

# Пример использования функции с списком продуктов и указанием количества попыток
products = [...]  # Список продуктов
result = await quotation_builder.process_ai_async(products, lang='ru', attempts=5)
print(result)
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> bool:
    """
    Saves individual product data to a file.

    Args:
        product_data (dict): Formatted product data.
    """
    file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
    if not j_dumps(product_data, file_path, ensure_ascii=False):
        logger.error(f'Ошибка сохранения словаря {print(product_data)}\n Путь: {file_path}')
        ...
        return
    return True
```

**Назначение**: Сохраняет данные об отдельном продукте в файл в формате JSON.

**Параметры**:
- `product_data` (dict): Словарь с данными о продукте.

**Возвращает**:
- `bool`: `True`, если данные успешно сохранены, иначе `None`.

**Как работает функция**:

1. **Формирование пути к файлу**: Создает путь к файлу, используя `export_path`, `'products'` и `product_id` из `product_data`.
2. **Сохранение данных в файл**: Использует функцию `j_dumps` для сохранения `product_data` в файл по указанному пути. Если `j_dumps` возвращает `False`, это означает, что произошла ошибка при сохранении.
3. **Обработка ошибки**: Если произошла ошибка при сохранении, функция логирует ошибку с использованием `logger.error` и возвращает `None`.
4. **Возврат результата**: Если данные успешно сохранены, функция возвращает `True`.

**Примеры**:

```python
# Пример использования функции с данными о продукте
product_data = {'product_id': '123', 'name': 'Example Product', ...}
result = await quotation_builder.save_product_data(product_data)
if result:
    print("Данные о продукте успешно сохранены")
else:
    print("Ошибка при сохранении данных о продукте")
```

### `post_facebook_async`

```python
async def post_facebook_async(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
    ...
    self.driver.get_url(r'https://www.facebook.com/profile.php?id=61566067514123')
    currency = "ש''ח"
    title = f'{mexiron.title}\n{mexiron.description}\n{mexiron.price} {currency}'
    if not post_message_title(self.d, title):
        logger.warning(f'Не получилось отправить название мехирона')
        ...
        return

    if not upload_post_media(self.d, media = mexiron.products):
        logger.warning(f'Не получилось отправить media')
        ...
        return
    if not message_publish(self.d):
        logger.warning(f'Не получилось отправить media')
        ...
        return

    return True
```

**Назначение**: Асинхронно публикует рекламное сообщение в Facebook, используя данные из объекта `mexiron`.

**Параметры**:
- `mexiron` (SimpleNamespace): Объект, содержащий данные для публикации в Facebook, такие как заголовок, описание, цена и медиафайлы.

**Возвращает**:
- `bool`: `True`, если публикация прошла успешно, иначе `None`.

**Как работает функция**:

1. **Переход на страницу Facebook**: Открывает указанную страницу Facebook с использованием `self.driver.get_url`.
2. **Формирование заголовка**: Формирует заголовок сообщения, объединяя заголовок, описание и цену из объекта `mexiron`.
3. **Публикация сообщения**:
   - Использует функцию `post_message_title` для отправки заголовка сообщения. Если отправка не удалась, функция логирует предупреждение и возвращает `None`.
   - Использует функцию `upload_post_media` для загрузки медиафайлов. Если загрузка не удалась, функция логирует предупреждение и возвращает `None`.
   - Использует функцию `message_publish` для публикации сообщения. Если публикация не удалась, функция логирует предупреждение и возвращает `None`.
4. **Возврат результата**: Если все этапы прошли успешно, функция возвращает `True`.

**Примеры**:

```python
# Пример использования функции с объектом mexiron
mexiron_data = SimpleNamespace(title='Example Title', description='Example Description', price=100, products=[...])
result = await quotation_builder.post_facebook_async(mexiron_data)
if result:
    print("Сообщение успешно опубликовано в Facebook")
else:
    print("Ошибка при публикации сообщения в Facebook")
```

## Функции

### `main`

```python
def main():
    """"""
    ...
    lang:str = 'he'
    
    mexiron_name: str = '250203025325520'
    base_path:Path = Path(gs.path.external_storage)
    export_path = base_path / ENDPOINT / 'mexironim' / mexiron_name
    html_path: Path = export_path / f'{mexiron_name}_{lang}.html'
    pdf_path: Path = export_path / f'{mexiron_name}_{lang}.pdf'
    docx_path:Path = export_path / f'{mexiron_name}_{lang}.doc'
    data = j_loads(export_path / f'{mexiron_name}_{lang}.json')

    quotation = QuotationBuilder(mexiron_name)
    asyncio.run(quotation.create_reports(data[lang], mexiron_name, lang, html_path, pdf_path, docx_path))
```

**Назначение**: Главная функция, которая выполняет основные операции: загрузку данных, создание отчетов.

**Как работает функция**:

1. **Определение переменных**:
   - Устанавливает язык (`lang`) на `'he'`.
   - Устанавливает имя Mexiron (`mexiron_name`).
   - Определяет базовый путь (`base_path`).
   - Формирует пути для экспорта (`export_path`), HTML-файла (`html_path`), PDF-файла (`pdf_path`) и DOCX-файла (`docx_path`).
   - Загружает данные из JSON-файла с использованием `j_loads`.
2. **Инициализация `QuotationBuilder`**: Создает экземпляр класса `QuotationBuilder` с именем Mexiron.
3. **Создание отчетов**: Вызывает асинхронную функцию `quotation.create_reports` для создания отчетов, используя загруженные данные и сформированные пути.

**Примеры**:

```python
# Пример вызова функции main
if __name__ == '__main__':
    main()