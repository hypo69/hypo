# Модуль DeepseekAI_JanusPro7b

## Обзор

Модуль `DeepseekAI_JanusPro7b` предоставляет асинхронный генератор для взаимодействия с моделью DeepseekAI Janus-Pro-7B, размещенной на Hugging Face Spaces. Он поддерживает как текстовые запросы, так и запросы к генерации изображений.

## Подробней

Этот модуль позволяет пользователям отправлять запросы к модели DeepseekAI Janus-Pro-7B через API Hugging Face Spaces. Он включает поддержку стриминга ответов, системных сообщений и истории сообщений. Модуль также обеспечивает возможность отправки изображений для генерации изображений на основе текстовых запросов.

## Классы

### `DeepseekAI_JanusPro7b`

**Описание**: Класс `DeepseekAI_JanusPro7b` является провайдером асинхронного генератора и предоставляет методы для взаимодействия с моделью DeepseekAI Janus-Pro-7B.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("DeepseekAI Janus-Pro-7B").
- `space` (str): Имя пространства Hugging Face, где размещена модель ("deepseek-ai/Janus-Pro-7B").
- `url` (str): URL страницы пространства Hugging Face.
- `api_url` (str): URL API для взаимодействия с моделью.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер стриминг ответов (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию для текстовых запросов ("janus-pro-7b").
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений ("janus-pro-7b-image").
- `default_vision_model` (str): Модель, используемая по умолчанию для vision запросов (совпадает с `default_model`).
- `image_models` (list[str]): Список поддерживаемых моделей для генерации изображений.
- `vision_models` (list[str]): Список поддерживаемых моделей для vision запросов.
- `models` (list[str]): Объединение `vision_models` и `image_models`.

**Методы**:

- `run(method: str, session: StreamSession, prompt: str, conversation: JsonConversation, image: dict = None, seed: int = 0)`: Отправляет запрос к API Hugging Face Spaces.
- `create_async_generator(model: str, messages: Messages, media: MediaListType = None, prompt: str = None, proxy: str = None, cookies: Cookies = None, api_key: str = None, zerogpu_uuid: str = "[object Object]", return_conversation: bool = False, conversation: JsonConversation = None, seed: int = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с моделью.

## Функции

### `run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, prompt: str, conversation: JsonConversation, image: dict = None, seed: int = 0):
    """
    Отправляет запрос к API Hugging Face Spaces.

    Args:
        method (str): HTTP-метод ("post" или "image" или "get").
        session (StreamSession): Асинхровая сессия для выполнения HTTP-запросов.
        prompt (str): Текст запроса.
        conversation (JsonConversation): Объект, содержащий информацию о сессии и токены.
        image (dict, optional): Данные изображения для запросов к генерации изображений. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.

    Returns:
        StreamResponse: Объект ответа от API.

    Как работает функция:
    1. Формирует заголовки запроса, включая токены и информацию о сессии.
    2. В зависимости от значения параметра `method` выполняет POST или GET запрос к API Hugging Face Spaces.
    3. Для методов "post" и "image" отправляет JSON-данные, содержащие запрос, seed и другие параметры.
    4. Возвращает объект ответа от API.

    Блоки функции:
    A: Подготовка запроса
    │
    ├── B: Выбор метода (post/image/get)
    │    │
    │    ├── C1: POST запрос (method == "post")
    │    │
    │    ├── C2: POST запрос для изображений (method == "image")
    │    │
    │    └── C3: GET запрос (method == "get")
    │
    └── D: Возврат ответа

    ```mermaid
    graph TD
        A[Подготовка запроса] --> B{Выбор метода (post/image/get)}
        B -- post --> C1[POST запрос (method == "post")]
        B -- image --> C2[POST запрос для изображений (method == "image")]
        B -- get --> C3[GET запрос (method == "get")]
        C1 --> D[Возврат ответа]
        C2 --> D
        C3 --> D
    ```

    **Примеры**:

    ```python
    # Пример вызова функции run
    # async with StreamSession() as session:
    #     response = await DeepseekAI_JanusPro7b.run("post", session, "Hello", JsonConversation(session_hash="123"))
    ```
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
        media: MediaListType = None,
        prompt: str = None,
        proxy: str = None,
        cookies: Cookies = None,
        api_key: str = None,
        zerogpu_uuid: str = "[object Object]",
        return_conversation: bool = False,
        conversation: JsonConversation = None,
        seed: int = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с моделью.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки.
            media (MediaListType, optional): Список медиа-файлов для отправки. По умолчанию `None`.
            prompt (str, optional): Текст запроса. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            cookies (Cookies, optional): Cookies для отправки с запросами. По умолчанию `None`.
            api_key (str, optional): API-ключ для доступа к модели. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
            return_conversation (bool, optional): Указывать, возвращать ли объект разговора. По умолчанию `False`.
            conversation (JsonConversation, optional): Объект, содержащий информацию о сессии. По умолчанию `None`.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Результаты генерации от модели.

        Как работает функция:
        1. Определяет метод запроса ("post" или "image") в зависимости от типа модели и наличия запроса.
        2. Форматирует запрос, используя `format_prompt` или `format_image_prompt`.
        3. Генерирует случайное seed, если оно не предоставлено.
        4. Создает или использует существующий объект `JsonConversation` для управления сессией.
        5. Загружает медиа-файлы на сервер, если они предоставлены.
        6. Отправляет запрос к API, используя метод `run`.
        7. Обрабатывает ответы от API, извлекая информацию о прогрессе, статусе и сгенерированных данных.
        8. Возвращает результаты генерации в виде асинхронного генератора.

        Блоки функции:
        A: Определение метода запроса
        │
        ├── B: Форматирование запроса
        │
        ├── C: Управление сессией (JsonConversation)
        │
        ├── D: Загрузка медиа-файлов (если есть)
        │
        └── E: Отправка запроса и обработка ответов

        ```mermaid
        graph TD
            A[Определение метода запроса] --> B[Форматирование запроса]
            B --> C{Управление сессией (JsonConversation)}
            C --> D{Загрузка медиа-файлов (если есть)}
            D --> E[Отправка запроса и обработка ответов]
            E --> F[Возврат результатов]
        ```

        **Примеры**:

        ```python
        # Пример вызова функции create_async_generator
        # async for result in DeepseekAI_JanusPro7b.create_async_generator(model="janus-pro-7b", messages=[{"role": "user", "content": "Hello"}])
        #     print(result)
        ```
        """
        ...
