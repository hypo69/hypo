# Модуль управления категориями Aliexpress

## Обзор

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса продуктов, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

## Подорбней

Модуль содержит различные функции и методы для взаимодействия с категориями продуктов на AliExpress, включая извлечение URL-адресов продуктов, обновление категорий в файлах сценариев и управление данными категорий в базе данных.

### Основные функции:
- **Извлечение URL-адресов продуктов**: Собирает URL-адреса продуктов со страниц категорий.
- **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s: Supplier) -> list[str, str]:
    """
    Args:
        s (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.

    Returns:
        list[str, str]: Список URL-адресов продуктов со страницы категории.

    Raises:
        Не вызывает исключений.

    Example:
        from src.suppliers.aliexpress.category import get_list_products_in_category
        supplier_instance = Supplier()
        category_urls = get_list_products_in_category(supplier_instance)
        print(category_urls)
    """
    ...
```

**Описание**: Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

**Параметры**:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает**:
- Список URL-адресов продуктов со страницы категории.

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s: Supplier) -> list[str]:
    """
    Args:
        s (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.

    Returns:
        list[str]: Список URL-адресов продуктов.

    Raises:
        Не вызывает исключений.

    Example:
        from src.suppliers.aliexpress.category import get_prod_urls_from_pagination
        supplier_instance = Supplier()
        product_urls = get_prod_urls_from_pagination(supplier_instance)
        print(product_urls)
    """
    ...
```

**Описание**: Получает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию.

**Параметры**:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает**:
- Список URL-адресов продуктов.

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool:
    """
    Args:
        s (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.
        scenario_filename (str): Имя файла сценария, который необходимо обновить.

    Returns:
        bool: `True`, если категории были успешно обновлены, `False` в противном случае.

    Raises:
        Не вызывает исключений.

    Example:
        from src.suppliers.aliexpress.category import update_categories_in_scenario_file
        supplier_instance = Supplier()
        result = update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
        print(result)
    """
    ...
```

**Описание**: Сравнивает категории на сайте с категориями в предоставленном файле сценария и обновляет файл с любыми изменениями.

**Параметры**:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_filename` (`str`): Имя файла сценария, который необходимо обновить.

**Возвращает**:
- `True`, если категории были успешно обновлены, `False` в противном случае.

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list:
    """
    Args:
        s (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.
        scenario_file (str): Файл сценария, содержащий информацию о категории.
        brand (str, optional): Фильтр бренда для категорий.

    Returns:
        list: Список категорий с сайта.

    Raises:
        Не вызывает исключений.

    Example:
        from src.suppliers.aliexpress.category import get_list_categories_from_site
        supplier_instance = Supplier()
        categories = get_list_categories_from_site(supplier_instance, 'example_scenario.json', brand='example_brand')
        print(categories)
    """
    ...
```

**Описание**: Получает список категорий с сайта AliExpress на основе предоставленного файла сценария.

**Параметры**:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_file` (`str`): Файл сценария, содержащий информацию о категории.
- `brand` (`str`, optional): Фильтр бренда для категорий.

**Возвращает**:
- Список категорий с сайта.

## Классы

### `DBAdaptor`

**Описание**: Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.

**Методы**:
- `select`: Извлекает записи из таблицы `AliexpressCategory`.
- `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
- `update`: Обновляет существующую запись в таблице `AliexpressCategory`.
- `delete`: Удаляет запись из таблицы `AliexpressCategory`.

## Зависимости

Этот модуль зависит от нескольких других модулей для различных функциональных возможностей:

- `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
- `src.utils.jjson`: Для работы с данными JSON.
- `src.logger`: Для регистрации ошибок и сообщений.
- `requests`: Для выполнения HTTP-запросов для получения данных категорий с сайта AliExpress.

## Пример использования

```python
from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

# Пример использования
supplier_instance = Supplier()
category_urls = get_list_products_in_category(supplier_instance)
update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
```

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT.