# Модуль stubs

## Обзор

Модуль `stubs` содержит определения классов, используемых для представления структур данных, возвращаемых API gpt4free.
Он включает в себя модели для представления токенов, использования моделей, вызовов инструментов, сообщений чата, выбора завершения чата и ответов изображений.

## Подробнее

Этот модуль определяет структуры данных, используемые для взаимодействия с API gpt4free. Он содержит классы для представления различных типов данных, таких как информация об использовании токенов, вызовы инструментов, сообщения чата и ответы изображений. Модуль также включает вспомогательные функции для создания экземпляров моделей и фильтрации значений None.

## Классы

### `BaseModel`

**Описание**: Базовый класс для моделей данных, используемый для представления структур данных.

**Принцип работы**:
- Если `pydantic` не установлен, предоставляет базовую реализацию для `model_construct`.
- В противном случае, наследуется от `pydantic.BaseModel` и расширяет функциональность `model_construct`.

**Методы**:
- `model_construct(**data)`: Создает экземпляр класса, инициализируя атрибуты данными из словаря `data`.

### `TokenDetails`

**Описание**: Модель данных, представляющая детали токенов.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `cached_tokens` (int): Количество кэшированных токенов.

### `UsageModel`

**Описание**: Модель данных, представляющая информацию об использовании модели.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `prompt_tokens` (int): Количество токенов в запросе.
- `completion_tokens` (int): Количество токенов в ответе.
- `total_tokens` (int): Общее количество токенов.
- `prompt_tokens_details` (TokenDetails): Детали токенов в запросе.
- `completion_tokens_details` (TokenDetails): Детали токенов в ответе.

**Методы**:
- `model_construct(prompt_tokens: int = 0, completion_tokens: int = 0, total_tokens: int = 0, prompt_tokens_details: TokenDetails = None, completion_tokens_details: TokenDetails = None, **kwargs)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

### `ToolFunctionModel`

**Описание**: Модель данных, представляющая функцию инструмента.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `name` (str): Имя функции.
- `arguments` (str): Аргументы функции.

### `ToolCallModel`

**Описание**: Модель данных, представляющая вызов инструмента.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `id` (str): Идентификатор вызова инструмента.
- `type` (str): Тип вызова инструмента.
- `function` (ToolFunctionModel): Функция инструмента.

**Методы**:
- `model_construct(function: ToolFunctionModel = None, **kwargs)`: Создает экземпляр класса, инициализируя атрибут `function` моделью `ToolFunctionModel`, если она предоставлена.

### `ChatCompletionChunk`

**Описание**: Модель данных, представляющая чанк завершения чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `id` (str): Идентификатор чанка.
- `object` (str): Тип объекта.
- `created` (int): Время создания чанка.
- `model` (str): Модель, используемая для создания чанка.
- `provider` (Optional[str]): Провайдер модели.
- `choices` (List[ChatCompletionDeltaChoice]): Список вариантов выбора чанка.
- `usage` (UsageModel): Информация об использовании модели.

**Методы**:
- `model_construct(content: str, finish_reason: str, completion_id: str = None, created: int = None, usage: UsageModel = None)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

### `ChatCompletionMessage`

**Описание**: Модель данных, представляющая сообщение завершения чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `role` (str): Роль сообщения.
- `content` (str): Содержание сообщения.
- `tool_calls` (list[ToolCallModel]): Список вызовов инструментов.

**Методы**:
- `model_construct(content: str, tool_calls: list = None)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.
- `save(self, filepath: str, allowd_types = None)`: Сохраняет содержимое сообщения в файл.

### `ChatCompletionChoice`

**Описание**: Модель данных, представляющая выбор завершения чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `index` (int): Индекс выбора.
- `message` (ChatCompletionMessage): Сообщение выбора.
- `finish_reason` (str): Причина завершения.

**Методы**:
- `model_construct(message: ChatCompletionMessage, finish_reason: str)`: Создает экземпляр класса, инициализируя атрибуты значениями, если они предоставлены.

### `ChatCompletion`

**Описание**: Модель данных, представляющая завершение чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `id` (str): Идентификатор завершения.
- `object` (str): Тип объекта.
- `created` (int): Время создания завершения.
- `model` (str): Модель, используемая для создания завершения.
- `provider` (Optional[str]): Провайдер модели.
- `choices` (list[ChatCompletionChoice]): Список вариантов выбора завершения.
- `usage` (UsageModel): Информация об использовании модели.
- `conversation` (dict): Контекст диалога.

**Методы**:
- `model_construct(content: str, finish_reason: str, completion_id: str = None, created: int = None, tool_calls: list[ToolCallModel] = None, usage: UsageModel = None, conversation: dict = None)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

