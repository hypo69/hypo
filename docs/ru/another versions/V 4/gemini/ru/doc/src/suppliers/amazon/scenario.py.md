# Модуль `src.suppliers.amazon.scenario`

## Обзор

Модуль `src.suppliers.amazon.scenario` предназначен для сбора информации о товарах со страниц категорий поставщика Amazon с использованием веб-драйвера. Он содержит функциональность для извлечения списка категорий и товаров, а также для обработки данных о товарах. Модуль адаптирован для работы с Amazon и может быть расширен для поддержки других поставщиков.

## Подробней

Этот модуль играет важную роль в процессе сбора данных о товарах от поставщиков. Он автоматизирует навигацию по страницам категорий на сайте Amazon, извлекает ссылки на товары и передает их для дальнейшей обработки. Модуль также включает логику для проверки наличия товаров в базе данных магазина.
В проекте `hypotez` этот модуль обеспечивает сбор данных о товарах с сайта Amazon, что необходимо для анализа и обработки информации о товарах.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str,str,None]:
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
    @param s: Supplier - Supplier intstance
    @returns list or one of products urls or None
    """
```

**Описание**:
Функция `get_list_products_in_category` извлекает список URL товаров со страницы категории.

**Параметры**:
- `s`: Supplier - экземпляр класса `Supplier`.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`, если список не найден.

**Пример**:

```python
from src.suppliers.amazon.scenario import get_list_products_in_category
from src.suppliers.amazon.supplier import Supplier

# Пример использования функции get_list_products_in_category
supplier = Supplier()  # Инициализация экземпляра Supplier
product_list = get_list_products_in_category(supplier)

if product_list:
    print(f"Найдено {len(product_list)} товаров.")
    for product_url in product_list:
        print(product_url)
else:
    print("Товары не найдены.")