Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код из файла `hypotez/src/suppliers/aliexpress/affiliated_products_generator.py` предоставляет класс `AliAffiliatedProducts`, который собирает данные о продуктах с AliExpress, включая аффилированные ссылки и сохраненные изображения/видео. Он обрабатывает список идентификаторов продуктов (URL или ID), извлекает аффилированные ссылки, загружает изображения и видео, сохраняет данные в файлы JSON и возвращает список обработанных продуктов в формате `SimpleNamespace`.

Шаги выполнения
-------------------------
1. **Инициализация класса `AliAffiliatedProducts`:**
   - Создается экземпляр класса `AliAffiliatedProducts`, передавая язык и валюту для кампании.
   - Если язык или валюта не указаны, генерируется критическое сообщение и выполнение прерывается.
   - Вызывается метод `super().__init__(language, currency)` родительского класса `AliApi` для дальнейшей инициализации.

2. **Обработка списка идентификаторов продуктов (`process_affiliate_products`):**
   - В качестве входных данных принимается список идентификаторов продуктов (`prod_ids`) и путь к корневой директории категории (`category_root`).
   - Используется функция `ensure_https` для приведения URL продуктов к виду `https://...`.
   - Для каждого URL продукта из списка:
     - Вызывается метод `get_affiliate_links` для получения аффилированной ссылки.
     - Если аффилированная ссылка найдена:
       - Сохраняется ссылка в список `_promotion_links`.
       - Сохраняется URL продукта в список `_prod_urls`.
       - Записывается сообщение об успехе в лог.
     - Если аффилированная ссылка не найдена, переходит к следующему продукту.

3. **Проверка наличия аффилированных ссылок:**
   - Если список `_promotion_links` пустой, генерируется предупреждение в лог и функция возвращает пустой список.

4. **Получение данных о продуктах:**
   - Вызывается метод `retrieve_product_details` для извлечения подробных данных о продуктах, используя список `_prod_urls`.
   - Если данные не получены, функция возвращает пустой список.

5. **Обработка и сохранение данных о продуктах:**
   - Для каждого продукта и аффилированной ссылки:
     - Записывается заголовок продукта в список `product_titles`.
     - Устанавливаются `language` и `promotion_link` для каждого продукта.
     - Сохраняется изображение продукта в формате PNG по пути `category_root/images/<product_id>.png`.
     - Сохраняется видео продукта (если есть), если URL не пустой.
     - Сохраняется информация о продукте в файл JSON по пути `category_root/<language>_<currency>/<product_id>.json`.
     - Добавляется обработанный продукт в список `affiliated_products_list`.

6. **Сохранение заголовков продуктов:**
   - Сохраняются заголовки продуктов в текстовый файл `category_root/<language>_<currency>/product_titles.txt`.

7. **Возврат обработанного списка продуктов:**
   - Возвращается список `affiliated_products_list` с обработанными данными продуктов.


Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from pathlib import Path
    from types import SimpleNamespace
    from hypotez.src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    async def main():
        prod_ids = ["http://example.com/product1", "http://example.com/product2"]
        category_root = Path("./campaign_data")
        generator = AliAffiliatedProducts(language="EN", currency="USD")
        products = await generator.process_affiliate_products(prod_ids, category_root)
        for product in products:
            print(f"Product Title: {product.product_title}, Affiliate Link: {product.promotion_link}")

    asyncio.run(main())