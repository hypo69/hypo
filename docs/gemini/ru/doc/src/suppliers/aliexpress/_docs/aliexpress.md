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
Класс `Aliexpress` инициализирует экземпляры классов `Supplier`, `AliRequests` и `AliApi`, предоставляя удобный интерфейс для работы с AliExpress. В зависимости от переданных параметров, он может работать с использованием WebDriver или без него.

**Примеры использования**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')

# Режим запросов (requests)
a = Aliexpress(requests=True)
```

### Метод `__init__`

**Описание**: Инициализирует класс `Aliexpress`.

```python
def __init__(webdriver: bool | str = False, locale: str | dict = {'EN': 'USD'}, *args, **kwargs):
    """Инициализирует класс `Aliexpress`.

    Args:
        webdriver (bool | str, optional): Определяет режим использования WebDriver. Возможные значения:
            - `False` (по умолчанию): WebDriver не используется.
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
  - `False` (по умолчанию): WebDriver не используется.
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

**Как работает функция**:
1. **Инициализация**: Функция `__init__` принимает параметры, определяющие режим работы класса `Aliexpress`.
2. **Определение типа WebDriver**: В зависимости от значения параметра `webdriver`, функция определяет, какой WebDriver использовать (Chrome, Mozilla, Edge или системный по умолчанию) или не использовать WebDriver вообще.
3. **Конфигурация локали**: Функция устанавливает языковые и валютные настройки на основе параметра `locale`. Если параметр не указан, используются настройки по умолчанию (`{'EN': 'USD'}`).
4. **Инициализация компонентов**: Функция создает экземпляры классов `Supplier`, `AliRequests` и `AliApi`, передавая им необходимые параметры.
5. **Передача аргументов**: Функция передает дополнительные позиционные и именованные аргументы в компоненты `Supplier`, `AliRequests` и `AliApi`.

**ASCII flowchart**:

```
    Начало
    │
    ├── webdriver (bool | str)
    │   │
    │   ├── Определить тип WebDriver
    │   │   │
    │   │   ├── Chrome, Mozilla, Edge, Default -> Использовать указанный WebDriver
    │   │   │
    │   │   └── False -> Не использовать WebDriver
    │   │
    ├── locale (str | dict)
    │   │
    │   ├── Установить локаль
    │   │   │
    │   │   └── Если указан -> Использовать указанную локаль
    │   │   │
    │   │   └── Иначе -> Использовать локаль по умолчанию {'EN': 'USD'}
    │
    ├── Инициализация Supplier, AliRequests, AliApi
    │
    └── Передача *args и **kwargs в компоненты
    │
    Конец
```

**Примеры**:

```python
# Инициализация без WebDriver
a = Aliexpress()

# Chrome WebDriver
a = Aliexpress('chrome')

# Инициализация с указанием локали
a = Aliexpress(locale={'RU': 'RUB'})
```