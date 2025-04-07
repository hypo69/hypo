# Документация модуля управления категориями AliExpress

## Обзор

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса продуктов, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

## Подробнее

Модуль содержит различные функции и методы для взаимодействия с категориями продуктов на AliExpress, включая извлечение URL-адресов продуктов, обновление категорий в файлах сценариев и управление данными категорий в базе данных.

### Основные функции:

-   **Извлечение URL-адресов продуктов**: Собирает URL-адреса продуктов со страниц категорий.
-   **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
-   **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

## Функции

### `get_list_products_in_category(s: Supplier) -> list[str, str]`

Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

**Параметры:**

*   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает:**

*   Список URL-адресов продуктов со страницы категории.

**Как работает функция:**

1.  Функция `get_list_products_in_category` извлекает URL-адреса продуктов из указанной категории на сайте AliExpress.
2.  Она использует предоставленный экземпляр `Supplier` (`s`) для взаимодействия с веб-сайтом через драйвер браузера и локаторы элементов.
3.  Функция обрабатывает пагинацию, чтобы получить все URL-адреса продуктов, даже если они распределены по нескольким страницам.

**ASCII flowchart:**

```
Начало --> Получение URL-адресов продуктов с текущей страницы --> Проверка пагинации --> Если есть следующая страница, переход на неё и повторное получение URL-адресов --> Объединение всех URL-адресов --> Конец
```

**Примеры:**

```python
from src.suppliers.aliexpress.category import get_list_products_in_category
from src.suppliers.aliexpress.supplier import Supplier

# Пример использования
supplier_instance = Supplier() # <инструкция для модели gemini: не забудь инициализировать supplier_instance>
category_urls = get_list_products_in_category(supplier_instance)
if category_urls:
    print(f"Найдено {len(category_urls)} URL-адресов продуктов в категории.")
else:
    print("Не удалось получить URL-адреса продуктов в категории.")
```

---

### `get_prod_urls_from_pagination(s: Supplier) -> list[str]`

Извлекает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию.

**Параметры:**

*   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает:**

*   Список URL-адресов продуктов.

**Как работает функция:**

1.  Функция `get_prod_urls_from_pagination` извлекает URL-адреса продуктов с текущей страницы категории на сайте AliExpress.
2.  Она использует предоставленный экземпляр `Supplier` (`s`) для взаимодействия с веб-сайтом через драйвер браузера и локаторы элементов.
3.  Функция находит все URL-адреса продуктов на текущей странице и возвращает их в виде списка.

**ASCII flowchart:**

```
Начало --> Извлечение URL-адресов продуктов с текущей страницы --> Конец
```

**Примеры:**

```python
from src.suppliers.aliexpress.category import get_prod_urls_from_pagination
from src.suppliers.aliexpress.supplier import Supplier

# Пример использования
supplier_instance = Supplier() # <инструкция для модели gemini: не забудь инициализировать supplier_instance>
product_urls = get_prod_urls_from_pagination(supplier_instance)
if product_urls:
    print(f"Найдено {len(product_urls)} URL-адресов продуктов на странице.")
else:
    print("Не удалось получить URL-адреса продуктов на странице.")
```

---

### `update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool`

Сравнивает категории на сайте с категориями в предоставленном файле сценариев и обновляет файл любыми изменениями.

**Параметры:**

*   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
*   `scenario_filename` (`str`): Имя файла сценария для обновления.

**Возвращает:**

*   `True`, если категории были успешно обновлены, `False` в противном случае.

**Как работает функция:**

1.  Функция `update_categories_in_scenario_file` сравнивает категории, доступные на сайте AliExpress, с категориями, указанными в файле сценария (`scenario_filename`).
2.  Используя предоставленный экземпляр `Supplier` (`s`), функция взаимодействует с веб-сайтом для получения текущих данных о категориях.
3.  Затем она сравнивает эти данные с категориями, хранящимися в файле сценария.
4.  Если обнаружены какие-либо различия (например, добавлены новые категории или изменены существующие), функция обновляет файл сценария, чтобы отразить эти изменения.

**ASCII flowchart:**

```
Начало --> Получение категорий с сайта --> Чтение категорий из файла сценария --> Сравнение категорий --> Обновление файла сценария (если есть изменения) --> Конец
```

**Примеры:**

```python
from src.suppliers.aliexpress.category import update_categories_in_scenario_file
from src.suppliers.aliexpress.supplier import Supplier

# Пример использования
supplier_instance = Supplier() # <инструкция для модели gemini: не забудь инициализировать supplier_instance>
scenario_file = 'aliexpress_categories.json'
update_result = update_categories_in_scenario_file(supplier_instance, scenario_file)
if update_result:
    print(f"Файл сценария '{scenario_file}' успешно обновлен.")
else:
    print(f"Не удалось обновить файл сценария '{scenario_file}'.")
```

---

### `get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list`

Извлекает список категорий с сайта AliExpress на основе предоставленного файла сценариев.

**Параметры:**

*   `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
*   `scenario_file` (`str`): Файл сценария, содержащий информацию о категориях.
*   `brand` (`str`, optional): Фильтр по бренду для категорий.

**Возвращает:**

*   Список категорий с сайта.

**Как работает функция:**

1.  Функция `get_list_categories_from_site` извлекает список категорий с сайта AliExpress.
2.  Она использует предоставленный экземпляр `Supplier` (`s`) для взаимодействия с веб-сайтом через драйвер браузера и локаторы элементов.
3.  Функция читает информацию о категориях из файла сценария (`scenario_file`).
4.  При необходимости она применяет фильтр по бренду (`brand`) для получения только категорий, соответствующих указанному бренду.

**ASCII flowchart:**

```
Начало --> Чтение информации о категориях из файла сценария --> Получение списка категорий с сайта --> Применение фильтра по бренду (если указан) --> Конец
```

**Примеры:**

```python
from src.suppliers.aliexpress.category import get_list_categories_from_site
from src.suppliers.aliexpress.supplier import Supplier

# Пример использования
supplier_instance = Supplier() # <инструкция для модели gemini: не забудь инициализировать supplier_instance>
scenario_file = 'aliexpress_categories.json'
brand_filter = 'ExampleBrand'
category_list = get_list_categories_from_site(supplier_instance, scenario_file, brand_filter)
if category_list:
    print(f"Найдено {len(category_list)} категорий на сайте.")
else:
    print("Не удалось получить список категорий с сайта.")
```

---

## Классы

### `DBAdaptor`

Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.

**Методы:**

*   `select`: Извлекает записи из таблицы `AliexpressCategory`.
*   `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
*   `update`: Обновляет существующую запись в таблице `AliexpressCategory`.
*   `delete`: Удаляет запись из таблицы `AliexpressCategory`.

**Принцип работы:**

Класс `DBAdaptor` предоставляет абстракцию для выполнения операций с базой данных, специфичных для категорий AliExpress. Он инкапсулирует методы для выборки, вставки, обновления и удаления записей из таблицы `AliexpressCategory`.

## Зависимости

Этот модуль зависит от нескольких других модулей для различных функциональных возможностей:

*   `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
*   `src.utils.jjson`: Для работы с данными JSON.
*   `src.logger`: Для ведения журнала ошибок и сообщений.
*   `requests`: Для выполнения HTTP-запросов для получения данных о категориях с сайта AliExpress.

---

## Пример использования

```python
from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file
from src.suppliers.aliexpress.supplier import Supplier

# Пример использования
supplier_instance = Supplier() # <инструкция для модели gemini: не забудь инициализировать supplier_instance>
category_urls = get_list_products_in_category(supplier_instance)
update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
```

---

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT.