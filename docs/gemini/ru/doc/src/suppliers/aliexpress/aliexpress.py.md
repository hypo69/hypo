# Модуль для работы с AliExpress
## Обзор

Модуль `aliexpress.py` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress.

## Подробнее

Этот модуль предназначен для упрощения взаимодействия с AliExpress. Он позволяет выполнять запросы к AliExpress, используя как webdriver, так и requests, а также предоставляет API для работы с данными AliExpress. Расположен в директории `src/suppliers/aliexpress/`.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для AliExpress.

**Методы**:
- `__init__`: Инициализирует класс `Aliexpress`.

**Параметры**:
- `webdriver` (bool | str): Режим веб-драйвера. Поддерживаемые значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать веб-драйвер Chrome.
    - `'mozilla'`: Использовать веб-драйвер Mozilla.
    - `'edge'`: Использовать веб-драйвер Edge.
    - `'default'`: Использовать системный веб-драйвер по умолчанию.
- `locale` (str | dict): Настройки языка и валюты для скрипта.
- `args`: Дополнительные позиционные аргументы.
- `kwargs`: Дополнительные именованные аргументы.

**Примеры**:

- Запуск без веб-драйвера:

```python
a = Aliexpress()
```

- Webdriver `Chrome`:

```python
a = Aliexpress('chrome')
```

## Функции

### `__init__`

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

**Описание**: Инициализирует класс `Aliexpress`.

**Параметры**:
- `webdriver` (bool | str): Режим веб-драйвера. Поддерживаемые значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать веб-драйвер Chrome.
    - `'mozilla'`: Использовать веб-драйвер Mozilla.
    - `'edge'`: Использовать веб-драйвер Edge.
    - `'default'`: Использовать системный веб-драйвер по умолчанию.
- `locale` (str | dict): Настройки языка и валюты для скрипта.
- `args`: Дополнительные позиционные аргументы.
- `kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')
```