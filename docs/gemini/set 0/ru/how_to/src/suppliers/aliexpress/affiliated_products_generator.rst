Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код из файла `hypotez/src/suppliers/aliexpress/affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который генерирует и сохраняет информацию о продуктах с аффилированными ссылками для рекламных кампаний на AliExpress.  Он получает данные о продуктах по списку ID или URL, извлекает аффилированные ссылки, загружает изображения и видео продуктов, сохраняет их локально, и формирует JSON файлы с данными.  Класс наследуется от `AliApi`, используя его методы для извлечения аффилированных ссылок и данных продуктов.

Шаги выполнения
-------------------------
1. **Инициализация класса `AliAffiliatedProducts`:**
   - Создается экземпляр класса `AliAffiliatedProducts` с указанием языка и валюты.  Необходимы `language` и `currency` для корректной работы. Если они не предоставлены, функция завершается с критическим сообщением.
   - Вызывается конструктор родительского класса `AliApi` с переданными параметрами языка и валюты.

2. **Обработка списка product_ids:**
   - Метод `process_affiliate_products` принимает список `prod_ids` (списки ID или URL продуктов) и путь `category_root` к директории для сохранения данных.
   -  Происходит нормализация URL, переводя их к виду `https://aliexpress.com/item/<product_id>.html` (функция `ensure_https`).
   - Для каждого `prod_url` из списка:
     - Извлекаются аффилированные ссылки с помощью метода `get_affiliate_links` родительского класса `AliApi`.
     - Если аффилированная ссылка найдена, добавляется в `_promotion_links` и `_prod_urls`.  Также выводится сообщение об успехе в лог.
     - Если аффилированная ссылка не найдена, пропускается текущий продукт.

3. **Проверка на отсутствие аффилированных ссылок:**
   - Если ни одной аффилированной ссылки не найдено, выводится предупреждение в лог и функция возвращает пустой список.

4. **Извлечение подробностей о продуктах:**
   - Метод `retrieve_product_details` получает подробную информацию о продуктах по URL из `_prod_urls`.  Результат сохраняется в `_affiliated_products`.
   - Если `_affiliated_products` пуст, функция возвращает пустой список.


5. **Обработка и сохранение данных о продуктах:**
   - Цикл `for` обрабатывает каждый `product` и соответствующую ему `promotion_link`:
     - Устанавливаются значения `language` и `promotion_link` для объекта `product`.
     - Загружается изображение продукта с помощью `save_png_from_url` и сохраняется в папку `images`. Путь к изображению сохраняется в `product.local_saved_image`.
     - Если у продукта есть видео (`product.product_video_url`), оно загружается и сохраняется в папку `videos` с помощью `save_video_from_url`, а путь к нему сохраняется в `product.local_saved_video`.
     - Сохраняется JSON с данными продукта в файл в указанной директории.
     - Добавляется обработанный продукт в `affiliated_products_list`.

6. **Сохранение списка названий продуктов:**
   - Сохраняет список названий продуктов `product_titles` в текстовый файл `product_titles.txt`.

7. **Возврат списка продуктов:**
   - Возвращает список обработанных продуктов `affiliated_products_list`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    from types import SimpleNamespace

    async def main():
        prod_ids = ["http://example.com/product1", "http://example.com/product2"]
        category_root = Path("./campaign_data")
        ali_affiliated_products = AliAffiliatedProducts(language="EN", currency="USD")
        products = await ali_affiliated_products.process_affiliate_products(prod_ids, category_root)
        for product in products:
            print(product.product_title)
            print(product.local_saved_image)

    asyncio.run(main())