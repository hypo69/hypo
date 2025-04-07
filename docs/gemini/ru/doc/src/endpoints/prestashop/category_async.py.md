# Модуль `category_async.py`

## Обзор

Модуль `category_async.py` предоставляет асинхронный класс `PrestaCategoryAsync` для управления категориями в PrestaShop. Он включает функциональность для получения списка родительских категорий в асинхронном режиме.

## Подробнее

Этот модуль предназначен для асинхронного взаимодействия с API PrestaShop, обеспечивая возможность получения информации о категориях. Класс `PrestaCategoryAsync` наследуется от `PrestaShopAsync` и использует асинхронные запросы для работы с категориями.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Наследует**:
- `PrestaShopAsync`: Асинхронный класс для взаимодействия с API PrestaShop.

**Атрибуты**:
- Отсутствуют, используются атрибуты родительского класса `PrestaShopAsync`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCategoryAsync`, проверяет наличие `api_domain` и `api_key`.
- `get_parent_categories_list_async`: Асинхронно получает список родительских категорий для заданной категории.

### `__init__`

```python
 def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
     """! Async class for managing categories in PrestaShop.
     Args:
         credentials (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace, содержащий учетные данные API. По умолчанию `None`.
         api_domain (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
         api_key (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

     Raises:
         ValueError: Если `api_domain` или `api_key` не предоставлены.
     """
     ...
```

**Назначение**: Инициализирует экземпляр класса `PrestaCategoryAsync`.

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или `SimpleNamespace`, содержащий учетные данные API. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены.

**Как работает функция**:

1. Извлекает `api_domain` и `api_key` из `credentials`, если они предоставлены.
2. Проверяет, что `api_domain` и `api_key` заданы. Если нет, вызывает исключение `ValueError`.
3. Инициализирует родительский класс `PrestaShopAsync` с `api_domain` и `api_key`.

```
    A -- Проверка наличия credentials
    |
    B -- Извлечение api_domain и api_key из credentials (если есть)
    |
    C -- Проверка наличия api_domain и api_key
    |
    D -- Инициализация родительского класса PrestaShopAsync
```

**Примеры**:

```python
# Пример инициализации с использованием credentials
credentials = {'api_domain': 'example.com', 'api_key': 'test_key'}
category_manager = PrestaCategoryAsync(credentials=credentials)

# Пример инициализации с использованием отдельных параметров
category_manager = PrestaCategoryAsync(api_domain='example.com', api_key='test_key')
```

### `get_parent_categories_list_async`

```python
 async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
     """! Asynchronously retrieve parent categories for a given category."""
     Args:
         id_category (int | str): Идентификатор категории, для которой нужно получить родительские категории.
         additional_categories_list (Optional[List[int] | int], optional): Список дополнительных категорий для включения. По умолчанию `[]`.

     Returns:
         List[int]: Список идентификаторов родительских категорий.

     Raises:
         Exception: Если возникает ошибка при чтении категорий.
     """
     ...
```

**Назначение**: Асинхронно получает список родительских категорий для заданной категории.

**Параметры**:
- `id_category` (int | str): Идентификатор категории, для которой нужно получить родительские категории.
- `additional_categories_list` (Optional[List[int]  | int], optional): Список дополнительных категорий для включения. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список идентификаторов родительских категорий.

**Как работает функция**:

1. Преобразует `id_category` в целое число.
2. Преобразует `additional_categories_list` в список, если это не список. Добавляет `id_category` в `additional_categories_list`.
3. Итерируется по списку категорий `additional_categories_list`.
4. Для каждой категории пытается получить информацию о родительской категории с помощью `super().read`.
5. Если родительская категория <= 2, возвращает накопленный список `out_categories_list`.
6. Добавляет полученную родительскую категорию в `out_categories_list`.

```
    A -- Преобразование id_category в int
    |
    B -- Преобразование additional_categories_list в list и добавление id_category
    |
    C -- Итерация по additional_categories_list
    |
    D -- Получение информации о родительской категории с помощью super().read
    |
    E -- Проверка parent <= 2
    |
    F -- Добавление родительской категории в out_categories_list
```

**Примеры**:

```python
# Пример вызова функции
import asyncio
async def main():
    category_manager = PrestaCategoryAsync(api_domain='example.com', api_key='test_key')
    parent_categories = await category_manager.get_parent_categories_list_async(id_category=5, additional_categories_list=[6, 7])
    print(parent_categories)

asyncio.run(main())
```

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

**Назначение**:
- Функция, предназначенная для демонстрации или тестирования асинхронного кода. В текущей версии она содержит только `...`, что означает отсутствие конкретной реализации.

**Как работает функция**:
- В текущем виде функция не выполняет никаких действий, так как содержит только `...`.

## Главный блок `if __name__ == '__main__'`

В главном блоке вызывается функция `main()`, что позволяет выполнять асинхронный код при запуске скрипта.
```python
if __name__ == '__main__':
    main()
```