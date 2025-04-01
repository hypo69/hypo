# Документация модуля управления категориями AliExpress

## Обзор

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса продуктов, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

## Подробней

Модуль содержит различные функции и методы для взаимодействия с категориями продуктов на AliExpress, включая извлечение URL-адресов продуктов, обновление категорий в файлах сценариев и управление данными категорий в базе данных.

### Ключевые особенности:

-   **Извлечение URL-адресов продуктов**: Собирает URL-адреса продуктов со страниц категорий.
-   **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
-   **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

## Функции

### `get_list_products_in_category(s: Supplier) -> list[str, str]`

Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

#### Параметры:

-   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

#### Возвращает:

-   Список URL-адресов продуктов со страницы категории.

#### Как работает функция:

1.  Функция `get_list_products_in_category` извлекает список URL-адресов товаров из категории, обрабатывая пагинацию.
2.  Она использует экземпляр `Supplier`, содержащий драйвер браузера и локаторы элементов на странице AliExpress.

```
Начало -> Получение URL продуктов со страницы -> Обработка пагинации -> Список URL продуктов
```

#### Примеры:

```python
from src.suppliers.aliexpress.category import get_list_products_in_category
from src.suppliers.aliexpress import Supplier  # Предполагаемый импорт класса Supplier

# Пример использования
supplier_instance = Supplier()  # Создание экземпляра Supplier (требуется настроить)
category_urls = get_list_products_in_category(supplier_instance)
if category_urls:
    print(f"Найдено {len(category_urls)} URL-адресов продуктов в категории.")
else:
    print("Не удалось получить URL-адреса продуктов в категории.")
```

---

### `get_prod_urls_from_pagination(s: Supplier) -> list[str]`

Получает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию.

#### Параметры:

-   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

#### Возвращает:

-   Список URL-адресов продуктов.

#### Как работает функция:

1.  Функция `get_prod_urls_from_pagination` извлекает URL-адреса товаров, обрабатывая пагинацию на страницах категорий.
2.  Она использует экземпляр `Supplier`, содержащий драйвер браузера и локаторы элементов на странице AliExpress.

```
Начало -> Получение URL продуктов с пагинации -> Список URL продуктов
```

#### Примеры:

```python
from src.suppliers.aliexpress.category import get_prod_urls_from_pagination
from src.suppliers.aliexpress import Supplier  # Предполагаемый импорт класса Supplier

# Пример использования
supplier_instance = Supplier()  # Создание экземпляра Supplier (требуется настроить)
product_urls = get_prod_urls_from_pagination(supplier_instance)
if product_urls:
    print(f"Найдено {len(product_urls)} URL-адресов продуктов на страницах с пагинацией.")
else:
    print("Не удалось получить URL-адреса продуктов со страниц с пагинацией.")
```

---

### `update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool`

Сравнивает категории на сайте с категориями в предоставленном файле сценариев и обновляет файл с любыми изменениями.

#### Параметры:

-   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
-   `scenario_filename` (`str`): Имя файла сценариев для обновления.

#### Возвращает:

-   `True`, если категории были успешно обновлены, `False` в противном случае.

#### Как работает функция:

1.  Функция `update_categories_in_scenario_file` сравнивает категории на сайте с категориями, указанными в файле сценария.
2.  Если обнаружены изменения, файл сценария обновляется.

```
Начало -> Сравнение категорий на сайте и в файле сценария -> Обновление файла сценария (если есть изменения) -> True/False
```

#### Примеры:

```python
from src.suppliers.aliexpress.category import update_categories_in_scenario_file
from src.suppliers.aliexpress import Supplier  # Предполагаемый импорт класса Supplier

# Пример использования
supplier_instance = Supplier()  # Создание экземпляра Supplier (требуется настроить)
scenario_file = 'aliexpress_scenario.json'
update_result = update_categories_in_scenario_file(supplier_instance, scenario_file)
if update_result:
    print("Файл сценария успешно обновлен.")
else:
    print("Не удалось обновить файл сценария.")
```

---

### `get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list`

Извлекает список категорий с сайта AliExpress на основе предоставленного файла сценариев.

#### Параметры:

-   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
-   `scenario_file` (`str`): Файл сценариев, содержащий информацию о категориях.
-   `brand` (`str`, optional): Фильтр по бренду для категорий. По умолчанию ''.

#### Возвращает:

-   Список категорий с сайта.

#### Как работает функция:

1.  Функция `get_list_categories_from_site` извлекает список категорий с сайта AliExpress, используя информацию из файла сценария.
2.  Можно указать фильтр по бренду.

```
Начало -> Чтение категорий из файла сценария -> Извлечение категорий с сайта с фильтром по бренду -> Список категорий
```

#### Примеры:

```python
from src.suppliers.aliexpress.category import get_list_categories_from_site
from src.suppliers.aliexpress import Supplier  # Предполагаемый импорт класса Supplier

# Пример использования
supplier_instance = Supplier()  # Создание экземпляра Supplier (требуется настроить)
scenario_file = 'aliexpress_scenario.json'
categories = get_list_categories_from_site(supplier_instance, scenario_file, brand='Xiaomi')
if categories:
    print(f"Найдено {len(categories)} категорий.")
else:
    print("Не удалось получить список категорий.")
```

---

## Классы

### `DBAdaptor`

Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` с записями `AliexpressCategory`.

#### Методы:

-   `select`: Извлекает записи из таблицы `AliexpressCategory`.
-   `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
-   `update`: Обновляет существующую запись в таблице `AliexpressCategory`.
-   `delete`: Удаляет запись из таблицы `AliexpressCategory`.

#### Принцип работы:

Класс `DBAdaptor` предоставляет интерфейс для выполнения операций CRUD (Create, Read, Update, Delete) с таблицей `AliexpressCategory` в базе данных. Он абстрагирует детали реализации базы данных, позволяя другим частям приложения взаимодействовать с базой данных через методы этого класса.

## Зависимости

Этот модуль зависит от нескольких других модулей для различных функциональных возможностей:

-   `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
-   `src.utils.jjson`: Для работы с данными JSON.
-   `src.logger`: Для логирования ошибок и сообщений.
-   `requests`: Для выполнения HTTP-запросов для получения данных категорий с сайта AliExpress.

---

## Пример использования

```python
from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file
from src.suppliers.aliexpress import Supplier # Предполагаемый импорт класса Supplier

# Пример использования
supplier_instance = Supplier() # Создание экземпляра Supplier (требуется настроить)
category_urls = get_list_products_in_category(supplier_instance)
update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
```

---

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT.