# Модуль исполнения сценария создания мехирона для Сергея Казаринова

## Обзор

Модуль `from_supplier_to_prestashop.py` предназначен для автоматизации процесса извлечения, обработки и публикации данных о продуктах от различных поставщиков в интернет-магазин PrestaShop. Он включает в себя сбор данных, их преобразование с использованием AI, а также интеграцию с PrestaShop для создания и обновления товарных позиций.

## Подробней

Этот модуль является частью системы автоматизации, цель которой - упростить и ускорить процесс добавления новых товаров в PrestaShop. Он использует веб-драйвер для сбора информации с сайтов поставщиков, AI (Google Gemini) для обработки и улучшения описаний товаров, и API PrestaShop для публикации товаров на платформе. Модуль также включает функциональность для создания отчетов и публикации информации о товарах в социальных сетях, таких как Facebook.

## Классы

### `SupplierToPrestashopProvider`

**Описание**: Класс `SupplierToPrestashopProvider` управляет процессом получения данных о продуктах от поставщиков, их преобразованием и сохранением в PrestaShop. Он использует веб-драйвер для сбора данных, AI для обработки информации и API PrestaShop для публикации продуктов.

**Принцип работы**:
1.  Инициализация класса с необходимыми параметрами, такими как API-ключи, URL-адреса и язык.
2.  Загрузка конфигурационных файлов и инициализация AI-модели Gemini.
3.  Сбор данных о продуктах с использованием веб-драйвера и граберов для конкретных поставщиков.
4.  Преобразование данных о продуктах с использованием AI для создания привлекательных и информативных описаний.
5.  Сохранение данных о продуктах в формате, совместимом с PrestaShop.
6.  Публикация товаров в PrestaShop с использованием API.
7.  Создание отчетов о проделанной работе и их отправка.
8.  Публикация информации о товарах в социальных сетях.

**Атрибуты**:

*   `driver` (Driver): Экземпляр Selenium WebDriver для взаимодействия с веб-страницами.
*   `export_path` (Path): Путь к директории, где сохраняются данные о продуктах.
*   `mexiron_name` (str): Название мехирона.
*   `price` (float): Цена продукта.
*   `timestamp` (str): Временная метка для идентификации операций.
*   `products_list` (list): Список данных о продуктах.
*   `model` (GoogleGenerativeAI): Экземпляр AI-модели Google Gemini.
*   `config` (SimpleNamespace): Конфигурация модуля, загруженная из JSON-файла.
*   `local_images_path` (Path): Путь к локальной директории для хранения изображений товаров.
*   `lang` (str): Язык, используемый для обработки данных и генерации отчетов.
*   `gemini_api` (str): API-ключ для доступа к Google Gemini.
*   `presta_api` (str): API-ключ для доступа к PrestaShop.
*   `presta_url` (str): URL-адрес API PrestaShop.

**Методы**:

*   `__init__`: Инициализирует класс `SupplierToPrestashopProvider` с необходимыми компонентами.
*   `initialise_ai_model`: Инициализирует модель Gemini.
*   `run_scenario`: Выполняет сценарий: разбирает продукты, обрабатывает их через AI и сохраняет данные.
*   `save_product_data`: Сохраняет отдельные данные о продукте в файл.
*   `process_ai`: Обрабатывает список продуктов через AI-модель.
*   `read_data_from_json`: Загружает JSON файлы и фотографии, полученные через телеграм.
*   `save_in_prestashop`: Сохраняет товары в PrestaShop.
*   `post_facebook`: Исполняет сценарий рекламного модуля `facebook`.
*   `create_report`: Отправляет задание на создание мехирона в формате `html` и `pdf`.

## Функции

### `__init__`

```python
def __init__(self, 
             lang:str, 
             gemini_api: str,
             presta_api: str,
             presta_url: str,
             driver: Optional [Driver] = None,
             ):
    """
    Initializes SupplierToPrestashopProvider class with required components.

    Args:
        driver (Driver): Selenium WebDriver instance.
        

    """
```

**Назначение**: Инициализирует экземпляр класса `SupplierToPrestashopProvider`, устанавливая необходимые параметры и зависимости для дальнейшей работы.

**Параметры**:

*   `lang` (str): Язык, используемый в сценарии.
*   `gemini_api` (str): API-ключ для доступа к сервисам Gemini AI.
*   `presta_api` (str): API-ключ для доступа к PrestaShop.
*   `presta_url` (str): URL API PrestaShop.
*   `driver` (Optional[Driver]): Экземпляр веб-драйвера для управления браузером. Если не указан, создается новый экземпляр Firefox. По умолчанию `None`.

**Как работает функция**:

