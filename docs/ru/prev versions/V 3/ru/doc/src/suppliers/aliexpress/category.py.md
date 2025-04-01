# Модуль `category`

## Обзор

Модуль `category` предназначен для управления категориями товаров на сайте Aliexpress. Он включает в себя функции для сбора URL товаров из категорий, обновления информации о категориях из файлов сценариев, а также для взаимодействия с базой данных категорий.

## Подробнее

Этот модуль является частью процесса сбора данных с сайта Aliexpress. Он позволяет автоматизировать навигацию по категориям сайта, извлечение ссылок на товары и синхронизацию данных о категориях между локальными файлами сценариев и информацией на сайте. Также модуль предоставляет интерфейс для выполнения основных операций с базой данных категорий, таких как выборка, вставка, обновление и удаление записей.

## Содержание

- [Функции](#Функции)
  - [`get_list_products_in_category`](#get_list_products_in_category)
  - [`get_prod_urls_from_pagination`](#get_prod_urls_from_pagination)
  - [`update_categories_in_scenario_file`](#update_categories_in_scenario_file)
  - [`get_list_categories_from_site`](#get_list_categories_from_site)
- [Классы](#Классы)
  - [`DBAdaptor`](#DBAdaptor)

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str, str]:
    """  
     Считывает URL товаров со страницы категории.

    @details Если есть несколько страниц с товарами в одной категории - листает все.
    Важно понимать, что к этому моменту вебдрайвер уже открыл страницу категорий.

    @param s `Supplier` - экземпляр поставщика
    @param run_async `bool` - устанавливает синхронность/асинхронность исполнения функции `async_get_list_products_in_category()`

    @returns list_products_in_category `list` - список собранных URL. Может быть пустым, если в исследуемой категории нет товаров.
    """
    ...
```

**Описание**: Считывает URL товаров со страницы категории, перелистывая все страницы, если их несколько. Функция предполагает, что веб-драйвер уже открыл страницу категории.

**Параметры**:
- `s`: `Supplier` - экземпляр поставщика.

**Возвращает**:
- `list[str, str]`: Список собранных URL товаров. Может быть пустым, если в категории нет товаров.

**Примеры**:
```python
# Пример вызова функции get_list_products_in_category
# result = get_list_products_in_category(supplier_instance)
# print(result)
```

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    ...
```

**Описание**: Функция собирает ссылки на товары со страницы категории с перелистыванием страниц.

**Параметры**:
- `s`: `Supplier` - экземпляр поставщика.

**Возвращает**:
- `list[str]`: Список ссылок на товары, собранных со страницы категории.

**Примеры**:
```python
# Пример вызова функции get_prod_urls_from_pagination
# result = get_prod_urls_from_pagination(supplier_instance)
# print(result)
```

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    ...
```

**Описание**: Проверяет изменения категорий на сайте, сравнивая файл JSON, полученный с сайта, с локальным файлом сценария.

**Параметры**:
- `s`: `Supplier` - экземпляр поставщика.
- `scenario_filename`: `str` - имя файла сценария.

**Возвращает**:
- `bool`: `True`, если обновление выполнено успешно.

**Примеры**:
```python
# Пример вызова функции update_categories_in_scenario_file
# result = update_categories_in_scenario_file(supplier_instance, "scenario.json")
# print(result)
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    ...
```

**Описание**: Получает список категорий с сайта.

**Параметры**:
- `s`: `Supplier` - экземпляр поставщика.
- `scenario_file`: `str` - имя файла сценария.
- `brand`: `str` - бренд (по умолчанию '').

**Примеры**:
```python
# Пример вызова функции get_list_categories_from_site
# get_list_categories_from_site(supplier_instance, "scenario.json", "SomeBrand")
```

## Классы

### `DBAdaptor`

**Описание**: Класс `DBAdaptor` предоставляет методы для взаимодействия с базой данных категорий Aliexpress.

**Методы**:
- `select`: Выбирает записи из таблицы `AliexpressCategory`.
- `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
- `update`: Обновляет запись в таблице `AliexpressCategory`.
- `delete`: Удаляет запись из таблицы `AliexpressCategory`.

#### `select`

```python
def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
    # Пример операции SELECT
    # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен 'parent_id_value'
    records = manager.select_record(AliexpressCategory, parent_category_id='parent_id_value')
    print(records)
```

**Описание**: Выбирает записи из таблицы `AliexpressCategory` на основе заданных критериев.

**Параметры**:
- `cat_id`: `int`, идентификатор категории.
- `parent_id`: `int`, идентификатор родительской категории.
- `project_cat_id`: `int`, идентификатор категории в проекте.

**Примеры**:
```python
# Пример вызова метода select
# DBAdaptor.select(parent_id=123)
```

#### `insert`

```python
def insert():  
    # Пример операции INSERT
    # Вставить новую запись в таблицу AliexpressCategory
    fields = {
        'category_name': 'New Category',
        'parent_category_id': 'Parent ID',
        'hypotez_category_id': 'Hypotez ID'
    }
    manager.insert_record(AliexpressCategory, fields)
```

**Описание**: Вставляет новую запись в таблицу `AliexpressCategory`.

**Примеры**:
```python
# Пример вызова метода insert
# DBAdaptor.insert()
```

#### `update`

```python
def update(): 
    # Пример операции UPDATE
    # Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')
```

**Описание**: Обновляет запись в таблице `AliexpressCategory`.

**Примеры**:
```python
# Пример вызова метода update
# DBAdaptor.update()
```

#### `delete`

```python
def delete():
    # Пример операции DELETE
    # Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.delete_record(AliexpressCategory, 'hypotez_id_value')
```

**Описание**: Удаляет запись из таблицы `AliexpressCategory`.

**Примеры**:
```python
# Пример вызова метода delete
# DBAdaptor.delete()
```