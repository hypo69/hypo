# Модуль `via_webdriver.py`

## Обзор

Модуль `via_webdriver.py` предназначен для парсинга данных с сайта Kualastyle с использованием веб-драйвера. Он содержит функции для получения списка URL товаров на странице категории.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`get_list_products_in_category`](#get_list_products_in_category)

## Функции

### `get_list_products_in_category`

**Описание**: Возвращает список URL товаров со страницы категории.

**Параметры**:
- `s` (Suplier): Объект поставщика, содержащий драйвер и локаторы.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`.

**Пример использования**
   ```python
   s = Suplier(...)
   list_of_products = get_list_products_in_category(s)
   if list_of_products:
       for product_url in list_of_products:
          print(product_url)
   ```