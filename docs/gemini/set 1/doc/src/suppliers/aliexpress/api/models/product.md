# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Этот модуль содержит определение класса `Product`, представляющего данные о продукте, полученные с сайта AliExpress.  Класс содержит различные поля, описывающие характеристики продукта, такие как цена, категория, URL и т.д.

## Классы

### `Product`

**Описание**: Класс `Product` предназначен для хранения и представления данных о продукте AliExpress.  Он содержит множество атрибутов, описывающих различные аспекты продукта.

**Атрибуты**:

- `app_sale_price` (str): Цена продукта в приложении.
- `app_sale_price_currency` (str): Валюта цены в приложении.
- `commission_rate` (str): Комиссионная ставка.
- `discount` (str): Скидка.
- `evaluate_rate` (str): Рейтинг оценки.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Комиссионная ставка для популярных товаров.
- `lastest_volume` (int): Последний объем продаж. (Повторное определение, вероятно ошибка в исходном коде)
- `original_price` (str): Исходная цена.
- `original_price_currency` (str): Валюта исходной цены.
- `product_detail_url` (str): Ссылка на подробную страницу продукта.
- `product_id` (int): Идентификатор продукта.
- `product_main_image_url` (str): URL основного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL изображений меньшего размера.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта (если есть).
- `promotion_link` (str): Ссылка на акцию/предложение.
- `relevant_market_commission_rate` (str): Комиссионная ставка, релевантная рынку.
- `sale_price` (str): Цена со скидкой.
- `sale_price_currency` (str): Валюта цены со скидкой.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): Ссылка на страницу магазина.
- `target_app_sale_price` (str): Целевая цена продукта в приложении.
- `target_app_sale_price_currency` (str): Валюта целевой цены в приложении.
- `target_original_price` (str): Целевая исходная цена.
- `target_original_price_currency` (str): Валюта целевой исходной цены.
- `target_sale_price` (str): Целевая цена со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены со скидкой.


## Функции

(В данном файле нет определений функций)


**Примечания**:  Необходимо убедиться, что все типы данных (`str`, `int`, `List`) соответствуют ожиданиям при использовании данных из класса.  Повторное объявление `lastest_volume`  может быть ошибкой в исходном коде.