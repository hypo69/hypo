# Модуль `category`

## Обзор

Модуль `category` предназначен для управления категориями товаров на сайте Aliexpress. Он предоставляет функциональность для сбора ссылок на товары, проверки изменений в категориях на сайте по сравнению с данными в файле сценария, а также для адаптации данных категорий между сайтом и базой данных.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за автоматизацию работы с категориями товаров Aliexpress. Он используется для извлечения информации о категориях с сайта, сравнения этой информации с данными, хранящимися в файлах сценариев, и обновления этих файлов при необходимости. Также модуль предоставляет инструменты для взаимодействия с базой данных, позволяя добавлять, изменять и удалять категории.

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

**Описание**: Извлекает URL товаров со страницы категории Aliexpress.

**Как работает функция**: Функция предполагает, что веб-драйвер уже открыл страницу категории. Она собирает URL товаров, проходя по всем страницам категории, если их несколько.

**Параметры**:

-   `s`: Экземпляр класса `Supplier`, представляющий поставщика (Aliexpress).

**Возвращает**:

-   `list[str, str]`: Список URL товаров в категории. Может быть пустым, если товаров в категории нет.

**Примеры**:

```python
# Пример использования функции (требуется экземпляр класса Supplier)
# s = Supplier(...)
# urls = get_list_products_in_category(s)
# if urls:
#     print(f"Найдено {len(urls)} товаров в категории")
# else:
#     print("В категории нет товаров")
```

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    ...
```

**Описание**: Собирает ссылки на товары со страницы категории, перелистывая страницы.

**Как работает функция**: Функция использует экземпляр `Supplier` для доступа к веб-драйверу и локаторам элементов на странице. Она извлекает ссылки на товары с текущей страницы и переходит на следующую страницу, пока это возможно.

**Параметры**:

-   `s`: Экземпляр класса `Supplier`, содержащий веб-драйвер и локаторы.

**Возвращает**:

-   `list[str]`: Список URL товаров, найденных на всех страницах категории.

**Примеры**:

```python
# Пример использования функции (требуется экземпляр класса Supplier)
# s = Supplier(...)
# product_urls = get_prod_urls_from_pagination(s)
# if product_urls:
#     print(f"Собрано {len(product_urls)} ссылок на товары")
# else:
#     print("Не найдено ссылок на товары")
```

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    ...
```

**Описание**: Проверяет и обновляет информацию о категориях в файле сценария на основе данных с сайта Aliexpress.

**Как работает функция**: Функция загружает файл сценария, получает список категорий с сайта и сравнивает их. Если находит различия (добавленные или удаленные категории), то обновляет файл сценария и отправляет уведомление.

**Параметры**:

-   `s`: Экземпляр класса `Supplier`.
-   `scenario_filename`: Имя файла сценария.

**Возвращает**:

-   `bool`: `True`, если обновление выполнено успешно.

**Примеры**:

```python
# Пример использования функции (требуется экземпляр класса Supplier и имя файла сценария)
# s = Supplier(...)
# filename = "example_scenario.json"
# result = update_categories_in_scenario_file(s, filename)
# if result:
#     print(f"Файл сценария {filename} успешно обновлен")
# else:
#     print(f"Не удалось обновить файл сценария {filename}")
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    ...
```

**Описание**: Извлекает список категорий с сайта Aliexpress.

**Как работает функция**: Функция получает URL страницы категорий из файла сценария, открывает эту страницу с помощью веб-драйвера и извлекает информацию о категориях. <инструкция для модели gemini:Доработай код функции, чтобы извлекать данные о категориях с веб-страницы и возвращать их в структурированном формате.>

**Параметры**:

-   `s`: Экземпляр класса `Supplier`.
-   `scenario_file`: Имя файла сценария, содержащего URL страницы категорий.
-   `brand`: Бренд (по умолчанию пустая строка).

**Возвращает**:

-   Возвращает: <инструкция для модели gemini:Замените тип возвращаемого значения на описание возвращаемой структуры данных с категориями.>

**Примеры**:

```python
# Пример использования функции (требуется экземпляр класса Supplier и имя файла сценария)
# s = Supplier(...)
# filename = "example_scenario.json"
# categories = get_list_categories_from_site(s, filename)
# if categories:
#     print(f"Найдено {len(categories)} категорий на сайте")
# else:
#     print("Не удалось получить список категорий с сайта")
```

## Классы

### `DBAdaptor`

**Описание**: Класс `DBAdaptor` предоставляет методы для выполнения операций с базой данных, связанных с категориями Aliexpress.

**Как работает класс**:
Класс `DBAdaptor` предоставляет интерфейс для выполнения основных операций с базой данных, таких как выборка, вставка, обновление и удаление записей в таблице `AliexpressCategory`. Он использует класс `CategoryManager` для взаимодействия с базой данных.

**Методы**:

-   `select(cat_id: int = None, parent_id: int = None, project_cat_id: int = None)`: Выполняет операцию SELECT для выборки записей из таблицы `AliexpressCategory`.
-   `insert()`: Выполняет операцию INSERT для добавления новой записи в таблицу `AliexpressCategory`.
-   `update()`: Выполняет операцию UPDATE для обновления существующей записи в таблице `AliexpressCategory`.
-   `delete()`: Выполняет операцию DELETE для удаления записи из таблицы `AliexpressCategory`.

#### `select`

```python
def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
    # Пример операции SELECT
    # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен 'parent_id_value'
    records = manager.select_record(AliexpressCategory, parent_category_id='parent_id_value')
    print(records)
```

**Описание**: Выполняет операцию SELECT для выборки записей из таблицы `AliexpressCategory`.

**Как работает функция**: Функция вызывает метод `select_record` класса `CategoryManager` для выборки записей из таблицы `AliexpressCategory` на основе заданных критериев.

**Параметры**:

-   `cat_id`: Идентификатор категории.
-   `parent_id`: Идентификатор родительской категории.
-   `project_cat_id`: Идентификатор категории в проекте.

**Примеры**:

```python
# Пример использования функции
# db_adaptor = DBAdaptor()
# db_adaptor.select(parent_id=123)
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

**Описание**: Выполняет операцию INSERT для добавления новой записи в таблицу `AliexpressCategory`.

**Как работает функция**: Функция создает словарь с данными новой записи и вызывает метод `insert_record` класса `CategoryManager` для добавления записи в таблицу `AliexpressCategory`.

**Примеры**:

```python
# Пример использования функции
# db_adaptor = DBAdaptor()
# db_adaptor.insert()
```

#### `update`

```python
def update(): 
    # Пример операции UPDATE
    # Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')
```

**Описание**: Выполняет операцию UPDATE для обновления существующей записи в таблице `AliexpressCategory`.

**Как работает функция**: Функция вызывает метод `update_record` класса `CategoryManager` для обновления записи в таблице `AliexpressCategory` на основе заданных критериев и новых данных.

**Примеры**:

```python
# Пример использования функции
# db_adaptor = DBAdaptor()
# db_adaptor.update()
```

#### `delete`

```python
def delete():
    # Пример операции DELETE
    # Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.delete_record(AliexpressCategory, 'hypotez_id_value')
```

**Описание**: Выполняет операцию DELETE для удаления записи из таблицы `AliexpressCategory`.

**Как работает функция**: Функция вызывает метод `delete_record` класса `CategoryManager` для удаления записи из таблицы `AliexpressCategory` на основе заданных критериев.

**Примеры**:

```python
# Пример использования функции
# db_adaptor = DBAdaptor()
# db_adaptor.delete()
```