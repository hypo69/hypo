# Модуль API для взаимодействия с gpt4free

## Обзор

Модуль `api.py` предоставляет API для взаимодействия с различными провайдерами gpt4free. Он включает в себя функции для получения моделей, провайдеров, версий, а также для обработки разговоров и создания потоков ответов.

## Подробней

Этот модуль является частью графического интерфейса сервера и служит для организации взаимодействия с различными поставщиками языковых моделей. Он предоставляет набор статических методов и функций для получения информации о моделях, провайдерах и версиях, а также для управления ходом диалогов и формирования ответов.

## Классы

### `Api`

**Описание**: Класс `Api` предоставляет статические методы для получения информации о моделях, провайдерах и версиях, а также методы для обработки разговоров и создания потоков ответов.

**Принцип работы**:
Класс `Api` предоставляет набор статических методов для получения информации о моделях, провайдерах и версиях. Он также содержит методы для подготовки параметров разговора, создания потока ответов, обработки провайдеров и форматирования JSON-ответов.

**Методы**:

- `get_models()`: Возвращает список доступных моделей.
- `get_provider_models(provider: str, api_key: str = None, api_base: str = None)`: Возвращает список моделей, доступных для указанного провайдера.
- `get_providers()`: Возвращает список доступных провайдеров.
- `get_version()`: Возвращает информацию о текущей и последней версиях.
- `serve_images(name)`: Возвращает запрошенное изображение из директории изображений.
- `_prepare_conversation_kwargs(json_data: dict)`: Подготавливает аргументы для создания разговора.
- `_create_response_stream(self, kwargs: dict, conversation_id: str, provider: str, download_media: bool = True)`: Создает поток ответов от провайдера.
- `_yield_logs()`: Возвращает логи отладки.
- `_format_json(self, response_type: str, content = None, **kwargs)`: Форматирует JSON-ответ.
- `handle_provider(self, provider_handler, model)`: Обрабатывает провайдера и возвращает информацию о нем.

## Функции

### `get_error_message`

```python
def get_error_message(exception: Exception) -> str:
    """
    Формирует сообщение об ошибке из перехваченного исключения.

    Args:
        exception (Exception): Объект исключения.

    Returns:
        str: Отформатированное сообщение об ошибке, включающее тип исключения и сообщение.
    """
```

**Назначение**: Формирует сообщение об ошибке на основе переданного исключения.

**Параметры**:

- `exception` (Exception): Объект исключения, для которого требуется получить сообщение об ошибке.

**Возвращает**:

- `str`: Отформатированное сообщение об ошибке, содержащее тип исключения и сообщение.

**Как работает функция**:

1.  Получает тип исключения (`type(exception).__name__`).
2.  Получает строковое представление исключения (`str(exception)`).
3.  Форматирует строку, объединяя тип исключения и сообщение.

**ASCII flowchart**:

```
Exception -> Get exception type -> Get exception message -> Format message -> Return message
```

**Примеры**:

```python
try:
    raise ValueError("Invalid value")
except ValueError as ex:
    error_message = get_error_message(ex)
    print(error_message)  # Вывод: ValueError: Invalid value
```
```python
try:
    raise TypeError("Incorrect type")
except TypeError as ex:
    error_message = get_error_message(ex)
    print(error_message) # Вывод: TypeError: Incorrect type
```

### `Api.get_models`

```python
@staticmethod
def get_models():
    """
    Получает список доступных моделей.

    Returns:
        list: Список словарей, содержащих информацию о моделях.
              Каждый словарь содержит ключи "name" (название модели), "image" (поддержка изображений),
              "vision" (поддержка vision) и "providers" (список провайдеров, поддерживающих модель).
    """
```

**Назначение**: Возвращает список доступных моделей с информацией о поддержке изображений, vision и провайдерах.

**Возвращает**:

- `list`: Список словарей, содержащих информацию о моделях.

**Как работает функция**:

1.  Проходит по всем моделям и провайдерам в `models.__models__.values()`.
2.  Для каждой модели создает словарь с информацией о названии, поддержке изображений и vision.
3.  Собирает список провайдеров, поддерживающих модель.
4.  Возвращает список словарей с информацией о моделях.

