# Модуль PollinationsAI

## Обзор

Модуль `PollinationsAI` предоставляет асинхронный интерфейс для взаимодействия с API Pollinations AI, который позволяет генерировать как текст, так и изображения. Он поддерживает потоковую передачу данных и различные модели, включая OpenAI и другие.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими функциональности генерации контента с использованием моделей Pollinations AI.
Он обеспечивает гибкий способ взаимодействия с API, поддерживая различные параметры настройки, такие как выбор модели, прокси, кэширование и т. д.

## Классы

### `PollinationsAI`

**Описание**: Класс `PollinationsAI` является основным классом, предоставляющим методы для генерации текста и изображений с использованием API Pollinations AI.

**Принцип работы**:

1.  Инициализация: Класс инициализируется с настройками по умолчанию, такими как базовые URL для API, список поддерживаемых моделей и заголовки HTTP.
2.  Получение моделей: Метод `get_models` используется для динамического получения списка доступных моделей как для текста, так и для изображений.
3.  Генерация контента: Методы `create_async_generator`, `_generate_image` и `_generate_text` предоставляют интерфейс для генерации изображений и текста соответственно. Они принимают параметры, такие как модель, входные сообщения, настройки прокси и другие параметры конфигурации.
4.  Обработка ответов: Класс обрабатывает ответы от API, включая потоковую передачу и ошибки, и возвращает результаты в формате, подходящем для дальнейшей обработки.

**Методы**:

*   `get_models(cls, **kwargs)`: Получает и обновляет список доступных моделей для генерации текста и изображений из API Pollinations AI.
*   `create_async_generator(cls, model: str, messages: Messages, stream: bool = True, proxy: str = None, cache: bool = False, prompt: str = None, aspect_ratio: str = "1:1", width: int = None, height: int = None, seed: Optional[int] = None, nologo: bool = True, private: bool = False, enhance: bool = False, safe: bool = False, n: int = 1, media: MediaListType = None, temperature: float = None, presence_penalty: float = None, top_p: float = None, frequency_penalty: float = None, response_format: Optional[dict] = None, extra_parameters: list[str] = ["tools", "parallel_tool_calls", "tool_choice", "reasoning_effort", "logit_bias", "voice", "modalities", "audio"], **kwargs) -> AsyncResult`: Создает асинхронный генератор для генерации текста или изображений на основе предоставленных параметров.
*   `_generate_image(cls, model: str, prompt: str, proxy: str, aspect_ratio: str, width: int, height: int, seed: Optional[int], cache: bool, nologo: bool, private: bool, enhance: bool, safe: bool, n: int) -> AsyncResult`: Генерирует изображения с использованием API Pollinations AI на основе предоставленных параметров.
*   `_generate_text(cls, model: str, messages: Messages, media: MediaListType, proxy: str, temperature: float, presence_penalty: float, top_p: float, frequency_penalty: float, response_format: Optional[dict], seed: Optional[int], cache: bool, stream: bool, extra_parameters: list[str], **kwargs) -> AsyncResult`: Генерирует текст с использованием API Pollinations AI на основе предоставленных параметров.

