# Модуль `retry_provider`

## Обзор

Модуль `retry_provider` предоставляет классы для реализации стратегий повторных попыток при использовании различных поставщиков (providers) для генерации текста или других данных. Он содержит два основных класса: `IterListProvider` и `RetryProvider`. `IterListProvider` перебирает список поставщиков, пока один из них успешно не сгенерирует результат. `RetryProvider` добавляет функциональность повторных попыток для одного поставщика или списка поставщиков.

## Подробнее

Этот модуль полезен в сценариях, когда необходимо обеспечить отказоустойчивость и надежность при работе с внешними сервисами или API, которые могут быть временно недоступны или возвращать ошибки. Он позволяет автоматически повторять запросы к поставщикам, пока не будет получен успешный результат или не будет достигнуто максимальное количество попыток.

## Классы

### `IterListProvider`

**Описание**:
Класс `IterListProvider` является базовым классом для перебора списка поставщиков и использования первого успешного поставщика для генерации результата.

**Принцип работы**:
Класс принимает список поставщиков (`providers`) и флаг (`shuffle`), указывающий, нужно ли перемешивать список поставщиков перед использованием. Метод `create_completion` перебирает поставщиков и пытается сгенерировать результат с помощью каждого из них. Если поставщик возвращает ошибку, метод переходит к следующему поставщику.

**Атрибуты**:
- `providers` (List[Type[BaseProvider]]): Список поставщиков для использования.
- `shuffle` (bool): Флаг, указывающий, нужно ли перемешивать список поставщиков.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

**Методы**:

- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True) -> None:`
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
            shuffle (bool): Флаг, указывающий, нужно ли перемешивать список провайдеров.
        """
    ```

- `create_completion(model: str, messages: Messages, stream: bool = False, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> CreateResult:`
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
        Создает завершение, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель, используемая для завершения.
            messages (Messages): Сообщения, используемые для генерации завершения.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию False.
        Yields:
            CreateResult: Токены или результаты от завершения.
        Raises:
            Exception: Любое исключение, возникшее во время процесса завершения.
        """
    ```
    **Как работает функция**:
    1. Инициализирует словарь `exceptions` для хранения исключений, возникших при использовании разных провайдеров, и переменную `started` для отслеживания, был ли успешно начат процесс генерации результата.
    2. Получает список провайдеров из метода `get_providers`, учитывая поддержку потоковой передачи и список игнорируемых провайдеров.
    3. В цикле перебирает провайдеров из полученного списка. Для каждого провайдера:
        - Устанавливает `self.last_provider` равным текущему провайдеру.
        - Выводит в лог информацию об используемом провайдере.
        - Передает информацию о провайдере в yield, включая его параметры и модель.
        - Пытается получить функцию создания результата (`provider.get_create_function()`) и вызывает её с параметрами `model`, `messages` и `stream`.
        - В цикле перебирает чанки (части) результата, полученные от провайдера.
            - Если чанк не пустой, передает его в yield.
            - Если чанк является строкой или экземпляром `MediaResponse`, устанавливает `started = True`.
        - Если `started == True`, то есть был получен хотя бы один чанк, возвращает управление.
        - Если при работе с провайдером возникло исключение, добавляет его в словарь `exceptions` и выводит информацию об ошибке в лог.
        - Если `started == True`, то есть был получен хотя бы один чанк, но затем возникла ошибка, вызывает исключение.
        - Передает информацию об ошибке в yield.
    4. После перебора всех провайдеров, если ни один из них не вернул результат, вызывает функцию `raise_exceptions`, которая генерирует исключение на основе собранных исключений.
    ```
    Например:
    A - Инициализация
    |
    B - Получение списка провайдеров
    |
    C - Цикл по провайдерам
    |
    D - Попытка получения и обработки результата от провайдера
    |
    E - Обработка исключений
    |
    F - Вызов исключения, если ни один провайдер не вернул результат
    ```

- `create_async_generator(model: str, messages: Messages, stream: bool = True, ignore_stream: bool = False, ignored: list[str] = [], **kwargs) -> AsyncResult:`
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
        Асинхронно создает генератор, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель, используемая для завершения.
            messages (Messages): Сообщения, используемые для генерации завершения.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию True.
        Yields:
            AsyncResult: Токены или результаты от завершения.
        Raises:
            Exception: Любое исключение, возникшее во время процесса завершения.
        """
    ```

- `get_create_function() -> callable:`
    ```python
    def get_create_function(self) -> callable:
        """
        Возвращает функцию для создания завершения.
        Returns:
            callable: Функция для создания завершения.
        """
    ```

- `get_async_create_function() -> callable:`
    ```python
    def get_async_create_function(self) -> callable:
        """
        Возвращает асинхронную функцию для создания генератора.
        Returns:
            callable: Асинхронная функция для создания генератора.
        """
    ```

- `get_providers(stream: bool, ignored: list[str]) -> list[ProviderType]:`
    ```python
    def get_providers(self, stream: bool, ignored: list[str]) -> list[ProviderType]:
        """
        Возвращает список провайдеров, поддерживающих потоковую передачу или не игнорируемых.
        Args:
            stream (bool): Флаг, указывающий, требуется ли потоковая передача.
            ignored (list[str]): Список имен провайдеров, которые следует игнорировать.
        Returns:
            list[ProviderType]: Список провайдеров.
        """
    ```

**Примеры**:

```python
from typing import List, Type
from g4f.providers import BaseProvider, RetryProvider

