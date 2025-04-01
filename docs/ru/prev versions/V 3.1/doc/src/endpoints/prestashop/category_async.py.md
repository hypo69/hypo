# Модуль `category_async`

## Обзор

Модуль `category_async` предоставляет асинхронный класс `PrestaCategoryAsync` для управления категориями в PrestaShop. Он позволяет асинхронно извлекать родительские категории для заданной категории, используя API PrestaShop.

## Подробней

Этот модуль предназначен для работы с категориями в PrestaShop с использованием асинхронного подхода. Класс `PrestaCategoryAsync` наследуется от `PrestaShopAsync` и предоставляет методы для получения информации о категориях, в частности, для получения списка родительских категорий. Он использует асинхронные запросы для повышения производительности при работе с API PrestaShop.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCategoryAsync`.
- `get_parent_categories_list_async`: Асинхронно извлекает родительские категории для заданной категории.

#### `__init__`

```python
    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        """
        Args:
            credentials (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными API. По умолчанию `None`.
            api_domain (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
            api_key (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

        Raises:
            ValueError: Если не указаны `api_domain` или `api_key`.

        Example:
            Примеры вызовов:
            >>> category_api = PrestaCategoryAsync(credentials={'api_domain': 'your_domain', 'api_key': 'your_key'})
            >>> category_api = PrestaCategoryAsync(api_domain='your_domain', api_key='your_key')
        """
        ...
```

**Описание**: Инициализирует экземпляр класса `PrestaCategoryAsync`.

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными API. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` или `api_key`.

#### `get_parent_categories_list_async`

```python
    async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
        """
        Args:
            id_category (int | str): Идентификатор категории, для которой нужно получить родительские категории.
            additional_categories_list (Optional[List[int] | int], optional): Список дополнительных категорий для поиска. По умолчанию [].

        Returns:
            List[int]: Список идентификаторов родительских категорий.

        Raises:
            Exception: Если возникает ошибка при чтении категории.

        Example:
            Примеры вызовов:
            >>> category_api = PrestaCategoryAsync(api_domain='your_domain', api_key='your_key')
            >>> asyncio.run(category_api.get_parent_categories_list_async(3))
            [2]
        """
        ...
```

**Описание**: Асинхронно извлекает родительские категории для заданной категории.

**Параметры**:
- `id_category` (int | str): Идентификатор категории, для которой нужно получить родительские категории.
- `additional_categories_list` (Optional[List[int] | int], optional): Список дополнительных категорий для поиска. По умолчанию [].

**Возвращает**:
- `List[int]`: Список идентификаторов родительских категорий.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении категории.

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

**Описание**: Функция, представляющая точку входа для асинхронной программы.

**Методы**:
- Нет

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

**Примеры**:
   Нет примеров

```python

if __name__ == '__main__':
    main()
```