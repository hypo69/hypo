# Модуль `affiliated_products_generator.ru`

## Обзор

Данный модуль предоставляет инструменты для генерации аффилированных ссылок для продуктов с AliExpress.  Он содержит класс `AliAffiliatedProducts`, позволяющий собирать информацию о продуктах и формировать соответствующие ссылки.  Этот документ демонстрирует пример использования класса и его методов.

## Таблица Содержимого

- [Модуль `affiliated_products_generator.ru`](#модуль-affiliated-products-generator-ru)
- [Обзор](#обзор)
- [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
- [Функция `main`](#функция-main)
- [Пример использования `AliAffiliatedProducts`](#пример-использования-aliaffiliatedproducts)
- [Объяснение примера](#объяснение-примера)
- [Полный файл примеров](#полный-файл-примеров)


## Класс `AliAffiliatedProducts`

**Описание**:  Класс `AliAffiliatedProducts` предназначен для обработки данных о продуктах с AliExpress и создания аффилированных ссылок. Он принимает параметры рекламной кампании и список URL или ID продуктов.

**Методы**:

- `process_affiliate_products`: Обрабатывает список продуктов, получает аффилированные ссылки и сохраняет изображения/видео.


## Функция `main`

**Описание**:  Функция `main` демонстрирует пример использования класса `AliAffiliatedProducts`. Она создает экземпляр класса, обрабатывает список продуктов, а затем выводит информацию о полученных аффилированных продуктах.

**Параметры**:
- Нет входных параметров.

**Возвращаемые значения**:
- Нет возвращаемого значения.


## Пример использования `AliAffiliatedProducts`

**Описание**: Приведенный пример демонстрирует, как использовать класс `AliAffiliatedProducts` для получения аффилированных ссылок.  Он задает параметры кампании, предоставляет список продуктов, обрабатывает их, и выводит информацию о полученных результатах.

```python
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Задайте параметры рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно задать None, если категория не нужна
    language = "EN"  # Язык для кампании
    currency = "USD"  # Валюта для кампании

    # Создайте экземпляр класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL продуктов или их ID
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
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


## Объяснение примера

- **Создание экземпляра `AliAffiliatedProducts`**:  Создается объект класса, передавая параметры кампании.
- **Список URL продуктов или их ID**:  Задается список URL или ID продуктов для обработки.
- **Обработка продуктов**: Вызывается метод `process_affiliate_products` для получения аффилированных ссылок и обработки данных.
- **Проверка результатов**: Проверяется, получен ли список продуктов, и информация выводится пользователю.


## Полный файл примеров

(Полный код приведен в исходном запросе.)


**Примечание**:  Документация предполагает, что в файле `affiliated_products_generator.py` есть класс `AliAffiliatedProducts` с соответствующим методом `process_affiliate_products` и что `product` объекты имеют атрибуты `product_id`, `promotion_link`, `local_saved_image` и `local_saved_video`.