1.  Сохраняет переданные API-ключи и URL PrestaShop в атрибуты экземпляра класса.
2.  Пытается загрузить конфигурацию из JSON-файла, расположенного в директории `src/endpoints/emil`.
3.  Инициализирует временную метку `timestamp` с текущим временем.
4.  Инициализирует веб-драйвер, если он не был передан в качестве аргумента, используя Firefox.
5.  Инициализирует AI-модель Gemini, используя метод `initialise_ai_model`.

```
A: Присвоение параметров
|
B: Загрузка конфигурации
|
C: Инициализация timestamp
|
D: Инициализация драйвера
|
E: Инициализация AI-модели
```

**Примеры**:

```python
provider = SupplierToPrestashopProvider(
    lang='ru',
    gemini_api='your_gemini_api_key',
    presta_api='your_prestashop_api_key',
    presta_url='https://your-prestashop.com/api',
    driver=Driver(Firefox)
)
```

### `initialise_ai_model`

```python
def initialise_ai_model(self):
    """Инициализация модели Gemini"""
    try:
        system_instruction = (gs.path.endpoints / 'emil' / 'instructions' / f'system_instruction_mexiron.{self.lang}.md').read_text(encoding='UTF-8')
        return GoogleGenerativeAI(
            api_key=gs.credentials.gemini.emil,
            system_instruction=system_instruction,
            generation_config={'response_mime_type': 'application/json'}
        )
    except Exception as ex:
        logger.error(f"Error loading instructions", ex)
        return
```

**Назначение**: Инициализирует и настраивает модель Google Gemini для обработки данных.

**Как работает функция**:

1.  Пытается прочитать файл с системными инструкциями для модели Gemini. Файл находится в директории `src/endpoints/emil/instructions` и имеет имя `system_instruction_mexiron.{lang}.md`, где `{lang}` - язык, указанный при инициализации класса `SupplierToPrestashopProvider`.
2.  Создает экземпляр класса `GoogleGenerativeAI`, передавая ему API-ключ, системные инструкции и конфигурацию генерации.
3.  В случае возникновения ошибки при чтении файла с инструкциями, логирует ошибку и возвращает `None`.

```
A: Чтение файла с инструкциями
|
B: Создание экземпляра GoogleGenerativeAI
|
C: Обработка исключения
```

**Примеры**:

```python
model = self.initialise_ai_model()
```

### `run_scenario`

```python
async def run_scenario(
    self, 
    urls: list[str],
    price: Optional[str] = '', 
    mexiron_name: Optional[str] = '', 
    
) -> bool:
    """
    Executes the scenario: parses products, processes them via AI, and stores data.

    Args:
        system_instruction (Optional[str]): System instructions for the AI model.
        price (Optional[str]): Price to process.
        mexiron_name (Optional[str]): Custom Mexiron name.
        urls (Optional[str | List[str]]): Product page URLs.

    Returns:
        bool: True if the scenario executes successfully, False otherwise.

    .. todo:
        сделать логер перед отрицательным выходом из функции. 
        Важно! модель ошибается. 

    """
```

**Назначение**: Выполняет основной сценарий: собирает данные о товарах с указанных URL, обрабатывает их с помощью AI и сохраняет полученные данные.

**Параметры**:

*   `urls` (list[str]): Список URL-адресов, с которых необходимо собрать данные о товарах.
*   `price` (Optional[str]): Цена товара. По умолчанию ''.
*   `mexiron_name` (Optional[str]): Название мехирона. По умолчанию ''.

**Возвращает**:

*   `bool`: `True`, если сценарий выполнен успешно, `False` в противном случае.

**Как работает функция**:

1.  Определяет список обязательных полей товара (`required_fields`).
2.  Итерируется по списку URL-адресов.
3.  Для каждого URL определяет грабер с помощью функции `get_graber_by_supplier_url`.
4.  Если грабер не найден, переходит к следующему URL.
5.  Извлекает данные о товаре с помощью грабера.
6.  Преобразует полученные данные с помощью метода `convert_product_fields`.
7.  Сохраняет данные о товаре с помощью метода `save_product_data`.
8.  Добавляет данные о товаре в список `products_list`.

```
A: Определение обязательных полей
|
B: Итерация по URL-адресам
|
C: Определение грабера
|
D: Извлечение данных о товаре
|
E: Преобразование данных
|
F: Сохранение данных
|
G: Добавление в список
```

**Примеры**:

```python
await provider.run_scenario(
    urls=['https://example.com/product1', 'https://example.com/product2'],
    price='100',
    mexiron_name='Мехирон 1'
)
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict):
    """
    Saves individual product data to a file.

    Args:
        product_data (dict): Formatted product data.
    """
```

**Назначение**: Сохраняет данные о продукте в JSON-файл.

**Параметры**:

*   `product_data` (dict): Словарь с данными о продукте.

**Возвращает**:

*   `bool`: `True`, если данные успешно сохранены, `None` в противном случае.

