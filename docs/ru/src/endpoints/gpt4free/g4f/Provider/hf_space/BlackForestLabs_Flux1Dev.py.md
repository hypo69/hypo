# Модуль BlackForestLabs_Flux1Dev

## Обзор

Модуль `BlackForestLabs_Flux1Dev` предоставляет асинхронный генератор для взаимодействия с моделью Flux-1-Dev от Black Forest Labs, размещенной на платформе Hugging Face Spaces. Он позволяет генерировать изображения на основе текстовых запросов, используя API Gradio. Модуль поддерживает настройку параметров генерации изображений, таких как размеры, соотношение сторон, seed и guidance scale.

## Подробней

Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, предоставляя возможность генерации изображений с использованием модели Flux-1-Dev. Он использует асинхронный подход для обеспечения неблокирующего взаимодействия с API, что позволяет эффективно обрабатывать запросы. Модуль также включает обработку ошибок и логирование для обеспечения стабильной работы.

## Классы

### `BlackForestLabs_Flux1Dev`

**Описание**: Класс `BlackForestLabs_Flux1Dev` является асинхронным генератором и предоставляет методы для взаимодействия с моделью Flux-1-Dev от Black Forest Labs.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера "BlackForestLabs Flux-1-Dev".
- `url` (str): URL пространства Hugging Face Spaces, где размещена модель.
- `space` (str): Имя пространства Hugging Face Spaces.
- `referer` (str): Referer для HTTP-запросов.
- `working` (bool): Указывает, что провайдер в рабочем состоянии.
- `default_model` (str): Модель по умолчанию 'black-forest-labs-flux-1-dev'.
- `default_image_model` (str): Модель изображения по умолчанию.
- `model_aliases` (dict): Алиасы моделей.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей.

**Методы**:
- `run`: Выполняет HTTP-запрос к API Gradio.
- `create_async_generator`: Создает асинхронный генератор для генерации изображений.

### `run`

```python
    @classmethod
    def run(cls, method: str, session: StreamSession, conversation: JsonConversation, data: list = None):
        """Выполняет HTTP-запрос к API Gradio.

        Args:
            method (str): HTTP-метод ("post" или "get").
            session (StreamSession): Асинхровая сессия для выполнения запросов.
            conversation (JsonConversation): Объект, содержащий данные для разговора, такие как токены и UUID.
            data (list, optional): Данные для отправки в запросе. По умолчанию `None`.

        Returns:
            StreamSession: Объект асинхронной сессии с выполненным запросом.

        Raises:
            ResponseError: В случае ошибки при выполнении запроса.

        Как работает функция:
         1. Функция `run` выполняет HTTP-запросы к API Gradio, используя предоставленные параметры.
         2. Заголовки запроса формируются на основе данных разговора и включают токен, UUID и referer.
         3. В зависимости от HTTP-метода, выполняется POST-запрос для присоединения к очереди или GET-запрос для получения данных.

         ASCII flowchart:

         Начало
         ↓
         Заголовки запроса (headers)
         ↓
         Проверка HTTP-метода (method)
         │
         ├─ POST: Выполнение POST-запроса к API Gradio
         │   ↓
         └─ GET: Выполнение GET-запроса к API Gradio
         ↓
         Возврат объекта асинхронной сессии
        """
        ...
```

**Параметры**:
- `method` (str): HTTP-метод ("post" или "get").
- `session` (StreamSession): Асинхровая сессия для выполнения запросов.
- `conversation` (JsonConversation): Объект, содержащий данные для разговора, такие как токены и UUID.
- `data` (list, optional): Данные для отправки в запросе. По умолчанию `None`.

**Возвращает**:
- `StreamSession`: Объект асинхронной сессии с выполненным запросом.

**Вызывает исключения**:
- `ResponseError`: В случае ошибки при выполнении запроса.

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
            model (str): Имя модели.
            messages (Messages): Список сообщений для формирования запроса.
            prompt (str, optional): Текстовый запрос. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            guidance_scale (float, optional): Guidance scale. По умолчанию 3.5.
            num_inference_steps (int, optional): Количество шагов inference. По умолчанию 28.
            seed (int, optional): Seed для генерации. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
            cookies (dict, optional): Cookies для HTTP-запросов. По умолчанию `None`.
            api_key (str, optional): API ключ. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий объекты `ImagePreview`, `ImageResponse` и `Reasoning`.

        Raises:
            RuntimeError: В случае ошибки при парсинге сообщения.
            ResponseError: В случае ошибки ответа от сервера.

        Как работает функция:
          1. Функция `create_async_generator` создает асинхронный генератор для генерации изображений на основе текстового запроса.
          2. Формируется запрос к API Gradio с использованием параметров, таких как модель, текстовый запрос, размеры изображения и другие параметры генерации.
          3. Функция отправляет POST-запрос для присоединения к очереди и GET-запрос для получения данных о процессе генерации.
          4. В процессе генерации возвращаются объекты `ImagePreview` с предварительным просмотром изображения и `Reasoning` с информацией о статусе.
          5. По завершении генерации возвращается объект `ImageResponse` с URL готового изображения.
          6. Функция обрабатывает ошибки, возникающие в процессе генерации, и выбрасывает исключение `RuntimeError` или `ResponseError` в случае необходимости.

        ASCII flowchart:

         Начало
         ↓
         Формирование данных запроса (data)
         ↓
         Создание объекта JsonConversation
         ↓
         Получение ZeroGPU токена (при необходимости)
         ↓
         Выполнение POST-запроса для присоединения к очереди
         ↓
         Выполнение GET-запроса для получения данных о процессе генерации
         │
         ├─ Обработка каждого чанка данных
         │  │
         │  ├─ Обработка сообщений типа 'log' -> Reasoning
         │  │
         │  ├─ Обработка сообщений типа 'progress' -> Reasoning
         │  │
         │  ├─ Обработка сообщений типа 'process_generating' -> ImagePreview
         │  │
         │  └─ Обработка сообщений типа 'process_completed' -> ImageResponse
         │
         ↓
         Конец
        """
        ...
```

**Параметры**:
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Текстовый запрос. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `guidance_scale` (float, optional): Guidance scale. По умолчанию 3.5.
- `num_inference_steps` (int, optional): Количество шагов inference. По умолчанию 28.
- `seed` (int, optional): Seed для генерации. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
- `cookies` (dict, optional): Cookies для HTTP-запросов. По умолчанию `None`.
- `api_key` (str, optional): API ключ. По умолчанию `None`.
- `zerogpu_uuid` (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImagePreview`, `ImageResponse` и `Reasoning`.

**Вызывает исключения**:
- `RuntimeError`: В случае ошибки при парсинге сообщения.
- `ResponseError`: В случае ошибки ответа от сервера.

## Функции

В данном модуле нет отдельных функций, не связанных с классами.