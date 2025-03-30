# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о товарах с сайта поставщика hb.co.il через веб-драйвер. Он содержит функции для извлечения списка категорий и товаров, а также для навигации по страницам категорий.

## Подробней

Этот модуль является частью процесса сбора данных о товарах с сайта поставщика hb.co.il. Он отвечает за получение списка категорий товаров, списка товаров в каждой категории и передачу URL страниц товаров для дальнейшей обработки. Модуль использует веб-драйвер для взаимодействия с сайтом и извлечения необходимой информации.

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

**Описание**: Возвращает список URL товаров со страницы категории. Функция пролистывает страницы категорий, если это необходимо.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий информацию о текущем сценарии и драйвере.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров или `None`, если товары не найдены.

**Примеры**:
```python
# Пример вызова функции
supplier = Supplier(...)
product_list = get_list_products_in_category(supplier)
if product_list:
    print(f'Найдено {len(product_list)} товаров в категории')
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

**Описание**: Функция для навигации по страницам категорий. Она нажимает на кнопку "назад" для перехода на следующую страницу.

**Параметры**:
- `d` (Driver): Объект веб-драйвера.
- `locator` (dict): Словарь с локаторами элементов на странице.
- `list_products_in_category` (list): Список товаров в текущей категории.

**Возвращает**:
- `bool`: `True`, если переход на следующую страницу был успешным, иначе `None`.

**Примеры**:
```python
# Пример вызова функции
driver = Driver(...)
locator = {'pagination': {'<-': 'locator_значение'}}
product_list = ['товар1', 'товар2']
if paginator(driver, locator, product_list):
    print('Переход на следующую страницу выполнен')
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...
```

**Описание**: Функция для сбора актуальных категорий с сайта.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий информацию о текущем сценарии и драйвере.

**Возвращает**:
- *Нет возвращаемого значения*.

**Примеры**:
```python
# Пример вызова функции
supplier = Supplier(...)
get_list_categories_from_site(supplier)
print('Список категорий собран')