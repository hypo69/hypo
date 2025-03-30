# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о товарах с сайта поставщика Kualastyle. Он содержит функции для получения списка категорий и товаров, а также для навигации по страницам категорий. Модуль использует веб-драйвер для взаимодействия с сайтом и извлекает информацию о товарах и категориях.

## Подробней

Этот модуль играет важную роль в процессе сбора данных о товарах от поставщика Kualastyle. Он автоматизирует процесс обхода сайта, начиная со сбора списка категорий (`get_list_categories_from_site()`) и заканчивая извлечением ссылок на товары в каждой категории (`get_list_products_in_category()`). Полученные данные затем используются для дальнейшей обработки и сохранения информации о товарах.

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

**Описание**: Возвращает список URL товаров со страницы категории.

**Параметры**:
- `s` (Supplier): Объект поставщика.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`.

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
- `locator` (dict): Словарь с локаторами элементов страницы.
- `list_products_in_category` (list): Список URL товаров в категории.

**Возвращает**:
- `bool`: `True`, если переключение страницы успешно, иначе `None`.

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...
```

**Описание**: Собирает актуальный список категорий с сайта.

**Параметры**:
- `s`: Параметры

**Возвращает**:
- Нет возвращаемого значения.