# Руководство по использованию модуля `affiliated_products_generator.py`

Этот документ предоставляет руководство по использованию модуля `affiliated_products_generator.py`, предназначенного для сбора данных о продуктах с AliExpress и генерации аффилированных ссылок.

## Описание модуля

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который позволяет обрабатывать данные о продуктах AliExpress, включая получение аффилированных ссылок, загрузку изображений и видео.

## Пример использования

```python
# example_usage.py
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Укажите параметры рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно указать None, если категория не нужна
    language = "EN"
    currency = "USD"

    # Создайте экземпляр класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Список URL продуктов или их ID (могут быть как ID, так и URL)
    prod_urls = [
        "123",
        "https://www.aliexpress.com/item/123.html",
        "456",
        "https://www.aliexpress.com/item/456.html",
    ]

    # Обработайте продукты и получите список с аффилированными ссылками
    products = parser.process_affiliate_products(prod_urls)

    # Обработка результатов
    if products:
        print(f"Найдено {len(products)} аффилированных продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Путь к сохраненному изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к сохраненному видео: {product.local_saved_video}")
            print("-" * 20)  # Разделитель для наглядности
    else:
        print("Не удалось получить аффилированные продукты.")


if __name__ == "__main__":
    main()
```

**Ключевые моменты:**

* **`campaign_name`**, **`campaign_category`**, **`language`**, **`currency`**:  Укажите параметры кампании для контекста и обработки.
* **`prod_urls`**:  Список URL или ID продуктов, которые нужно обработать.  Поддерживаются как ID, так и полные URL.
* **Обработка результатов**: Проверьте наличие результатов и выведите информацию о каждом продукте. Обратите внимание на использование `product.local_saved_image` и `product.local_saved_video`.


## Как использовать

1.  **Установка зависимостей:**  Убедитесь, что необходимые библиотеки установлены (например, для работы с веб-скрейпингом).

2.  **Импорт:** Импортируйте класс `AliAffiliatedProducts` из файла `affiliated_products_generator.py`.

3.  **Настройка параметров:** Задайте значения для `campaign_name`, `campaign_category`, `language` и `currency`.

4.  **Обработка данных:** Создайте экземпляр класса и вызовите `process_affiliate_products(prod_urls)`.

5.  **Обработка результатов:** Проверьте полученный список продуктов `products` и обработайте данные о каждом продукте.


## Возможные проблемы

* **Ошибка подключения:** Проверьте доступ к интернету.
* **Некорректные данные:** Убедитесь, что данные `prod_urls` содержат корректные ID или URL продуктов.
* **Отсутствие необходимых библиотек:** Установите необходимые библиотеки (например, для работы с веб-скрейпингом).

## Дополнительные сведения

*   Посмотрите документацию класса `AliAffiliatedProducts` для получения подробной информации о доступных методах и параметрах.
*   Подготовьте методы обработки ошибок для устойчивого поведения программы.


Этот документ предоставляет основу для работы с модулем. Обратите внимание на подробные комментарии в исходном коде модуля `affiliated_products_generator.py` для получения дополнительных деталей.