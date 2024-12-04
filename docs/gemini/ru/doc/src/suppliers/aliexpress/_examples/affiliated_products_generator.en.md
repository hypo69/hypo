# Модуль `affiliated_products_generator.en.md`

## Обзор

Этот модуль предоставляет класс `AliAffiliatedProducts` для получения данных о продуктах и создания ссылок на партнёрские программы на AliExpress.  Он позволяет задать параметры рекламной кампании, список URL или ID продуктов и получить список продуктов с ссылками и сохранёнными изображениями.

## Оглавление

- [Модуль `affiliated_products_generator.en.md`](#модуль-affiliated-products-generator-en-md)
- [Обзор](#обзор)
- [Классы](#классы)
  - [`AliAffiliatedProducts`](#али-affiliatedproducts)
- [Пример использования](#пример-использования)
- [Описание примера](#описание-примера)


## Классы

### `AliAffiliatedProducts`

**Описание**: Класс `AliAffiliatedProducts` отвечает за обработку данных о продуктах AliExpress для создания партнёрских ссылок.

**Методы**:

- `process_affiliate_products`:  Обрабатывает список URL или ID продуктов, создаёт партнёрские ссылки и сохраняет изображения и видео.

**Конструктор**:

```python
def __init__(self, campaign_name: str, campaign_category: Optional[str] = None, language: str, currency: str) -> None:
    """
    Args:
        campaign_name (str): Название рекламной кампании.
        campaign_category (Optional[str], optional): Категория рекламной кампании. По умолчанию `None`.
        language (str): Язык рекламной кампании.
        currency (str): Валюта рекламной кампании.

    Raises:
        ValueError: Если входные данные некорректны.
    """
```


## Пример использования

```python
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

def main():
    # Настройка параметров рекламной кампании
    campaign_name = "summer_sale_2024"
    campaign_category = "electronics"  # Можно установить в None, если категория не нужна
    language = "EN"
    currency = "USD"

    # Создание экземпляра класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример списков URL или ID продуктов
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработка продуктов и получение списка продуктов с партнёрскими ссылками и сохранёнными изображениями
    products = parser.process_affiliate_products(prod_urls)

    # Проверка результатов
    if products:
        print(f"Получено {len(products)} продуктов с партнёрскими ссылками.")
        for product in products:
            print(f"ID продукта: {product.product_id}")
            print(f"Партнёрская ссылка: {product.promotion_link}")
            print(f"Путь к локальному изображению: {product.local_saved_image}")
            if product.local_saved_video:
                print(f"Путь к локальному видео: {product.local_saved_video}")
            print()
    else:
        print("Партнёрских продуктов не найдено.")

if __name__ == "__main__":
    main()
```

## Описание примера

Пример демонстрирует использование класса `AliAffiliatedProducts` для обработки списка URL или ID продуктов. Он настраивает параметры кампании, создаёт экземпляр класса, обрабатывает продукты и выводит полученные результаты. Код обрабатывает возможный случай, когда список продуктов пуст.


**Примечание**: Этот пример предполагает наличие определения класса `Product` и его атрибутов (`product_id`, `promotion_link`, `local_saved_image`, `local_saved_video`) в модуле `affiliated_products_generator.py`.  Для полноценной работы необходимо реализовать методы класса `AliAffiliatedProducts`, в частности `process_affiliate_products`, который отвечает за взаимодействие с API AliExpress и загрузку данных.