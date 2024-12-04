# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Модуль `product.py` содержит определение класса `Product`, представляющего собой модель данных для продукта с AliExpress.  Класс содержит атрибуты для хранения различных характеристик продукта, включая цены, категории, ссылки и т.д.


## Классы

### `Product`

**Описание**: Класс `Product` описывает структуру данных для представления информации о продукте с AliExpress.

**Атрибуты**:

- `app_sale_price` (str): Цена приложения.
- `app_sale_price_currency` (str): Валюта цены приложения.
- `commission_rate` (str): Ставка комиссии.
- `discount` (str): Скидка.
- `evaluate_rate` (str): Рейтинг оценки.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем.
- `hot_product_commission_rate` (str): Ставка комиссии для горячих продуктов.
- `lastest_volume` (int): Последний объем.
- `original_price` (str): Исходная цена.
- `original_price_currency` (str): Валюта исходной цены.
- `product_detail_url` (str): Ссылка на страницу подробностей продукта.
- `product_id` (int): Идентификатор продукта.
- `product_main_image_url` (str): Ссылка на основное изображение продукта.
- `product_small_image_urls` (List[str]): Список ссылок на маленькие изображения продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): Ссылка на видео продукта.
- `promotion_link` (str): Ссылка на акцию.
- `relevant_market_commission_rate` (str): Ставка комиссии для релевантного рынка.
- `sale_price` (str): Цена продажи.
- `sale_price_currency` (str): Валюта цены продажи.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): Ссылка на магазин.
- `target_app_sale_price` (str): Целевая цена приложения.
- `target_app_sale_price_currency` (str): Целевая валюта цены приложения.
- `target_original_price` (str): Целевая исходная цена.
- `target_original_price_currency` (str): Целевая валюта исходной цены.
- `target_sale_price` (str): Целевая цена продажи.
- `target_sale_price_currency` (str): Целевая валюта цены продажи.


## Функции

(В данном файле нет определенных функций, только класс `Product`)


**Примечание:**  Код содержит повторяющийся атрибут `lastest_volume`.  Рекомендуется исправить это для повышения читаемости и соответствия наименованиям.