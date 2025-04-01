# Документация модуля `test_aliexpress_scenario.py`

## Обзор

Модуль `test_aliexpress_scenario.py` предназначен для проведения экспериментов и тестирования сценариев работы с поставщиком AliExpress в рамках проекта `hypotez`. Он включает в себя функции для инициализации поставщика, настройки тестовых сценариев и создания экземпляров продуктов для тестирования.

## Подорбней

Модуль содержит функции для запуска поставщика (`start_supplier`), определения тестовых сценариев (`test_scenario`), списка тестовых продуктов (`test_products_list`) и создания экземпляра продукта (`start_product`). Он используется для тестирования интеграции с AliExpress и проверки корректности работы основных функций, таких как извлечение данных о продуктах и добавление их в PrestaShop.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Инициализирует и возвращает объект поставщика на основе переданного префикса.

    Args:
        supplier_prefix (str): Префикс поставщика, например 'aliexpress'.

    Returns:
        Supplier: Объект поставщика с заданным префиксом.
    """
```

**Как работает функция**:

1.  Функция принимает префикс поставщика в качестве аргумента.
2.  Создает словарь `params`, содержащий префикс поставщика.
3.  Инициализирует объект `Supplier` с использованием словаря `params`.
4.  Возвращает созданный объект `Supplier`.

**Примеры**:

```python
supplier_prefix = 'aliexpress'
s = start_supplier(supplier_prefix)
```

### `start_product`

```python
def start_product() -> Product:
    """
    Инициализирует и возвращает объект продукта с заданными параметрами, включая информацию о поставщике,
    локаторах веб-элементов и категориях продукта.

    Args:
        Нет аргументов.

    Returns:
        Product: Объект продукта с заданными параметрами.
    """
```

**Как работает функция**:

1.  Создает словарь `params`, содержащий информацию о поставщике (`s`), локаторах веб-элементов (`s.locators.get('product')`) и категориях продукта (`test_scenario['iPhone 13 & 13 MINI']['presta_categories']`).
2.  Инициализирует объект `Product` с использованием словаря `params`.
3.  Возвращает созданный объект `Product`.

**Примеры**:

```python
p = start_product()
```

## Переменные

### `supplier_prefix`

```python
supplier_prefix = 'aliexpress'
```

Описание:
- `supplier_prefix` (str): Префикс поставщика, используемый для инициализации объекта `Supplier`.

### `s`

```python
s = start_supplier(supplier_prefix)
```

Описание:
- `s` (Supplier): Объект поставщика, созданный с использованием функции `start_supplier`.
- На протяжении всего кода `s` означает класс `Supplier`.

### `test_scenario`

```python
test_scenario: dict = {
    "iPhone 13 & 13 MINI": {
        "category ID on site": 40000002781737,
        "brand": "APPLE",
        "url": "https://hi5group.aliexpress.com/store/group/iPhone-13-13-mini/1053035_40000002781737.html",
        "active": True,
        "condition": "new",
        "presta_categories": {
            "template": {
                "apple": "iPhone 13"
            }
        },
        "product combinations": [
            "bundle",
            "color"
        ]
    }
}
```

Описание:
- `test_scenario` (dict): Словарь, содержащий информацию о тестовом сценарии для продукта "iPhone 13 & 13 MINI", включая ID категории на сайте, бренд, URL, активность, состояние, категории PrestaShop и комбинации продуктов.

### `test_products_list`

```python
test_products_list: list = [
    'https://s.click.aliexpress.com/e/_oFLpkfz',
    'https://s.click.aliexpress.com/e/_oE5V3d9',
    'https://s.click.aliexpress.com/e/_oDnvttN',
    'https://s.click.aliexpress.com/e/_olWWQCP',
    'https://s.click.aliexpress.com/e/_ok0xeMn'
]
```

Описание:
- `test_products_list` (list): Список URL тестовых продуктов, используемых для тестирования извлечения данных о продуктах.

### `p`

```python
p = start_product()
```

Описание:
- `p` (Product): Объект продукта, созданный с использованием функции `start_product`.

### `d`

```python
d = s.driver
```

Описание:
- `d` (webdriver): Драйвер веб-браузера, полученный из объекта поставщика `s`.

### `_`

```python
_ = d.execute_locator
```

Описание:
- `_` (function): Функция для выполнения локаторов веб-элементов, полученная из драйвера `d`.

### `f`

```python
f = p.fields
```

Описание:
- `f` (fields): Поля продукта, полученные из объекта продукта `p`.

### `l`

```python
l = p.webelements_locators
```

Описание:
- `l` (webelements_locators): Локаторы веб-элементов продукта, полученные из объекта продукта `p`.