### `ChatCompletionDelta`

**Описание**: Модель данных, представляющая дельту завершения чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `role` (str): Роль дельты.
- `content` (str): Содержание дельты.

**Методы**:
- `model_construct(content: Optional[str])`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

### `ChatCompletionDeltaChoice`

**Описание**: Модель данных, представляющая выбор дельты завершения чата.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `index` (int): Индекс выбора.
- `delta` (ChatCompletionDelta): Дельта выбора.
- `finish_reason` (Optional[str]): Причина завершения.

**Методы**:
- `model_construct(delta: ChatCompletionDelta, finish_reason: Optional[str])`: Создает экземпляр класса, инициализируя атрибуты значениями, если они предоставлены.

### `Image`

**Описание**: Модель данных, представляющая изображение.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `url` (Optional[str]): URL изображения.
- `b64_json` (Optional[str]): Изображение в формате base64 JSON.
- `revised_prompt` (Optional[str]): Пересмотренный запрос.

**Методы**:
- `model_construct(url: str = None, b64_json: str = None, revised_prompt: str = None)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

### `ImagesResponse`

**Описание**: Модель данных, представляющая ответ изображений.

**Наследует**:
- `BaseModel`

**Атрибуты**:
- `data` (List[Image]): Список изображений.
- `model` (str): Модель, используемая для создания изображений.
- `provider` (str): Провайдер модели.
- `created` (int): Время создания изображений.

**Методы**:
- `model_construct(data: List[Image], created: int = None, model: str = None, provider: str = None)`: Создает экземпляр класса, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

## Функции

### `BaseModel.model_construct`

```python
@classmethod
def model_construct(cls, **data)
```

**Назначение**: Создает экземпляр класса, инициализируя атрибуты данными из словаря `data`.

**Параметры**:
- `cls`: Класс, для которого создается экземпляр.
- `data` (dict): Словарь, содержащий данные для инициализации атрибутов класса.

**Возвращает**:
- Экземпляр класса.

**Как работает функция**:

1. Функция проверяет, установлен ли `pydantic`. Если нет, она предоставляет базовую реализацию для создания экземпляра класса и инициализации его атрибутов данными из словаря `data`.
2. Если `pydantic` установлен, функция наследуется от `pydantic.BaseModel` и расширяет функциональность `model_construct`.
3.  Функция проходит по всем элементам в `data`
4.  Для каждого элемента устанавливает переданное значение как значение атрибута класса

**Примеры**:

```python
class MyClass(BaseModel):
    name: str
    age: int

# Пример создания экземпляра класса с использованием model_construct
instance = MyClass.model_construct(name="John", age=30)
print(instance.name)  # John
print(instance.age)   # 30
```

### `UsageModel.model_construct`

```python
@classmethod
def model_construct(cls, prompt_tokens=0, completion_tokens=0, total_tokens=0, prompt_tokens_details=None, completion_tokens_details=None, **kwargs)
```

**Назначение**: Создает экземпляр класса `UsageModel`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `prompt_tokens` (int): Количество токенов в запросе. По умолчанию 0.
- `completion_tokens` (int): Количество токенов в ответе. По умолчанию 0.
- `total_tokens` (int): Общее количество токенов. По умолчанию 0.
- `prompt_tokens_details` (TokenDetails): Детали токенов в запросе. По умолчанию `None`.
- `completion_tokens_details` (TokenDetails): Детали токенов в ответе. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- Экземпляр класса `UsageModel`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются значения параметров, а также создаются экземпляры `TokenDetails` для `prompt_tokens_details` и `completion_tokens_details`, если они не были переданы. Если `prompt_tokens_details` или `completion_tokens_details` равны `None`, то создаются экземпляры `TokenDetails` с `cached_tokens=0`.
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `UsageModel`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
usage = UsageModel.model_construct(prompt_tokens=10, completion_tokens=20, total_tokens=30)
print(usage.prompt_tokens)    # 10
print(usage.completion_tokens) # 20
print(usage.total_tokens)      # 30

usage_with_details = UsageModel.model_construct(
    prompt_tokens=10,
    completion_tokens=20,
    total_tokens=30,
    prompt_tokens_details={"cached_tokens": 5},
    completion_tokens_details={"cached_tokens": 10}
)
print(usage_with_details.prompt_tokens_details.cached_tokens)    # 5
print(usage_with_details.completion_tokens_details.cached_tokens) # 10
```

