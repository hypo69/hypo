# Модуль исполнения сценария создания мехирона для Сергея Казаринова

## Обзор

Модуль предназначен для извлечения, разбора и обработки данных о товарах от различных поставщиков с целью их последующей публикации в Prestashop. Он включает в себя функциональность для подготовки данных, обработки с использованием искусственного интеллекта и интеграции с Prestashop.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса получения данных о товарах от поставщиков, их обработки и публикации в интернет-магазине Prestashop. Модуль использует веб-драйвер для извлечения данных с сайтов поставщиков, AI-модель Gemini для обработки текста и изображений, а также API Prestashop для публикации товаров.

## Классы

### `SupplierToPrestashopProvider`

**Описание**: Класс `SupplierToPrestashopProvider` обрабатывает извлечение, разбор и сохранение данных о продуктах поставщиков.

**Как работает класс**:
1.  **Инициализация**: Класс инициализируется с параметрами, необходимыми для подключения к API Gemini и Prestashop, а также для управления веб-драйвером.
2.  **Получение данных о товарах**: Использует граберы (парсеры) для извлечения данных о товарах с сайтов поставщиков.
3.  **Обработка данных с использованием AI**: Применяет AI-модель Gemini для обработки полученных данных, например, для создания описаний товаров.
4.  **Сохранение данных**: Сохраняет обработанные данные о товарах в формате JSON.
5.  **Публикация в Prestashop**: Использует API Prestashop для создания новых товаров с использованием полученных данных.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `SupplierToPrestashopProvider`.
*   `initialise_ai_model`: Инициализирует модель Gemini.
*   `run_scenario`: Запускает сценарий обработки данных о товарах.
*   `save_product_data`: Сохраняет данные о товаре в файл.
*   `process_ai`: Обрабатывает список продуктов с использованием AI модели.
*   `read_data_from_json`: Загружает JSON файлы и фотки, которые были получены через телеграм.
*   `save_in_prestashop`: Сохраняет товары в Prestashop.
*   `post_facebook`: Исполняет сценарий рекламного модуля `facebook`.
*   `create_report`: Создаёт отчет о мехироне в формате `html` и `pdf`.

**Параметры**:

*   `driver` (Driver): Экземпляр Selenium WebDriver.
*   `export_path` (Path): Путь для экспорта данных.
*   `products_list` (List\[dict]): Список обработанных данных о продуктах.

### `__init__`

```python
def __init__(
    self,
    lang: str,
    gemini_api: str,
    presta_api: str,
    presta_url: str,
    driver: Optional[Driver] = None,
) -> None:
    """
    Initializes SupplierToPrestashopProvider class with required components.

    Args:
        driver (Driver): Selenium WebDriver instance.

    """
```

**Описание**: Инициализирует класс `SupplierToPrestashopProvider` с необходимыми компонентами.

**Как работает функция**:
1.  Сохраняет переданные API ключи и URL в атрибуты экземпляра класса.
2.  Загружает конфигурационный файл `emil.json` в пространство имен `self.config`.
3.  Инициализирует текущую временную метку `self.timestamp`.
4.  Создает экземпляр `Driver` (если не передан) для управления браузером.
5.  Инициализирует AI модель Gemini с помощью метода `initialise_ai_model`.

**Параметры**:

*   `lang` (str): Язык, используемый в сценарии.
*   `gemini_api` (str): API ключ для доступа к Gemini.
*   `presta_api` (str): API ключ для доступа к Prestashop.
*   `presta_url` (str): URL адрес Prestashop.
*   `driver` (Optional\[Driver], optional): Экземпляр Selenium WebDriver. По умолчанию `None`.

**Возвращает**:

*   `None`

### `initialise_ai_model`

```python
def initialise_ai_model(self):
    """Инициализация модели Gemini"""
```

**Описание**: Инициализирует модель Gemini.

**Как работает функция**:
1.  Формирует путь к файлу с системной инструкцией для Gemini на основе языка `self.lang`.
2.  Читает содержимое файла с инструкцией.
3.  Создает экземпляр класса `GoogleGenerativeAI` с использованием API ключа, системной инструкции и конфигурации генерации.

**Параметры**:

*   `self`

**Возвращает**:

*   Возвращает экземпляр класса `GoogleGenerativeAI`.

**Вызывает исключения**:

*   `Exception`: Если не удается загрузить инструкции.

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

**Описание**: Выполняет сценарий: парсит продукты, обрабатывает их через AI и сохраняет данные.

**Как работает функция**:
1.  Инициализирует список `products_list` для хранения данных о товарах.
2.  Перебирает URL-ы товаров в списке `urls`.
3.  Для каждого URL определяет грабер (парсер) с помощью функции `get_graber_by_supplier_url`.
4.  Если грабер не найден, переходит к следующему URL.
5.  Извлекает данные о товаре с помощью грабера и сохраняет их в переменной `f`.
6.  Преобразует полученные данные с помощью метода `convert_product_fields`.
7.  Сохраняет преобразованные данные с помощью метода `save_product_data`.
8.  Добавляет данные о товаре в список `products_list`.

**Параметры**:

*   `urls` (list\[str]): Список URL-ов товаров.
*   `price` (Optional\[str], optional): Цена товара. По умолчанию ''.
*   `mexiron_name` (Optional\[str], optional): Название мехирона. По умолчанию ''.

**Возвращает**:

*   `bool`: `True`, если сценарий выполнен успешно, `False` в противном случае.

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> None:
    """
    Saves individual product data to a file.

    Args:
        product_data (dict): Formatted product data.
    """
