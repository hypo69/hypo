# Модуль `src.suppliers.aliexpress.api.models.product`

## Обзор

Модуль `src.suppliers.aliexpress.api.models.product` определяет структуру данных `Product`, используемую для представления информации о товаре, полученной от AliExpress API. Этот модуль включает поля, такие как цена, валюта, скидки, рейтинг, категории, объемы продаж, изображения, URL-адреса и идентификаторы, необходимые для отображения и анализа данных о товарах.

## Подробней

Этот код предоставляет модель данных `Product`, которая содержит информацию о продукте с AliExpress. Эта модель используется для структурированного хранения и передачи данных между различными компонентами приложения, такими как API-клиенты и пользовательский интерфейс. Модель включает в себя поля для хранения цен, валют, скидок, оценок, категорий, объемов продаж, изображений, URL-адресов и идентификаторов.

## Классы

### `Product`

**Описание**:
Класс `Product` представляет собой модель данных для хранения информации о товаре с AliExpress.

**Методы**:
- Нет явно определенных методов в предоставленном коде.

**Параметры**:
- `app_sale_price` (str): Цена товара в приложении со скидкой.
- `app_sale_price_currency` (str): Валюта цены товара в приложении со скидкой.
- `commission_rate` (str): Комиссионный тариф.
- `discount` (str): Размер скидки на товар.
- `evaluate_rate` (str): Рейтинг товара.
- `first_level_category_id` (int): Идентификатор категории первого уровня.
- `first_level_category_name` (str): Название категории первого уровня.
- `lastest_volume` (int): Последний объем продаж.
- `hot_product_commission_rate` (str): Комиссионный тариф для популярных товаров.
- `original_price` (str): Оригинальная цена товара.
- `original_price_currency` (str): Валюта оригинальной цены товара.
- `product_detail_url` (str): URL страницы с подробной информацией о товаре.
- `product_id` (int): Идентификатор товара.
- `product_main_image_url` (str): URL главного изображения товара.
- `product_small_image_urls` (List[str]): Список URL маленьких изображений товара.
- `product_title` (str): Название товара.
- `product_video_url` (str): URL видео товара.
- `promotion_link` (str): Ссылка на промо-акцию товара.
- `relevant_market_commission_rate` (str): Комиссионный тариф для соответствующего рынка.
- `sale_price` (str): Цена товара со скидкой.
- `sale_price_currency` (str): Валюта цены товара со скидкой.
- `second_level_category_id` (int): Идентификатор категории второго уровня.
- `second_level_category_name` (str): Название категории второго уровня.
- `shop_id` (int): Идентификатор магазина.
- `shop_url` (str): URL магазина.
- `target_app_sale_price` (str): Целевая цена товара в приложении со скидкой.
- `target_app_sale_price_currency` (str): Валюта целевой цены товара в приложении со скидкой.
- `target_original_price` (str): Целевая оригинальная цена товара.
- `target_original_price_currency` (str): Валюта целевой оригинальной цены товара.
- `target_sale_price` (str): Целевая цена товара со скидкой.
- `target_sale_price_currency` (str): Валюта целевой цены товара со скидкой.

**Примеры**:

```python
from src.suppliers.aliexpress.api.models import Product

# Пример создания экземпляра класса Product
product = Product()
product.product_title = 'Example Product'
product.sale_price = '25.00'
product.sale_price_currency = 'USD'
print(f'Product title: {product.product_title}, price: {product.sale_price} {product.sale_price_currency}')
```

## Функции

В данном модуле функции отсутствуют.