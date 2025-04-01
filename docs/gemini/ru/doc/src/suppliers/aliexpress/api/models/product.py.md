# Модуль `product`

## Обзор

Модуль `product` содержит класс `Product`, предназначенный для представления информации о продукте с AliExpress. Этот класс содержит атрибуты, описывающие различные характеристики продукта, такие как цена, скидка, рейтинг, изображения, URL-адреса и т.д.

## Подробней

Модуль определяет структуру данных для хранения информации о продукте, полученной через API AliExpress.
Класс `Product` служит для организации и удобного доступа к данным о продукте, таким как цены, изображения, ссылки и категории. Данные могут использоваться для дальнейшей обработки, анализа или отображения информации о продукте.

## Классы

### `Product`

**Описание**: Класс `Product` предназначен для хранения информации о продукте с AliExpress.

**Принцип работы**:
Класс `Product` содержит атрибуты, соответствующие различным полям данных о продукте, таким как цены, скидки, изображения, URL-адреса и прочее. Он служит для представления структуры данных о продукте.

**Атрибуты**:
- `app_sale_price` (str): Цена продукта в приложении во время распродажи.
- `app_sale_price_currency` (str): Валюта цены продукта в приложении во время распродажи.
- `commission_rate` (str): Комиссионный процент.
- `discount` (str): Размер скидки.
- `evaluate_rate` (str): Рейтинг продукта.
- `first_level_category_id` (int): ID категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Комиссионный процент для популярных продуктов.
- `original_price` (str): Оригинальная цена продукта.
- `original_price_currency` (str): Валюта оригинальной цены продукта.
- `product_detail_url` (str): URL страницы с детальным описанием продукта.
- `product_id` (int): ID продукта.
- `product_main_image_url` (str): URL главного изображения продукта.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений продукта.
- `product_title` (str): Название продукта.
- `product_video_url` (str): URL видео продукта.
- `promotion_link` (str): Ссылка на акцию.
- `relevant_market_commission_rate` (str): Комиссионный процент для релевантного рынка.
- `sale_price` (str): Цена продукта во время распродажи.
- `sale_price_currency` (str): Валюта цены продукта во время распродажи.
- `second_level_category_id` (int): ID категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): ID магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена продукта в приложении во время распродажи.
- `target_app_sale_price_currency` (str): Валюта целевой цены продукта в приложении во время распродажи.
- `target_original_price` (str): Целевая оригинальная цена продукта.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены продукта.
- `target_sale_price` (str): Целевая цена продукта во время распродажи.
- `target_sale_price_currency` (str): Валюта целевой цены продукта во время распродажи.

**Методы**:
- Отсутствуют.

