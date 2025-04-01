# Модуль для работы с Gemini Pro API от Google
## Обзор

Модуль `GeminiPro.py` предоставляет асинхронный интерфейс для взаимодействия с API Google Gemini Pro. Он позволяет генерировать текст на основе предоставленных сообщений, поддерживая потоковую передачу данных, системные сообщения и мультимедийные вложения. Модуль включает в себя функциональность для обработки аутентификации, управления моделями и обработки ошибок API.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для использования в качестве одного из провайдеров API для генерации текста. Он интегрируется с другими компонентами проекта, такими как `AsyncGeneratorProvider`, `ProviderModelMixin`, `MediaListType`, `Usage`, `FinishReason` и другими.

## Классы

### `GeminiPro`

**Описание**: Класс `GeminiPro` предоставляет асинхронный генератор для взаимодействия с API Google Gemini Pro. Он поддерживает потоковую генерацию текста, передачу системных сообщений и обработку мультимедийных данных.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для управления моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, "Google Gemini API".
- `url` (str): URL главной страницы Google AI, "https://ai.google.dev".
- `login_url` (str): URL для получения API ключа, "https://aistudio.google.com/u/0/apikey".
- `api_base` (str): Базовый URL API, "https://generativelanguage.googleapis.com/v1beta".
- `working` (bool): Указывает, что провайдер в рабочем состоянии.
- `supports_message_history` (bool): Указывает на поддержку истории сообщений.
- `supports_system_message` (bool): Указывает на поддержку системных сообщений.
- `needs_auth` (bool): Указывает на необходимость аутентификации.
- `default_model` (str): Модель по умолчанию, "gemini-1.5-pro".
- `default_vision_model` (str): Модель по умолчанию для обработки изображений, "gemini-1.5-pro".
- `fallback_models` (list[str]): Список резервных моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

### `get_models`

```python
    @classmethod
    def get_models(cls, api_key: str = None, api_base: str = api_base) -> list[str]:
        """Получает список доступных моделей из API Google Gemini.

        Args:
            api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
            api_base (str, optional): Базовый URL API. По умолчанию `api_base`.

        Returns:
            list[str]: Список доступных моделей.

        Raises:
            MissingAuthError: Если `api_key` недействителен.

        Пример:
            >>> GeminiPro.get_models(api_key='YOUR_API_KEY')
            ['gemini-1.5-pro', 'gemini-pro', ...]
        """
```

**Назначение**: Получение списка доступных моделей из API Google Gemini.

**Параметры**:
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API. По умолчанию `api_base`.

**Возвращает**:
- `list[str]`: Список доступных моделей.

**Вызывает исключения**:
- `MissingAuthError`: Если `api_key` недействителен.

**Как работает функция**:
1. Проверяет, был ли уже получен список моделей (хранится в `cls.models`).
2. Если список моделей не был получен, функция пытается получить его из API.
3. Формирует URL для запроса списка моделей.
4. Отправляет GET-запрос к API с использованием `requests`.
5. Обрабатывает ответ, извлекая имена моделей, поддерживающих метод `generateContent`.
6. Сортирует список моделей.
7. В случае ошибки (например, недействительный API-ключ) перехватывает исключение и возвращает список резервных моделей.

**ASCII flowchart**:

```
A [Проверка наличия cls.models]
|
B [Формирование URL]
|
C [Отправка GET запроса]
|
D [Обработка ответа и извлечение моделей]
|
E [Сортировка моделей]
|
F [Обработка исключений]
```

**Примеры**:
```python
models = GeminiPro.get_models(api_key="YOUR_API_KEY")
print(models)
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = False,
        proxy: str = None,
        api_key: str = None,
        api_base: str = api_base,
        use_auth_header: bool = False,
        media: MediaListType = None,
        tools: Optional[list] = None,
        connector: BaseConnector = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для взаимодействия с API Google Gemini.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки в API.
            stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            api_key (str, optional): API ключ для аутентификации. По умолчанию `None`.
            api_base (str, optional): Базовый URL API. По умолчанию `api_base`.
            use_auth_header (bool, optional): Флаг, указывающий, использовать ли заголовок авторизации. По умолчанию `False`.
            media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
            tools (Optional[list], optional): Список инструментов (функций) для использования. По умолчанию `None`.
            connector (BaseConnector, optional): AIOHTTP коннектор. По умолчанию `None`.
            **kwargs: Дополнительные параметры для передачи в API.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов от API.

        Raises:
            MissingAuthError: Если отсутствует `api_key`.
            RuntimeError: Если API возвращает ошибку.

        Пример:
            >>> async for chunk in GeminiPro.create_async_generator(model='gemini-pro', messages=[{'role': 'user', 'content': 'Hello'}], api_key='YOUR_API_KEY'):
            ...     print(chunk)
        """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API Google Gemini.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `api_base` (str, optional): Базовый URL API. По умолчанию `api_base`.
- `use_auth_header` (bool, optional): Флаг, указывающий, использовать ли заголовок авторизации. По умолчанию `False`.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `tools (Optional[list], optional)`: Список инструментов (функций) для использования. По умолчанию `None`.
- `connector` (BaseConnector, optional): AIOHTTP коннектор. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры для передачи в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует `api_key`.
- `RuntimeError`: Если API возвращает ошибку.

**Как работает функция**:

1. Проверяет наличие `api_key`. Если ключ отсутствует, выбрасывает исключение `MissingAuthError`.
2. Получает имя модели с помощью `cls.get_model`.
3. Определяет, использовать ли заголовок авторизации или параметры запроса для передачи API-ключа.
4. Формирует URL для запроса в зависимости от того, используется ли потоковая передача данных.
5. Создает `ClientSession` для выполнения асинхронных запросов.
6. Преобразует сообщения в формат, ожидаемый API Gemini.
7. Добавляет медиафайлы (изображения) в запрос, если они предоставлены.
8. Формирует структуру данных для отправки в API, включая сообщения, параметры генерации и инструменты (функции).
9. Добавляет системные инструкции в запрос, если они предоставлены.
10. Отправляет POST-запрос к API и обрабатывает ответ.
11. Если используется потоковая передача данных, обрабатывает чанки данных, извлекая текст, причину завершения и информацию об использовании токенов.
12. Если потоковая передача не используется, извлекает текст ответа и причину завершения.
13. Возвращает асинхронный генератор, который позволяет получать ответы от API по частям.

**Внутренние функции**:
- Отсутствуют.

**ASCII flowchart**:

```
A [Проверка api_key]
|
B [Получение имени модели]
|
C [Определение способа аутентификации]
|
D [Формирование URL]
|
E [Создание ClientSession]
|
F [Преобразование сообщений]
|
G [Добавление медиафайлов]
|
H [Формирование структуры данных]
|
I [Добавление системных инструкций]
|
J [Отправка POST запроса]
|
K [Обработка ответа]
|
L [Извлечение данных (потоковая передача)]
|
M [Извлечение данных (не потоковая передача)]
|
N [Возврат асинхронного генератора]
```

**Примеры**:
```python
async for chunk in GeminiPro.create_async_generator(model="gemini-pro", messages=[{"role": "user", "content": "Hello"}], api_key="YOUR_API_KEY"):
    print(chunk)