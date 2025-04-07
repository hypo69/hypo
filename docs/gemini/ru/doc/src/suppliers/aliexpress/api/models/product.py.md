# Модуль `product`

## Обзор

Модуль `product` содержит класс `Product`, предназначенный для представления структуры данных товара, получаемого из API AliExpress. Этот класс служит контейнером для хранения информации о продукте, такой как цены, скидки, ссылки и идентификаторы.

## Подробней

Модуль определяет структуру данных для товаров, извлекаемых из API AliExpress. Он используется для организации и хранения информации о продуктах, что облегчает дальнейшую обработку и использование этих данных в других частях проекта `hypotez`. Данные включают в себя информацию о ценах, комиссиях, скидках, URL и другие важные атрибуты продукта.

## Классы

### `Product`

**Описание**: Класс `Product` представляет структуру данных товара, полученного из API AliExpress. Он содержит атрибуты, описывающие различные характеристики продукта, такие как цены, скидки, ссылки и идентификаторы.

**Принцип работы**:
Класс `Product` служит контейнером для хранения данных о товаре. Он не содержит методов для обработки данных, а лишь определяет структуру данных, что делает его удобным для передачи и хранения информации о продукте.

**Атрибуты**:
- `app_sale_price` (str): Цена товара для мобильного приложения.
- `app_sale_price_currency` (str): Валюта цены товара для мобильного приложения.
- `commission_rate` (str): Комиссионные отчисления.
- `discount` (str): Размер скидки на товар.
- `evaluate_rate` (str): Рейтинг товара.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Объем продаж за последнее время.
- `hot_product_commission_rate` (str): Комиссионные отчисления для "горячих" товаров.
- `original_price` (str): Оригинальная цена товара.
- `original_price_currency` (str): Валюта оригинальной цены товара.
- `product_detail_url` (str): URL страницы с детальным описанием товара.
- `product_id` (int): Уникальный идентификатор товара.
- `product_main_image_url` (str): URL основного изображения товара.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений товара.
- `product_title` (str): Название товара.
- `product_video_url` (str): URL видео о товаре.
- `promotion_link` (str): Ссылка на промо-акцию товара.
- `relevant_market_commission_rate` (str): Комиссионные отчисления для соответствующего рынка.
- `sale_price` (str): Цена товара со скидкой.
- `sale_price_currency` (str): Валюта цены товара со скидкой.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена товара для мобильного приложения.
- `target_app_sale_price_currency` (str): Валюта целевой цены товара для мобильного приложения.
- `target_original_price` (str): Целевая оригинальная цена товара.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены товара.
- `target_sale_price` (str): Целевая цена товара со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены товара со скидкой.

**Методы**:
- Класс `Product` не содержит методов.

**Примеры**
```python
from typing import List

# Пример создания экземпляра класса Product
product = Product()
product.app_sale_price = "19.99"
product.app_sale_price_currency = "USD"
product.commission_rate = "0.05"
product.discount = "0.20"
product.evaluate_rate = "4.5"
product.first_level_category_id = 123
product.first_level_category_name = "Electronics"
product.lastest_volume = 1000
product.hot_product_commission_rate = "0.07"
product.original_price = "24.99"
product.original_price_currency = "USD"
product.product_detail_url = "https://example.com/product/123"
product.product_id = 123
product.product_main_image_url = "https://example.com/image/123.jpg"
product.product_small_image_urls = ["https://example.com/image/123_small.jpg"]
product.product_title = "Amazing Gadget"
product.product_video_url = "https://example.com/video/123.mp4"
product.promotion_link = "https://example.com/promotion/123"
product.relevant_market_commission_rate = "0.06"
product.sale_price = "19.99"
product.sale_price_currency = "USD"
product.second_level_category_id = 456
product.second_level_category_name = "Smartphones"
product.shop_id = 789
product.shop_url = "https://example.com/shop/789"
product.target_app_sale_price = "18.99"
product.target_app_sale_price_currency = "USD"
product.target_original_price = "23.99"
product.target_original_price_currency = "USD"
product.target_sale_price = "18.99"
product.target_sale_price_currency = "USD"

# Вывод информации о товаре
print(f"Product Title: {product.product_title}")
print(f"Sale Price: {product.sale_price} {product.sale_price_currency}")