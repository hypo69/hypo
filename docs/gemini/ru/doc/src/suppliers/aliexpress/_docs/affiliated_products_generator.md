# Модуль `affiliated_products_generator.py`

## Обзор

Файл `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который отвечает за генерацию полных данных о продуктах из Aliexpress Affiliate API. Он основан на классе `AliApi` для обработки URL-адресов или идентификаторов продуктов и получения подробной информации о партнерских продуктах, включая сохранение изображений, видео и данных JSON.

## Подробнее

Этот модуль предназначен для извлечения и обработки данных о партнерских продуктах с платформы Aliexpress. Он использует API для получения информации о продуктах, включая партнерские ссылки, изображения и видео, и сохраняет эти данные локально для дальнейшего использования, например, в рекламных кампаниях.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов с использованием Aliexpress Affiliate API.

**Наследует**:
- `AliApi`: Класс `AliAffiliatedProducts` наследует от класса `AliApi`, что позволяет ему использовать функциональность для взаимодействия с API Aliexpress.

**Атрибуты**:
- `campaign_name` (str): Название рекламной кампании.
- `campaign_category` (Optional[str]): Категория кампании (по умолчанию `None`).
- `campaign_path` (Path): Путь к каталогу, где хранятся материалы кампании.
- `language` (str): Язык для кампании (по умолчанию `'EN'`).
- `currency` (str): Валюта для кампании (по умолчанию `'USD'`).

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliAffiliatedProducts`.
- `process_affiliate_products`: Обрабатывает список URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.
- `delete_product`: Удаляет продукт, у которого нет партнерской ссылки.

### `__init__`

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
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

**Назначение**: Инициализирует новый экземпляр класса `AliAffiliatedProducts`.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании. Используется для определения каталога с подготовленными материалами.
- `campaign_category` (Optional[str], optional): Категория кампании (по умолчанию `None`).
- `language` (str, optional): Язык для кампании (по умолчанию `'EN'`).
- `currency` (str, optional): Валюта для кампании (по умолчанию `'USD'`).
- `*args`: Произвольные позиционные аргументы, которые передаются в конструктор родительского класса.
- `**kwargs`: Произвольные именованные аргументы, которые передаются в конструктор родительского класса.

**Как работает функция**:

1. Вызывает конструктор родительского класса `AliApi` с параметрами `language` и `currency`.
2. Инициализирует атрибуты экземпляра класса: `campaign_name`, `campaign_category`, `language` и `currency`.
3. Формирует локаль (`locale`) на основе языка и валюты.
4. Определяет путь к каталогу кампании (`campaign_path`) на основе названия кампании и категории, используя структуру каталогов Google Drive.

```
A: Вызов конструктора родительского класса AliApi
│
B: Инициализация атрибутов экземпляра класса
│
C: Формирование локали на основе языка и валюты
│
D: Определение пути к каталогу кампании
```

**Примеры**:

```python
# Пример инициализации класса AliAffiliatedProducts
parser = AliAffiliatedProducts(
    campaign_name="my_campaign",
    campaign_category="electronics",
    language="RU",
    currency="RUB"
)
```

### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    ...
    _promotion_links: list = []
    _prod_urls: list = []
    promotional_prod_urls = ensure_https(prod_urls)
    print_flag = 'new_line'
    for prod_url in promotional_prod_urls:
        _link = super().get_affiliate_links(prod_url)
        if _link:
            _link = _link[0]    
        if hasattr(_link, 'promotion_link'):
            _promotion_links.append(_link.promotion_link)
            _prod_urls.append(prod_url)
            
            pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
            print_flag = 'inline'
        else:
            logger.info_red(f'Not found affiliate for {prod_url}')
    
    if not _promotion_links:
        logger.error('No affiliate products returned')
        return
    logger.info_red('Start receiving product details...')
    _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
    if not _affiliate_products:
        return 
    
    print_flag = 'new_line'
    for product, promotion_link in zip(_affiliate_products, _promotion_links):
        ...

        if not promotion_link:
            parsed_url = urlparse(product.promotion_link)
            query_params = parse_qs(parsed_url.query)
            aff_short_key = query_params.get('aff_short_key', [None])[0]
            if aff_short_key:
                product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'
            else:
                """ This product is not an affiliate"""
                self.delete_product(product.product_id)
                ...
        else:
            product.promotion_link = promotion_link
        
        image_path = self.campaign_path / 'images' / f"{product.product_id}.png"
        save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
        product.local_image_path = str(image_path)
        if len(product.product_video_url) > 1:
            parsed_url = urlparse(product.product_video_url)
            suffix = Path(parsed_url.path).suffix
            
            video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
            save_video_from_url(product.product_video_url, video_path, exc_info=False)
            product.local_video_path = str(video_path)

        pprint(f'caught product - {product.product_id}', end=print_flag)
        print_flag = 'inline'
        
        if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):
            logger.warning(f"""Failed to write dictionary: \n {pprint(product)} \n path: {self.campaign_path / self.locale / product.product_id}.json""", exc_info=False)
            ...
            continue
            
    pprint(f'caught {len(_affiliate_products)}', end='new_line')
    return _affiliate_products
