# Модуль `affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который отвечает за генерацию полных данных о продуктах из Aliexpress Affiliate API. Он расширяет класс `AliApi` для обработки URL-адресов или идентификаторов продуктов и извлечения деталей об партнерских продуктах, включая сохранение изображений, видео и данных JSON.

## Подробнее

Этот код используется для автоматизации сбора информации о продуктах с AliExpress, предназначенных для рекламных кампаний. Он позволяет извлекать партнерские ссылки, сохранять медиа-контент и структурировать данные о продуктах для дальнейшего использования.

## Содержание

- [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
    - [Описание](#описание)
    - [Параметры](#параметры)
    - [Методы](#методы)
        - [`__init__`](#__init__)
        - [`process_affiliate_products`](#process_affiliate_products)
        - [`delete_product`](#delete_product)

## Классы

### `AliAffiliatedProducts`

```python
class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs
    locator_description For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`
    @code
    # Example usage:
    prod_urls = ['123','456',...]
    prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

**Описание**: Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов.

**Принцип работы**:
1.  Класс инициализируется с параметрами рекламной кампании, такими как имя, категория, язык и валюта.
2.  Метод `process_affiliate_products` принимает список URL-адресов продуктов или идентификаторов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.
3.  Внутри класса используются методы для получения партнерских ссылок, извлечения деталей продукта, сохранения изображений и видео.

**Параметры**:

*   `campaign_name` (str): Имя рекламной кампании.
*   `campaign_category` (Optional[str]): Категория для кампании (по умолчанию `None`).
*   `language` (str): Язык для кампании (по умолчанию `'EN'`).
*   `currency` (str): Валюта для кампании (по умолчанию `'USD'`).

**Методы**:

*   [`__init__`](#__init__): Инициализация класса.
*   [`process_affiliate_products`](#process_affiliate_products): Обработка списка URL-адресов продуктов.
*   [`delete_product`](#delete_product): Удаление продукта, у которого нет партнерской ссылки.

#### `__init__`

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

**Назначение**: Инициализация экземпляра класса `AliAffiliatedProducts`.

**Параметры**:

*   `campaign_name` (str): Имя рекламной кампании. Используется для определения директории с подготовленными материалами.
*   `campaign_category` (Optional[str], optional): Категория рекламной кампании (по умолчанию `None`).
*   `language` (str, optional): Язык кампании (по умолчанию `'EN'`).
*   `currency` (str, optional): Валюта кампании (по умолчанию `'USD'`).
*   `*args`: Произвольные позиционные аргументы.
*   `**kwargs`: Произвольные именованные аргументы.

**Как работает функция**:

1.  Вызывает конструктор родительского класса `AliApi` с параметрами `language` и `currency`.
2.  Сохраняет значения параметров `campaign_name`, `campaign_category`, `language` и `currency` в атрибутах экземпляра класса.
3.  Формирует атрибут `locale` как строку, объединяющую язык и валюту.
4.  Формирует путь к директории кампании `campaign_path` на основе имени и категории кампании. Путь строится с использованием атрибутов объекта `gs.path.google_drive`.

#### `process_affiliate_products`

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
        
        if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):\n            logger.warning(f"""Failed to write dictionary: \\n {pprint(product)} \\n path: {self.campaign_path / self.locale / product.product_id}.json""", exc_info=False)\n            ...\n            continue
            
    pprint(f'caught {len(_affiliate_products)}', end='new_line')
    return _affiliate_products
```

**Назначение**: Обрабатывает список URL-адресов продуктов или идентификаторов, чтобы получить партнерские ссылки, сохранить изображения и видео, а также сохранить детали продукта.

**Параметры**:

*   `prod_urls` (List[str]): Список URL-адресов продуктов или идентификаторов.

**Возвращает**:

*   List[SimpleNamespace]: Список объектов `SimpleNamespace`, представляющих обработанные продукты.

**Как работает функция**:

1.  Инициализирует пустые списки `_promotion_links` и `_prod_urls`.
2.  Преобразует URL-адреса продуктов в HTTPS, используя функцию `ensure_https`.
3.  Перебирает URL-адреса продуктов:

    *   Получает партнерские ссылки, вызывая метод `get_affiliate_links` родительского класса.
    *   Если партнерская ссылка найдена, добавляет ее в список `_promotion_links`, а URL-адрес продукта - в список `_prod_urls`.
    *   Выводит информацию о найденной партнерской ссылке.
    *   Если партнерская ссылка не найдена, записывает информацию об этом в журнал.
4.  Если список партнерских ссылок пуст, записывает ошибку в журнал и возвращает `None`.
5.  Записывает информацию в журнал о начале получения деталей продукта.
6.  Извлекает детали продукта, вызывая метод `retrieve_product_details`.
7.  Перебирает продукты и партнерские ссылки:

    *   Если партнерская ссылка отсутствует, пытается извлечь `aff_short_key` из URL-адреса продукта.
    *   Если `aff_short_key` найден, формирует партнерскую ссылку на его основе.
    *   Если `aff_short_key` не найден, удаляет продукт, вызывая метод `delete_product`.
    *   Если партнерская ссылка присутствует, присваивает ее продукту.
    *   Формирует путь для сохранения изображения продукта и сохраняет изображение с использованием функции `save_png_from_url`.
    *   Формирует путь для сохранения видео продукта и сохраняет видео с использованием функции `save_video_from_url`.
    *   Сохраняет информацию о продукте в формате JSON, используя функцию `j_dumps`.

8.  Возвращает список обработанных продуктов.

#### `delete_product`

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

*   `product_id` (str): Идентификатор продукта.
*   `exc_info` (bool, optional): Определяет, нужно ли выводить служебную информацию об ошибке (по умолчанию `False`).

**Как работает функция**:

1.  Извлекает идентификатор продукта, используя функцию `extract_prod_ids`.
2.  Определяет пути к файлам `sources.txt` и `_sources.txt`, содержащим список продуктов.
3.  Читает содержимое файла `sources.txt` с использованием функции `read_text_file`.
4.  Если список продуктов не пуст:

    *   Преобразует список продуктов в однородный список, используя функцию `convert_list_to_homogeneous_list`.
    *   Перебирает записи в списке продуктов:
        *   Если идентификатор продукта был успешно извлечен:
            *   Извлекает идентификатор текущей записи.
            *   Если идентификатор текущей записи соответствует заданному `product_id`, удаляет запись из списка и сохраняет обновленный список в файл `_sources.txt`.
        *   В противном случае, если текущая запись соответствует `product_id`, удаляет запись из списка и сохраняет обновленный список в файл `sources.txt`.

5.  Если список продуктов пуст:

    *   Определяет путь к HTML-файлу продукта.
    *   Пытается переименовать HTML-файл продукта, добавляя символ `_` к имени файла.
    *   Записывает информацию об успешном переименовании файла в журнал.
    *   В случае возникновения исключения `FileNotFoundError`, записывает информацию об ошибке в журнал.
    *   В случае возникновения другого исключения, записывает критическую ошибку в журнал.