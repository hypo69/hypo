# Модуль aliexpress

## Обзор

Модуль `aliexpress.py` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он упрощает взаимодействие с AliExpress, предлагая различные режимы работы, включая использование веб-драйвера и запросы напрямую.

## Подорбней

Этот модуль предназначен для интеграции с AliExpress, предоставляя инструменты для выполнения запросов, работы с API и управления сеансами. Он позволяет автоматизировать задачи, такие как сбор данных о продуктах, выполнение заказов и другие операции, связанные с AliExpress.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress.

**Как работает класс**:
Класс `Aliexpress` наследуется от классов `Supplier`, `AliRequests` и `AliApi`, объединяя их функциональность для обеспечения удобного взаимодействия с AliExpress. Он позволяет настраивать различные параметры, такие как использование веб-драйвера, локаль и другие параметры, необходимые для работы с AliExpress.

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
```

**Описание**: Инициализирует класс `Aliexpress`.

**Как работает функция**:
Функция `__init__` инициализирует класс `Aliexpress`, настраивая параметры веб-драйвера и локали. Она также вызывает конструктор суперкласса `Supplier` с указанием префикса поставщика и переданными параметрами.
Если `webdriver` имеет значение `False` (по умолчанию), веб-драйвер не используется. Если указано конкретное значение (например, `'chrome'`), используется соответствующий веб-драйвер.
Параметр `locale` определяет язык и валюту, используемые при взаимодействии с AliExpress.
`*args` и `**kwargs` позволяют передавать дополнительные позиционные и ключевые аргументы в конструктор суперкласса.

**Параметры**:
- `webdriver` (bool | str): Режим веб-драйвера. Поддерживаемые значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать веб-драйвер Chrome.
    - `'mozilla'`: Использовать веб-драйвер Mozilla.
    - `'edge'`: Использовать веб-драйвер Edge.
    - `'default'`: Использовать веб-драйвер, установленный в системе по умолчанию.
- `locale` (str | dict): Настройки языка и валюты для скрипта. По умолчанию `{'EN': 'USD'}`.
- `args`: Дополнительные позиционные аргументы.
- `kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
# Запуск без веб-драйвера
a = Aliexpress()

# Веб-драйвер Chrome
a = Aliexpress('chrome')
```
```python
super().__init__(supplier_prefix = 'aliexpress', 
                         locale = locale, 
                         webdriver = webdriver, 
                         *args, **kwargs)
```
```python
"""
.. module:: src.suppliers.aliexpress 
	:platform: Windows, Unix
	:synopsis: module provides the `Aliexpress` class, which integrates functionality
from `Supplier`, `AliRequests`, and `AliApi` for working with AliExpress.

"""