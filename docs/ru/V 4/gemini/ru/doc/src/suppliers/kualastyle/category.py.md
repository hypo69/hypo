# src.suppliers.kualastyle.category

## Обзор

Модуль `category.py` предназначен для сбора данных о товарах с сайта поставщика Kualastyle, начиная со страниц категорий. Он содержит функции для извлечения списка категорий и товаров, а также для навигации по страницам категорий.

## Подробней

Этот модуль играет важную роль в процессе сбора данных о товарах у поставщика Kualastyle. Он использует веб-драйвер для взаимодействия с сайтом, извлекает информацию о категориях товаров и ссылки на отдельные товары в этих категориях. Собранные данные затем используются для дальнейшей обработки и сохранения информации о товарах.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category (s: Supplier) -> list[str, str, None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
    ...
```

**Описание**: Извлекает список URL товаров со страницы категории. Если требуется, осуществляет пролистывание страниц категорий.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий информацию о драйвере и локаторах элементов на странице.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`, если товары не найдены.

**Примеры**:
```python
# Пример вызова функции
supplier = Supplier(...)  # Необходимо инициализировать объект Supplier
product_list = get_list_products_in_category(supplier)
if product_list:
    print(f'Найдено {len(product_list)} товаров в категории')
else:
    print('Товары в категории не найдены')
```

### `paginator`

```python
def paginator(d:Driver, locator: dict, list_products_in_category: list):
    """ Листалка """
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0): 
        ...
        return
    return True
```

**Описание**: Осуществляет навигацию по страницам категорий.

**Параметры**:
- `d` (Driver): Объект веб-драйвера.
- `locator` (dict): Словарь с локаторами элементов на странице.
- `list_products_in_category` (list): Список товаров в категории.

**Возвращает**:
- `bool`: `True`, если перелистывание выполнено успешно, иначе `None`.

**Примеры**:
```python
# Пример вызова функции
driver = Driver(...)  # Необходимо инициализировать объект Driver
locator = {...}  # Необходимо определить локаторы
product_list = [...]  # Необходимо инициализировать список товаров
if paginator(driver, locator, product_list):
    print('Страница перелистнута')
else:
    print('Перелистывание не выполнено')
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...
```

**Описание**: Собирает список актуальных категорий с сайта.

**Параметры**:
- `s` (Supplier): Объект поставщика.

**Примеры**:
```python
# Пример вызова функции
supplier = Supplier(...)  # Необходимо инициализировать объект Supplier
categories = get_list_categories_from_site(supplier)
if categories:
    print(f'Найдено {len(categories)} категорий')
else:
    print('Категории не найдены')