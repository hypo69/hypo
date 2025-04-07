# Модуль для тестирования сценариев Aliexpress

## Обзор

Модуль `test_aliexpress_scenario.py` предназначен для тестирования сценариев работы с поставщиком Aliexpress. Он содержит функции для инициализации поставщика, продукта и выполнения различных действий, связанных с добавлением товаров в PrestaShop.

## Подробней

Этот модуль предоставляет инструменты для автоматизации тестирования взаимодействия с Aliexpress, включая создание экземпляров поставщика и продукта, получение информации о товарах и добавление их в базу данных PrestaShop. Он использует классы `Supplier` и `Product` из проекта `hypotez`, а также модуль `logger` для логирования.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Инициализирует и возвращает объект поставщика (Supplier) с заданным префиксом.

    Args:
        supplier_prefix (str): Префикс поставщика, используемый для инициализации.

    Returns:
        Supplier: Объект поставщика (Supplier) с заданными параметрами.

    Как работает функция:
    1. Создается словарь `params` с префиксом поставщика.
    2. Возвращается экземпляр класса `Supplier`, инициализированный с использованием словаря `params`.

    ASCII flowchart:
    params = {'supplier_prefix': supplier_prefix}
    ↓
    return Supplier(**params)
    """
    params: dict = {
        'supplier_prefix': supplier_prefix
    }
    return Supplier(**params)
```

**Параметры:**

-   `supplier_prefix` (str): Префикс поставщика.

**Возвращает:**

-   `Supplier`: Объект поставщика (Supplier).

**Примеры:**

```python
supplier = start_supplier('aliexpress')
```

### `start_product`

```python
def start_product() -> Product:
    """
    Создает и возвращает экземпляр класса `Product`, используя параметры, необходимые для тестов.

    Args:
        Нет

    Returns:
        Product: Объект `Product`, инициализированный с параметрами поставщика, локаторами веб-элементов и категориями продукта.

    Как работает функция:
    1. Получает локаторы веб-элементов и категории продукта из тестового сценария.
    2. Создает словарь `params` с параметрами поставщика, локаторами и категориями.
    3. Возвращает экземпляр класса `Product`, инициализированный с использованием словаря `params`.

    ASCII flowchart:
    Получение локаторов и категорий из test_scenario
    ↓
    params = {'supplier': s, 'webelements_locators': s.locators.get('product'), 'product_categories': test_scenario['iPhone 13 & 13 MINI']['presta_categories']}
    ↓
    return Product(**params)
    """
    params: dict = {
        'supplier': s,
        'webelements_locators': s.locators.get('product'),
        'product_categories': test_scenario['iPhone 13 & 13 MINI']['presta_categories'],
        #'product_fields':product_fields,
    }
    return Product(**params)
```

**Параметры:**

-   Нет

**Возвращает:**

-   `Product`: Объект `Product`.

**Примеры:**

```python
product = start_product()
```

## Переменные

### `supplier_prefix`

```python
supplier_prefix = 'aliexpress'
```

-   **Описание**: Префикс поставщика, используемый в данном сценарии. В данном случае - 'aliexpress'.

### `s`

```python
s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """
```

-   **Описание**: Экземпляр класса `Supplier`, инициализированный с префиксом 'aliexpress'.

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

-   **Описание**: Словарь, содержащий информацию о тестовом сценарии для iPhone 13 & 13 MINI, включая ID категории на сайте, бренд, URL, активность, состояние, категории PrestaShop и комбинации продуктов.

### `test_products_list`

```python
test_products_list: list = ['https://s.click.aliexpress.com/e/_oFLpkfz',
                            'https://s.click.aliexpress.com/e/_oE5V3d9',
                            'https://s.click.aliexpress.com/e/_oDnvttN',
                            'https://s.click.aliexpress.com/e/_olWWQCP',
                            'https://s.click.aliexpress.com/e/_ok0xeMn']
```

-   **Описание**: Список URL-адресов тестовых продуктов.

### `p`

```python
p = start_product()
```

-   **Описание**: Экземпляр класса `Product`, инициализированный с использованием функции `start_product()`.

### `d`

```python
d = s.driver
```

-   **Описание**: Драйвер веб-браузера, полученный из экземпляра класса `Supplier`.

### `_`

```python
_ = d.execute_locator
```

-   **Описание**: Функция для выполнения локаторов веб-элементов с использованием драйвера.

### `f`

```python
f = p.fields
```

-   **Описание**: Поля продукта, полученные из экземпляра класса `Product`.

### `l`

```python
l = p.webelements_locators
```

-   **Описание**: Локаторы веб-элементов продукта, полученные из экземпляра класса `Product`.