# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Этот модуль содержит определение класса `Product`, представляющего данные о продукте с AliExpress.  Класс хранит различные атрибуты, такие как цена, валюта, ID категории, URL изображения и т.д.

## Оглавление

* [Классы](#классы)
    * [Product](#product)


## Классы

### `Product`

**Описание**: Представляет данные о продукте с AliExpress.

**Атрибуты**:

- `app_sale_price` (str): Цена товара в приложении.
- `app_sale_price_currency` (str): Валюта цены товара в приложении.
- `commission_rate` (str): Процентная ставка комиссии.
- `discount` (str): Скидка.
- `evaluate_rate` (str): Рейтинг оценки.
- `first_level_category_id` (int): ID первой категории.
- `first_level_category_name` (str): Название первой категории.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Процентная ставка комиссии для популярных продуктов.
- `lastest_volume` (int): Последний объем продаж (повторение).  Вероятно, ошибка в коде.
- `original_price` (str): Исходная цена товара.
- `original_price_currency` (str): Валюта исходной цены товара.
- `product_detail_url` (str): URL страницы с подробной информацией о товаре.
- `product_id` (int): ID товара.
- `product_main_image_url` (str): URL основного изображения товара.
- `product_small_image_urls` (List[str]): Список URL-адресов маленьких изображений товара.
- `product_title` (str): Название товара.
- `product_video_url` (str): URL видео товара (если есть).
- `promotion_link` (str): Ссылка на акцию/промо.
- `relevant_market_commission_rate` (str): Процентная ставка комиссии для соответствующего рынка.
- `sale_price` (str): Цена товара со скидкой.
- `sale_price_currency` (str): Валюта цены товара со скидкой.
- `second_level_category_id` (int): ID второй категории.
- `second_level_category_name` (str): Название второй категории.
- `shop_id` (int): ID магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Ценовая цель для цены в приложении.
- `target_app_sale_price_currency` (str): Валюта целевой цены в приложении.
- `target_original_price` (str): Целевая исходная цена.
- `target_original_price_currency` (str): Валюта целевой исходной цены.
- `target_sale_price` (str): Целевая цена со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены со скидкой.


**Примечания**:  Повторение поля `lastest_volume` в определении класса указывает на потенциальную ошибку в исходном коде.  Важно проверить и исправить эту ошибку, чтобы избежать нежелательных проблем в обработке данных.