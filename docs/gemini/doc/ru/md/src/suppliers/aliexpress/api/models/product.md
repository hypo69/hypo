# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Данный модуль содержит определение класса `Product`, представляющего собой модель продукта с AliExpress.  Класс содержит различные атрибуты, описывающие характеристики продукта, такие как цена, категория, URL и т.д.


## Классы

### `Product`

**Описание**: Класс `Product` описывает структуру данных для представления продукта с AliExpress.  Он содержит множество атрибутов, отражающих различные детали продукта, включая цены, категории, ссылки и прочую информацию.

**Атрибуты**:

- `app_sale_price` (str): Цена продукта по приложению.
- `app_sale_price_currency` (str): Валюта цены продукта по приложению.
- `commission_rate` (str): Ставка комиссии.
- `discount` (str): Скидка.
- `evaluate_rate` (str): Рейтинг оценки.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Ставка комиссии для горячих продуктов.
- `lastest_volume` (int): Последний объем продаж.  (Дублирование, вероятно, ошибка в исходном коде)
- `original_price` (str): Исходная цена.
- `original_price_currency` (str): Валюта исходной цены.
- `product_detail_url` (str): Ссылка на подробную страницу продукта.
- `product_id` (int): Идентификатор продукта.
- `product_main_image_url` (str): Ссылка на главное изображение продукта.
- `product_small_image_urls` (List[str]): Список ссылок на маленькие изображения продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): Ссылка на видео продукта.
- `promotion_link` (str): Ссылка на промоакцию.
- `relevant_market_commission_rate` (str): Ставка комиссии для релевантного рынка.
- `sale_price` (str): Цена со скидкой.
- `sale_price_currency` (str): Валюта цены со скидкой.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): Ссылка на страницу магазина.
- `target_app_sale_price` (str): Целевая цена продукта по приложению.
- `target_app_sale_price_currency` (str): Валюта целевой цены продукта по приложению.
- `target_original_price` (str): Целевая исходная цена.
- `target_original_price_currency` (str): Валюта целевой исходной цены.
- `target_sale_price` (str): Целевая цена со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены со скидкой.