# Пример использования IterListProvider с двумя поставщиками
# Предположим, что BaseProvider1 и BaseProvider2 - это классы, наследующие BaseProvider
# providers: List[Type[BaseProvider]] = [BaseProvider1, BaseProvider2] # <инструкция для модели gemini:Здесь должны быть классы поставщиков>

# Создание инстанса IterListProvider
# iter_list_provider = IterListProvider(providers=providers, shuffle=True) # <инструкция для модели gemini:Раскомментируй код>

# Использование iter_list_provider для создания завершения
# model = "gpt-3.5-turbo" # <инструкция для модели gemini:Укажи название модели>
# messages = [{"role": "user", "content": "Hello"}] # <инструкция для модели gemini:Задай роль и сообщение>
# for chunk in iter_list_provider.create_completion(model=model, messages=messages, stream=True): # <инструкция для модели gemini:Раскомментируй код>
#     print(chunk, end="") # <инструкция для модели gemini:Раскомментируй код>
```

### `RetryProvider`

**Описание**:
Класс `RetryProvider` является подклассом `IterListProvider` и добавляет функциональность повторных попыток для одного или нескольких поставщиков.

**Принцип работы**:
Класс принимает список поставщиков (`providers`), флаг (`shuffle`), указывающий, нужно ли перемешивать список поставщиков, флаг (`single_provider_retry`), указывающий, нужно ли повторять попытки только для одного поставщика, и максимальное количество попыток (`max_retries`). Если `single_provider_retry` установлен в `True`, класс будет повторять попытки только для первого поставщика в списке, пока не будет получен успешный результат или не будет достигнуто максимальное количество попыток. Если `single_provider_retry` установлен в `False`, класс будет перебирать список поставщиков, как это делает `IterListProvider`, но с возможностью повторных попыток для каждого поставщика.

**Атрибуты**:
- `providers` (List[Type[BaseProvider]]): Список поставщиков для использования.
- `shuffle` (bool): Флаг, указывающий, нужно ли перемешивать список поставщиков.
- `single_provider_retry` (bool): Флаг, указывающий, нужно ли повторять попытки только для одного поставщика.
- `max_retries` (int): Максимальное количество попыток для одного поставщика.

**Методы**:

- `__init__(providers: List[Type[BaseProvider]], shuffle: bool = True, single_provider_retry: bool = False, max_retries: int = 3) -> None:`
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
            shuffle (bool): Флаг, указывающий, нужно ли перемешивать список провайдеров.
            single_provider_retry (bool): Флаг, указывающий, следует ли повторять попытки для одного провайдера, если он не удался.
            max_retries (int): Максимальное количество повторных попыток для одного провайдера.
        """
    ```

- `create_completion(model: str, messages: Messages, stream: bool = False, **kwargs) -> CreateResult:`
    ```python
    def create_completion(
        self,
        model: str,
        messages: Messages,
        stream: bool = False,
        **kwargs,
    ) -> CreateResult:
        """
        Создает завершение, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель, используемая для завершения.
            messages (Messages): Сообщения, используемые для генерации завершения.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию False.
        Yields:
            CreateResult: Токены или результаты от завершения.
        Raises:
            Exception: Любое исключение, возникшее во время процесса завершения.
        """
    ```

