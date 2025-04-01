# Модуль Cloudflare

## Обзор

Модуль `Cloudflare` предоставляет асинхронный интерфейс для взаимодействия с API Cloudflare AI, позволяя генерировать текст на основе различных моделей, включая Llama и Qwen. Модуль поддерживает потоковую передачу данных, использование системных сообщений и сохранение истории сообщений. Он также включает механизмы аутентификации и кэширования для повышения эффективности.

## Подробней

Модуль предназначен для использования в проектах, требующих взаимодействия с моделями Cloudflare AI. Он предоставляет удобный интерфейс для отправки запросов и получения ответов в асинхронном режиме. Модуль использует `nodriver` или `curl_cffi` для выполнения HTTP-запросов, а также поддерживает прокси и cookies.

## Классы

### `Cloudflare`

**Описание**:
Класс `Cloudflare` является основным классом, предоставляющим функциональность для взаимодействия с API Cloudflare AI. Он наследуется от `AsyncGeneratorProvider`, `ProviderModelMixin` и `AuthFileMixin`, что обеспечивает поддержку асинхронной генерации, управления моделями и аутентификации через файлы.

**Принцип работы**:

1.  **Инициализация**: Класс инициализируется с предопределенными значениями, такими как `label`, `url`, `api_endpoint` и `models_url`.
2.  **Получение моделей**: Метод `get_models` используется для получения списка доступных моделей из API Cloudflare. Если модели еще не были загружены, он выполняет HTTP-запрос к `models_url` и извлекает список моделей из JSON-ответа.
3.  **Создание асинхронного генератора**: Метод `create_async_generator` создает асинхронный генератор, который отправляет запросы к API Cloudflare и возвращает ответы в потоковом режиме. Он использует `StreamSession` для выполнения HTTP-запросов и обрабатывает ответы построчно.
4.  **Обработка ответов**: Генератор обрабатывает строки, начинающиеся с `0:`, как JSON-данные, содержащие сгенерированный текст. Строки, начинающиеся с `e:`, обрабатываются как JSON-данные, содержащие информацию об использовании и причине завершения.
5.  **Кэширование**: Класс использует кэширование для хранения аргументов (`_args`) и cookies, чтобы избежать повторных запросов к API аутентификации. Файл кэша (`cache_file`) используется для сохранения и загрузки этих данных.

**Атрибуты**:

*   `label` (str): Метка провайдера ("Cloudflare AI").
*   `url` (str): URL главной страницы Cloudflare AI ("https://playground.ai.cloudflare.com").
*   `working` (bool): Флаг, указывающий, работает ли провайдер (True).
*   `use_nodriver` (bool): Флаг, указывающий, используется ли `nodriver` для выполнения запросов (True).
*   `api_endpoint` (str): URL API для выполнения запросов к моделям ("https://playground.ai.cloudflare.com/api/inference").
*   `models_url` (str): URL для получения списка доступных моделей ("https://playground.ai.cloudflare.com/api/models").
*   `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (True).
*   `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
*   `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (True).
*   `default_model` (str): Модель, используемая по умолчанию ("@cf/meta/llama-3.3-70b-instruct-fp8-fast").
*   `model_aliases` (dict): Псевдонимы для моделей.
*   `_args` (dict): Аргументы для HTTP-запросов, включая заголовки и cookies.

**Методы**:

*   `get_models(cls) -> str`:
    *   **Назначение**: Получает список доступных моделей из API Cloudflare.
    *   **Как работает функция**:
        1.  Проверяет, загружены ли уже модели (`cls.models`). Если да, возвращает их.
        2.  Проверяет, инициализированы ли аргументы (`cls._args`). Если нет, пытается получить их с помощью `get_args_from_nodriver` или использует `DEFAULT_HEADERS`.
        3.  Выполняет HTTP-запрос к `cls.models_url` с использованием `Session`.
        4.  Извлекает список моделей из JSON-ответа и сохраняет их в `cls.models`.
        5.  В случае ошибки возвращает текущие `cls.models`.

        **Примеры**:

        ```python
        models = Cloudflare.get_models()
        print(models)
        ```
    *   `create_async_generator(cls, model: str, messages: Messages, proxy: str = None, max_tokens: int = 2048, cookies: Cookies = None, timeout: int = 300, **kwargs) -> AsyncResult`:
        *   **Назначение**: Создает асинхронный генератор для взаимодействия с API Cloudflare.
        *   **Параметры**:
            *   `model` (str): Название модели для использования.
            *   `messages` (Messages): Список сообщений для отправки в API.
            *   `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            *   `max_tokens` (int, optional): Максимальное количество токенов для генерации. По умолчанию `2048`.
            *   `cookies` (Cookies, optional): Cookies для отправки в API. По умолчанию `None`.
            *   `timeout` (int, optional): Время ожидания ответа от API в секундах. По умолчанию `300`.
            *   `**kwargs`: Дополнительные аргументы.

        *   **Возвращает**:
            *   `AsyncResult`: Асинхронный генератор, возвращающий сгенерированный текст, информацию об использовании и причине завершения.

        *   **Вызывает исключения**:
            *   `ModelNotFoundError`: Если указанная модель не найдена.
            *   `ResponseStatusError`: Если HTTP-запрос завершился с ошибкой.

        *   **Как работает функция**:

            1.  Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API Cloudflare.
            2.  Она инициализирует аргументы (`cls._args`) из кэша или с помощью `get_args_from_nodriver`.
            3.  Создает полезную нагрузку (`data`) с сообщениями, моделью и параметрами генерации.
            4.  Отправляет POST-запрос к API Cloudflare (`cls.api_endpoint`) с использованием `StreamSession`.
            5.  Обрабатывает ответы построчно, извлекая сгенерированный текст, информацию об использовании и причине завершения.
            6.  Кэширует аргументы (`cls._args`) в файл для последующего использования.

        *   **Внутренние функции**: Нет.

        *   **Примеры**:

            ```python
            model = "@cf/meta/llama-3.3-70b-instruct-fp8-fast"
            messages = [{"role": "user", "content": "Hello, how are you?"}]
            generator = await Cloudflare.create_async_generator(model=model, messages=messages)
            async for item in generator:
                print(item)
            ```

## Функции

### `get_models`

```python
@classmethod
def get_models(cls) -> str:
    """
    Получает список доступных моделей из API Cloudflare.

    Args:
        cls: Класс Cloudflare.

    Returns:
        str: Список доступных моделей.
    """
```

### `create_async_generator`

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
    Создает асинхронный генератор для взаимодействия с API Cloudflare.

    Args:
        cls: Класс Cloudflare.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов для генерации. По умолчанию `2048`.
        cookies (Cookies, optional): Cookies для отправки в API. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа от API в секундах. По умолчанию `300`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий сгенерированный текст, информацию об использовании и причине завершения.
    """