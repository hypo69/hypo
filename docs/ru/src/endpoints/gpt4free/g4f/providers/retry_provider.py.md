# Модуль retry_provider

## Обзор

Модуль `retry_provider` предоставляет классы `IterListProvider` и `RetryProvider` для организации отказоустойчивой работы с несколькими провайдерами, выполняющими задачи completion (например, генерацию текста). Он позволяет перебирать список провайдеров, повторно выполнять запросы в случае ошибок и обрабатывать потоковые ответы.

## Подробнее

Этот модуль предназначен для использования в системах, требующих высокой надежности при работе с внешними сервисами, такими как AI-модели. Он позволяет автоматически переключаться на резервные провайдеры в случае недоступности основных, а также повторять запросы при временных сбоях.

## Классы

### `IterListProvider`

**Описание**: Класс `IterListProvider` предназначен для последовательного перебора списка провайдеров и выполнения запросов completion с использованием первого доступного и работоспособного провайдера.

**Принцип работы**:
1.  При инициализации класс принимает список провайдеров, флаг для перемешивания списка и устанавливает начальные значения.
2.  Метод `create_completion` перебирает провайдеров из списка.
3.  Для каждого провайдера вызывается функция `get_create_function`, которая выполняет запрос completion.
4.  Если провайдер возвращает результат, он передается вызывающей стороне.
5.  Если провайдер вызывает исключение, оно обрабатывается, и происходит переход к следующему провайдеру.

**Аттрибуты**:
- `providers` (List[Type[BaseProvider]]): Список провайдеров для использования.
- `shuffle` (bool): Флаг, указывающий, нужно ли перемешивать список провайдеров.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

**Методы**:

- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True) -> None`:
    Инициализирует `IterListProvider` с заданным списком провайдеров и параметрами.
- `create_completion(model: str, messages: Messages, stream: bool = False, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> CreateResult`:
    Создает completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
- `create_async_generator(model: str, messages: Messages, stream: bool = True, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> AsyncResult`:
    Асинхронно создает completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
- `get_create_function() -> callable`:
    Возвращает функцию для создания completion (`create_completion`).
- `get_async_create_function() -> callable`:
    Возвращает асинхронную функцию для создания completion (`create_async_generator`).
- `get_providers(stream: bool, ignored: list[str]) -> list[ProviderType]`:
    Возвращает список провайдеров, поддерживающих потоковую передачу, исключая игнорируемые.

#### `__init__`
```python
    def __init__(
        self,
        providers: List[Type[BaseProvider]],
        shuffle: bool = True
    ) -> None:
        """
        Инициализирует BaseRetryProvider.
        Args:
            providers (List[Type[BaseProvider]]): Список провайдеров для использования.
            shuffle (bool): Определяет, следует ли перемешивать список провайдеров.
            single_provider_retry (bool): Определяет, следует ли повторять попытки для одного провайдера в случае сбоя.
            max_retries (int): Максимальное количество повторных попыток для одного провайдера.
        """
```

#### `create_completion`
```python
    def create_completion(
        self,
        model: str,
        messages: Messages,
        stream: bool = False,
        ignore_stream: bool = False,
        ignored: list[str] = [],
        **kwargs,
    ) -> CreateResult:
        """
        Создает completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель для использования для completion.
            messages (Messages): Сообщения для использования при генерации completion.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию False.
        Yields:
            CreateResult: Токены или результаты из completion.
        Raises:
            Exception: Любое исключение, возникшее во время процесса completion.
        """
```

#### `create_async_generator`
```python
    async def create_async_generator(
        self,
        model: str,
        messages: Messages,
        stream: bool = True,
        ignore_stream: bool = False,
        ignored: list[str] = [],
        **kwargs
    ) -> AsyncResult:
        """
        Асинхронно создает генератор completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель для использования для completion.
            messages (Messages): Сообщения для использования при генерации completion.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию True.
        Yields:
            AsyncResult: Асинхронные токены или результаты из completion.
        Raises:
            Exception: Любое исключение, возникшее во время процесса completion.
        """
```

#### `get_create_function`
```python
    def get_create_function(self) -> callable:
        """
        Возвращает функцию для создания completion.
        Returns:
            callable: Функция для создания completion (self.create_completion).
        """
```

#### `get_async_create_function`
```python
    def get_async_create_function(self) -> callable:
        """
        Возвращает асинхронную функцию для создания completion.
        Returns:
            callable: Асинхронная функция для создания completion (self.create_async_generator).
        """
```

#### `get_providers`
```python
    def get_providers(self, stream: bool, ignored: list[str]) -> list[ProviderType]:
        """
        Возвращает список провайдеров, поддерживающих потоковую передачу, исключая игнорируемые.
        Args:
            stream (bool): Флаг, указывающий, нужна ли поддержка потоковой передачи.
            ignored (list[str]): Список имен провайдеров, которые следует игнорировать.
        Returns:
            list[ProviderType]: Список провайдеров, соответствующих критериям.
        """
```

### `RetryProvider`

**Описание**: Класс `RetryProvider` наследуется от `IterListProvider` и добавляет функциональность повторных попыток выполнения запросов completion при возникновении ошибок.

**Принцип работы**:
1.  При инициализации класс принимает список провайдеров, флаг для перемешивания списка, флаг для повторных попыток для одного провайдера и максимальное количество повторных попыток.
2.  Метод `create_completion` проверяет, нужно ли выполнять повторные попытки для одного провайдера.
3.  Если флаг установлен, выполняется заданное количество попыток с использованием первого провайдера из списка.
4.  Если провайдер возвращает результат, он передается вызывающей стороне.
5.  Если провайдер вызывает исключение, оно обрабатывается, и выполняется следующая попытка.
6.  Если после всех попыток не удалось получить результат, вызывается исключение.
7.  Если флаг не установлен, вызывается метод `create_completion` родительского класса `IterListProvider`, который перебирает всех провайдеров из списка.

**Наследует**:
- `IterListProvider`: Наследует функциональность последовательного перебора провайдеров.

**Аттрибуты**:
- `single_provider_retry` (bool): Флаг, указывающий, нужно ли выполнять повторные попытки только для одного провайдера.
- `max_retries` (int): Максимальное количество повторных попыток.

**Методы**:

- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True, single_provider_retry: bool = False, max_retries: int = 3) -> None`:
    Инициализирует `RetryProvider` с заданным списком провайдеров и параметрами повторных попыток.
- `create_completion(model: str, messages: Messages, stream: bool = False, **kwargs) -> CreateResult`:
    Создает completion, используя доступных провайдеров, с возможностью повторных попыток и потоковой передачи ответа.
- `create_async_generator(model: str, messages: Messages, stream: bool = True, **kwargs) -> AsyncResult`:
    Асинхронно создает completion, используя доступных провайдеров, с возможностью повторных попыток и потоковой передачи ответа.

#### `__init__`
```python
    def __init__(
        self,
        providers: List[Type[BaseProvider]],
        shuffle: bool = True,
        single_provider_retry: bool = False,
        max_retries: int = 3,
    ) -> None:
        """
        Инициализирует BaseRetryProvider.
        Args:
            providers (List[Type[BaseProvider]]): Список провайдеров для использования.
            shuffle (bool): Определяет, следует ли перемешивать список провайдеров.
            single_provider_retry (bool): Определяет, следует ли повторять попытки для одного провайдера в случае сбоя.
            max_retries (int): Максимальное количество повторных попыток для одного провайдера.
        """
```

#### `create_completion`
```python
    def create_completion(
        self,
        model: str,
        messages: Messages,
        stream: bool = False,
        **kwargs,
    ) -> CreateResult:
        """
        Создает completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель для использования для completion.
            messages (Messages): Сообщения для использования при генерации completion.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию False.
        Yields:
            CreateResult: Токены или результаты из completion.
        Raises:
            Exception: Любое исключение, возникшее во время процесса completion.
        """
```

#### `create_async_generator`
```python
    async def create_async_generator(
        self,
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> AsyncResult:
        """
        Асинхронно создает completion, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель для использования для completion.
            messages (Messages): Сообщения для использования при генерации completion.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию True.
        Yields:
            AsyncResult: Асинхронные токены или результаты из completion.
        Raises:
            Exception: Любое исключение, возникшее во время процесса completion.
        """
```

## Функции

### `raise_exceptions`

```python
def raise_exceptions(exceptions: dict) -> None:
    """
    Raise a combined exception if any occurred during retries.

    Raises:
        RetryProviderError: If any provider encountered an exception.
        RetryNoProviderError: If no provider is found.
    """
```

**Назначение**: Функция `raise_exceptions` предназначена для генерации исключений, если во время повторных попыток произошли какие-либо ошибки.

**Как работает функция**:

1.  Функция принимает словарь `exceptions`, содержащий информацию об исключениях, возникших у разных провайдеров.
2.  Если словарь `exceptions` не пуст, функция генерирует исключение `RetryProviderError`, которое содержит объединенное сообщение об ошибках от всех провайдеров.
3.  Если словарь `exceptions` пуст, функция генерирует исключение `RetryNoProviderError`, указывающее, что ни один провайдер не был найден.

```
    A (Проверка наличия исключений)
    |
    -- B (Если исключения есть: создание сообщения об ошибке)
    |  |
    |  -- C (Генерация RetryProviderError)
    |
    -- D (Если исключений нет: генерация RetryNoProviderError)
```

**Параметры**:
- `exceptions` (dict): Словарь, содержащий исключения, возникшие у разных провайдеров.

**Возвращает**:
- None

**Вызывает исключения**:
- `RetryProviderError`: Если какой-либо провайдер столкнулся с исключением.
- `RetryNoProviderError`: Если ни один провайдер не найден.

**Примеры**:

Пример 1: Возникли исключения у провайдеров.

```python
exceptions = {
    "Provider1": ValueError("Invalid value"),
    "Provider2": TimeoutError("Request timed out")
}
try:
    raise_exceptions(exceptions)
except RetryProviderError as ex:
    print(ex)
```

Пример 2: Ни один провайдер не найден.

```python
exceptions = {}
try:
    raise_exceptions(exceptions)
except RetryNoProviderError as ex:
    print(ex)
```