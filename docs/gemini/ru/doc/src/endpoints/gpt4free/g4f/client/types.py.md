# Модуль определения типов для g4f клиента

## Обзор

Этот модуль определяет типы данных, используемые в g4f клиенте, такие как `ImageProvider`, `Proxies`, `IterResponse` и `AsyncIterResponse`. Также включает класс `Client` для управления API ключом и прокси.

## Подробней

Этот код определяет структуры данных и класс `Client`, используемые для взаимодействия с различными поставщиками изображений и управления прокси. Это важная часть проекта `hypotez`, поскольку обеспечивает гибкость в выборе провайдеров и настройке прокси для выполнения запросов.

## Классы

### `Client`

**Описание**: Класс `Client` предназначен для управления API-ключом и прокси-серверами при взаимодействии с различными поставщиками.

**Принцип работы**:
Класс `Client` инициализируется с API-ключом и настройками прокси. Он предоставляет метод `get_proxy` для получения настроек прокси из различных источников (переданные параметры, переменные окружения).

**Атрибуты**:
- `api_key` (str): API-ключ для аутентификации.
- `proxies` (Proxies): Настройки прокси-сервера. Может быть строкой или словарем.
- `proxy` (str): Фактический используемый прокси-сервер.

**Методы**:
- `__init__(self, api_key: str = None, proxies: Proxies = None, **kwargs) -> None`: Инициализирует экземпляр класса `Client` с API-ключом и настройками прокси.
- `get_proxy(self) -> Union[str, None]`: Получает строку прокси-сервера из различных источников.

## Функции

### `__init__`

```python
def __init__(
        self,
        api_key: str = None,
        proxies: Proxies = None,
        **kwargs
    ) -> None:
    """Инициализирует экземпляр класса `Client` с API-ключом и настройками прокси.

    Args:
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        proxies (Proxies, optional): Настройки прокси-сервера. Может быть строкой или словарем. По умолчанию `None`.

    Returns:
        None

    Raises:
        Нет
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `Client`.

**Параметры**:
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `proxies` (Proxies, optional): Настройки прокси-сервера. Может быть строкой или словарем. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет

**Как работает функция**:
1. Присваивает переданные значения `api_key` и `proxies` атрибутам экземпляра класса.
2. Вызывает метод `self.get_proxy()` для получения значения прокси-сервера и присваивает его атрибуту `self.proxy`.

```mermaid
graph LR
A[Присвоение api_key] --> B(Присвоение proxies)
B --> C{Получение proxy через get_proxy()}
C --> D(Присвоение значения proxy)
```

**Примеры**:

```python
client = Client(api_key="ключ", proxies={"https": "http://proxy.com"})
print(client.api_key, client.proxies)
```

### `get_proxy`

```python
def get_proxy(self) -> Union[str, None]:
    """Получает строку прокси-сервера из различных источников.

    Returns:
        Union[str, None]: Строка прокси-сервера или `None`, если прокси не настроен.

    Raises:
        Нет
    """
    ...
```

**Назначение**: Получение строки прокси-сервера из различных источников.

**Параметры**:
- Нет

**Возвращает**:
- `Union[str, None]`: Строка прокси-сервера или `None`, если прокси не настроен.

**Вызывает исключения**:
- Нет

**Как работает функция**:
1. Проверяет, является ли `self.proxies` строкой. Если да, возвращает её.
2. Если `self.proxies` равно `None`, пытается получить значение переменной окружения `G4F_PROXY` и возвращает его.
3. Если `self.proxies` является словарем, проверяет наличие ключей `"all"` или `"https"` и возвращает соответствующее значение.
4. Если ни одно из условий не выполнено, возвращает `None`.

```mermaid
graph LR
A{self.proxies is str} -->|Yes| B(return self.proxies)
A -->|No| C{self.proxies is None}
C -->|Yes| D(os.environ.get("G4F_PROXY"))
D --> E(return значение из os.environ или None)
C -->|No| F{all in self.proxies}
F -->|Yes| G(return self.proxies["all"])
F -->|No| H{https in self.proxies}
H -->|Yes| I(return self.proxies["https"])
H -->|No| J(return None)
```

**Примеры**:

```python
import os
os.environ["G4F_PROXY"] = "http://proxy_from_env.com"
client1 = Client()
print(client1.get_proxy())  # Выведет: http://proxy_from_env.com

client2 = Client(proxies="http://прямой_прокси.com")
print(client2.get_proxy())  # Выведет: http://прямой_прокси.com

client3 = Client(proxies={"https": "http://https_прокси.com"})
print(client3.get_proxy())  # Выведет: http://https_прокси.com