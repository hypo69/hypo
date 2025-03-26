# Пример использования модуля `affiliated_products_generator.py`

## Обзор

Этот файл демонстрирует, как использовать класс `AliAffiliatedProducts` для сбора данных о продуктах и обработки партнерских ссылок.

## Оглавление
- [Обзор](#обзор)
- [Пример использования `AliAffiliatedProducts`](#пример-использования-aliaffiliatedproducts)
- [Разъяснение примера](#разъяснение-примера)
- [Полный пример файла](#полный-пример-файла)

## Пример использования `AliAffiliatedProducts`

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Настройка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить в None, если категория не нужна
    language = "EN"  # Язык для кампании
    currency = "USD"  # Валюта для кампании

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL-адресов или ID продуктов
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с партнерскими ссылками и сохраненными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} партнерских продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Партнерская ссылка: {product.promotion_link}")
            print(f"Локальный путь к изображению: {product.local_image_path}")
            if product.local_video_path:
                print(f"Локальный путь к видео: {product.local_video_path}")
            print()
    else:
        print("Партнерские продукты не найдены.")

if __name__ == "__main__":
    main()
```

## Разъяснение примера

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

- **Список URL-адресов или ID продуктов**:
  ```python
  prod_urls = [
      '123',
      'https://www.aliexpress.com/item/123.html',
      '456',
      'https://www.aliexpress.com/item/456.html',
  ]
  ```
  Это пример списка URL-адресов или ID продуктов. Вы можете предоставить либо только ID, либо полные URL-адреса.

- **Обработка продуктов**:
  ```python
  products = parser.process_affiliate_products(prod_urls)
  ```
  Мы вызываем метод `process_affiliate_products` для обработки продуктов, получения партнерских ссылок и сохранения изображений и видео.

- **Проверка результатов**:
  ```python
  if products:
      print(f"Получено {len(products)} партнерских продуктов.")
      for product in products:
          print(f"ID продукта: {product.product_id}")
          print(f"Партнерская ссылка: {product.promotion_link}")
          print(f"Локальный путь к изображению: {product.local_image_path}")
          if product.local_video_path:
              print(f"Локальный путь к видео: {product.local_video_path}")
          print()
  else:
      print("Партнерские продукты не найдены.")
  ```
  Мы проверяем, есть ли обработанные продукты, и выводим подробную информацию о каждом продукте.

## Полный пример файла

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Настройка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить в None, если категория не нужна
    language = "EN"  # Язык для кампании
    currency = "USD"  # Валюта для кампании

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL-адресов или ID продуктов
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с партнерскими ссылками и сохраненными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} партнерских продуктов.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Партнерская ссылка: {product.promotion_link}")
            print(f"Локальный путь к изображению: {product.local_image_path}")
            if product.local_video_path:
                print(f"Локальный путь к видео: {product.local_video_path}")
            print()
    else:
        print("Партнерские продукты не найдены.")

if __name__ == "__main__":
    main()
```

Этот файл можно использовать в качестве шаблона для тестирования функциональности класса `AliAffiliatedProducts` и его методов. Вы можете адаптировать его для своих конкретных нужд и добавить дополнительную функциональность по мере необходимости.