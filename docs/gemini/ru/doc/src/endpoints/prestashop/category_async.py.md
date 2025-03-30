# Модуль `category_async`

## Обзор

Модуль `category_async` предоставляет асинхронтный класс `PrestaCategoryAsync` для управления категориями в PrestaShop. Он позволяет асинхронно извлекать родительские категории для заданной категории. Модуль использует `PrestaShopAsync` для взаимодействия с API PrestaShop и включает функциональность логирования ошибок.

## Подробней

Этот модуль предназначен для асинхронной работы с категориями в PrestaShop. Он позволяет извлекать список родительских категорий для заданной категории, используя асинхронные запросы к API PrestaShop. Это особенно полезно для задач, требующих высокой производительности и неблокирующих операций, таких как обновление структуры категорий или анализ дерева категорий.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCategoryAsync`.
- `get_parent_categories_list_async`: Асинхронно извлекает родительские категории для заданной категории.

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или пространство имен с учетными данными API (api_domain, api_key). По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Примеры**

```python
import asyncio
from types import SimpleNamespace
from src.endpoints.prestashop.category_async import PrestaCategoryAsync

async def main():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    
    category_id = 3  # ID категории, для которой нужно получить родительские категории
    parent_categories = await category_manager.get_parent_categories_list_async(category_id)
    
    print(f"Parent categories for category {category_id}: {parent_categories}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `get_parent_categories_list_async`

```python
async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
    """! Asynchronously retrieve parent categories for a given category."""
    ...
```

**Описание**: Асинхронно извлекает родительские категории для заданной категории.

**Параметры**:
- `id_category` (int | str): Идентификатор категории, для которой требуется получить список родительских категорий.
- `additional_categories_list` (Optional[List[int] | int], optional): Дополнительный список идентификаторов категорий. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список идентификаторов родительских категорий.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены при инициализации класса.

**Примеры**:

```python
import asyncio
from types import SimpleNamespace
from src.endpoints.prestashop.category_async import PrestaCategoryAsync

async def main():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    
    category_id = 3  # ID категории, для которой нужно получить родительские категории
    parent_categories = await category_manager.get_parent_categories_list_async(category_id)
    
    print(f"Parent categories for category {category_id}: {parent_categories}")

if __name__ == "__main__":
    asyncio.run(main())