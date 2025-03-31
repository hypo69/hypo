# Модуль для работы с поставщиками PrestaShop

## Обзор

Модуль `src.endpoints.prestashop.supplier` предоставляет класс `PrestaSupplier` для взаимодействия с API PrestaShop с целью управления информацией о поставщиках. Он наследуется от класса `PrestaShop` и предоставляет функциональность для инициализации и настройки соединения с API PrestaShop.

## Подробней

Этот модуль предназначен для упрощения работы с поставщиками в PrestaShop. Он позволяет инициализировать подключение к API PrestaShop, используя домен API и ключ API, которые могут быть переданы как отдельные параметры или как часть словаря с учетными данными.

## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` предназначен для работы с поставщиками PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop.

**Как работает класс**:

1.  При инициализации класса происходит проверка наличия необходимых параметров для подключения к API PrestaShop (домен и ключ API).
2.  Если параметры переданы через словарь `credentials`, они извлекаются из него.
3.  Если параметры не переданы или отсутствуют, вызывается исключение `ValueError`.
4.  Вызывается конструктор родительского класса `PrestaShop` для инициализации соединения с API.

**Методы**:

*   `__init__`: Инициализация экземпляра класса `PrestaSupplier`.

    **Параметры**:

    *   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
    *   `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
    *   `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

    **Возвращает**:

    *   None

    **Вызывает исключения**:

    *   `ValueError`: Если не переданы `api_domain` или `api_key`.

    **Примеры**:

    ```python
    from types import SimpleNamespace
    # Пример 1: Инициализация с использованием отдельных параметров
    supplier = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')

    # Пример 2: Инициализация с использованием словаря credentials
    credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
    supplier = PrestaSupplier(credentials=credentials)

    # Пример 3: Инициализация с использованием SimpleNamespace
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    supplier = PrestaSupplier(credentials=credentials)
    ```