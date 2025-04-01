# Модуль определения типов для g4f клиента

## Обзор

Модуль `types.py` определяет типы данных, используемые в g4f клиенте. Он включает в себя импорты для работы с чат-завершениями, провайдерами, итераторами и прокси. Также, в модуле определен класс `Client`, который инициализирует API ключ и прокси для работы с g4f.

## Подробней

Этот модуль содержит определения типов, которые используются для обеспечения строгой типизации и лучшей поддержки в IDE. Определяются типы для провайдеров изображений, прокси, итераторов и асинхронных итераторов ответов. Класс `Client` позволяет инициализировать клиент с API ключом и прокси, а также предоставляет метод для получения прокси из различных источников.

## Классы

### `Client`

**Описание**: Класс `Client` инициализирует API ключ и прокси для работы с g4f.

**Принцип работы**:
Класс `Client` принимает API ключ и прокси в качестве аргументов при инициализации. Он также предоставляет метод `get_proxy` для получения прокси из различных источников, таких как переменные окружения и словарь прокси.

**Аттрибуты**:
- `api_key` (str): API ключ для аутентификации.
- `proxies` (Proxies): Прокси для использования при запросах.
- `proxy` (str | None): Прокси, полученный из различных источников.

**Методы**:
- `get_proxy()`: Получает прокси из различных источников.

## Функции

### `get_proxy`

```python
def get_proxy(self) -> Union[str, None]:
    """ Функция получает прокси из различных источников.

    Args:
        self (Client): Экземпляр класса `Client`.

    Returns:
        str | None: Прокси в виде строки или `None`, если прокси не найден.
    """
```

**Назначение**: Функция `get_proxy` определяет, какой прокси использовать для HTTP запросов.

**Как работает функция**:

1.  **Проверка типа `self.proxies`**:
    - Если `self.proxies` является строкой, функция возвращает эту строку как прокси.
    - Если `self.proxies` равно `None`, функция пытается получить прокси из переменной окружения `G4F_PROXY`.

2.  **Поиск прокси в словаре**:
    - Если `self.proxies` является словарем, функция проверяет наличие ключей `"all"` и `"https"` в словаре.
    - Если ключ `"all"` присутствует, функция возвращает значение этого ключа как прокси.
    - Если ключ `"https"` присутствует, функция возвращает значение этого ключа как прокси.

3.  **Возврат значения**:
    - Если ни одно из условий не выполнено, функция возвращает `None`.

```
Проверка типа прокси --> Прокси строка? --> Вернуть прокси
        |                 |
        |                 Нет
        |                 |
        Да                Прокси = None? --> Попытка получить прокси из G4F_PROXY --> Вернуть прокси
        |                               |                                      |
        Конец                             |                                      Нет
                                          |                                      |
                                          Да                                     Конец
                                          |
                                          Прокси словарь? --> "all" в прокси? --> Вернуть прокси из "all"
                                                              |                                  |
                                                              |                                  Да
                                                              Нет                                |
                                                              |                                  Конец
                                                              |
                                                              "https" в прокси? --> Вернуть прокси из "https"
                                                                                |
                                                                                Да
                                                                                |
                                                                                Конец
```

**Примеры**:

```python
from __future__ import annotations

import os

from .stubs import ChatCompletion, ChatCompletionChunk
from ..providers.types import BaseProvider
from typing import Union, Iterator, AsyncIterator

ImageProvider = Union[BaseProvider, object]
Proxies = Union[dict, str]
IterResponse = Iterator[Union[ChatCompletion, ChatCompletionChunk]]
AsyncIterResponse = AsyncIterator[Union[ChatCompletion, ChatCompletionChunk]]

class Client():
    def __init__(
        self,
        api_key: str = None,
        proxies: Proxies = None,
        **kwargs
    ) -> None:
        self.api_key: str = api_key
        self.proxies= proxies 
        self.proxy: str = self.get_proxy()

    def get_proxy(self) -> Union[str, None]:
        if isinstance(self.proxies, str):
            return self.proxies
        elif self.proxies is None:
            return os.environ.get("G4F_PROXY")
        elif "all" in self.proxies:
            return self.proxies["all"]
        elif "https" in self.proxies:
            return self.proxies["https"]

# Пример 1: Инициализация клиента без прокси
client = Client(api_key="test_api_key")
print(f"Proxy: {client.get_proxy()}")  # Вывод: Proxy: None (если переменная окружения G4F_PROXY не установлена)

# Пример 2: Инициализация клиента с прокси в виде строки
client = Client(api_key="test_api_key", proxies="http://proxy.example.com:8080")
print(f"Proxy: {client.get_proxy()}")  # Вывод: Proxy: http://proxy.example.com:8080

# Пример 3: Инициализация клиента с прокси в виде словаря
client = Client(api_key="test_api_key", proxies={"https": "http://proxy.example.com:8080"})
print(f"Proxy: {client.get_proxy()}")  # Вывод: Proxy: http://proxy.example.com:8080

# Пример 4: Инициализация клиента с прокси в виде словаря с ключом "all"
client = Client(api_key="test_api_key", proxies={"all": "http://proxy.example.com:8080"})
print(f"Proxy: {client.get_proxy()}")  # Вывод: Proxy: http://proxy.example.com:8080