**Как работает функция**:

1.  Формирует путь к файлу, используя `export_path` и `product_id` из `product_data`.
2.  Сохраняет `product_data` в JSON-файл с помощью функции `j_dumps`.
3.  В случае ошибки логирует её и возвращает `None`.

```
A: Формирование пути к файлу
|
B: Сохранение данных в файл
|
C: Обработка ошибок
```

**Примеры**:

```python
await provider.save_product_data({'product_id': '123', 'name': 'Product 1'})
```

### `process_ai`

```python
async def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Processes the product list through the AI model.

    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.

    .. note::
        Модель может возвращать невелидный результат.
        В таком случае я переспрашиваю модель разумное количество раз.
    """
```

**Назначение**: Обрабатывает список товаров с использованием AI-модели Google Gemini.

**Параметры**:

*   `products_list` (List[str]): Список данных о товарах в виде строки.
*   `lang` (str): Язык, на котором запрашивается ответ от AI-модели.
*   `attempts` (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию 3.

**Возвращает**:

*   `dict`: Обработанный ответ от AI-модели в формате словаря.
*   `dict`: Пустой словарь (`{}`), если не удалось получить валидный ответ после всех попыток.

**Как работает функция**:

1.  Проверяет, остались ли попытки для запроса к AI-модели. Если нет, возвращает пустой словарь.
2.  Формирует команду для AI-модели, считывая содержимое файла `command_instruction_mexiron_{lang}.md` и добавляя к ней строку с данными о товарах.
3.  Отправляет запрос к AI-модели с помощью метода `ask` класса `GoogleGenerativeAI`.
4.  Проверяет, получен ли ответ от AI-модели. Если нет, логирует ошибку и возвращает пустой словарь.
5.  Парсит ответ от AI-модели в формат словаря с помощью функции `j_loads`.
6.  Если не удалось распарсить ответ, логирует ошибку и, если остались попытки, рекурсивно вызывает себя для повторного запроса к AI-модели.
7.  Возвращает полученный словарь с обработанными данными.

```
A: Проверка количества попыток
|
B: Формирование команды для AI-модели
|
C: Отправка запроса к AI-модели
|
D: Проверка ответа от AI-модели
|
E: Парсинг ответа
|
F: Рекурсивный вызов при ошибке
|
G: Возврат результата
```

**Примеры**:

```python
response = await provider.process_ai(products_list, lang='ru', attempts=3)
```

### `read_data_from_json`

```python
async def read_data_from_json(self):
    """Загружаю JSON файлы и фотки, которые я сделал через телеграм"""

    # 1. Get from JSON
    raw_data =  j_loads_ns(self.local_images_path)
    print(raw_data)
```

**Назначение**: Загружает данные из JSON-файлов, расположенных в директории `local_images_path`.

**Как работает функция**:

1.  Использует функцию `j_loads_ns` для загрузки данных из JSON-файла, путь к которому хранится в атрибуте `local_images_path`.
2.  Выводит загруженные данные в консоль с помощью функции `print`.

```
A: Загрузка данных из JSON-файла
|
B: Вывод данных в консоль
```

**Примеры**:

```python
await provider.read_data_from_json()
```

### `save_in_prestashop`

```python
async def save_in_prestashop(self, products_list:ProductFields | list[ProductFields]) -> bool:
    """Функция, которая сохраняет товары в Prestashop emil-design.com """

    products_list: list = products_list if isinstance(products_list, list) else [products_list]

    p = PrestaProduct(api_key=self.presta_api, api_domain=self.presta_url)

    for f in products_list:
        p.add_new_product(f)
```

**Назначение**: Сохраняет данные о товарах в PrestaShop.

**Параметры**:

*   `products_list` (ProductFields | list[ProductFields]): Список объектов `ProductFields` или один объект, содержащий данные о товарах для сохранения в PrestaShop.

**Как работает функция**:

1.  Преобразует входной параметр `products_list` в список, если он не является списком.
2.  Создает экземпляр класса `PrestaProduct`, передавая ему API-ключ и URL PrestaShop.
3.  Итерируется по списку товаров и для каждого товара вызывает метод `add_new_product` класса `PrestaProduct` для добавления товара в PrestaShop.

```
A: Преобразование входного параметра в список
|
B: Создание экземпляра PrestaProduct
|
C: Итерация по списку товаров
|
D: Добавление товара в PrestaShop
```

**Примеры**:

```python
await provider.save_in_prestashop(products_list=[product1, product2])
```

### `post_facebook`

```python
async def post_facebook(self, mexiron:SimpleNamespace) -> bool:
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

**Назначение**: Публикует информацию о товаре на странице Facebook.

**Параметры**:

*   `mexiron` (SimpleNamespace): Объект, содержащий данные о товаре, такие как название, описание, цена и изображения.

**Как работает функция**:

1.  Переходит на страницу Facebook.
2.  Формирует заголовок сообщения, включающий название, описание и цену товара.
3.  Публикует заголовок сообщения на странице Facebook с помощью функции `post_message_title`.
4.  Загружает изображения товара на страницу Facebook с помощью функции `upload_post_media`.
5.  Публикует сообщение на странице Facebook с помощью функции `message_publish`.
6.  В случае неудачи при выполнении какого-либо из этапов, логирует предупреждение и возвращает `None`.

```
A: Переход на страницу Facebook
|
B: Формирование заголовка сообщения
|
C: Публикация заголовка сообщения
|
D: Загрузка изображений
|
E: Публикация сообщения
```

**Примеры**:

```python
await provider.post_facebook(mexiron=product_data)
```

### `create_report`

```python
async def create_report(self, data: dict, lang:str, html_file: Path, pdf_file: Path) -> bool:
    """Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
    Если мехорон в pdf создался (`generator.create_report()` вернул True) - 
    отправить его боту
    """

    report_generator = ReportGenerator()

    if await report_generator.create_report(data, lang, html_file, pdf_file):
        # Проверка, существует ли файл и является ли он файлом
        if pdf_file.exists() and pdf_file.is_file():
            # Отправка боту PDF-файл через reply_document()
            await self.update.message.reply_document(document=pdf_file)
            return True
        else:
            logger.error(f"PDF файл не найден или не является файлом: {pdf_file}")
            return
```

**Назначение**: Генерирует отчет о товаре в форматах HTML и PDF и отправляет PDF-файл боту.

**Параметры**:

*   `data` (dict): Данные о товаре для включения в отчет.
*   `lang` (str): Язык, на котором генерируется отчет.
*   `html_file` (Path): Путь к файлу HTML-отчета.
*   `pdf_file` (Path): Путь к файлу PDF-отчета.

**Как работает функция**:

1.  Создает экземпляр класса `ReportGenerator`.
2.  Генерирует отчет в форматах HTML и PDF с помощью метода `create_report` класса `ReportGenerator`.
3.  Проверяет, был ли успешно создан PDF-файл.
4.  Если PDF-файл существует, отправляет его боту с помощью метода `reply_document`.
5.  В случае ошибки логирует её и возвращает `None`.

```
A: Создание экземпляра ReportGenerator
|
B: Генерация отчета
|
C: Проверка существования PDF-файла
|
D: Отправка PDF-файла боту
|
E: Обработка ошибок
```

**Примеры**:

```python
await provider.create_report(
    data=product_data,
    lang='ru',
    html_file=Path('report.html'),
    pdf_file=Path('report.pdf')
)
```

### `main`

```python
async def main(suppier_to_presta):
    """На данный момент функция читает JSON со списком фотографий , которые были получены от Эмиля"""    
    lang = 'he'
    products_ns = j_loads_ns(gs.path.external_storage / ENDPOINT / 'out_250108230345305_he.json')

    suppier_to_presta = SupplierToPrestashopProvider(lang)
    products_list:list = [f for f in products_ns]
    await suppier_to_presta.save_in_prestashop(products_list)
```

**Назначение**: Выполняет основной поток задач, связанных с обработкой и загрузкой данных о продуктах в PrestaShop. В текущей реализации функция считывает JSON-файл со списком фотографий, полученных от Эмиля, и загружает эти данные в PrestaShop.

**Параметры**:

*   `suppier_to_presta`: Переменная, которая не используется внутри функции. Вероятно, планировалось передавать экземпляр класса `SupplierToPrestashopProvider`, но в текущей реализации он создается внутри функции.

**Как работает функция**:

1.  Устанавливает язык (`lang`) на иврит (`'he'`).
2.  Загружает данные о продуктах из JSON-файла с использованием функции `j_loads_ns`. Путь к файлу формируется на основе констант `gs.path.external_storage`, `ENDPOINT` и имени файла `'out_250108230345305_he.json'`.
3.  Создает экземпляр класса `SupplierToPrestashopProvider`, передавая ему язык. Важно отметить, что API-ключи и URL PrestaShop не передаются, что может привести к проблемам при попытке сохранить данные в PrestaShop.
4.  Преобразует загруженные данные в список (`products_list`).
5.  Сохраняет данные о продуктах в PrestaShop с использованием метода `save_in_prestashop` класса `SupplierToPrestashopProvider`.

```
A: Установка языка
↓
B: Загрузка данных о продуктах из JSON-файла
↓
C: Создание экземпляра класса SupplierToPrestashopProvider
↓
D: Преобразование данных в список
↓
E: Сохранение данных в PrestaShop
```

**Примеры**:

```python
asyncio.run(main(suppier_to_presta=None))