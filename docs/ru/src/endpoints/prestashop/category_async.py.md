# Модуль `category_async`

## Обзор

Модуль `category_async` предназначен для асинхронного управления категориями в PrestaShop. Он предоставляет функциональность для получения родительских категорий для заданной категории.

## Подробней

Этот модуль предоставляет асинхронный класс `PrestaCategoryAsync`, который позволяет взаимодействовать с API PrestaShop для управления категориями. Он использует асинхронные запросы для повышения производительности при работе с API. Расположение файла: `hypotez/src/endpoints/prestashop/category_async.py` указывает на его роль в структуре проекта, как часть endpoints для работы с PrestaShop.

## Классы

### `PrestaCategoryAsync`

**Описание**: Асинхронный класс для управления категориями в PrestaShop.

**Как работает класс**:
Класс `PrestaCategoryAsync` наследуется от `PrestaShopAsync` и предоставляет методы для работы с категориями в PrestaShop. При инициализации класса требуется передать учетные данные (либо в виде словаря, либо как отдельные параметры `api_domain` и `api_key`). Если учетные данные не переданы, будет вызвано исключение `ValueError`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaCategoryAsync`.
- `get_parent_categories_list_async`: Асинхронно получает список родительских категорий для заданной категории.

#### `__init__`

```python
def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
    """Инициализирует экземпляр класса `PrestaCategoryAsync`.

    Args:
        credentials (Optional[Union[dict, SimpleNamespace]], optional): Словарь или SimpleNamespace с учетными данными API. По умолчанию None.
        api_domain (Optional[str], optional): Домен API PrestaShop. По умолчанию None.
        api_key (Optional[str], optional): Ключ API PrestaShop. По умолчанию None.

    Raises:
        ValueError: Если не переданы `api_domain` или `api_key`.

    """
```

**Параметры**:
- `credentials` (Optional[Union[dict, SimpleNamespace]], optional): Словарь или `SimpleNamespace` с учетными данными API (`api_domain` и `api_key`). По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.

**Вызывает исключения**:
- `ValueError`: Если не переданы `api_domain` или `api_key`.

#### `get_parent_categories_list_async`

```python
async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
    """Асинхронно получает список родительских категорий для заданной категории.

    Args:
        id_category (int | str): ID категории, для которой нужно получить родительские категории.
        additional_categories_list (Optional[List[int] | int], optional): Список дополнительных категорий для обработки. По умолчанию [].

    Returns:
        List[int]: Список ID родительских категорий.

    Raises:
        Exception: Если возникает ошибка при чтении данных о категории.

    """
```

**Как работает функция**:
1. Функция принимает `id_category` (ID категории) и `additional_categories_list` (список дополнительных категорий).
2. Преобразует `id_category` в целое число, если это возможно. В случае ошибки логирует ошибку и пропускает итерацию.
3. Преобразует `additional_categories_list` в список, если это необходимо, и добавляет `id_category` в этот список.
4. Итерируется по списку категорий `additional_categories_list`.
5. Для каждой категории пытается получить информацию о родительской категории с использованием метода `read` класса `PrestaShopAsync`.
6. Если родительская категория меньше или равна 2, возвращает накопленный список родительских категорий (так как дерево категорий начинается с 2).
7. Добавляет ID родительской категории в список `out_categories_list`.
8. В случае ошибки при чтении данных о категории, логирует ошибку и переходит к следующей итерации.

**Параметры**:
- `id_category` (int | str): ID категории, для которой нужно получить родительские категории.
- `additional_categories_list` (Optional[List[int] | int], optional): Список дополнительных категорий для обработки. По умолчанию `[]`.

**Возвращает**:
- `List[int]`: Список ID родительских категорий.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении данных о категории.

## Функции

### `main`

```python
async def main():
    """"""
    ...
```

**Описание**:
Функция `main` предназначена для асинхронного выполнения основной логики.

**Как работает функция**:
Функция помечена как `async`, что позволяет использовать в ней асинхронные вызовы. Внутри тела функции находится `...`, что означает, что функция не реализована и требует дальнейшей доработки.

### Примеры
Примеры вызовов
```python
async def main():
    # Пример использования класса PrestaCategoryAsync и метода get_parent_categories_list_async
    category_manager = PrestaCategoryAsync(api_domain='your_api_domain', api_key='your_api_key')
    category_id = 10
    parent_categories = await category_manager.get_parent_categories_list_async(category_id)
    print(f"Parent categories for category {category_id}: {parent_categories}")

if __name__ == '__main__':
    asyncio.run(main())