```

### `get_zerogpu_token`

```python
async def get_zerogpu_token(space: str, session: StreamSession, conversation: JsonConversation, cookies: Cookies = None):
    """
    Получает ZeroGPU token и UUID из Hugging Face Spaces.

    Args:
        space (str): Имя пространства Hugging Face.
        session (StreamSession): Асинхровая сессия для выполнения HTTP-запросов.
        conversation (JsonConversation): Объект, содержащий информацию о сессии.
        cookies (Cookies, optional): Cookies для отправки с запросами. По умолчанию `None`.

    Returns:
        tuple[str | None, str]: Кортеж, содержащий ZeroGPU UUID и token.

    Как работает функция:
    1. Пытается получить ZeroGPU UUID из объекта `conversation`, если он существует.
    2. Выполняет GET-запрос к странице Hugging Face Spaces для извлечения ZeroGPU token и UUID из HTML-кода.
    3. Если cookies предоставлены, выполняет GET-запрос к API Hugging Face для получения ZeroGPU token.
    4. Возвращает ZeroGPU UUID и token.

    Блоки функции:
    A: Попытка получить UUID из conversation
    │
    ├── B: GET-запрос к странице Hugging Face
    │
    └── C: GET-запрос к API Hugging Face (если есть cookies)

    ```mermaid
    graph TD
        A[Попытка получить UUID из conversation] --> B{GET-запрос к странице Hugging Face}
        B --> C{GET-запрос к API Hugging Face (если есть cookies)}
        C --> D[Возврат UUID и token]
    ```

    **Примеры**:

    ```python
    # Пример вызова функции get_zerogpu_token
    # zerogpu_uuid, zerogpu_token = await get_zerogpu_token("deepseek-ai/Janus-Pro-7B", StreamSession(), JsonConversation(session_hash="123"))
    ```
    """
    ...