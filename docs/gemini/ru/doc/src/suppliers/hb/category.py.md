# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о категориях и товарах с сайта поставщика hb.co.il с использованием веб-драйвера. Он включает функции для получения списка категорий, списка товаров в категории и итерации по страницам категорий.

## Оглавление

1.  [Функции](#Функции)
    *   [`get_list_products_in_category`](#get_list_products_in_category)
    *   [`paginator`](#paginator)
    *   [`get_list_categories_from_site`](#get_list_categories_from_site)

## Функции

### `get_list_products_in_category`

**Описание**: Возвращает список URL-адресов товаров со страницы категории.

**Параметры**:

*   `s` (Supplier): Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:

*   `list[str, str, None]`: Список URL-адресов товаров или `None`, если товары не найдены.

**Пример использования:**

```python
    d:Driver = s.driver
    l: dict = s.locators['category']
    ...
    d.wait(1)
    d.execute_locator (s.locators ['product']['close_banner'] )
    d.scroll()
    ...

    list_products_in_category: List = d.execute_locator(l['product_links'])

    if not list_products_in_category:
        logger.warning('Нет ссылок на товары. Так бывает')
        ...
        return
    ...
    while d.current_url != d.previous_url:
        if paginator(d,l,list_products_in_category):
            list_products_in_category.append(d.execute_locator(l['product_links']))
        else:
            break
        
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category

    logger.debug(f""" Found {len(list_products_in_category)} items in category {s.current_scenario['name']} """)
    
    return list_products_in_category
```

### `paginator`

**Описание**: Функция для перелистывания страниц категории.

**Параметры**:

*   `d` (Driver): Объект веб-драйвера.
*   `locator` (dict): Словарь с локаторами для элементов пагинации.
*   `list_products_in_category` (list): Список URL-адресов товаров.

**Возвращает**:

*   `bool | None`: `True`, если удалось перейти на следующую страницу, `None` в противном случае.

**Пример использования:**

```python
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0): 
        ...
        return
    return True
```

### `get_list_categories_from_site`

**Описание**: Функция для сбора списка актуальных категорий с сайта.

**Параметры**:

*   `s` (Supplier): Объект поставщика.

**Возвращает**:

*   `None`: Функция не возвращает значения напрямую.

**Пример использования:**

```python
    ...
```