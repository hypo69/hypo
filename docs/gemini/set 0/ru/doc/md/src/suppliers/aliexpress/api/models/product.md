# Модуль `hypotez/src/suppliers/aliexpress/api/models/product.py`

## Обзор

Данный модуль содержит определение класса `Product`, представляющего собой модель продукта с АлиЭкспресс.  Класс содержит атрибуты, описывающие различные характеристики продукта, такие как цена, категория, ссылки на изображения и видео.

## Классы

### `Product`

**Описание**: Класс `Product` описывает продукт на платформе АлиЭкспресс. Он хранит информацию о цене, валюте, комиссии, скидке, рейтинге, категориях, объеме продаж, ссылках и других важных данных.

**Атрибуты**:

- `app_sale_price`: Цена приложения. Тип: `str`.
- `app_sale_price_currency`: Валюта цены приложения. Тип: `str`.
- `commission_rate`: Ставка комиссии. Тип: `str`.
- `discount`: Скидка. Тип: `str`.
- `evaluate_rate`: Рейтинг. Тип: `str`.
- `first_level_category_id`: Идентификатор категории первого уровня. Тип: `int`.
- `first_level_category_name`: Название категории первого уровня. Тип: `str`.
- `lastest_volume`: Последний объем продаж. Тип: `int`.
- `hot_product_commission_rate`: Ставка комиссии на горячие товары. Тип: `str`.
- `lastest_volume`: Последний объем продаж. Тип: `int`. (Дублирование, возможно ошибка в исходном коде)
- `original_price`: Исходная цена. Тип: `str`.
- `original_price_currency`: Валюта исходной цены. Тип: `str`.
- `product_detail_url`: Ссылка на подробную информацию о товаре. Тип: `str`.
- `product_id`: Идентификатор товара. Тип: `int`.
- `product_main_image_url`: Ссылка на основное изображение товара. Тип: `str`.
- `product_small_image_urls`: Список ссылок на дополнительные изображения товара. Тип: `List[str]`.
- `product_title`: Название товара. Тип: `str`.
- `product_video_url`: Ссылка на видео товара. Тип: `str`.
- `promotion_link`: Ссылка на промоакцию. Тип: `str`.
- `relevant_market_commission_rate`: Ставка комиссии на соответствующий рынок. Тип: `str`.
- `sale_price`: Цена продажи. Тип: `str`.
- `sale_price_currency`: Валюта цены продажи. Тип: `str`.
- `second_level_category_id`: Идентификатор категории второго уровня. Тип: `int`.
- `second_level_category_name`: Название категории второго уровня. Тип: `str`.
- `shop_id`: Идентификатор магазина. Тип: `int`.
- `shop_url`: Ссылка на магазин. Тип: `str`.
- `target_app_sale_price`: Целевая цена приложения. Тип: `str`.
- `target_app_sale_price_currency`: Валюта целевой цены приложения. Тип: `str`.
- `target_original_price`: Целевая исходная цена. Тип: `str`.
- `target_original_price_currency`: Валюта целевой исходной цены. Тип: `str`.
- `target_sale_price`: Целевая цена продажи. Тип: `str`.
- `target_sale_price_currency`: Валюта целевой цены продажи. Тип: `str`.


## Функции

(Нет функций в этом модуле)


**Примечание**:  Поле `lastest_volume`  дублируется в коде.  Это, вероятно, ошибка, и необходимо исправить дублирование.