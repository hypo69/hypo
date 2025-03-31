# Модуль `category_async`

## Обзор

Модуль `category_async` предназначен для асинхронного управления категориями в PrestaShop. Он предоставляет функциональность для получения списка родительских категорий для заданной категории. Модуль использует асинхронные запросы к API PrestaShop для повышения производительности.

## Подробней

Модуль `category_async` содержит класс `PrestaCategoryAsync`, который наследуется от `PrestaShopAsync`. Он инициализируется с использованием учетных данных API PrestaShop и предоставляет метод `get_parent_categories_list_async` для асинхронного получения родительских категорий. Этот модуль важен для работы с категориями в PrestaShop, особенно когда требуется асинхронное выполнение операций для оптимизации производительности.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Как работает класс**:
Класс `PrestaCategoryAsync` наследуется от `PrestaShopAsync` и предназначен для выполнения асинхронных операций с категориями в PrestaShop. При инициализации класса проверяется наличие `api_domain` и `api_key`, которые необходимы для взаимодействия с API PrestaShop. Класс предоставляет метод `get_parent_categories_list_async` для получения списка родительских категорий для заданной категории.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCategoryAsync`.
- `get_parent_categories_list_async`: Асинхронно получает список родительских категорий для заданной категории.

#### `__init__`

```python
def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
    """! Async class for managing categories in PrestaShop."""
    ...
```

**Назначение**: Инициализирует экземпляр класса `PrestaCategoryAsync`.

**Как работает функция**:
При инициализации проверяется наличие переданных учетных данных (`credentials`) или отдельных параметров `api_domain` и `api_key`. Если учетные данные переданы, они используются для установки значений `api_domain` и `api_key`. Если ни `api_domain`, ни `api_key` не предоставлены, вызывается исключение `ValueError`.

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или объект SimpleNamespace, содержащий учетные данные API. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key`.

#### `get_parent_categories_list_async`

```python
async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
    """! Asynchronously retrieve parent categories for a given category."""
    ...
```

**Назначение**: Асинхронно получает список родительских категорий для заданной категории.

**Как работает функция**:
Функция принимает идентификатор категории (`id_category`) и список дополнительных категорий (`additional_categories_list`). Она пытается преобразовать `id_category` в целое число и обрабатывает исключение, если это не удается. Затем она добавляет `id_category` в `additional_categories_list`, если его там нет. Для каждой категории в `additional_categories_list` функция выполняет асинхронный запрос к API PrestaShop для получения родительской категории. Если родительская категория меньше или равна 2, функция возвращает накопленный список родительских категорий.

**Параметры**:
- `id_category` (int | str): Идентификатор категории.
- `additional_categories_list` (Optional[List[int]  |  int], optional): Список дополнительных категорий. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список родительских категорий.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при получении родительской категории.

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

**Назначение**: Главная функция для демонстрации работы модуля.

**Как работает функция**:
Функция `main` предназначена для демонстрации работы модуля. В предоставленном коде она содержит только `...`, что означает, что её реализация не показана. В реальном сценарии она может включать создание экземпляра класса `PrestaCategoryAsync`, вызов метода `get_parent_categories_list_async` и вывод результатов.

## Примеры

Пример использования класса `PrestaCategoryAsync` и метода `get_parent_categories_list_async`:

```python
import asyncio
from types import SimpleNamespace
from src.endpoints.prestashop.category_async import PrestaCategoryAsync

async def main():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    category_id = 10  # Пример идентификатора категории
    parent_categories = await category_manager.get_parent_categories_list_async(category_id)
    print(f"Parent categories for category {category_id}: {parent_categories}")

if __name__ == '__main__':
    asyncio.run(main())
```