# Модуль для работы с API

## Обзор

Модуль `api.py` предоставляет API для взаимодействия с различными моделями и провайдерами, используемыми в проекте. Он включает в себя функции для получения списка моделей, провайдеров, версий, а также для обработки разговоров и создания потоков ответов.

## Подробнее

Этот модуль является центральным звеном для обработки запросов к API, предоставляя интерфейс для получения информации о доступных моделях и провайдерах, а также для управления ходом разговоров с использованием этих моделей.

## Классы

### `Api`

**Описание**: Класс `Api` предоставляет статические методы для получения информации о моделях, провайдерах и версиях, а также методы для обработки запросов к API и создания потоков ответов.

**Методы**:

- `get_models()`:
- `get_provider_models(provider: str, api_key: str = None, api_base: str = None)`:
- `get_providers()`:
- `get_version()`:
- `serve_images(name)`:
- `_prepare_conversation_kwargs(json_data: dict)`:
- `_create_response_stream(self, kwargs: dict, conversation_id: str, provider: str, download_media: bool = True)`:
- `_yield_logs()`:
- `_format_json(response_type: str, content = None, **kwargs)`:
- `handle_provider(provider_handler, model)`:

## Функции

### `get_models`

```python
    @staticmethod
    def get_models():
        return [{
            "name": model.name,
            "image": isinstance(model, models.ImageModel),
            "vision": isinstance(model, models.VisionModel),
            "providers": [
                getattr(provider, "parent", provider.__name__)
                for provider in providers
                if provider.working
            ]
        }
        for model, providers in models.__models__.values()]
```

**Назначение**: Возвращает список доступных моделей с информацией об их поддержке изображений, vision и провайдерах.

**Параметры**:
- Нет.

**Возвращает**:
- `list[dict]`: Список словарей, где каждый словарь содержит информацию о модели, включая её имя, поддержку изображений и vision, а также список провайдеров.

**Как работает функция**:
1. Функция `get_models` перебирает значения из `models.__models__.values()`.
2. Для каждой модели создает словарь, содержащий:
   - `'name'`: Имя модели.
   - `'image'`: `True`, если модель поддерживает изображения (`isinstance(model, models.ImageModel)`), иначе `False`.
   - `'vision'`: `True`, если модель поддерживает vision (`isinstance(model, models.VisionModel)`), иначе `False`.
   - `'providers'`: Список провайдеров, поддерживающих данную модель. Провайдеры берутся из атрибута `parent` или `__name__` каждого провайдера, если провайдер рабочий (`provider.working`).
3. Возвращает список этих словарей.

```
Начало
   │
   │ Перебор моделей из models.__models__.values()
   │
   └───> Для каждой модели:
         │
         │ Создание словаря с информацией о модели
         │
         ├───> name: model.name
         │
         ├───> image: isinstance(model, models.ImageModel)
         │
         ├───> vision: isinstance(model, models.VisionModel)
         │
         └───> providers: Список провайдеров, поддерживающих модель
         │
         │ Добавление словаря в список
         │
   │
   └───> Возврат списка словарей
   │
Конец
```

**Примеры**:

```python
result = Api.get_models()
print(result)
#  [{'name': 'gpt-3.5-turbo', 'image': False, 'vision': False, 'providers': ['OpenAI']}, {'name': 'gemini-pro', 'image': False, 'vision': False, 'providers': ['Google']}]
```

### `get_provider_models`

```python
    @staticmethod
    def get_provider_models(provider: str, api_key: str = None, api_base: str = None):
        if provider in ProviderUtils.convert:
            provider = ProviderUtils.convert[provider]
            if issubclass(provider, ProviderModelMixin):
                if "api_key" in signature(provider.get_models).parameters:
                    models = provider.get_models(api_key=api_key, api_base=api_base)
                else:
                    models = provider.get_models()
                return [
                    {
                        "model": model,
                        "default": model == provider.default_model,
                        "vision": getattr(provider, "default_vision_model", None) == model or model in getattr(provider, "vision_models", []),
                        "image": False if provider.image_models is None else model in provider.image_models,
                        "task": None if not hasattr(provider, "task_mapping") else provider.task_mapping[model] if model in provider.task_mapping else None
                    }
                    for model in models
                ]
        return []
```

