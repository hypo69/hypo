# Модуль `hypotez/src/suppliers/aliexpress/api/models/__init__.py`

## Обзор

Данный модуль инициализирует пакет `models` и предоставляет доступ к различным моделям данных, используемым в API AliExpress. Он импортирует классы и перечисления, представляющие языки, валюты, параметры запросов, аффилированные ссылки, горячие товары, продукты и категории.

## Оглавление

1. [Импортированные модули](#импортированные-модули)
2. [Перечисления](#перечисления)
   - [Language](#language)
   - [Currency](#currency)
   - [ProductType](#producttype)
   - [SortBy](#sortby)
   - [LinkType](#linktype)
3. [Модели данных](#модели-данных)
   - [AffiliateLink](#affiliatelink)
   - [HotProductsResponse](#hotproductsresponse)
   - [Product](#product)
   - [Category](#category)
   - [ChildCategory](#childcategory)

## Импортированные модули

Этот раздел описывает модули, импортированные в данном файле.

- `from .languages import Language`: Импортирует перечисление `Language` из модуля `languages.py`.
- `from .currencies import Currency`: Импортирует перечисление `Currency` из модуля `currencies.py`.
- `from .request_parameters import ProductType, SortBy, LinkType`: Импортирует перечисления `ProductType`, `SortBy` и `LinkType` из модуля `request_parameters.py`.
- `from .affiliate_link import AffiliateLink`: Импортирует класс `AffiliateLink` из модуля `affiliate_link.py`.
- `from .hotproducts import HotProductsResponse`: Импортирует класс `HotProductsResponse` из модуля `hotproducts.py`.
- `from .product import Product`: Импортирует класс `Product` из модуля `product.py`.
- `from .category import Category, ChildCategory`: Импортирует классы `Category` и `ChildCategory` из модуля `category.py`.

## Перечисления

### `Language`

**Описание**: Перечисление, представляющее языки.

**Импорт**: `from .languages import Language`

### `Currency`

**Описание**: Перечисление, представляющее валюты.

**Импорт**: `from .currencies import Currency`

### `ProductType`

**Описание**: Перечисление, представляющее типы продуктов.

**Импорт**: `from .request_parameters import ProductType`

### `SortBy`

**Описание**: Перечисление, представляющее способы сортировки.

**Импорт**: `from .request_parameters import SortBy`

### `LinkType`

**Описание**: Перечисление, представляющее типы ссылок.

**Импорт**: `from .request_parameters import LinkType`

## Модели данных

### `AffiliateLink`

**Описание**: Класс, представляющий аффилированную ссылку.

**Импорт**: `from .affiliate_link import AffiliateLink`

### `HotProductsResponse`

**Описание**: Класс, представляющий ответ с горячими продуктами.

**Импорт**: `from .hotproducts import HotProductsResponse`

### `Product`

**Описание**: Класс, представляющий продукт.

**Импорт**: `from .product import Product`

### `Category`

**Описание**: Класс, представляющий категорию.

**Импорт**: `from .category import Category`

### `ChildCategory`

**Описание**: Класс, представляющий подкатегорию.

**Импорт**: `from .category import ChildCategory`