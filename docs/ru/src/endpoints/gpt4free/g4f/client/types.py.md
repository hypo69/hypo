# Модуль типов для g4f клиента

## Обзор

Этот модуль определяет типы данных, используемые в g4f клиенте. Он содержит определения для `ImageProvider`, `Proxies`, `IterResponse`, `AsyncIterResponse` и класса `Client`. Модуль также импортирует необходимые классы и типы из других модулей, таких как `ChatCompletion`, `ChatCompletionChunk`, `BaseProvider`, `Union`, `Iterator`, `AsyncIterator`.

## Подробней

Этот модуль является частью g4f клиента и определяет типы данных, используемые в других частях клиента. Он также содержит класс `Client`, который используется для взаимодействия с API g4f.

## Классы

### `Client`

**Описание**: Класс `Client` используется для создания экземпляра клиента для взаимодействия с API g4f.

**Принцип работы**:
Класс `Client` инициализируется с использованием `api_key`, `proxies` и дополнительных аргументов. Он устанавливает значения для `api_key`, `proxies` и `proxy`. Метод `get_proxy` используется для получения прокси из различных источников, таких как переданные прокси, переменные окружения или предопределенные ключи в словаре прокси.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Client`.
- `get_proxy`: Возвращает прокси-сервер для использования в запросах.

#### `__init__`

```python
def __init__(
    self,
    api_key: str = None,
    proxies: Proxies = None,
    **kwargs
) -> None:
    """
    Инициализирует экземпляр класса `Client`.

    Args:
        api_key (str, optional): Ключ API для аутентификации. По умолчанию `None`.
        proxies (Proxies, optional): Прокси-серверы для использования в запросах. Может быть строкой или словарем. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        None

    Raises:
        None
    """
```

**Параметры**:
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `proxies` (Proxies, optional): Прокси-серверы для использования в запросах. Может быть строкой или словарем. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Как работает функция**:
1. Метод инициализирует экземпляр класса `Client`.
2. Устанавливает значения для `api_key`, `proxies` и `proxy`.
3. Вызывает метод `get_proxy` для получения прокси.

#### `get_proxy`

```python
def get_proxy(self) -> Union[str, None]:
    """
    Возвращает прокси-сервер для использования в запросах.

    Args:
        None

    Returns:
        Union[str, None]: Прокси-сервер или `None`, если прокси не найден.

    Raises:
        None
    """
```

**Параметры**:
- Нет параметров.

**Возвращает**:
- `Union[str, None]`: Прокси-сервер или `None`, если прокси не найден.

**Как работает функция**:
1. Проверяет, является ли `self.proxies` строкой. Если да, возвращает его.
2. Если `self.proxies` равен `None`, пытается получить прокси из переменной окружения `G4F_PROXY`.
3. Если `self.proxies` является словарем, проверяет наличие ключей `"all"` или `"https"` и возвращает соответствующее значение.

**Примеры**:

```python
# Пример 1: Использование прокси из строки
client = Client(proxies='http://proxy.example.com')
proxy = client.get_proxy()
print(proxy)  # Вывод: http://proxy.example.com

# Пример 2: Использование прокси из словаря
client = Client(proxies={'https': 'http://proxy.example.com'})
proxy = client.get_proxy()
print(proxy)  # Вывод: http://proxy.example.com

# Пример 3: Использование прокси из переменной окружения
os.environ['G4F_PROXY'] = 'http://proxy.example.com'
client = Client()
proxy = client.get_proxy()
print(proxy)  # Вывод: http://proxy.example.com
```

## Типы

- `ImageProvider`: Тип для провайдера изображений. Может быть экземпляром `BaseProvider` или `object`.
- `Proxies`: Тип для прокси-серверов. Может быть словарем или строкой.
- `IterResponse`: Тип для итератора ответов. Итерирует `ChatCompletion` или `ChatCompletionChunk`.
- `AsyncIterResponse`: Тип для асинхронного итератора ответов. Асинхронно итерирует `ChatCompletion` или `ChatCompletionChunk`.