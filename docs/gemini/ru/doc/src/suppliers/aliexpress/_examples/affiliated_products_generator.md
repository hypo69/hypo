# Модуль `hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.py`

## Обзор

Этот модуль предоставляет примеры использования класса `AliAffiliatedProducts` для генерации аффилированных ссылок на продукты с AliExpress.  Модуль демонстрирует создание экземпляра класса с заданными параметрами рекламной кампании и обработку списка URL-адресов продуктов для получения аффилированных ссылок.

## Оглавление

* [Обзор](#обзор)
* [Функции](#функции)
    * [`main`](#main)


## Функции

### `main`

**Описание**:  Функция `main` демонстрирует использование класса `AliAffiliatedProducts` для получения аффилированных ссылок на продукты с AliExpress. Она задает параметры рекламной кампании, создает экземпляр класса, обрабатывает список URL-адресов продуктов и выводит полученные результаты.

**Параметры**:

- Нет явных параметров.

**Возвращает**:

- Нет возвращаемого значения.

**Вызывает исключения**:

- Возможные исключения, генерируемые внутри `AliAffiliatedProducts.process_affiliate_products`, должны быть обработаны в `main`.


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

**Примечание:**  Этот пример требует наличия класса `AliAffiliatedProducts` в модуле `src.suppliers.aliexpress.affiliated_products_generator`.  Документация для этого класса должна быть предоставлена отдельно, чтобы этот пример был полным.  Обработка потенциальных исключений не показана в примере, но необходима для надежного использования в реальных сценариях.