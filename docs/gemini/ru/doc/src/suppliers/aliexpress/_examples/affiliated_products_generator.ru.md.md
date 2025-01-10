# Примеры использования модуля `affiliated_products_generator.py`

## Обзор

Этот файл содержит примеры использования класса `AliAffiliatedProducts` для сбора данных о продуктах и обработки аффилированных ссылок. Примеры демонстрируют, как инициализировать класс, обрабатывать список URL продуктов или их ID, и получать информацию о продуктах, включая аффилированные ссылки и локальные пути к изображениям и видео.

## Содержание

- [Примеры использования модуля `affiliated_products_generator.py`](#примеры-использования-модуля-affiliated_products_generatorpy)
  - [Обзор](#обзор)
  - [Содержание](#содержание)
  - [Пример использования `AliAffiliatedProducts`](#пример-использования-aliaffiliatedproducts)
    - [Объяснение примера](#объяснение-примера)
      - [Создание экземпляра `AliAffiliatedProducts`](#создание-экземпляра-aliaffiliatedproducts)
      - [Список URL продуктов или их ID](#список-url-продуктов-или-их-id)
      - [Обработка продуктов](#обработка-продуктов)
      - [Проверка результатов](#проверка-результатов)
    - [Полный файл примеров](#полный-файл-примеров)

## Пример использования `AliAffiliatedProducts`

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
            print(f"Локальный путь к изображению: {product.local_image_path}")
            if product.local_video_path:
                print(f"Локальный путь к видео: {product.local_video_path}")
            print()
    else:
        print("Не удалось получить аффилированные продукты.")

if __name__ == "__main__":
    main()
```

### Объяснение примера

#### Создание экземпляра `AliAffiliatedProducts`

```python
parser = AliAffiliatedProducts(
    campaign_name,
    campaign_category,
    language,
    currency
)
```

Здесь создается объект класса `AliAffiliatedProducts`, передавая параметры рекламной кампании: название кампании, категорию, язык и валюту.

#### Список URL продуктов или их ID

```python
prod_urls = [
    '123',
    'https://www.aliexpress.com/item/123.html',
    '456',
    'https://www.aliexpress.com/item/456.html',
]
```

Пример списка продуктов. Можно указывать как просто ID, так и полные URL.

#### Обработка продуктов

```python
products = parser.process_affiliate_products(prod_urls)
```

Вызывается метод `process_affiliate_products`, который обрабатывает продукты, получает аффилированные ссылки, и сохраняет изображения и видео.

#### Проверка результатов

```python
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
```

Проверяется, есть ли обработанные продукты, и выводится информация о каждом продукте, включая ID продукта, аффилированную ссылку, локальный путь к изображению и, если есть, локальный путь к видео.

### Полный файл примеров

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
            print(f"Локальный путь к изображению: {product.local_image_path}")
            if product.local_video_path:
                print(f"Локальный путь к видео: {product.local_video_path}")
            print()
    else:
        print("Не удалось получить аффилированные продукты.")

if __name__ == "__main__":
    main()
```

Этот файл можно использовать как шаблон для тестирования работы класса и методов модуля `affiliated_products_generator.py`.