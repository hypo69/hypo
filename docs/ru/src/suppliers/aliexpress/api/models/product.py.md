# Модуль: src.suppliers.aliexpress.api.models

## Обзор

Модуль `product.py` содержит определение класса `Product`, который используется для представления информации о продукте с AliExpress. Этот класс содержит атрибуты, описывающие различные характеристики продукта, такие как цена, скидка, рейтинг, изображения и ссылки.

## Подробнее

Этот код используется для хранения и передачи данных о продуктах, полученных через API AliExpress. Класс `Product` служит моделью данных, которая облегчает доступ к информации о продукте и её обработку.

## Классы

### `Product`

**Описание**: Класс `Product` представляет модель данных продукта с AliExpress. Он содержит атрибуты, соответствующие различным характеристикам продукта, таким как цены, скидки, изображения и ссылки.

**Принцип работы**:
Класс `Product` служит контейнером для хранения данных о продукте. Он определяет атрибуты, которые будут содержать информацию о продукте, полученную из API AliExpress.

**Атрибуты**:
- `app_sale_price` (str): Цена продукта в приложении.
- `app_sale_price_currency` (str): Валюта цены продукта в приложении.
- `commission_rate` (str): Комиссионный процент.
- `discount` (str): Размер скидки.
- `evaluate_rate` (str): Рейтинг продукта.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Комиссионный процент для популярных продуктов.
- `original_price` (str): Оригинальная цена продукта.
- `original_price_currency` (str): Валюта оригинальной цены продукта.
- `product_detail_url` (str): URL страницы с деталями продукта.
- `product_id` (int): ID продукта.
- `product_main_image_url` (str): URL главного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта.
- `promotion_link` (str): Ссылка на акцию продукта.
- `relevant_market_commission_rate` (str): Комиссионный процент для соответствующего рынка.
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

**Примеры**:

```python
# Пример создания экземпляра класса Product
product = Product()
product.product_title = 'Пример товара'
product.sale_price = '10.00'
product.sale_price_currency = 'USD'
print(f'Название товара: {product.product_title}, цена: {product.sale_price} {product.sale_price_currency}')
```
```output
Название товара: Пример товара, цена: 10.00 USD