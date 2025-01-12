# Модуль `src.suppliers.kualastyle.via_webdriver`

## Обзор

Модуль `via_webdriver.py` предназначен для парсинга данных с сайта Kualastyle с использованием веб-драйвера. Он включает в себя функции для получения списка URL-адресов товаров из категорий.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`get_list_products_in_category`](#get_list_products_in_category)

## Функции

### `get_list_products_in_category`

**Описание**: Возвращает список URL-адресов товаров со страницы категории.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list[str, str, None]`: Список URL-адресов товаров или `None`, если не удалось получить список.

**Пример использования**:
```python
# Предполагается, что s - это экземпляр класса поставщика.
list_of_products = get_list_products_in_category(s)
if list_of_products:
    for product_url in list_of_products:
        print(product_url)
```

```