**Назначение**: Возвращает список моделей, поддерживаемых указанным провайдером.

**Параметры**:
- `provider` (str): Имя провайдера.
- `api_key` (str, optional): API ключ для провайдера. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL для API провайдера. По умолчанию `None`.

**Возвращает**:
- `list[dict]`: Список словарей, где каждый словарь содержит информацию о модели, включая её имя, является ли она моделью по умолчанию, поддерживает ли она vision и изображения.

**Как работает функция**:

1. Функция `get_provider_models` принимает имя провайдера, API-ключ и базовый URL.
2. Проверяет, есть ли провайдер в `ProviderUtils.convert` и получает соответствующий класс провайдера.
3. Проверяет, является ли класс провайдера подклассом `ProviderModelMixin`.
4. Если провайдер требует API-ключ (проверяется через сигнатуру метода `get_models`), вызывает `provider.get_models` с API-ключом и базовым URL. В противном случае вызывает `provider.get_models` без параметров.
5. Формирует список словарей, содержащих информацию о каждой модели, включая:
   - `'model'`: Имя модели.
   - `'default'`: `True`, если модель является моделью по умолчанию для провайдера, иначе `False`.
   - `'vision'`: `True`, если модель поддерживает vision (является моделью `default_vision_model` или находится в списке `vision_models`), иначе `False`.
   - `'image'`: `True`, если модель находится в списке `image_models`, иначе `False`.
   - `'task'`: Соответствующая задача из `task_mapping`, если она определена для модели.
6. Возвращает список этих словарей.

```
Начало
   │
   │ Проверка наличия провайдера в ProviderUtils.convert
   │
   ├───> Если провайдер найден:
   │     │
   │     │ Проверка, является ли провайдер подклассом ProviderModelMixin
   │     │
   │     ├───> Если является:
   │     │   │
   │     │   │ Проверка наличия api_key в параметрах get_models
   │     │   │
   │     │   ├───> Если api_key требуется:
   │     │   │   │
   │     │   │   │ Вызов provider.get_models с api_key и api_base
   │     │   │   │
   │     │   ├───> Иначе:
   │     │   │   │
   │     │   │   │ Вызов provider.get_models без параметров
   │     │   │   │
   │     │   │   │
   │     │   │   │ Формирование списка словарей с информацией о каждой модели
   │     │   │   │
   │     │   │   │ Возврат списка словарей
   │     │   │   │
   │     │   └───>
   │     │
   │     └───>
   │
   └───> Возврат пустого списка
   │
Конец
```

**Примеры**:

```python
result = Api.get_provider_models(provider='OpenAI', api_key='test_key')
print(result)
#  [{'model': 'gpt-3.5-turbo', 'default': True, 'vision': False, 'image': False, 'task': None}]
```

### `get_providers`

```python
    @staticmethod
    def get_providers() -> dict[str, str]:
        return [{\n            "name": provider.__name__,\n            "label": provider.label if hasattr(provider, "label") else provider.__name__,\n            "parent": getattr(provider, "parent", None),\n            "image": bool(getattr(provider, "image_models", False)),\n            "vision": getattr(provider, "default_vision_model", None) is not None,\n            "nodriver": getattr(provider, "use_nodriver", False),\n            "hf_space": getattr(provider, "hf_space", False),\n            "auth": provider.needs_auth,\n            "login_url": getattr(provider, "login_url", None),\n        } for provider in __providers__ if provider.working]
```

**Назначение**: Возвращает список доступных провайдеров с информацией об их поддержке изображений, vision, необходимости авторизации и т.д.

**Параметры**:
- Нет.

**Возвращает**:
- `dict[str, str]`: Список словарей, где каждый словарь содержит информацию о провайдере, включая его имя, метку, поддержку изображений и vision, необходимость авторизации и т.д.

