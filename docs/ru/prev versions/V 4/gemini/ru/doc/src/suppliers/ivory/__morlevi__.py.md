# Модуль src.suppliers.ivory.__morlevi__

## Обзор

Модуль предназначен для работы с поставщиком Morlevi. Он содержит функции для авторизации на сайте поставщика, сбора информации о товарах и получения списка товаров в категории.

## Подробней

Модуль `__morlevi__.py` является частью пакета `src.suppliers.ivory` и предназначен для автоматизации взаимодействия с сайтом поставщика Morlevi. Он включает в себя функции для входа в систему, сбора данных о товарах и навигации по категориям. Этот модуль использует библиотеки `requests`, `pandas` и `selenium` для выполнения HTTP-запросов, обработки данных и управления веб-браузером. Модуль предназначен для интеграции с системой PrestaShop.

## Функции

### `login`

```python
def login(supplier):
    """
    Args:
        supplier: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

    Returns:
        bool: True, если вход выполнен успешно, иначе None.

    Raises:
        Exception: Если не удалось залогиниться.

    Example:
        >>> # Пример использования функции login
        >>> supplier = Supplier(...)
        >>> if login(supplier):
        >>>     print("Login successful")
        >>> else:
        >>>     print("Login failed")
    """
    ...
```

**Описание**: Выполняет вход на сайт поставщика Morlevi.

**Параметры**:

- `supplier`: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `None`.

**Вызывает исключения**:

- `Exception`: Если не удалось залогиниться.

### `_login`

```python
def _login(_s):
    """
    Args:
        _s: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

    Returns:
        bool: True, если вход выполнен успешно, иначе None.

    Raises:
        Exception: Если произошла ошибка во время входа.

    Example:
        >>> # Пример использования функции _login
        >>> supplier = Supplier(...)
        >>> if _login(supplier):
        >>>     print("Login successful")
        >>> else:
        >>>     print("Login failed")
    """
    ...
```

**Описание**: Внутренняя функция для выполнения фактического входа на сайт Morlevi.

**Параметры**:

- `_s`: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `None`.

**Вызывает исключения**:

- `Exception`: Если произошла ошибка во время входа.

### `grab_product_page`

```python
def grab_product_page(s):
    """
    Args:
        s: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

    Returns:
        Product: Объект Product, содержащий информацию о товаре.

    Raises:
        Exception: Если не удалось получить информацию о товаре.

    Example:
        >>> # Пример использования функции grab_product_page
        >>> supplier = Supplier(...)
        >>> product = grab_product_page(supplier)
        >>> print(product.fields)
    """
    ...
```

**Описание**: Собирает информацию о товаре со страницы товара на сайте поставщика.

**Параметры**:

- `s`: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

**Возвращает**:

- `Product`: Объект `Product`, содержащий информацию о товаре.

### `list_products_in_category_from_pagination`

```python
def list_products_in_category_from_pagination(supplier):
    """
    Args:
        supplier: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

    Returns:
        list: Список ссылок на товары в категории.

    Raises:
        Exception: Если не удалось получить список товаров в категории.

    Example:
        >>> # Пример использования функции list_products_in_category_from_pagination
        >>> supplier = Supplier(...)
        >>> product_list = list_products_in_category_from_pagination(supplier)
        >>> print(product_list)
    """
    ...
```

**Описание**: Получает список товаров в категории, переходя по страницам пагинации.

**Параметры**:

- `supplier`: Объект поставщика, содержащий информацию о поставщике и драйвер Selenium.

**Возвращает**:

- `list`: Список ссылок на товары в категории.

**Вызывает исключения**:

- `Exception`: Если не удалось получить список товаров в категории.

### `get_list_products_in_category`

```python
def get_list_products_in_category(s, scenario, presath):
    """
    Args:
        s: Supplier
        scenario: JSON
        presath: PrestaShopWebServiceDict

    Returns:
        None:

    Raises:
        Exception: Описание ситуации, в которой возникает исключение `Exception`.
    """
    ...
```

**Описание**: Функция для получения списка продуктов в заданной категории.

**Параметры**:

- `s`: Объект поставщика `Supplier`.
- `scenario`: JSON-сценарий.
- `presath`: Словарь для взаимодействия с PrestaShop WebService.

**Возвращает**:

- `None`: Функция ничего не возвращает.

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    """
    Args:
        s:
        scenario_file:
        brand (str, optional):  (Default: '')

    Returns:
        None:

    Raises:
        Exception: Описание ситуации, в которой возникает исключение `Exception`.
    """
    ...
```

**Описание**: Функция для получения списка категорий с сайта.

**Параметры**:

- `s`: Объект поставщика.
- `scenario_file`: Файл сценария.
- `brand` (str, optional): Бренд. По умолчанию ''.

**Возвращает**:

- `None`: Функция ничего не возвращает.