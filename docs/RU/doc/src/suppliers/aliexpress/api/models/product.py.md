# Модуль `product`

## Обзор

Модуль `product` содержит описание класса `Product`, представляющего модель данных товара с AliExpress.

## Оглавление

- [Классы](#классы)
    - [`Product`](#product)

## Классы

### `Product`

**Описание**: Класс `Product` представляет собой модель данных товара, полученного с AliExpress API. Он содержит информацию о цене, скидках, категориях, изображениях, ссылках и других характеристиках товара.

**Атрибуты**:

- `app_sale_price` (str): Цена товара для мобильного приложения.
- `app_sale_price_currency` (str): Валюта цены товара для мобильного приложения.
- `commission_rate` (str): Комиссионный процент.
- `discount` (str): Размер скидки на товар.
- `evaluate_rate` (str): Рейтинг оценки товара.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
-  `lastest_volume` (int): Последний объем продаж товара.
- `hot_product_commission_rate` (str): Комиссионный процент для горячего товара.
- `original_price` (str): Исходная цена товара.
- `original_price_currency` (str): Валюта исходной цены товара.
- `product_detail_url` (str): URL страницы с детальным описанием товара.
- `product_id` (int): ID товара.
- `product_main_image_url` (str): URL основного изображения товара.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений товара.
- `product_title` (str): Название товара.
- `product_video_url` (str): URL видео о товаре.
- `promotion_link` (str): Ссылка на продвижение товара.
- `relevant_market_commission_rate` (str): Комиссионный процент для конкретного рынка.
- `sale_price` (str): Цена товара со скидкой.
- `sale_price_currency` (str): Валюта цены товара со скидкой.
- `second_level_category_id` (int): ID категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): ID магазина, продающего товар.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена товара для мобильного приложения.
- `target_app_sale_price_currency` (str): Валюта целевой цены товара для мобильного приложения.
- `target_original_price` (str): Целевая исходная цена товара.
- `target_original_price_currency` (str): Валюта целевой исходной цены товара.
- `target_sale_price` (str): Целевая цена товара со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены товара со скидкой.