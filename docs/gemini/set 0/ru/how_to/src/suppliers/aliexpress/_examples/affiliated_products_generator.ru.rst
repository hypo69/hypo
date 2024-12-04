Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код демонстрирует использование класса `AliAffiliatedProducts` для получения аффилированных ссылок на продукты с AliExpress. Он принимает список URL или ID продуктов, обрабатывает их, собирает аффилированные ссылки и сохраняет локальные пути к изображениям и видео, если таковые имеются.

Шаги выполнения
-------------------------
1. **Импортирование класса:** Импортируется класс `AliAffiliatedProducts` из модуля `affiliated_products_generator`.
2. **Установка параметров кампании:** Задаются параметры рекламной кампании: имя кампании (`campaign_name`), категория (`campaign_category`), язык (`language`) и валюта (`currency`).  Эти параметры используются для настройки процесса получения аффилированных ссылок.
3. **Создание экземпляра класса:** Создается экземпляр класса `AliAffiliatedProducts` с указанными параметрами кампании.
4. **Формирование списка продуктов:** Создается список `prod_urls` с URL или ID продуктов, для которых необходимо получить аффилированные ссылки.  Можно использовать как ссылки, так и ID продуктов.
5. **Обработка продуктов:** Вызывается метод `process_affiliate_products` экземпляра класса, передавая список `prod_urls`. Этот метод выполняет поиск аффилированных ссылок, скачивает изображения и видео (если они есть), и сохраняет локальные пути к ним. Результат – список объектов, содержащих информацию о каждом продукте.
6. **Обработка результатов:** Проверяется, получен ли список продуктов. Если да, то выводится информация о каждом продукте, включая ID, аффилированную ссылку и пути к локально сохранённым изображению и видео. В противном случае выводится сообщение об ошибке.

Пример использования
-------------------------
.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        campaign_name = "summer_sale_2024"
        campaign_category = "electronics"
        language = "EN"
        currency = "USD"

        parser = AliAffiliatedProducts(
            campaign_name,
            campaign_category,
            language,
            currency
        )

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