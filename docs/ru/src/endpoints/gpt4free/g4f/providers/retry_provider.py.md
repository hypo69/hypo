# Модуль `retry_provider.py`

## Обзор

Модуль `retry_provider.py` предоставляет классы для реализации логики повторных попыток при использовании различных провайдеров для генерации текста. Он содержит классы `IterListProvider` и `RetryProvider`, которые позволяют перебирать список провайдеров и выполнять повторные попытки в случае сбоев.

## Подробнее

Этот модуль предназначен для обеспечения отказоустойчивости при работе с различными API для генерации текста. Он позволяет автоматически переключаться между провайдерами в случае сбоев и выполнять повторные попытки для повышения надежности.

## Классы

### `IterListProvider`

**Описание**:
Класс `IterListProvider` предоставляет механизм для итерации по списку провайдеров и выполнения запросов к ним.

**Принцип работы**:
Класс принимает список провайдеров и флаг `shuffle`, определяющий, нужно ли перемешивать список провайдеров перед использованием. Методы `create_completion` и `create_async_generator` перебирают провайдеров из списка и пытаются выполнить запрос к каждому из них. В случае успеха возвращается результат, в случае неудачи — происходит переход к следующему провайдеру.

**Аттрибуты**:
- `providers` (List[Type[BaseProvider]]): Список провайдеров для использования.
- `shuffle` (bool): Флаг, определяющий, нужно ли перемешивать список провайдеров. По умолчанию `True`.
- `working` (bool): Флаг, указывающий, что провайдер работает.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

**Методы**:
- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True) -> None`: Инициализирует класс `IterListProvider`.
- `create_completion(model: str, messages: Messages, stream: bool = False, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> CreateResult`: Выполняет запрос к провайдерам из списка и возвращает результат.
- `create_async_generator(model: str, messages: Messages, stream: bool = True, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> AsyncResult`: Асинхронно выполняет запрос к провайдерам из списка и возвращает результат.
- `get_create_function() -> callable`: Возвращает функцию для создания завершения.
- `get_async_create_function() -> callable`: Возвращает асинхронную функцию для создания завершения.
- `get_providers(stream: bool, ignored: list[str]) -> list[ProviderType]`: Возвращает список провайдеров, поддерживающих потоковую передачу данных, исключая провайдеров из списка игнорируемых.

### `RetryProvider`

**Описание**:
Класс `RetryProvider` наследуется от `IterListProvider` и добавляет логику повторных попыток при использовании одного провайдера.

**Принцип работы**:
Класс принимает список провайдеров, флаг `shuffle`, флаг `single_provider_retry`, определяющий, нужно ли выполнять повторные попытки только для одного провайдера, и `max_retries`, определяющий максимальное количество повторных попыток. Если `single_provider_retry` установлен в `True`, то при неудаче запроса к первому провайдеру будет выполнено `max_retries` попыток, прежде чем перейти к следующему провайдеру.

**Аттрибуты**:
- `providers` (List[Type[BaseProvider]]): Список провайдеров для использования.
- `shuffle` (bool): Флаг, определяющий, нужно ли перемешивать список провайдеров. По умолчанию `True`.
- `single_provider_retry` (bool): Флаг, определяющий, нужно ли выполнять повторные попытки только для одного провайдера.
- `max_retries` (int): Максимальное количество повторных попыток для одного провайдера.

**Методы**:
- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True, single_provider_retry: bool = False, max_retries: int = 3) -> None`: Инициализирует класс `RetryProvider`.
- `create_completion(model: str, messages: Messages, stream: bool = False, **kwargs) -> CreateResult`: Выполняет запрос к провайдерам с учетом повторных попыток.
- `create_async_generator(model: str, messages: Messages, stream: bool = True, **kwargs) -> AsyncResult`: Асинхронно выполняет запрос к провайдерам с учетом повторных попыток.

## Функции

### `raise_exceptions`

**Назначение**:
Функция `raise_exceptions` вызывает исключение, если во время повторных попыток возникли какие-либо ошибки.

**Параметры**:
- `exceptions` (dict): Словарь исключений, возникших во время повторных попыток.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `RetryProviderError`: Если какой-либо провайдер столкнулся с исключением.
- `RetryNoProviderError`: Если не найдено ни одного провайдера.

**Как работает функция**:

1. **Проверка наличия исключений**: Функция проверяет, содержит ли словарь `exceptions` какие-либо элементы.
2. **Вызов исключения `RetryProviderError`**: Если словарь `exceptions` не пуст, функция формирует сообщение об ошибке, включающее имена провайдеров и типы возникших исключений, и вызывает исключение `RetryProviderError` с этим сообщением.
3. **Вызов исключения `RetryNoProviderError`**: Если словарь `exceptions` пуст, функция вызывает исключение `RetryNoProviderError` с сообщением о том, что ни один провайдер не найден.

```ascii
Проверка наличия исключений --> Формирование сообщения об ошибке --> Вызов RetryProviderError
     |
     Нет исключений
     |
     Вызов RetryNoProviderError
```

**Примеры**:

Пример вызова функции с исключениями:

```python
exceptions = {"Provider1": ValueError("Some error"), "Provider2": TypeError("Another error")}
try:
    raise_exceptions(exceptions)
except RetryProviderError as ex:
    print(ex)
```

Пример вызова функции без исключений:

```python
exceptions = {}
try:
    raise_exceptions(exceptions)
except RetryNoProviderError as ex:
    print(ex)