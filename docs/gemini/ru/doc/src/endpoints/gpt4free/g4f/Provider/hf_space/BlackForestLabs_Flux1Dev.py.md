# Модуль BlackForestLabs_Flux1Dev

## Обзор

Модуль `BlackForestLabs_Flux1Dev` предоставляет асинхронный генератор для взаимодействия с моделью BlackForestLabs Flux-1-Dev через Hugging Face Space. Он позволяет генерировать изображения на основе текстовых запросов, используя API BlackForestLabs.

## Подробней

Модуль предназначен для создания изображений с использованием модели BlackForestLabs Flux-1-Dev. Он включает в себя функции для отправки запросов к API, обработки ответов и извлечения сгенерированных изображений.

## Классы

### `BlackForestLabs_Flux1Dev`

**Описание**: Класс для взаимодействия с моделью BlackForestLabs Flux-1-Dev.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Название провайдера - "BlackForestLabs Flux-1-Dev".
- `url` (str): URL Hugging Face Space - "https://black-forest-labs-flux-1-dev.hf.space".
- `space` (str): Имя Space - "black-forest-labs/FLUX.1-dev".
- `referer` (str): Referer для запросов - f"{url}/?__theme=light".
- `working` (bool): Указывает, что провайдер работает - `True`.
- `default_model` (str): Модель по умолчанию - 'black-forest-labs-flux-1-dev'.
- `default_image_model` (str): Модель изображений по умолчанию - совпадает с `default_model`.
- `model_aliases` (dict): Псевдонимы моделей, такие как {"flux-dev": default_image_model, "flux": default_image_model}.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список всех моделей.

**Методы**:
- `run`: Отправляет HTTP-запросы к API.
- `create_async_generator`: Создает асинхронный генератор для генерации изображений.

## Функции

### `run`

```python
    @classmethod
    def run(cls, method: str, session: StreamSession, conversation: JsonConversation, data: list = None):
        """
        Отправляет HTTP-запросы к API.

        Args:
            method (str): HTTP-метод ("post" или "get").
            session (StreamSession): Сессия для отправки запросов.
            conversation (JsonConversation): Объект, содержащий информацию о сессии.
            data (list, optional): Данные для отправки в теле запроса. По умолчанию `None`.

        Returns:
            StreamSession: Объект ответа от API.

        Raises:
            ResponseError: Если возникает ошибка при выполнении запроса.

        """
        ...
```

**Назначение**: Отправляет HTTP-запросы к API BlackForestLabs Flux-1-Dev.

**Параметры**:
- `method` (str): HTTP-метод ("post" или "get").
- `session` (StreamSession): Сессия для отправки запросов.
- `conversation` (JsonConversation): Объект, содержащий информацию о сессии (zerogpu_token, zerogpu_uuid, session_hash).
- `data` (list, optional): Данные для отправки в теле запроса. По умолчанию `None`.

**Возвращает**:
- `StreamSession`: Объект ответа от API.

**Вызывает исключения**:
- `ResponseError`: Если возникает ошибка при выполнении запроса.

**Как работает функция**:
1. **Формирование заголовков**: Создаются заголовки запроса, включающие `accept`, `content-type`, `x-zerogpu-token`, `x-zerogpu-uuid` и `referer`.
2. **Выбор метода запроса**: В зависимости от значения параметра `method` выполняется либо POST-запрос для присоединения к очереди, либо GET-запрос для получения данных.
3. **Отправка запроса**: Используется объект `session` для отправки запроса с указанными заголовками и данными.

**ASCII flowchart**:
```
    Начало
    │
    ├── Заголовки (accept, content-type, x-zerogpu-token, x-zerogpu-uuid, referer)
    │
    ├── Проверка method == "post"
    │   ├── True: POST-запрос к /gradio_api/queue/join
    │   │   └── Отправка данных: data, event_data, fn_index, trigger_id, session_hash
    │   │
    │   └── False: GET-запрос к /gradio_api/queue/data
    │       └── Отправка session_hash
    │
    └── Возврат response
```

