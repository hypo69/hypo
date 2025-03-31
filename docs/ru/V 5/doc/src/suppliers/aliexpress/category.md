# Модуль управления категориями Aliexpress

## Обзор

Этот модуль предоставляет функциональность для управления категориями на AliExpress. Он позволяет извлекать URL-адреса продуктов, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

## Подробней

Модуль содержит различные функции и методы для взаимодействия с категориями продуктов на AliExpress, включая извлечение URL-адресов продуктов, обновление категорий в файлах сценариев и управление данными категорий в базе данных.

### Ключевые особенности:
- **Получение URL-адресов продуктов**: Собирает URL-адреса продуктов со страниц категорий.
- **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.

## Функции

### `get_list_products_in_category(s: Supplier) -> list[str, str]`

Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

**Как работает функция**:
Функция принимает экземпляр поставщика `s`, содержащий драйвер браузера и локаторы, и извлекает список URL-адресов продуктов со страницы категории. Она обрабатывает пагинацию для получения всех URL-адресов продуктов в категории.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает**:
- `list[str, str]`: Список URL-адресов продуктов со страницы категории.

**Примеры**:
```python
from src.suppliers.aliexpress.category import get_list_products_in_category

# Пример использования
supplier_instance = Supplier()
category_urls = get_list_products_in_category(supplier_instance)
print(category_urls)
```

---

### `get_prod_urls_from_pagination(s: Supplier) -> list[str]`

Получает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию.

**Как работает функция**:
Функция принимает экземпляр поставщика `s` и извлекает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию. Она используется для получения URL-адресов продуктов с нескольких страниц категории.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.

**Возвращает**:
- `list[str]`: Список URL-адресов продуктов.

**Примеры**:
```python
from src.suppliers.aliexpress.category import get_prod_urls_from_pagination

# Пример использования
supplier_instance = Supplier()
product_urls = get_prod_urls_from_pagination(supplier_instance)
print(product_urls)
```

---

### `update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool`

Сравнивает категории на сайте с категориями в предоставленном файле сценариев и обновляет файл любыми изменениями.

**Как работает функция**:
Функция принимает экземпляр поставщика `s` и имя файла сценария `scenario_filename`. Она сравнивает категории на сайте с категориями в файле сценария и обновляет файл, если есть изменения.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_filename` (str): Имя файла сценария для обновления.

**Возвращает**:
- `bool`: `True`, если категории были успешно обновлены, `False` в противном случае.

**Примеры**:
```python
from src.suppliers.aliexpress.category import update_categories_in_scenario_file

# Пример использования
supplier_instance = Supplier()
scenario_file = 'example_scenario.json'
updated = update_categories_in_scenario_file(supplier_instance, scenario_file)
print(f'Categories updated: {updated}')
```

---

### `get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list`

Извлекает список категорий с сайта AliExpress на основе предоставленного файла сценария.

**Как работает функция**:
Функция принимает экземпляр поставщика `s`, имя файла сценария `scenario_file` и необязательный фильтр бренда `brand`. Она извлекает список категорий с сайта AliExpress на основе информации в файле сценария.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_file` (str): Файл сценария, содержащий информацию о категориях.
- `brand` (str, optional): Фильтр бренда для категорий.

**Возвращает**:
- `list`: Список категорий с сайта.

**Примеры**:
```python
from src.suppliers.aliexpress.category import get_list_categories_from_site

# Пример использования
supplier_instance = Supplier()
scenario_file = 'example_scenario.json'
categories = get_list_categories_from_site(supplier_instance, scenario_file, brand='ExampleBrand')
print(categories)
```

---

## Классы

### `DBAdaptor`

Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` над записями `AliexpressCategory`.

**Как работает класс**:
Класс `DBAdaptor` предоставляет интерфейс для взаимодействия с базой данных, содержащей категории AliExpress. Он инкапсулирует методы для выполнения стандартных операций CRUD (Create, Read, Update, Delete) над записями `AliexpressCategory`.

**Методы**:
- `select`: Извлекает записи из таблицы `AliexpressCategory`.
- `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
- `update`: Обновляет существующую запись в таблице `AliexpressCategory`.
- `delete`: Удаляет запись из таблицы `AliexpressCategory`.

**Примеры**:
```python
from src.suppliers.aliexpress.category import DBAdaptor

# Пример использования
db_adaptor = DBAdaptor()

# Пример вставки новой категории
db_adaptor.insert(name='New Category', url='http://example.com/new-category')

# Пример выборки категорий
categories = db_adaptor.select(where="name='New Category'")

# Пример обновления категории
if categories:
    category = categories[0]
    db_adaptor.update(category.id, name='Updated Category')

# Пример удаления категории
    db_adaptor.delete(category.id)
```

---

## Зависимости

Этот модуль зависит от нескольких других модулей для различных функциональных возможностей:

- `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
- `src.utils.jjson`: Для работы с данными JSON.
- `src.logger`: Для ведения журнала ошибок и сообщений.
- `requests`: Для выполнения HTTP-запросов для получения данных о категориях с сайта AliExpress.

---

## Пример использования

```python
from src.suppliers.aliexpress.category import get_list_products_in_category, update_categories_in_scenario_file

# Пример использования
supplier_instance = Supplier()
category_urls = get_list_products_in_category(supplier_instance)
update_categories_in_scenario_file(supplier_instance, 'example_scenario.json')
```

---

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT.