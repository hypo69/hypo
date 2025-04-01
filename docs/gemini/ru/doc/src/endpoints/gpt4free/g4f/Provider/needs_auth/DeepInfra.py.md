# Модуль `DeepInfra.py`

## Обзор

Модуль предоставляет класс `DeepInfra`, который является адаптером для взаимодействия с API DeepInfra. DeepInfra предоставляет доступ к различным моделям, включая модели генерации текста и модели генерации изображений. Модуль включает методы для получения списка доступных моделей, создания запросов к API для генерации текста и изображений, а также обработки ответов от API.

## Подробней

Модуль `DeepInfra.py` расположен в директории `hypotez/src/endpoints/gpt4free/g4f/Provider/needs_auth/`. Это указывает на то, что модуль является частью системы `hypotez`, использующей GPT-4 (или аналогичную технологию) через провайдера DeepInfra и требует аутентификации.

Класс `DeepInfra` наследуется от `OpenaiTemplate`, что предполагает использование шаблона, аналогичного OpenAI, для взаимодействия с API.

Модуль содержит методы для получения моделей, как для генерации текста, так и для генерации изображений, и использует асинхронные генераторы для обработки потоковых ответов от API.

## Классы

### `DeepInfra`

**Описание**: Класс для взаимодействия с API DeepInfra.

**Наследует**:

- `OpenaiTemplate`: Предоставляет базовый функционал для взаимодействия с API, использующими шаблоны OpenAI.

**Атрибуты**:

- `url` (str): URL главной страницы DeepInfra.
- `login_url` (str): URL страницы для получения ключей API DeepInfra.
- `api_base` (str): Базовый URL API DeepInfra.
- `working` (bool): Указывает, что провайдер в данный момент работает.
- `needs_auth` (bool): Указывает, что для работы с API требуется аутентификация.
- `default_model` (str): Модель, используемая по умолчанию для генерации текста.
- `default_image_model` (str): Модель, используемая по умолчанию для генерации изображений.
- `models` (list): Список доступных текстовых моделей.
- `image_models` (list): Список доступных моделей для генерации изображений.

**Методы**:

- `get_models(**kwargs)`: Получает список доступных моделей.
- `get_image_models(**kwargs)`: Получает список доступных моделей для генерации изображений.
- `create_async_generator(model: str, messages: Messages, stream: bool, prompt: str = None, temperature: float = 0.7, max_tokens: int = 1028, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения текстовых ответов от API.
- `create_async_image(prompt: str, model: str, api_key: str = None, api_base: str = "https://api.deepinfra.com/v1/inference", proxy: str = None, timeout: int = 180, extra_data: dict = {}, **kwargs) -> ImageResponse`: Создает асинхронный запрос для генерации изображений через API.

## Функции

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Получает список доступных моделей из API DeepInfra.

        Args:
            **kwargs: Дополнительные параметры для запроса.

        Returns:
            list: Список доступных моделей.

        Как работает функция:
        1. Проверяет, были ли уже загружены модели (cls.models). Если да, возвращает сохраненный список.
        2. Если модели еще не загружены, отправляет GET-запрос к API DeepInfra для получения списка моделей.
        3. Обрабатывает ответ API, разделяя модели на текстовые и графические, и сохраняет их в cls.models и cls.image_models соответственно.
        4. Объединяет списки моделей в cls.models и возвращает его.

        flowchart:

        A[Проверка загруженных моделей]
        |\n
        B[Запрос к API DeepInfra]
        |\n
        C[Обработка ответа API и разделение моделей]
        |\n
        D[Сохранение моделей в cls.models и cls.image_models]
        |\n
        E[Возврат списка моделей]

        Примеры:
            >>> DeepInfra.get_models()
            ['meta-llama/Meta-Llama-3.1-70B-Instruct', 'stabilityai/sd3.5']
        """
        if not cls.models:
            url = 'https://api.deepinfra.com/models/featured'
            response = requests.get(url)
            models = response.json()
            
            cls.models = []
            cls.image_models = []
            
            for model in models:
                if model["type"] == "text-generation":
                    cls.models.append(model['model_name'])
                elif model["reported_type"] == "text-to-image":
                    cls.image_models.append(model['model_name'])
            
            cls.models.extend(cls.image_models)

        return cls.models
```

### `get_image_models`