**Как работает функция**:
1. Функция `get_providers` перебирает провайдеров из `__providers__`.
2. Для каждого провайдера, который является рабочим (`provider.working`), создает словарь, содержащий:
   - `'name'`: Имя провайдера (`provider.__name__`).
   - `'label'`: Метка провайдера (`provider.label`), если она определена, иначе имя провайдера.
   - `'parent'`: Родительский провайдер (`getattr(provider, "parent", None)`), если он есть.
   - `'image'`: `True`, если провайдер поддерживает изображения (`bool(getattr(provider, "image_models", False))`), иначе `False`.
   - `'vision'`: `True`, если провайдер поддерживает vision (`getattr(provider, "default_vision_model", None) is not None`), иначе `False`.
   - `'nodriver'`: Значение атрибута `use_nodriver` провайдера.
   - `'hf_space'`: Значение атрибута `hf_space` провайдера.
   - `'auth'`: Значение атрибута `needs_auth` провайдера.
   - `'login_url'`: URL для логина (`getattr(provider, "login_url", None)`), если он есть.
3. Возвращает список этих словарей.

```
Начало
   │
   │ Перебор провайдеров из __providers__
   │
   └───> Для каждого провайдера, который является рабочим:
         │
         │ Создание словаря с информацией о провайдере
         │
         ├───> name: provider.__name__
         │
         ├───> label: provider.label или provider.__name__
         │
         ├───> parent: getattr(provider, "parent", None)
         │
         ├───> image: bool(getattr(provider, "image_models", False))
         │
         ├───> vision: getattr(provider, "default_vision_model", None) is not None
         │
         ├───> nodriver: getattr(provider, "use_nodriver", False)
         │
         ├───> hf_space: getattr(provider, "hf_space", False)
         │
         ├───> auth: provider.needs_auth
         │
         └───> login_url: getattr(provider, "login_url", None)
         │
         │ Добавление словаря в список
         │
   │
   └───> Возврат списка словарей
   │
Конец
```

**Примеры**:

```python
result = Api.get_providers()
print(result)
#  [{'name': 'OpenAI', 'label': 'OpenAI', 'parent': None, 'image': False, 'vision': False, 'nodriver': False, 'hf_space': False, 'auth': True, 'login_url': None}, {'name': 'Google', 'label': 'Google', 'parent': None, 'image': False, 'vision': False, 'nodriver': False, 'hf_space': False, 'auth': True, 'login_url': None}]
```

### `get_version`

```python
    @staticmethod
    def get_version() -> dict:
        current_version = None
        latest_version = None
        try:
            current_version = version.utils.current_version
            latest_version = version.utils.latest_version
        except VersionNotFoundError:
            pass
        return {
            "version": current_version,
            "latest_version": latest_version,
        }
```

**Назначение**: Возвращает текущую и последнюю доступные версии.

**Параметры**:
- Нет.

**Возвращает**:
- `dict`: Словарь, содержащий текущую и последнюю доступные версии.

**Как работает функция**:
1. Функция `get_version` пытается получить текущую и последнюю версии из `version.utils`.
2. Если возникает исключение `VersionNotFoundError`, оно игнорируется.
3. Возвращает словарь с ключами `"version"` и `"latest_version"`, содержащими соответствующие значения.

```
Начало
   │
   │ Попытка получить current_version и latest_version из version.utils
   │
   ├───> Если VersionNotFoundError:
   │     │
   │     │ Игнорирование исключения
   │     │
   │     └───>
   │
   │
   │ Создание словаря с current_version и latest_version
   │
   │ Возврат словаря
   │
Конец
```

**Примеры**:

```python
result = Api.get_version()
print(result)
#  {'version': '1.0.0', 'latest_version': '1.0.1'}
```

### `serve_images`

```python
    def serve_images(self, name):
        ensure_images_dir()
        return send_from_directory(os.path.abspath(images_dir), name)
```

**Назначение**: Обслуживает статические изображения из указанной директории.

**Параметры**:
- `name` (str): Имя файла изображения.

**Возвращает**:
- `Response`: Ответ Flask, содержащий запрошенное изображение.

**Как работает функция**:
1. Функция `serve_images` принимает имя файла изображения.
2. Вызывает `ensure_images_dir()`, чтобы убедиться, что директория для изображений существует.
3. Использует `send_from_directory` для отправки файла из директории `images_dir`.