```

**Назначение**: Обрабатывает список URL-адресов продуктов, получает партнерские ссылки, сохраняет изображения и видео, и сохраняет детали продукта.

**Параметры**:
- `prod_urls` (List[str]): Список URL-адресов или идентификаторов продуктов.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, представляющих обработанные продукты.

**Как работает функция**:

1. Инициализирует списки `_promotion_links` и `_prod_urls` для хранения партнерских ссылок и URL-адресов продуктов соответственно.
2. Преобразует URL-адреса продуктов в HTTPS, используя функцию `ensure_https`.
3. Итерируется по URL-адресам продуктов и получает партнерские ссылки с помощью метода `get_affiliate_links` родительского класса `AliApi`.
4. Если партнерская ссылка найдена, она добавляется в список `_promotion_links`, а URL-адрес продукта — в список `_prod_urls`.
5. Если партнерские ссылки не найдены, функция регистрирует ошибку и возвращает `None`.
6. Вызывает метод `retrieve_product_details` для получения деталей продукта.
7. Итерируется по продуктам и соответствующим партнерским ссылкам, сохраняет изображения и видео, и сохраняет детали продукта в файл JSON.
8. Если продукт не является партнерским, он удаляется с помощью метода `delete_product`.
9. Регистрирует информацию об успешной обработке каждого продукта.
10. Возвращает список обработанных продуктов.

```
A: Инициализация списков
│
B: Преобразование URL-адресов в HTTPS
│
C: Получение партнерских ссылок
│
D: Получение деталей продукта
│
E: Сохранение изображений и видео
│
F: Сохранение деталей продукта в JSON
│
G: Удаление не партнерских продуктов
│
H: Возврат списка обработанных продуктов
```

**Примеры**:

```python
# Пример обработки списка URL-адресов продуктов
prod_urls = [
    "https://www.aliexpress.com/item/1234567890.html",
    "https://www.aliexpress.com/item/0987654321.html"
]
products = parser.process_affiliate_products(prod_urls)
if products:
    for product in products:
        print(f"Product ID: {product.product_id}, Promotion Link: {product.promotion_link}")
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    ...
    _product_id = extract_prod_ids(product_id)
    
    product_path = self.campaign_path / 'sources.txt'
    prepared_product_path = self.campaign_path / '_sources.txt'
    products_list = read_text_file(product_path)
    if products_list:
        products_list = convert_list_to_homogeneous_list(products_list)
        for record in products_list:
            if _product_id:
                record_id = extract_prod_ids(record)
                if record_id == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), prepared_product_path)
                    break
            else:
                if record == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), product_path)
            
    else:
        product_path = self.campaign_path / 'sources' / f'{product_id}.html'    
        try:
            product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
            # product_path.unlink()
            logger.success(f"Product file {product_path} renamed successfully.")
        except FileNotFoundError as ex:
            logger.error(f"Product file {product_path} not found.", exc_info=exc_info)
        except Exception as ex:
            logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)                
    ...
```

**Назначение**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `product_id` (str): Идентификатор продукта, который нужно удалить.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли выводить информацию об исключении в лог (по умолчанию `False`).

**Как работает функция**:

1. Извлекает идентификатор продукта с помощью функции `extract_prod_ids`.
2. Определяет пути к файлам `sources.txt` и `_sources.txt` в каталоге кампании.
3. Читает содержимое файла `sources.txt` и, если файл существует, преобразует список продуктов в однородный список.
4. Итерируется по списку продуктов и удаляет продукт с соответствующим идентификатором.
5. Сохраняет обновленный список продуктов в файл `_sources.txt`.
6. Если файл `sources.txt` не существует, переименовывает файл продукта в каталоге `sources`.
7. Регистрирует информацию об успешном переименовании файла продукта.
8. Обрабатывает исключения `FileNotFoundError` и `Exception` при переименовании файла продукта.

```
A: Извлечение идентификатора продукта
│
B: Определение путей к файлам
│
C: Чтение содержимого файла sources.txt
│
D: Удаление продукта из списка
│
E: Сохранение обновленного списка в файл _sources.txt
│
F: Переименование файла продукта
│
G: Обработка исключений
```

**Примеры**:

```python
# Пример удаления продукта с идентификатором "1234567890"
parser.delete_product("1234567890")
```

## Функции

В данном файле не обнаружено отдельных функций, не являющихся методами класса.