```python
    @classmethod
    def get_image_models(cls, **kwargs):
        """Получает список доступных моделей для генерации изображений из API DeepInfra.

        Args:
            **kwargs: Дополнительные параметры для запроса.

        Returns:
            list: Список доступных моделей для генерации изображений.

        Как работает функция:
        1. Проверяет, были ли уже загружены модели изображений (cls.image_models).
        2. Если список моделей изображений пуст, вызывает cls.get_models() для загрузки всех моделей.
        3. Возвращает сохраненный список моделей изображений (cls.image_models).

        flowchart:

        A[Проверка загруженных моделей изображений]
        |\n
        B[Вызов cls.get_models() при необходимости]
        |\n
        C[Возврат списка моделей изображений]

        Примеры:
            >>> DeepInfra.get_image_models()
            ['stabilityai/sd3.5']
        """
        if not cls.image_models:
            cls.get_models()
        return cls.image_models
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        prompt: str = None,
        temperature: float = 0.7,
        max_tokens: int = 1028,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения текстовых ответов от API DeepInfra.

        Args:
            model (str): Имя модели для генерации текста.
            messages (Messages): Список сообщений для передачи в модель.
            stream (bool): Флаг, указывающий, следует ли использовать потоковый режим.
            prompt (str, optional): Дополнительный промт для генерации текста. По умолчанию None.
            temperature (float, optional): Температура для генерации текста. По умолчанию 0.7.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 1028.
            **kwargs: Дополнительные параметры для запроса.

        Returns:
            AsyncResult: Асинхронный генератор для получения текстовых ответов.

        Как работает функция:
        1. Проверяет, является ли запрошенная модель моделью для генерации изображений. Если да, вызывает `cls.create_async_image` и возвращает результат.
        2. Если модель предназначена для генерации текста, устанавливает заголовки для запроса к API DeepInfra.
        3. Вызывает метод `super().create_async_generator` для выполнения запроса к API с использованием параметров и заголовков.
        4. Возвращает асинхронный генератор, который предоставляет чанки текста из ответа API.

        flowchart:

        A[Проверка типа модели (текст/изображение)]
        |\n
        B[Вызов cls.create_async_image (если изображение)]
        |\n
        C[Установка заголовков для запроса API]
        |\n
        D[Вызов super().create_async_generator]
        |\n
        E[Возврат асинхронного генератора для текстовых ответов]

        Примеры:
            >>> async for chunk in DeepInfra.create_async_generator(model='meta-llama/Meta-Llama-3.1-70B-Instruct', messages=[{'role': 'user', 'content': 'Hello'}]):
            ...     print(chunk)
            Hello!
        """
        if model in cls.get_image_models():
            yield cls.create_async_image(
                format_image_prompt(messages, prompt),
                model,
                **kwargs
            )
            return

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'Origin': 'https://deepinfra.com',
            'Referer': 'https://deepinfra.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Deepinfra-Source': 'web-embed',
        }
        async for chunk in super().create_async_generator(
            model, messages,
            stream=stream,
            temperature=temperature,
            max_tokens=max_tokens,
            headers=headers,
            **kwargs
        ):
            yield chunk
```

### `create_async_image`

```python
    @classmethod
    async def create_async_image(
        cls,
        prompt: str,
        model: str,
        api_key: str = None,
        api_base: str = "https://api.deepinfra.com/v1/inference",
        proxy: str = None,
        timeout: int = 180,
        extra_data: dict = {},
        **kwargs
    ) -> ImageResponse:
        """Создает асинхронный запрос для генерации изображений через API DeepInfra.

        Args:
            prompt (str): Текст запроса для генерации изображения.
            model (str): Имя модели для генерации изображений.
            api_key (str, optional): Ключ API для аутентификации. По умолчанию None.
            api_base (str, optional): Базовый URL API DeepInfra. По умолчанию "https://api.deepinfra.com/v1/inference".
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию None.
            timeout (int, optional): Максимальное время ожидания ответа от API. По умолчанию 180.
            extra_data (dict, optional): Дополнительные данные для передачи в запросе. По умолчанию {}.
            **kwargs: Дополнительные параметры для запроса.

        Returns:
            ImageResponse: Объект ImageResponse, содержащий сгенерированное изображение.

        Raises:
            RuntimeError: Если API возвращает ошибку или не возвращает изображение.

        Как работает функция:
        1. Устанавливает заголовки для запроса к API DeepInfra, включая информацию о браузере и источнике запроса.
        2. Если предоставлен ключ API, добавляет его в заголовок Authorization.
        3. Создает асинхронную сессию с использованием StreamSession и переданных параметров (прокси, заголовки, таймаут).
        4. Получает имя модели, приводя его к нужному формату.
        5. Формирует данные запроса, включая текст запроса (prompt) и дополнительные данные (extra_data).
        6. Отправляет POST-запрос к API DeepInfra с сформированными данными.
        7. Обрабатывает ответ API, извлекая URL изображения из ответа.
        8. Возвращает объект ImageResponse, содержащий URL изображения и текст запроса.
        9. В случае ошибки API или отсутствия изображения в ответе, вызывает исключение RuntimeError.

        flowchart:

        A[Установка заголовков для запроса API]
        |\n
        B[Добавление ключа API в заголовок (если есть)]
        |\n
        C[Создание асинхронной сессии]
        |\n
        D[Формирование данных запроса (prompt + extra_data)]
        |\n
        E[Отправка POST-запроса к API DeepInfra]
        |\n
        F[Обработка ответа API и извлечение URL изображения]
        |\n
        G[Возврат объекта ImageResponse]
        |\n
        H[Вызов исключения RuntimeError (если ошибка API или нет изображения)]

        Примеры:
            >>> image_response = await DeepInfra.create_async_image(prompt='A cat', model='stabilityai/sd3.5', api_key='YOUR_API_KEY')
            >>> print(image_response.image_url)
            https://example.com/image.jpg
        """
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'Connection': 'keep-alive',
            'Origin': 'https://deepinfra.com',
            'Referer': 'https://deepinfra.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Deepinfra-Source': 'web-embed',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"
        async with StreamSession(
            proxies={"all": proxy},
            headers=headers,
            timeout=timeout
        ) as session:
            model = cls.get_model(model)
            data = {"prompt": prompt, **extra_data}
            data = {"input": data} if model == cls.default_model else data
            async with session.post(f"{api_base.rstrip('/')}/{model}", json=data) as response:
                await raise_for_status(response)
                data = await response.json()
                images = data.get("output", data.get("images", data.get("image_url")))
                if not images:
                    raise RuntimeError(f"Response: {data}")
                images = images[0] if len(images) == 1 else images
                return ImageResponse(images, prompt)