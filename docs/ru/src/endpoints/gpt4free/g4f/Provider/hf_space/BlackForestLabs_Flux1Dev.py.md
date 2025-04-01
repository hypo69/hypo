# Модуль BlackForestLabs_Flux1Dev

## Обзор

Модуль `BlackForestLabs_Flux1Dev` предоставляет асинхронный генератор для взаимодействия с моделью BlackForestLabs Flux-1-Dev.
Он позволяет генерировать изображения на основе текстового запроса, используя API сервиса Black Forest Labs.

## Подробнее

Этот модуль предназначен для интеграции с платформой `hypotez` и обеспечивает возможность создания изображений, используя модель `BlackForestLabs Flux-1-Dev`.
Модуль использует `StreamSession` для асинхронного обмена данными, что позволяет эффективно обрабатывать запросы.
Он также включает механизмы для обработки ошибок и предварительного просмотра сгенерированных изображений.

## Классы

### `BlackForestLabs_Flux1Dev`

**Описание**: Класс `BlackForestLabs_Flux1Dev` является асинхронным провайдером генерации изображений, использующим модель Flux-1-Dev от Black Forest Labs.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("BlackForestLabs Flux-1-Dev").
- `url` (str): URL сервиса Black Forest Labs ("https://black-forest-labs-flux-1-dev.hf.space").
- `space` (str): Идентификатор пространства Hugging Face Space ("black-forest-labs/FLUX.1-dev").
- `referer` (str): Referer для HTTP-запросов (содержит URL и параметр темы).
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель, используемая по умолчанию ('black-forest-labs-flux-1-dev').
- `default_image_model` (str): Модель изображений, используемая по умолчанию (совпадает с `default_model`).
- `model_aliases` (dict): Псевдонимы моделей (например, "flux-dev" и "flux" указывают на `default_image_model`).
- `image_models` (list): Список моделей изображений (ключи `model_aliases`).
- `models` (list): Список доступных моделей (совпадает с `image_models`).

**Методы**:
- `run(method: str, session: StreamSession, conversation: JsonConversation, data: list = None)`: Выполняет HTTP-запрос к API.
- `create_async_generator(...)`: Создает асинхронный генератор для генерации изображений.

## Функции

### `run`

```python
@classmethod
def run(cls, method: str, session: StreamSession, conversation: JsonConversation, data: list = None):
    """
    Выполняет HTTP-запрос к API Black Forest Labs Flux-1-Dev.

    Args:
        method (str): HTTP-метод ("post" или "get").
        session (StreamSession): Асинхровая сессия для выполнения запросов.
        conversation (JsonConversation): Объект, содержащий данные для разговора, такие как токены и UUID.
        data (list, optional): Данные для отправки в запросе POST. По умолчанию `None`.

    Returns:
        AsyncGeneratorProvider: Асинхронный генератор

    Raises:
        Exception: В случае ошибок при выполнении запроса.

    """
    ...
```

**Назначение**: Отправляет HTTP-запрос к API Black Forest Labs Flux-1-Dev для взаимодействия с моделью. Функция отвечает за отправку данных и получение ответов от API, используя указанный HTTP-метод (`POST` или `GET`).

**Параметры**:
- `method` (str): HTTP-метод, который будет использован для запроса. Допустимые значения: `"post"` или `"get"`.
- `session` (StreamSession): Асинхровая сессия, используемая для выполнения HTTP-запросов. Это позволяет отправлять запросы асинхронно, не блокируя основной поток выполнения.
- `conversation` (JsonConversation): Объект, содержащий метаданные для взаимодействия с API, такие как `zerogpu_token`, `zerogpu_uuid` и `session_hash`.
- `data` (list, optional): Данные, которые будут отправлены в теле запроса, если используется метод `POST`. По умолчанию `None`.

**Возвращает**:
- Возвращает объект `session.post` или `session.get`, который представляет собой асинхронный HTTP-запрос.

**Как работает функция**:

1. **Подготовка заголовков**:
   - Определяются заголовки HTTP-запроса, включающие `accept`, `content-type`, `x-zerogpu-token`, `x-zerogpu-uuid` и `referer`.
   - Заголовки `x-zerogpu-token` и `x-zerogpu-uuid` используются для аутентификации и авторизации запроса.

2. **Выполнение запроса**:
   - Если `method` равен `"post"`, выполняется `POST`-запрос к API для присоединения к очереди обработки.
   - Если `method` равен `"get"`, выполняется `GET`-запрос к API для получения данных сессии.

3. **Возврат результата**:
   - Возвращается объект асинхронного HTTP-запроса (`session.post` или `session.get`).

**ASCII Flowchart**:

```
    Заголовки
    |
    Метод (POST/GET)
    |
    Запрос (POST: присоединение к очереди, GET: получение данных)
    |
    Возврат результата
```

**Примеры**:

