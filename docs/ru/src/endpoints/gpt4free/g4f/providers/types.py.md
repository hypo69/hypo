# Модуль `types.py`

## Обзор

Модуль `types.py` определяет абстрактные базовые классы для провайдеров, используемых в проекте `hypotez` для взаимодействия с различными сервисами, такими как GPT-4free. Он содержит абстрактные классы `BaseProvider` и `BaseRetryProvider`, а также класс `Streaming`.

## Подробней

Этот модуль задает интерфейсы, которые должны быть реализованы конкретными провайдерами. `BaseProvider` определяет основные атрибуты и методы, необходимые для работы с провайдером, такие как URL, статус работы, необходимость аутентификации и поддержку потоковой передачи. `BaseRetryProvider` расширяет `BaseProvider`, добавляя логику повторных попыток с использованием списка провайдеров. Класс Streaming предназначен для обработки потоковых данных.

## Классы

### `BaseProvider`

**Описание**: Абстрактный базовый класс для провайдеров.

**Принцип работы**:
`BaseProvider` является основой для всех провайдеров. Он определяет общие атрибуты и абстрактные методы, которые должны быть реализованы в подклассах. Это позволяет обеспечить единый интерфейс для работы с различными провайдерами.

**Аттрибуты**:

- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для работы с провайдером.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `params` (str): Список параметров для провайдера.

**Методы**:

- `get_create_function() -> callable`
    - **Назначение**: Возвращает функцию создания для провайдера.
    - **Как работает функция**: Это абстрактный метод, который должен быть реализован в подклассах для возвращения функции, используемой для создания экземпляра провайдера.
- `get_async_create_function() -> callable`
    - **Назначение**: Возвращает асинхронную функцию создания для провайдера.
    - **Как работает функция**: Это абстрактный метод, который должен быть реализован в подклассах для возвращения асинхронной функции, используемой для создания экземпляра провайдера.
- `get_dict() -> Dict[str, str]`
    - **Назначение**: Возвращает словарь, представляющий провайдера.
    - **Как работает функция**: Этот метод создает и возвращает словарь, содержащий имя, URL и метку провайдера.

```python
    @classmethod
    def get_dict(cls) -> Dict[str, str]:
        """
        Get a dictionary representation of the provider.

        Returns:
            Dict[str, str]: A dictionary with provider's details.
        """
        return {'name': cls.__name__, 'url': cls.url, 'label': getattr(cls, 'label', None)}
```

     A -> B -> C

     A: Начало (вход в функцию)
     B: Создание словаря с данными провайдера
     C: Возврат словаря

**Примеры**:

```python
class MyProvider(BaseProvider):
    url = "https://example.com"
    working = True
    needs_auth = False
    supports_stream = True
    supports_message_history = True
    supports_system_message = True
    params = "param1, param2"

    def get_create_function(self) -> callable:
        def create_function():
            return "Provider created"
        return create_function

    def get_async_create_function(self) -> callable:
        async def async_create_function():
            return "Async Provider created"
        return async_create_function

    @classmethod
    def get_dict(cls) -> Dict[str, str]:
        return {'name': cls.__name__, 'url': cls.url, 'label': getattr(cls, 'label', None)}
```

### `BaseRetryProvider`

**Описание**: Базовый класс для провайдера, реализующего логику повторных попыток.

**Наследует**: `BaseProvider`

**Принцип работы**:
`BaseRetryProvider` расширяет `BaseProvider`, добавляя функциональность для повторных попыток при сбое. Он использует список провайдеров и пытается выполнить операцию с каждым из них, пока не будет достигнут успех или не будут исчерпаны все провайдеры.

**Аттрибуты**:

- `providers` (List[Type[BaseProvider]]): Список провайдеров для использования в повторных попытках.
- `shuffle` (bool): Указывает, нужно ли перемешивать список провайдеров.
- `exceptions` (Dict[str, Exception]): Словарь возникших исключений.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

```python
    __name__: str = "RetryProvider"
    supports_stream: bool = True
    last_provider: Type[BaseProvider] = None
```

**Примеры**:

```python
from typing import List, Type

class MyRetryProvider(BaseRetryProvider):
    providers: List[Type[BaseProvider]] = []
    shuffle: bool = True
    exceptions: Dict[str, Exception] = {}
    last_provider: Type[BaseProvider] = None
```

### `Streaming`

**Описание**: Класс для представления потоковых данных.

**Принцип работы**:

Класс Streaming предназначен для хранения и представления потоковых данных в виде строки.

**Аттрибуты**:

- `data` (str): Строка, содержащая потоковые данные.

**Методы**:

- `__init__(self, data: str) -> None`
    - **Назначение**: Инициализирует экземпляр класса `Streaming`.
    - **Параметры**:
        - `data` (str): Данные для инициализации.
- `__str__(self) -> str`
    - **Назначение**: Возвращает строковое представление данных.
    - **Как работает функция**: Преобразует данные в строковое представление.

**Примеры**:

```python
streaming_data = Streaming("Пример потоковых данных")
print(str(streaming_data))  # Вывод: Пример потоковых данных
```

## Функции

### `get_create_function`
```python
@abstractmethod
def get_create_function() -> callable:
    """
    Get the create function for the provider.

    Returns:
        callable: The create function.
    """
    raise NotImplementedError()
```
**Назначение**: Получить функцию создания для провайдера.
**Параметры**: Нет

**Возвращает**:
`callable`: Функция создания.

**Вызывает исключения**:
`NotImplementedError`: Если функция не реализована в подклассе.

**Как работает функция**:
1. Это абстрактный метод, который должен быть реализован в подклассах для возвращения функции, используемой для создания экземпляра провайдера.

ASCII flowchart:
```
    Начало -> Вызвать исключение NotImplementedError -> Конец
```

### `get_async_create_function`
```python
@abstractmethod
def get_async_create_function() -> callable:
    """
    Get the async create function for the provider.

    Returns:
        callable: The create function.
    """
    raise NotImplementedError()
```

**Назначение**: Получить асинхронную функцию создания для провайдера.

**Параметры**: Нет

**Возвращает**:
`callable`: Асинхронная функция создания.

**Вызывает исключения**:
`NotImplementedError`: Если функция не реализована в подклассе.

**Как работает функция**:
1. Это абстрактный метод, который должен быть реализован в подклассах для возвращения асинхронной функции, используемой для создания экземпляра провайдера.

ASCII flowchart:
```
    Начало -> Вызвать исключение NotImplementedError -> Конец
```

### `get_dict`
```python
@classmethod
def get_dict(cls) -> Dict[str, str]:
    """
    Get a dictionary representation of the provider.

    Returns:
        Dict[str, str]: A dictionary with provider's details.
    """
    return {'name': cls.__name__, 'url': cls.url, 'label': getattr(cls, 'label', None)}
```

**Назначение**: Получить словарь, представляющий провайдера.

**Параметры**: Нет

**Возвращает**:
`Dict[str, str]`: Словарь с деталями провайдера.

**Как работает функция**:
1.  Создает словарь, содержащий имя, URL и метку провайдера.
2.  Возвращает созданный словарь.

ASCII flowchart:
```
    Начало -> Создать словарь -> Вернуть словарь -> Конец
```
## Переменные

### `ProviderType`

**Описание**: Псевдоним типа, представляющий либо `BaseProvider`, либо `BaseRetryProvider`.

**Принцип работы**:
Используется для указания типа провайдера, который может быть либо базовым, либо поддерживающим повторные попытки.
```python
ProviderType = Union[Type[BaseProvider], BaseRetryProvider]
```
```