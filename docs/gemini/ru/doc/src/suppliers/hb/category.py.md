# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о товарах с сайта поставщика hb.co.il через веб-драйвер. Он включает в себя функциональность для извлечения списка категорий и товаров из этих категорий. Модуль учитывает возможность изменения структуры категорий на сайте поставщика и предоставляет методы для итерации по страницам категорий, а также для обработки страниц отдельных товаров.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`get_list_products_in_category`](#get_list_products_in_category)
    - [`paginator`](#paginator)
    - [`get_list_categories_from_site`](#get_list_categories_from_site)

## Функции

### `get_list_products_in_category`

**Описание**: Возвращает список URL товаров со страницы категории. Если необходимо, пролистывает страницы категории.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий необходимую информацию (драйвер, локаторы).

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`, если товары не найдены.

**Пример использования**
```python
from src.suppliers import Supplier
def example():
    s = Supplier()
    list_of_products = get_list_products_in_category(s)
    if list_of_products:
        print(f"Найдено {len(list_of_products)} товаров")
        for product_url in list_of_products:
            print(product_url)
    else:
        print("Товары не найдены")
```

### `paginator`

**Описание**: Функция для переключения на следующую страницу пагинации.

**Параметры**:
- `d` (Driver): Объект веб-драйвера.
- `locator` (dict): Словарь с локаторами элементов.
- `list_products_in_category` (list): Список уже собранных товаров.

**Возвращает**:
- `bool | None`: `True`, если переключение на следующую страницу удалось, `None` в противном случае.

**Пример использования**
```python
from src.webdriver.driver import Driver
def example():
    d = Driver()
    locator = {
        "pagination": {
            "<-": "#next_page"
        }
    }
    list_products_in_category = []
    if paginator(d, locator, list_products_in_category):
        print("Перешли на следующую страницу")
    else:
        print("Следующей страницы нет")
```

### `get_list_categories_from_site`

**Описание**: Функция для сбора списка актуальных категорий с сайта.

**Параметры**:
- `s`:  Объект поставщика.

**Возвращает**:
- `None`:  Функция ничего не возвращает явно.

**Пример использования**
```python
from src.suppliers import Supplier
def example():
    s = Supplier()
    get_list_categories_from_site(s)
    print("Список категорий получен")
```