# Модуль PollinationsAI

## Обзор

Модуль `PollinationsAI` предоставляет асинхронный генератор для взаимодействия с API Pollinations AI для генерации текста и изображений. Поддерживает различные модели, включая OpenAI, flux и другие. Позволяет настраивать параметры генерации, такие как температуру, присутствие штрафа и другие.

## Подробнее

Модуль предназначен для интеграции с платформой Pollinations AI, предоставляя удобный интерфейс для генерации контента на основе текста или изображений. Он включает в себя функции для управления моделями, выполнения запросов к API и обработки ответов.

## Классы

### `PollinationsAI`

**Описание**: Класс `PollinationsAI` является основным классом, предоставляющим методы для генерации текста и изображений с использованием API Pollinations AI.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, "Pollinations AI".
- `url` (str): URL сайта Pollinations AI, "https://pollinations.ai".
- `working` (bool): Флаг, указывающий, что провайдер работает, `True`.
- `supports_system_message` (bool): Флаг, указывающий поддержку системных сообщений, `True`.
- `supports_message_history` (bool): Флаг, указывающий поддержку истории сообщений, `True`.
- `text_api_endpoint` (str): URL для API генерации текста, "https://text.pollinations.ai".
- `openai_endpoint` (str): URL для API OpenAI, "https://text.pollinations.ai/openai".
- `image_api_endpoint` (str): URL для API генерации изображений, "https://image.pollinations.ai/".
- `default_model` (str): Модель по умолчанию для генерации текста, "openai".
- `default_image_model` (str): Модель по умолчанию для генерации изображений, "flux".
- `default_vision_model` (str): Модель по умолчанию для задач vision, совпадает с `default_model`.
- `text_models` (list[str]): Список поддерживаемых моделей для генерации текста.
- `image_models` (list[str]): Список поддерживаемых моделей для генерации изображений.
- `extra_image_models` (list[str]): Список дополнительных моделей для генерации изображений.
- `vision_models` (list[str]): Список моделей для vision задач.
- `extra_text_models` (list[str]): Список дополнительных моделей для генерации текста.
- `_models_loaded` (bool): Флаг, указывающий, загружен ли список моделей, `False`.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_models()`: Получает список доступных моделей.
- `create_async_generator()`: Создает асинхронный генератор для генерации текста или изображений.
- `_generate_image()`: Асинхронно генерирует изображения на основе заданных параметров.
- `_generate_text()`: Асинхронно генерирует текст на основе заданных параметров.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, **kwargs):
    """
    Получает список доступных моделей с API Pollinations AI и обновляет атрибуты класса.

    Args:
        **kwargs: Дополнительные аргументы (не используются).

    Returns:
        list[str]: Список доступных текстовых и графических моделей.

    Raises:
        Exception: Если не удается получить модели с API, используются модели по умолчанию.

    Как работает функция:
    1. Проверяет, были ли уже загружены модели (`cls._models_loaded`).
    2. Если модели еще не загружены, пытается получить список моделей изображений с `https://image.pollinations.ai/models`.
    3. Объединяет полученные модели изображений с уже имеющимися моделями (`cls.image_models` и `cls.extra_image_models`), удаляя дубликаты.
    4. Получает список текстовых моделей с `https://text.pollinations.ai/models`.
    5. Извлекает имена моделей чата и аудиомоделей из полученных данных.
    6. Объединяет все текстовые модели, удаляя дубликаты.
    7. Устанавливает флаг `cls._models_loaded` в `True`.
    8. В случае ошибки при получении моделей с API, использует модели по умолчанию, чтобы избежать сбоев.

    ASCII Flowchart:

    Проверка загрузки моделей -> Получение списка моделей изображений -> Объединение моделей изображений
    ↓
    Получение списка текстовых моделей -> Извлечение имен моделей чата и аудиомоделей -> Объединение текстовых моделей
    ↓
    Установка флага загрузки моделей -> Возврат списка моделей
    """
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        proxy: str = None,
        cache: bool = False,
        # Image generation parameters
        prompt: str = None,
        aspect_ratio: str = "1:1",
        width: int = None,
        height: int = None,
        seed: Optional[int] = None,
        nologo: bool = True,
        private: bool = False,
        enhance: bool = False,
        safe: bool = False,
        n: int = 1,
        # Text generation parameters
        media: MediaListType = None,
        temperature: float = None,
        presence_penalty: float = None,
        top_p: float = None,
        frequency_penalty: float = None,
        response_format: Optional[dict] = None,
        extra_parameters: list[str] = ["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "voice", "modalities", "audio"],
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для генерации текста или изображений.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для генерации текста.
            stream (bool, optional): Флаг для стриминга ответов. По умолчанию `True`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            cache (bool, optional): Флаг для использования кэша. По умолчанию `False`.
            prompt (str, optional): Текст запроса для генерации изображения. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            seed (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            nologo (bool, optional): Флаг для удаления логотипа. По умолчанию `True`.
            private (bool, optional): Флаг для приватного использования. По умолчанию `False`.
            enhance (bool, optional): Флаг для улучшения изображения. По умолчанию `False`.
            safe (bool, optional): Флаг для безопасной генерации. По умолчанию `False`.
            n (int, optional): Количество генерируемых изображений. По умолчанию 1.
            media (MediaListType, optional): Список медиафайлов для генерации текста. По умолчанию `None`.
            temperature (float, optional): Температура для генерации текста. По умолчанию `None`.
            presence_penalty (float, optional): Штраф за присутствие для генерации текста. По умолчанию `None`.
            top_p (float, optional): Значение top_p для генерации текста. По умолчанию `None`.
            frequency_penalty (float, optional): Штраф за частоту для генерации текста. По умолчанию `None`.
            response_format (Optional[dict], optional): Формат ответа. По умолчанию `None`.
            extra_parameters (list[str], optional): Список дополнительных параметров для передачи в API.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Части сгенерированного текста или изображения.

        Raises:
            ModelNotFoundError: Если указанная модель не найдена.
            Exception: Если происходит ошибка при генерации.

        Как работает функция:
        1. Загружает список моделей с помощью `cls.get_models()`.
        2. Определяет, является ли модель аудиомоделью.
        3. Получает модель с помощью `cls.get_model(model)`.
        4. Если модель является моделью изображения, вызывает `cls._generate_image()` для генерации изображения.
        5. Иначе вызывает `cls._generate_text()` для генерации текста.

        ASCII Flowchart:

        Загрузка списка моделей -> Определение типа модели (текст/изображение/аудио)
        ↓
        Вызов соответствующего метода генерации (_generate_image или _generate_text) -> Возврат результатов
        """
