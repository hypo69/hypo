Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код предоставляет пример использования класса `AliAffiliatedProducts` для генерации аффилированных ссылок на продукты с AliExpress. Код задаёт параметры рекламной кампании, определяет список URL-адресов продуктов или их ID, обрабатывает эти продукты и выводит информацию об аффилированных ссылках и сохранённых изображениях/видео.  Код проверяет, успешно ли получены данные, и выводит соответствующее сообщение.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Код импортирует класс `AliAffiliatedProducts` из модуля `src.suppliers.aliexpress.affiliated_products_generator`.
2. **Запись параметров кампании**: Определяются переменные для имени кампании (`campaign_name`), категории (`campaign_category`), языка (`language`) и валюты (`currency`).  Можно задать категорию `None`, если она не нужна.
3. **Создание экземпляра класса**: Создаётся экземпляр класса `AliAffiliatedProducts` с указанными параметрами кампании.
4. **Определение списка URL продуктов**: Создаётся список (`prod_urls`) с URL-адресами или ID продуктов с AliExpress.
5. **Обработка продуктов**: Метод `process_affiliate_products` обрабатывает список продуктов, генерирует аффилированные ссылки и сохраняет изображения/видео (если они есть).
6. **Получение и вывод результатов**: Проверяется, получен ли список продуктов (`products`). Если да, выводятся информация о каждом продукте (ID, аффилированная ссылка, локальный путь к изображению, локальный путь к видео), иначе выводится сообщение об ошибке.


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