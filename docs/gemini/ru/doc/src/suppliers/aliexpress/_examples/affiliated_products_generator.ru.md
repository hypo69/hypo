# Модуль `affiliated_products_generator` - Генератор аффилированных ссылок для AliExpress

## Обзор

Этот модуль предоставляет инструменты для генерации аффилированных ссылок для продуктов с AliExpress.  Он содержит класс `AliAffiliatedProducts`, который позволяет обрабатывать данные о продуктах, получать аффилированные ссылки и сохранять связанные медиа-файлы (изображения, видео).

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс `AliAffiliatedProducts` отвечает за обработку данных о продуктах с AliExpress, получение аффилированных ссылок и загрузку изображений/видео.

**Методы**:

- `process_affiliate_products(prod_urls: list[str]) -> list[Product] | None`:
    **Описание**: Метод обрабатывает список URL или ID продуктов, генерирует аффилированные ссылки, скачивает изображения и видео, и возвращает список обработанных объектов `Product`.
    **Параметры**:
    - `prod_urls` (list[str]): Список URL или ID продуктов.
    **Возвращает**:
    - list[Product] | None: Список объектов `Product` с аффилированными ссылками и локальными путями к изображениям/видео. Возвращает `None`, если произошла ошибка.
    **Вызывает исключения**:
    - `APIError`: Возникает при проблемах с API AliExpress.
    - `DownloadError`: Возникает при проблемах с загрузкой изображений/видео.
    - `ValidationError`: Возникает, если данные не соответствуют ожидаемому формату.


## Пример использования

### Пример `example_usage`

**Описание**: Пример использования класса `AliAffiliatedProducts` для обработки списка URL продуктов и получения аффилированных ссылок.

```python
# пример_использования.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts


def main():
    # Задайте параметры рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно задать None, если категория не нужна
    language = "EN"  # Язык для кампании
    currency = "USD"  # Валюта для кампании

    # Создайте экземпляр класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name, campaign_category, language, currency
    )

    # Пример URL продуктов или их ID
    prod_urls = [
        "123",
        "https://www.aliexpress.com/item/123.html",
        "456",
        "https://www.aliexpress.com/item/456.html",
    ]

    # Обработайте продукты и получите список продуктов с аффилированными ссылками
    products = parser.process_affiliate_products(prod_urls)

    # Проверьте результаты
    if products:
        print(f"Получено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"Продукт ID: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Локальный путь к изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Локальный путь к видео: {product.local_saved_video}")
            print()
    else:
        print("Не удалось получить аффилированные продукты.")


if __name__ == "__main__":
    main()
```

**Описание примера:** Пример демонстрирует как использовать `AliAffiliatedProducts` для обработки списка `prod_urls` и вывода результатов.


## Класс `Product`

**Описание**: Класс `Product` используется для хранения информации о продукте, включая его ID, аффилированную ссылку и путь к сохранённому изображению/видео.


**Атрибуты**:

- `product_id`: ID продукта.
- `promotion_link`: Ссылка на аффилированный продукт.
- `local_saved_image`: Локальный путь к сохранённому изображению.
- `local_saved_video`: Локальный путь к сохранённому видео.



**Примечание**:  Предполагается, что модуль `affiliated_products_generator` содержит реализацию методов класса `AliAffiliatedProducts` и класса `Product` с необходимыми обработками и валидацией.