# Модуль `affiliated_products_generator.en`

## Обзор

Этот модуль предоставляет класс `AliAffiliatedProducts` для сбора данных о продуктах и генерации аффилированных ссылок для товаров с AliExpress. Он обрабатывает предоставленные ссылки на продукты, получает аффилированные ссылки и сохраняет изображения и видео.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс `AliAffiliatedProducts` используется для обработки данных о продуктах с AliExpress. Он принимает параметры рекламной кампании и список ссылок на продукты, чтобы получить аффилированные ссылки и сохраненные изображения.

**Методы**:

- `process_affiliate_products`:
    **Описание**: Обрабатывает список ссылок на продукты, возвращает список объектов `Product` с аффилированными ссылками и сохраненными изображениями/видео.

    **Параметры**:
    - `prod_urls` ([str]): Список ссылок на продукты или ID продуктов.


    **Возвращает**:
    - `list[Product]`: Список объектов `Product` с аффилированными ссылками и сохраненными изображениями/видео. Возвращает пустой список, если нет обработанных продуктов.

    **Возможные исключения**:
    - `Exception`: Общее исключение, если что-то пошло не так при обработке.


## Пример использования

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Настройка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить в None, если категория не нужна
    language = "EN"  # Язык кампании
    currency = "USD"  # Валюта кампании

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример списков ссылок на продукты или ID
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с аффилированными ссылками и сохраненными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Путь к сохраненному изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к сохраненному видео: {product.local_saved_video}")
            print()
    else:
        print("Аффилированных продуктов не найдено.")

if __name__ == "__main__":
    main()
```

**Примечание**: Для корректной работы этого кода необходимо определить класс `Product` и соответствующие атрибуты (`product_id`, `promotion_link`, `local_saved_image`, `local_saved_video`).  Этот пример демонстрирует базовый принцип использования модуля и требует имплементации `AliAffiliatedProducts` и `Product` классов.
```