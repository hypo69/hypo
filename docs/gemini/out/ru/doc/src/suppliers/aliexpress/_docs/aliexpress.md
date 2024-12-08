# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который интегрирует функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Он предназначен для задач, связанных с парсингом и взаимодействием с API AliExpress.

## Содержание

- [Модуль aliexpress](#модуль-aliexpress)
- [Класс Aliexpress](#класс-aliexpress)
  - [Метод __init__](#метод-__init__)


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
    - `'default'`: WebDriver по умолчанию для системы.
- `locale` (str | dict, optional): Параметры языка и валюты. По умолчанию `{'EN': 'USD'}`.
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
- Не возвращает значение.

**Возможные исключения**:
- Возможные исключения, связанные с инициализацией WebDriver или ошибками при взаимодействии с AliExpress.


```python
from typing import Optional

class Aliexpress:
    """
    Базовый класс для работы с AliExpress.
    """
    def __init__(self, webdriver: Optional[str | bool] = False, locale: Optional[str | dict] = {'EN': 'USD'}, *args, **kwargs) -> None:
        """
        Args:
            webdriver (Optional[str | bool], optional): Режим использования WebDriver.
                                                          False - WebDriver не используется.
                                                          'chrome' - Chrome WebDriver.
                                                          'mozilla' - Mozilla WebDriver.
                                                          'edge' - Edge WebDriver.
                                                          'default' - WebDriver по умолчанию для системы.
                                                          Defaults to False.
            locale (Optional[str | dict], optional): Параметры языка и валюты. По умолчанию {'EN': 'USD'}.
            *args: Дополнительные позиционные аргументы.
            **kwargs: Дополнительные именованные аргументы.
        
        Returns:
            None
        
        Raises:
            Exception: Любые ошибки при инициализации.
        """
        pass