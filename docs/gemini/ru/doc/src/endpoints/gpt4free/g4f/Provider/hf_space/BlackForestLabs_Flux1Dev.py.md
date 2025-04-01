# Модуль BlackForestLabs_Flux1Dev

## Обзор

Модуль предоставляет класс `BlackForestLabs_Flux1Dev`, который является асинхронным провайдером для генерации изображений с использованием модели Flux-1-Dev от Black Forest Labs через Hugging Face Space. Модуль позволяет создавать изображения на основе текстовых запросов с возможностью настройки различных параметров, таких как соотношение сторон, размеры изображения, seed и guidance scale.

## Подробнее

Этот модуль позволяет интегрировать функциональность генерации изображений от Black Forest Labs Flux-1-Dev в проект `hypotez`. Он использует Hugging Face Space для доступа к модели и предоставляет асинхронный интерфейс для взаимодействия с ней. Модуль также обрабатывает ошибки и возвращает результаты в виде объектов `ImageResponse` и `ImagePreview`.

## Классы

### `BlackForestLabs_Flux1Dev`

**Описание**: Класс, представляющий провайдера для генерации изображений с использованием модели Flux-1-Dev от Black Forest Labs.
**Наследует**: `AsyncGeneratorProvider`, `ProviderModelMixin`

**Атрибуты**:
- `label` (str): Название провайдера ("BlackForestLabs Flux-1-Dev").
- `url` (str): URL Hugging Face Space.
- `space` (str): Имя Hugging Face Space ("black-forest-labs/FLUX.1-dev").
- `referer` (str): Referer URL.
- `working` (bool): Указывает, что провайдер работает (True).
- `default_model` (str): Модель по умолчанию ('black-forest-labs-flux-1-dev').
- `default_image_model` (str): Модель изображения по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей.

**Методы**:
- `run(method: str, session: StreamSession, conversation: JsonConversation, data: list = None)`: Выполняет HTTP-запрос к Hugging Face Space.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, aspect_ratio: str = "1:1", width: int = None, height: int = None, guidance_scale: float = 3.5, num_inference_steps: int = 28, seed: int = 0, randomize_seed: bool = True, cookies: dict = None, api_key: str = None, zerogpu_uuid: str = "[object Object]", **kwargs) -> AsyncResult`: Создает асинхронный генератор для генерации изображений.

## Функции

### `run`

```python
    @classmethod
    def run(cls, method: str, session: StreamSession, conversation: JsonConversation, data: list = None):
        """Выполняет HTTP-запрос к Hugging Face Space.

        Args:
            method (str): HTTP-метод ("post" или "get").
            session (StreamSession): Асинхровая сессия для выполнения запросов.
            conversation (JsonConversation): Объект, содержащий информацию о сессии и токены.
            data (list, optional): Данные для отправки в запросе. По умолчанию `None`.

        Returns:
            объект ответа сессии: Объект ответа, возвращаемый `session.post` или `session.get`.

        Как работает функция:
        1. Функция `run` выполняет HTTP-запросы к Hugging Face Space в зависимости от указанного метода (`post` или `get`).
        2. Формирует заголовки запроса, включая токены и UUID.
        3. Отправляет запрос с использованием `session.post` или `session.get` и возвращает ответ.

        ASCII flowchart:

        A (method)
        |
        B (headers)
        |
        C (session.post or session.get)
        |
        D (return response)

        Где:
        A: Определяется метод HTTP-запроса (`post` или `get`).
        B: Формируются заголовки запроса, включая токены и UUID.
        C: Выполняется HTTP-запрос с использованием `session.post` или `session.get`.
        D: Возвращается объект ответа.
        """
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
        """Создает асинхронный генератор для генерации изображений.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений для формирования запроса.
            prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            proxy (str, optional): Proxy для использования при выполнении запроса. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            guidance_scale (float, optional): Guidance scale для генерации изображения. По умолчанию 3.5.
            num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 28.
            seed (int, optional): Seed для генерации изображения. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
            cookies (dict, optional): Cookies для отправки в запросе. По умолчанию `None`.
            api_key (str, optional): API key для доступа к Hugging Face Space. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий объекты `ImageResponse` и `ImagePreview`.

        Raises:
            RuntimeError: Если не удается распарсить сообщение от сервера.
            ResponseError: Если сервер возвращает ошибку.

        Как работает функция:
        1. Функция `create_async_generator` создает асинхронный генератор для генерации изображений на основе предоставленных параметров.
        2. Формирует данные запроса, включая текстовый запрос, seed, размеры изображения и guidance scale.
        3. Получает zerogpu_token, если он не был предоставлен.
        4. Отправляет POST-запрос для запуска процесса генерации.
        5. Получает события с сервера и обрабатывает их:
        - Если сообщение содержит статус (`msg` == 'log'), возвращает объект `Reasoning`.
        - Если сообщение содержит прогресс (`msg` == 'progress'), возвращает объект `Reasoning` с информацией о прогрессе.
        - Если сообщение содержит предварительный просмотр изображения (`msg` == 'process_generating'), возвращает объект `ImagePreview`.
        - Если сообщение содержит завершенный результат (`msg` == 'process_completed'), возвращает объект `ImageResponse`.
        6. Обрабатывает ошибки, возникающие при парсинге сообщений или при получении ошибок от сервера.

        ASCII flowchart:

        A (prompt, data)
        |
        B (zerogpu_token)
        |
        C (POST request)
        |
        D (event stream)
        |
        E (parse JSON data)
        |
        F (yield ImageResponse, ImagePreview, Reasoning)

        Где:
        A: Формируются текстовый запрос и данные для запроса.
        B: Получается `zerogpu_token`, если он не был предоставлен.
        C: Отправляется POST-запрос для запуска процесса генерации.
        D: Получается поток событий с сервера.
        E: Парсится JSON-данные из потока событий.
        F: Возвращаются объекты `ImageResponse`, `ImagePreview` или `Reasoning` в зависимости от типа сообщения.

        Примеры:
        ```python
        # Пример вызова функции
        async for result in BlackForestLabs_Flux1Dev.create_async_generator(
            model='black-forest-labs-flux-1-dev',
            messages=[{'role': 'user', 'content': 'A beautiful landscape'}],
            prompt='A beautiful landscape',
            aspect_ratio='16:9'
        ):
            if isinstance(result, ImageResponse):
                print(f'Image URL: {result.image_url}')
            elif isinstance(result, ImagePreview):
                print(f'Preview URL: {result.image_url}')
            elif isinstance(result, Reasoning):
                print(f'Status: {result.status}')
        ```
        """