# Модуль api.py для g4f

## Обзор

Модуль `api.py` является частью проекта `hypotez` и предназначен для организации взаимодействия с различными поставщиками (providers) моделей машинного обучения, такими как GPT-4. Он предоставляет API для получения информации о моделях и поставщиках, обработки диалогов и генерации ответов. Модуль использует фреймворк Flask для создания API endpoints.

## Подробнее

В данном модуле реализованы функции для получения списка доступных моделей, информации о поставщиках, а также для обработки запросов на генерацию текста с использованием различных моделей и поставщиков. Он также включает в себя механизм управления диалогами (conversations) и обработки медиа-контента.

## Классы

### `Api`

**Описание**: Класс `Api` предоставляет статические методы для получения информации о моделях и поставщиках, а также методы для обработки запросов и формирования ответов.

**Принцип работы**:
Класс `Api` содержит методы, которые используются для обработки HTTP-запросов, связанных с моделями машинного обучения и поставщиками. Он отвечает за подготовку данных, вызов соответствующих функций для генерации ответов и форматирование результатов в JSON.

**Методы**:
- `get_models`: Возвращает список доступных моделей и их свойств.
- `get_provider_models`: Возвращает список моделей, поддерживаемых указанным поставщиком.
- `get_providers`: Возвращает список доступных поставщиков и их свойств.
- `get_version`: Возвращает информацию о текущей и последней версиях.
- `serve_images`: Возвращает запрошенное изображение из директории с изображениями.
- `_prepare_conversation_kwargs`: Подготавливает аргументы для создания или продолжения диалога.
- `_create_response_stream`: Создает поток ответов от модели, обрабатывая различные типы ответов (текст, изображения, медиа).
- `_yield_logs`: Возвращает логи отладки.
- `_format_json`: Форматирует данные в JSON-ответ.
- `handle_provider`: Форматирует информацию о поставщике в JSON-ответ.

#### `get_models`

```python
@staticmethod
def get_models():
    """Возвращает список доступных моделей и их свойств.

    Args:
        Нет

    Returns:
        list[dict]: Список словарей, где каждый словарь содержит информацию о модели (имя, тип, поставщики).
    """
```

**Как работает функция**:
1. Проходится по всем доступным моделям и их поставщикам, собирая информацию о каждой модели.
2. Для каждой модели создается словарь, содержащий имя модели, тип (изображение или зрение), и список поставщиков, поддерживающих эту модель.
3. Возвращает список этих словарей.

**Пример**:

```python
models = Api.get_models()
print(models)
# [{'name': 'ModelA', 'image': False, 'vision': True, 'providers': ['Provider1', 'Provider2']}, ...]
```

#### `get_provider_models`

```python
@staticmethod
def get_provider_models(provider: str, api_key: str = None, api_base: str = None):
    """Возвращает список моделей, поддерживаемых указанным поставщиком.

    Args:
        provider (str): Имя поставщика.
        api_key (str, optional): API ключ для поставщика. По умолчанию `None`.
        api_base (str, optional): Базовый URL для API поставщика. По умолчанию `None`.

    Returns:
        list[dict]: Список словарей, где каждый словарь содержит информацию о модели, поддерживаемой поставщиком.
    """
```

**Как работает функция**:

1.  Проверяет, есть ли указанный поставщик в списке известных поставщиков.
2.  Если поставщик найден, проверяет, является ли он подклассом `ProviderModelMixin`.
3.  Если поставщик требует API ключ, вызывает метод `get_models` поставщика с API ключом.
4.  Формирует список словарей, содержащих информацию о каждой модели, поддерживаемой поставщиком.
5.  Возвращает этот список.

**Пример**:

```python
models = Api.get_provider_models('Provider1', api_key='test_api_key')
print(models)
# [{'model': 'ModelA', 'default': True, 'vision': False, 'image': True, 'task': None}, ...]
```

#### `get_providers`

```python
@staticmethod
def get_providers() -> dict[str, str]:
    """Возвращает список доступных поставщиков и их свойств.

    Args:
        Нет

    Returns:
        dict[str, str]: Список словарей, где каждый словарь содержит информацию о поставщике (имя, метка, родитель, поддержка изображений/зрения, и т.д.).
    """
```

**Как работает функция**:

1.  Проходится по всем известным поставщикам.
2.  Для каждого поставщика создает словарь, содержащий информацию о его свойствах, таких как имя, метка, родитель, поддержка изображений и зрения, и т.д.
3.  Возвращает список этих словарей.

**Пример**:

```python
providers = Api.get_providers()
print(providers)
# [{'name': 'Provider1', 'label': 'Provider 1', 'parent': None, 'image': True, 'vision': False, 'nodriver': False, 'hf_space': False, 'auth': True, 'login_url': None}, ...]
```

#### `get_version`

```python
@staticmethod
def get_version() -> dict:
    """Возвращает информацию о текущей и последней версиях.

    Args:
        Нет

    Returns:
        dict: Словарь, содержащий информацию о текущей и последней версиях.
    """
```

**Как работает функция**:

1.  Пытается получить текущую и последнюю версии.
2.  Если версии не найдены, перехватывает исключение `VersionNotFoundError`.
3.  Возвращает словарь, содержащий информацию о текущей и последней версиях.

**Пример**:

```python
version_info = Api.get_version()
print(version_info)
# {'version': '1.0.0', 'latest_version': '1.1.0'}
```

#### `serve_images`

```python
def serve_images(self, name):
    """Возвращает запрошенное изображение из директории с изображениями.

    Args:
        name (str): Имя файла изображения.

    Returns:
        Response: HTTP-ответ с изображением.
    """
```

**Как работает функция**:

