# Модуль `src.endpoints.prestashop.supplier`

## Обзор

Модуль `src.endpoints.prestashop.supplier` предназначен для работы с поставщиками в PrestaShop. Он содержит класс `PrestaSupplier`, который расширяет функциональность класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop для управления информацией о поставщиках.

## Подробней

Этот модуль предоставляет удобный интерфейс для выполнения операций, связанных с поставщиками, таких как получение списка поставщиков, добавление нового поставщика, обновление информации о существующем поставщике и удаление поставщика. Модуль использует API PrestaShop для взаимодействия с интернет-магазином. Для работы требуется указать домен API и ключ API PrestaShop.

## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` предназначен для работы с поставщиками PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для выполнения операций, связанных с поставщиками.

**Как работает класс**:
1.  При инициализации класса проверяются переданные параметры `api_domain` и `api_key`. Если они не указаны, выбрасывается исключение `ValueError`.
2.  Вызывается конструктор родительского класса `PrestaShop` с переданными параметрами.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `PrestaSupplier`.

    **Параметры**:
    -   `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
    -   `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
    -   `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.
    -   `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
    -   `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

    **Возвращает**:
    -   `None`

    **Вызывает исключения**:
    -   `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.

    **Пример**:

    ```python
    from types import SimpleNamespace

    # Инициализация с использованием словаря
    supplier = PrestaSupplier(credentials={'api_domain': 'example.com', 'api_key': 'test_key'})

    # Инициализация с использованием SimpleNamespace
    credentials = SimpleNamespace(api_domain='example.com', api_key='test_key')
    supplier = PrestaSupplier(credentials=credentials)

    # Инициализация с указанием параметров api_domain и api_key напрямую
    supplier = PrestaSupplier(api_domain='example.com', api_key='test_key')
    ```