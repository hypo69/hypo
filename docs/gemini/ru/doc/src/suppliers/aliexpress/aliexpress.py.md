# Модуль `aliexpress.py`

## Обзор

Модуль `aliexpress.py` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для взаимодействия с AliExpress.

## Оглавление

- [Класс `Aliexpress`](#класс-aliexpress)
    - [Метод `__init__`](#__init__)

## Классы

### `Aliexpress`

**Описание**:
Базовый класс для работы с AliExpress. Этот класс объединяет возможности классов `Supplier`, `AliRequests` и `AliApi` для упрощения взаимодействия с AliExpress.

**Примеры использования**:

```python
# Запуск без веб-драйвера
a = Aliexpress()

# Веб-драйвер `Chrome`
a = Aliexpress('chrome')

# Режим запросов
a = Aliexpress(requests=True)
```

#### `__init__`

**Описание**:
Инициализирует класс `Aliexpress`.

**Параметры**:
- `webdriver` (bool | str, optional): Режим веб-драйвера. Поддерживаемые значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать веб-драйвер Chrome.
    - `'mozilla'`: Использовать веб-драйвер Mozilla.
    - `'edge'`: Использовать веб-драйвер Edge.
    - `'default'`: Использовать веб-драйвер по умолчанию в системе.
- `locale` (str | dict, optional): Настройки языка и валюты для скрипта. По умолчанию `{'EN': 'USD'}`.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
# Запуск без веб-драйвера
a = Aliexpress()

# Веб-драйвер `Chrome`
a = Aliexpress('chrome')
```