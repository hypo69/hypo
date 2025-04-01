# Модуль управления категориями Aliexpress

Этот модуль предоставляет функциональные возможности для управления категориями на AliExpress. Он позволяет извлекать URL-адреса продуктов, обновлять списки категорий и взаимодействовать с платформой AliExpress для синхронизации категорий.

## Обзор

Модуль содержит различные функции и методы для взаимодействия с категориями продуктов на AliExpress, включая извлечение URL-адресов продуктов, обновление категорий в файлах сценариев и управление данными категорий в базе данных.

### Основные характеристики:
- **Извлечение URL-адресов продуктов**: Собирает URL-адреса продуктов со страниц категорий.
- **Синхронизация категорий**: Сравнивает и обновляет категории на сайте с категориями в локальных файлах сценариев.
- **Взаимодействие с базой данных**: Предлагает операции с базой данных для управления категориями.
  
## Функции

### `get_list_products_in_category(s: Supplier) -> list[str, str]`

Извлекает список URL-адресов продуктов со страницы категории, включая пагинацию.

#### Параметры:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

#### Возвращает:
- Список URL-адресов продуктов со страницы категории.

**Как работает функция**:

1.  Функция `get_list_products_in_category` извлекает URL-адреса товаров из указанной категории на сайте AliExpress.

2.  Внутри функции происходят следующие действия и преобразования:

    A.  `Проверка наличия пагинации` - Проверяет, есть ли пагинация на странице категории.
    |
    B.  `Получение URL-адресов` - Извлекает URL-адреса товаров либо с текущей страницы, либо переходит на каждую страницу пагинации и извлекает URL-адреса с каждой страницы.

#### Примеры:
```python
from src.suppliers.aliexpress.category import get_list_products_in_category
from src.suppliers.aliexpress.supplier import Supplier # Предполагаемый импорт

# Пример использования функции get_list_products_in_category
supplier = Supplier() # Инициализация объекта Supplier
product_urls = get_list_products_in_category(supplier)
if product_urls:
    print(f"Найдены URL-адреса продуктов: {product_urls}")
else:
    print("URL-адреса продуктов не найдены.")
```

---

### `get_prod_urls_from_pagination(s: Supplier) -> list[str]`

Извлекает URL-адреса продуктов со страниц категорий, обрабатывая пагинацию.

#### Параметры:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.

#### Возвращает:
- Список URL-адресов продуктов.

**Как работает функция**:

1.  Функция `get_prod_urls_from_pagination` отвечает за извлечение URL-адресов товаров с нескольких страниц категорий, когда присутствует пагинация.

2.  Внутри функции происходят следующие действия и преобразования:

    A.  `Переход по страницам` - Переходит по страницам пагинации.
    |
    B.  `Извлечение URL-адресов с каждой страницы` - Извлекает URL-адреса товаров с каждой страницы.

#### Примеры:
```python
from src.suppliers.aliexpress.category import get_prod_urls_from_pagination
from src.suppliers.aliexpress.supplier import Supplier # Предполагаемый импорт

# Пример использования функции get_prod_urls_from_pagination
supplier = Supplier() # Инициализация объекта Supplier
product_urls = get_prod_urls_from_pagination(supplier)
if product_urls:
    print(f"Найдены URL-адреса продуктов: {product_urls}")
else:
    print("URL-адреса продуктов не найдены.")
```

---

### `update_categories_in_scenario_file(s: Supplier, scenario_filename: str) -> bool`

Сравнивает категории на сайте с категориями в предоставленном файле сценария и обновляет файл любыми изменениями.

#### Параметры:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_filename` (`str`): Имя файла сценария для обновления.

#### Возвращает:
- `True`, если категории были успешно обновлены, `False` в противном случае.

**Как работает функция**:

1.  Функция `update_categories_in_scenario_file` синхронизирует категории, указанные в файле сценария, с категориями, представленными на сайте AliExpress.

2.  Внутри функции происходят следующие действия и преобразования:

    A.  `Считывание категорий из файла` - Читает существующие категории из указанного файла сценария.
    |
    B.  `Сравнение с категориями на сайте` - Получает список категорий с сайта и сравнивает их с категориями, считанными из файла.
    |
    C.  `Обновление файла сценария` - Обновляет файл сценария, добавляя или изменяя категории в соответствии с данными, полученными с сайта.

