# Модуль для работы с PollinationsAI
======================================

Модуль предоставляет асинхронный генератор для взаимодействия с PollinationsAI API для генерации текста и изображений.

## Обзор

Модуль содержит класс `PollinationsAI`, который является асинхронным провайдером и предоставляет методы для генерации текста и изображений с использованием API PollinationsAI. Он поддерживает различные модели, включая текстовые и графические модели, а также модели для работы с аудио.

## Подробнее

Этот модуль предназначен для интеграции с API PollinationsAI, обеспечивая удобный интерфейс для генерации контента на основе текста и изображений. Он включает в себя механизмы для управления моделями, обработки запросов и возврата результатов в асинхронном режиме.

## Классы

### `PollinationsAI`

**Описание**: Класс `PollinationsAI` является основным классом, предоставляющим функциональность для взаимодействия с API PollinationsAI. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для управления моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Pollinations AI").
- `url` (str): URL сайта PollinationsAI ("https://pollinations.ai").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `text_api_endpoint` (str): URL для API генерации текста ("https://text.pollinations.ai").
- `openai_endpoint` (str): URL для OpenAI API ("https://text.pollinations.ai/openai").
- `image_api_endpoint` (str): URL для API генерации изображений ("https://image.pollinations.ai/").
- `default_model` (str): Модель по умолчанию ("openai").
- `default_image_model` (str): Модель для генерации изображений по умолчанию ("flux").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (совпадает с `default_model`).
- `text_models` (list): Список поддерживаемых текстовых моделей.
- `image_models` (list): Список поддерживаемых моделей для генерации изображений.
- `extra_image_models` (list): Список дополнительных моделей для генерации изображений.
- `vision_models` (list): Список моделей для обработки изображений.
- `extra_text_models` (list): Список дополнительных текстовых моделей.
- `_models_loaded` (bool): Флаг, указывающий, были ли загружены модели (False).
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_models()`: Получает список поддерживаемых моделей.
- `create_async_generator()`: Создает асинхронный генератор для генерации текста или изображений.
- `_generate_image()`: Генерирует изображения.
- `_generate_text()`: Генерирует текст.

### `PollinationsAI.get_models`

```python
    @classmethod
    def get_models(cls, **kwargs) -> list[str]:
        """
        Получает список поддерживаемых моделей из API PollinationsAI.
        В случае ошибки возвращает модели по умолчанию.

        Args:
            **kwargs: Дополнительные аргументы.

        Returns:
            list[str]: Список поддерживаемых моделей.

        Raises:
            Exception: Если не удается получить список моделей из API.
        """
        ...
```

**Назначение**: Обновляет списки моделей (`cls.image_models` и `cls.text_models`) путем запроса к API PollinationsAI. В случае неудачи использует модели по умолчанию.

**Как работает функция**:

1. **Проверка загрузки моделей**: Проверяет, были ли уже загружены модели (`cls._models_loaded`). Если модели еще не были загружены, выполняется дальнейший процесс.

2. **Запрос моделей изображений**: Отправляет GET-запрос к API (`https://image.pollinations.ai/models`) для получения списка доступных моделей изображений.

3. **Обработка ответа моделей изображений**: Если запрос успешен, извлекает список моделей из JSON-ответа. В случае ошибки использует пустой список.

4. **Обновление списка моделей изображений**: Объединяет модели изображений из разных источников (уже существующие, дополнительные и полученные из API) и удаляет дубликаты.

5. **Запрос текстовых моделей**: Отправляет GET-запрос к API (`https://text.pollinations.ai/models`) для получения списка доступных текстовых моделей.

6. **Обработка ответа текстовых моделей**: Извлекает имена текстовых моделей из JSON-ответа, фильтруя модели типа "chat".

7. **Извлечение аудио моделей**: Извлекает имена аудио моделей и их голоса из JSON-ответа, фильтруя модели, поддерживающие аудио.

8. **Обновление списка текстовых моделей**: Объединяет текстовые модели из разных источников (уже существующие, дополнительные, полученные из API и модели для обработки изображений) и удаляет дубликаты.

9. **Установка флага загрузки**: Устанавливает флаг `cls._models_loaded` в `True`, чтобы указать, что модели были загружены.

10. **Обработка исключений**: Если в процессе выполнения возникают исключения, сохраняет модели по умолчанию (если они еще не установлены) и регистрирует ошибку.

11. **Возврат списка моделей**: Возвращает объединенный список текстовых и графических моделей.

