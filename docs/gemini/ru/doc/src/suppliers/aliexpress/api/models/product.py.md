# Модуль `product`

## Обзор

Модуль `product` содержит класс `Product`, представляющий модель продукта AliExpress. Класс содержит атрибуты, описывающие различные характеристики продукта, такие как цена, скидка, URL, категория и т.д.

## Оглавление

- [Классы](#классы)
  - [Product](#product)

## Классы

### `Product`

**Описание**: Класс `Product` представляет модель продукта AliExpress со всеми его свойствами.

**Атрибуты**:
- `app_sale_price` (str): Цена продукта для мобильного приложения.
- `app_sale_price_currency` (str): Валюта цены продукта для мобильного приложения.
- `commission_rate` (str): Комиссионный процент.
- `discount` (str): Размер скидки.
- `evaluate_rate` (str): Рейтинг продукта.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Объем продаж.
- `hot_product_commission_rate` (str): Комиссионный процент для горячих товаров.
- `original_price` (str): Оригинальная цена продукта.
- `original_price_currency` (str): Валюта оригинальной цены продукта.
- `product_detail_url` (str): URL страницы с деталями продукта.
- `product_id` (int): ID продукта.
- `product_main_image_url` (str): URL главного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL-адресов маленьких изображений продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта.
- `promotion_link` (str): Ссылка на акцию.
- `relevant_market_commission_rate` (str): Комиссионный процент для конкретного рынка.
- `sale_price` (str): Цена продукта со скидкой.
- `sale_price_currency` (str): Валюта цены продукта со скидкой.
- `second_level_category_id` (int): ID категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): ID магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена продукта для мобильного приложения.
- `target_app_sale_price_currency` (str): Валюта целевой цены продукта для мобильного приложения.
- `target_original_price` (str): Целевая оригинальная цена продукта.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены продукта.
- `target_sale_price` (str): Целевая цена продукта со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены продукта со скидкой.