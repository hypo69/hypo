# Модуль для работы с чат-ботом OpenAI через g4f

## Обзор

Этот модуль предоставляет пример использования библиотеки `g4f` для взаимодействия с моделью `gpt-3.5-turbo` через провайдера `OpenaiChat`. Он демонстрирует, как установить прокси и настроить повторные попытки при сбое соединения.

## Подробнее

Этот код используется для отправки сообщений в чат-бот OpenAI и получения ответов. Он полезен в ситуациях, когда требуется программный доступ к API OpenAI, но необходимо обходить географические ограничения или обеспечивать отказоустойчивость.

## Функции

### `Client`

```python
class Client:
    """ Клиент для взаимодействия с API.

    Args:
        proxies (dict, optional): Словарь с настройками прокси для HTTP и HTTPS. По умолчанию None.
        provider (RetryProvider, optional): Провайдер для повторных попыток при сбое соединения. По умолчанию None.
    """
```

**Назначение**: Создает клиент для взаимодействия с API.

**Параметры**:
- `proxies` (dict, optional): Словарь, содержащий настройки прокси для HTTP и HTTPS соединений. Необходим для обхода географических ограничений OpenAI. Пример: `{'http': 'http://username:password@host:port', 'https': 'http://username:password@host:port'}`. По умолчанию `None`.
- `provider` (RetryProvider, optional): Провайдер для автоматического повтора запросов в случае сбоя соединения. Обеспечивает отказоустойчивость. По умолчанию `None`.

**Как работает функция**:

1.  **Инициализация клиента**: Функция создает экземпляр класса `Client` с заданными настройками прокси и провайдера.
2.  **Настройка прокси**: Если предоставлены прокси, они используются для всех HTTP и HTTPS запросов, что позволяет обходить географические ограничения.
3.  **Настройка провайдера**: Если указан провайдер, он отвечает за автоматический повтор запросов при сбоях, увеличивая надежность соединения.

```
Инициализация клиента --> Настройка прокси --> Настройка провайдера
```

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import OpenaiChat, RetryProvider

# Пример с прокси
client = Client(
    proxies={
        'http': 'http://username:password@host:port',
        'https': 'http://username:password@host:port'
    },
    provider=RetryProvider([OpenaiChat], single_provider_retry=True, max_retries=5)
)

# Пример без прокси (если не требуется)
client = Client(provider=RetryProvider([OpenaiChat], single_provider_retry=True, max_retries=5))
```

### `RetryProvider`

```python
class RetryProvider:
    """ Провайдер для повторных попыток при сбое соединения.

    Args:
        providers (List[Provider], optional): Список провайдеров для использования.
        single_provider_retry (bool, optional): Повторять попытки только с одним провайдером. По умолчанию True.
        max_retries (int, optional): Максимальное количество попыток. По умолчанию 5.
    """
```

**Назначение**: Создает провайдер для автоматического повтора запросов при сбое соединения.

**Параметры**:
- `providers` (List[Provider], optional): Список провайдеров для использования.
- `single_provider_retry` (bool, optional): Определяет, следует ли повторять попытки только с одним провайдером. По умолчанию `True`.
- `max_retries` (int, optional): Максимальное количество повторных попыток. По умолчанию `5`.

**Как работает функция**:

1.  **Инициализация провайдера**: Функция создает экземпляр класса `RetryProvider` с заданными настройками.
2.  **Настройка списка провайдеров**: Указывается список провайдеров, которые будут использоваться для отправки запросов.
3.  **Настройка параметров повтора**: Определяется, следует ли использовать только одного провайдера для повторных попыток и максимальное количество таких попыток.

```
Инициализация провайдера --> Настройка списка провайдеров --> Настройка параметров повтора
```

**Примеры**:

```python
from g4f.Provider import OpenaiChat, RetryProvider

# Пример с OpenaiChat
provider = RetryProvider([OpenaiChat], single_provider_retry=True, max_retries=5)

# Пример с несколькими провайдерами
# provider = RetryProvider([OpenaiChat, AnotherProvider], single_provider_retry=False, max_retries=3)
```

### `chat.completions.create`

```python
def create(model: str, messages: list, stream: bool = True) -> Generator[str, None, None]:
    """ Создает запрос на завершение чата.

    Args:
        model (str): Имя модели для использования (например, 'gpt-3.5-turbo').
        messages (list): Список сообщений для отправки в чат.
        stream (bool, optional): Использовать ли потоковую передачу данных. По умолчанию True.

    Returns:
        Generator[str, None, None]: Генератор, возвращающий части ответа.
    """
```

**Назначение**: Отправляет запрос в чат-бот и получает ответ.

**Параметры**:
- `model` (str): Имя используемой модели (например, `gpt-3.5-turbo`).
- `messages` (list): Список сообщений, составляющих контекст чата. Каждое сообщение представляет собой словарь с ключами `role` и `content`.
- `stream` (bool, optional): Определяет, использовать ли потоковую передачу данных. Если `True`, ответ возвращается частями в виде генератора. По умолчанию `True`.

**Как работает функция**:

1.  **Отправка запроса**: Функция отправляет запрос к API чат-бота с указанной моделью и сообщениями.
2.  **Получение ответа**: В зависимости от параметра `stream`, ответ возвращается либо целиком (если `stream=False`), либо частями в виде генератора (если `stream=True`).
3.  **Обработка потока**: Если используется потоковая передача, функция возвращает генератор, который выдает части ответа по мере их поступления.

```
Отправка запроса --> Получение ответа (целиком или частями) --> Обработка потока (если stream=True)
```

**Примеры**:

```python
from g4f.client import Client
from g4f.Provider import OpenaiChat, RetryProvider

client = Client(
    proxies={
        'http': 'http://username:password@host:port',
        'https': 'http://username:password@host:port'
    },
    provider=RetryProvider([OpenaiChat], single_provider_retry=True, max_retries=5)
)

messages = [
    {'role': 'user', 'content': 'Hello'}
]

# Пример с потоковой передачей
response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages, stream=True)
for message in response:
    print(message.choices[0].delta.content or "")

# Пример без потоковой передачи (если поддерживается)
# response = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages, stream=False)
# print(response.choices[0].message.content)