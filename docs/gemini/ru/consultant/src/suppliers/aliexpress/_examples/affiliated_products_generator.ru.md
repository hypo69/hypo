# Received Code

```python
файл примеров для модуля `affiliated_products_generator.py`. Этот файл показывает, как использовать класс `AliAffiliatedProducts` для сбора данных о продуктах и обработки аффилированных ссылок.

### Пример использования `AliAffiliatedProducts`

```python
# пример_использования.py

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
```

### Объяснение примера

- **Создание экземпляра `AliAffiliatedProducts`**:
  ```python
  parser = AliAffiliatedProducts(
      campaign_name,
      campaign_category,
      language,
      currency
  )
  ```
  Здесь мы создаем объект класса `AliAffiliatedProducts`, передавая параметры рекламной кампании.

- **Список URL продуктов или их ID**:
  ```python
  prod_urls = [
      '123',
      'https://www.aliexpress.com/item/123.html',
      '456',
      'https://www.aliexpress.com/item/456.html',
  ]
  ```
  Пример списка продуктов. Можно указать как просто ID, так и полные URL.

- **Обработка продуктов**:
  ```python
  products = parser.process_affiliate_products(prod_urls)
  ```
  Мы вызываем метод `process_affiliate_products`, который обрабатывает продукты, получает аффилированные ссылки и сохраняет изображения и видео.

- **Проверка результатов**:
  ```python
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
  ```
  Здесь мы проверяем, есть ли обработанные продукты, и выводим информацию о каждом продукте.

Этот пример демонстрирует базовое использование класса `AliAffiliatedProducts` и его методов. Вы можете адаптировать его под свои нужды и добавить больше функциональности, если это необходимо.

### Полный файл примеров


```python

```

# Improved Code

```python
# affiliated_products_generator_example.py
"""
Пример использования модуля `affiliated_products_generator`.
============================================================

Этот пример демонстрирует, как использовать класс `AliAffiliatedProducts` для получения аффилированных ссылок для продуктов AliExpress.
"""

import os
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.utils.jjson import j_loads
from src.logger import logger


def main():
    """
    Основная функция для обработки аффилированных продуктов.

    :return: None
    """
    # Параметры рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно задать None
    language = "EN"
    currency = "USD"

    # Экземпляр класса для обработки AliExpress
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Список URL продуктов или их ID
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение аффилированных ссылок
    try:
        products = parser.process_affiliate_products(prod_urls)
    except Exception as e:
        logger.error("Ошибка при обработке продуктов:", exc_info=True)
        return

    # Вывод результатов
    if products:
        print(f"Найдено {len(products)} аффилированных продуктов:")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Путь к изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к видео: {product.local_saved_video}")
            print("-" * 20)
    else:
        print("Не удалось найти аффилированные продукты.")


if __name__ == "__main__":
    main()
```

# Changes Made

- Добавлена документация RST к функции `main`.
- Обработка исключений с использованием `try-except` и `logger.error` для записи ошибок в лог.
- Изменён вывод результатов,  используются более информативные сообщения.
- Удалены лишние комментарии и пояснения.
- Добавлена строка `from src.logger import logger` для импорта необходимой функции логирования.


# FULL Code

```python
# affiliated_products_generator_example.py
"""
Пример использования модуля `affiliated_products_generator`.
============================================================

Этот пример демонстрирует, как использовать класс `AliAffiliatedProducts` для получения аффилированных ссылок для продуктов AliExpress.
"""

import os
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.utils.jjson import j_loads
from src.logger import logger


def main():
    """
    Основная функция для обработки аффилированных продуктов.

    :return: None
    """
    # Параметры рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно задать None
    language = "EN"
    currency = "USD"

    # Экземпляр класса для обработки AliExpress
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Список URL продуктов или их ID
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение аффилированных ссылок
    try:
        products = parser.process_affiliate_products(prod_urls)
    except Exception as e:
        logger.error("Ошибка при обработке продуктов:", exc_info=True)
        return

    # Вывод результатов
    if products:
        print(f"Найдено {len(products)} аффилированных продуктов:")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Аффилированная ссылка: {product.promotion_link}")
            print(f"Путь к изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к видео: {product.local_saved_video}")
            print("-" * 20)
    else:
        print("Не удалось найти аффилированные продукты.")


if __name__ == "__main__":
    main()
```