**Примеры**:

```python
# Пример вызова функции
models = PollinationsAI.get_models()
print(models)
```

### `PollinationsAI.create_async_generator`

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
            model (str): Название модели.
            messages (Messages): Список сообщений для генерации.
            stream (bool, optional): Включить потоковую передачу. По умолчанию True.
            proxy (str, optional): Адрес прокси-сервера. По умолчанию None.
            cache (bool, optional): Использовать кэш. По умолчанию False.
            prompt (str, optional): Текст запроса для генерации изображения. По умолчанию None.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию None.
            height (int, optional): Высота изображения. По умолчанию None.
            seed (Optional[int], optional): Зерно для генерации. По умолчанию None.
            nologo (bool, optional): Убрать логотип. По умолчанию True.
            private (bool, optional): Сделать приватным. По умолчанию False.
            enhance (bool, optional): Улучшить качество. По умолчанию False.
            safe (bool, optional): Включить безопасный режим. По умолчанию False.
            n (int, optional): Количество изображений для генерации. По умолчанию 1.
            media (MediaListType, optional): Список медиафайлов. По умолчанию None.
            temperature (float, optional): Температура для генерации текста. По умолчанию None.
            presence_penalty (float, optional): Штраф за присутствие. По умолчанию None.
            top_p (float, optional): Top-p для генерации текста. По умолчанию None.
            frequency_penalty (float, optional): Штраф за частоту. По умолчанию None.
            response_format (Optional[dict], optional): Формат ответа. По умолчанию None.
            extra_parameters (list[str], optional): Список дополнительных параметров.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Часть сгенерированного текста или изображения.

        Raises:
            ModelNotFoundError: Если модель не найдена.
            Exception: Если происходит ошибка во время генерации.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для генерации текста или изображений в зависимости от указанной модели.

**Как работает функция**:

1. **Загрузка списка моделей**: Вызывает метод `cls.get_models()` для загрузки списка доступных моделей.

2. **Определение модели**: Если модель не указана, определяет, есть ли аудио в дополнительных аргументах или медиафайлах. Если аудио есть, выбирает первую аудиомодель из `cls.audio_models`.

3. **Получение модели**: Пытается получить модель с помощью `cls.get_model(model)`. Если модель не найдена и не является моделью изображения, вызывает исключение `ModelNotFoundError`.

4. **Генерация изображения**: Если модель является моделью изображения, вызывает метод `cls._generate_image()` для генерации изображения.

5. **Генерация текста**: Если модель не является моделью изображения, вызывает метод `cls._generate_text()` для генерации текста.

6. **Возврат результата**: Возвращает асинхронный генератор, который выдает части сгенерированного текста или изображения.

**Примеры**:

```python
# Пример вызова для генерации изображения
async for chunk in PollinationsAI.create_async_generator(model="flux", prompt="cat"):
    print(chunk)

# Пример вызова для генерации текста
async for chunk in PollinationsAI.create_async_generator(model="openai", messages=[{"role": "user", "content": "Hello!"}]):
    print(chunk)
```

