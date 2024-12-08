# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который интегрирует функциональность из классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он позволяет взаимодействовать с платформой, используя различные режимы, включая работу с веб-драйвером (Chrome, Mozilla, Edge, default) и запросы через `requests`.


## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress. Поддерживает различные режимы работы (с веб-драйвером или с использованием `requests`).

**Атрибуты**:

* `supplier_prefix`: Префикс для поставщика.

**Методы**:

* `__init__`: Инициализирует класс `Aliexpress`.

#### `__init__`

**Описание**: Инициализирует класс `Aliexpress`.

**Параметры**:

- `webdriver` (bool | str, optional): Режим работы с веб-драйвером. Возможные значения:
    - `False` (по умолчанию): Работа без веб-драйвера.
    - `'chrome'`: Использование веб-драйвера Chrome.
    - `'mozilla'`: Использование веб-драйвера Mozilla.
    - `'edge'`: Использование веб-драйвера Edge.
    - `'default'`: Использование системного веб-драйвера по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты для скрипта.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
# Работа без веб-драйвера
a = Aliexpress()

# Работа с веб-драйвером Chrome
a = Aliexpress('chrome')
```


**Возвращает**:

- Ничего не возвращает.

**Наследуется от**: `Supplier`, `AliRequests`, `AliApi`


## Функции

(Нет функций в данном файле)