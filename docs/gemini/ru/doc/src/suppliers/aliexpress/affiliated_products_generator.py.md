# Модуль `src.suppliers.aliexpress.affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator.py` предназначен для сбора и обработки данных о товарах с AliExpress, включая получение партнерских ссылок, сохранение изображений и видео, а также генерацию HTML-страниц для рекламных кампаний.

## Содержание

- [Классы](#классы)
    - [`AliAffiliatedProducts`](#aliaffiliatedproducts)
- [Функции](#функции)
    - [`__init__`](#__init__)
    - [`process_affiliate_products`](#process_affiliate_products)

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о товарах с AliExpress по URL-адресам или идентификаторам товаров. Подробности о создании шаблонов для рекламных кампаний см. в разделе "Управление рекламными кампаниями Aliexpress".

**Поля**:
- `language` (str): Язык для рекламной кампании.
- `currency` (str): Валюта для рекламной кампании.

**Методы**:
- [`__init__`](#__init__): Инициализирует класс `AliAffiliatedProducts`.
- [`process_affiliate_products`](#process_affiliate_products): Обрабатывает список идентификаторов или URL-адресов товаров и возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

## Функции

### `__init__`

**Описание**: Инициализирует класс `AliAffiliatedProducts`.

**Параметры**:
- `language` (str | dict, optional): Язык для кампании (по умолчанию 'EN').
- `currency` (str, optional): Валюта для кампании (по умолчанию 'USD').
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

### `process_affiliate_products`

**Описание**: Обрабатывает список идентификаторов или URL-адресов товаров и возвращает список товаров с партнерскими ссылками и сохраненными изображениями.

**Параметры**:
- `prod_ids` (list[str]): Список URL-адресов или идентификаторов товаров.
- `category_root` (Path | str): Корневой путь к каталогу категории.

**Возвращает**:
- `list[SimpleNamespace]`: Список обработанных товаров с партнерскими ссылками и сохраненными изображениями.

**Вызывает исключения**:
- `Exception`: Если имя категории не найдено в кампании.

**Примечания**:
- Получает содержимое страниц по URL-адресам.
- Обрабатывает партнерские ссылки и сохраняет изображения/видео.
- Генерирует и сохраняет данные кампании и выходные файлы.

**Блок-схема**:
```
┌───────────────────────────────────────────────┐
│ Start                                         │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ Try to get category from campaign using `category_name` │
└─────────────────────────────────────────────────────────┘
                            │
                            ┴───────────────────────────────────────────┐
                            │                                           │
                            ▼                                           ▼
┌──────────────────────────────────────────────────────┐
│ Campaign Category found: Initialize paths,           │
│ set promotional URLs, and process products           │
└──────────────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ No category found: Create default category    │
│ and initialize paths, set promotional URLs,   │
│ and process products                          │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Initialize paths and prepare data structures  │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Process products URLs to get affiliate links  │
└───────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────────────────────┐
                │                                       │
                ▼                                       ▼
┌─────────────────────────────────────────────┐
│ No affiliate links found: Log warning       │
└─────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Retrieve product details for affiliate URLs   │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Process each product and save images/videos   │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Prepare and save final output data            │
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ Return list of affiliated products            │    
└───────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────┐
│ End                                           │
└───────────────────────────────────────────────┘
```