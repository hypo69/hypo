# Модуль для выполнения инструментов (`run_tools.py`)

## Обзор

Модуль `run_tools.py` предназначен для обработки различных инструментов, таких как поиск в интернете, продолжение генерации текста и работа с хранилищем данных (bucket). Он содержит классы и функции для валидации аргументов инструментов, выполнения асинхронных и синхронных операций, управления ключами API и обработки результатов "размышлений" модели.

## Подробнее

Этот модуль является важной частью системы, поскольку он обеспечивает возможность расширения функциональности AI-моделей за счет использования внешних инструментов. Он позволяет моделям выполнять поиск информации в интернете, обращаться к хранилищу данных и продолжать генерацию текста с учетом предыдущего контекста.

## Классы

### `ToolHandler`

**Описание**: Класс `ToolHandler` предназначен для обработки различных типов инструментов. Он предоставляет статические методы для валидации аргументов инструментов и выполнения конкретных операций для каждого типа инструмента.

**Методы**:

- `validate_arguments(data: dict) -> dict`:
    ```python
    def validate_arguments(data: dict) -> dict:
        """
        Выполняет валидацию и разбор аргументов инструмента, представленных в виде словаря.

        Args:
            data (dict): Словарь, содержащий данные инструмента, включая аргументы.

        Returns:
            dict: Отфильтрованный словарь с аргументами инструмента.

        Raises:
            ValueError: Если аргументы инструмента не являются словарем или JSON-строкой.

        Как работает функция:
        1. Проверяет наличие ключа "arguments" в словаре `data`.
        2. Если "arguments" является строкой, пытается распарсить её как JSON.
        3. Проверяет, что "arguments" является словарем. Если нет, вызывает исключение ValueError.
        4. Фильтрует значения None в словаре аргументов с помощью функции filter_none.

        ASCII flowchart:

        Начало --> Проверка наличия 'arguments' --> [arguments is str?] --Да--> JSON.loads(arguments) --> [arguments is dict?] --Нет--> ValueError
                                                  --Нет--> [arguments is dict?] --Да--> filter_none(arguments)
                                                                             --Нет--> ValueError
        """
    ```

- `process_search_tool(messages: Messages, tool: dict) -> Messages`:
    ```python
    async def process_search_tool(messages: Messages, tool: dict) -> Messages:
        """
        Выполняет поисковый запрос и обновляет сообщения с результатами поиска.

        Args:
            messages (Messages): Список сообщений, представляющих контекст диалога.
            tool (dict): Словарь, содержащий информацию об инструменте поиска.

        Returns:
            Messages: Обновленный список сообщений с результатами поиска.
            Sources: Источники, найденные в результате поиска.

        Как работает функция:
        1. Создает копию списка сообщений.
        2. Валидирует и извлекает аргументы инструмента поиска.
        3. Выполняет поисковый запрос с помощью функции `do_search`.
        4. Обновляет последнее сообщение в списке сообщений результатами поиска.
        5. Возвращает обновленный список сообщений и источники.

        ASCII flowchart:

        Начало --> messages.copy() --> validate_arguments(tool["function"]) --> do_search() --> Обновление messages[-1]["content"] --> Конец
        """
    ```

- `process_continue_tool(messages: Messages, tool: dict, provider: Any) -> Tuple[Messages, Dict[str, Any]]`:
    ```python
    @staticmethod
    def process_continue_tool(messages: Messages, tool: dict, provider: Any) -> Tuple[Messages, Dict[str, Any]]:
        """
        Обрабатывает запрос на продолжение генерации текста.

        Args:
            messages (Messages): Список сообщений, представляющих контекст диалога.
            tool (dict): Словарь, содержащий информацию об инструменте продолжения.
            provider (Any): Провайдер модели.

        Returns:
            Tuple[Messages, Dict[str, Any]]: Обновленный список сообщений и дополнительные аргументы для провайдера.

        Как работает функция:
        1. Создает копию списка сообщений, если провайдер не "OpenaiAccount" или "HuggingFaceAPI".
        2. Извлекает последнюю строку из последнего сообщения.
        3. Формирует новое сообщение с запросом на продолжение с этой строки.
        4. Добавляет новое сообщение в список сообщений.
        5. Возвращает обновленный список сообщений и словарь с аргументом "action": "continue", если провайдер "OpenaiAccount" или "HuggingFaceAPI".

        ASCII flowchart:

        Начало --> [provider not in ("OpenaiAccount", "HuggingFaceAPI")] --Да--> messages.copy() --> Извлечение последней строки --> Формирование нового сообщения --> messages.append() --> Конец
                                                                          --Нет--> kwargs["action"] = "continue" --> Конец
        """
    ```

