# Модуль `category_async.py`

## Обзор

Модуль `category_async.py` предоставляет асинхронный класс `PrestaCategoryAsync` для управления категориями в PrestaShop. Он включает в себя функциональность для получения списка родительских категорий для заданной категории. Модуль использует асинхронные запросы для взаимодействия с API PrestaShop.

## Подробней

Этот модуль предназначен для асинхронного управления категориями в PrestaShop, что позволяет выполнять операции с категориями без блокировки основного потока выполнения. Класс `PrestaCategoryAsync` предоставляет методы для получения родительских категорий, используя API PrestaShop.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Наследует**: `PrestaShopAsync` - асинхронный класс для взаимодействия с API PrestaShop.

**Атрибуты**:
- Отсутствуют специфические атрибуты, кроме тех, что наследуются от `PrestaShopAsync`.

**Методы**:
- `__init__`: Конструктор класса, инициализирует объект с учетными данными API.
- `get_parent_categories_list_async`: Асинхронно получает список родительских категорий для заданной категории.

### `PrestaCategoryAsync.__init__`

```python
    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        """! Async class for managing categories in PrestaShop.

        Args:
            credentials (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными API (api_domain и api_key). По умолчанию `None`.
            api_domain (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
            api_key (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

        Raises:
            ValueError: Если `api_domain` или `api_key` не предоставлены.
        """
        ...
```

**Назначение**: Инициализирует объект `PrestaCategoryAsync` с учетными данными для доступа к API PrestaShop.

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или `SimpleNamespace`, содержащий `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены.

**Как работает класс**
1. Проверяет, были ли переданы учетные данные через параметр `credentials`. Если да, извлекает `api_domain` и `api_key` из него.
2. Если `api_domain` или `api_key` не были переданы ни через `credentials`, ни отдельными параметрами, вызывает исключение `ValueError`.
3. Вызывает конструктор суперкласса `PrestaShopAsync` с переданными `api_domain` и `api_key`.

**Примеры**:

```python
from types import SimpleNamespace

# Пример 1: Инициализация с использованием отдельных параметров
category_manager = PrestaCategoryAsync(api_domain='your_api_domain', api_key='your_api_key')

# Пример 2: Инициализация с использованием credentials
credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
category_manager = PrestaCategoryAsync(credentials=credentials)

# Пример 3: Инициализация с использованием SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
category_manager = PrestaCategoryAsync(credentials=credentials)
```

### `PrestaCategoryAsync.get_parent_categories_list_async`

```python
    async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
        """! Asynchronously retrieve parent categories for a given category."""
        try:
            id_category:int = id_category if isinstance(id_category, int) else int(id_category)
        except Exception as ex:
            logger.error(f"Недопустимый формат категории{id_category}", ex)

        additional_categories_list:list = additional_categories_list if isinstance(additional_categories_list, list) else [additional_categories_list]\
        additional_categories_list.append(id_category)

        out_categories_list:list = []

        for c in additional_categories_list:

            try:
                parent:int = await super().read('categories', resource_id=c, display='full', io_format='JSON')
            except Exception as ex:
                logger.error(f"Недопустимый формат категории", ex)
                continue            
                
            if parent <=2:
                return out_categories_list # Дошли до верха. Дерево категорий начинается с 2

            out_categories_list.append(parent)
```

**Назначение**: Асинхронно получает список родительских категорий для заданной категории.

**Параметры**:
- `id_category` (int | str): ID категории, для которой нужно получить родительские категории.
- `additional_categories_list` (Optional[List[int] | int], optional): Список дополнительных категорий для включения в поиск родительских категорий. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список ID родительских категорий.

**Как работает функция**:

1.  **Инициализация**:
    - Принимает `id_category` (ID категории для поиска родительских категорий) и `additional_categories_list` (список дополнительных категорий) в качестве аргументов.
    - Инициализирует пустой список `out_categories_list` для хранения ID родительских категорий.
2.  **Преобразование `id_category` в целое число**:
    - Пытается преобразовать `id_category` в целое число, если это строка.
    - Если преобразование не удаётся, логирует ошибку и переходит к следующей итерации цикла.
3.  **Преобразование `additional_categories_list` в список**:
    - Преобразует `additional_categories_list` в список, если это не список.
    - Добавляет `id_category` в `additional_categories_list`.
4.  **Цикл по категориям**:
    - Перебирает каждую категорию `c` в `additional_categories_list`.
5.  **Получение информации о родительской категории**:
    - Пытается получить информацию о родительской категории с использованием метода `read` суперкласса (API PrestaShop).
    - Если запрос не удаётся, логирует ошибку и переходит к следующей итерации цикла.
    - Если `parent` меньше или равно 2, это означает, что достигнута верхняя категория (дерево категорий начинается с 2), и функция возвращает текущий `out_categories_list`.
6.  **Добавление родительской категории в список**:
    - Добавляет `parent` в `out_categories_list`.

```
  Начало
  │
  ├── id_category (int/str)
  │   │
  │   └── Преобразование id_category в int (если str)
  │       │
  │       └── Обработка исключений при преобразовании
  │
  ├── additional_categories_list (List[int] | int)
  │   │
  │   └── Преобразование additional_categories_list в List (если не List)
  │   │
  │   └── Добавление id_category в additional_categories_list
  │
  ├── out_categories_list = []
  │
  └── Для каждой категории c в additional_categories_list:
      │
      ├── parent = await super().read('categories', resource_id=c)
      │   │
      │   └── Обработка исключений при чтении родительской категории
      │
      ├── Если parent <= 2:
      │   │
      │   └── return out_categories_list (Достигнута верхняя категория)
      │
      └── Добавление parent в out_categories_list
  │
  └── return out_categories_list
```

**Примеры**:

```python
import asyncio
from types import SimpleNamespace

# Пример 1: Получение родительских категорий для категории с ID 3
async def example():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    parent_categories = await category_manager.get_parent_categories_list_async(id_category=3)
    print(f"Parent categories: {parent_categories}")

asyncio.run(example())

# Пример 2: Получение родительских категорий с дополнительными категориями
async def example2():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    parent_categories = await category_manager.get_parent_categories_list_async(id_category=5, additional_categories_list=[3, 4])
    print(f"Parent categories: {parent_categories}")

asyncio.run(example2())

# Пример 3: ID категории передается как строка
async def example3():
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    category_manager = PrestaCategoryAsync(credentials=credentials)
    parent_categories = await category_manager.get_parent_categories_list_async(id_category="7")
    print(f"Parent categories: {parent_categories}")

asyncio.run(example3())
```

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

**Назначение**: Асинхронная функция `main` для демонстрации или тестирования функциональности модуля.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Внутри функции находится заглушка `...`, что означает, что функция не реализована.

**Примеры**:
- Невозможно привести примеры, так как функция не реализована.
```