### `ToolCallModel.model_construct`

```python
@classmethod
def model_construct(cls, function=None, **kwargs)
```

**Назначение**: Создает экземпляр класса `ToolCallModel`, инициализируя атрибут `function` моделью `ToolFunctionModel`, если она предоставлена.

**Параметры**:
- `function` (ToolFunctionModel): Функция инструмента. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- Экземпляр класса `ToolCallModel`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются дополнительные аргументы `kwargs`, а также создается экземпляр `ToolFunctionModel` для атрибута `function`, если он был передан. Если `function` равен `None`, то используется `ToolFunctionModel.model_construct(**function)`.
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ToolCallModel`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
tool_call = ToolCallModel.model_construct(
    id="tool_id",
    type="tool_type",
    function={"name": "tool_name", "arguments": "tool_args"}
)
print(tool_call.id)                # tool_id
print(tool_call.type)              # tool_type
print(tool_call.function.name)     # tool_name
print(tool_call.function.arguments)  # tool_args
```

### `ChatCompletionChunk.model_construct`

```python
@classmethod
def model_construct(cls, content: str, finish_reason: str, completion_id: str = None, created: int = None, usage: UsageModel = None)
```

**Назначение**: Создает экземпляр класса `ChatCompletionChunk`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `content` (str): Содержание чанка.
- `finish_reason` (str): Причина завершения.
- `completion_id` (str): Идентификатор завершения. По умолчанию `None`.
- `created` (int): Время создания чанка. По умолчанию `None`.
- `usage` (UsageModel): Информация об использовании модели. По умолчанию `None`.

**Возвращает**:
- Экземпляр класса `ChatCompletionChunk`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются идентификатор, тип объекта, время создания и модель (если они были переданы), а также создается список `ChatCompletionDeltaChoice` с экземпляром `ChatCompletionDelta` и причиной завершения.
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletionChunk`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
chunk = ChatCompletionChunk.model_construct(
    content="chunk content",
    finish_reason="stop",
    completion_id="completion_id",
    created=1678901234,
    usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
)
print(chunk.id)                     # chatcmpl-completion_id
print(chunk.object)                 # chat.completion.cunk
print(chunk.created)                # 1678901234
print(chunk.choices[0].delta.content) # chunk content
print(chunk.choices[0].finish_reason) # stop
print(chunk.usage.prompt_tokens)       # 10
```

### `ChatCompletionMessage.model_construct`

```python
@classmethod
def model_construct(cls, content: str, tool_calls: list = None)
```

**Назначение**: Создает экземпляр класса `ChatCompletionMessage`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `content` (str): Содержание сообщения.
- `tool_calls` (list): Список вызовов инструментов. По умолчанию `None`.

**Возвращает**:
- Экземпляр класса `ChatCompletionMessage`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передается роль "assistant", содержание сообщения и список вызовов инструментов (если он был передан).
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletionMessage`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
message = ChatCompletionMessage.model_construct(
    content="message content",
    tool_calls=[{"id": "tool_id", "type": "tool_type", "function": {"name": "tool_name", "arguments": "tool_args"}}]
)
print(message.role)      # assistant
print(message.content)   # message content
print(message.tool_calls[0].id) # tool_id
```

### `ChatCompletionChoice.model_construct`

```python
@classmethod
def model_construct(cls, message: ChatCompletionMessage, finish_reason: str)
```

**Назначение**: Создает экземпляр класса `ChatCompletionChoice`, инициализируя атрибуты значениями, если они предоставлены.

**Параметры**:
- `message` (ChatCompletionMessage): Сообщение выбора.
- `finish_reason` (str): Причина завершения.

