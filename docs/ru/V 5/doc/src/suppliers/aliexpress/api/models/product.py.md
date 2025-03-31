# Модуль `product`

## Обзор

Модуль содержит класс `Product`, который представляет модель продукта, полученную из API AliExpress. Он включает в себя атрибуты, описывающие основные характеристики товара, такие как цена, скидка, категория, изображения и ссылки.

## Подробней

Этот модуль используется для определения структуры данных, представляющей продукт AliExpress. Класс `Product` содержит атрибуты, соответствующие различным полям, возвращаемым API AliExpress. Эти данные могут быть использованы для отображения информации о продукте, сравнения цен, отслеживания скидок и т.д. в рамках проекта `hypotez`.

## Классы

### `Product`

**Описание**: Класс `Product` представляет собой модель данных для хранения информации о продукте, полученной из API AliExpress.

**Как работает класс**:
Класс `Product` содержит атрибуты, соответствующие полям, возвращаемым API AliExpress. Атрибуты класса определены с указанием типов данных, что помогает обеспечить консистентность данных и облегчает отладку.

**Атрибуты**:
- `app_sale_price` (str): Цена товара в приложении.
- `app_sale_price_currency` (str): Валюта цены товара в приложении.
- `commission_rate` (str): Комиссионные отчисления.
- `discount` (str): Размер скидки на товар.
- `evaluate_rate` (str): Рейтинг товара.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Объем продаж за последнее время.
- `hot_product_commission_rate` (str): Комиссионные отчисления для горячих товаров.
- `original_price` (str): Оригинальная цена товара.
- `original_price_currency` (str): Валюта оригинальной цены товара.
- `product_detail_url` (str): URL страницы с подробным описанием товара.
- `product_id` (int): ID товара.
- `product_main_image_url` (str): URL главного изображения товара.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений товара.
- `product_title` (str): Название товара.
- `product_video_url` (str): URL видео товара.
- `promotion_link` (str): Ссылка на страницу промоакции товара.
- `relevant_market_commission_rate` (str): Комиссионные отчисления для соответствующего рынка.
- `sale_price` (str): Цена товара со скидкой.
- `sale_price_currency` (str): Валюта цены товара со скидкой.
- `second_level_category_id` (int): ID категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): ID магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена товара в приложении.
- `target_app_sale_price_currency` (str): Валюта целевой цены товара в приложении.
- `target_original_price` (str): Целевая оригинальная цена товара.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены товара.
- `target_sale_price` (str): Целевая цена товара со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены товара со скидкой.

**Примеры**:

```python
product = Product()
product.product_id = 123456789
product.product_title = 'Example Product'
product.sale_price = '10.00'
product.sale_price_currency = 'USD'
print(f'Product ID: {product.product_id}, Title: {product.product_title}, Price: {product.sale_price} {product.sale_price_currency}')
```