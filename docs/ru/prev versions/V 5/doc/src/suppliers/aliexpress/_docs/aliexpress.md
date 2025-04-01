# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Он предназначен для задач, связанных с парсингом и взаимодействием с API AliExpress.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для упрощения взаимодействия с платформой AliExpress. Он предоставляет удобный интерфейс для выполнения различных операций, таких как поиск товаров, получение информации о товарах и выполнение других задач, связанных с AliExpress. Класс `Aliexpress` объединяет в себе функциональность нескольких классов, что упрощает его использование и повышает гибкость.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для удобного взаимодействия с AliExpress.

**Как работает класс**:
Класс `Aliexpress` инициализирует экземпляры классов `Supplier`, `AliRequests` и `AliApi`, предоставляя единую точку доступа к их функциональности. Он также позволяет настроить параметры, такие как использование WebDriver и локаль, для управления поведением при взаимодействии с AliExpress.

**Методы**:
- `__init__`: Инициализирует класс `Aliexpress`.

#### `__init__`

```python
def __init__(
    self,
    webdriver: bool | str = False,
    locale: str | dict = {'EN': 'USD'},
    *args,
    **kwargs,
) -> None:
    """
    Args:
        webdriver (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
            - `False` (по умолчанию): Без WebDriver.
            - `'chrome'`: Chrome WebDriver.
            - `'mozilla'`: Mozilla WebDriver.
            - `'edge'`: Edge WebDriver.
            - `'default'`: Системный WebDriver по умолчанию.
        locale (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
        *args: Дополнительные позиционные аргументы.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.

    Example:
        >>> a = Aliexpress()  # Инициализация без WebDriver
        >>> b = Aliexpress('chrome')  # Инициализация с Chrome WebDriver
    """
```

**Описание**: Инициализирует класс `Aliexpress`.

**Как работает функция**:
Метод `__init__` принимает параметры для настройки работы класса, такие как использование WebDriver и локаль. Он также инициализирует экземпляры классов `Supplier`, `AliRequests` и `AliApi`, передавая им дополнительные аргументы `*args` и `**kwargs`.

**Параметры**:
- `webdriver` (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
    - `False` (по умолчанию): Без WebDriver.
    - `'chrome'`: Chrome WebDriver.
    - `'mozilla'`: Mozilla WebDriver.
    - `'edge'`: Edge WebDriver.
    - `'default'`: Системный WebDriver по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- Ничего не возвращает.

**Вызывает исключения**:
- Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.

**Примеры**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Инициализация с Chrome WebDriver
b = Aliexpress('chrome')
```