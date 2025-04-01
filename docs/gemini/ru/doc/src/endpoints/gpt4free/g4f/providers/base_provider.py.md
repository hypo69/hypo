# Модуль `base_provider.py`

## Обзор

Модуль определяет абстрактные классы для реализации провайдеров, предоставляющих функциональность для создания завершений текста (completions) с использованием различных моделей. Он содержит базовые классы для синхронных, асинхронных и асинхронных генераторов, а также вспомогательные миксины для обработки ошибок, аутентификации и работы с моделями.

## Подробнее

Этот модуль является основой для создания провайдеров в проекте `hypotez`. Он определяет интерфейсы и общую логику, необходимую для взаимодействия с различными API, предоставляющими функциональность генерации текста. Модуль включает в себя классы для работы с асинхронными операциями и потоковой передачей данных, а также инструменты для управления аутентификацией и обработки ошибок.

## Содержание

1.  [Константы](#константы)
2.  [Классы](#классы)
    *   [AbstractProvider](#abstractprovider)
        *   [Методы класса](#методы-класса-abstractprovider)
    *   [AsyncProvider](#asyncprovider)
        *   [Методы класса](#методы-класса-asyncprovider)
    *   [AsyncGeneratorProvider](#asyncgeneratorprovider)
        *   [Методы класса](#методы-класса-asyncgeneratorprovider)
    *   [ProviderModelMixin](#providermodelmixin)
        *   [Методы класса](#методы-класса-providermodelmixin)
    *   [RaiseErrorMixin](#raiseerrormixin)
        *   [Методы класса](#методы-класса-raiseerrormixin)
    *   [AuthFileMixin](#authfilemixin)
        *   [Методы класса](#методы-класса-authfilemixin)
    *   [AsyncAuthedProvider](#asyncauthedprovider)
        *   [Методы класса](#методы-класса-asyncauthedprovider)

## Константы

### `SAFE_PARAMETERS`

Список безопасных параметров, которые можно передавать в запросы к провайдерам.

### `BASIC_PARAMETERS`

Словарь, содержащий базовые параметры, используемые при создании запросов к провайдерам.

### `PARAMETER_EXAMPLES`

Словарь, содержащий примеры значений параметров, используемых при создании запросов к провайдерам.

## Классы

### `AbstractProvider`

Абстрактный базовый класс для провайдеров.

**Описание**:
Определяет интерфейс для создания завершений текста (completions). Предоставляет абстрактный метод `create_completion`, который должен быть реализован в подклассах. Также предоставляет методы для асинхронного создания завершений и получения параметров.

#### Методы класса `AbstractProvider`

*   `create_completion`

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
        """
        Создает завершение текста (completion) с заданными параметрами.

        Args:
            model (str): Модель для использования.
            messages (Messages): Сообщения для обработки.
            stream (bool): Использовать ли потоковую передачу.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            CreateResult: Результат процесса создания.
        """
        ...
    ```

    **Назначение**:
    Абстрактный метод, который должен быть реализован в подклассах для создания завершения текста на основе предоставленных параметров.

    **Параметры**:
    - `model` (str): Имя модели, которую необходимо использовать для генерации ответа.
    - `messages` (Messages): Список сообщений, используемых для контекста генерации. Обычно это список словарей, где каждый словарь имеет ключи "role" (роль отправителя, например, "user" или "system") и "content" (содержимое сообщения).
    - `stream` (bool): Флаг, указывающий, использовать ли потоковый режим для генерации ответа. Если `True`, ответ будет генерироваться частями, а не целиком.
    - `**kwargs`: Дополнительные именованные аргументы, которые могут включать специфичные для конкретного провайдера параметры.

    **Возвращает**:
    - `CreateResult`: Результат создания завершения текста. Тип `CreateResult` является псевдонимом для `Generator[str, None, None] | str`, что означает, что функция может возвращать либо генератор строк (в случае потокового режима), либо строку с полным текстом ответа.

    **Вызывает исключения**:
    - `NotImplementedError`: Если метод не переопределен в производном классе.

    **Как работает функция**:

    1.  Метод является абстрактным, поэтому его реализация должна быть предоставлена в подклассах, которые наследуются от `AbstractProvider`.
    2.  Внутри подкласса, реализующего этот метод, должен быть код, который использует параметры `model`, `messages` и `kwargs` для взаимодействия с API провайдера и генерации ответа.
    3.  Если `stream` установлен в `True`, реализация должна возвращать генератор, который выдает части ответа по мере их генерации. В противном случае должна быть возвращена строка, содержащая полный ответ.

*   `create_async`

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
        """
        Асинхронно создает результат на основе заданной модели и сообщений.

        Args:
            cls (type): Класс, на котором вызывается этот метод.
            model (str): Модель для использования при создании.
            messages (Messages): Сообщения для обработки.
            loop (AbstractEventLoop, optional): Цикл событий для использования. По умолчанию None.
            executor (ThreadPoolExecutor, optional): Исполнитель для запуска асинхронных задач. По умолчанию None.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            str: Созданный результат в виде строки.
        """
        ...
    ```

    **Назначение**:
    Асинхронно создает результат на основе заданной модели и сообщений.

    **Параметры**:
    - `model` (str): Модель для использования при создании.
    - `messages` (Messages): Сообщения для обработки.
    - `timeout` (int, optional): Максимальное время ожидания выполнения операции. По умолчанию `None`.
    - `loop` (AbstractEventLoop, optional): Объект event loop для выполнения асинхронных операций. Если не указан, используется текущий event loop.
    - `executor` (ThreadPoolExecutor, optional): Executor для выполнения блокирующих операций в отдельном потоке. Если не указан, используется executor по умолчанию.
    - `**kwargs`: Дополнительные именованные аргументы, которые передаются в функцию `create_completion`.

    **Возвращает**:
    - `str`: Результат выполнения асинхронной операции в виде строки.

    **Как работает функция**:

    1.  Функция получает текущий event loop, если он не был передан в качестве аргумента.
    2.  Определяет внутреннюю функцию `create_func`, которая вызывает `cls.create_completion` с переданными аргументами и объединяет полученные чанки в одну строку с помощью `concat_chunks`.
    3.  Запускает `create_func` в executor с помощью `loop.run_in_executor`, что позволяет выполнять блокирующие операции в отдельном потоке, не блокируя основной event loop.
    4.  Ожидает завершения выполнения задачи с помощью `asyncio.wait_for` с заданным `timeout`. Если время ожидания истекает, выбрасывается исключение `asyncio.TimeoutError`.
    5.  Возвращает результат выполнения задачи в виде строки.

*   `get_create_function`

    ```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
    ```

    **Назначение**:
    Возвращает функцию для создания завершений.

    **Возвращает**:
    - `callable`: Функция `create_completion`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_completion` класса.

*   `get_async_create_function`

    ```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async
    ```

    **Назначение**:
    Возвращает асинхронную функцию для создания завершений.

    **Возвращает**:
    - `callable`: Асинхронная функция `create_async`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_async` класса.

*   `get_parameters`

    ```python
    @classmethod
    def get_parameters(cls, as_json: bool = False) -> dict[str, Parameter]:
        params = {name: parameter for name, parameter in signature(
            cls.create_async_generator if issubclass(cls, AsyncGeneratorProvider) else
            cls.create_async if issubclass(cls, AsyncProvider) else
            cls.create_completion
        ).parameters.items() if name in SAFE_PARAMETERS
            and (name != "stream" or cls.supports_stream)}
        if as_json:
            def get_type_as_var(annotation: type, key: str, default):
                if key in PARAMETER_EXAMPLES:
                    if key == "messages" and not cls.supports_system_message:
                        return [PARAMETER_EXAMPLES[key][-1]]
                    return PARAMETER_EXAMPLES[key]
                if isinstance(annotation, type):
                    if issubclass(annotation, int):
                        return 0
                    elif issubclass(annotation, float):
                        return 0.0
                    elif issubclass(annotation, bool):
                        return False
                    elif issubclass(annotation, str):
                        return ""
                    elif issubclass(annotation, dict):
                        return {}
                    elif issubclass(annotation, list):
                        return []
                    elif issubclass(annotation, BaseConversation):
                        return {}
                    elif issubclass(annotation, NoneType):
                        return {}
                elif annotation is None:
                    return None
                elif annotation == "str" or annotation == "list[str]":
                    return default
                elif isinstance(annotation, _GenericAlias):
                    if annotation.__origin__ is Optional:
                        return get_type_as_var(annotation.__args__[0])
                else:
                    return str(annotation)
            return { name: (
                param.default
                if isinstance(param, Parameter) and param.default is not Parameter.empty and param.default is not None
                else get_type_as_var(param.annotation, name, param.default) if isinstance(param, Parameter) else param
            ) for name, param in {
                **BASIC_PARAMETERS,
                **params,
                **{"provider": cls.__name__, "model": getattr(cls, "default_model", ""), "stream": cls.supports_stream},
            }.items()}
        return params
    ```

    **Назначение**:
    Возвращает параметры, поддерживаемые провайдером.

    **Параметры**:
    - `as_json` (bool, optional): Если `True`, возвращает параметры в формате JSON. По умолчанию `False`.

    **Возвращает**:
    - `dict[str, Parameter]`: Словарь, содержащий параметры и их значения.

    **Как работает функция**:

    1.  Определяет, какую функцию использовать для получения параметров (`create_async_generator`, `create_async` или `create_completion`) в зависимости от типа класса (AsyncGeneratorProvider, AsyncProvider или AbstractProvider).
    2.  Получает параметры из сигнатуры выбранной функции и фильтрует их, оставляя только те, которые находятся в списке `SAFE_PARAMETERS` и удовлетворяют условию `name != "stream" or cls.supports_stream`.
    3.  Если `as_json` равен `True`, преобразует значения параметров в JSON-совместимый формат, используя значения из `PARAMETER_EXAMPLES` или значения по умолчанию для каждого типа данных.
        - Внутренняя функция `get_type_as_var` рекурсивно определяет тип переменной и возвращает соответствующее значение по умолчанию.
    4.  Возвращает словарь с параметрами.

*   `params`

    ```python
    @classmethod
    @property
    def params(cls) -> str:
        """
        Возвращает параметры, поддерживаемые провайдером.

        Args:
            cls (type): Класс, на котором вызывается это свойство.

        Returns:
            str: Строка, перечисляющая поддерживаемые параметры.
        """
        ...
    ```

    **Назначение**:
    Возвращает параметры, поддерживаемые провайдером, в виде строки.

    **Возвращает**:
    - `str`: Строка, перечисляющая поддерживаемые параметры.

    **Как работает функция**:

    1.  Получает параметры с помощью метода `cls.get_parameters()`.
    2.  Форматирует каждый параметр в строку вида `\n {name}: {type} = {default_value}`.
    3.  Объединяет все параметры в одну строку и возвращает ее.

### `AsyncProvider`

Предоставляет асинхронную функциональность для создания завершений.

**Описание**:
Этот класс расширяет `AbstractProvider` и предоставляет реализацию для асинхронного создания завершений текста. Он использует `asyncio` для выполнения асинхронных операций и предоставляет метод `create_async` для запуска процесса создания завершения.

#### Методы класса `AsyncProvider`

*   `create_completion`

    ```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool = False,
        **kwargs
    ) -> CreateResult:
        """
        Создает результат завершения синхронно.

        Args:
            cls (type): Класс, на котором вызывается этот метод.
            model (str): Модель для использования при создании.
            messages (Messages): Сообщения для обработки.
            stream (bool): Указывает, следует ли передавать результаты потоком. По умолчанию False.
            loop (AbstractEventLoop, optional): Цикл событий для использования. По умолчанию None.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            CreateResult: Результат создания завершения.
        """
        ...
    ```

    **Назначение**:
    Создает результат завершения текста синхронно, используя асинхронную функцию `create_async`.

    **Параметры**:
    - `model` (str): Модель для использования при создании.
    - `messages` (Messages): Сообщения для обработки.
    - `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `False`.
    - `**kwargs`: Дополнительные именованные аргументы, передаваемые в `create_async`.

    **Возвращает**:
    - `CreateResult`: Результат создания завершения текста.

    **Как работает функция**:

    1.  Проверяет, запущен ли event loop, с помощью `get_running_loop(check_nested=False)`. Если event loop не запущен, будет выброшено исключение.
    2.  Вызывает асинхронную функцию `cls.create_async` с переданными аргументами и получает результат.
    3.  Использует `yield asyncio.run()` для преобразования асинхронного результата в синхронный генератор, который возвращает результат.

*   `create_async`

    ```python
    @staticmethod
    @abstractmethod
    async def create_async(
        model: str,
        messages: Messages,
        **kwargs
    ) -> str:
        """
        Абстрактный метод для создания асинхронных результатов.

        Args:
            model (str): Модель для использования при создании.
            messages (Messages): Сообщения для обработки.
            **kwargs: Дополнительные именованные аргументы.

        Raises:
            NotImplementedError: Если этот метод не переопределен в производных классах.

        Returns:
            str: Созданный результат в виде строки.
        """
        ...
    ```

    **Назначение**:
    Абстрактный метод для создания асинхронных результатов. Этот метод должен быть переопределен в подклассах.

    **Параметры**:
    - `model` (str): Модель для использования при создании.
    - `messages` (Messages): Сообщения для обработки.
    - `**kwargs`: Дополнительные именованные аргументы.

    **Возвращает**:
    - `str`: Созданный результат в виде строки.

    **Вызывает исключения**:
    - `NotImplementedError`: Если метод не переопределен в производных классах.

    **Как работает функция**:

    1.  Метод является абстрактным и должен быть реализован в подклассах `AsyncProvider`.
    2.  При реализации в подклассе, метод должен использовать параметры `model`, `messages` и `kwargs` для взаимодействия с API и создания асинхронного результата.

*   `get_create_function`

    ```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
    ```

    **Назначение**:
    Возвращает функцию для создания завершений.

    **Возвращает**:
    - `callable`: Функция `create_completion`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_completion` класса.

*   `get_async_create_function`

    ```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async
    ```

    **Назначение**:
    Возвращает асинхронную функцию для создания завершений.

    **Возвращает**:
    - `callable`: Асинхронная функция `create_async`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_async` класса.

### `AsyncGeneratorProvider`

Предоставляет функциональность асинхронного генератора для потоковой передачи результатов.

**Описание**:
Этот класс расширяет `AbstractProvider` и предоставляет функциональность для создания асинхронных генераторов, которые позволяют передавать результаты потоком. Он поддерживает потоковую передачу данных и предоставляет методы для создания как синхронных, так и асинхронных генераторов.

#### Методы класса `AsyncGeneratorProvider`

*   `create_completion`

    ```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> CreateResult:
        """
        Создает результат потоковой передачи завершения синхронно.

        Args:
            cls (type): Класс, на котором вызывается этот метод.
            model (str): Модель для использования при создании.
            messages (Messages): Сообщения для обработки.
            stream (bool): Указывает, следует ли передавать результаты потоком. По умолчанию True.
            loop (AbstractEventLoop, optional): Цикл событий для использования. По умолчанию None.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            CreateResult: Результат создания потоковой передачи завершения.
        """
        ...
    ```

    **Назначение**:
    Создает синхронный генератор для потоковой передачи результатов, используя асинхронный генератор `create_async_generator`.

    **Параметры**:
    - `model` (str): Модель для использования при создании.
    - `messages` (Messages): Сообщения для обработки.
    - `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `True`.
    - `**kwargs`: Дополнительные именованные аргументы, передаваемые в `create_async_generator`.

    **Возвращает**:
    - `CreateResult`: Результат создания потоковой передачи завершения.

    **Как работает функция**:

    1.  Вызывает асинхронный генератор `cls.create_async_generator` с переданными аргументами.
    2.  Использует `to_sync_generator` для преобразования асинхронного генератора в синхронный генератор.
    3.  Возвращает синхронный генератор, который выдает результаты потоком.

*   `create_async_generator`

    ```python
    @staticmethod
    @abstractmethod
    async def create_async_generator(
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> AsyncResult:
        """
        Абстрактный метод для создания асинхронного генератора.

        Args:
            model (str): Модель для использования при создании.
            messages (Messages): Сообщения для обработки.
            stream (bool): Указывает, следует ли передавать результаты потоком. По умолчанию True.
            **kwargs: Дополнительные именованные аргументы.

        Raises:
            NotImplementedError: Если этот метод не переопределен в производных классах.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий результаты.
        """
        ...
    ```

    **Назначение**:
    Абстрактный метод для создания асинхронного генератора. Этот метод должен быть переопределен в подклассах.

    **Параметры**:
    - `model` (str): Модель для использования при создании.
    - `messages` (Messages): Сообщения для обработки.
    - `stream` (bool, optional): Указывает, следует ли использовать потоковую передачу результатов. По умолчанию `True`.
    - `**kwargs`: Дополнительные именованные аргументы.

    **Возвращает**:
    - `AsyncResult`: Асинхронный генератор, выдающий результаты.

    **Вызывает исключения**:
    - `NotImplementedError`: Если метод не переопределен в производных классах.

    **Как работает функция**:

    1.  Метод является абстрактным и должен быть реализован в подклассах `AsyncGeneratorProvider`.
    2.  При реализации в подклассе, метод должен использовать параметры `model`, `messages` и `kwargs` для взаимодействия с API и создания асинхронного генератора.

*   `get_create_function`

    ```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
    ```

    **Назначение**:
    Возвращает функцию для создания завершений.

    **Возвращает**:
    - `callable`: Функция `create_completion`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_completion` класса.

*   `get_async_create_function`

    ```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async_generator
    ```

    **Назначение**:
    Возвращает асинхронную функцию для создания завершений.

    **Возвращает**:
    - `callable`: Асинхронная функция `create_async_generator`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_async_generator` класса.

### `ProviderModelMixin`

Миксин для работы с моделями провайдера.

**Описание**:
Этот миксин предоставляет атрибуты и методы для управления моделями, поддерживаемыми провайдером. Он позволяет определять модель по умолчанию, список поддерживаемых моделей и псевдонимы моделей.

#### Методы класса `ProviderModelMixin`

*   `get_models`

    ```python
    @classmethod
    def get_models(cls, **kwargs) -> list[str]:
        if not cls.models and cls.default_model is not None:
            return [cls.default_model]
        return cls.models
    ```

    **Назначение**:
    Возвращает список моделей, поддерживаемых провайдером.

    **Параметры**:
    - `**kwargs`: Дополнительные именованные аргументы.

    **Возвращает**:
    - `list[str]`: Список поддерживаемых моделей.

    **Как работает функция**:

    1.  Проверяет, определен ли список моделей (`cls.models`). Если список не определен и определена модель по умолчанию (`cls.default_model`), возвращает список, содержащий только модель по умолчанию.
    2.  В противном случае возвращает список моделей (`cls.models`).

*   `get_model`

    ```python
    @classmethod
    def get_model(cls, model: str, **kwargs) -> str:
        if not model and cls.default_model is not None:
            model = cls.default_model
        elif model in cls.model_aliases:
            model = cls.model_aliases[model]
        else:
            if model not in cls.get_models(**kwargs) and cls.models:
                raise ModelNotSupportedError(f"Model is not supported: {model} in: {cls.__name__} Valid models: {cls.models}")
        cls.last_model = model
        debug.last_model = model
        return model
    ```

    **Назначение**:
    Возвращает имя модели, используя псевдонимы и проверяя поддержку модели.

    **Параметры**:
    - `model` (str): Имя модели.
    - `**kwargs`: Дополнительные именованные аргументы.

    **Возвращает**:
    - `str`: Имя модели.

    **Вызывает исключения**:
    - `ModelNotSupportedError`: Если модель не поддерживается.

    **Как работает функция**:

    1.  Если `model` не указана и определена модель по умолчанию (`cls.default_model`), использует модель по умолчанию.
    2.  Если `model` есть в `cls.model_aliases`, заменяет `model` на соответствующий псевдоним.
    3.  Если `model` не поддерживается (нет в `cls.get_models(**kwargs)`) и список моделей `cls.models` не пуст, выбрасывает исключение `ModelNotSupportedError`.
    4.  Сохраняет `model` в `cls.last_model` и `debug.last_model`.
    5.  Возвращает `model`.

### `RaiseErrorMixin`

Миксин для обработки ошибок.

**Описание**:
Этот миксин предоставляет статический метод `raise_error` для обработки ошибок, возвращаемых API. Он проверяет наличие ключей `error_message` или `error` в данных и выбрасывает соответствующее исключение.

#### Методы класса `RaiseErrorMixin`

*   `raise_error`

    ```python
    @staticmethod
    def raise_error(data: dict, status: int = None):
        if "error_message" in data:
            raise ResponseError(data["error_message"])
        elif "error" in data:
            if isinstance(data["error"], str):
                if status is not None:
                    if status == 401:
                        raise MissingAuthError(f"Error {status}: {data['error']}")
                    elif status == 402:
                        raise PaymentRequiredError(f"Error {status}: {data['error']}")
                    raise ResponseError(f"Error {status}: {data['error']}")
                raise ResponseError(data["error"])
            elif isinstance(data["error"], bool):
                raise ResponseError(data)
            elif "code" in data["error"]:
                raise ResponseError("\n".join(
                    [e for e in [f'Error {data["error"]["code"]}: {data["error"]["message"]}', data["error"].get("failed_generation")] if e is not None]
                ))
            elif "message" in data["error"]:
                raise ResponseError(data["error"]["message"])
            else:
                raise ResponseError(data["error"])
        elif ("choices" not in data or not data["choices"]) and "data" not in data:
            raise ResponseError(f"Invalid response: {json.dumps(data)}")
    ```

    **Назначение**:
    Вызывает исключение на основе данных об ошибке.

    **Параметры**:
    - `data` (dict): Словарь с данными об ошибке.
    - `status` (int, optional): HTTP-статус код. По умолчанию `None`.

    **Вызывает исключения**:
    - `ResponseError`: Если обнаружено сообщение об ошибке.
    - `MissingAuthError`: Если статус код 401.
    - `PaymentRequiredError`: Если статус код 402.

    **Как работает функция**:

    1.  Проверяет наличие ключа `"error_message"` в словаре `data`. Если он есть, выбрасывает исключение `ResponseError` с соответствующим сообщением.
    2.  Если ключ `"error_message"` отсутствует, проверяет наличие ключа `"error"`.
        - Если `"error"` является строкой, проверяет наличие `status` и, в зависимости от его значения (401 или 402), выбрасывает исключения `MissingAuthError` или `PaymentRequiredError` соответственно. Если `status` не равен 401 или 402, выбрасывает исключение `ResponseError` с сообщением об ошибке и кодом статуса.
        - Если `"error"` является булевым значением, выбрасывает исключение `ResponseError` с данными об ошибке.
        - Если `"error"` является словарем и содержит ключ `"code"`, формирует сообщение об ошибке из кода и сообщения об ошибке и выбрасывает исключение `ResponseError`.
        - Если `"error"` является словарем и содержит ключ `"message"`, выбрасывает исключение `ResponseError` с сообщением об ошибке.
        - В противном случае выбрасывает исключение `ResponseError` с данными об ошибке.
    3.  Если ключи `"choices"` или `"data"` отсутствуют в словаре `data`, выбрасывает исключение `ResponseError` с сообщением о неверном ответе.

### `AuthFileMixin`

Миксин для работы с файлом аутентификации.

**Описание**:
Этот миксин предоставляет метод для получения пути к файлу кэша, используемому для хранения информации об аутентификации.

#### Методы класса `AuthFileMixin`

*   `get_cache_file`

    ```python
    @classmethod
    def get_cache_file(cls) -> Path:
        return Path(get_cookies_dir()) / f"auth_{cls.parent if hasattr(cls, 'parent') else cls.__name__}.json"
    ```

    **Назначение**:
    Возвращает путь к файлу кэша.

    **Возвращает**:
    - `Path`: Путь к файлу кэша.

    **Как работает функция**:

    1.  Получает путь к директории cookies с помощью `get_cookies_dir()`.
    2.  Формирует имя файла кэша, используя имя класса (`cls.__name__`) или имя родительского класса (`cls.parent`, если он существует).
    3.  Возвращает объект `Path`, представляющий путь к файлу кэша.

### `AsyncAuthedProvider`

Предоставляет асинхронную аутентификацию для провайдеров, использующих генераторы.

**Описание**:
Этот класс расширяет `AsyncGeneratorProvider` и `AuthFileMixin` и предоставляет функциональность для асинхронной аутентификации провайдеров. Он использует файл кэша для хранения информации об аутентификации и предоставляет методы для аутентификации, создания запросов и управления файлом кэша.

#### Методы класса `AsyncAuthedProvider`

*   `on_auth_async`

    ```python
    @classmethod
    async def on_auth_async(cls, **kwargs) -> AuthResult:
       if "api_key" not in kwargs:
           raise MissingAuthError(f"API key is required for {cls.__name__}")
       return AuthResult()
    ```

    **Назначение**:
    Асинхронно выполняет аутентификацию провайдера.

    **Параметры**:
    - `**kwargs`: Дополнительные именованные аргументы, содержащие параметры аутентификации.

    **Возвращает**:
    - `AuthResult`: Результат аутентификации.

    **Вызывает исключения**:
    - `MissingAuthError`: Если отсутствует ключ API.

    **Как работает функция**:

    1.  Проверяет наличие ключа `api_key` в `kwargs`. Если ключ отсутствует, выбрасывает исключение `MissingAuthError`.
    2.  Возвращает объект `AuthResult`, представляющий результат аутентификации.

*   `on_auth`

    ```python
    @classmethod
    def on_auth(cls, **kwargs) -> AuthResult:
        auth_result = cls.on_auth_async(**kwargs)
        if hasattr(auth_result, "__aiter__"):
            return to_sync_generator(auth_result)
        return asyncio.run(auth_result)
    ```

    **Назначение**:
    Синхронно выполняет аутентификацию провайдера.

    **Параметры**:
    - `**kwargs`: Дополнительные именованные аргументы, содержащие параметры аутентификации.

    **Возвращает**:
    - `AuthResult`: Результат аутентификации.

    **Как работает функция**:

    1.  Вызывает асинхронный метод `cls.on_auth_async` с переданными аргументами.
    2.  Если результат является асинхронным итератором, преобразует его в синхронный генератор с помощью `to_sync_generator`.
    3.  В противном случае запускает асинхронную операцию с помощью `asyncio.run` и возвращает результат.

*   `get_create_function`

    ```python
    @classmethod
    def get_create_function(cls) -> callable:
        return cls.create_completion
    ```

    **Назначение**:
    Возвращает функцию для создания завершений.

    **Возвращает**:
    - `callable`: Функция `create_completion`.

    **Как работает функция**:

    1.  Функция просто возвращает ссылку на метод `create_completion` класса.

*   `get_async_create_function`

    ```python
    @classmethod
    def get_async_create_function(cls) -> callable:
        return cls.create_async_generator
    ```

    **Назначение**:
    Возвращает асинхронную функцию для создания завершений.

    **