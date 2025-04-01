# Модуль `aliexpress`

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress.

## Подробней

Модуль предназначен для упрощения взаимодействия с AliExpress, объединяя в себе инструменты для выполнения запросов, работы с API и управления поставщиками. Он позволяет выполнять поиск, фильтрацию и получение информации о товарах на AliExpress.

## Классы

### `Aliexpress`

**Описание**:
Базовый класс для работы с AliExpress.

**Как работает класс**:
Класс `Aliexpress` наследует функциональность от классов `Supplier`, `AliRequests` и `AliApi`. Это позволяет ему выполнять задачи, связанные с отправкой запросов к AliExpress, обработкой ответов и управлением данными о поставщиках. Класс поддерживает работу как без веб-драйвера, так и с использованием веб-драйверов Chrome, Mozilla и Edge.

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

**Описание**:
Инициализирует экземпляр класса `Aliexpress`.

**Параметры**:
- `webdriver` (bool | str): Режим веб-драйвера. Возможные значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать веб-драйвер Chrome.
    - `'mozilla'`: Использовать веб-драйвер Mozilla.
    - `'edge'`: Использовать веб-драйвер Edge.
    - `'default'`: Использовать системный веб-драйвер по умолчанию.
- `locale` (str | dict): Настройки языка и валюты для скрипта. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Как работает функция**:
1. Инициализируется класс `Aliexpress` с указанными параметрами, такими как режим веб-драйвера и локаль.
2. Вызывается конструктор родительского класса `Supplier` с указанием префикса поставщика `'aliexpress'`, локали и режима веб-драйвера.
   A
   |
   -- B
   |
   C

   Где:
   - `A`: Инициализация класса `Aliexpress`.
   - `B`: Передача параметров в конструктор родительского класса.
   - `C`: Вызов конструктора `Supplier`.

**Примеры**:

```python
# Запуск без веб-драйвера
a = Aliexpress()

# Запуск с веб-драйвером Chrome
a = Aliexpress('chrome')