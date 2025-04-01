# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Он предназначен для задач, связанных с парсингом и взаимодействием с API AliExpress.

## Содержание

- [Модуль aliexpress](#модуль-aliexpress)
- [Класс Aliexpress](#класс-aliexpress)
  - [Метод __init__](#метод-__init__)

## Класс Aliexpress

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для удобного взаимодействия с AliExpress.

**Принцип работы**:
Класс `Aliexpress` предназначен для упрощения работы с AliExpress, объединяя функциональность нескольких классов в одном. Он инициализирует необходимые компоненты, такие как `Supplier`, `AliRequests` и `AliApi`, и позволяет настраивать режим работы (например, использование веб-драйвера или API).

**Примеры использования**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')

# Режим запросов
a = Aliexpress(requests=True)
```

### Метод `__init__`

**Описание**: Инициализирует класс `Aliexpress`.

```python
def __init__(
    self,
    webdriver: bool | str = False,
    locale: str | dict = {'EN': 'USD'},
    *args,
    **kwargs
) -> None:
    """
    Инициализирует класс `Aliexpress`.

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
        None

    Raises:
        Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.
    """
    ...
```

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

**Как работает функция**:

1. **Определение типа WebDriver**: Функция определяет, какой WebDriver следует использовать, на основе значения параметра `webdriver`. Если указано `'chrome'`, `'mozilla'`, `'edge'` или `'default'`, используется соответствующий WebDriver. Если `webdriver` равен `False`, WebDriver не используется.
2. **Конфигурирование локали**: Функция устанавливает локаль на основе значения параметра `locale`. Если параметр предоставлен (строка или словарь), устанавливается указанная локаль. В противном случае используется локаль по умолчанию `{'EN': 'USD'}`.
3. **Инициализация внутренних компонентов**: Функция инициализирует экземпляры классов `Supplier`, `AliRequests` и `AliApi`. Это включает настройку соединений, инициализацию структур данных и конфигураций.
4. **Передача аргументов**: Функция передает `*args` и `**kwargs` внутренним компонентам (`Supplier`, `AliRequests`, `AliApi`).

**Примеры**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')
```

**Возвращает**:
- Не возвращает значение.

**Вызывает исключения**:
- Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.