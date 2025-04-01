# Модуль управления категориями Aliexpress

## Обзор

Модуль предназначен для управления категориями товаров на Aliexpress. Он предоставляет функциональность для работы с категориями товаров, включая получение списка товаров из категории, обновление категорий на основе данных с сайта и операции с базой данных.

## Подробней

Модуль используется для автоматизации работы с категориями товаров на Aliexpress. Он позволяет получать актуальную информацию о категориях и товарах, а также обновлять данные в базе данных и файлах сценариев. Это необходимо для поддержания актуальности информации о товарах и категориях в проекте `hypotez`.

## Оглавление

- [Функции модуля](#функции-модуля)
  - [get_list_products_in_category(s)](#get_list_products_in_categorys)
  - [get_prod_urls_from_pagination(s)](#get_prod_urls_from_paginations)
  - [update_categories_in_scenario_file(s, scenario_filename)](#update_categories_in_scenario_files-scenario_filename)
  - [get_list_categories_from_site(s, scenario_file, brand='')](#get_list_categories_from_sites-scenario_file-brand)
- [Класс DBAdaptor](#класс-dbadaptor)
- [Установка](#установка)

## Функции модуля

### `get_list_products_in_category(s)`

```python
def get_list_products_in_category(s):
    """ This if example function
    Args:
        s (Supplier): Экземпляр поставщика.
    Returns:
        Список URL продуктов в категории.
     """
```

**Описание**: Считывает URL товаров со страницы категории. Если есть несколько страниц с товарами, функция будет перелистывать все страницы.

**Аргументы**:
- `s` (`Supplier`): Экземпляр поставщика.

**Возвращает**:
- Список URL продуктов в категории.

**Примеры**:
```python
# Пример использования функции get_list_products_in_category
products = get_list_products_in_category(supplier)
```

### `get_prod_urls_from_pagination(s)`

```python
def get_prod_urls_from_pagination(s):
    """ This if example function
    Args:
        s (Supplier): Экземпляр поставщика.
    Returns:
        Список ссылок на товары.
     """
```

**Описание**: Собирает ссылки на товары с страницы категории с перелистыванием страниц.

**Аргументы**:
- `s` (`Supplier`): Экземпляр поставщика.

**Возвращает**:
- Список ссылок на товары.

**Примеры**:
```python
# Пример использования функции get_prod_urls_from_pagination
product_urls = get_prod_urls_from_pagination(supplier)
```

### `update_categories_in_scenario_file(s, scenario_filename)`

```python
def update_categories_in_scenario_file(s, scenario_filename):
    """ This if example function
    Args:
        s (Supplier): Экземпляр поставщика.
        scenario_filename (str): Имя файла сценария для обновления.
    Returns:
        True, если обновление прошло успешно.
     """
```

**Описание**: Проверяет изменения категорий на сайте и обновляет файл сценария.

**Аргументы**:
- `s` (`Supplier`): Экземпляр поставщика.
- `scenario_filename` (str): Имя файла сценария для обновления.

**Возвращает**:
- `True`, если обновление прошло успешно.

**Примеры**:
```python
# Пример использования функции update_categories_in_scenario_file
updated = update_categories_in_scenario_file(supplier, "scenario_file.json")
```

### `get_list_categories_from_site(s, scenario_file, brand='')`

```python
def get_list_categories_from_site(s, scenario_file, brand=''):
    """ This if example function
    Args:
        s (Supplier): Экземпляр поставщика.
        scenario_file (str): Имя файла сценария.
        brand (str, optional): Опциональное имя бренда.
    Returns:
        Список категорий.
     """
```

**Описание**: Получает список категорий с сайта на основе файла сценария.

**Аргументы**:
- `s` (`Supplier`): Экземпляр поставщика.
- `scenario_file` (str): Имя файла сценария.
- `brand` (str, optional): Опциональное имя бренда.

**Возвращает**:
- Список категорий.

**Примеры**:
```python
# Пример использования функции get_list_categories_from_site
categories = get_list_categories_from_site(supplier, "scenario_file.json", brand="SomeBrand")
```

## Класс `DBAdaptor`

**Описание**: Предоставляет методы для выполнения операций с базой данных, таких как `SELECT`, `INSERT`, `UPDATE` и `DELETE`.

**Методы**:
- `select(cat_id, parent_id, project_cat_id)`: Выбирает записи из базы данных.
- `insert()`: Вставляет новые записи в базу данных.
- `update()`: Обновляет записи в базе данных.
- `delete()`: Удаляет записи из базы данных.

**Примеры**
```python
# Пример использования DBAdaptor для операций с базой данных
db = DBAdaptor()
db.select(cat_id=123)
db.insert()
db.update()
db.delete()
```

## Установка

Для работы с модулем необходимо установить зависимые пакеты, такие как `requests`, а также настроить соединение с базой данных через `gs.db_translations_credentials`.

### Зависимости:
- `requests`
- `src.utils.jjson`
- `src.db.manager_categories.suppliers_categories`