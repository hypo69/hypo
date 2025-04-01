# Документация модуля `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, предназначенный для сбора полных данных о товарах из API Aliexpress Affiliate. Он расширяет класс `AliApi` для обработки URL-адресов или идентификаторов товаров и получения подробной информации об аффилированных продуктах, включая сохранение изображений, видео и данных JSON.

## Подробнее

Этот модуль является частью проекта `hypotez` и служит для автоматизации процесса получения информации о товарах с AliExpress через Affiliate API. Он используется для создания рекламных кампаний, требующих детальной информации о продуктах, включая изображения и видео.

## Содержание

1.  [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
    *   [Описание](#описание)
    *   [Атрибуты](#атрибуты)
    *   [Метод `__init__`](#метод-__init__)
    *   [Метод `process_affiliate_products`](#метод-process_affiliate_products)
    *   [Метод `delete_product`](#метод-delete_product)
2.  [Импортируемые модули](#импортируемые-модули)

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о товарах из URL-адресов или идентификаторов товаров, используя API Aliexpress Affiliate.

**Принцип работы**:

1.  Инициализируется с именем рекламной кампании, категорией, языком и валютой.
2.  Использует API Aliexpress для получения аффилированных ссылок на товары.
3.  Сохраняет изображения и видео товаров локально.
4.  Сохраняет данные о товарах в формате JSON.

**Наследует**:

*   `AliApi`: Класс, предоставляющий базовые функции для взаимодействия с API Aliexpress.

**Атрибуты**:

*   `campaign_name` (str): Имя рекламной кампании.
*   `campaign_category` (Optional[str]): Категория кампании (по умолчанию `None`).
*   `campaign_path` (Path): Путь к каталогу, где хранятся материалы кампании.
*   `language` (str): Язык для кампании (по умолчанию `'EN'`).
*   `currency` (str): Валюта для кампании (по умолчанию `'USD'`).
*   `locale` (str): Локаль для кампании, формируется как `"{language}_{currency}"`.

### Метод `__init__`

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Name of the advertising campaign. The directory with the prepared material is taken by name.
    @param campaign_category `Optional[str]`: Category for the campaign (default None).
    @param language `str`: Language for the campaign (default 'EN').
    @param currency `str`: Currency for the campaign (default 'USD').
    @param tracking_id `str`: Tracking ID for Aliexpress API.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `AliAffiliatedProducts`.

**Параметры**:

*   `campaign_name` (str): Имя рекламной кампании.
*   `campaign_category` (Optional[str], optional): Категория для кампании (по умолчанию `None`).
*   `language` (str, optional): Язык для кампании (по умолчанию `'EN'`).
*   `currency` (str, optional): Валюта для кампании (по умолчанию `'USD'`).
*   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса.
*   `**kwargs`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса.

**Как работает метод**:

1.  Вызывает конструктор родительского класса `AliApi` с параметрами `language` и `currency`.
2.  Сохраняет переданные параметры в атрибуты экземпляра класса.
3.  Формирует путь к каталогу кампании на основе имени и категории кампании.

**Примеры**:

```python
parser = AliAffiliatedProducts(
    campaign_name='test_campaign',
    campaign_category='electronics',
    language='RU',
    currency='RUB'
)
```

### Метод `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    ...
```

**Назначение**: Обрабатывает список URL-адресов продуктов для получения аффилированных ссылок, сохранения изображений и видео, а также сохранения деталей продукта.

**Параметры**:

*   `prod_urls` (List[str]): Список URL-адресов или идентификаторов продуктов.

**Возвращает**:

*   List[SimpleNamespace]: Список объектов `SimpleNamespace`, представляющих обработанные продукты.

**Как работает метод**:

1.  Инициализирует списки для хранения аффилированных ссылок и URL-адресов продуктов.
2.  Применяет функцию `ensure_https` для обеспечения использования HTTPS в URL-адресах продуктов.
3.  Итерируется по URL-адресам продуктов, получая аффилированные ссылки с помощью метода `get_affiliate_links` родительского класса `AliApi`.
4.  Сохраняет аффилированные ссылки и URL-адреса продуктов в соответствующие списки.
5.  Вызывает метод `retrieve_product_details` для получения детальной информации о продуктах.
6.  Итерируется по полученным продуктам и аффилированным ссылкам, сохраняя изображения и видео продуктов локально.
7.  Сохраняет информацию о продукте в формате JSON.

```text
process_affiliate_products
│
├───> Инициализация списков _promotion_links, _prod_urls
│
├───> Обеспечение HTTPS для URL-адресов продуктов
│
├───> Итерация по URL-адресам продуктов
│   │
│   └───> Получение аффилированной ссылки с помощью get_affiliate_links
│   │
│   └───> Если аффилированная ссылка найдена:
│       │   └───> Добавление ссылки и URL в списки
│       │   └───> Вывод сообщения об успехе
│   │
│   └───> Если аффилированная ссылка не найдена:
│       │   └───> Логирование ошибки
│
├───> Получение детальной информации о продуктах с помощью retrieve_product_details
│
├───> Итерация по продуктам и аффилированным ссылкам
│   │
│   └───> Если аффилированная ссылка отсутствует:
│       │   └───> Попытка извлечения из параметров URL
│       │   └───> Если не удалось, удаление продукта
│   │
│   └───> Сохранение изображения продукта локально
│   │
│   └───> Сохранение видео продукта локально
│   │
│   └───> Сохранение информации о продукте в формате JSON
│
└───> Возврат списка обработанных продуктов
```

**Примеры**:

```python
prod_urls = ['https://www.aliexpress.com/item/1234567890.html']
products = parser.process_affiliate_products(prod_urls)
if products:
    print(f"Обработанные продукты: {products}")
```

### Метод `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    ...
```

**Назначение**: Удаляет информацию о продукте, для которого не найдена аффилированная ссылка.

**Параметры**:

*   `product_id` (str): Идентификатор продукта.
*   `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении (по умолчанию `False`).

**Как работает метод**:

1.  Извлекает идентификатор продукта с помощью функции `extract_prod_ids`.
2.  Формирует пути к файлам, связанным с продуктом.
3.  Пытается удалить запись о продукте из файла `sources.txt`.
4.  Если файл `sources.txt` не найден, пытается переименовать файл продукта.
5.  Логирует результаты операций.

```text
delete_product
│
├───> Извлечение идентификатора продукта
│
├───> Формирование путей к файлам продукта
│
├───> Чтение файла sources.txt
│   │
│   └───> Если файл существует:
│       │   └───> Удаление записи о продукте из списка
│       │   └───> Сохранение обновленного списка
│
├───> Если файл sources.txt не существует:
│   │
│   └───> Переименование файла продукта
│
└───> Логирование результатов
```

**Примеры**:

```python
parser.delete_product(product_id='1234567890')
```

## Импортируемые модули

*   `asyncio`: Для поддержки асинхронного программирования.
*   `itertools.count`: Для создания итераторов.
*   `math.log`: Для математических операций.
*   `pathlib.Path`: Для работы с путями к файлам и каталогам.
*   `typing.List`, `typing.Union`, `typing.Optional`: Для аннотации типов.
*   `types.SimpleNamespace`: Для создания простых объектов с атрибутами.
*   `urllib.parse.urlparse`, `urllib.parse.parse_qs`: Для разбора URL-адресов.
*   `src.gs`: Модуль, содержащий глобальные настройки проекта.
*   `src.suppliers.aliexpress.AliApi`: Базовый класс для взаимодействия с API Aliexpress.
*   `src.suppliers.aliexpress.Aliexpress`: Модуль, содержащий общие функции для работы с Aliexpress.
*   `src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver.AffiliateLinksShortener`: Класс для сокращения аффилированных ссылок через webdriver.
*   `src.suppliers.aliexpress.utils.extract_product_id.extract_prod_ids`: Функция для извлечения идентификаторов продуктов из URL-адресов.
*   `src.suppliers.aliexpress.utils.set_full_https.ensure_https`: Функция для обеспечения использования HTTPS в URL-адресах.
*   `src.utils.convertor.csv2json.csv2dict`: Функция для преобразования CSV в словарь.
*   `src.utils.jjson.j_dumps`: Функция для записи данных в формате JSON.
*   `src.utils.save_png_from_url`, `src.utils.save_video_from_url`: Функции для сохранения изображений и видео из URL-адресов.
*   `src.utils.printer.pprint`: Функция для красивой печати данных.
*   `src.utils.file.read_text_file`, `src.utils.file.save_text_file`: Функции для чтения и записи текстовых файлов.
*   `src.logger.logger.logger`: Модуль для логирования событий.