**Возвращает**:
- Экземпляр класса `ChatCompletionChoice`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются индекс 0, сообщение выбора и причина завершения.
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletionChoice`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
message = ChatCompletionMessage.model_construct(content="message content")
choice = ChatCompletionChoice.model_construct(message=message, finish_reason="stop")
print(choice.index)            # 0
print(choice.message.content)  # message content
print(choice.finish_reason)    # stop
```

### `ChatCompletion.model_construct`

```python
@classmethod
def model_construct(cls, content: str, finish_reason: str, completion_id: str = None, created: int = None, tool_calls: list[ToolCallModel] = None, usage: UsageModel = None, conversation: dict = None)
```

**Назначение**: Создает экземпляр класса `ChatCompletion`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `content` (str): Содержание завершения.
- `finish_reason` (str): Причина завершения.
- `completion_id` (str): Идентификатор завершения. По умолчанию `None`.
- `created` (int): Время создания завершения. По умолчанию `None`.
- `tool_calls` (list[ToolCallModel]): Список вызовов инструментов. По умолчанию `None`.
- `usage` (UsageModel): Информация об использовании модели. По умолчанию `None`.
- `conversation` (dict): Контекст диалога. По умолчанию `None`.

**Возвращает**:
- Экземпляр класса `ChatCompletion`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются идентификатор, тип объекта, время создания и модель (если они были переданы), а также создается список `ChatCompletionChoice` с экземпляром `ChatCompletionMessage` и причиной завершения.
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletion`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
completion = ChatCompletion.model_construct(
    content="completion content",
    finish_reason="stop",
    completion_id="completion_id",
    created=1678901234,
    tool_calls=[{"id": "tool_id", "type": "tool_type", "function": {"name": "tool_name", "arguments": "tool_args"}}],
    usage={"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
    conversation={"key": "value"}
)
print(completion.id)                     # chatcmpl-completion_id
print(completion.object)                 # chat.completion
print(completion.created)                # 1678901234
print(completion.choices[0].message.content) # completion content
print(completion.choices[0].finish_reason) # stop
print(completion.usage.prompt_tokens)       # 10
print(completion.conversation["key"])      # value
```

### `ChatCompletionDelta.model_construct`

```python
@classmethod
def model_construct(cls, content: Optional[str])
```

**Назначение**: Создает экземпляр класса `ChatCompletionDelta`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `content` (Optional[str]): Содержание дельты.

**Возвращает**:
- Экземпляр класса `ChatCompletionDelta`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передается роль "assistant" и содержание дельты (если оно было передано).
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletionDelta`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
delta = ChatCompletionDelta.model_construct(content="delta content")
print(delta.role)     # assistant
print(delta.content)  # delta content
```

### `ChatCompletionDeltaChoice.model_construct`

```python
@classmethod
def model_construct(cls, delta: ChatCompletionDelta, finish_reason: Optional[str])
```

**Назначение**: Создает экземпляр класса `ChatCompletionDeltaChoice`, инициализируя атрибуты значениями, если они предоставлены.

**Параметры**:
- `delta` (ChatCompletionDelta): Дельта выбора.
- `finish_reason` (Optional[str]): Причина завершения.

**Возвращает**:
- Экземпляр класса `ChatCompletionDeltaChoice`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются индекс 0, дельта выбора и причина завершения (если она была передана).
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ChatCompletionDeltaChoice`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
delta = ChatCompletionDelta.model_construct(content="delta content")
choice = ChatCompletionDeltaChoice.model_construct(delta=delta, finish_reason="stop")
print(choice.index)       # 0
print(choice.delta.content) # delta content
print(choice.finish_reason) # stop
```

### `Image.model_construct`

```python
@classmethod
def model_construct(cls, url: str = None, b64_json: str = None, revised_prompt: str = None)
```

**Назначение**: Создает экземпляр класса `Image`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `url` (str): URL изображения. По умолчанию `None`.
- `b64_json` (str): Изображение в формате base64 JSON. По умолчанию `None`.
- `revised_prompt` (str): Пересмотренный запрос. По умолчанию `None`.