## Функции

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Получает и обновляет список доступных моделей для генерации текста и изображений из API Pollinations AI.

        Args:
            **kwargs: Дополнительные параметры.

        Returns:
            list: Список доступных моделей, объединяющий текстовые и графические модели.

        Как работает функция:
        1. Проверяет, загружены ли уже модели. Если нет, пытается загрузить их из API.
        2. Запрашивает список графических моделей с `https://image.pollinations.ai/models`.
        3. Запрашивает список текстовых моделей с `https://text.pollinations.ai/models`.
        4. Объединяет полученные списки моделей, удаляя дубликаты.
        5. В случае ошибки при запросе моделей использует модели по умолчанию.

        Внутри функции происходят следующие действия и преобразования:
        A - Получение списка графических моделей: Отправляет GET-запрос к API для получения списка графических моделей.
        |
        B - Обработка ответа графических моделей: Обрабатывает полученный ответ, извлекая список доступных графических моделей.
        |
        C - Получение списка текстовых моделей: Отправляет GET-запрос к API для получения списка текстовых моделей.
        |
        D - Обработка ответа текстовых моделей: Обрабатывает полученный ответ, извлекая список доступных текстовых моделей.
        |
        E - Объединение списков моделей: Объединяет списки графических и текстовых моделей, удаляя дубликаты.
        |
        F - Обработка ошибок: В случае возникновения ошибки при получении списков моделей, использует списки моделей по умолчанию.

        Примеры:
            >>> PollinationsAI.get_models()
            ['openai', 'flux']
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
        """Создает асинхронный генератор для генерации текста или изображений на основе предоставленных параметров.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для генерации текста.
            stream (bool, optional): Флаг для потоковой передачи данных. По умолчанию `True`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            cache (bool, optional): Флаг для использования кэша. По умолчанию `False`.
            prompt (str, optional): Текст запроса для генерации изображения. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию `"1:1"`.
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            seed (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            nologo (bool, optional): Флаг для удаления логотипа. По умолчанию `True`.
            private (bool, optional): Флаг для приватности. По умолчанию `False`.
            enhance (bool, optional): Флаг для улучшения изображения. По умолчанию `False`.
            safe (bool, optional): Флаг для безопасного режима. По умолчанию `False`.
            n (int, optional): Количество генерируемых изображений. По умолчанию `1`.
            media (MediaListType, optional): Список медиафайлов. По умолчанию `None`.
            temperature (float, optional): Температура для генерации текста. По умолчанию `None`.
            presence_penalty (float, optional): Штраф за присутствие токена. По умолчанию `None`.
            top_p (float, optional): Вероятность выбора наиболее вероятного токена. По умолчанию `None`.
            frequency_penalty (float, optional): Штраф за частоту токена. По умолчанию `None`.
            response_format (Optional[dict], optional): Формат ответа. По умолчанию `None`.
            extra_parameters (list[str], optional): Список дополнительных параметров.
            **kwargs: Дополнительные параметры.

        Yields:
            AsyncResult: Асинхронный генератор, возвращающий сгенерированный текст или изображение.

        Raises:
            ModelNotFoundError: Если указанная модель не найдена.

        Как работает функция:
        1. Загружает список доступных моделей.
        2. Определяет, является ли запрошенная модель графической или текстовой.
        3. Вызывает соответствующий метод для генерации изображения или текста.

        Внутри функции происходят следующие действия и преобразования:
        A - Загрузка списка моделей: Вызывает метод `get_models` для загрузки списка доступных моделей.
        |
        B - Определение типа модели: Проверяет, является ли запрошенная модель графической или текстовой.
        |
        C - Генерация изображения: Если модель графическая, вызывает метод `_generate_image` для генерации изображения.
        |
        D - Генерация текста: Если модель текстовая, вызывает метод `_generate_text` для генерации текста.

        Примеры:
            >>> async for chunk in PollinationsAI.create_async_generator(model='openai', messages=[{'role': 'user', 'content': 'Hello'}]):
            ...     print(chunk)
        """
        ...
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
        """Генерирует изображения с использованием API Pollinations AI на основе предоставленных параметров.

        Args:
            model (str): Имя модели для использования.
            prompt (str): Текст запроса для генерации изображения.
            proxy (str): URL прокси-сервера.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг для использования кэша.
            nologo (bool): Флаг для удаления логотипа.
            private (bool): Флаг для приватности.
            enhance (bool): Флаг для улучшения изображения.
            safe (bool): Флаг для безопасного режима.
            n (int): Количество генерируемых изображений.

        Yields:
            AsyncResult: Асинхронный генератор, возвращающий URL сгенерированного изображения.

        Как работает функция:
        1. Формирует параметры запроса на основе предоставленных аргументов.
        2. Кодирует текст запроса и параметры в URL.
        3. Отправляет асинхронный GET-запрос к API для генерации изображения.
        4. Возвращает URL сгенерированного изображения.

        Внутри функции происходят следующие действия и преобразования:
        A - Формирование параметров запроса: Формирует словарь с параметрами запроса на основе предоставленных аргументов.
        |
        B - Кодирование параметров в URL: Кодирует параметры запроса в URL-формат.
        |
        C - Отправка GET-запроса: Отправляет асинхронный GET-запрос к API для генерации изображения.
        |
        D - Обработка ответа: Обрабатывает ответ от API, извлекая URL сгенерированного изображения.
        |
        E - Возврат URL изображения: Возвращает URL сгенерированного изображения.

        Примеры:
            >>> async for chunk in PollinationsAI._generate_image(model='flux', prompt='A cat', proxy=None, aspect_ratio='1:1', width=512, height=512, seed=None, cache=False, nologo=True, private=False, enhance=False, safe=True, n=1):
            ...     print(chunk)
        """
        ...
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
        extra_parameters: list[str],\n        **kwargs\n    ) -> AsyncResult:
        """Генерирует текст с использованием API Pollinations AI на основе предоставленных параметров.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для генерации текста.
            media (MediaListType): Список медиафайлов.
            proxy (str): URL прокси-сервера.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие токена.
            top_p (float): Вероятность выбора наиболее вероятного токена.
            frequency_penalty (float): Штраф за частоту токена.
            response_format (Optional[dict]): Формат ответа.
            seed (Optional[int]): Зерно для генерации случайных чисел.
            cache (bool): Флаг для использования кэша.
            stream (bool): Флаг для потоковой передачи данных.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные параметры.

        Yields:
            AsyncResult: Асинхронный генератор, возвращающий сгенерированный текст.

        Как работает функция:
        1.  Формирует параметры запроса на основе предоставленных аргументов.
        2.  Отправляет асинхронный POST-запрос к API для генерации текста.
        3.  Обрабатывает ответ от API, возвращая сгенерированный текст.

        Внутри функции происходят следующие действия и преобразования:
        A - Формирование параметров запроса: Формирует словарь с параметрами запроса на основе предоставленных аргументов, включая сообщения, модель, температуру и другие параметры.
        |
        B - Отправка POST-запроса: Отправляет асинхронный POST-запрос к API для генерации текста с использованием сформированных параметров.
        |
        C - Обработка ответа: Обрабатывает ответ от API, проверяя тип контента и возвращая сгенерированный текст, информацию об использовании ресурсов и причину завершения.

        Примеры:
            >>> async for chunk in PollinationsAI._generate_text(model='openai', messages=[{'role': 'user', 'content': 'Hello'}], media=None, proxy=None, temperature=0.7, presence_penalty=0.0, top_p=1.0, frequency_penalty=0.0, response_format=None, seed=None, cache=False, stream=True, extra_parameters=[]):
            ...     print(chunk)
        """
        ...