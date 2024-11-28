# Пример использования модуля `affiliated_products_generator.py` для AliExpress

Этот документ описывает пример использования модуля `affiliated_products_generator.py` для сбора данных о продуктах AliExpress и генерации аффилированных ссылок.

### Файл примера (`пример_использования.py`)

Файл `пример_использования.py` демонстрирует, как использовать класс `AliAffiliatedProducts` для получения аффилированных ссылок для нескольких продуктов.

```python
# пример_использования.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Задайте параметры рекламной кампании.
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно задать None, если категория не нужна
    language = "EN"  # Язык для кампании
    currency = "USD"  # Валюта для кампании

    # Создайте экземпляр класса AliAffiliatedProducts.
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL продуктов или их ID.
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработайте продукты и получите список продуктов с аффилированными ссылками.
    products = parser.process_affiliate_products(prod_urls)

    # Проверьте результаты.
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

### Объяснение кода:

* **`AliAffiliatedProducts(campaign_name, campaign_category, language, currency)`:**  Создает экземпляр класса для обработки аффилированных продуктов.  Необходимо указать название кампании, категорию, язык и валюту.
* **`prod_urls`:** Список URL или ID продуктов AliExpress.  Можно использовать как ID продукта, так и полные URL.
* **`parser.process_affiliate_products(prod_urls)`:** Этот метод обрабатывает предоставленные URL/ID, получает аффилированные ссылки, скачивает изображения и видео, и сохраняет их локально (если это возможно). Результат — список объектов `Product`.
* **Обработка результатов:** Программа проверяет, был ли успешно получен список продуктов, и выводит информацию об каждом продукте, включая его ID, аффилированную ссылку и пути к сохранённым изображениям и видео.

###  Важные моменты:

* **Обработка ошибок:**  В реальном коде необходимо добавить обработку ошибок (например, исключения, если сайт не отвечает или продукт не найден), чтобы предотвратить неожиданное завершение программы.
* **Сохранение изображений и видео:**  Локальное сохранение изображений и видео предполагает наличие соответствующей логики и параметров сохранения в классе `AliAffiliatedProducts`.
* **`Product` объект:**  В примере предполагается, что класс `AliAffiliatedProducts` возвращает список объектов `Product`, у которых есть атрибуты `product_id`, `promotion_link`, `local_saved_image` и `local_saved_video`.


Этот пример демонстрирует базовые принципы использования модуля.  Для более сложных сценариев необходимо адаптировать код и добавить дополнительные проверки.