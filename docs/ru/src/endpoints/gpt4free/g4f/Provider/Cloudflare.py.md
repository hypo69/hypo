# Модуль Cloudflare

## Обзор

Модуль `Cloudflare.py` предоставляет асинхронный интерфейс для взаимодействия с моделями искусственного интеллекта Cloudflare. Он позволяет генерировать текст на основе предоставленных сообщений, поддерживая стриминг ответов и работу с историей сообщений.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-провайдерами. Он использует асинхронные запросы для эффективной работы с API Cloudflare и предоставляет удобные инструменты для управления моделями и параметрами запросов.

## Классы

### `Cloudflare`

**Описание**: Класс `Cloudflare` реализует асинхронного провайдера для работы с AI Cloudflare.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.
- `AuthFileMixin`: Добавляет возможность авторизации через файл.

**Атрибуты**:
- `label` (str): Метка провайдера ("Cloudflare AI").
- `url` (str): URL главной страницы Cloudflare AI ("https://playground.ai.cloudflare.com").
- `working` (bool): Указывает, работает ли провайдер (True).
- `use_nodriver` (bool): Указывает, используется ли nodriver (True).
- `api_endpoint` (str): URL API для вывода ("https://playground.ai.cloudflare.com/api/inference").
- `models_url` (str): URL для получения списка моделей ("https://playground.ai.cloudflare.com/api/models").
- `supports_stream` (bool): Поддержка стриминга ответов (True).
- `supports_system_message` (bool): Поддержка системных сообщений (True).
- `supports_message_history` (bool): Поддержка истории сообщений (True).
- `default_model` (str): Модель по умолчанию ("@cf/meta/llama-3.3-70b-instruct-fp8-fast").
- `model_aliases` (dict): Псевдонимы моделей.
- `_args` (dict): Аргументы для сессии.

**Методы**:
- `get_models()`: Возвращает список доступных моделей.
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от AI Cloudflare.

### `Cloudflare.get_models`

```python
    @classmethod
    def get_models(cls) -> str:
        """
        Получает список доступных моделей от Cloudflare AI.

        Returns:
            str: Список доступных моделей.

        Как работает функция:
        1. Проверяет, загружены ли модели в атрибут `cls.models`.
        2. Если модели не загружены, проверяет, инициализирован ли атрибут `cls._args`.
        3. Если `cls._args` не инициализирован, проверяет наличие `nodriver`.
        4. Если `nodriver` доступен, получает аргументы из `nodriver` и сохраняет в `cls._args`.
        5. Если `nodriver` недоступен, проверяет наличие `curl_cffi`.
        6. Если `curl_cffi` недоступен, возвращает текущее значение `cls.models`.
        7. Если `curl_cffi` доступен, инициализирует `cls._args` с заголовками и куками по умолчанию.
        8. Создает сессию с использованием `cls._args`.
        9. Отправляет GET-запрос к `cls.models_url`.
        10. Обновляет куки в `cls._args` из ответа.
        11. Обрабатывает возможные ошибки статуса ответа.
        12. Извлекает список моделей из JSON-ответа и сохраняет в `cls.models`.
        13. Возвращает список моделей.

        Примеры:
        >>> Cloudflare.get_models()
        ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', ...]
        """
```

**Как работает функция `get_models`**:

```
Проверка загруженности моделей  --> Проверка инициализации _args --> Получение аргументов из nodriver/инициализация с DEFAULT_HEADERS  --> Создание сессии --> GET-запрос к models_url --> Обработка ошибок статуса ответа --> Извлечение списка моделей
```

### `Cloudflare.create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        max_tokens: int = 2048,
        cookies: Cookies = None,
        timeout: int = 300,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от AI Cloudflare.

        Args:
            model (str): Имя используемой модели.
            messages (Messages): Список сообщений для отправки в AI.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `2048`.
            cookies (Cookies, optional): Куки для использования в запросах. По умолчанию `None`.
            timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `300`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от AI Cloudflare.

        Raises:
            ModelNotFoundError: Если указанная модель не найдена.
            ResponseStatusError: Если получен некорректный статус ответа от API.

        Как работает функция:
        1. Получает путь к файлу кэша.
        2. Проверяет, инициализирован ли атрибут `cls._args`.
        3. Если `cls._args` не инициализирован, пытается загрузить его из файла кэша, иначе получает аргументы из `nodriver` или инициализирует с заголовками и куками по умолчанию.
        4. Пытается получить модель по имени, обрабатывая исключение `ModelNotFoundError`.
        5. Формирует данные запроса, включая сообщения, модель и параметры генерации.
        6. Отправляет POST-запрос к `cls.api_endpoint` с данными запроса.
        7. Обновляет куки в `cls._args` из ответа.
        8. Обрабатывает возможные ошибки статуса ответа.
        9. Итерирует по строкам ответа и извлекает данные JSON.
        10. Для строк, начинающихся с '0:', извлекает контент.
        11. Для строк, начинающихся с 'e:', извлекает информацию об использовании и причине завершения.
        12. Сохраняет `cls._args` в файл кэша.

        Внутренние функции:
            Нет

        Примеры:
        >>> async for response in Cloudflare.create_async_generator(model='@cf/meta/llama-3.3-70b-instruct-fp8-fast', messages=[{'role': 'user', 'content': 'Hello, how are you?'}]):
        ...     print(response)
        ...
        {'token': 'I', 'logprobs': {}}
        {'token': ' am', 'logprobs': {}}
        {'token': ' doing', 'logprobs': {}}
        {'token': ' well', 'logprobs': {}}
        ...
        Usage(prompt_tokens=12, completion_tokens=20, total_tokens=32)
        FinishReason('length')
        """
```

**Как работает функция `create_async_generator`**:

```
Получение пути к файлу кэша --> Проверка инициализации _args --> Загрузка из файла кэша/получение из nodriver/инициализация с DEFAULT_HEADERS --> Формирование данных запроса --> POST-запрос к api_endpoint --> Обработка ошибок статуса ответа --> Итерация по строкам ответа --> Извлечение данных JSON (контент, использование, причина завершения) --> Сохранение _args в файл кэша