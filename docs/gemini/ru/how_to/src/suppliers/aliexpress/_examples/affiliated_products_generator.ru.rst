Как использовать модуль affiliated_products_generator
========================================================================================

Описание
-------------------------
Данный модуль предоставляет класс `AliAffiliatedProducts` для сбора данных о продуктах AliExpress и создания аффилированных ссылок.  Он позволяет указать параметры рекламной кампании, список URL или ID продуктов и получить список продуктов с созданными аффилированными ссылками, локальными путями к сохранённым изображениям и видео.

Шаги выполнения
-------------------------
1. **Импортирование класса:** Импортируйте класс `AliAffiliatedProducts` из модуля `affiliated_products_generator`:

   .. code-block:: python
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

2. **Установка параметров кампании:**  Создайте экземпляр класса `AliAffiliatedProducts`, передавая следующие параметры:
    - `campaign_name`: Название рекламной кампании (строка).
    - `campaign_category`: Категория рекламной кампании (строка, или `None`, если не нужна).
    - `language`: Язык для кампании (строка).
    - `currency`: Валюта для кампании (строка).


   .. code-block:: python
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"
    language = "EN"
    currency = "USD"
    parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)

3. **Подготовьте список URL продуктов или их ID:**
   Создайте список `prod_urls` с URL или ID продуктов AliExpress.

   .. code-block:: python
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

4. **Обработайте продукты:**
   Вызовите метод `process_affiliate_products` класса `AliAffiliatedProducts`, передавая список `prod_urls`.  Метод вернёт список объектов, содержащих информацию о продуктах с аффилированными ссылками.

   .. code-block:: python
    products = parser.process_affiliate_products(prod_urls)


5. **Обработайте результаты:**
   Проверьте, не пуст ли список `products`. Если он не пуст, выведите информацию о каждом продукте, включая ID продукта, аффилированную ссылку, локальный путь к изображению и локальный путь к видео (если оно есть).

   .. code-block:: python
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


Пример использования
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        campaign_name = "summer_sale_2024"
        campaign_category = None  # Можно задать None, если категория не нужна
        language = "EN"
        currency = "USD"

        parser = AliAffiliatedProducts(campaign_name, campaign_category, language, currency)

        prod_urls = [
            '123',
            'https://www.aliexpress.com/item/123.html',
            '456',
            'https://www.aliexpress.com/item/456.html',
        ]

        products = parser.process_affiliate_products(prod_urls)

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