# Модуль `affiliated_products_generator.en.md`

## Обзор

Этот модуль предоставляет класс `AliAffiliatedProducts`, предназначенный для получения данных о продуктах и создания аффилированных ссылок для кампаний на AliExpress. Модуль позволяет задавать параметры кампании, такие как имя, категория, язык и валюта, а также список ссылок на продукты.  После обработки, модуль возвращает список продуктов с аффилированными ссылками и сохраненными изображениями (и видео, если таковые имеются).

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для обработки данных о продуктах AliExpress и создания аффилированных ссылок.

**Методы**:

- `process_affiliate_products(prod_urls: list[str | int]) -> list[Product] | None`:
    **Описание**: Обрабатывает список ссылок или идентификаторов продуктов, получая аффилированные ссылки, сохраняя изображения и видео.

    **Параметры**:
    - `prod_urls` (list[str | int]): Список ссылок или идентификаторов продуктов.

    **Возвращает**:
    - list[Product] | None: Список объектов `Product` с аффилированными ссылками и сохранёнными локальными путями к изображениям/видео, или `None`, если обработка не выполнена успешно.

    **Вызывает исключения**:
    - `Exception`: Возможные ошибки при работе с API AliExpress или сохранении данных.


## Пример использования

### Пример `example_usage.py`

```python
# example_usage.py
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts


def main():
    # Настройка параметров кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить None, если категория не нужна
    language = "EN"
    currency = "USD"

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name, campaign_category, language, currency
    )

    # Список ссылок/идентификаторов продуктов
    prod_urls = [
        "123",
        "https://www.aliexpress.com/item/123.html",
        "456",
        "https://www.aliexpress.com/item/456.html",
    ]

    # Обработка продуктов
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Путь к сохранённому изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к сохранённому видео: {product.local_saved_video}")
            print()
    else:
        print("Аффилированных продуктов не найдено.")


if __name__ == "__main__":
    main()
```

**Описание примера**:

Пример демонстрирует использование класса `AliAffiliatedProducts` для получения аффилированных ссылок и сохранения изображений/видео. Он демонстрирует создание экземпляра класса с параметрами кампании и обработку списка ссылок на продукты.  Результаты отображаются на консоли.



**Примечание:**  Для корректной работы необходимо реализовать класс `Product` и соответствующие методы в `affiliated_products_generator.py`.  Также, необходимо установить необходимые библиотеки для работы с API AliExpress.