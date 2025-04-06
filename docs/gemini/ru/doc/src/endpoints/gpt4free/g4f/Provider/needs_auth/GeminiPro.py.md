# Модуль GeminiPro

## Обзор

Модуль `GeminiPro.py` предназначен для взаимодействия с API Google Gemini для генерации контента на основе предоставленных сообщений, изображений и инструментов. Он поддерживает как потоковую, так и не потоковую генерацию контента.

## Подробней

Модуль предоставляет класс `GeminiPro`, который является асинхронным провайдером и поддерживает историю сообщений, системные сообщения и требует аутентификацию.

## Классы

### `GeminiPro`

**Описание**: Класс для взаимодействия с API Google Gemini.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию контента.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Google Gemini API").
- `url` (str): URL главной страницы Google AI ("https://ai.google.dev").
- `login_url` (str): URL для получения API key ("https://aistudio.google.com/u/0/apikey").
- `api_base` (str): Базовый URL API ("https://generativelanguage.googleapis.com/v1beta").
- `working` (bool): Флаг, указывающий, что провайдер работает (True).
- `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений (True).
- `supports_system_message` (bool): Флаг, указывающий, что провайдер поддерживает системные сообщения (True).
- `needs_auth` (bool): Флаг, указывающий, что провайдер требует аутентификацию (True).
- `default_model` (str): Модель, используемая по умолчанию ("gemini-1.5-pro").
- `default_vision_model` (str): Модель для работы с изображениями, используемая по умолчанию ("gemini-1.5-pro").
- `fallback_models` (list[str]): Список моделей для fallback в случае проблем с основной моделью.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models(api_key: str = None, api_base: str = api_base) -> list[str]`: Возвращает список доступных моделей.
- `create_async_generator(model: str, messages: Messages, stream: bool = False, proxy: str = None, api_key: str = None, api_base: str = api_base, use_auth_header: bool = False, media: MediaListType = None, tools: Optional[list] = None, connector: BaseConnector = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения контента от API.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, api_key: str = None, api_base: str = api_base) -> list[str]:
    """
    Получает список доступных моделей из API Google Gemini.

    Args:
        api_key (str, optional): API ключ для аутентификации. По умолчанию None.
        api_base (str, optional): Базовый URL API. По умолчанию значение атрибута `api_base` класса.

    Returns:
        list[str]: Список имен моделей.

    Raises:
        MissingAuthError: Если `api_key` не указан и происходит ошибка при получении списка моделей.

    Как работает функция:
    1. Проверяет, если список моделей уже получен и сохранен в атрибуте `cls.models`. Если да, возвращает сохраненный список.
    2. Если список моделей не получен, пытается получить его из API.
    3. Формирует URL для запроса списка моделей.
    4. Отправляет GET запрос к API, используя `requests`.
    5. Проверяет статус ответа с помощью `raise_for_status`. Если статус не OK, вызывает исключение.
    6. Извлекает список моделей из JSON ответа.
    7. Сохраняет полученный список моделей в атрибуте `cls.models`.
    8. Если во время получения списка моделей происходит ошибка, логирует ошибку с помощью `debug.error`.
    9. Если `api_key` не указан, вызывает исключение `MissingAuthError`.
    10. Если произошла ошибка, возвращает список моделей fallback из атрибута `cls.fallback_models`.

    ascii
    Получение списка моделей
    │
    ├─── Проверка наличия моделей в cls.models
    │    │
    │    └─── Да: Возврат cls.models
    │    │
    │    └─── Нет:
    │         │
    │         ├─── Формирование URL
    │         │
    │         ├─── GET запрос к API
    │         │
    │         ├─── Проверка статуса ответа
    │         │    │
    │         │    └─── OK: Извлечение списка моделей
    │         │    │
    │         │    └─── Не OK: Обработка ошибки
    │         │
    │         ├─── Сохранение списка моделей в cls.models
    │         │
    │         └─── Возврат cls.models
    │
    └─── Обработка ошибок
         │
         └─── Логирование ошибки
         │
         └─── Вызов MissingAuthError, если api_key не указан
         │
         └─── Возврат cls.fallback_models

    Примеры:
    >>> GeminiPro.get_models(api_key='your_api_key')
    ['gemini-1.5-flash', 'gemini-1.5-flash-8b', 'gemini-1.5-pro', 'gemini-2.0-flash-exp', 'gemini-pro']
    """
    ...
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
    """
    Создает асинхронный генератор для получения контента от API Google Gemini.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую генерацию. По умолчанию False.
        proxy (str, optional): URL прокси-сервера. По умолчанию None.
        api_key (str, optional): API ключ для аутентификации. По умолчанию None.
        api_base (str, optional): Базовый URL API. По умолчанию значение атрибута `api_base` класса.
        use_auth_header (bool, optional): Флаг, указывающий, передавать ли API ключ через заголовок Authorization. По умолчанию False.
        media (MediaListType, optional): Список медиафайлов для отправки в API. По умолчанию None.
        tools (Optional[list], optional): Список инструментов (функций), доступных модели. По умолчанию None.
        connector (BaseConnector, optional): Aiohttp connector для управления соединениями. По умолчанию None.
        **kwargs: Дополнительные параметры для конфигурации генерации.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий контент от API.

    Raises:
        MissingAuthError: Если `api_key` не указан.
        RuntimeError: Если при запросе к API произошла ошибка.

    Как работает функция:
    1. Проверяет наличие `api_key`. Если он не указан, вызывает исключение `MissingAuthError`.
    2. Получает имя модели, используя метод `cls.get_model`.
    3. Определяет заголовки и параметры запроса в зависимости от значения `use_auth_header`.
    4. Формирует URL для запроса, используя `api_base`, `model` и `method` (streamGenerateContent или generateContent).
    5. Создает `ClientSession` с использованием `aiohttp` для выполнения асинхронных запросов.
    6. Формирует тело запроса `data`, содержащее список сообщений, конфигурацию генерации и инструменты.
    7. Обрабатывает список сообщений, преобразуя их в формат, ожидаемый API.
    8. Если предоставлены медиафайлы, добавляет их в тело запроса.
    9. Если предоставлено системное сообщение, добавляет его в тело запроса.
    10. Отправляет POST запрос к API.
    11. Если запрос завершается с ошибкой, извлекает сообщение об ошибке из JSON ответа и вызывает исключение `RuntimeError`.
    12. Если используется потоковая генерация:
        - Читает ответ по частям (chunks).
        - Обрабатывает каждый chunk, извлекая текст и информацию об использовании токенов.
        - Возвращает текст, причину завершения и информацию об использовании токенов через генератор.
    13. Если потоковая генерация не используется:
        - Читает полный ответ.
        - Извлекает текст из ответа.
        - Возвращает текст через генератор.

    ASCII flowchart:

    Проверка API ключа
    │
    ├─── Отсутствует API ключ: Выброс MissingAuthError
    │
    ├─── API ключ присутствует:
    │   │
    │   ├─── Определение заголовков и параметров запроса
    │   │
    │   ├─── Формирование URL запроса
    │   │
    │   ├─── Создание асинхронной сессии
    │   │
    │   ├─── Формирование тела запроса (data)
    │   │
    │   ├─── POST запрос к API
    │   │
    │   ├─── Обработка ответа
    │   │   │
    │   │   ├─── Ошибка в ответе: Выброс RuntimeError
    │   │   │
    │   │   ├─── Stream True: Потоковая обработка чанков
    │   │   │
    │   │   ├─── Stream False: Обработка полного ответа
    │   │   │
    │   │   └─── Возврат контента через генератор
    │   │
    │   └─── Закрытие асинхронной сессии
    │
    └─── Конец

    Примеры:
    >>> async for chunk in GeminiPro.create_async_generator(model='gemini-1.5-pro', messages=[{'role': 'user', 'content': 'Напиши короткий стих о весне' }], api_key='your_api_key'):
    ...     print(chunk)
    """
    ...