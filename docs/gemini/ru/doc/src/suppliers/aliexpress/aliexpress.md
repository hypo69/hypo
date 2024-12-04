# Модуль `aliexpress`

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, интегрирующий функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он позволяет осуществлять запросы к API AliExpress и взаимодействовать с сайтом через веб-драйверы.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress. Объединяет функциональность `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress.  Поддерживает работу с веб-драйверами (Chrome, Mozilla, Edge) и без них.

**Методы**:

- `__init__`: Инициализирует экземпляр класса.

**Подробное описание методов:**

#### `__init__`

**Описание**: Инициализирует экземпляр класса `Aliexpress`.

**Параметры**:

- `webdriver` (bool | str, optional): Режим работы с веб-драйвером. Доступные значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использование веб-драйвера Chrome.
    - `'mozilla'`: Использование веб-драйвера Mozilla.
    - `'edge'`: Использование веб-драйвера Edge.
    - `'default'`: Использование системного веб-драйвера по умолчанию.
- `locale` (str | dict, optional): Настройки языка и валюты. По умолчанию: `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.


**Возвращает**:

- Ничего не возвращает.


**Примеры использования**:

```python
# Run without a webdriver
a = Aliexpress()

# Webdriver Chrome
a = Aliexpress('chrome')
```

## Функции

(Список функций отсутствует в предоставленном коде)


## Модули

- `header`
- `pickle`
- `requests`
- `threading`
- `requests.sessions`
- `fake_useragent`
- `pathlib`
- `typing`
- `requests.cookies`
- `urllib.parse`
- `src.gs`
- `src.suppliers.supplier`
- `src.suppliers.aliexpress.alirequests`
- `src.suppliers.aliexpress.aliapi`
- `src.logger`


## Описание переменных

- `MODE`: Строковая переменная, хранящая режим работы (например, 'dev').


```