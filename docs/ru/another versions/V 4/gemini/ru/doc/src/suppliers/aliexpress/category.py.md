# Модуль `category`

## Обзор

Модуль `category` предназначен для управления категориями товаров на сайте Aliexpress. Он включает в себя функции для сбора URL товаров, обновления категорий в файлах сценариев, а также адаптер для работы с базой данных категорий.

## Подробней

Модуль предназначен для автоматизации работы с категориями товаров на Aliexpress. Он позволяет получать список товаров в категории, обновлять информацию о категориях в файлах сценариев, а также взаимодействовать с базой данных категорий. Модуль использует различные вспомогательные функции и классы, такие как `CategoryManager` и `AliexpressCategory`, для упрощения работы с данными. Расположен в структуре проекта как часть поставщика `aliexpress`, что говорит о его непосредственной связи с задачами парсинга и обработки данных именно с этого сайта.

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

**Описание**: Считывает URL товаров со страницы категории, перелистывая все страницы, если их несколько.

**Параметры**:
- `s`: Экземпляр класса `Supplier`.

**Возвращает**:
- `list[str, str]`: Список собранных URL товаров. Может быть пустым, если в категории нет товаров.

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц 
    @param s `Supplier` 
    @returns list_products_in_category `list` :  Список ссылок, собранных со страницы категории"""
    ...
```

**Описание**: Собирает ссылки на товары со страницы категории с перелистыванием страниц.

**Параметры**:
- `s`: Экземпляр класса `Supplier`.

**Возвращает**:
- `list[str]`: Список ссылок на товары, собранных со страницы категории.

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте 
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    ...
```

**Описание**: Проверяет изменения категорий на сайте и обновляет файл сценария.

**Параметры**:
- `s`: Экземпляр класса `Supplier`.
- `scenario_filename` (str): Имя файла сценария.

**Возвращает**:
- `bool`: `True`, если обновление прошло успешно.

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f\'\'\'{scenario_file}\'\'\'))
    _d.get_url(scenario_json[\'store\'][\'shop categories page\'])\n
    ...
```

**Описание**: Получает список категорий с сайта.

**Параметры**:
- `s`: Экземпляр класса `Supplier`.
- `scenario_file`: Имя файла сценария.
- `brand` (str, optional): Бренд. По умолчанию ''.

## Классы

### `DBAdaptor`

**Описание**: Адаптер для работы с базой данных категорий.

**Методы**:
- `select`: Выборка записей из таблицы категорий.
- `insert`: Вставка новой записи в таблицу категорий.
- `update`: Обновление записи в таблице категорий.
- `delete`: Удаление записи из таблицы категорий.

#### `select`

```python
def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
    # Пример операции SELECT
    # Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен 'parent_id_value'
    records = manager.select_record(AliexpressCategory, parent_category_id='parent_id_value')
    print(records)
```

**Описание**: Выбирает записи из таблицы `AliexpressCategory`.

**Параметры**:
- `cat_id` (int, optional): ID категории. По умолчанию `None`.
- `parent_id` (int, optional): ID родительской категории. По умолчанию `None`.
- `project_cat_id` (int, optional): ID категории проекта. По умолчанию `None`.

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

#### `update`

```python
def update(): 
    # Пример операции UPDATE
    # Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')
```

**Описание**: Обновляет запись в таблице `AliexpressCategory`.

#### `delete`

```python
def delete():
    # Пример операции DELETE
    # Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен 'hypotez_id_value'
    manager.delete_record(AliexpressCategory, 'hypotez_id_value')
```

**Описание**: Удаляет запись из таблицы `AliexpressCategory`.