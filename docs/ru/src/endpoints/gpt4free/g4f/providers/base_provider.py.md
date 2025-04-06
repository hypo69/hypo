# Модуль `base_provider.py`

## Обзор

Модуль `base_provider.py` содержит абстрактные классы и базовые классы для реализации провайдеров, обеспечивающих взаимодействие с различными языковыми моделями. Определяет общие интерфейсы и вспомогательные функции, используемые для создания запросов к моделям, обработки ответов и аутентификации.

## Подробнее

Этот модуль предоставляет основу для создания провайдеров, которые могут быть использованы для взаимодействия с различными API языковых моделей. Он определяет абстрактные методы, которые должны быть реализованы в подклассах, а также предоставляет реализации общих задач, таких как асинхронное выполнение задач и управление аутентификацией.

## Содержание

- [Константы](#константы)
- [Классы](#классы)
  - [AbstractProvider](#abstractprovider)
    - [create_completion](#create_completion)
    - [create_async](#create_async)
    - [get_create_function](#get_create_function)
    - [get_async_create_function](#get_async_create_function)
    - [get_parameters](#get_parameters)
    - [params](#params)
  - [AsyncProvider](#asyncprovider)
    - [create_completion (AsyncProvider)](#create_completion-asyncprovider)
    - [create_async (AsyncProvider)](#create_async-asyncprovider)
    - [get_create_function (AsyncProvider)](#get_create_function-asyncprovider)
    - [get_async_create_function (AsyncProvider)](#get_async_create_function-asyncprovider)
  - [AsyncGeneratorProvider](#asyncgeneratorprovider)
    - [create_completion (AsyncGeneratorProvider)](#create_completion-asyncgeneratorprovider)
    - [create_async_generator](#create_async_generator)
    - [get_create_function (AsyncGeneratorProvider)](#get_create_function-asyncgeneratorprovider)
    - [get_async_create_function (AsyncGeneratorProvider)](#get_async_create_function-asyncgeneratorprovider)
  - [ProviderModelMixin](#providermodelmixin)
    - [get_models](#get_models)
    - [get_model](#get_model)
  - [RaiseErrorMixin](#raiseerrormixin)
    - [raise_error](#raise_error)
  - [AuthFileMixin](#authfilemixin)
    - [get_cache_file](#get_cache_file)
  - [AsyncAuthedProvider](#asyncauthedprovider)
    - [on_auth_async](#on_auth_async)
    - [on_auth](#on_auth)
    - [get_create_function (AsyncAuthedProvider)](#get_create_function-asyncauthedprovider)
    - [get_async_create_function (AsyncAuthedProvider)](#get_async_create_function-asyncauthedprovider)
    - [write_cache_file](#write_cache_file)
    - [create_completion (AsyncAuthedProvider)](#create_completion-asyncauthedprovider)
    - [create_async_generator (AsyncAuthedProvider)](#create_async_generator-asyncauthedprovider)

## Константы

### `SAFE_PARAMETERS`
Список безопасных параметров, которые можно передавать в функции создания запросов.
```python
SAFE_PARAMETERS = [
    "model", "messages", "stream", "timeout",
    "proxy", "media", "response_format",
    "prompt", "negative_prompt", "tools", "conversation",
    "history_disabled",
    "temperature",  "top_k", "top_p",
    "frequency_penalty", "presence_penalty",
    "max_tokens", "stop",
    "api_key", "api_base", "seed", "width", "height",
    "max_retries", "web_search",
    "guidance_scale", "num_inference_steps", "randomize_seed",
    "safe", "enhance", "private", "aspect_ratio", "n",
]
```

### `BASIC_PARAMETERS`
Словарь базовых параметров с значениями по умолчанию.
```python
BASIC_PARAMETERS = {
    "provider": None,
    "model": "",
    "messages": [],
    "stream": False,
    "timeout": 0,
    "response_format": None,
    "max_tokens": 4096,
    "stop": ["stop1", "stop2"],
}
```

### `PARAMETER_EXAMPLES`
Словарь примеров значений параметров.
```python
PARAMETER_EXAMPLES = {
    "proxy": "http://user:password@127.0.0.1:3128",
    "temperature": 1,
    "top_k": 1,
    "top_p": 1,
    "frequency_penalty": 1,
    "presence_penalty": 1,
    "messages": [{"role": "system", "content": ""}, {"role": "user", "content": ""}],
    "media": [["data:image/jpeg;base64,...", "filename.jpg"]],
    "response_format": {"type": "json_object"},
    "conversation": {"conversation_id": "550e8400-e29b-11d4-a716-...", "message_id": "550e8400-e29b-11d4-a716-..."},
    "seed": 42,
    "tools": [],
}
```

## Классы

### `AbstractProvider`

**Описание**:
Абстрактный базовый класс для провайдеров. Определяет интерфейс для создания запросов к языковым моделям.

**Методы**:

#### `create_completion`

```python
    @classmethod
    @abstractmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        **kwargs
    ) -> CreateResult:
```

**Назначение**:
Абстрактный метод для создания завершения (completion) на основе предоставленных параметров.

**Параметры**:
- `model` (str): Имя модели, используемой для создания завершения.
- `messages` (Messages): Список сообщений для обработки моделью.
- `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `CreateResult`: Результат создания завершения.

**Вызывает исключения**:
- `NotImplementedError`: Если метод не реализован в подклассе.

**Как работает функция**:
1. Метод является абстрактным, и его необходимо переопределить в каждом подклассе `AbstractProvider`.
2. Он принимает параметры `model`, `messages` и `stream`, которые определяют, какую модель использовать, какие сообщения обрабатывать и использовать ли потоковую передачу.
3. Дополнительные параметры передаются через `kwargs`.
4. Метод должен возвращать объект `CreateResult`, который содержит результат создания завершения.

#### `create_async`

```python
    @classmethod
    async def create_async(
        cls,
        model: str,
        messages: Messages,
        *,
        timeout: int = None,
        loop: AbstractEventLoop = None,
        executor: ThreadPoolExecutor = None,
        **kwargs
    ) -> str:
```

**Назначение**:
Асинхронно создает результат на основе указанной модели и сообщений.

**Параметры**:
- `model` (str): Модель, используемая для создания.
- `messages` (Messages): Сообщения для обработки.
- `timeout` (int, optional): Максимальное время ожидания выполнения запроса. По умолчанию `None`.
- `loop` (AbstractEventLoop, optional): Событийный цикл для выполнения асинхронных задач. По умолчанию `None`.
- `executor` (ThreadPoolExecutor, optional): Исполнитель для запуска синхронных задач в отдельном потоке. По умолчанию `None`.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `str`: Созданный результат в виде строки.

**Как работает функция**:
1. Получает текущий событийный цикл, если он не был передан в качестве аргумента.
2. Определяет внутреннюю функцию `create_func`, которая вызывает метод `create_completion` для создания завершения и объединяет полученные чанки.
3. Запускает `create_func` в отдельном потоке с использованием `loop.run_in_executor`.
4. Ожидает завершения выполнения задачи в течение указанного времени `timeout`.

#### `get_create_function`

```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
```

**Назначение**:
Возвращает функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Функция `create_completion`.

#### `get_async_create_function`

```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async
```

**Назначение**:
Возвращает асинхронную функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Асинхронная функция `create_async`.

#### `get_parameters`

```python
    @classmethod
    def get_parameters(cls, as_json: bool = False) -> dict[str, Parameter]:
```

**Назначение**:
Возвращает словарь параметров, поддерживаемых провайдером.

**Параметры**:
- `as_json` (bool, optional): Если `True`, возвращает параметры в формате JSON. По умолчанию `False`.

**Возвращает**:
- `dict[str, Parameter]`: Словарь параметров, где ключ - имя параметра, а значение - объект `Parameter`.

**Как работает функция**:
1. Получает параметры из сигнатуры метода `create_async_generator` (если класс является подклассом `AsyncGeneratorProvider`), `create_async` (если класс является подклассом `AsyncProvider`) или `create_completion`.
2. Фильтрует параметры, оставляя только те, которые указаны в `SAFE_PARAMETERS` и не являются `stream` (если `supports_stream` равно `False`).
3. Если `as_json` равно `True`, преобразует параметры в JSON-совместимый формат, используя примеры значений из `PARAMETER_EXAMPLES` и значения по умолчанию.
4. Возвращает словарь параметров.

**Внутренние функции**:
- `get_type_as_var`: Определяет тип переменной на основе аннотации и возвращает соответствующее значение по умолчанию.

#### `params`

```python
    @classmethod
    @property
    def params(cls) -> str:
```

**Назначение**:
Возвращает строку, содержащую информацию о параметрах, поддерживаемых провайдером.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Строка с информацией о поддерживаемых параметрах.

**Как работает функция**:
1. Получает словарь параметров, используя метод `get_parameters`.
2. Форматирует каждый параметр в строку, включающую имя, тип и значение по умолчанию.
3. Объединяет все строки параметров в одну строку и возвращает ее.

**Внутренние функции**:
- `get_type_name`: Возвращает имя типа на основе аннотации.

### `AsyncProvider`

**Описание**:
Предоставляет асинхронную функциональность для создания завершений.

**Наследует**:
- `AbstractProvider`

**Методы**:

#### `create_completion (AsyncProvider)`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool = False,
        **kwargs
    ) -> CreateResult:
```

**Назначение**:
Создает результат завершения синхронно.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `False`.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `CreateResult`: Результат создания завершения.

**Как работает функция**:
1. Проверяет, запущен ли событийный цикл.
2. Запускает асинхронную функцию `create_async` и возвращает результат.

#### `create_async (AsyncProvider)`

```python
    @staticmethod
    @abstractmethod
    async def create_async(
        model: str,
        messages: Messages,
        **kwargs
    ) -> str:
```

**Назначение**:
Абстрактный статический метод для создания асинхронных результатов.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Вызывает исключения**:
- `NotImplementedError`: Если метод не переопределен в производных классах.

**Возвращает**:
- `str`: Созданный результат в виде строки.

**Как работает функция**:
1. Метод является абстрактным, и его необходимо переопределить в каждом подклассе `AsyncProvider`.
2. Он принимает параметры `model` и `messages`, которые определяют, какую модель использовать и какие сообщения обрабатывать.
3. Дополнительные параметры передаются через `kwargs`.
4. Метод должен возвращать строку, содержащую результат создания.

#### `get_create_function (AsyncProvider)`

```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
```

**Назначение**:
Возвращает функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Функция `create_completion`.

#### `get_async_create_function (AsyncProvider)`

```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async
```

**Назначение**:
Возвращает асинхронную функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Асинхронная функция `create_async`.

### `AsyncGeneratorProvider`

**Описание**:
Предоставляет функциональность асинхронного генератора для потоковой передачи результатов.

**Наследует**:
- `AbstractProvider`

**Атрибуты**:
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу. Всегда `True`.

**Методы**:

#### `create_completion (AsyncGeneratorProvider)`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> CreateResult:
```

**Назначение**:
Создает результат потокового завершения синхронно.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `True`.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `CreateResult`: Результат создания потокового завершения.

**Как работает функция**:
1. Преобразует асинхронный генератор `create_async_generator` в синхронный генератор с помощью функции `to_sync_generator`.
2. Возвращает синхронный генератор.

#### `create_async_generator`

```python
    @staticmethod
    @abstractmethod
    async def create_async_generator(
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> AsyncResult:
```

**Назначение**:
Абстрактный статический метод для создания асинхронного генератора.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `True`.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Вызывает исключения**:
- `NotImplementedError`: Если метод не переопределен в производных классах.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий результаты.

**Как работает функция**:
1. Метод является абстрактным, и его необходимо переопределить в каждом подклассе `AsyncGeneratorProvider`.
2. Он принимает параметры `model`, `messages` и `stream`, которые определяют, какую модель использовать, какие сообщения обрабатывать и использовать ли потоковую передачу.
3. Дополнительные параметры передаются через `kwargs`.
4. Метод должен возвращать асинхронный генератор, который выдает результаты создания.

#### `get_create_function (AsyncGeneratorProvider)`

```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
```

**Назначение**:
Возвращает функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Функция `create_completion`.

#### `get_async_create_function (AsyncGeneratorProvider)`

```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async_generator
```

**Назначение**:
Возвращает асинхронную функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Асинхронная функция `create_async_generator`.

### `ProviderModelMixin`

**Описание**:
Миксин для классов провайдеров, добавляющий поддержку выбора модели.

**Атрибуты**:
- `default_model` (str): Модель по умолчанию.
- `models` (list[str]): Список поддерживаемых моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.
- `image_models` (list): Список моделей для работы с изображениями.
- `vision_models` (list): Список моделей для компьютерного зрения.
- `last_model` (str): Последняя использованная модель.

**Методы**:

#### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs) -> list[str]:
```

**Назначение**:
Возвращает список поддерживаемых моделей.

**Параметры**:
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `list[str]`: Список поддерживаемых моделей.

**Как работает функция**:
1. Если список `models` пуст, и `default_model` не `None`, возвращает список, содержащий только `default_model`.
2. В противном случае возвращает список `models`.

#### `get_model`

```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
```

**Назначение**:
Возвращает имя модели на основе предоставленного имени модели и псевдонимов.

**Параметры**:
- `model` (str): Имя модели.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `str`: Имя модели.

**Вызывает исключения**:
- `ModelNotSupportedError`: Если модель не поддерживается.

**Как работает функция**:
1. Если `model` не указана, и `default_model` не `None`, возвращает `default_model`.
2. Если `model` есть в `model_aliases`, возвращает соответствующий псевдоним.
3. Если `model` нет в списке `models`, и список `models` не пуст, вызывает исключение `ModelNotSupportedError`.
4. Устанавливает `last_model` в значение `model` и возвращает `model`.

### `RaiseErrorMixin`

**Описание**:
Миксин для классов провайдеров, добавляющий функциональность обработки ошибок.

**Методы**:

#### `raise_error`

```python
    @staticmethod
    def raise_error(data: dict, status: int = None):
```

**Назначение**:
Вызывает исключение на основе данных об ошибке.

**Параметры**:
- `data` (dict): Данные об ошибке.
- `status` (int, optional): HTTP-статус код. По умолчанию `None`.

**Вызывает исключения**:
- `ResponseError`: Если в данных есть ключ `error_message` или `error`.
- `MissingAuthError`: Если статус код 401 и в данных есть `error`.
- `PaymentRequiredError`: Если статус код 402 и в данных есть `error`.

**Как работает функция**:
1. Проверяет наличие ключей `error_message` или `error` в данных.
2. В зависимости от типа данных в `error`, вызывает соответствующее исключение.

### `AuthFileMixin`

**Описание**:
Миксин для классов провайдеров, добавляющий функциональность кэширования аутентификации в файл.

**Методы**:

#### `get_cache_file`

```python
    @classmethod
    def get_cache_file(cls) -> Path:
```

**Назначение**:
Возвращает путь к файлу кэша.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Path`: Путь к файлу кэша.

**Как работает функция**:
1. Формирует путь к файлу кэша в директории cookies, используя имя класса или имя родительского класса (если атрибут `parent` присутствует).

### `AsyncAuthedProvider`

**Описание**:
Предоставляет асинхронную функциональность для провайдеров, требующих аутентификацию.

**Наследует**:
- `AsyncGeneratorProvider`
- `AuthFileMixin`

**Методы**:

#### `on_auth_async`

```python
    @classmethod
    async def on_auth_async(cls, **kwargs) -> AuthResult:
```

**Назначение**:
Асинхронно выполняет аутентификацию.

**Параметры**:
- `kwargs` (dict): Дополнительные именованные аргументы.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует ключ `api_key` в `kwargs`.

**Возвращает**:
- `AuthResult`: Результат аутентификации.

**Как работает функция**:
1. Проверяет наличие ключа `api_key` в `kwargs`. Если его нет, вызывает исключение `MissingAuthError`.
2. Возвращает объект `AuthResult`.

#### `on_auth`

```python
    @classmethod
    def on_auth(cls, **kwargs) -> AuthResult:
```

**Назначение**:
Синхронно выполняет аутентификацию.

**Параметры**:
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `AuthResult`: Результат аутентификации.

**Как работает функция**:
1. Вызывает асинхронный метод `on_auth_async`.
2. Если результат является асинхронным итератором, преобразует его в синхронный генератор.
3. Запускает асинхронную функцию и возвращает результат.

#### `get_create_function (AsyncAuthedProvider)`

```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
```

**Назначение**:
Возвращает функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Функция `create_completion`.

#### `get_async_create_function (AsyncAuthedProvider)`

```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async_generator
```

**Назначение**:
Возвращает асинхронную функцию для создания завершений.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Асинхронная функция `create_async_generator`.

#### `write_cache_file`

```python
    @classmethod
    def write_cache_file(cls, cache_file: Path, auth_result: AuthResult = None):
```

**Назначение**:
Записывает результат аутентификации в файл кэша.

**Параметры**:
- `cache_file` (Path): Путь к файлу кэша.
- `auth_result` (AuthResult, optional): Результат аутентификации. По умолчанию `None`.

**Как работает функция**:
1. Если `auth_result` не `None`, создает директорию для файла кэша (если она не существует) и записывает результат аутентификации в файл в формате JSON.
2. Если `auth_result` равно `None`, и файл кэша существует, удаляет файл.

#### `create_completion (AsyncAuthedProvider)`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        **kwargs
) -> CreateResult:
```

**Назначение**:
Создает результат завершения с использованием аутентификации.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `CreateResult`: Результат создания завершения.

**Как работает функция**:
1. Пытается загрузить результат аутентификации из файла кэша.
2. Если файл кэша существует, использует результат аутентификации для создания завершения с помощью метода `create_authed`.
3. Если файл кэша не существует или содержит неверные данные, выполняет аутентификацию с помощью метода `on_auth` и сохраняет результат в файл кэша.
4. Возвращает результат создания завершения.

#### `create_async_generator (AsyncAuthedProvider)`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        **kwargs
    ) -> AsyncResult:
```

**Назначение**:
Асинхронно создает результат завершения с использованием аутентификации.

**Параметры**:
- `model` (str): Модель для использования при создании.
- `messages` (Messages): Сообщения для обработки.
- `kwargs` (dict): Дополнительные именованные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий результаты.

**Как работает функция**:
1. Пытается загрузить результат аутентификации из файла кэша.
2. Если файл кэша существует, использует результат аутентификации для создания завершения с помощью метода `create_authed`.
3. Если файл кэша не существует или содержит неверные данные, выполняет аутентификацию с помощью метода `on_auth_async` и сохраняет результат в файл кэша.
4. Возвращает асинхронный генератор, выдающий результаты.