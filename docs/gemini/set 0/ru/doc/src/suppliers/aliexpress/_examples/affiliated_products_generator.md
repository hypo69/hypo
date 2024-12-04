# Модуль `hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.py`

## Обзор

Этот модуль содержит пример использования класса `AliAffiliatedProducts` для получения аффилированных ссылок на продукты с AliExpress.  В нем демонстрируется как создавать экземпляры класса и обрабатывать список URL-адресов или ID продуктов, получая информацию о продуктах с аффилированными ссылками.

## Оглавление

* [Функции](#функции)


## Функции

### `main`

**Описание**: Функция `main` демонстрирует пример использования класса `AliAffiliatedProducts`. Она создает экземпляр класса, передавая параметры рекламной кампании, обрабатывает список URL-адресов продуктов и выводит информацию об аффилированных продуктах, включая ID продукта, аффилированную ссылку и пути к сохранённым изображениям и видео.

**Параметры**:
- Нет явных параметров.

**Возвращает**:
- Нет значения возврата.

**Вызывает исключения**:
- Любые исключения, которые могут быть вызваны методами внутри класса `AliAffiliatedProducts`.


```python
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
```


**Примечание**: Этот пример предполагает, что класс `AliAffiliatedProducts` определен в файле `src/suppliers/aliexpress/affiliated_products_generator.py` и содержит метод `process_affiliate_products`, который возвращает список объектов, содержащих информацию о продуктах.  Для полноценной работы необходимо определить этот класс и методы `product_id`, `promotion_link`, `local_saved_image` и `local_saved_video` внутри него.
```