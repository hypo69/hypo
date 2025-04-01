# Модуль поддержки инструментов

## Обзор

Модуль `tool_support.py` предоставляет класс `ToolSupportProvider`, который является асинхронным провайдером для работы с инструментами (tools) в запросах к моделям. Он позволяет использовать инструменты, такие как JSON, для форматирования ответов.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с различными моделями, поддерживающими инструменты, такие как JSON. Он обрабатывает запросы, форматирует сообщения и предоставляет ответы в нужном формате.
Модуль использует другие модули проекта, такие как `typing`, `service`, `helper`, `base_provider` и `response`.

## Классы

### `ToolSupportProvider`

**Описание**:
Класс `ToolSupportProvider` предоставляет асинхронный генератор для поддержки инструментов при взаимодействии с моделями.

**Наследует**:
`AsyncGeneratorProvider` - базовый класс для асинхронных провайдеров генераторов.

**Атрибуты**:
- `working` (bool): Флаг, указывающий, работает ли провайдер. Установлен в `True`.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    media: MediaListType = None,
    tools: list[str] = None,
    response_format: dict = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для работы с моделями, поддерживающими инструменты.

    Args:
        model (str): Имя модели. Может включать имя провайдера через двоеточие (например, "provider:model").
        messages (Messages): Список сообщений для отправки в модель.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `True`.
        media (MediaListType, optional): Список медиафайлов для отправки в модель. По умолчанию `None`.
        tools (list[str], optional): Список инструментов для использования. Поддерживается только один инструмент. По умолчанию `None`.
        response_format (dict, optional): Формат ответа. По умолчанию `None`.
        **kwargs: Дополнительные аргументы, передаваемые в функцию создания модели.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки данных.

    Raises:
        ValueError: Если передано более одного инструмента.

    Как работает функция:
    1.  Определяется провайдер и модель на основе входного параметра `model`. Если в `model` указан провайдер через двоеточие, то он извлекается.
    2.  Полученные провайдер и модель передаются в функцию `get_model_and_provider`, которая возвращает соответствующие объекты.
    3.  Если указаны инструменты (`tools` is not `None`):
        *   Проверяется, что передан только один инструмент. Если инструментов больше одного, вызывается исключение `ValueError`.
        *   Если `response_format` не указан, устанавливается значение по умолчанию `{"type": "json"}`.
        *   Извлекаются параметры инструмента и формируется сообщение для модели с инструкцией о формате ответа.
        *   Обновляется список сообщений (`messages`), добавляя в начало сообщение с инструкцией о формате ответа.
    4.  Инициализируются переменные `finish`, `chunks` и `has_usage` для хранения промежуточных результатов.
    5.  Вызывается асинхронный генератор `provider.get_async_create_function()`, который возвращает чанки данных от модели.
    6.  В цикле перебираются чанки данных:
        *   Если чанк является строкой (`str`), он добавляется в список `chunks`.
        *   Если чанк является объектом `Usage`, он передается в вызывающий код и устанавливается флаг `has_usage`.
        *   Если чанк является объектом `FinishReason`, он сохраняется в переменной `finish` и цикл завершается.
        *   В противном случае чанк передается в вызывающий код.
    7.  Если не было информации об использовании токенов (`not has_usage`), генерируется объект `Usage` на основе длины накопленных чанков и передается в вызывающий код.
    8.  Накопленные чанки объединяются в одну строку (`chunks`).
    9.  Если использовались инструменты (`tools` is not `None`):
        *   Формируется объект `ToolCalls` с информацией о вызове инструмента, включая имя функции и аргументы, извлеченные из чанков.
        *   Объект `ToolCalls` передается в вызывающий код.
    10. Объединенная строка чанков передается в вызывающий код.
    11. Если была получена причина завершения (`finish` is not `None`), она передается в вызывающий код.

    A --> get_model_and_provider
    |
    B --> Проверка инструментов
    |
    C --> provider.get_async_create_function
    |
    D --> Обработка чанков
    |
    E --> ToolCalls
    |
    F

    Примеры:
    async def example():
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        async for chunk in ToolSupportProvider.create_async_generator(model=model, messages=messages):
            print(chunk)

    """
    provider = None
    if ":" in model:
        provider, model = model.split(":", 1)
    model, provider = get_model_and_provider(
        model, provider,
        stream, logging=False,
        has_images=media is not None
    )
    if tools is not None:
        if len(tools) > 1:
            raise ValueError("Only one tool is supported.")
        if response_format is None:
            response_format = {"type": "json"}
        tools = tools.pop()
        lines = ["Respone in JSON format."]
        properties = tools["function"]["parameters"]["properties"]
        properties = {key: value["type"] for key, value in properties.items()}
        lines.append(f"Response format: {json.dumps(properties, indent=2)}")
        messages = [{"role": "user", "content": "\\n".join(lines)}] + messages

    finish = None
    chunks = []
    has_usage = False
    async for chunk in provider.get_async_create_function()(
        model,
        messages,
        stream=stream,
        media=media,
        response_format=response_format,
        **kwargs
    ):
        if isinstance(chunk, str):
            chunks.append(chunk)
        elif isinstance(chunk, Usage):
            yield chunk
            has_usage = True
        elif isinstance(chunk, FinishReason):
            finish = chunk
            break
        else:
            yield chunk

    if not has_usage:
        yield Usage(completion_tokens=len(chunks), total_tokens=len(chunks))

    chunks = "".join(chunks)
    if tools is not None:
        yield ToolCalls([{\
            "id": "",\
            "type": "function",\
            "function": {\
                "name": tools["function"]["name"],\
                "arguments": filter_json(chunks)\
            }\
        }])
    yield chunks

    if finish is not None:
        yield finish