```

### `_generate_image`

```python
    @classmethod
    async def _generate_image(
        cls,
        model: str,
        prompt: str,
        proxy: str,
        aspect_ratio: str,
        width: int,
        height: int,
        seed: Optional[int],
        cache: bool,
        nologo: bool,
        private: bool,
        enhance: bool,
        safe: bool,
        n: int
    ) -> AsyncResult:
        """
        Асинхронно генерирует изображения на основе заданных параметров.

        Args:
            model (str): Название модели для использования.
            prompt (str): Текст запроса для генерации изображения.
            proxy (str): URL прокси-сервера.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг для использования кэша.
            nologo (bool): Флаг для удаления логотипа.
            private (bool): Флаг для приватного использования.
            enhance (bool): Флаг для улучшения изображения.
            safe (bool): Флаг для безопасной генерации.
            n (int): Количество генерируемых изображений.

        Yields:
            AsyncResult: URL сгенерированного изображения.

        Raises:
            Exception: Если происходит ошибка при получении изображения.

        Как работает функция:
        1. Формирует параметры запроса, включая ширину, высоту, модель, флаги и соотношение сторон.
        2. Кодирует запрос и промпт для URL.
        3. Определяет функцию `get_image_url` для создания URL изображения с учетом зерна и кэширования.
        4. Использует `ClientSession` для выполнения асинхронных GET-запросов к API генерации изображений.
        5. Определяет функцию `get_image` для выполнения запроса и обработки ответа.
        6. Генерирует несколько изображений параллельно с помощью `asyncio.gather`.
        7. Возвращает URL сгенерированных изображений.

        ASCII Flowchart:

        Формирование параметров запроса -> Кодирование запроса и промпта
        ↓
        Определение функции get_image_url -> Выполнение асинхронных GET-запросов
        ↓
        Обработка ответа -> Возврат URL изображений
        """
```

### `_generate_text`

```python
    @classmethod
    async def _generate_text(
        cls,
        model: str,
        messages: Messages,
        media: MediaListType,
        proxy: str,
        temperature: float,
        presence_penalty: float,
        top_p: float,
        frequency_penalty: float,
        response_format: Optional[dict],\
        seed: Optional[int],\
        cache: bool,\
        stream: bool,\
        extra_parameters: list[str],\
        **kwargs\
    ) -> AsyncResult:\
        """\
        Асинхронно генерирует текст на основе заданных параметров.\
\
        Args:\
            model (str): Название модели для использования.\
            messages (Messages): Список сообщений для генерации текста.\
            media (MediaListType): Список медиафайлов для генерации текста.\
            proxy (str): URL прокси-сервера.\
            temperature (float): Температура для генерации текста.\
            presence_penalty (float): Штраф за присутствие для генерации текста.\
            top_p (float): Значение top_p для генерации текста.\
            frequency_penalty (float): Штраф за частоту для генерации текста.\
            response_format (Optional[dict]): Формат ответа.\
            seed (Optional[int]): Зерно для генерации случайных чисел.\
            cache (bool): Флаг для использования кэша.\
            stream (bool): Флаг для стриминга ответов.\
            extra_parameters (list[str]): Список дополнительных параметров для передачи в API.\
            **kwargs: Дополнительные аргументы.\
\
        Yields:\
            AsyncResult: Части сгенерированного текста.\
\
        Raises:\
            Exception: Если происходит ошибка при генерации текста.\
\
        Как работает функция:\
        1. Инициализирует зерно случайных чисел, если оно не задано и кэширование не используется.\
        2. Определяет, включен ли режим JSON.\
        3. Использует `ClientSession` для выполнения асинхронных POST-запросов к API генерации текста.\
        4. Формирует параметры запроса, включая сообщения, модель, температуру, штрафы и другие параметры.\
        5. Выполняет POST-запрос к API и обрабатывает ответ.\
        6. Если ответ содержит медиафайлы, сохраняет их.\
        7. Если ответ имеет тип `text/plain`, возвращает текст ответа.\
        8. Если ответ имеет тип `text/event-stream`, обрабатывает стриминговый ответ.\
        9. Иначе обрабатывает JSON-ответ и извлекает сгенерированный текст.\
\
        ASCII Flowchart:\
\
        Инициализация зерна -> Определение режима JSON\
        ↓\
        Формирование параметров запроса -> Выполнение POST-запроса\
        ↓\
        Обработка ответа (медиафайлы/текст/стриминг/JSON) -> Возврат сгенерированного текста\
        """