**ASCII flowchart**:

```
Models -> Iterate through models -> Create model dictionary -> Collect providers -> Return list of dictionaries
```

**Примеры**:

```python
models = Api.get_models()
print(models)
```

### `Api.get_provider_models`

```python
@staticmethod
def get_provider_models(provider: str, api_key: str = None, api_base: str = None):
    """
    Получает список моделей, доступных для указанного провайдера.

    Args:
        provider (str): Название провайдера.
        api_key (str, optional): API ключ для провайдера. По умолчанию None.
        api_base (str, optional): Базовый URL для API провайдера. По умолчанию None.

    Returns:
        list: Список словарей, содержащих информацию о моделях провайдера.
              Каждый словарь содержит ключи "model" (название модели), "default" (является ли модель моделью по умолчанию),
              "vision" (поддержка vision), "image" (поддержка изображений) и "task" (тип задачи).
    """
```

**Назначение**: Возвращает список моделей, доступных для указанного провайдера, с информацией о поддержке vision, изображений и типе задачи.

**Параметры**:

- `provider` (str): Название провайдера.
- `api_key` (str, optional): API ключ для провайдера. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL для API провайдера. По умолчанию `None`.

**Возвращает**:

- `list`: Список словарей, содержащих информацию о моделях провайдера.

**Как работает функция**:

1.  Проверяет, есть ли провайдер в `ProviderUtils.convert`.
2.  Если провайдер найден и является подклассом `ProviderModelMixin`, получает список моделей провайдера.
3.  Для каждой модели создает словарь с информацией о названии, является ли модель моделью по умолчанию, поддержке vision, изображений и типе задачи.
4.  Возвращает список словарей с информацией о моделях провайдера.

**ASCII flowchart**:

```
Provider -> Check if provider exists -> Get provider models -> Iterate through models -> Create model dictionary -> Return list of dictionaries
```

**Примеры**:

```python
provider_models = Api.get_provider_models("Cohere", api_key="YOUR_API_KEY")
print(provider_models)
```

### `Api.get_providers`

```python
@staticmethod
def get_providers() -> dict[str, str]:
    """
    Получает список доступных провайдеров.

    Returns:
        dict[str, str]: Список словарей, содержащих информацию о провайдерах.
                       Каждый словарь содержит ключи "name" (название провайдера), "label" (отображаемое имя провайдера),
                       "parent" (родительский провайдер), "image" (поддержка изображений), "vision" (поддержка vision),
                       "nodriver" (не требует драйвера), "hf_space" (является HF Space), "auth" (требуется аутентификация) и
                       "login_url" (URL для логина).
    """
```

**Назначение**: Возвращает список доступных провайдеров с информацией о поддержке изображений, vision, аутентификации и других параметрах.

**Возвращает**:

- `dict[str, str]`: Список словарей, содержащих информацию о провайдерах.

**Как работает функция**:

1.  Проходит по всем провайдерам в `__providers__`.
2.  Для каждого провайдера создает словарь с информацией о названии, отображаемом имени, поддержке изображений, vision, аутентификации и других параметрах.
3.  Возвращает список словарей с информацией о провайдерах.

**ASCII flowchart**:

```
Providers -> Iterate through providers -> Create provider dictionary -> Return list of dictionaries
```

**Примеры**:

```python
providers = Api.get_providers()
print(providers)
```

### `Api.get_version`

```python
@staticmethod
def get_version() -> dict:
    """
    Получает информацию о текущей и последней версиях.

    Returns:
        dict: Словарь, содержащий информацию о версиях.
              Ключи: "version" (текущая версия) и "latest_version" (последняя версия).
    """
```

**Назначение**: Возвращает информацию о текущей и последней версиях.

**Возвращает**:

- `dict`: Словарь, содержащий информацию о версиях.

**Как работает функция**:

1.  Пытается получить текущую и последнюю версии из `version.utils`.
2.  В случае ошибки `VersionNotFoundError` устанавливает значения версий в `None`.
3.  Возвращает словарь с информацией о версиях.

**ASCII flowchart**:

```
Try -> Get current version -> Get latest version -> Except VersionNotFoundError -> Set versions to None -> Return dictionary
```

