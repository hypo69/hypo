# Модуль `category.py`

## Обзор

Модуль `category.py` предназначен для сбора данных о категориях и товарах с веб-сайта поставщика kualastyle. Он включает в себя функции для получения списка категорий, списка товаров в каждой категории и итерации по страницам категорий. Модуль использует веб-драйвер для взаимодействия с сайтом и извлечения необходимой информации.

## Подробней

Этот модуль является частью процесса сбора данных о товарах от поставщика kualastyle. Он выполняет следующие основные задачи:

1.  **Сбор списка категорий**: Получает список категорий товаров с сайта поставщика.
2.  **Сбор списка товаров**: Для каждой категории собирает список URL товаров.
3.  **Обработка страниц**: Итерируется по страницам категорий, передавая URL товаров для дальнейшей обработки.

Модуль также включает логирование для отслеживания процесса сбора данных и обработки ошибок.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category (s: Supplier) -> list[str, str, None]:
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
        s - Supplier
    @returns
        list or one of products urls or None
    """
```

**Назначение**: Получает список URL товаров со страницы категории. Если необходимо, пролистывает страницы категорий.

**Параметры**:

*   `s` (Supplier): Объект поставщика, содержащий информацию о текущем сценарии, локаторы элементов и драйвер веб-браузера.

**Возвращает**:

*   `list[str, str, None]`: Список URL товаров или `None`, если список товаров не найден.

**Как работает функция**:

1.  **Инициализация**:
    *   Получает драйвер (`d`) и локаторы (`l`) из объекта поставщика (`s`).
    *   Ожидает 1 секунду для загрузки элементов на странице.
    *   Закрывает всплывающее окно, если оно есть.
    *   Прокручивает страницу вниз.
2.  **Извлечение ссылок на товары**:
    *   Извлекает список ссылок на товары с использованием локатора `l['product_links']`.
3.  **Обработка отсутствия ссылок**:
    *   Если ссылки на товары не найдены, регистрирует предупреждение в лог и возвращает `None`.
4.  **Пагинация**:
    *   Если текущий URL отличается от предыдущего, пытается выполнить пагинацию, вызывая функцию `paginator`.
    *   Добавляет новые ссылки на товары в общий список.
5.  **Формирование списка**:
    *   Преобразует список товаров в список, если он является строкой.
6.  **Логирование**:
    *   Регистрирует количество найденных товаров в категории.
7.  **Возврат результата**:
    *   Возвращает список URL товаров.

**Внутренние функции**:

*   Внутри этой функции вызывается функция `paginator`. Она будет рассмотрена отдельно

**ASCII Flowchart**:

```
    Supplier (s)
    │
    ├───► Driver (d), Locators (l)
    │
    ├───► Ожидание загрузки страницы
    │
    ├───► Закрытие баннера (если есть)
    │
    ├───► Прокрутка страницы
    │
    ├───► Извлечение ссылок на товары
    │
    ├───► Проверка наличия ссылок
    │   └───► Если нет, логирование и выход
    │
    ├───► Пагинация (если необходимо)
    │
    ├───► Формирование списка ссылок на товары
    │
    └───► Логирование количества товаров и возврат списка
```

**Примеры**:

```python
# Пример вызова функции
from src.suppliers import Supplier  # Предполагается, что класс Supplier определен в этом модуле
from src.webdriver.driver import Driver, Firefox
from typing import Dict

# Создание фиктивного объекта Supplier для примера
class MockSupplier(Supplier):
    def __init__(self, driver, locators, current_scenario):
        self.driver = driver
        self.locators = locators
        self.current_scenario = current_scenario

# Создание инстанса драйвера (пример с Firefox)
driver = Driver(Firefox)

# Пример локаторов
locators: Dict = {
    'category': {
        'product_links': {
            'by': 'CSS_SELECTOR',
            'selector': '.product-item a',
        },
        'pagination': {
            '<-': {
                'by': 'CSS_SELECTOR',
                'selector': '.pagination a.next',
            }
        }
    },
    'product': {
        'close_banner': {
            'by': 'CSS_SELECTOR',
            'selector': '.close-banner',
            'mandatory': False
        }
    }
}
# Пример текущего сценария
current_scenario = {'name': 'example_category'}

# Создание инстанса MockSupplier
supplier = MockSupplier(driver, locators, current_scenario)

# Вызов функции
product_urls = get_list_products_in_category(supplier)

if product_urls:
    print(f"Found {len(product_urls)} product URLs")
else:
    print("No product URLs found")
```

### `paginator`

```python
def paginator(d:Driver, locator: dict, list_products_in_category: list):
    """ Листалка """
    response = d.execute_locator(locator['pagination']['<-'])
    if not response or (isinstance(response, list) and len(response) == 0): 
        ...
        return
    return True
```

**Назначение**: Осуществляет пагинацию на странице категории.

**Параметры**:

*   `d` (Driver): Объект драйвера веб-браузера.
*   `locator` (dict): Словарь с локаторами элементов страницы.
*   `list_products_in_category` (list): Текущий список URL товаров в категории.

**Возвращает**:

*   `True`: Если пагинация прошла успешно.
*   `None`: Если пагинация не удалась.

**Как работает функция**:

1.  **Извлечение следующей страницы**:
    *   Пытается извлечь элемент следующей страницы с использованием локатора `locator['pagination']['<-']`.
2.  **Проверка результата**:
    *   Если элемент не найден или является пустым списком, возвращает `None`.
3.  **Возврат `True`**:
    *   Если пагинация прошла успешно, возвращает `True`.

**ASCII Flowchart**:

```
    Driver (d), Locator (locator)
    │
    ├───► Попытка извлечения элемента следующей страницы
    │
    ├───► Проверка результата
    │   └───► Если не найден, выход
    │
    └───► Возврат True
```

**Примеры**:

```python
# Пример вызова функции
from src.webdriver.driver import Driver, Firefox
from typing import Dict

# Создание инстанса драйвера (пример с Firefox)
driver = Driver(Firefox)

# Пример локаторов
locator: Dict = {
    'pagination': {
        '<-': {
            'by': 'CSS_SELECTOR',
            'selector': '.pagination a.next',
        }
    }
}

# Пример списка товаров в категории
list_products_in_category: list = ['https://example.com/product1', 'https://example.com/product2']

# Вызов функции
result = paginator(driver, locator, list_products_in_category)

if result:
    print("Pagination successful")
else:
    print("Pagination failed")
```

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(s):
    """ сборщик актуальных категорий с сайта """
    ...
```

**Назначение**: Собирает актуальные категории с сайта.
**Параметры**:
*   `s`:  Параметр не документирован.

**Возвращает**:
*   Возвращаемое значение не документировано

**Как работает функция**:
1.  Функция выполняет неопределенную операцию по сбору актуальных категорий с сайта. Подробности реализации скрыты.

**ASCII Flowchart**:

```
    S (Параметр не документирован)
    │
    └───►  сборщик актуальных категорий с сайта
```

**Примеры**:
```python
# TODO: Добавить пример использования функции.