1. **Выполнение POST-запроса**:
   ```python
   import asyncio
   from aiohttp import ClientSession
   from src.providers.response import JsonConversation

   async def run_post_request():
       session = ClientSession()
       conversation = JsonConversation(zerogpu_token='test_token', zerogpu_uuid='test_uuid', session_hash='test_hash')
       data = ['prompt', 0, False, 512, 512, 7.5, 20]
       response = await BlackForestLabs_Flux1Dev.run("post", session, conversation, data)
       await session.close()
   asyncio.run(run_post_request())
   ```

2. **Выполнение GET-запроса**:
   ```python
   import asyncio
   from aiohttp import ClientSession
   from src.providers.response import JsonConversation

   async def run_get_request():
       session = ClientSession()
       conversation = JsonConversation(zerogpu_token='test_token', zerogpu_uuid='test_uuid', session_hash='test_hash')
       response = await BlackForestLabs_Flux1Dev.run("get", session, conversation)
       await session.close()
   asyncio.run(run_get_request())
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
    Создает асинхронный генератор для генерации изображений на основе текстового запроса.

    Args:
        model (str): Модель для генерации изображений.
        messages (Messages): Список сообщений для формирования запроса.
        prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
        aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
        width (int, optional): Ширина изображения. По умолчанию `None`.
        height (int, optional): Высота изображения. По умолчанию `None`.
        guidance_scale (float, optional): Масштаб соответствия запросу. По умолчанию 3.5.
        num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 28.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.
        randomize_seed (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
        cookies (dict, optional): Cookies для выполнения запросов. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий изображения.

    Raises:
        RuntimeError: Если не удается разобрать сообщение от API.
        ResponseError: Если API возвращает ошибку.

    """
    ...
```

**Назначение**: Создает асинхронный генератор для генерации изображений на основе текстового запроса, используя API BlackForestLabs Flux-1-Dev.

**Параметры**:
- `model` (str): Модель, используемая для генерации изображений.
- `messages` (Messages): Список сообщений, используемых для формирования запроса.
- `prompt` (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию `"1:1"`.
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `guidance_scale` (float, optional): Масштаб соответствия запросу. По умолчанию `3.5`.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию `28`.
- `seed` (int, optional): Зерно для генерации случайных чисел. По умолчанию `0`.
- `randomize_seed` (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
- `cookies` (dict, optional): Cookies для выполнения запросов. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `zerogpu_uuid` (str, optional): UUID для zerogpu. По умолчанию `"[object Object]"`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который возвращает изображения в виде объектов `ImageResponse` и `ImagePreview`, а также информацию о ходе выполнения в виде объектов `Reasoning`.

**Как работает функция**:

1. **Инициализация**:
   - Создается асинхронная сессия `StreamSession` для выполнения запросов.
   - Форматируется текстовый запрос `prompt` на основе переданных сообщений `messages`.
   - Определяются параметры изображения `width` и `height` на основе `aspect_ratio`.
   - Готовятся данные для запроса `data`, включающие `prompt`, `seed`, `randomize_seed`, `width`, `height`, `guidance_scale` и `num_inference_steps`.
   - Создается объект `JsonConversation` для хранения метаданных сессии, таких как `zerogpu_token`, `zerogpu_uuid` и `session_hash`.

2. **Аутентификация**:
   - Если `zerogpu_token` не предоставлен, он получается с использованием функции `get_zerogpu_token`.

3. **Выполнение запросов**:
   - Выполняется `POST`-запрос для присоединения к очереди обработки.
   - Выполняется `GET`-запрос для получения данных о ходе выполнения и результатов генерации.

4. **Обработка данных**:
   - Данные, получаемые из API, обрабатываются построчно.
   - Если строка начинается с `"data: "`, она интерпретируется как JSON.
   - В зависимости от значения ключа `"msg"` в JSON-данных, генерируются различные типы объектов:
     - `"log"`: `Reasoning` с информацией о статусе.
     - `"progress"`: `Reasoning` с информацией о прогрессе.
     - `"process_generating"`: `ImagePreview` с предварительным просмотром изображения.
     - `"process_completed"`: `ImageResponse` с окончательным изображением и `Reasoning` с информацией о завершении.

5. **Обработка ошибок**:
   - Если API возвращает ошибку, выбрасывается исключение `ResponseError`.
   - Если не удается разобрать JSON-данные, выбрасывается исключение `RuntimeError`.

**ASCII Flowchart**:

```
    Начало
    |
    Создание сессии
    |
    Форматирование запроса
    |
    Получение токена (если необходимо)
    |
    Запрос (POST/GET)
    |
    Обработка данных
    |
    Вывод (ImageResponse/ImagePreview/Reasoning)
    |
    Конец
```

**Примеры**:

1. **Создание асинхронного генератора для генерации изображения**:
   ```python
   import asyncio
   from src.typing import Messages

   async def generate_image():
       messages: Messages = [{"role": "user", "content": "A cat"}]
       async for item in BlackForestLabs_Flux1Dev.create_async_generator(model='flux-dev', messages=messages):
           print(item)

   asyncio.run(generate_image())