# Модуль Aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Он предназначен для задач, связанных с парсингом и взаимодействием с API AliExpress.

## Содержание

- [Модуль Aliexpress](#модуль-aliexpress)
- [Класс Aliexpress](#класс-aliexpress)
  - [Метод __init__](#метод-__init__)

## Класс Aliexpress

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для удобного взаимодействия с AliExpress.

**Принцип работы**:
Класс `Aliexpress` инициализирует экземпляры классов `Supplier`, `AliRequests` и `AliApi`, что позволяет выполнять запросы к AliExpress, обрабатывать полученные данные и взаимодействовать с API. В зависимости от переданных параметров, класс может использовать WebDriver для работы через браузер или отправлять запросы напрямую.

**Примеры использования**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Инициализация с Chrome WebDriver
a = Aliexpress('chrome')

# Инициализация в режиме запросов
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
    **kwargs,
) -> None:
    """
    Инициализирует класс `Aliexpress`.

    Args:
        webdriver (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
            - `False` (по умолчанию): WebDriver не используется.
            - `'chrome'`: Chrome WebDriver.
            - `'mozilla'`: Mozilla WebDriver.
            - `'edge'`: Edge WebDriver.
            - `'default'`: Используется системный WebDriver по умолчанию.
        locale (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
        *args: Дополнительные позиционные аргументы.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        None

    Raises:
        Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.
    """
```

**Параметры**:

- `webdriver` (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
  - `False` (по умолчанию): WebDriver не используется.
  - `'chrome'`: Chrome WebDriver.
  - `'mozilla'`: Mozilla WebDriver.
  - `'edge'`: Edge WebDriver.
  - `'default'`: Используется системный WebDriver по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.

**Как работает функция**:
1. **Инициализация**: Метод `__init__` инициализирует класс `Aliexpress` с заданными параметрами.
2. **Определение типа WebDriver**: В зависимости от значения параметра `webdriver`, определяется, будет ли использоваться WebDriver и какой именно.
3. **Конфигурирование локали**: Если параметр `locale` предоставлен (в виде строки или словаря), устанавливаются соответствующие настройки языка и валюты. В противном случае используется значение по умолчанию `{'EN': 'USD'}`.
4. **Инициализация внутренних компонентов**: Создаются экземпляры классов `Supplier`, `AliRequests` и `AliApi`. Это включает в себя настройку соединений, инициализацию структур данных и конфигураций.
5. **Назначение аргументов**: Аргументы `*args` и `**kwargs` передаются внутренним компонентам (`Supplier`, `AliRequests`, `AliApi`).

**ASCII flowchart**:

```
[Начало]
    ↓
[Проверка webdriver]
    ↓
[Конфигурация локали]
    ↓
[Инициализация Supplier]
    ↓
[Инициализация AliRequests]
    ↓
[Инициализация AliApi]
    ↓
[Назначение аргументов]
    ↓
[Конец]
```

**Примеры**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Инициализация с Chrome WebDriver
a = Aliexpress('chrome')

# Инициализация в режиме запросов
a = Aliexpress(requests=True)