**Примеры**:

```python
version_info = Api.get_version()
print(version_info)
```

### `Api.serve_images`

```python
def serve_images(self, name):
    """
    Возвращает запрошенное изображение из директории изображений.

    Args:
        name (str): Имя файла изображения.

    Returns:
        flask.Response: Ответ Flask с запрошенным изображением.
    """
```

**Назначение**: Возвращает запрошенное изображение из директории изображений.

**Параметры**:

- `name` (str): Имя файла изображения.

**Возвращает**:

- `flask.Response`: Ответ Flask с запрошенным изображением.

**Как работает функция**:

1.  Вызывает функцию `ensure_images_dir()` для обеспечения существования директории изображений.
2.  Использует функцию `send_from_directory` из Flask для отправки файла из директории изображений.

**ASCII flowchart**:

```
Name -> Ensure images directory -> Send file from directory -> Return response
```

**Примеры**:

```python
from flask import Flask

app = Flask(__name__)
api = Api()

@app.route("/images/<name>")
def serve_image(name):
    return api.serve_images(name)

if __name__ == "__main__":
    app.run(debug=True)
```

### `Api._prepare_conversation_kwargs`

```python
def _prepare_conversation_kwargs(self, json_data: dict):
    """
    Подготавливает аргументы для создания разговора.

    Args:
        json_data (dict): JSON данные запроса.

    Returns:
        dict: Словарь с подготовленными аргументами для создания разговора.
    """
```

**Назначение**: Подготавливает аргументы для создания разговора на основе данных JSON-запроса.

**Параметры**:

- `json_data` (dict): JSON данные запроса.

**Возвращает**:

- `dict`: Словарь с подготовленными аргументами для создания разговора.

**Как работает функция**:

1.  Копирует данные из `json_data` в словарь `kwargs`.
2.  Извлекает модель, провайдера и сообщения из `json_data`.
3.  Добавляет `tool_calls` в `kwargs` для `bucket_tool` и `continue_tool` (если `action == "continue"`).
4.  Обрабатывает параметр `conversation`: если это словарь, создает объект `JsonConversation`; если это `conversation_id`, пытается получить существующий разговор из `conversations`.
5.  Возвращает словарь с подготовленными аргументами, включающий модель, провайдера, сообщения и другие параметры.

**ASCII flowchart**:

```
JSON Data -> Extract data -> Add tool_calls -> Handle conversation -> Return kwargs
```

**Примеры**:

```python
json_data = {
    "model": "gemini",
    "provider": "google",
    "messages": [{"role": "user", "content": "Hello"}],
    "action": "continue",
    "conversation_id": "123"
}
kwargs = api._prepare_conversation_kwargs(json_data)
print(kwargs)
```

### `Api._create_response_stream`

```python
def _create_response_stream(self, kwargs: dict, conversation_id: str, provider: str, download_media: bool = True) -> Iterator:
    """
    Создает поток ответов от провайдера.

    Args:
        kwargs (dict): Аргументы для создания разговора.
        conversation_id (str): ID разговора.
        provider (str): Название провайдера.
        download_media (bool, optional): Флаг загрузки медиа. По умолчанию True.

    Yields:
        Iterator: Поток ответов от провайдера в формате JSON.
    """
```

**Назначение**: Создает поток ответов от провайдера, обрабатывая различные типы ответов (сообщения, изображения, логи и т.д.).

**Параметры**:

- `kwargs` (dict): Аргументы для создания разговора.
- `conversation_id` (str): ID разговора.
- `provider` (str): Название провайдера.
- `download_media` (bool, optional): Флаг загрузки медиа. По умолчанию `True`.

**Yields**:

- `Iterator`: Поток ответов от провайдера в формате JSON.

**Как работает функция**:

1.  Определяет функцию `decorated_log` для логирования отладочной информации.
2.  Получает модель и обработчик провайдера с помощью `get_model_and_provider`.
3.  Обрабатывает ответы от провайдера в цикле, используя `iter_run_tools`:
    -   Обрабатывает `ProviderInfo`, `BaseConversation`, `Exception`, `RequestLogin`, `PreviewResponse`, `ImagePreview`, `MediaResponse`, `SynthesizeData`, `TitleGeneration`, `Parameters`, `FinishReason`, `Usage`, `Reasoning`, `YouTube`, `AudioResponse`, `DebugResponse`, `RawResponse`.
    -   Форматирует ответы в JSON с помощью `self._format_json`.
