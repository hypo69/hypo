# ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ МОДУЛЯ `affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator` предназначен для получения полной информации о продуктах с помощью API AliExpress Affiliate. Он извлекает данные о продуктах, включая ссылки, изображения и видео, и сохраняет их локально. Класс `AliAffiliatedProducts` обрабатывает список URL-адресов или идентификаторов продуктов, извлекает данные о продуктах, сохраняет изображения и видео и записывает JSON данные в файл.

## Импорты и Зависимости

Модуль использует следующие импорты:

* **Стандартные библиотеки Python:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
* **Внешние библиотеки:** `gs`, `AliApi`, `Aliexpress`, `AffiliateLinksShortener`, `extract_prod_ids`, `ensure_https`, `csv2dict`, `j_dumps`, `save_png_from_url`, `save_video_from_url`, `pprint`, `read_text_file`, `save_text_file`, `logger`.

Эти импорты обеспечивают необходимые функциональности, такие как асинхронное программирование, обработка файлов, сохранение изображений и видео, работу с URL, запись JSON и логирование.


## Класс `AliAffiliatedProducts`

### Описание класса

```python
class AliAffiliatedProducts(AliApi):
    """Класс для сбора полной информации о продукте с URL-адресов или идентификаторов продуктов.
    locator_description Для более подробной информации о создании шаблонов для рекламных кампаний, см. раздел `Управление рекламными кампаниями Aliexpress`.
    @code
    # Пример использования:
    prod_urls = ['123', '456', ...]
    prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

Класс `AliAffiliatedProducts` наследуется от класса `AliApi`. Он отвечает за получение полной информации о продуктах, включая ссылки, изображения и видео.

### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

* `campaign_name`: Название рекламной кампании.
* `campaign_category`: Категория кампании (по умолчанию `None`).
* `campaign_path`: Путь к каталогу, где хранятся материалы кампании.
* `language`: Язык кампании (по умолчанию `'EN'`).
* `currency`: Валюта кампании (по умолчанию `'USD'`).

### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом берется по имени.
    @param campaign_category `Optional[str]`: Категория кампании (по умолчанию None).
    @param language `str`: Язык кампании (по умолчанию 'EN').
    @param currency `str`: Валюта кампании (по умолчанию 'USD').
    @param tracking_id `str`: Идентификатор отслеживания для API AliExpress.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

Инициализирует атрибуты класса, вызывая конструктор родительского класса `AliApi` и устанавливая путь к каталогу кампании.

### Методы

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """Обрабатывает список URL-адресов и возвращает список продуктов с аффилированными ссылками и сохраненными изображениями.

    :param prod_urls: Список URL-адресов или идентификаторов продуктов.
    :return: Список обработанных продуктов.
    """
    # ... (код метода)
```

Метод обрабатывает список URL-адресов, извлекая аффилированные ссылки, сохраняя изображения и видео, и сохраняет данные о продуктах локально.  Возвращает список объектов `SimpleNamespace` с данными о продуктах.

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """Удаляет продукт, для которого не найдена аффилированная ссылка."""
    # ... (код метода)
```

Метод удаляет информацию о продукте, если для него не найдена аффилированная ссылка.

## Функции (если есть)

... (Список функций, если они есть в модуле)

## Примечания

Подробная документация для каждого метода и атрибута должна содержать описание, параметры, возвращаемые значения и возможные исключения.