1.  Обеспечивает существование директории для изображений.
2.  Возвращает изображение из директории с изображениями с использованием `send_from_directory`.

**Пример**:

```python
from flask import Flask

app = Flask(__name__)
api = Api()

@app.route('/images/<name>')
def get_image(name):
    return api.serve_images(name)
```

#### `_prepare_conversation_kwargs`

```python
def _prepare_conversation_kwargs(self, json_data: dict):
    """Подготавливает аргументы для создания или продолжения диалога.

    Args:
        json_data (dict): Словарь с данными запроса.

    Returns:
        dict: Словарь с подготовленными аргументами для создания или продолжения диалога.
    """
```

**Как работает функция**:

1.  Извлекает данные из `json_data`.
2.  Добавляет информацию о `tool_calls`.
3.  Если указано действие "continue", добавляет соответствующую информацию о `tool_calls`.
4.  Подготавливает информацию о диалоге (conversation), если он есть.
5.  Возвращает словарь с подготовленными аргументами.

**Примеры работы функции**:

```python
json_data = {
    "model": "ModelA",
    "provider": "Provider1",
    "messages": [{"role": "user", "content": "Hello"}],
    "action": "continue",
    "conversation_id": "123"
}
kwargs = Api()._prepare_conversation_kwargs(json_data)
print(kwargs)
```

#### `_create_response_stream`

```python
def _create_response_stream(self, kwargs: dict, conversation_id: str, provider: str, download_media: bool = True) -> Iterator:
    """Создает поток ответов от модели, обрабатывая различные типы ответов (текст, изображения, медиа).

    Args:
        kwargs (dict): Словарь с параметрами запроса.
        conversation_id (str): Идентификатор диалога.
        provider (str): Имя поставщика.
        download_media (bool, optional): Флаг, указывающий, нужно ли загружать медиа-контент. По умолчанию `True`.

    Yields:
        Iterator: Поток JSON-ответов.
    """
```

**Как работает функция**:

1.  Устанавливает функцию логирования для отладки.
2.  Получает модель и обработчик поставщика на основе переданных аргументов.
3.  Обрабатывает различные типы ответов, такие как текстовые сообщения, изображения, медиа-контент, запросы на вход, и т.д.
4.  Форматирует ответы в JSON и отправляет их в поток.
5.  Обрабатывает ошибки и исключения, формируя соответствующие JSON-ответы.

    **Внутренние функции**:

    `decorated_log`
    ```python
    def decorated_log(text: str, file = None):
        """Декорирует функцию логирования для добавления отладочной информации.

        Args:
            text (str): Текст сообщения для логирования.
            file (File, optional): Файл для логирования. По умолчанию `None`.
        """
    ```

**Пример**:

```python
kwargs = {
    "model": "ModelA",
    "provider": "Provider1",
    "messages": [{"role": "user", "content": "Hello"}],
    "stream": True,
    "ignore_stream": True
}
stream = Api()._create_response_stream(kwargs, "123", "Provider1")
for response in stream:
    print(response)
```

#### `_yield_logs`

```python
def _yield_logs(self):
    """Возвращает логи отладки.

    Yields:
        dict: JSON-ответ с логами отладки.
    """
```

**Как работает функция**:

1.  Проверяет, есть ли логи отладки.
2.  Если логи есть, отправляет каждый лог в виде JSON-ответа в поток.
3.  Очищает список логов.

**Пример**:

```python
stream = Api()._yield_logs()
for log in stream:
    print(log)
```

#### `_format_json`

```python
def _format_json(self, response_type: str, content = None, **kwargs):
    """Форматирует данные в JSON-ответ.

    Args:
        response_type (str): Тип ответа.
        content (Any, optional): Содержимое ответа. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        dict: JSON-ответ.
    """
```

**Как работает функция**:

1.  Формирует словарь, содержащий тип ответа и содержимое (если есть).
2.  Добавляет дополнительные аргументы в словарь.
3.  Возвращает JSON-ответ.

**Примеры**:

```python
json_response = Api()._format_json("content", "Hello")
print(json_response)
# {'type': 'content', 'content': 'Hello'}

json_response = Api()._format_json("error", message="Something went wrong", error_code=500)
print(json_response)
# {'type': 'error', 'message': 'Something went wrong', 'error_code': 500}
```

#### `handle_provider`

```python
def handle_provider(self, provider_handler, model):
    """Форматирует информацию о поставщике в JSON-ответ.

    Args:
        provider_handler (BaseRetryProvider): Обработчик поставщика.
        model (str): Имя модели.

    Returns:
        dict: JSON-ответ с информацией о поставщике.
    """
```

**Как работает функция**:

1.  Если обработчик поставщика является экземпляром `BaseRetryProvider`, использует последний использованный поставщик.
2.  Формирует JSON-ответ, содержащий информацию о поставщике и модели (если есть).
3.  Возвращает JSON-ответ.

**Примеры**:

```python
class MockProvider:
    def get_dict(self):
        return {"name": "MockProvider"}

provider = MockProvider()
json_response = Api().handle_provider(provider, "ModelA")
print(json_response)
# {'type': 'provider', 'provider': {'name': 'MockProvider', 'model': 'ModelA'}}
```

## Функции

### `get_error_message`

```python
def get_error_message(exception: Exception) -> str:
    """Получает сообщение об ошибке из исключения.

    Args:
        exception (Exception): Исключение.

    Returns:
        str: Сообщение об ошибке.
    """
```

**Как работает функция**:
1.  Форматирует сообщение об ошибке, включая имя типа исключения и текст исключения.
2.  Возвращает сообщение об ошибке.

**Примеры**:

```python
try:
    raise ValueError("Invalid value")
except ValueError as ex:
    message = get_error_message(ex)
    print(message)
    # ValueError: Invalid value
```