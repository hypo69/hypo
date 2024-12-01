Как использовать модуль affiliated_products_generator
==========================================================================================

Описание
-------------------------
Данный модуль предоставляет класс `AliAffiliatedProducts`, который позволяет собирать данные о товарах с AliExpress, генерировать аффилированные ссылки и сохранять изображения (и видео, если они присутствуют). Модуль позволяет указать параметры кампании, например, название, категорию, язык и валюту.  Он принимает список идентификаторов или URL-адресов товаров и возвращает список обработанных объектов `product`, содержащих аффилированную ссылку и путь к сохранённому изображению (и видео).

Шаги выполнения
-------------------------
1. **Импортировать класс `AliAffiliatedProducts`:**
   ```python
   from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
   ```

2. **Создать экземпляр класса `AliAffiliatedProducts`:**
   ```python
   parser = AliAffiliatedProducts(
       campaign_name,
       campaign_category,
       language,
       currency
   )
   ```
   Укажите параметры кампании: `campaign_name`, `campaign_category`, `language` и `currency`.

3. **Создать список `prod_urls` с идентификаторами или URL-адресами товаров:**
   ```python
   prod_urls = [
       '123',
       'https://www.aliexpress.com/item/123.html',
       '456',
       'https://www.aliexpress.com/item/456.html',
   ]
   ```
   Список может содержать как сами идентификаторы товаров, так и полные URL-адреса.

4. **Обработать товары с помощью метода `process_affiliate_products`:**
   ```python
   products = parser.process_affiliate_products(prod_urls)
   ```
   Этот метод собирает данные, генерирует аффилированные ссылки и сохраняет изображения (и видео). Результат - список объектов `product`.

5. **Проверить полученный результат и обработать список `products`:**
   ```python
   if products:
       print(f"Получено {len(products)} аффилированных товаров.")
       for product in products:
           print(f"ID товара: {product.product_id}")
           print(f"Ссылка: {product.promotion_link}")
           print(f"Путь к изображению: {product.local_saved_image}")
           if product.local_saved_video:
               print(f"Путь к видео: {product.local_saved_video}")
           print()
   else:
       print("Аффилированных товаров не найдено.")
   ```
   Если список `products` пуст, значит, данные для указанных товаров не были получены или обработаны.

Пример использования
-------------------------
```python
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
        print(f"Получено {len(products)} аффилированных товаров.")
        for product in products:
            print(f"ID товара: {product.product_id}")
            print(f"Ссылка: {product.promotion_link}")
            print(f"Путь к изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к видео: {product.local_saved_video}")
            print()
    else:
        print("Аффилированных товаров не найдено.")

if __name__ == "__main__":
    main()
```
```