- `create_async_generator(model: str, messages: Messages, stream: bool = True, **kwargs) -> AsyncResult:`
    ```python
    async def create_async_generator(
        self,
        model: str,
        messages: Messages,
        stream: bool = True,
        **kwargs
    ) -> AsyncResult:
        """
        Асинхронно создает генератор, используя доступных провайдеров, с возможностью потоковой передачи ответа.
        Args:
            model (str): Модель, используемая для завершения.
            messages (Messages): Сообщения, используемые для генерации завершения.
            stream (bool, optional): Флаг, указывающий, следует ли передавать ответ потоком. По умолчанию True.
        Yields:
            AsyncResult: Токены или результаты от завершения.
        Raises:
            Exception: Любое исключение, возникшее во время процесса завершения.
        """
    ```

**Примеры**:

```python
from typing import List, Type
from g4f.providers import BaseProvider, RetryProvider

# Пример использования RetryProvider с двумя поставщиками и повторными попытками для каждого поставщика
# Предположим, что BaseProvider1 и BaseProvider2 - это классы, наследующие BaseProvider
# providers: List[Type[BaseProvider]] = [BaseProvider1, BaseProvider2] # <инструкция для модели gemini:Укажи классы поставщиков>

# Создание инстанса RetryProvider
# retry_provider = RetryProvider(providers=providers, shuffle=True, single_provider_retry=False, max_retries=3) # <инструкция для модели gemini:Раскомментируй код>

# Использование retry_provider для создания завершения
# model = "gpt-3.5-turbo" # <инструкция для модели gemini:Укажи название модели>
# messages = [{"role": "user", "content": "Hello"}] # <инструкция для модели gemini:Укажи роль и сообщение>
# for chunk in retry_provider.create_completion(model=model, messages=messages, stream=True): # <инструкция для модели gemini:Раскомментируй код>
#     print(chunk, end="") # <инструкция для модели gemini:Раскомментируй код>
```

## Функции

### `raise_exceptions(exceptions: dict) -> None`

```python
def raise_exceptions(exceptions: dict) -> None:
    """
    Вызывает объединенное исключение, если какие-либо произошли во время повторных попыток.

    Raises:
        RetryProviderError: Если какой-либо провайдер столкнулся с исключением.
        RetryNoProviderError: Если ни один провайдер не найден.
    """
```

**Назначение**:
Функция `raise_exceptions` предназначена для обработки исключений, которые могут возникнуть при использовании нескольких поставщиков (providers) в стратегиях повторных попыток. Она анализирует словарь исключений и вызывает соответствующее исключение в зависимости от ситуации.

**Как работает функция**:
1. Проверяет, является ли словарь `exceptions` пустым.
2. Если словарь `exceptions` не пуст, это означает, что во время повторных попыток возникли исключения. В этом случае функция вызывает исключение `RetryProviderError`, которое содержит информацию обо всех произошедших исключениях.
3. Если словарь `exceptions` пуст, это означает, что ни один из поставщиков не был найден. В этом случае функция вызывает исключение `RetryNoProviderError`.
```
ASCII flowchart:

    A - Проверка, есть ли исключения
    |
    B - Если есть исключения, вызывается RetryProviderError с информацией о каждом исключении
    |
    C - Если нет исключений, вызывается RetryNoProviderError
```

**Примеры**:

```python
from g4f.errors import RetryProviderError, RetryNoProviderError
from g4f.providers.retry_provider import raise_exceptions

# Пример 1: Вызов RetryProviderError
# exceptions = {"Provider1": ValueError("Invalid value"), "Provider2": TypeError("Invalid type")} # <инструкция для модели gemini:Определить словарь исключений>
# try: # <инструкция для модели gemini:Раскомментируй код>
#     raise_exceptions(exceptions) # <инструкция для модели gemini:Раскомментируй код>
# except RetryProviderError as e: # <инструкция для модели gemini:Раскомментируй код>
#     print(e) # <инструкция для модели gemini:Раскомментируй код>

# Пример 2: Вызов RetryNoProviderError
# exceptions = {} # <инструкция для модели gemini:Определить пустой словарь исключений>
# try: # <инструкция для модели gemini:Раскомментируй код>
#     raise_exceptions(exceptions) # <инструкция для модели gemini:Раскомментируй код>
# except RetryNoProviderError as e: # <инструкция для модели gemini:Раскомментируй код>
#     print(e) # <инструкция для модели gemini:Раскомментируй код>