**Примеры**:
```python
# Пример POST-запроса
# response = BlackForestLabs_Flux1Dev.run("post", session, conversation, data=[prompt, seed, randomize_seed, width, height, guidance_scale, num_inference_steps])

# Пример GET-запроса
# response = BlackForestLabs_Flux1Dev.run("get", session, conversation)
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls, 
        model: str, 
        messages: Messages,
        prompt: str = None,
        proxy: str = None,
        aspect_ratio: str = "1:1",
        width: int = None,
        height: int = None,
        guidance_scale: float = 3.5,
        num_inference_steps: int = 28,
        seed: int = 0,
        randomize_seed: bool = True,
        cookies: dict = None,
        api_key: str = None,
        zerogpu_uuid: str = "[object Object]",
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для генерации изображений.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений для формирования запроса.
            prompt (str, optional): Текстовый запрос. По умолчанию `None`.
            proxy (str, optional): Прокси-сервер. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            guidance_scale (float, optional): Масштаб соответствия запросу. По умолчанию 3.5.
            num_inference_steps (int, optional): Количество шагов для генерации. По умолчанию 28.
            seed (int, optional): Зерно для генерации. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
            cookies (dict, optional): Куки для запросов. По умолчанию `None`.
            api_key (str, optional): API ключ. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий изображения.

        Raises:
            RuntimeError: Если не удается распарсить сообщение от API.
            ResponseError: Если API возвращает ошибку.

        """
        ...
```

**Назначение**: Создает асинхронный генератор для генерации изображений с использованием API BlackForestLabs Flux-1-Dev.

**Параметры**:
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Текстовый запрос. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `guidance_scale` (float, optional): Масштаб соответствия запросу. По умолчанию 3.5.
- `num_inference_steps` (int, optional): Количество шагов для генерации. По умолчанию 28.
- `seed` (int, optional): Зерно для генерации. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
- `cookies` (dict, optional): Куки для запросов. По умолчанию `None`.
- `api_key` (str, optional): API ключ. По умолчанию `None`.
- `zerogpu_uuid` (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий изображения.

**Вызывает исключения**:
- `RuntimeError`: Если не удается распарсить сообщение от API.
- `ResponseError`: Если API возвращает ошибку.

**Как работает функция**:
1. **Инициализация сессии**: Создается асинхронная сессия с использованием `StreamSession`.
2. **Форматирование запроса**: Формируется текстовый запрос на основе сообщений и `prompt`.
3. **Подготовка данных**: Подготавливаются данные для запроса, включая размеры изображения, масштаб соответствия и количество шагов.
4. **Создание объекта conversation**: Создается объект `JsonConversation`, содержащий информацию о сессии (zerogpu_token, zerogpu_uuid, session_hash).
5. **Получение zerogpu_token**: Если `conversation.zerogpu_token` отсутствует, он получается с помощью `get_zerogpu_token`.
6. **Отправка POST-запроса**: Отправляется POST-запрос к API для присоединения к очереди.
7. **Отправка GET-запроса и обработка ответов**: Отправляется GET-запрос для получения данных и обрабатываются чанки ответа.
8. **Обработка сообщений**: В зависимости от типа сообщения (log, progress, process_generating, process_completed) генерируются соответствующие объекты (`Reasoning`, `ImagePreview`, `ImageResponse`).
9. **Обработка ошибок**: Обрабатываются ошибки парсинга JSON и ошибки, возвращаемые API.

**Внутренние функции**:

Внутри `create_async_generator` нет явно определенных внутренних функций, но используется асинхронный контекстный менеджер `StreamSession` и `cls.run`. Также вызывается `get_zerogpu_token`, которая не определена в данном коде, но импортируется из другого модуля.

**ASCII flowchart**:
```
    Начало
    │
    ├── Инициализация StreamSession
    │
    ├── Форматирование prompt
    │
    ├── Подготовка data (размеры, guidance_scale, num_inference_steps)
    │
    ├── Создание JsonConversation (zerogpu_token, zerogpu_uuid, session_hash)
    │
    ├── Проверка наличия zerogpu_token
    │   ├── Отсутствует: Получение zerogpu_token с помощью get_zerogpu_token
    │   │
    │   └── Присутствует: Продолжение
    │
    ├── POST-запрос к /gradio_api/queue/join
    │
    ├── GET-запрос к /gradio_api/queue/data
    │
    ├── Обработка чанков ответа
    │   ├── Проверка chunk.startswith(b"data: ")
    │   │   ├── True: Обработка JSON
    │   │   │   ├── msg == 'log': yield Reasoning
    │   │   │   ├── msg == 'progress': yield Reasoning
    │   │   │   ├── msg == 'process_generating': yield ImagePreview
    │   │   │   ├── msg == 'process_completed': yield ImageResponse
    │   │   │   └── Обработка ошибок парсинга JSON и ошибок API
    │   │   └── False: Пропуск
    │
    └── Конец
```

**Примеры**:
```python
# Пример использования async-генератора для генерации изображения
# async for item in BlackForestLabs_Flux1Dev.create_async_generator(model="flux-dev", messages=[{"role": "user", "content": "a cat"}], prompt="a cat"):
#     if isinstance(item, ImageResponse):
#         print(f"Image URL: {item.image_url}")