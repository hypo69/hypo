# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который интегрирует функциональность из классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он обрабатывает различные режимы работы, включая использование веб-драйвера (например, Chrome) и работу с библиотекой `requests`.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Поддерживает различные режимы работы.

**Методы**:

- `__init__`: Инициализирует класс `Aliexpress`.

#### `__init__`

**Описание**: Инициализация класса.

**Параметры**:

- `webdriver` (bool | str, опционально): Режим работы с веб-драйвером. Доступные значения:
    - `False` (по умолчанию): Отсутствует веб-драйвер.
    - `'chrome'`: Используется веб-драйвер Chrome.
    - `'mozilla'`: Используется веб-драйвер Mozilla.
    - `'edge'`: Используется веб-драйвер Edge.
    - `'default'`: Используется системный веб-драйвер по умолчанию.
- `locale` (str | dict, опционально): Настройки языка и валюты для скрипта. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- Без возвращаемого значения.

**Примечания**: Вызывает конструктор базового класса `Supplier`.
```
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
    super().__init__(supplier_prefix='aliexpress',
                     locale=locale,
                     webdriver=webdriver,
                     *args, **kwargs)
```


```
## Функции

Не содержит функций.

## Модули

- `header`:
- `pickle`:
- `requests`:
- `threading`:
- `fake_useragent`:
- `pathlib`:
- `typing`:
- `requests.cookies`:
- `urllib.parse`:
- `gs`:
- `src.suppliers.supplier`:
- `.alirequests`:
- `.aliapi`:
- `src.logger`:


## Константы

- `MODE`: Значение константы `MODE`.