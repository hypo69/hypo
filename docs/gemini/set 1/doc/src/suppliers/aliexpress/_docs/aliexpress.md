# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который интегрирует функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Он предназначен для задач, связанных с парсингом и взаимодействием с API AliExpress.

## Содержание

- [Модуль aliexpress](#module-aliexpress)
- [Класс Aliexpress](#class-aliexpress)
  - [Метод `__init__`](#method-__init__)


## Класс Aliexpress

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для удобного взаимодействия с AliExpress.

**Примеры использования**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')

# Режим работы с requests
a = Aliexpress(requests=True)
```


### Метод `__init__`

**Описание**: Инициализирует класс `Aliexpress`.

**Параметры**:

- `webdriver` (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
    - `False` (по умолчанию): WebDriver не используется.
    - `'chrome'`: Chrome WebDriver.
    - `'mozilla'`: Mozilla WebDriver.
    - `'edge'`: Edge WebDriver.
    - `'default'`: WebDriver по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')
```

**Возвращает**:
- Не возвращает значения.

**Возможные исключения**:
- Возможны исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.


```python
class Aliexpress:
    """
    Args:
        webdriver (bool | str, optional): Determines the WebDriver usage mode. Possible values:
            - False (default): No WebDriver.
            - 'chrome': Chrome WebDriver.
            - 'mozilla': Mozilla WebDriver.
            - 'edge': Edge WebDriver.
            - 'default': Default system WebDriver.
        locale (str | dict, optional): Language and currency settings. Defaults to {'EN': 'USD'}.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        None: Does not return a value.

    Raises:
        WebDriverException: Exception during WebDriver initialization.
        ConnectionError: Problem connecting to AliExpress.
        APIError: API-specific error from AliExpress.
    """
    def __init__(self, webdriver=False, locale={'EN': 'USD'}, *args, **kwargs):
        # Обработка исключений
        try:
            # Логика инициализации WebDriver
            if webdriver:
                # ...
                pass

            # Логика инициализации locale
            if locale:
                # ...
                pass
            
            # Инициализация внутренних компонентов
            # ... (Supplier, AliRequests, AliApi)
        except Exception as ex:
            raise Exception(f"Ошибка инициализации: {ex}") from ex