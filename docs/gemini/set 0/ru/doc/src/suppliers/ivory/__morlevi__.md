# Модуль `hypotez/src/suppliers/ivory/__morlevi__.py`

## Обзор

Этот модуль предоставляет функции для работы с поставщиком `Morlevi`. Он содержит функции для входа в систему, сбора данных о продуктах и работы с категориями.

## Функции

### `login`

**Описание**: Функция осуществляет вход в систему поставщика `Morlevi`.  Она пытается войти, а затем обрабатывает возможные всплывающие окна.

**Параметры**:
- `supplier` (объект): Объект, содержащий данные о поставщике (например, драйвер браузера и логгер).

**Возвращает**:
- `bool | None`: `True`, если вход успешен, `None` в случае ошибки.


**Вызывает исключения**:
- `Exception`: Возникает в случае непредвиденных ошибок при работе с сайтом Morlevi (например, проблемы с нахождением элементов на странице).


### `_login`

**Описание**: Вспомогательная функция для осуществления входа.  Пробует найти и заполнить поля формы входа.

**Параметры**:
- `_s` (объект): Объект, содержащий данные о поставщике.

**Возвращает**:
- `bool | None`: `True`, если вход успешен, `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при проблемах с нахождением элементов формы или ввода данных.


### `grab_product_page`

**Описание**: Функция собирает данные о продукте с сайта Morlevi.

**Параметры**:
- `s` (объект): Объект, содержащий данные о поставщике.

**Возвращает**:
- `Product`: Объект `Product`, содержащий собранные данные о продукте. Возвращает `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при проблемах с нахождением элементов страницы или обработкой данных.


### `list_products_in_category_from_pagination`

**Описание**: Функция получает список ссылок на продукты из категории на сайте Morlevi, используя пагинацию.

**Параметры**:
- `supplier` (объект): Объект, содержащий данные о поставщике.

**Возвращает**:
- `list`: Список ссылок на продукты или пустой список, если продуктов в категории нет.

**Вызывает исключения**:
- `Exception`: Возникает при проблемах с нахождением элементов на странице или обработкой данных.


### `get_list_products_in_category`

**Описание**: Функция получает список продуктов из категории, используя предоставленные параметры.

**Параметры**:
- `s` (объект): Объект, содержащий данные о поставщике.
- `scenario` (JSON): JSON-данные для сценария.
- `presath` (словарь): Данные для Престашоп.

**Возвращает**:
- `list`: Список продуктов.

**Вызывает исключения**:
- `Exception`: Возникает при проблемах с обработкой данных.


### `get_list_categories_from_site`

**Описание**: Функция для получения списка категорий с сайта.

**Параметры**:
- `s` (объект): Объект, содержащий данные о поставщике.
- `scenario_file` (строка): Путь к файлу с сценарием.
- `brand` (строка, опционально): Название бренда.

**Возвращает**:
-  (не определено): Возвращаемое значение не описано в коде.


## Константы

### `MODE`

**Описание**: Переменная, определяющая режим работы модуля.  В данном случае, значение `'dev'` указывает на режим разработки.


## Импорты

- `pathlib`
- `requests`
- `pandas`
- `selenium.webdriver.remote.webelement`
- `selenium.webdriver.common.keys`
- `gs` (Повторный импорт)
- `settings`
- `suppliers.Product`
- и другие


## Дополнительные Примечания

-  Функции `set_*` внутри `grab_product_page` представляют собой методы для заполнения атрибутов объекта `Product`.
-  Некоторые части кода (например, обработка ошибок и выходные данные) нуждаются в более подробном описании.
-  Используется объектно-ориентированный подход для работы с данными поставщика.
-  Обработка ошибок (`try...except`) должна быть более детализирована.
-  Документация к некоторым функциям (например, `get_list_categories_from_site`) неполная.