# Модуль Aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который интегрирует функциональность из классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он предназначен для выполнения задач, связанных с парсингом и взаимодействием с API AliExpress.

## Подробней

Модуль является частью проекта `hypotez` и предназначен для интеграции с платформой AliExpress. Он объединяет классы `Supplier`, `AliRequests` и `AliApi`, чтобы обеспечить удобный интерфейс для выполнения различных задач, таких как парсинг данных и взаимодействие с API AliExpress.

## Оглавление

- [Модуль Aliexpress](#модуль-aliexpress)
- [Обзор](#обзор)
- [Подробней](#подробней)
- [Классы](#классы)
  - [Aliexpress](#aliexpress)
    - [Метод `__init__`](#__init__)

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для удобного взаимодействия с AliExpress.

**Примеры использования**:

```python
# Запуск без вебдрайвера
a = Aliexpress()

# Вебдрайвер Chrome
a = Aliexpress('chrome')

# Режим Requests
a = Aliexpress(requests=True)
```

### Метод `__init__`

```python
def __init__(self, webdriver: bool | str = False, locale: Optional[str | dict] = {'EN': 'USD'}, *args, **kwargs):
    """
    Args:
        webdriver (bool | str, optional): Определяет режим использования вебдрайвера. Возможные значения:
            - `False` (по умолчанию): Без вебдрайвера.
            - `'chrome'`: Вебдрайвер Chrome.
            - `'mozilla'`: Вебдрайвер Mozilla.
            - `'edge'`: Вебдрайвер Edge.
            - `'default'`: Системный вебдрайвер по умолчанию.
        locale (str | dict, optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
        *args: Дополнительные позиционные аргументы.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        None

    Raises:
        Exception: Возможны исключения, связанные с инициализацией вебдрайвера или ошибки при взаимодействии с AliExpress.

    Example:
        >>> # Запуск без вебдрайвера
        >>> a = Aliexpress()
        >>> # Вебдрайвер Chrome
        >>> a = Aliexpress('chrome')
    """
```

**Описание**: Инициализирует класс `Aliexpress`.

**Параметры**:

- `webdriver` (bool | str, optional): Определяет режим использования вебдрайвера. Возможные значения:
  - `False` (по умолчанию): Без вебдрайвера.
  - `'chrome'`: Вебдрайвер Chrome.
  - `'mozilla'`: Вебдрайвер Mozilla.
  - `'edge'`: Вебдрайвер Edge.
  - `'default'`: Системный вебдрайвер по умолчанию.
- `locale` (Optional[str | dict], optional): Настройки языка и валюты. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:

- None

**Вызывает исключения**:

- Exception: Возможны исключения, связанные с инициализацией вебдрайвера или ошибки при взаимодействии с AliExpress.

**Примеры**:

```python
# Запуск без вебдрайвера
a = Aliexpress()

# Вебдрайвер Chrome
a = Aliexpress('chrome')
```
```