**Возвращает**:
- Экземпляр класса `Image`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. При вызове `model_construct` базового класса передаются URL, изображение в формате base64 JSON и пересмотренный запрос (если они были переданы).
3.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `Image`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
image = Image.model_construct(url="image url", b64_json="image base64", revised_prompt="revised prompt")
print(image.url)            # image url
print(image.b64_json)       # image base64
print(image.revised_prompt) # revised prompt
```

### `ImagesResponse.model_construct`

```python
@classmethod
def model_construct(cls, data: List[Image], created: int = None, model: str = None, provider: str = None)
```

**Назначение**: Создает экземпляр класса `ImagesResponse`, инициализируя атрибуты значениями по умолчанию, если они не предоставлены.

**Параметры**:
- `data` (List[Image]): Список изображений.
- `created` (int): Время создания изображений. По умолчанию `None`.
- `model` (str): Модель, используемая для создания изображений. По умолчанию `None`.
- `provider` (str): Провайдер модели. По умолчанию `None`.

**Возвращает**:
- Экземпляр класса `ImagesResponse`.

**Как работает функция**:

1. Функция вызывает метод `model_construct` базового класса (`super().model_construct`).
2. Если время создания `created` не указано, оно устанавливается равным текущему времени.
3. При вызове `model_construct` базового класса передаются список изображений, время создания, модель и провайдер (если они были переданы).
4.  Созданные или переданные значения присваиваются атрибутам экземпляра класса `ImagesResponse`.

**Примеры**:

```python
# Пример создания экземпляра класса с использованием model_construct
image = Image.model_construct(url="image url", b64_json="image base64", revised_prompt="revised prompt")
response = ImagesResponse.model_construct(data=[image], created=1678901234, model="image model", provider="image provider")
print(response.data[0].url)     # image url
print(response.created)        # 1678901234
print(response.model)          # image model
print(response.provider)       # image provider
```

## ASCII Flowcharts

### `BaseModel.model_construct`

```
  data (dict)
       ↓
  Инициализация экземпляра класса
       ↓
  Присвоение атрибутам значений из data
       ↓
  Экземпляр класса
```

### `UsageModel.model_construct`

```
  prompt_tokens, completion_tokens, total_tokens, prompt_tokens_details, completion_tokens_details
       ↓
  Создание экземпляров TokenDetails (если необходимо)
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра UsageModel
       ↓
  Экземпляр UsageModel
```

### `ToolCallModel.model_construct`

```
  function, kwargs
       ↓
  Создание экземпляра ToolFunctionModel (если необходимо)
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ToolCallModel
       ↓
  Экземпляр ToolCallModel
```

### `ChatCompletionChunk.model_construct`

```
  content, finish_reason, completion_id, created, usage
       ↓
  Создание экземпляра ChatCompletionDelta
       ↓
  Создание экземпляра ChatCompletionDeltaChoice
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletionChunk
       ↓
  Экземпляр ChatCompletionChunk
```

### `ChatCompletionMessage.model_construct`

```
  content, tool_calls
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletionMessage
       ↓
  Экземпляр ChatCompletionMessage
```

### `ChatCompletionChoice.model_construct`

```
  message, finish_reason
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletionChoice
       ↓
  Экземпляр ChatCompletionChoice
```

### `ChatCompletion.model_construct`

```
  content, finish_reason, completion_id, created, tool_calls, usage, conversation
       ↓
  Создание экземпляра ChatCompletionMessage
       ↓
  Создание экземпляра ChatCompletionChoice
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletion
       ↓
  Экземпляр ChatCompletion
```

### `ChatCompletionDelta.model_construct`

```
  content
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletionDelta
       ↓
  Экземпляр ChatCompletionDelta
```

### `ChatCompletionDeltaChoice.model_construct`

```
  delta, finish_reason
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ChatCompletionDeltaChoice
       ↓
  Экземпляр ChatCompletionDeltaChoice
```

### `Image.model_construct`

```
  url, b64_json, revised_prompt
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра Image
       ↓
  Экземпляр Image
```

### `ImagesResponse.model_construct`

```
  data, created, model, provider
       ↓
  Установка created в текущее время (если необходимо)
       ↓
  Вызов super().model_construct с параметрами
       ↓
  Инициализация экземпляра ImagesResponse
       ↓
  Экземпляр ImagesResponse