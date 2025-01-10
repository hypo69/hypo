# Модуль `affiliated_products_generator.ru`

## Обзор

Этот модуль предоставляет инструменты для генерации аффилированных ссылок для продуктов с AliExpress. Он включает класс `AliAffiliatedProducts`, который позволяет собирать данные о продуктах и обрабатывать аффилированные ссылки.

## Таблица содержания

* [Модуль `affiliated_products_generator.ru`](#модуль-affiliated-products-generator-ru)
* [Обзор](#обзор)
* [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
    * [`process_affiliate_products`](#process-affiliate-products)
* [Пример использования](#пример-использования)

## Класс `AliAffiliatedProducts`

**Описание**: Класс для работы с аффилированными продуктами с AliExpress. Он позволяет получить аффилированные ссылки, обработать изображения и видео.

### `process_affiliate_products`

**Описание**: Метод для обработки списка продуктов и получения аффилированных ссылок.

**Параметры**:
* `prod_urls` (list): Список URL или ID продуктов.

**Возвращает**:
* `list[Product]`: Список объектов `Product` с аффилированными ссылками, изображениями и видео. Возвращает пустой список, если обработка не удалась или нет продуктов.

**Возможные исключения**:
* `ValueError`: Если входной `prod_urls` не является списком.
* `APIError`: Если произошла ошибка при взаимодействии с API AliExpress.
* `ImageError`: Если возникла проблема при загрузке или обработке изображений.
* `VideoError`: Если возникла проблема при загрузке или обработке видео.


## Пример использования

**Описание**: Пример кода, демонстрирующий использование класса `AliAffiliatedProducts` для получения аффилированных ссылок для продуктов.

```python
# пример_использования.py
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts


def main():
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"
    language = "EN"
    currency = "USD"

    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    products = parser.process_affiliate_products(prod_urls)

    if products:
        print(f"Получено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"Продукт ID: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Локальный путь к изображению: {product.local_image_path}")
            if product.local_video_path:
                print(f"Локальный путь к видео: {product.local_video_path}")
            print()
    else:
        print("Не удалось получить аффилированные продукты.")


if __name__ == "__main__":
    main()
```

**Примечания**:

* В примере предполагается, что класс `Product` содержит атрибуты `product_id`, `promotion_link`, `local_image_path`, и `local_video_path`.
*  Класс `AliAffiliatedProducts` должен быть определён в модуле `affiliated_products_generator.py`.
*  Обратите внимание на обработку исключений (try...except) для надежности в реальной программе.

Этот пример показывает базовый способ использования модуля.  Вы можете настроить его под ваши конкретные нужды.
```