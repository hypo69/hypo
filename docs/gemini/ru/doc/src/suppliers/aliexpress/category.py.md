# Модуль для управления категориями Aliexpress

## Обзор

Модуль `category.py` предназначен для управления категориями на сайте Aliexpress. Он включает в себя функции для сбора URL товаров из категорий, обновления информации о категориях в файлах сценариев, а также для адаптации данных категорий к базе данных.

## Подробнее

Этот модуль играет важную роль в процессе сбора данных с Aliexpress, обеспечивая функции для навигации по категориям, извлечения информации о товарах и синхронизации данных о категориях между сайтом и локальными файлами сценариев. Он использует веб-драйвер для взаимодействия с сайтом, а также функции для работы с JSON-файлами и базой данных.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str, str]:
    """  
     Считывает URL товаров со страницы категории.

    Args:
        s: экземпляр класса `Supplier`.
        
    Returns:
        list[str, str]: список собранных URL. Может быть пустым, если в исследуемой категории нет товаров.
    """
    ...
```

**Назначение**: Считывает URL товаров со страницы категории Aliexpress. Если категория содержит несколько страниц, функция переходит по ним, собирая ссылки на все товары.

**Параметры**:

-   `s` (Supplier): Экземпляр класса `Supplier`, содержащий информацию о поставщике, включая веб-драйвер и локаторы элементов на странице.

**Возвращает**:

-   `list[str, str]`: Список URL товаров, найденных в категории. Возвращает пустой список, если в категории нет товаров.

**Как работает функция**:

1.  Функция вызывает `get_prod_urls_from_pagination(s)` для получения списка URL товаров.
2.  Возвращает полученный список URL.

**Примеры**:
Предположим, что у нас есть экземпляр класса `Supplier` с настроенным веб-драйвером и определенными локаторами.

```python
# Пример вызова функции
# from src.suppliers.aliexpress.supplier import Supplier  # Assuming Supplier class is defined in supplier.py

# s = Supplier(...)  # Initialize your Supplier object
# product_urls = get_list_products_in_category(s)
# if product_urls:
#     print("Found product URLs:", product_urls)
# else:
#     print("No products found in the category.")
```

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    Args:
        s: экземпляр класса `Supplier`.
        
    Returns:
        list[str]: Список ссылок, собранных со страницы категории
    """
    ...
```

**Назначение**: Функция собирает ссылки на товары со страницы категории, перелистывая страницы пагинации.

**Параметры**:

-   `s` (Supplier): Экземпляр класса `Supplier`, содержащий информацию о поставщике, включая веб-драйвер и локаторы элементов на странице.

**Возвращает**:

-   `list[str]`: Список URL товаров, найденных на всех страницах категории.

**Как работает функция**:

1.  Извлекает драйвер (`_d`) и локаторы (`_l`) из экземпляра поставщика `s`.
2.  Инициализирует пустой список `list_products_in_category` для хранения URL товаров.
3.  Выполняет поиск элементов, соответствующих локатору `_l`, и добавляет их в список `list_products_in_category`.
4.  Если список `list_products_in_category` пуст, возвращает пустой список, так как это означает, что в категории нет товаров.
5.  Запускает цикл, который продолжается до тех пор, пока не будет достигнута последняя страница категории.
6.  Внутри цикла проверяет, есть ли кнопка "следующая страница" (определяется через `s.locators['category']['pagination']['->']`).
    -   Если кнопки "следующая страница" нет, цикл завершается.
    -   Если кнопка есть, добавляет URL товаров с текущей страницы в список `list_products_in_category`.
7.  Возвращает список `list_products_in_category` содержащий URL товаров.

```
    Начало
     ↓
    Извлечение драйвера и локаторов из Supplier (s)
     ↓
    Инициализация списка list_products_in_category
     ↓
    Получение ссылок на товары с текущей страницы
     ↓
    Список list_products_in_category пуст?
     ├── Да: Возврат пустого списка
     └── Нет:
         ↓
        Цикл: Пока есть кнопка "следующая страница"
         ↓
        Нажатие на кнопку "следующая страница"
         ↓
        Добавление ссылок на товары с текущей страницы в list_products_in_category
         ↓
        Конец цикла
         ↓
    Возврат списка list_products_in_category
     ↓
    Конец
```

**Примеры**:

