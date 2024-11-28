# Модуль `affiliated_products_generator.en.md`

## Обзор

Этот модуль предоставляет класс `AliAffiliatedProducts` для получения данных о продуктах с AliExpress и создания аффилированных ссылок. Он позволяет задавать параметры рекламной кампании (название, категория, язык, валюта), обрабатывать списки URL или ID продуктов и сохранять полученные аффилированные ссылки и изображения.

## Оглавление

* [Обзор](#обзор)
* [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
    * [Метод `process_affiliate_products`](#метод-process_affiliate_products)

## Класс `AliAffiliatedProducts`

**Описание**:  Класс `AliAffiliatedProducts` обрабатывает запросы к API AliExpress для получения информации о продуктах, создания аффилированных ссылок и сохранения изображений.

**Методы**:

### `process_affiliate_products`

**Описание**: Обрабатывает список URL или ID продуктов, возвращая список объектов `Product` с аффилированными ссылками и сохранёнными изображениями.

**Параметры**:

* `prod_urls` (list): Список URL или ID продуктов.


**Возвращает**:

* `list[Product]`: Список объектов `Product` с аффилированными ссылками и сохранёнными изображениями. Возвращает пустой список, если продукты не найдены или произошла ошибка.

**Возможные исключения**:

* `APIError`: Ошибка при запросе к API AliExpress.
* `ProductNotFoundError`: Продукт не найден.
* `InvalidInputError`: Некорректные входные данные.
* `ImageDownloadError`: Ошибка при загрузке изображения.
* `OtherError`: Другие ошибки, возникающие во время выполнения.


## Пример использования

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Установка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить None, если категория не нужна
    language = "EN"  # Язык кампании
    currency = "USD"  # Валюта кампании

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример списков URL или ID продуктов
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с аффилированными ссылками и сохранёнными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Ссылка: {product.promotion_link}")
            print(f"Путь к изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к видео: {product.local_saved_video}")
            print()
    else:
        print("Аффилированных продуктов не найдено.")

if __name__ == "__main__":
    main()
```

**Важно**:  Этот пример демонстрирует общий шаблон использования. Необходимо добавить обработку ошибок и детализацию обработки в зависимости от конкретных требований проекта.  Этот пример предполагает, что `Product` - это класс, определяемый в том же модуле или в другом, и содержит необходимые атрибуты (product_id, promotion_link, local_saved_image, local_saved_video).