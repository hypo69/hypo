# Модуль `product`

## Обзор

Модуль `product` содержит класс `Product`, который представляет собой модель данных для информации о продукте с AliExpress. Этот класс используется для хранения различных атрибутов продукта, таких как цена, валюта, комиссия, скидка, рейтинг, категории, объемы продаж, изображения, URL-адреса и т.д.

## Подробней

Этот модуль предназначен для структурированного хранения и передачи данных о продуктах, полученных из API AliExpress. Класс `Product` служит контейнером для всех значимых характеристик товара, что упрощает доступ к ним и их обработку в других частях проекта `hypotez`.

## Классы

### `Product`

**Описание**: Класс `Product` представляет собой модель данных для информации о продукте с AliExpress.

**Параметры**:
- `app_sale_price` (str): Цена продукта в приложении.
- `app_sale_price_currency` (str): Валюта цены продукта в приложении.
- `commission_rate` (str): Комиссионные отчисления.
- `discount` (str): Скидка на продукт.
- `evaluate_rate` (str): Рейтинг продукта.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Комиссионные отчисления для популярных продуктов.
- `original_price` (str): Оригинальная цена продукта.
- `original_price_currency` (str): Валюта оригинальной цены продукта.
- `product_detail_url` (str): URL страницы с деталями продукта.
- `product_id` (int): ID продукта.
- `product_main_image_url` (str): URL главного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта.
- `promotion_link` (str): Ссылка на акцию продукта.
- `relevant_market_commission_rate` (str): Комиссионные отчисления для соответствующего рынка.
- `sale_price` (str): Цена продукта со скидкой.
- `sale_price_currency` (str): Валюта цены продукта со скидкой.
- `second_level_category_id` (int): ID категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): ID магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена продукта в приложении.
- `target_app_sale_price_currency` (str): Валюта целевой цены продукта в приложении.
- `target_original_price` (str): Целевая оригинальная цена продукта.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены продукта.
- `target_sale_price` (str): Целевая цена продукта со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены продукта со скидкой.

**Примеры**

```python
from typing import List

class Product:
    app_sale_price: str
    app_sale_price_currency: str
    commission_rate: str
    discount: str
    evaluate_rate: str
    first_level_category_id: int
    first_level_category_name: str
    lastest_volume: int
    hot_product_commission_rate: str
    lastest_volume: int
    original_price: str
    original_price_currency: str
    product_detail_url: str
    product_id: int
    product_main_image_url: str
    product_small_image_urls: List[str]
    product_title: str
    product_video_url: str
    promotion_link: str
    relevant_market_commission_rate: str
    sale_price: str
    sale_price_currency: str
    second_level_category_id: int
    second_level_category_name: str
    shop_id: int
    shop_url: str
    target_app_sale_price: str
    target_app_sale_price_currency: str
    target_original_price: str
    target_original_price_currency: str
    target_sale_price: str
    target_sale_price_currency: str

# Пример создания экземпляра класса Product
product = Product()
product.product_title = "Example Product"
product.sale_price = "25.00"
product.sale_price_currency = "USD"

print(f"Product: {product.product_title}, Price: {product.sale_price} {product.sale_price_currency}")
```