```
Начало
   │
   │ Вызов ensure_images_dir()
   │
   │ Использование send_from_directory для отправки файла
   │
Конец
```

**Примеры**:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/images/<name>")
def serve_image(name):
    api = Api()
    return api.serve_images(name)

if __name__ == '__main__':
    app.run(debug=True)
```

### `_prepare_conversation_kwargs`

```python
    def _prepare_conversation_kwargs(self, json_data: dict):
        kwargs = {**json_data}
        model = json_data.get('model')
        provider = json_data.get('provider')
        messages = json_data.get('messages')
        kwargs["tool_calls"] = [{\n            "function": {\n                "name": "bucket_tool"\n            },\n            "type": "function"\n        }]
        action = json_data.get('action')
        if action == "continue":
            kwargs["tool_calls"].append({\n                "function": {\n                    "name": "continue_tool"\n                },\n                "type": "function"\n            })
        conversation = json_data.get("conversation")
        if isinstance(conversation, dict):
            kwargs["conversation"] = JsonConversation(**conversation)
        else:
            conversation_id = json_data.get("conversation_id")
            if conversation_id and provider:
                if provider in conversations and conversation_id in conversations[provider]:
                    kwargs["conversation"] = conversations[provider][conversation_id]
        return {\n            "model": model,\n            "provider": provider,\n            "messages": messages,\n            "stream": True,\n            "ignore_stream": True,\n            "return_conversation": True,\n            **kwargs\n        }
```

**Назначение**: Подготавливает аргументы для начала или продолжения разговора, включая информацию о модели, провайдере, сообщениях и инструментах.

**Параметры**:
- `json_data` (dict): Словарь с данными запроса.

**Возвращает**:
- `dict`: Словарь, содержащий аргументы для создания или продолжения разговора.

**Как работает функция**:

1. Функция `_prepare_conversation_kwargs` принимает словарь `json_data` с данными запроса.
2. Создает копию `json_data` в словаре `kwargs`.
3. Извлекает значения `model`, `provider` и `messages` из `json_data`.
4. Добавляет информацию об инструментах (`tool_calls`) в `kwargs`. Инструменты включают `bucket_tool` и, если `action` равно `"continue"`, `continue_tool`.
5. Обрабатывает информацию о разговоре (`conversation`):
   - Если `conversation` является словарем, создает экземпляр `JsonConversation` на основе этого словаря и добавляет его в `kwargs`.
   - Иначе, если есть `conversation_id` и `provider`, пытается найти существующий разговор в словаре `conversations` и добавить его в `kwargs`.
6. Возвращает словарь, содержащий `model`, `provider`, `messages`, информацию о стриминге (`stream`, `ignore_stream`), флаг возврата разговора (`return_conversation`) и все остальные аргументы из `kwargs`.

```
Начало
   │
   │ Создание копии json_data в kwargs
   │
   │ Извлечение model, provider и messages из json_data
   │
   │ Добавление информации об инструментах (tool_calls) в kwargs
   │
   │ Обработка информации о разговоре (conversation)
   │
   ├───> Если conversation - словарь:
   │     │
   │     │ Создание экземпляра JsonConversation и добавление в kwargs
   │     │
   ├───> Иначе:
   │     │
   │     │ Если есть conversation_id и provider:
   │     │
   │     │ Поиск существующего разговора в conversations и добавление в kwargs
   │     │
   │     └───>
   │
   │
   │ Возврат словаря с аргументами для создания/продолжения разговора
   │
Конец
```

**Примеры**:

```python
data = {
    "model": "gpt-3.5-turbo",
    "provider": "OpenAI",
    "messages": [{"role": "user", "content": "Hello"}],
    "action": "continue",
    "conversation_id": "123"
}