4.  Обрабатывает исключения `MissingAuthError` и `Exception`.
5.  Возвращает логи отладки с помощью `self._yield_logs()`.

**ASCII flowchart**:

```
KWArgs, Conversation ID, Provider -> Decorated Log -> Get Model and Provider -> Try: Iterate through chunks -> Handle chunk types -> Format as JSON -> Yield JSON -> Except MissingAuthError/Exception: Handle error -> Finally: Yield Logs
```

**Примеры**:

```python
kwargs = {
    "model": "gemini",
    "provider": "google",
    "messages": [{"role": "user", "content": "Hello"}]
}
conversation_id = "123"
provider = "google"
stream = api._create_response_stream(kwargs, conversation_id, provider)
for chunk in stream:
    print(chunk)
```

### `Api._yield_logs`

```python
def _yield_logs(self):
    """
    Возвращает логи отладки.

    Yields:
        dict: JSON с логами отладки.
    """
```

**Назначение**: Возвращает логи отладки в формате JSON.

**Yields**:

- `dict`: JSON с логами отладки.

**Как работает функция**:

1.  Проверяет, есть ли логи в `debug.logs`.
2.  Если есть, проходит по всем логам и форматирует их в JSON с помощью `self._format_json`.
3.  Очищает список логов `debug.logs`.

**ASCII flowchart**:

```
Check Debug Logs -> Iterate through Logs -> Format as JSON -> Yield JSON -> Clear Logs
```

**Примеры**:

```python
debug.logs = ["Log message 1", "Log message 2"]
for log in api._yield_logs():
    print(log)
```

### `Api._format_json`

```python
def _format_json(self, response_type: str, content = None, **kwargs):
    """
    Форматирует JSON-ответ.

    Args:
        response_type (str): Тип ответа.
        content (str, optional): Содержимое ответа. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Returns:
        dict: JSON-ответ.
    """
```

**Назначение**: Форматирует JSON-ответ с указанным типом и содержимым.

**Параметры**:

- `response_type` (str): Тип ответа.
- `content` (str, optional): Содержимое ответа. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `dict`: JSON-ответ.

**Как работает функция**:

1.  Создает словарь с ключом `type` и значением `response_type`.
2.  Если `content` не `None`, добавляет ключ `response_type` со значением `content`.
3.  Добавляет дополнительные аргументы из `kwargs`.
4.  Возвращает полученный словарь.

**ASCII flowchart**:

```
Response Type, Content, KWArgs -> Create Dictionary -> Add Content (if exists) -> Add KWArgs -> Return Dictionary
```

**Примеры**:

```python
json_response = api._format_json("message", "Hello", error="None")
print(json_response)  # Вывод: {'type': 'message', 'message': 'Hello', 'error': 'None'}
```

### `Api.handle_provider`

```python
def handle_provider(self, provider_handler, model):
    """
    Обрабатывает провайдера и возвращает информацию о нем.

    Args:
        provider_handler: Обработчик провайдера.
        model: Модель.

    Returns:
        dict: JSON с информацией о провайдере.
    """
```

**Назначение**: Обрабатывает провайдера и возвращает информацию о нем в формате JSON.

**Параметры**:

- `provider_handler`: Обработчик провайдера.
- `model`: Модель.

**Возвращает**:

- `dict`: JSON с информацией о провайдере.

**Как работает функция**:

1.  Проверяет, является ли `provider_handler` экземпляром `BaseRetryProvider` и имеет ли `last_provider`. Если да, использует `last_provider`.
2.  Форматирует информацию о провайдере в JSON с помощью `self._format_json`, включая информацию о модели (если она есть).

**ASCII flowchart**:

```
Provider Handler, Model -> Check Retry Provider -> Format as JSON -> Return JSON
```

**Примеры**:

```python
provider_handler = GoogleProvider()
model = "gemini"
provider_info = api.handle_provider(provider_handler, model)
print(provider_info)