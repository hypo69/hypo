# Модуль для работы с AliExpress

## Обзор

Модуль предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с AliExpress. Он объединяет возможности работы через веб-драйвер и прямые HTTP-запросы, а также предоставляет API для выполнения специфичных действий, таких как поиск товаров.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress.

**Наследует**:
- `Supplier`: Предоставляет общую функциональность для работы с поставщиками.
- `AliRequests`: Отвечает за выполнение HTTP-запросов к AliExpress.
- `AliApi`: Предоставляет API для взаимодействия с AliExpress.

**Принцип работы**:
Класс `Aliexpress` объединяет функциональность трех базовых классов (`Supplier`, `AliRequests`, `AliApi`) для обеспечения комплексного взаимодействия с платформой AliExpress. Он позволяет выполнять запросы к API, управлять сессиями и использовать веб-драйвер для автоматизации действий на сайте.

**Методы**:
- `__init__`: Инициализирует класс `Aliexpress`.

#### `__init__`

```python
def __init__(self, 
             webdriver: bool | str = False, 
             locale: str | dict = {'EN': 'USD'},
             *args, **kwargs):
    """
    Initialize the Aliexpress class.

    :param webdriver: Webdriver mode. Supported values are:
        - `False` (default): No webdriver.
        - `'chrome'`: Use the Chrome webdriver.
        - `'mozilla'`: Use the Mozilla webdriver.
        - `'edge'`: Use the Edge webdriver.
        - `'default'`: Use the system's default webdriver.
    :type webdriver: bool | str

    :param locale: The language and currency settings for the script.
    :type locale: str | dict

    :param args: Additional positional arguments.
    :param kwargs: Additional keyword arguments.

    **Examples**:

    .. code-block:: python

        # Run without a webdriver
        a = Aliexpress()

        # Webdriver `Chrome`
        a = Aliexpress('chrome')

    """
    ...
    super().__init__(supplier_prefix = 'aliexpress', 
                     locale = locale, 
                     webdriver = webdriver, 
                     *args, **kwargs)
```

**Назначение**: Инициализирует экземпляр класса `Aliexpress`.

**Параметры**:
- `webdriver` (bool | str, optional): Определяет режим работы с использованием веб-драйвера. Допустимые значения:
  - `False` (по умолчанию): Без веб-драйвера.
  - `'chrome'`: Использовать Chrome webdriver.
  - `'mozilla'`: Использовать Mozilla webdriver.
  - `'edge'`: Использовать Edge webdriver.
  - `'default'`: Использовать системный веб-драйвер по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты для скрипта. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Как работает функция**:

1.  Инициализация класса `Aliexpress`:
    *   Принимает аргументы, определяющие режим работы (с веб-драйвером или без), локаль и другие параметры.
2.  Вызов конструктора родительского класса `Supplier`:
    *   Инициализирует общие параметры поставщика, такие как префикс (`aliexpress`), локаль и режим веб-драйвера.

```
Инициализация класса Aliexpress (webdriver, locale, *args, **kwargs)
↓
Вызов __init__ родительского класса Supplier (supplier_prefix, locale, webdriver, *args, **kwargs)
```

**Примеры**:

```python
# Запуск без веб-драйвера
a = Aliexpress()

# Запуск с Chrome webdriver
a = Aliexpress('chrome')