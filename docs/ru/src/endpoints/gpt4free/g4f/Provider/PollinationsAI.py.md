# Модуль `PollinationsAI`

## Обзор

Модуль `PollinationsAI` предоставляет асинхронный интерфейс для взаимодействия с сервисом Pollinations AI, который позволяет генерировать текст и изображения на основе различных моделей. Он поддерживает потоковую передачу результатов, работу с прокси и кэширование.

## Подробней

Модуль предназначен для интеграции в проекты, требующие генерации контента с использованием AI. Он включает в себя функциональность для выбора модели, форматирования запросов и обработки ответов от API Pollinations AI.

## Классы

### `PollinationsAI`

**Описание**: Класс `PollinationsAI` является основным классом для взаимодействия с сервисом Pollinations AI.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, значение: `"Pollinations AI"`.
- `url` (str): URL сервиса Pollinations AI, значение: `"https://pollinations.ai"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, значение: `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений, значение: `True`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений, значение: `True`.
- `text_api_endpoint` (str): URL для API генерации текста, значение: `"https://text.pollinations.ai"`.
- `openai_endpoint` (str): URL для API OpenAI, значение: `"https://text.pollinations.ai/openai"`.
- `image_api_endpoint` (str): URL для API генерации изображений, значение: `"https://image.pollinations.ai/"`.
- `default_model` (str): Модель по умолчанию для генерации текста, значение: `"openai"`.
- `default_image_model` (str): Модель по умолчанию для генерации изображений, значение: `"flux"`.
- `default_vision_model` (str): Модель по умолчанию для vision, значение: `default_model`.
- `text_models` (list[str]): Список поддерживаемых моделей для генерации текста, включает `default_model`.
- `image_models` (list[str]): Список поддерживаемых моделей для генерации изображений, включает `default_image_model`.
- `extra_image_models` (list[str]): Список дополнительных моделей для генерации изображений.
- `vision_models` (list[str]): Список поддерживаемых моделей для vision, включает `default_vision_model`.
- `extra_text_models` (list[str]): Список дополнительных моделей для генерации текста.
- `_models_loaded` (bool): Флаг, указывающий, были ли загружены модели, значение: `False`.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_models(**kwargs)`: Получает список доступных моделей.
- `create_async_generator(model, messages, stream, proxy, cache, prompt, aspect_ratio, width, height, seed, nologo, private, enhance, safe, n, media, temperature, presence_penalty, top_p, frequency_penalty, response_format, extra_parameters, **kwargs)`: Создает асинхронный генератор для генерации текста или изображений.
- `_generate_image(model, prompt, proxy, aspect_ratio, width, height, seed, cache, nologo, private, enhance, safe, n)`: Генерирует изображения.
- `_generate_text(model, messages, media, proxy, temperature, presence_penalty, top_p, frequency_penalty, response_format, seed, cache, stream, extra_parameters, **kwargs)`: Генерирует текст.

## Функции

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Получает список доступных моделей для генерации текста и изображений.

        Args:
            **kwargs: Дополнительные аргументы.

        Returns:
            list[str]: Список доступных моделей.

        Raises:
            Exception: Если не удается получить список моделей с API.

        Как работает функция:
        1. Проверяет, были ли уже загружены модели. Если да, возвращает текущий список.
        2. Если модели еще не загружены, пытается получить списки моделей для изображений и текста с соответствующих API.
        3. Объединяет полученные списки моделей, удаляя дубликаты.
        4. В случае ошибки при получении списков моделей, использует модели по умолчанию.
        5. Устанавливает флаг `_models_loaded` в `True`.

        ASCII flowchart:
        A: Проверка `cls._models_loaded`
        |
        -- B: Запрос к API изображений и текстов
        |
        C: Объединение моделей
        |
        D: Обработка исключений -> E: Использование моделей по умолчанию
        |
        F: `cls._models_loaded = True`

        Примеры:
            >>> PollinationsAI.get_models()
            ['openai', 'flux']
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
        """Создает асинхронный генератор для генерации текста или изображений.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для генерации.
            stream (bool): Флаг, указывающий на потоковую передачу результатов.
            proxy (str): URL прокси-сервера.
            cache (bool): Флаг, указывающий на использование кэша.
            prompt (str): Текст запроса для генерации изображения.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            nologo (bool): Флаг, указывающий на необходимость удаления логотипа.
            private (bool): Флаг, указывающий на приватность генерации.
            enhance (bool): Флаг, указывающий на улучшение качества изображения.
            safe (bool): Флаг, указывающий на безопасный режим.
            n (int): Количество генерируемых изображений.
            media (MediaListType): Список медиа-файлов.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие токенов.
            top_p (float): Вероятность выбора наиболее вероятного токена.
            frequency_penalty (float): Штраф за частоту токенов.
            response_format (Optional[dict]): Формат ответа.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Асинхронный результат генерации.

        Raises:
            ModelNotFoundError: Если указанная модель не найдена.
            Exception: Если произошла ошибка при генерации.

        Как работает функция:
        1. Загружает список доступных моделей.
        2. Определяет, является ли запрошенная модель моделью для генерации изображений или текста.
        3. Вызывает соответствующий метод (`_generate_image` или `_generate_text`) для генерации контента.

        ASCII flowchart:
        A: Загрузка моделей
        |
        -- B: Определение типа модели (изображение/текст)
        |
        C: Вызов `_generate_image` или `_generate_text`
        |
        D: Генерация контента и передача результата

        Примеры:
            >>> async for result in PollinationsAI.create_async_generator(model='openai', messages=[{'role': 'user', 'content': 'Hello'}]):
            ...     print(result)

            >>> async for result in PollinationsAI.create_async_generator(model='flux', prompt='A cat', aspect_ratio='16:9'):
            ...     print(result)
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
        """Генерирует изображения на основе заданных параметров.

        Args:
            model (str): Название модели для генерации изображений.
            prompt (str): Текст запроса для генерации изображения.
            proxy (str): URL прокси-сервера.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг, указывающий на использование кэша.
            nologo (bool): Флаг, указывающий на необходимость удаления логотипа.
            private (bool): Флаг, указывающий на приватность генерации.
            enhance (bool): Флаг, указывающий на улучшение качества изображения.
            safe (bool): Флаг, указывающий на безопасный режим.
            n (int): Количество генерируемых изображений.

        Yields:
            AsyncResult: Асинхронный результат генерации изображения.

        Raises:
            Exception: Если произошла ошибка при получении изображения.

        Как работает функция:
        1. Формирует параметры запроса на основе переданных аргументов.
        2. Генерирует URL для запроса к API генерации изображений.
        3. Отправляет асинхронный запрос к API и получает изображение.

        ASCII flowchart:
        A: Формирование параметров запроса
        |
        -- B: Генерация URL запроса
        |
        C: Асинхронный запрос к API
        |
        D: Получение и передача изображения

        Примеры:
            >>> async for result in PollinationsAI._generate_image(model='flux', prompt='A cat', aspect_ratio='16:9', proxy=None, width=512, height=512, seed=None, cache=False, nologo=True, private=False, enhance=False, safe=True, n=1):
            ...     print(result)
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
        response_format: Optional[dict],
        seed: Optional[int],
        cache: bool,
        stream: bool,
        extra_parameters: list[str],
        **kwargs
    ) -> AsyncResult:
        """Генерирует текст на основе заданных параметров.

        Args:
            model (str): Название модели для генерации текста.
            messages (Messages): Список сообщений для генерации.
            media (MediaListType): Список медиа-файлов.
            proxy (str): URL прокси-сервера.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие токенов.
            top_p (float): Вероятность выбора наиболее вероятного токена.
            frequency_penalty (float): Штраф за частоту токенов.
            response_format (Optional[dict]): Формат ответа.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг, указывающий на использование кэша.
            stream (bool): Флаг, указывающий на потоковую передачу результатов.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Асинхронный результат генерации текста.

        Raises:
            Exception: Если произошла ошибка при генерации текста.

        Как работает функция:
        1. Формирует параметры запроса на основе переданных аргументов.
        2. Генерирует URL для запроса к API генерации текста.
        3. Отправляет асинхронный запрос к API и получает текст.

        ASCII flowchart:
        A: Формирование параметров запроса
        |
        -- B: Генерация URL запроса
        |
        C: Асинхронный запрос к API
        |
        D: Получение и передача текста

        Примеры:
            >>> async for result in PollinationsAI._generate_text(model='openai', messages=[{'role': 'user', 'content': 'Hello'}], media=None, proxy=None, temperature=0.7, presence_penalty=0.0, top_p=1.0, frequency_penalty=0.0, response_format=None, seed=None, cache=False, stream=True, extra_parameters=[]):
            ...     print(result)
        """