#### Примеры:
```python
from src.suppliers.aliexpress.category import update_categories_in_scenario_file
from src.suppliers.aliexpress.supplier import Supplier # Предполагаемый импорт

# Пример использования функции update_categories_in_scenario_file
supplier = Supplier() # Инициализация объекта Supplier
scenario_file = 'example_scenario.json'
success = update_categories_in_scenario_file(supplier, scenario_file)
if success:
    print(f"Файл сценария '{scenario_file}' успешно обновлен.")
else:
    print(f"Не удалось обновить файл сценария '{scenario_file}'.")
```

---

### `get_list_categories_from_site(s: Supplier, scenario_file: str, brand: str = '') -> list`

Извлекает список категорий с сайта AliExpress на основе предоставленного файла сценария.

#### Параметры:
- `s` (`Supplier`): Экземпляр поставщика с драйвером браузера и локаторами.
- `scenario_file` (`str`): Файл сценария, содержащий информацию о категориях.
- `brand` (`str`, optional): Фильтр по бренду для категорий.

#### Возвращает:
- Список категорий с сайта.

**Как работает функция**:

1.  Функция `get_list_categories_from_site` получает список категорий с сайта AliExpress, используя информацию из файла сценария и фильтр по бренду.

2.  Внутри функции происходят следующие действия и преобразования:

    A.  `Чтение информации о категориях из файла сценария` - Считывает данные о категориях, включая URL-адреса и другие параметры.
    |
    B.  `Посещение сайта AliExpress` - Использует драйвер браузера для посещения страниц категорий на сайте.
    |
    C.  `Извлечение списка категорий` - Извлекает список категорий с каждой страницы, применяя фильтр по бренду, если он указан.

#### Примеры:
```python
from src.suppliers.aliexpress.category import get_list_categories_from_site
from src.suppliers.aliexpress.supplier import Supplier # Предполагаемый импорт

# Пример использования функции get_list_categories_from_site
supplier = Supplier() # Инициализация объекта Supplier
scenario_file = 'example_scenario.json'
brand = 'ExampleBrand'
categories = get_list_categories_from_site(supplier, scenario_file, brand)
if categories:
    print(f"Найдены категории: {categories}")
else:
    print("Категории не найдены.")
```

---

## Классы

### `DBAdaptor`

Предоставляет методы для взаимодействия с базой данных, позволяя выполнять стандартные операции, такие как `SELECT`, `INSERT`, `UPDATE` и `DELETE` для записей `AliexpressCategory`.

#### Методы:
- `select`: Извлекает записи из таблицы `AliexpressCategory`.
- `insert`: Вставляет новую запись в таблицу `AliexpressCategory`.
- `update`: Обновляет существующую запись в таблице `AliexpressCategory`.
- `delete`: Удаляет запись из таблицы `AliexpressCategory`.

**Как работает класс**:

1.  Класс `DBAdaptor` предоставляет интерфейс для взаимодействия с базой данных, позволяя выполнять операции CRUD (Create, Read, Update, Delete) для записей, связанных с категориями AliExpress.

2.  Описание каждого метода:

    *   `select`: Извлекает записи из таблицы `AliexpressCategory` на основе заданных критериев.
    *   `insert`: Добавляет новую запись в таблицу `AliexpressCategory`, представляющую новую категорию.
    *   `update`: Обновляет существующую запись в таблице `AliexpressCategory` на основе заданных критериев.
    *   `delete`: Удаляет запись из таблицы `AliexpressCategory` на основе заданных критериев.

```python
from src.suppliers.aliexpress.category import DBAdaptor
from src.db.manager_categories.suppliers_categories import AliexpressCategory  # Предполагаемый импорт
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Пример использования класса DBAdaptor
# Создание тестовой базы данных в памяти
engine = create_engine('sqlite:///:memory:')
AliexpressCategory.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание экземпляра DBAdaptor
db_adaptor = DBAdaptor(session, AliexpressCategory)

# Пример использования методов DBAdaptor
# Вставка новой категории
new_category = AliexpressCategory(name='Test Category', url='http://example.com')
db_adaptor.insert(new_category)

# Выбор всех категорий
categories = db_adaptor.select()
for category in categories:
    print(f"Category ID: {category.id}, Name: {category.name}, URL: {category.url}")

# Закрытие сессии
session.close()
```

---

## Зависимости

Этот модуль зависит от нескольких других модулей для различных функциональных возможностей:

- `src.db.manager_categories.suppliers_categories`: Для управления категориями в базе данных.
- `src.utils.jjson`: Для работы с данными JSON.
- `src.logger`: Для логирования ошибок и сообщений.
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