- `process_bucket_tool(messages: Messages, tool: dict) -> Messages`:
    ```python
    @staticmethod
    def process_bucket_tool(messages: Messages, tool: dict) -> Messages:
        """
        Обрабатывает запросы к хранилищу данных (bucket) и заменяет идентификаторы хранилища содержимым.

        Args:
            messages (Messages): Список сообщений, представляющих контекст диалога.
            tool (dict): Словарь, содержащий информацию об инструменте хранилища.

        Returns:
            Messages: Обновленный список сообщений с содержимым хранилища.

        Как работает функция:
        1. Создает копию списка сообщений.
        2. Определяет внутреннюю функцию `on_bucket`, которая считывает содержимое хранилища по идентификатору.
        3. Проходит по всем сообщениям и заменяет идентификаторы хранилища содержимым с помощью регулярного выражения.
        4. Если в последнем сообщении есть маркер источника, добавляет инструкцию о добавлении источников цитирования.
        5. Возвращает обновленный список сообщений.

        ASCII flowchart:

        Начало --> messages.copy() --> Определение on_bucket() --> Проход по сообщениям --> re.sub() --> [Замена произошла?] --Да--> has_bucket = True
                                                                                                    --Нет-->
                --> [has_bucket and last_message contains "\\nSource: "] --Да--> Добавление BUCKET_INSTRUCTIONS --> Конец
                                                                        --Нет--> Конец
        """
    ```

- `process_tools(messages: Messages, tool_calls: List[dict], provider: Any) -> Tuple[Messages, Dict[str, Any]]`:
    ```python
    @staticmethod
    async def process_tools(messages: Messages, tool_calls: List[dict], provider: Any) -> Tuple[Messages, Dict[str, Any]]:
        """
        Обрабатывает список вызовов инструментов и возвращает обновленные сообщения и дополнительные аргументы.

        Args:
            messages (Messages): Список сообщений, представляющих контекст диалога.
            tool_calls (List[dict]): Список словарей, содержащих информацию о вызовах инструментов.
            provider (Any): Провайдер модели.

        Returns:
            Tuple[Messages, Dict[str, Any]]: Обновленный список сообщений, источники и дополнительные аргументы для провайдера.

        Как работает функция:
        1. Проверяет, есть ли вызовы инструментов. Если нет, возвращает исходные сообщения и пустой словарь.
        2. Создает копию списка сообщений.
        3. Проходит по всем вызовам инструментов.
        4. Для каждого вызова определяет имя функции и вызывает соответствующий метод `ToolHandler` для обработки инструмента.
        5. Обновляет список сообщений и словарь дополнительных аргументов.
        6. Возвращает обновленный список сообщений, источники и словарь дополнительных аргументов.

        ASCII flowchart:

        Начало --> [tool_calls?] --Нет--> Конец
                          --Да--> messages.copy() --> Проход по tool_calls --> Определение function_name --> Вызов ToolHandler.process_*_tool() --> Обновление messages и extra_kwargs --> Конец
        """
    ```

### `AuthManager`

**Описание**: Класс `AuthManager` управляет ключами API.

**Методы**:

- `get_api_key_file(cls) -> Path`:
    ```python
    @staticmethod
    def get_api_key_file(cls) -> Path:
        """
        Возвращает путь к файлу, содержащему ключ API для указанного провайдера.

        Args:
            cls: Класс провайдера.

        Returns:
            Path: Объект Path, представляющий путь к файлу ключа API.

        Как работает функция:
        1. Определяет имя файла ключа API на основе имени класса провайдера.
        2. Возвращает объект Path, представляющий путь к файлу в директории cookies.

        ASCII flowchart:

        Начало --> Определение имени файла --> Возврат Path к файлу --> Конец
        """
    ```

- `load_api_key(provider: Any) -> Optional[str]`:
    ```python
    @staticmethod
    def load_api_key(provider: Any) -> Optional[str]:
        """
        Загружает ключ API из файла конфигурации, если это необходимо.

        Args:
            provider (Any): Провайдер, для которого требуется ключ API.

        Returns:
            Optional[str]: Ключ API или None, если он не требуется или не найден.

        Как работает функция:
        1. Проверяет, требуется ли провайдеру аутентификация. Если нет, возвращает None.
        2. Получает путь к файлу ключа API с помощью метода `get_api_key_file`.
        3. Пытается загрузить ключ API из файла.
        4. В случае ошибки логирует исключение и возвращает None.

        ASCII flowchart:

        Начало --> [provider.needs_auth?] --Нет--> Конец (None)
                                     --Да--> get_api_key_file() --> [Файл существует?] --Да--> Загрузка ключа из файла --> Конец
                                                                                    --Нет--> Конец (None)
        """
    ```

### `ThinkingProcessor`

**Описание**: Класс `ThinkingProcessor` обрабатывает чанки "размышлений".

**Методы**:

- `process_thinking_chunk(chunk: str, start_time: float = 0) -> Tuple[float, List[Union[str, Reasoning]]]`:
    ```python
    @staticmethod
    def process_thinking_chunk(chunk: str, start_time: float = 0) -> Tuple[float, List[Union[str, Reasoning]]]:
        """
        Обрабатывает чанк "размышлений" и возвращает время и результаты.

        Args:
            chunk (str): Чанк текста, содержащий информацию о "размышлениях".
            start_time (float, optional): Время начала "размышлений". По умолчанию 0.

        Returns:
            Tuple[float, List[Union[str, Reasoning]]]: Время окончания "размышлений" и список результатов.

        Как работает функция:
        1. Определяет, является ли чанк не-thinking чанком (не содержит "<think>" и "</think>"). Если да, возвращает исходный чанк.
        2. Обрабатывает начало "размышлений" ("<think>").
        3. Обрабатывает окончание "размышлений" ("</think>").
        4. Обрабатывает текущее состояние "размышлений".
        5. Возвращает время и список результатов.

        ASCII flowchart:

        Начало --> [chunk содержит "<think>" или "</think">?] --Нет--> Возврат исходного чанка
                                                               --Да--> [chunk содержит "<think>"] --Да--> Обработка начала "размышлений"
                                                                                           --Нет--> [chunk содержит "</think>"] --Да--> Обработка окончания "размышлений"
                                                                                                                            --Нет--> Обработка текущего состояния "размышлений"
        """
    ```

## Функции

### `perform_web_search(messages: Messages, web_search_param: Any) -> Tuple[Messages, Optional[Sources]]`

```python
async def perform_web_search(messages: Messages, web_search_param: Any) -> Tuple[Messages, Optional[Sources]]:
    """
    Выполняет поиск в интернете и возвращает обновленные сообщения и источники.

    Args:
        messages (Messages): Список сообщений, представляющих контекст диалога.
        web_search_param (Any): Параметр поиска в интернете.

    Returns:
        Tuple[Messages, Optional[Sources]]: Обновленный список сообщений и источники.

    Как работает функция:
    1. Создает копию списка сообщений.
    2. Проверяет, нужно ли выполнять поиск в интернете. Если нет, возвращает исходные сообщения и None.
    3. Извлекает поисковый запрос из параметра `web_search_param`.
    4. Выполняет поисковый запрос с помощью функции `do_search`.
    5. В случае ошибки логирует исключение.
    6. Возвращает обновленный список сообщений и источники.

    ASCII flowchart:

    Начало --> messages.copy() --> [web_search_param?] --Нет--> Конец (messages, None)
                                              --Да--> Извлечение поискового запроса --> do_search() --> Конец
    """
```

### `async_iter_run_tools(provider: ProviderType, model: str, messages: Messages, tool_calls: Optional[List[dict]] = None, **kwargs) -> AsyncIterator`

```python
async def async_iter_run_tools(
    provider: ProviderType, 
    model: str, 
    messages: Messages, 
    tool_calls: Optional[List[dict]] = None, 
    **kwargs
) -> AsyncIterator:
    """
    Асинхронно выполняет инструменты и возвращает результаты.

    Args:
        provider (ProviderType): Провайдер модели.
        model (str): Имя модели.
        messages (Messages): Список сообщений, представляющих контекст диалога.
        tool_calls (Optional[List[dict]], optional): Список вызовов инструментов. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncIterator: Чанки ответа.

    Как работает функция:
    1. Выполняет поиск в интернете, если указан параметр `web_search`.
    2. Загружает ключ API, если это необходимо.
    3. Обрабатывает вызовы инструментов с помощью `ToolHandler.process_tools`.
    4. Генерирует ответ с помощью асинхронной функции `create_function` провайдера.
    5. Возвращает чанки ответа.
    6. Возвращает источники, если они есть.

    ASCII flowchart:

    Начало --> perform_web_search() --> load_api_key() --> ToolHandler.process_tools() --> create_function() --> Возврат чанков ответа --> Конец
    """
```

### `iter_run_tools(iter_callback: Callable, model: str, messages: Messages, provider: Optional[str] = None, tool_calls: Optional[List[dict]] = None, **kwargs) -> Iterator`

```python
def iter_run_tools(
    iter_callback: Callable,
    model: str,
    messages: Messages,
    provider: Optional[str] = None,
    tool_calls: Optional[List[dict]] = None,
    **kwargs
) -> Iterator:
    """
    Синхронно выполняет инструменты и возвращает результаты.

    Args:
        iter_callback (Callable): Функция обратного вызова для итерации по чанкам ответа.
        model (str): Имя модели.
        messages (Messages): Список сообщений, представляющих контекст диалога.
        provider (Optional[str], optional): Провайдер модели. По умолчанию None.
        tool_calls (Optional[List[dict]], optional): Список вызовов инструментов. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Yields:
        Iterator: Чанки ответа.

    Как работает функция:
    1. Выполняет поиск в интернете, если указан параметр `web_search`.
    2. Загружает ключ API, если это необходимо.
    3. Обрабатывает вызовы инструментов.
    4. Обрабатывает чанки ответа с помощью `ThinkingProcessor`.
    5. Возвращает чанки ответа.
    6. Возвращает источники, если они есть.

    ASCII flowchart:

    Начало --> perform_web_search() --> load_api_key() --> Обработка tool_calls --> iter_callback() --> ThinkingProcessor.process_thinking_chunk() --> Возврат чанков ответа --> Конец
    """