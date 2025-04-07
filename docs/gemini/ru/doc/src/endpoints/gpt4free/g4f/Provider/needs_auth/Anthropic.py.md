# Модуль Anthropic

## Обзор

Модуль `Anthropic` предоставляет интерфейс для взаимодействия с API Anthropic, включая поддержку стриминга, системных сообщений и истории сообщений. Он также поддерживает отправку изображений в сообщениях.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями Anthropic. Он предоставляет функциональность для аутентификации, отправки запросов и обработки ответов от API Anthropic.
Модуль позволяет использовать различные модели Anthropic, включая `claude-3-5-sonnet-latest`, `claude-3-opus-latest` и другие.

## Классы

### `Anthropic(OpenaiAPI)`

**Описание**: Класс `Anthropic` наследует функциональность от класса `OpenaiAPI` и предоставляет методы для взаимодействия с API Anthropic.

**Наследует**:
- `OpenaiAPI`: Класс, предоставляющий базовую функциональность для работы с API OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера API ("Anthropic API").
- `url` (str): URL консоли Anthropic ("https://console.anthropic.com").
- `login_url` (str): URL для входа в Anthropic ("https://console.anthropic.com/settings/keys").
- `working` (bool): Указывает, работает ли API (True).
- `api_base` (str): Базовый URL API Anthropic ("https://api.anthropic.com/v1").
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `supports_stream` (bool): Указывает, поддерживается ли стриминг (True).
- `supports_system_message` (bool): Указывает, поддерживаются ли системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживается ли история сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("claude-3-5-sonnet-latest").
- `models` (list[str]): Список поддерживаемых моделей.
- `models_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models()`: Возвращает список доступных моделей.
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с API Anthropic.
- `get_headers()`: Возвращает заголовки для запросов к API Anthropic.

## Функции

### `get_models(api_key: str = None, **kwargs) -> list[str]`

**Назначение**: Получает список доступных моделей от API Anthropic.

**Параметры**:
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `list[str]`: Список идентификаторов моделей.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если возникает ошибка при выполнении HTTP-запроса.

**Как работает функция**:

1. **Проверка наличия моделей в кэше**: Проверяется, загружены ли уже модели в атрибут `cls.models`.
2. **Выполнение HTTP-запроса**: Если модели не загружены, выполняется GET-запрос к API Anthropic для получения списка моделей.
3. **Обработка ответа**: Извлекаются идентификаторы моделей из JSON-ответа и сохраняются в `cls.models`.
4. **Возврат списка моделей**: Возвращается список идентификаторов моделей.

```ascii
Проверка наличия моделей в кэше
↓
Выполнение HTTP-запроса к API Anthropic
↓
Обработка ответа (извлечение идентификаторов моделей)
↓
Сохранение идентификаторов моделей в cls.models
↓
Возврат списка идентификаторов моделей
```

**Примеры**:

```python
# Пример получения списка моделей
models = Anthropic.get_models(api_key='YOUR_API_KEY')
print(models)
# Вывод: ['claude-3-5-sonnet-latest', 'claude-3-5-sonnet-20241022', ...]
```

### `create_async_generator(model: str, messages: Messages, proxy: str = None, timeout: int = 120, media: MediaListType = None, api_key: str = None, temperature: float = None, max_tokens: int = 4096, top_k: int = None, top_p: float = None, stop: list[str] = None, stream: bool = False, headers: dict = None, impersonate: str = None, tools: Optional[list] = None, extra_data: dict = {}, **kwargs) -> AsyncResult`

**Назначение**: Создает асинхронный генератор для взаимодействия с API Anthropic.

