Как использовать модуль affiliated_products_generator
=========================================================================================

Описание
-------------------------
Этот модуль предоставляет класс `AliAffiliatedProducts`, предназначенный для получения данных о продуктах с сайта AliExpress, включая аффилированные ссылки и сохраненные изображения (и видео, если таковые имеются).  Модуль позволяет настроить параметры кампании (название, категория, язык, валюта) и обработать список URL или ID товаров, чтобы получить аффилированные ссылки и локальные пути к сохраненным изображениям/видео.

Шаги выполнения
-------------------------
1. **Импортировать класс `AliAffiliatedProducts`:**
   ```python
   from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
   ```

2. **Настроить параметры кампании:**
   ```python
   campaign_name = "summer_sale_2024"
   campaign_category = "electronics"  # Можно установить в None, если категория не нужна
   language = "EN"
   currency = "USD"
   ```
   Укажите название кампании, категорию, язык и валюту для обработки данных.

3. **Создать экземпляр класса `AliAffiliatedProducts`:**
   ```python
   parser = AliAffiliatedProducts(
       campaign_name,
       campaign_category,
       language,
       currency
   )
   ```
   Создайте объект класса с заданными параметрами.

4. **Подготовить список URL или ID продуктов:**
   ```python
   prod_urls = [
       '123',
       'https://www.aliexpress.com/item/123.html',
       '456',
       'https://www.aliexpress.com/item/456.html',
   ]
   ```
   Создайте список с URL или ID продуктов, которые нужно обработать.

5. **Обработать продукты с помощью метода `process_affiliate_products`:**
   ```python
   products = parser.process_affiliate_products(prod_urls)
   ```
   Этот метод получит данные о продуктах, включая аффилированные ссылки и пути к изображениям/видео.

6. **Проверить полученные результаты:**
   ```python
   if products:
       print(f"Получено {len(products)} аффилированных продуктов.")
       for product in products:
           print(f"ID продукта: {product.product_id}")
           print(f"Аффилированная ссылка: {product.promotion_link}")
           print(f"Локальный путь к изображению: {product.local_saved_image}")
           if product.local_saved_video:
               print(f"Локальный путь к видео: {product.local_saved_video}")
           print()
   else:
       print("Аффилированные продукты не найдены.")
   ```
   Проверьте, есть ли полученные продукты и выведите данные о каждом продукте.

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
        # ... (код проверки результатов, как описано в шагах)

    if __name__ == "__main__":
        main()