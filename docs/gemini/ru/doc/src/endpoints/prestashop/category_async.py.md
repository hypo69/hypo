# Модуль `category_async`

## Обзор

Модуль `category_async` предоставляет асинхронный класс `PrestaCategoryAsync` для управления категориями в PrestaShop. Он позволяет асинхронно получать родительские категории для заданной категории.

## Подробнее

Модуль предназначен для асинхронного взаимодействия с API PrestaShop для выполнения операций, связанных с категориями. Он использует асинхронные запросы для повышения производительности и эффективности при работе с большим количеством категорий. Расположен в `/src/endpoints/prestashop/category_async.py` и является частью подсистемы для интеграции с PrestaShop.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Наследует**:
- `PrestaShopAsync`: Наследует методы для асинхронного взаимодействия с API PrestaShop.

**Атрибуты**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.

**Методы**:
- `__init__(credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None)`: Инициализирует экземпляр класса `PrestaCategoryAsync`.
- `get_parent_categories_list_async(self, id_category: int|str, additional_categories_list: Optional[List[int] | int] = []) -> List[int]`: Асинхронно получает список родительских категорий для заданной категории.

#### `__init__`

```python
def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
    """
    Инициализирует экземпляр класса `PrestaCategoryAsync`.

    Args:
        credentials (Optional[Union[dict, SimpleNamespace]], optional): Словарь или `SimpleNamespace` с учетными данными API. По умолчанию `None`.
        api_domain (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
        api_key (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

    Raises:
        ValueError: Если `api_domain` или `api_key` не предоставлены.
    """
    ...
```

**Как работает класс**:

1.  Инициализация экземпляра класса `PrestaCategoryAsync`.
2.  Извлекает `api_domain` и `api_key` из `credentials`, если они предоставлены.
3.  Проверяет, что `api_domain` и `api_key` не пусты. В противном случае вызывает исключение `ValueError`.
4.  Вызывает конструктор родительского класса `PrestaShopAsync` с `api_domain` и `api_key`.

#### `get_parent_categories_list_async`

```python
async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
    """
    Асинхронно получает родительские категории для заданной категории.

    Args:
        id_category (int | str): ID категории, для которой нужно получить родительские категории.
        additional_categories_list (Optional[List[int] | int], optional): Список дополнительных категорий для обработки. По умолчанию пустой список `[]`.

    Returns:
        List[int]: Список ID родительских категорий.

    Raises:
        Exception: Если возникает ошибка при чтении категории.
    """
    ...
```

**Как работает функция**:

1.  Преобразует `id_category` в целое число, если это возможно. Если преобразование не удается, записывает ошибку в лог.
2.  Преобразует `additional_categories_list` в список, если это не список.
3.  Добавляет `id_category` в `additional_categories_list`.
4.  Инициализирует пустой список `out_categories_list` для хранения ID родительских категорий.
5.  Перебирает категории в `additional_categories_list`.
6.  Для каждой категории пытается асинхронно прочитать информацию о родительской категории с помощью метода `read` родительского класса `PrestaShopAsync`.
7.  Если чтение не удается, записывает ошибку в лог и переходит к следующей категории.
8.  Если родительская категория <= 2, возвращает `out_categories_list`, так как это верхний уровень дерева категорий (дерево категорий начинается с 2).
9.  Добавляет ID родительской категории в `out_categories_list`.
10. Возвращает `out_categories_list`.

**ASCII схема работы функции**:

```
Начало --> Преобразование id_category в int --> Преобразование additional_categories_list в list --> Добавление id_category в additional_categories_list --> Инициализация out_categories_list -->
    Цикл по категориям в additional_categories_list:
        --> Асинхронное чтение родительской категории через API PrestaShop
        --> Если ошибка при чтении: Лог ошибки --> Следующая категория
        --> Если родительская категория <= 2: Возврат out_categories_list
        --> Добавление ID родительской категории в out_categories_list
    Конец цикла
--> Возврат out_categories_list
```

**Примеры**:

```python
# Пример использования класса PrestaCategoryAsync и метода get_parent_categories_list_async
import asyncio
from types import SimpleNamespace

async def main():
    # Предположим, что у вас есть учетные данные
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    
    # Создаем экземпляр класса PrestaCategoryAsync
    category_manager = PrestaCategoryAsync(credentials=credentials)
    
    # ID категории, для которой нужно получить родительские категории
    category_id = 3
    
    # Получаем список родительских категорий
    parent_categories = await category_manager.get_parent_categories_list_async(category_id)
    
    # Выводим список родительских категорий
    print(f"Parent categories for category {category_id}: {parent_categories}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

Функция `main` является асинхронной функцией, предназначенной для демонстрации или тестирования функциональности модуля. В текущей реализации она не содержит конкретной логики (`...`).