**Примеры**
```python
# Пример создания экземпляра класса Product
product = Product()
product.product_title = "Example Product"
product.sale_price = "25.00"
print(product.product_title, product.sale_price)
```
```text
Example Product 25.00
```
```python
from typing import List

class Product:
    app_sale_price: str
    app_sale_price_currency: str
    commission_rate: str
    discount: str
    evaluate_rate: str
    first_level_category_id: int
    first_level_category_name: str
    lastest_volume: int
    hot_product_commission_rate: str
    lastest_volume: int
    original_price: str
    original_price_currency: str
    product_detail_url: str
    product_id: int
    product_main_image_url: str
    product_small_image_urls: List[str]
    product_title: str
    product_video_url: str
    promotion_link: str
    relevant_market_commission_rate: str
    sale_price: str
    sale_price_currency: str
    second_level_category_id: int
    second_level_category_name: str
    shop_id: int
    shop_url: str
    target_app_sale_price: str
    target_app_sale_price_currency: str
    target_original_price: str
    target_original_price_currency: str
    target_sale_price: str
    target_sale_price_currency: str

# Пример создания и инициализации объекта Product
product = Product()
product.app_sale_price = "19.99"
product.app_sale_price_currency = "USD"
product.commission_rate = "0.05"
product.discount = "10%"
product.evaluate_rate = "4.5"
product.first_level_category_id = 123
product.first_level_category_name = "Electronics"
product.lastest_volume = 1000
product.hot_product_commission_rate = "0.08"
product.original_price = "29.99"
product.original_price_currency = "USD"
product.product_detail_url = "http://example.com/product/123"
product.product_id = 456
product.product_main_image_url = "http://example.com/image/456.jpg"
product.product_small_image_urls = ["http://example.com/image/456_1.jpg", "http://example.com/image/456_2.jpg"]
product.product_title = "Wireless Headphones"
product.product_video_url = "http://example.com/video/456.mp4"
product.promotion_link = "http://example.com/promotion/456"
product.relevant_market_commission_rate = "0.07"
product.sale_price = "24.99"
product.sale_price_currency = "USD"
product.second_level_category_id = 456
product.second_level_category_name = "Headphones"
product.shop_id = 789
product.shop_url = "http://example.com/shop/789"
product.target_app_sale_price = "17.99"
product.target_app_sale_price_currency = "USD"
product.target_original_price = "27.99"
product.target_original_price_currency = "USD"
product.target_sale_price = "22.99"
product.target_sale_price_currency = "USD"

# Вывод информации о продукте
print(f"Product Title: {product.product_title}")
print(f"Sale Price: {product.sale_price} {product.sale_price_currency}")
print(f"Original Price: {product.original_price} {product.original_price_currency}")
print(f"Discount: {product.discount}")
print(f"Product Detail URL: {product.product_detail_url}")
```

```text
Product Title: Wireless Headphones
Sale Price: 24.99 USD
Original Price: 29.99 USD
Discount: 10%
Product Detail URL: http://example.com/product/123
```
```python
from typing import List

# Определение класса Product
class Product:
    # Цена продукта в приложении во время распродажи
    app_sale_price: str
    # Валюта цены продукта в приложении во время распродажи
    app_sale_price_currency: str
    # Комиссионный процент
    commission_rate: str
    # Размер скидки
    discount: str
    # Рейтинг продукта
    evaluate_rate: str
    # ID категории первого уровня
    first_level_category_id: int
    # Название категории первого уровня
    first_level_category_name: str
    # Последний объем продаж
    lastest_volume: int
    # Комиссионный процент для популярных продуктов
    hot_product_commission_rate: str
    # Оригинальная цена продукта
    original_price: str
    # Валюта оригинальной цены продукта
    original_price_currency: str
    # URL страницы с детальным описанием продукта
    product_detail_url: str
    # ID продукта
    product_id: int
    # URL главного изображения продукта
    product_main_image_url: str
    # Список URL маленьких изображений продукта
    product_small_image_urls: List[str]
    # Название продукта
    product_title: str
    # URL видео продукта
    product_video_url: str
    # Ссылка на акцию
    promotion_link: str
    # Комиссионный процент для релевантного рынка
    relevant_market_commission_rate: str
    # Цена продукта во время распродажи
    sale_price: str
    # Валюта цены продукта во время распродажи
    sale_price_currency: str
    # ID категории второго уровня
    second_level_category_id: int
    # Название категории второго уровня
    second_level_category_name: str
    # ID магазина
    shop_id: int
    # URL магазина
    shop_url: str
    # Целевая цена продукта в приложении во время распродажи
    target_app_sale_price: str
    # Валюта целевой цены продукта в приложении во время распродажи
    target_app_sale_price_currency: str
    # Целевая оригинальная цена продукта
    target_original_price: str
    # Валюта целевой оригинальной цены продукта
    target_original_price_currency: str
    # Целевая цена продукта во время распродажи
    target_sale_price: str
    # Валюта целевой цены продукта во время распродажи
    target_sale_price_currency: str

# Пример использования класса Product
# Создание экземпляра класса Product
product = Product()

# Заполнение атрибутов объекта product
product.app_sale_price = "29.99"
product.app_sale_price_currency = "USD"
product.commission_rate = "0.05"
product.discount = "20%"
product.evaluate_rate = "4.7"
product.first_level_category_id = 100
product.first_level_category_name = "Electronics"
product.lastest_volume = 500
product.hot_product_commission_rate = "0.08"
product.original_price = "39.99"
product.original_price_currency = "USD"
product.product_detail_url = "https://example.com/product/123"
product.product_id = 12345
product.product_main_image_url = "https://example.com/image/main.jpg"
product.product_small_image_urls = ["https://example.com/image/small1.jpg", "https://example.com/image/small2.jpg"]
product.product_title = "Noise Cancelling Headphones"
product.product_video_url = "https://example.com/video/123"
product.promotion_link = "https://example.com/promotion/456"
product.relevant_market_commission_rate = "0.07"
product.sale_price = "34.99"
product.sale_price_currency = "USD"
product.second_level_category_id = 200
product.second_level_category_name = "Headphones"
product.shop_id = 10
product.shop_url = "https://example.com/shop/10"
product.target_app_sale_price = "27.99"
product.target_app_sale_price_currency = "USD"
product.target_original_price = "37.99"
product.target_original_price_currency = "USD"
product.target_sale_price = "32.99"
product.target_sale_price_currency = "USD"

# Вывод информации о продукте
print(f"Product Title: {product.product_title}")
print(f"Sale Price: {product.sale_price} {product.sale_price_currency}")
print(f"Original Price: {product.original_price} {product.original_price_currency}")
print(f"Discount: {product.discount}")
print(f"Product Detail URL: {product.product_detail_url}")
```