```python
# from src.suppliers.aliexpress.supplier import Supplier  # Assuming Supplier class is defined in supplier.py

# s = Supplier(...)  # Initialize your Supplier object
# product_urls = get_prod_urls_from_pagination(s)
# if product_urls:
#     print("Found product URLs:", product_urls)
# else:
#     print("No products found in the category.")
```

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    Args:
        s:  `Supplier`
        scenario_filename (str): Имя файла сценария.
        
    Returns:
        bool: True в случае успешного завершения.
    """
    ...
```

**Назначение**: Проверяет изменения категорий на сайте Aliexpress и обновляет информацию о категориях в файле сценария.

**Параметры**:

-   `s` (Supplier): Экземпляр класса `Supplier`.
-   `scenario_filename` (str): Имя файла сценария, который необходимо обновить.

**Возвращает**:

-   `bool`: `True` в случае успешного завершения, `None` в случае ошибки.

**Как работает функция**:

1.  Загружает JSON-файл сценария.
2.  Извлекает список категорий из файла сценария.
3.  Получает список категорий с сайта Aliexpress.
4.  Сравнивает списки категорий и определяет добавленные и удаленные категории.
5.  Обновляет файл сценария, добавляя новые категории и отключая удаленные.
6.  Отправляет уведомления о добавленных и удаленных категориях.
7.  Внутренняя функция `_update_all_ids_in_file()`:
    *   Проходит по всем категориям в файле сценария.
    *   Извлекает `category ID on site`, иначе извлекает ID из URL категории.
    *   Формирует список `all_ids_in_file`

```
Начало
 ↓
Загрузка JSON-файла сценария (scenario_filename)
 ↓
Извлечение списка категорий из файла (scenarios_in_file)
 ↓
Получение списка категорий с сайта (categoris_on_site)
 ↓
Инициализация списка all_ids_in_file
 ↓
Определение добавленных и удаленных категорий
 ↓
Обновление файла сценария (добавление новых, отключение удаленных)
 ↓
Отправка уведомлений о добавленных и удаленных категориях
 ↓
Конец
```

**Примеры**:

```python
# from src.suppliers.aliexpress.supplier import Supplier  # Assuming Supplier class is defined in supplier.py

# s = Supplier(...)  # Initialize your Supplier object
# scenario_filename = "example_scenario.json"
# success = update_categories_in_scenario_file(s, scenario_filename)
# if success:
#     print("Scenario file updated successfully.")
# else:
#     print("Failed to update scenario file.")
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand='')
    """ """
    ...
```

**Назначение**: <описание отсутствует>

**Параметры**:
-   `s`: <описание отсутствует>
-   `scenario_file`: <описание отсутствует>
-   `brand`: <описание отсутствует>

**Возвращает**:

-  Отсутствует

**Как работает функция**:

1.  Определяет вебдрайвер `_d` из экземпляра `s`.
2.  Загружает JSON из файла сценария `scenario_file`
3.  Выполняет `_d.get_url(scenario_json['store']['shop categories page'])`

**Примеры**:

```python
# from src.suppliers.aliexpress.supplier import Supplier  # Assuming Supplier class is defined in supplier.py

# s = Supplier(...)  # Initialize your Supplier object
# scenario_file = "example_scenario.json"
# success = get_list_categories_from_site(s, scenario_file)
```

## Классы

### `DBAdaptor`

**Описание**:
Класс `DBAdaptor` предоставляет методы для выполнения операций с базой данных, связанных с категориями Aliexpress. Он использует класс `CategoryManager` для выполнения операций CRUD (Create, Read, Update, Delete) с таблицей `AliexpressCategory`.

**Методы**:

-   `select(cat_id: int = None, parent_id: int = None, project_cat_id: int = None)`: Выбирает записи из таблицы `AliexpressCategory` на основе заданных критериев.
-   `insert()`: Вставляет новую запись в таблицу `AliexpressCategory`.
-   `update()`: Обновляет запись в таблице `AliexpressCategory` на основе заданных критериев.
-   `delete()`: Удаляет запись из таблицы `AliexpressCategory` на основе заданных критериев.

#### `select`

```python
    def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
        # Пример операции SELECT
        # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен 'parent_id_value'
        records = manager.select_record(AliexpressCategory, parent_category_id='parent_id_value')
        print(records)
```

**Назначение**:
Выбирает записи из таблицы `AliexpressCategory` на основе заданных критериев. В текущей реализации выбирает все записи, где `parent_category_id` равен `'parent_id_value'`.

**Параметры**:
-   `cat_id` (int, optional): ID категории. По умолчанию `None`.
-   `parent_id` (int, optional): ID родительской категории. По умолчанию `None`.
-   `project_cat_id` (int, optional): ID категории проекта. По умолчанию `None`.

**Возвращает**:
-   Отсутствует. Результат выборки выводится в консоль.

**Пример использования**:

```python
# Пример вызова метода select
db_adaptor = DBAdaptor()
db_adaptor.select()
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

**Назначение**:
Вставляет новую запись в таблицу `AliexpressCategory` с заданными полями.

**Параметры**:
-   Отсутствуют.

**Возвращает**:
-   Отсутствует.

**Пример использования**:

```python
# Пример вызова метода insert
db_adaptor = DBAdaptor()
db_adaptor.insert()
```

#### `update`

```python
    def update(): 
        # Пример операции UPDATE
        # Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
        manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')
```

**Назначение**:
Обновляет запись в таблице `AliexpressCategory`, где `hypotez_category_id` равен `'hypotez_id_value'`, устанавливая новое значение для `category_name`.

**Параметры**:
-   Отсутствуют.

**Возвращает**:
-   Отсутствует.

**Пример использования**:

```python
# Пример вызова метода update
db_adaptor = DBAdaptor()
db_adaptor.update()
```

#### `delete`

```python
    def delete():
        # Пример операции DELETE
        # Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
        manager.delete_record(AliexpressCategory, 'hypotez_id_value')
```

**Назначение**:
Удаляет запись из таблицы `AliexpressCategory`, где `hypotez_category_id` равен `'hypotez_id_value'`.

**Параметры**:
-   Отсутствуют.

**Возвращает**:
-   Отсутствует.

**Пример использования**:

```python
# Пример вызова метода delete
db_adaptor = DBAdaptor()
db_adaptor.delete()