# Пример использования `AliAffiliatedProducts`

## Обзор

Этот файл демонстрирует, как использовать класс `AliAffiliatedProducts` для сбора данных о продуктах и обработки партнерских ссылок.

## Оглавление
1. [Пример использования `AliAffiliatedProducts`](#пример-использования-aliaffiliatedproducts)
2. [Объяснение примера](#объяснение-примера)
3. [Полный пример файла](#полный-пример-файла)

## Пример использования `AliAffiliatedProducts`
```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Set up the ad campaign parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # You can set this to None if you don't need a category
    language = "EN"  # Language for the campaign
    currency = "USD"  # Currency for the campaign

    # Create an instance of the AliAffiliatedProducts class
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Example product URLs or IDs
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Process the products and get a list of products with affiliate links and saved images
    products = parser.process_affiliate_products(prod_urls)

    # Check the results
    if products:
        print(f"Received {len(products)} affiliate products.")
        for product in products:
            print(f"Product ID: {product.product_id}")
            print(f"Affiliate Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_image_path}")
            if product.local_video_path:
                print(f"Local Video Path: {product.local_video_path}")
            print()
    else:
        print("No affiliate products found.")

if __name__ == "__main__":
    main()
```

## Объяснение примера

- **Создание экземпляра `AliAffiliatedProducts`**:
  ```python
  parser = AliAffiliatedProducts(
      campaign_name,
      campaign_category,
      language,
      currency
  )
  ```
  Здесь мы создаем объект `AliAffiliatedProducts` с параметрами рекламной кампании.

- **Список URL-адресов или идентификаторов продуктов**:
  ```python
  prod_urls = [
      '123',
      'https://www.aliexpress.com/item/123.html',
      '456',
      'https://www.aliexpress.com/item/456.html',
  ]
  ```
  Это пример списка URL-адресов или идентификаторов продуктов. Вы можете предоставить либо только идентификаторы, либо полные URL-адреса.

- **Обработка продуктов**:
  ```python
  products = parser.process_affiliate_products(prod_urls)
  ```
  Мы вызываем метод `process_affiliate_products` для обработки продуктов, получения партнерских ссылок и сохранения изображений и видео.

- **Проверка результатов**:
  ```python
  if products:
      print(f"Received {len(products)} affiliate products.")
      for product in products:
          print(f"Product ID: {product.product_id}")
          print(f"Affiliate Link: {product.promotion_link}")
          print(f"Local Image Path: {product.local_image_path}")
          if product.local_video_path:
              print(f"Local Video Path: {product.local_video_path}")
          print()
  else:
      print("No affiliate products found.")
  ```
  Мы проверяем, есть ли обработанные продукты, и выводим подробности о каждом продукте.

## Полный пример файла
```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Set up the ad campaign parameters
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # You can set this to None if you don't need a category
    language = "EN"  # Language for the campaign
    currency = "USD"  # Currency for the campaign

    # Create an instance of the AliAffiliatedProducts class
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Example product URLs or IDs
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Process the products and get a list of products with affiliate links and saved images
    products = parser.process_affiliate_products(prod_urls)

    # Check the results
    if products:
        print(f"Received {len(products)} affiliate products.")
        for product in products:
            print(f"Product ID: {product.product_id}")
            print(f"Affiliate Link: {product.promotion_link}")
            print(f"Local Image Path: {product.local_image_path}")
            if product.local_video_path:
                print(f"Local Video Path: {product.local_video_path}")
            print()
    else:
        print("No affiliate products found.")

if __name__ == "__main__":
    main()
```

Этот файл можно использовать в качестве шаблона для тестирования функциональности класса `AliAffiliatedProducts` и его методов. Вы можете адаптировать его под свои конкретные нужды и добавить больше функциональности по мере необходимости.