**Параметры**:
- `model` (str): Идентификатор модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 4096.
- `top_k` (int, optional): Параметр top_k для генерации текста. По умолчанию `None`.
- `top_p` (float, optional): Параметр top_p для генерации текста. По умолчанию `None`.
- `stop` (list[str], optional): Список стоп-слов. По умолчанию `None`.
- `stream` (bool, optional): Указывает, использовать ли стриминг. По умолчанию `False`.
- `headers` (dict, optional): Дополнительные заголовки для запроса. По умолчанию `None`.
- `impersonate` (str, optional): Имя пользователя для имитации. По умолчанию `None`.
- `tools` (Optional[list], optional): Список инструментов для использования. По умолчанию `None`.
- `extra_data` (dict, optional): Дополнительные данные для запроса. По умолчанию `{}`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API Anthropic.

**Вызывает исключения**:
- `MissingAuthError`: Если не указан `api_key`.
- `requests.exceptions.HTTPError`: Если возникает ошибка при выполнении HTTP-запроса.

**Как работает функция**:

1. **Проверка наличия API-ключа**: Проверяется, передан ли `api_key`. Если нет, вызывается исключение `MissingAuthError`.
2. **Обработка медиафайлов**: Если переданы медиафайлы, они кодируются в base64 и добавляются в сообщение.
3. **Подготовка системного сообщения**: Извлекаются системные сообщения из списка сообщений.
4. **Создание асинхронной сессии**: Создается асинхронная сессия для выполнения HTTP-запросов.
5. **Подготовка данных для запроса**: Подготавливаются данные для запроса, включая сообщения, модель, параметры генерации и т.д.
6. **Выполнение POST-запроса**: Выполняется POST-запрос к API Anthropic.
7. **Обработка ответа**:
   - Если стриминг не используется, ответ обрабатывается как JSON.
   - Если стриминг используется, ответ обрабатывается построчно.
8. **Генерация результатов**: Возвращается асинхронный генератор, который выдает результаты по мере их получения от API Anthropic.

```ascii
Проверка наличия API-ключа
↓
Обработка медиафайлов (кодирование в base64)
↓
Подготовка системного сообщения
↓
Создание асинхронной сессии
↓
Подготовка данных для запроса
↓
Выполнение POST-запроса к API Anthropic
↓
Обработка ответа (JSON или построчно)
↓
Генерация результатов
```

**Примеры**:

```python
# Пример создания асинхронного генератора
async def main():
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for chunk in Anthropic.create_async_generator(model='claude-3-5-sonnet-latest', messages=messages, api_key='YOUR_API_KEY'):
        print(chunk, end='')

import asyncio
asyncio.run(main())
# Вывод: Hello, I am doing well. How can I assist you today?
```

### `get_headers(stream: bool, api_key: str = None, headers: dict = None) -> dict`

**Назначение**: Формирует заголовки для HTTP-запроса к API Anthropic.

**Параметры**:
- `stream` (bool): Указывает, используется ли стриминг.
- `api_key` (str, optional): Ключ API для аутентификации. По умолчанию `None`.
- `headers` (dict, optional): Дополнительные заголовки. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь с заголовками для запроса.

**Как работает функция**:

1. **Определение типа содержимого**: В зависимости от параметра `stream` устанавливается заголовок `Accept` (text/event-stream или application/json).
2. **Добавление API-ключа**: Если передан `api_key`, добавляется заголовок `x-api-key`.
3. **Добавление версии API**: Добавляется заголовок `anthropic-version` с версией API.
4. **Объединение заголовков**: Объединяются все заголовки в один словарь.

```ascii
Определение типа содержимого (stream или json)
↓
Добавление API-ключа (если передан)
↓
Добавление версии API
↓
Объединение всех заголовков в один словарь
↓
Возврат словаря с заголовками
```

**Примеры**:

```python
# Пример получения заголовков для запроса
headers = Anthropic.get_headers(stream=True, api_key='YOUR_API_KEY')
print(headers)
# Вывод: {'Accept': 'text/event-stream', 'Content-Type': 'application/json', 'x-api-key': 'YOUR_API_KEY', 'anthropic-version': '2023-06-01'}