api = Api()
kwargs = api._prepare_conversation_kwargs(data)
print(kwargs)
```

### `_create_response_stream`

```python
    def _create_response_stream(self, kwargs: dict, conversation_id: str, provider: str, download_media: bool = True) -> Iterator:
        def decorated_log(text: str, file = None):
            debug.logs.append(text)
            if debug.logging:
                debug.log_handler(text, file=file)
        debug.log = decorated_log
        proxy = os.environ.get("G4F_PROXY")
        provider = kwargs.get("provider")
        try:
            model, provider_handler = get_model_and_provider(\
                kwargs.get("model"), provider,\
                stream=True,\
                ignore_stream=True,\
                logging=False,\
                has_images="media" in kwargs,\
            )
        except Exception as e:
            debug.error(e)
            yield self._format_json(\'error\', type(e).__name__, message=get_error_message(e))
            return
        if not isinstance(provider_handler, BaseRetryProvider):\n            if not provider:\n                provider = provider_handler.__name__\n            yield self.handle_provider(provider_handler, model)\n            if hasattr(provider_handler, "get_parameters"):\n                yield self._format_json("parameters", provider_handler.get_parameters(as_json=True))\n        try:\n            result = iter_run_tools(ChatCompletion.create, **{**kwargs, "model": model, "provider": provider_handler, "download_media": download_media})\n            for chunk in result:\n                if isinstance(chunk, ProviderInfo):\n                    yield self.handle_provider(chunk, model)\n                    provider = chunk.name\n                elif isinstance(chunk, BaseConversation):\n                    if provider is not None:\n                        if hasattr(provider, "__name__"):\n                            provider = provider.__name__\n                        if provider not in conversations:\n                            conversations[provider] = {}\n                        conversations[provider][conversation_id] = chunk\n                        if isinstance(chunk, JsonConversation):\n                            yield self._format_json("conversation", {\n                                provider: chunk.get_dict()\n                            })\n                        else:\n                            yield self._format_json("conversation_id", conversation_id)\n                elif isinstance(chunk, Exception):\n                    logger.exception(chunk)\n                    debug.error(chunk)\n                    yield self._format_json(\'message\', get_error_message(chunk), error=type(chunk).__name__)\n                elif isinstance(chunk, RequestLogin):\n                    yield self._format_json("preview", chunk.to_string())\n                elif isinstance(chunk, PreviewResponse):\n                    yield self._format_json("preview", chunk.to_string())\n                elif isinstance(chunk, ImagePreview):\n                    yield self._format_json("preview", chunk.to_string(), urls=chunk.urls, alt=chunk.alt)\n                elif isinstance(chunk, MediaResponse):\n                    media = chunk\n                    if download_media or chunk.get("cookies"):\n                        chunk.alt = format_image_prompt(kwargs.get("messages"), chunk.alt)\n                        tags = [model, kwargs.get("aspect_ratio"), kwargs.get("resolution"), kwargs.get("width"), kwargs.get("height")]\n                        media = asyncio.run(copy_media(chunk.get_list(), chunk.get("cookies"), chunk.get("headers"), proxy=proxy, alt=chunk.alt, tags=tags))\n                        media = ImageResponse(media, chunk.alt) if isinstance(chunk, ImageResponse) else VideoResponse(media, chunk.alt)\n                    yield self._format_json("content", str(media), urls=chunk.urls, alt=chunk.alt)\n                elif isinstance(chunk, SynthesizeData):\n                    yield self._format_json("synthesize", chunk.get_dict())\n                elif isinstance(chunk, TitleGeneration):\n                    yield self._format_json("title", chunk.title)\n                elif isinstance(chunk, RequestLogin):\n                    yield self._format_json("login", str(chunk))\n                elif isinstance(chunk, Parameters):\n                    yield self._format_json("parameters", chunk.get_dict())\n                elif isinstance(chunk, FinishReason):\n                    yield self._format_json("finish", chunk.get_dict())\n                elif isinstance(chunk, Usage):\n                    yield self._format_json("usage", chunk.get_dict())\n                elif isinstance(chunk, Reasoning):\n                    yield self._format_json("reasoning", **chunk.get_dict())\n                elif isinstance(chunk, YouTube):\n                    yield self._format_json("content", chunk.to_string())\n                elif isinstance(chunk, AudioResponse):\n                    yield self._format_json("content", str(chunk))\n                elif isinstance(chunk, DebugResponse):\n                    yield self._format_json("log", chunk.log)\n                elif isinstance(chunk, RawResponse):\n                    yield self._format_json(chunk.type, **chunk.get_dict())\n                else:\n                    yield self._format_json("content", str(chunk))\n        except MissingAuthError as e:\n            yield self._format_json(\'auth\', type(e).__name__, message=get_error_message(e))\n        except Exception as e:\n            logger.exception(e)\n            debug.error(e)\n            yield self._format_json(\'error\', type(e).__name__, message=get_error_message(e))\n        finally:\n            yield from self._yield_logs()\n```

**Назначение**: Создает поток ответов от модели, обрабатывая различные типы ответов, такие как текст, изображения, логи, и информацию о провайдере.

**Параметры**:
- `kwargs` (dict): Словарь с аргументами для запроса к модели.
- `conversation_id` (str): Идентификатор разговора.
- `provider` (str): Имя провайдера.
- `download_media` (bool): Флаг, указывающий, нужно ли скачивать медиафайлы. По умолчанию `True`.

**Возвращает**:
- `Iterator`: Итератор, генерирующий словари в формате JSON с различными типами ответов.

**Как работает функция**:

1.  Функция `_create_response_stream` принимает аргументы для запроса к модели, идентификатор разговора, имя провайдера и флаг скачивания медиафайлов.
2.  Определяет внутреннюю функцию `decorated_log` для логирования отладочной информации.
3.  Получает прокси из переменной окружения `G4F_PROXY`.
4.  Пытается получить модель и обработчик провайдера с помощью `get_model_and_provider`.
5.  Если возникает исключение при получении модели или провайдера, генерирует сообщение об ошибке.
6.  Если обработчик провайдера не является экземпляром `BaseRetryProvider`, генерирует информацию о провайдере и его параметрах.
7.  Вызывает `iter_run_tools` для выполнения запроса к модели.
8.  Перебирает результаты, возвращаемые `iter_run_tools`, и обрабатывает различные типы ответов:
    *   `ProviderInfo`: Генерирует информацию о провайдере.
    *   `BaseConversation`: Сохраняет информацию о разговоре и генерирует идентификатор разговора или словарь с информацией о разговоре.
    *   `Exception`: Генерирует сообщение об ошибке.
    *   `RequestLogin`, `PreviewResponse`, `ImagePreview`: Генерирует превью.
    *   `MediaResponse`: Скачивает медиафайлы (если `download_media` равно `True`) и генерирует URL медиафайлов.
    *   `SynthesizeData`, `TitleGeneration`, `Parameters`, `FinishReason`, `Usage`, `Reasoning`, `YouTube`, `AudioResponse`, `DebugResponse`, `RawResponse`: Генерирует соответствующие данные.
    *   По умолчанию генерирует контент ответа.
9.  Обрабатывает исключения `MissingAuthError` и `Exception`, генерируя соответствующие сообщения об ошибках.
10. В блоке `finally` генерирует логи.

```
Начало
   │
   │ Определение внутренней функции decorated_log для логирования
   │
   │ Получение прокси из переменной окружения G4F_PROXY
   │
   │ Попытка получить модель и обработчик провайдера с помощью get_model_and_provider
   │
   ├───> Если возникает исключение:
   │     │
   │     │ Генерация сообщения об ошибке
   │     │
   │     └───>
   │
   │
   │ Если обработчик провайдера не является экземпляром BaseRetryProvider:
   │
   │ Генерация информации о провайдере и его параметрах
   │
   │ Вызов iter_run_tools для выполнения запроса к модели
   │
   │ Перебор результатов, возвращаемых iter_run_tools, и обработка различных типов ответов
   │
   │ Обработка исключений MissingAuthError и Exception, генерация соответствующих сообщений об ошибках
   │
   │ В блоке finally генерация логов
   │
Конец
```

**Примеры**:

```python
kwargs = {
    "model": "gpt-3.5-turbo",
    "provider": "OpenAI",
    "messages": [{"role": "user", "content": "Hello"}]
}

api = Api()
response_stream = api._create_response_stream(kwargs, "123", "OpenAI")
for chunk in response_stream:
    print(chunk)
```

### `_yield_logs`

```python
    def _yield_logs(self):
        if debug.logs:
            for log in debug.logs:
                yield self._format_json("log", log)
            debug.logs = []
```

**Назначение**: Генерирует логи из списка `debug.logs` и очищает его.

**Параметры**:
- Нет.

**Возвращает**:
- `Iterator`: Итератор, генерирующий словари в формате JSON с логами.

**Как работает функция**:
1. Функция `_yield_logs` проверяет, есть ли логи в списке `debug.logs`.
2. Если логи есть, она перебирает их и генерирует каждый лог в формате JSON с типом `"log"`.
3. После генерации всех логов, список `debug.logs` очищается.

```
Начало
   │
   │ Проверка наличия логов в списке debug.logs
   │
   ├───> Если логи есть:
   │     │
   │     │ Перебор логов
   │     │
   │     │ Генерация каждого лога в формате JSON с типом "log"
   │     │
   │     │ Очистка списка debug.logs
   │     │
   │     └───>
   │
Конец
```

**Примеры**:

```python
debug.logs = ["Log message 1", "Log message 2"]
api = Api()
logs = list(api._yield_logs())
print(logs)
# Вывод:
# [{'type': 'log', 'log': 'Log message 1'}, {'type': 'log', 'log': 'Log message 2'}]
print(debug.logs)
# Вывод:
# []
```

### `_format_json`

```python
    def _format_json(self, response_type: str, content = None, **kwargs):
        if content is not None and isinstance(response_type, str):
            return {\n                \'type\': response_type,\n                response_type: content,\n                **kwargs\n            }
        return {\n            \'type\': response_type,\n            **kwargs\n        }
```

**Назначение**: Форматирует данные в JSON-формат для отправки в качестве ответа.

**Параметры**:
- `response_type` (str): Тип ответа.
- `content` (Any, optional): Содержимое ответа. По умолчанию `None`.
- `kwargs` (dict, optional): Дополнительные аргументы.

**Возвращает**:
- `dict`: Словарь в формате JSON.

**Как работает функция**:
1. Функция `_format_json` принимает тип ответа, содержимое и дополнительные аргументы.
2. Если содержимое не равно `None` и тип ответа является строкой, она возвращает словарь, содержащий ключи `'type'` (тип ответа), ключ с именем типа ответа (содержимое) и все дополнительные аргументы.
3. В противном случае она возвращает словарь, содержащий только ключ `'type'` (тип ответа) и дополнительные аргументы.

```
Начало
   │
   │ Проверка, что content не None и response_type - строка
   │
   ├───> Если да:
   │     │
   │     │ Форматирование JSON с полями type, response_type и kwargs
   │     │
   │     └───>
   │
   │
   │ Форматирование JSON с полями type и kwargs
   │
   │ Возврат JSON
   │
Конец
```

**Примеры**:

```python
api = Api()
json1 = api._format_json("content", "Hello, world!")
print(json1)
# Вывод:
# {'type': 'content', 'content': 'Hello, world!'}

json2 = api._format_json("error", message="Something went wrong", code=500)
print(json2)
# Вывод:
# {'type': 'error', 'error': None, 'message': 'Something went wrong', 'code': 500}
```

### `handle_provider`

```python
    def handle_provider(self, provider_handler, model):
        if isinstance(provider_handler, BaseRetryProvider) and provider_handler.last_provider is not None:\n            provider_handler = provider_handler.last_provider
        if model:\n            return self._format_json("provider", {**provider_handler.get_dict(), "model": model})\n        return self._format_json("provider", provider_handler.get_dict())
```

**Назначение**: Форматирует информацию о провайдере в JSON-формат.

**Параметры**:
- `provider_handler` (object): Обработчик провайдера.
- `model` (str, optional): Имя модели. По умолчанию `None`.

**Возвращает**:
- `dict`: Словарь в формате JSON с информацией о провайдере.

**Как работает функция**:
1. Функция `handle_provider` принимает обработчик провайдера и имя модели (необязательный параметр).
2. Если обработ