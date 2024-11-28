# Пример использования модуля `affiliated_products_generator.py` для AliExpress

Этот файл демонстрирует, как использовать класс `AliAffiliatedProducts` для сбора данных о продуктах и обработки аффилированных ссылок для AliExpress.

**Пример использования `AliAffiliatedProducts`**

```python
# example_usage.py

from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Настройка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить значение None, если категория не нужна
    language = "EN"  # Язык кампании
    currency = "USD"  # Валюта кампании

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL или ID продуктов
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с аффилированными ссылками и сохраненными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
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
        print("Аффилированных продуктов не найдено.")

if __name__ == "__main__":
    main()
```

**Описание примера:**

* **Создание экземпляра `AliAffiliatedProducts`:**
  ```python
  parser = AliAffiliatedProducts(
      campaign_name,
      campaign_category,
      language,
      currency
  )
  ```
  Создает объект `AliAffiliatedProducts` с параметрами рекламной кампании.

* **Список URL или ID продуктов:**
  ```python
  prod_urls = [
      '123',
      'https://www.aliexpress.com/item/123.html',
      '456',
      'https://www.aliexpress.com/item/456.html',
  ]
  ```
  Это пример списка URL или ID продуктов. Можно использовать только ID или полные URL-адреса.

* **Обработка продуктов:**
  ```python
  products = parser.process_affiliate_products(prod_urls)
  ```
  Вызывает метод `process_affiliate_products`, чтобы обработать продукты, получить аффилированные ссылки и сохранить изображения и видео.

* **Проверка результатов:**
  ```python
  if products:
      # Вывод результатов обработки
  else:
      # Вывод сообщения об отсутствии продуктов
  ```
  Проверяет, есть ли обработанные продукты, и выводит детали каждого продукта.

**Важно:**

Этот код является примером.  Для его работы необходим класс `AliAffiliatedProducts` (в файле `affiliated_products_generator.py`), содержащий логику для получения аффилированных ссылок, скачивания изображений и видео.  В примере предполагается, что у класса `AliAffiliatedProducts` есть атрибуты `product_id`, `promotion_link`, `local_saved_image` и `local_saved_video`.  Кроме того, необходимо установить необходимую библиотеку для работы с сайтом AliExpress.


Этот файл можно использовать как шаблон для тестирования функциональности класса `AliAffiliatedProducts` и его методов.  Его можно адаптировать под ваши потребности и добавить дополнительную функциональность по мере необходимости.