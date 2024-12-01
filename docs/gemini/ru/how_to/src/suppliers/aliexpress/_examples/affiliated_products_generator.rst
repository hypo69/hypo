Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет пример использования класса `AliAffiliatedProducts` для генерации аффилированных ссылок на продукты с AliExpress. Код задаёт параметры кампании, список URL-адресов или ID продуктов, обрабатывает их и выводит информацию о полученных аффилированных ссылках.

Шаги выполнения
-------------------------
1. **Импортирует необходимый класс:** Импортирует класс `AliAffiliatedProducts` из модуля `affiliated_products_generator`.

2. **Определяет параметры кампании:** Устанавливает название кампании (`campaign_name`), категорию (`campaign_category`), язык (`language`) и валюту (`currency`).

3. **Создаёт экземпляр класса `AliAffiliatedProducts`:** Создаёт объект класса `AliAffiliatedProducts`, передавая в конструктор заданные параметры кампании.

4. **Задаёт список продуктов:** Определяет список URL-адресов или ID продуктов (`prod_urls`), которые необходимо обработать.

5. **Обрабатывает продукты:** Вызывает метод `process_affiliate_products` у экземпляра класса `AliAffiliatedProducts`, передавая список `prod_urls`. Этот метод генерирует аффилированные ссылки для каждого продукта.

6. **Проверяет результат и выводит информацию:** Проверяет, пуст ли полученный список продуктов (`products`). Если список не пуст, выводит количество полученных продуктов и подробную информацию о каждом из них, включая ID продукта, аффилированную ссылку и локальные пути к сохранённым изображениям/видео, если они есть. В случае, если список пуст, выводит сообщение об ошибке.

Пример использования
-------------------------
.. code-block:: python

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