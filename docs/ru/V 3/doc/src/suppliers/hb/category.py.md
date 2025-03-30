# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о товарах с сайта поставщика hb.co.il через вебдрайвер. Он включает в себя функции для получения списка категорий и товаров, а также для навигации по страницам категорий.

## Подробней

Этот модуль играет важную роль в процессе сбора данных о товарах с сайта поставщика. Он автоматизирует навигацию по сайту, извлекает необходимые данные и передает их для дальнейшей обработки. Модуль взаимодействует с вебдрайвером для эмуляции действий пользователя и получения динамически загружаемого контента.

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
- `s` (Supplier): Объект поставщика, содержащий информацию о текущем сценарии и драйвере.

**Возвращает**:
- `list[str, str, None]`: Список URL товаров в категории или `None`, если список пуст.

**Пример**:
```python
# Необходима инициализация объекта Supplier
# from src.suppliers import Supplier
# s = Supplier(...) 
# product_list = get_list_products_in_category(s)
# if product_list:
#     print(f'Найдено {len(product_list)} товаров в категории')
# else:
#     print('Товары в категории не найдены')
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

**Описание**: Осуществляет перелистывание страниц категорий.

**Параметры**:
- `d` (Driver): Объект вебдрайвера.
- `locator` (dict): Словарь с локаторами элементов на странице.
- `list_products_in_category` (list): Список URL товаров в категории.

**Возвращает**:
- `True`: Если перелистывание успешно выполнено.
- `None`: Если перелистывание не удалось.

**Пример**:
```python
# from src.webdriver.driver import Driver
# d = Driver(...)
# locator = {'pagination': {'<-': 'locator_значение'}}
# list_products = ['url1', 'url2']
# if paginator(d, locator, list_products):
#     print('Страница успешно перелистнута')
# else:
#     print('Перелистывание не удалось')
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...
```

**Описание**: Собирает актуальные категории с сайта.

**Параметры**:
- `s`: Параметр не указан в предоставленном коде.

**Возвращает**:
- Нет информации о возвращаемом значении в предоставленном коде.

**Пример**:
```python
# from src.suppliers import Supplier
# s = Supplier(...)
# get_list_categories_from_site(s)