```

**Описание**: Сохраняет отдельные данные о продукте в файл.

**Как работает функция**:
1.  Формирует путь к файлу для сохранения данных о товаре на основе `product_id`.
2.  Преобразует словарь `product_data` в JSON формат и сохраняет его в файл.

**Параметры**:

*   `product_data` (dict): Отформатированные данные о продукте.

**Возвращает**:

*   `True` в случае успешного сохранения, иначе `None`.

### `process_ai`

```python
async def process_ai(
    self, products_list: List[str], lang: str, attempts: int = 3
) -> tuple | bool:
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

**Описание**: Обрабатывает список продуктов через AI модель.

**Как работает функция**:
1.  Проверяет количество оставшихся попыток. Если их нет, возвращает пустой словарь.
2.  Формирует путь к файлу с инструкцией для модели на основе языка `lang`.
3.  Читает содержимое файла с инструкцией.
4.  Формирует запрос к модели, объединяя инструкцию и данные о продуктах.
5.  Отправляет запрос в AI модель и получает ответ.
6.  Если ответ пустой, логирует ошибку и возвращает пустой словарь.
7.  Парсит ответ модели в словарь.
8.  Если парсинг не удался, логирует ошибку и, если есть еще попытки, рекурсивно вызывает себя.

**Параметры**:

*   `products_list` (str): Список словарей с данными о продуктах в виде строки.
*   `lang` (str): Язык, на котором нужно получить ответ от модели.
*   `attempts` (int, optional): Количество попыток повтора запроса в случае неудачи. По умолчанию 3.

**Возвращает**:

*   `dict`: Обработанный ответ от модели в виде словаря.
*   `{}`: Если не удалось получить валидный ответ после всех попыток.

### `read_data_from_json`

```python
async def read_data_from_json(self):
    """Загружаю JSON файлы и фотки, которые я сделал через телеграм"""
```

**Описание**: Загружает JSON файлы и фотографии, полученные через Telegram.

**Как работает функция**:

1.  Загружает данные из JSON файла, расположенного по пути `self.local_images_path`.
2.  Выводит загруженные данные в консоль.

**Параметры**:

*   `self`

**Возвращает**:

*   `None`

### `save_in_prestashop`

```python
async def save_in_prestashop(
    self, products_list: ProductFields | list[ProductFields]
) -> bool:
    """Функция, которая сохраняет товары в Prestashop emil-design.com"""
```

**Описание**: Функция, которая сохраняет товары в Prestashop emil-design.com.

**Как работает функция**:

1.  Преобразует входной параметр `products_list` в список, если это не список.
2.  Создает экземпляр класса `PrestaProduct` с использованием API ключа и URL Prestashop.
3.  Перебирает элементы списка `products_list` и для каждого элемента вызывает метод `add_new_product` экземпляра `PrestaProduct`.

**Параметры**:

*   `products_list` (ProductFields | list\[ProductFields]): Список товаров для сохранения в Prestashop.

**Возвращает**:

*   `bool`: Всегда возвращает `True` после завершения процесса.

### `post_facebook`

```python
async def post_facebook(self, mexiron: SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
```

**Описание**: Функция исполняет сценарий рекламного модуля `facebook`.

**Как работает функция**:

1.  Открывает страницу Facebook.
2.  Формирует заголовок сообщения для публикации, объединяя название, описание и цену товара.
3.  Публикует заголовок сообщения.
4.  Загружает медиафайлы (изображения) для публикации.
5.  Публикует сообщение.

**Параметры**:

*   `mexiron` (SimpleNamespace): Объект с данными о мехироне (товаре).

**Возвращает**:

*   `bool`: `True` в случае успешной публикации, `False` в противном случае.

### `create_report`

```python
async def create_report(
    self, data: dict, lang: str, html_file: Path, pdf_file: Path
) -> bool:
    """Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
    Если мехорон в pdf создался (`generator.create_report()` вернул True) -
    отправить его боту
    """
```

**Описание**: Функция отправляет задание на создание мехирона в формате `html` и `pdf`.

**Как работает функция**:

1.  Создает экземпляр класса `ReportGenerator`.
2.  Вызывает метод `create_report` для генерации отчета в формате `html` и `pdf`.
3.  Если отчет создан успешно, проверяет существование и тип PDF файла.
4.  Отправляет PDF файл боту, используя `reply_document`.

**Параметры**:

*   `data` (dict): Данные для отчета.
*   `lang` (str): Язык отчета.
*   `html_file` (Path): Путь для сохранения HTML версии отчета.
*   `pdf_file` (Path): Путь для сохранения PDF версии отчета.

**Возвращает**:

*   `bool`: `True`, если отчет создан и отправлен успешно, `False` в противном случае.

## Функции

### `main`

```python
async def main(suppier_to_presta):
    """На данный момент функция читает JSON со списком фотографий , которые были получены от Эмиля"""
```

**Описание**: На данный момент функция читает JSON со списком фотографий, которые были получены от Эмиля.

**Как работает функция**:
1.  Устанавливает язык `lang` в значение `'he'`.
2.  Загружает данные о продуктах из JSON файла.
3.  Создает экземпляр класса `SupplierToPrestashopProvider`.
4.  Извлекает список продуктов из загруженных данных.
5.  Сохраняет продукты в Prestashop с помощью метода `save_in_prestashop`.

**Параметры**:

*   `suppier_to_presta`: Объект, который нигде не используется

**Примеры**:

```python
import asyncio
async def main():
    lang = 'he'
    products_ns = j_loads_ns(gs.path.external_storage / ENDPOINT / 'out_250108230345305_he.json')

    suppier_to_presta = SupplierToPrestashopProvider(lang)
    products_list:list = [f for f in products_ns]
    await suppier_to_presta.save_in_prestashop(products_list)

if __name__ == '__main__':
    asyncio.run(main())
```