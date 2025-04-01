# Модуль `Prodia`

## Обзор

Модуль `Prodia` предоставляет асинхронный интерфейс для взаимодействия с API сервиса Prodia для генерации изображений. Он позволяет генерировать изображения на основе текстовых запросов (prompt) с использованием различных моделей и параметров.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими функциональность генерации изображений. Он предоставляет возможность выбора модели, задания параметров генерации, таких как количество шагов, коэффициент cfg, seed и aspect ratio. Модуль использует асинхронные запросы для неблокирующего взаимодействия с API Prodia.

## Классы

### `Prodia`

**Описание**: Класс `Prodia` является асинхронным провайдером и миксином для работы с API Prodia. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных провайдеров, генерирующих данные.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `url` (str): Базовый URL сервиса Prodia (`"https://app.prodia.com"`).
- `api_endpoint` (str): URL API для генерации изображений (`"https://api.prodia.com/generate"`).
- `working` (bool): Указывает, работает ли провайдер в данный момент (по умолчанию `False`).
- `default_model` (str): Модель, используемая по умолчанию (`'absolutereality_v181.safetensors [3d9d4d2b]'`).
- `default_image_model` (str): Модель изображения, используемая по умолчанию (совпадает с `default_model`).
- `image_models` (List[str]): Список доступных моделей изображений.
- `models` (List[str]): Список всех доступных моделей (в данном случае совпадает с `image_models`).

**Методы**:
- `get_model(model: str) -> str`: Возвращает имя модели на основе входного параметра, проверяя наличие в списке доступных моделей и алиасов.
- `create_async_generator(...) -> AsyncResult`: Асинхронный генератор для создания изображений на основе заданных параметров.
- `_poll_job(...) -> str`: Асинхронный метод для опроса статуса задачи генерации изображения.

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str) -> str:
        """
        Возвращает имя модели на основе входного параметра.

        Args:
            model (str): Имя модели.

        Returns:
            str: Имя модели, если она найдена в списке доступных моделей или алиасов, иначе возвращает модель по умолчанию.

        Как работает функция:
        1. Проверяет, входит ли входная модель в список доступных моделей (`cls.models`).
        2. Если нет, проверяет, входит ли модель в список алиасов моделей (`cls.model_aliases`).
        3. Если модель не найдена ни в одном из списков, возвращает модель по умолчанию (`cls.default_model`).

        A --> B --> C --> D
        |       |       |
        (model in   (model in     (return
        cls.models)   cls.model_aliases)  cls.default_model)
        
        Примеры:
            >>> Prodia.get_model('absolutereality_v181.safetensors [3d9d4d2b]')
            'absolutereality_v181.safetensors [3d9d4d2b]'

            >>> Prodia.get_model('non_existent_model')
            'absolutereality_v181.safetensors [3d9d4d2b]'
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
        proxy: str = None,
        negative_prompt: str = "",
        steps: str = 20, # 1-25
        cfg: str = 7, # 0-20
        seed: Optional[int] = None,
        sampler: str = "DPM++ 2M Karras", # "Euler", "Euler a", "Heun", "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM"
        aspect_ratio: str = "square", # "square", "portrait", "landscape"
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для создания изображений на основе заданных параметров.

        Args:
            model (str): Имя модели для генерации изображения.
            messages (Messages): Список сообщений, содержащих текстовый запрос (prompt).
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            negative_prompt (str, optional): Негативный запрос, описывающий, что не должно быть на изображении. По умолчанию "".
            steps (str, optional): Количество шагов для генерации изображения (1-25). По умолчанию "20".
            cfg (str, optional): Коэффициент соответствия запросу (0-20). По умолчанию "7".
            seed (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            sampler (str, optional): Метод дискретизации. По умолчанию "DPM++ 2M Karras".
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "square".
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий объект `ImageResponse` с URL сгенерированного изображения.

        Как работает функция:
        1. Получает имя модели с помощью `cls.get_model(model)`.
        2. Если `seed` не задан, генерирует случайное зерно.
        3. Формирует заголовки запроса.
        4. Создает асинхронную сессию `aiohttp.ClientSession` с заданными заголовками.
        5. Извлекает текстовый запрос из списка сообщений (`messages`).
        6. Формирует параметры запроса `params` для API Prodia.
        7. Отправляет GET-запрос к API Prodia с заданными параметрами и прокси.
        8. Получает `job_id` из ответа API.
        9. Опрашивает API с помощью `cls._poll_job` до тех пор, пока задача не будет выполнена или не произойдет ошибка.
        10. Возвращает объект `ImageResponse` с URL сгенерированного изображения.

        A --> B --> C --> D --> E --> F --> G --> H --> I
        |       |       |       |       |       |       |       |
        (get_model   (seed      (create    (extract  (create   (send     (get        (poll_job  (return
        model)     is None)    headers)  prompt)   params)   request)  job_id)     image_url)   ImageResponse)

        Примеры:
            # Пример использования функции create_async_generator
            # В данном случае необходимо создать тестовые messages, чтобы пример был полным
            >>> messages = [{'content': 'A beautiful landscape'}]
            >>> async def test():
            ...     async for image_response in Prodia.create_async_generator(model='absolutereality_v181.safetensors [3d9d4d2b]', messages=messages):
            ...         print(image_response.url)

        """
        ...
```

### `_poll_job`

```python
    @classmethod
    async def _poll_job(cls, session: ClientSession, job_id: str, proxy: str, max_attempts: int = 30, delay: int = 2) -> str:
        """
        Опрашивает API до тех пор, пока задача не будет выполнена или не произойдет ошибка.

        Args:
            session (ClientSession): Асинхронная сессия для выполнения запросов.
            job_id (str): Идентификатор задачи.
            proxy (str): Прокси-сервер для использования.
            max_attempts (int, optional): Максимальное количество попыток опроса. По умолчанию 30.
            delay (int, optional): Задержка между попытками в секундах. По умолчанию 2.

        Returns:
            str: URL сгенерированного изображения.

        Raises:
            Exception: Если задача завершилась с ошибкой или превышено максимальное количество попыток.

        Как работает функция:
        1. Выполняет цикл опроса API до тех пор, пока не будет достигнуто максимальное количество попыток (`max_attempts`).
        2. Отправляет GET-запрос к API для получения статуса задачи.
        3. Проверяет статус задачи (`job_status["status"]`).
        4. Если статус "succeeded", возвращает URL сгенерированного изображения.
        5. Если статус "failed", вызывает исключение `Exception`.
        6. Если задача еще не завершена, ждет `delay` секунд и повторяет попытку.
        7. Если превышено максимальное количество попыток, вызывает исключение `Exception`.

        A --> B --> C --> D --> E --> F
        |       |       |       |       |
        (loop     (send    (check   (return   (raise   (raise
        max_attempts) request)  status)  image_url) Exception) Exception)
        
        Примеры:
            # Пример использования функции _poll_job
            # В данном случае необходимо создать тестовую асинхронную сессию и job_id, чтобы пример был полным
            >>> import aiohttp
            >>> import asyncio
            >>> async def test():
            ...     async with aiohttp.ClientSession() as session:
            ...         try:
            ...             image_url = await Prodia._poll_job(session, "test_job_id", None, max_attempts=3, delay=1)
            ...             print(image_url)
            ...         except Exception as e:
            ...             print(f"Error: {e}")

        """
        ...
```

## Функции

В данном модуле функции отсутствуют.