# Модуль `hypotez/src/suppliers/aliexpress/category.py`

## Обзор

Модуль `hypotez/src/suppliers/aliexpress/category.py` содержит функции и классы для управления категориями на сайте AliExpress. Он предоставляет инструменты для получения списка товаров в категории, обновления списка категорий в сценарии и взаимодействия с базой данных.

## Оглавление

- [Функции](#функции)
- [Класс `DBAdaptor`](#класс-dbadaptor)


## Функции

### `get_list_products_in_category`

**Описание**: Функция считывает URL товаров со страницы категории, включая перелистывание страниц, если необходимо.

**Параметры**:
- `s` (`Supplier`): Экземпляр класса `Supplier`, предоставляющий доступ к веб-драйверу и локаторам.
- `run_async` (`bool`, необязательный): Устанавливает асинхронность выполнения функции. По умолчанию `False`.


**Возвращает**:
- `list[str, str]`: Список URL-адресов товаров в категории. Возвращает пустой список, если товары отсутствуют.


### `get_prod_urls_from_pagination`

**Описание**: Функция собирает ссылки на товары со страницы категории с перелистыванием страниц.

**Параметры**:
- `s` (`Supplier`): Экземпляр класса `Supplier`.


**Возвращает**:
- `list[str]`: Список URL-адресов товаров. Возвращает пустой список, если товары отсутствуют.


### `update_categories_in_scenario_file`

**Описание**: Функция проверяет изменения категорий на сайте и обновляет файл сценария.

**Параметры**:
- `s` (`Supplier`): Экземпляр класса `Supplier`.
- `scenario_filename` (str): Имя файла сценария.


**Возвращает**:
- `bool`: `True`, если обновление прошло успешно, иначе `None`


**Примечания**:
- Функция требует корректного определения идентификаторов категорий на сайте.
- Функция использует модуль `requests` для получения данных с сайта.


## Класс `DBAdaptor`

**Описание**: Класс, предоставляющий интерфейс для взаимодействия с базой данных для работы с категориями.

**Методы**:

### `select`

**Описание**: Выполняет операцию `SELECT` в базе данных.

**Параметры**:
- `cat_id` (`int`, необязательный): Идентификатор категории.
- `parent_id` (`int`, необязательный): Идентификатор родительской категории.
- `project_cat_id` (`int`, необязательный): Идентификатор категории проекта.


**Возвращает**:
- `list`: Список результатов запроса.

**Примечания**:
- Данный пример демонстрирует запрос к базе данных.  Реальный запрос может быть более сложным.


### `insert`

**Описание**: Выполняет операцию `INSERT` в базе данных.

**Параметры**:
- `fields` (dict): Словарь с полями для вставки.

**Примечания**:
- Данный метод вставляет новую запись в таблицу `AliexpressCategory`.


### `update`

**Описание**: Выполняет операцию `UPDATE` в базе данных.

**Параметры**:
- `hypotez_id_value` (str): Значение `hypotez_category_id` для обновления.
- `category_name` (str): Новое значение для поля `category_name`.

**Примечания**:
- Данный метод обновляет запись в таблице `AliexpressCategory`.


### `delete`

**Описание**: Выполняет операцию `DELETE` в базе данных.

**Параметры**:
- `hypotez_id_value` (str): Значение `hypotez_category_id` для удаления.

**Примечания**:
- Данный метод удаляет запись из таблицы `AliexpressCategory`.