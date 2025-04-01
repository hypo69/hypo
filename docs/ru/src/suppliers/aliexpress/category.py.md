# Модуль для управления категориями Aliexpress

## Обзор

Модуль `category.py` предназначен для управления категориями товаров на сайте Aliexpress. Он предоставляет функциональность для сбора URL товаров из категорий, обновления информации о категориях в файлах сценариев, а также для взаимодействия с базой данных категорий.

## Подробнее

Модуль выполняет следующие основные задачи:

1.  Сбор ссылок на товары из категорий Aliexpress, включая перелистывание страниц пагинации.
2.  Обновление информации о категориях в файлах сценариев, сравнивая данные на сайте с данными в файле.
3.  Адаптация для работы с базой данных категорий, включая выборку, вставку, обновление и удаление категорий.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str, str]:
    """  
    Считывает URL товаров со страницы категории.

    Args:
        s: Экземпляр класса `Supplier`.

    Returns:
        list[str, str]: Список собранных URL товаров.

    Raises:
        Не вызывает исключений напрямую, но может возникнуть исключение в вызываемой функции `get_prod_urls_from_pagination`.

    Как работает функция:
    1.  Вызывает функцию `get_prod_urls_from_pagination` для получения списка URL товаров.

    2.  Внутри функции происходят следующие действия и преобразования:
        Вызов `get_prod_urls_from_pagination` -> Возврат списка URL товаров
    """
    ...
```

### `get_prod_urls_from_pagination`

```python
def get_prod_urls_from_pagination(s) -> list[str]:
    """   Функция собирает ссылки на товары со страницы категории с перелистыванием страниц

    Args:
        s: Экземпляр класса `Supplier`.

    Returns:
        list[str]: Список ссылок, собранных со страницы категории.

    Raises:
        Не вызывает исключений напрямую, но могут возникнуть исключения при работе с веб-драйвером.

    Как работает функция:
    1.  Получает экземпляр веб-драйвера и локаторы элементов страницы из объекта `Supplier`.
    2.  Извлекает список ссылок на товары с текущей страницы категории.
    3.  Если список пуст, возвращает пустой список.
    4.  В цикле перелистывает страницы категории, пока не достигнет последней страницы.
    5.  Расширяет список ссылок на товары ссылками с каждой новой страницы.
    6.  Возвращает общий список ссылок на товары.

    Внутри функции происходят следующие действия и преобразования:
    A: Инициализация -> B: Извлечение ссылок с текущей страницы -> C: Проверка наличия товаров -> D: Перелистывание страницы (если возможно) -> E: Повторение B-D до последней страницы -> F: Возврат списка ссылок
    """
    ...
```

### `update_categories_in_scenario_file`

```python
def update_categories_in_scenario_file(s, scenario_filename: str) -> bool:
    """  Проверка изменений категорий на сайте
    @details Сличаю фактически файл JSON, полученный с  сайта
    @todo не проверен !!!! """
    ...
```

### Внутренняя функция `_update_all_ids_in_file`

```python
def _update_all_ids_in_file():
    """
    Обновляет список идентификаторов категорий из файла сценария.

    Args:
        Нет явных аргументов. Использует внешние переменные `scenario_json` и `all_ids_in_file`.

    Returns:
        None

    Raises:
        Может вызвать исключение, если значение 'category ID on site' не определено в файле сценария.

    Как работает функция:
    1.  Перебирает все категории в файле сценария.
    2.  Если идентификатор категории больше 0, добавляет его в список `all_ids_in_file`.
    3.  Если идентификатор категории не определен, извлекает его из URL категории и добавляет в список.

    Внутри функции происходят следующие действия и преобразования:
    A: Инициализация -> B: Перебор категорий -> C: Проверка ID категории -> D: Добавление ID в список
    """
    ...
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s,scenario_file,brand=''):
    _d = s.driver
    scenario_json = json_loads(Path(gs.dir_scenarios, f'''{scenario_file}'''))
    _d.get_url(scenario_json['store']['shop categories page'])
    ...
```

## Классы

### `DBAdaptor`

```python
class DBAdaptor:
    """ Адаптер для работы с базой данных категорий Aliexpress.
    Предоставляет методы для выполнения операций CRUD (Create, Read, Update, Delete) с использованием CategoryManager.
    """
    def select(cat_id:int = None, parent_id:int = None, project_cat_id:int = None ):
        """ Пример операции SELECT
        Выбрать все записи из таблицы AliexpressCategory, где parent_category_id равен \'parent_id_value\'
        records = manager.select_record(AliexpressCategory, parent_category_id=\'parent_id_value\')
        print(records)
        """
        ...

    def insert():
        """ Пример операции INSERT
        Вставить новую запись в таблицу AliexpressCategory
        fields = {
            'category_name': 'New Category',
            'parent_category_id': 'Parent ID',
            'hypotez_category_id': 'Hypotez ID'
        }
        manager.insert_record(AliexpressCategory, fields)
        """
        ...

    def update():
        """ Пример операции UPDATE
        Обновить запись в таблице AliexpressCategory, где hypotez_category_id равен \'hypotez_id_value\'
        manager.update_record(AliexpressCategory, 'hypotez_id_value', category_name='Updated Category')
        """
        ...

    def delete():
        """ Пример операции DELETE
        Удалить запись из таблицы AliexpressCategory, где hypotez_category_id равен \'hypotez_id_value\'
        manager.delete_record(AliexpressCategory, 'hypotez_id_value')
        """
        ...
```