```text
Product Title: Noise Cancelling Headphones
Sale Price: 34.99 USD
Original Price: 39.99 USD
Discount: 20%
Product Detail URL: https://example.com/product/123
```
```python
from typing import List

class Product:
    app_sale_price: str
    app_sale_price_currency: str
    commission_rate: str
    discount: str
    evaluate_rate: str
    first_level_category_id: int
    first_level_category_name: str
    lastest_volume: int
    hot_product_commission_rate: str
    original_price: str
    original_price_currency: str
    product_detail_url: str
    product_id: int
    product_main_image_url: str
    product_small_image_urls: List[str]
    product_title: str
    product_video_url: str
    promotion_link: str
    relevant_market_commission_rate: str
    sale_price: str
    sale_price_currency: str
    second_level_category_id: int
    second_level_category_name: str
    shop_id: int
    shop_url: str
    target_app_sale_price: str
    target_app_sale_price_currency: str
    target_original_price: str
    target_original_price_currency: str
    target_sale_price: str
    target_sale_price_currency: str

# Пример заполнения объекта Product
product = Product()
product.app_sale_price = "15.99"
product.app_sale_price_currency = "USD"
product.commission_rate = "0.04"
product.discount = "5%"
product.evaluate_rate = "4.6"
product.first_level_category_id = 101
product.first_level_category_name = "Home & Garden"
product.lastest_volume = 1200
product.hot_product_commission_rate = "0.06"
product.original_price = "19.99"
product.original_price_currency = "USD"
product.product_detail_url = "https://example.com/product/456"
product.product_id = 54321
product.product_main_image_url = "https://example.com/image/456.jpg"
product.product_small_image_urls = [
    "https://example.com/image/456_small1.jpg",
    "https://example.com/image/456_small2.jpg"
]
product.product_title = "LED String Lights"
product.product_video_url = "https://example.com/video/456.mp4"
product.promotion_link = "https://example.com/promotion/789"
product.relevant_market_commission_rate = "0.05"
product.sale_price = "17.99"
product.sale_price_currency = "USD"
product.second_level_category_id = 202
product.second_level_category_name = "Lighting"
product.shop_id = 11
product.shop_url = "https://example.com/shop/11"
product.target_app_sale_price = "14.99"
product.target_app_sale_price_currency = "USD"
product.target_original_price = "18.99"
product.target_original_price_currency = "USD"
product.target_sale_price = "16.99"
product.target_sale_price_currency = "USD"

print(f"Product Title: {product.product_title}")
print(f"Sale Price: {product.sale_price} {product.sale_price_currency}")
print(f"Product ID: {product.product_id}")
```

```text
Product Title: LED String Lights
Sale Price: 17.99 USD
Product ID: 54321
```