### `PollinationsAI._generate_image`

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
        Генерирует изображения с использованием API PollinationsAI.

        Args:
            model (str): Название модели.
            prompt (str): Текст запроса.
            proxy (str): Адрес прокси-сервера.
            aspect_ratio (str): Соотношение сторон изображения.
            width (int): Ширина изображения.
            height (int): Высота изображения.
            seed (Optional[int]): Зерно для генерации.
            nologo (bool): Убрать логотип.
            private (bool): Сделать приватным.
            enhance (bool): Улучшить качество.
            safe (bool): Включить безопасный режим.
            n (int): Количество изображений для генерации.

        Yields:
            ImageResponse: Объект, содержащий URL сгенерированного изображения.

        Raises:
            Exception: Если происходит ошибка при генерации изображения.
        """
        ...
```

**Назначение**: Генерирует изображения, используя API PollinationsAI.

**Как работает функция**:

1. **Подготовка параметров**: Создает словарь `params` с параметрами запроса, включая размеры изображения, модель, флаги `nologo`, `private`, `enhance` и `safe`. Использует функцию `use_aspect_ratio` для корректировки размеров изображения в соответствии с заданным соотношением сторон.

2. **Формирование URL**: Формирует URL для запроса к API, добавляя параметры запроса и текст запроса (`prompt`).

3. **Определение функции для получения URL изображения**: Определяет внутреннюю функцию `get_image_url`, которая генерирует URL для получения изображения с учетом зерна (`seed`) и кэширования.

4. **Создание сессии**: Создает асинхронную сессию с использованием `ClientSession` и `get_connector` для поддержки прокси.

5. **Определение асинхронной функции для получения изображения**: Определяет внутреннюю асинхронную функцию `get_image`, которая отправляет GET-запрос к API для получения изображения и обрабатывает возможные ошибки.

6. **Сбор результатов**: Использует `asyncio.gather` для параллельного выполнения нескольких запросов на генерацию изображений.

7. **Возврат результата**: Возвращает объект `ImageResponse`, содержащий список URL сгенерированных изображений и текст запроса.

**Примеры**:

```python
# Пример вызова функции
async for chunk in PollinationsAI._generate_image(
    model="flux",
    prompt="cat",
    proxy=None,
    aspect_ratio="1:1",
    width=512,
    height=512,
    seed=None,
    cache=False,
    nologo=True,
    private=False,
    enhance=False,
    safe=True,
    n=1
):
    print(chunk)
```

### `PollinationsAI._generate_text`

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
        """
        Генерирует текст с использованием API PollinationsAI.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений для генерации.
            media (MediaListType): Список медиафайлов.
            proxy (str): Адрес прокси-сервера.
            temperature (float): Температура для генерации текста.
            presence_penalty (float): Штраф за присутствие.
            top_p (float): Top-p для генерации текста.
            frequency_penalty (float): Штраф за частоту.
            response_format (Optional[dict]): Формат ответа.
            seed (Optional[int]): Зерно для генерации.
            cache (bool): Использовать кэш.
            stream (bool): Включить потоковую передачу.
            extra_parameters (list[str]): Список дополнительных параметров.
            **kwargs: Дополнительные аргументы.

        Yields:
            str: Часть сгенерированного текста.
            Usage: Информация об использовании ресурсов.
            FinishReason: Причина завершения генерации.

        Raises:
            Exception: Если происходит ошибка при генерации текста.
        """
        ...
```

**Назначение**: Генерирует текст, используя API PollinationsAI.

**Как работает функция**:

1. **Инициализация**:
   - Устанавливает случайное зерно (`seed`), если оно не задано и кэширование отключено.
   - Определяет, включен ли режим JSON (`json_mode`) на основе формата ответа (`response_format`).

2. **Создание сессии**:
   - Создает асинхронную сессию с использованием `ClientSession` и `get_connector` для поддержки прокси.

3. **Определение URL**:
   - Определяет URL для запроса к API в зависимости от того, является ли модель аудиомоделью или нет. Если модель является аудиомоделью, используется `cls.text_api_endpoint`, иначе используется `cls.openai_endpoint`.
   - Если модель является аудиомоделью, отключается потоковая передача (`stream = False`).

4. **Подготовка данных**:
   - Формирует словарь `data` с параметрами запроса, включая сообщения, модель, температуру, штрафы, режим JSON, флаг потоковой передачи, зерно и кэширование.
   - Использует функцию `filter_none` для удаления параметров со значением `None`.
   - Преобразует сообщения с использованием `render_messages` и медиафайлы.

5. **Отправка запроса**:
   - Отправляет POST-запрос к API с данными в формате JSON.

6. **Обработка ответа**:
   - Обрабатывает ответ от API в зависимости от типа контента:
     - Если тип контента начинается с `text/plain`, возвращает текст ответа.
     - Если тип контента начинается с `text/event-stream`, обрабатывает потоковую передачу данных и возвращает части сгенерированного текста, информацию об использовании ресурсов и причину завершения генерации.
     - Если тип контента не соответствует ни одному из вышеперечисленных, пытается преобразовать ответ в формат JSON и извлекает сгенерированный текст, информацию об использовании ресурсов и причину завершения генерации.

7. **Возврат результата**:
   - Возвращает части сгенерированного текста, информацию об использовании ресурсов и причину завершения генерации.

**Примеры**:

```python
# Пример вызова функции
async for chunk in PollinationsAI._generate_text(
    model="openai",
    messages=[{"role": "user", "content": "Hello!"}],
    media=None,
    proxy=None,
    temperature=0.7,
    presence_penalty=0.0,
    top_p=1.0,
    frequency_penalty=0.0,
    response_format=None,
    seed=None,
    cache=False,
    stream=True,
    extra_parameters=[]
):
    print(chunk)