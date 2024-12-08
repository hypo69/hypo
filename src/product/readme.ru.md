```rst
.. :module: src.product
```
[Root ↑](https://github.com/hypo69/hypo/blob/master/REDAME.MD)

[English](https://github.com/hypo69/hypo/blob/master/src/product/README.MD)
# Модуль hypotez/src/product/product.py

## Обзор

Модуль `src.product` определяет поведение продукта в проекте, обеспечивая взаимодействие между веб-сайтом, продуктом и API PrestaShop. Он использует классы из модулей `src.endpoints.prestashop`, `src.category`, и `src.product.product_fields`.

## Классы

### `Product`

**Описание**: Класс `Product` наследуется от `ProductFields` и `PrestaShop`, предоставляя методы для работы с продуктами.  Изначально собирает данные с страницы продукта и затем работает с API PrestaShop.

**Методы**:

- `__init__`: Инициализирует объект `Product`.
  
  **Параметры**:
   - `*args`: Переменная длина аргументов.
   - `**kwargs`: Произвольные именованные аргументы.

- `get_parent_categories`: Возвращает список родительских категорий для указанной категории.

### `ProductFields`

**Описание**:  Базовый класс для работы с полями продукта. (Описание класса `ProductFields` отсутствует в предоставленном коде, но будет нужно для полной документации)

### `PrestaShop`

**Описание**:  Класс для работы с API PrestaShop. (Описание класса `PrestaShop` отсутствует в предоставленном коде, но будет нужно для полной документации)


## Статические методы

### `get_parent_categories`

**Описание**:  Получает список родительских категорий для заданной категории по её ID. Дублирует функцию `get_parents` из класса `Category`.

**Параметры**:
 - `id_category` (int): ID категории.
 - `dept` (int, optional): Глубина категории. По умолчанию 0.

**Возвращает**:
 - list: Список родительских категорий.

**Возможные исключения**:
 - `TypeError`: Если `id_category` не является целым числом.

# Модуль hypotez/src/product/product_fields/product_fields.py

## Обзор

Модуль `hypotez/src/product/product_fields/product_fields.py` содержит класс `ProductFields`, предназначенный для работы с полями товаров в системе управления контентом PrestaShop. Класс предоставляет свойства и методы для доступа и изменения различных полей товара, а также для загрузки данных из файлов.  Документация описывает структуру таблиц PrestaShop, содержащих информацию о товарах, и методы работы с полями этих таблиц.

## Классы

### `ProductFields`

**Описание**: Класс `ProductFields` предоставляет методы и свойства для работы с полями товаров в базе данных PrestaShop. Он загружает данные полей из файлов и предоставляет методы доступа и изменения этих полей.

**Атрибуты**:

- `product_fields_list`: Список названий полей товара, загруженный из файла `fields_list.txt`.
- `language`: Словарь, содержащий соответствие между кодами языков и их идентификаторами в PrestaShop.
- `presta_fields`: Объект `SimpleNamespace`, содержащий поля товара.
- `assist_fields_dict`: Словарь дополнительных служебных полей (например, URL изображений).

**Методы**:

- `__init__(self)`: Инициализирует объект `ProductFields`. Загружает список полей, языки и дефолтные значения.
- `_load_product_fields_list(self) -> List[str]`: Загружает список полей из файла `fields_list.txt`.
- `_payload(self) -> bool`: Загружает дефолтные значения полей из файла `product_fields_default_values.json`. Возвращает `True`, если загрузка успешна, иначе `False`.


## Свойства

(Список свойств с подробными описаниями, параметрами, возвращаемыми значениями и исключениями)

### `id_product`

**Описание**:  `ID` товара. Для нового товара ID назначается из PrestaShop.

**Доступ**: `product_fields.id_product`

**Установление**: `product_fields.id_product = value`

**Параметры**:
- `value (int, optional)`:  Требуется при операциях над существующим товаром. `ps_product.id`. Для нового товара ID вернется из системы при занесении товара в базу данных.

**Возвращает**:
- `bool`: `True` если успешно, `False` в случае ошибки.


###  `id_supplier`, `id_manufacturer`, `id_category_default`, `id_shop_default`, `id_tax`, `on_sale`, `online_only`, `ean13`, `isbn`, `upc`, `mpn`, `ecotax`, `quantity`, `minimal_quantity`, `low_stock_threshold`, `low_stock_alert`, `price`, `wholesale_price`, `unity`, `unit_price_ratio`, `additional_shipping_cost`, `reference`, `supplier_reference`, `location`, `width`, `height`, `depth`, `weight`, `volume`, `out_of_stock`, `additional_delivery_times`, `quantity_discount`, `customizable`, `uploadable_files`, `text_fields`, `active`, `redirect_type`, `id_type_redirected`, `available_for_order`, `available_date`, `show_condition`, `condition`, `show_price`, `indexed`, `visibility`, `cache_is_pack`, `cache_has_attachments`, `is_virtual`, `cache_default_attribute`, `date_add`, `date_upd`, `advanced_stock_management`, `pack_stock_type`, `state`, `product_type`, `link_to_video`, `images_urls`

**Описание**:  Список остальных свойств с аналогичной структурой описания аргументов, параметров и возвращаемых значений, как и для `id_product`.  Подробности для каждого свойства находятся в его описании в коде.  Обратите внимание на сложную структуру данных для полей, связанных с языками (напр., `description`, `name`).
