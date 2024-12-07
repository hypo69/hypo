# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Этот модуль содержит определение класса `Product`, представляющего данные о продукте с AliExpress.  Класс содержит различные атрибуты, описывающие характеристики продукта, такие как цена, категория, изображения и т.д.

## Оглавление

- [Классы](#классы)
    - [Product](#product)


## Классы

### `Product`

**Описание**: Класс `Product` представляет данные о продукте с AliExpress. Он содержит различные поля, описывающие характеристики продукта.

**Атрибуты**:

- `app_sale_price` (str): Цена продукта по приложению.
- `app_sale_price_currency` (str): Валюта цены продукта по приложению.
- `commission_rate` (str): Ставка комиссии.
- `discount` (str): Скидка.
- `evaluate_rate` (str): Рейтинг оценки.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Ставка комиссии для популярных товаров.
- `lastest_volume` (int): Последний объем продаж. (Повторение, возможно, ошибка в исходном коде.)
- `original_price` (str): Исходная цена продукта.
- `original_price_currency` (str): Валюта исходной цены продукта.
- `product_detail_url` (str): Ссылка на страницу подробного описания продукта.
- `product_id` (int): Идентификатор продукта.
- `product_main_image_url` (str): URL основного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL-адресов малых изображений продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта (если есть).
- `promotion_link` (str): Ссылка на промоакцию (если есть).
- `relevant_market_commission_rate` (str): Ставка комиссии для данного рынка.
- `sale_price` (str): Цена продажи продукта.
- `sale_price_currency` (str): Валюта цены продажи продукта.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): Ссылка на магазин.
- `target_app_sale_price` (str): Целевая цена продукта по приложению.
- `target_app_sale_price_currency` (str): Валюта целевой цены по приложению.
- `target_original_price` (str): Целевая исходная цена продукта.
- `target_original_price_currency` (str): Валюта целевой исходной цены.
- `target_sale_price` (str): Целевая цена продажи продукта.
- `target_sale_price_currency` (str): Валюта целевой цены продажи.