# Модуль stubs
## Обзор

Модуль `stubs` содержит определения классов, используемых для представления структур данных, возвращаемых API g4f. Он включает модели для работы с токенами, информацией об использовании, вызовами инструментов, чат-завершениями, дельтами чат-завершений, изображениями и ответами на запросы изображений. Модуль предоставляет статические методы `model_construct` для удобного создания экземпляров моделей с параметрами по умолчанию и фильтрацией `None` значений.

## Подробнее

Этот модуль предоставляет классы, необходимые для работы с данными, возвращаемыми API g4f. Он включает модели для различных аспектов взаимодействия с API, таких как управление токенами, отслеживание использования, вызовы инструментов и создание чат-завершений. Модуль также включает модели для работы с изображениями и ответами на запросы изображений.

Модуль использует библиотеку `pydantic` для определения моделей данных. Если `pydantic` не установлен, используется базовый класс `BaseModel` с минимальной функциональностью.
Все классы моделей наследуются от `BaseModel` и предоставляют статические методы `model_construct` для удобного создания экземпляров моделей с параметрами по умолчанию и фильтрацией `None` значений.

## Классы

### `BaseModel`
**Описание**: Базовый класс для всех моделей данных. Если `pydantic` не установлен, используется упрощенная реализация `BaseModel`.

**Методы**:
- `model_construct(**data)`: Создает экземпляр класса, устанавливая атрибуты из переданного словаря `data`.

### `TokenDetails`
**Описание**: Модель для хранения информации о токенах.
**Атрибуты**:
- `cached_tokens` (int): Количество кэшированных токенов.

### `UsageModel`
**Описание**: Модель для хранения информации об использовании токенов.

**Атрибуты**:
- `prompt_tokens` (int): Количество токенов, использованных в запросе.
- `completion_tokens` (int): Количество токенов, использованных в ответе.
- `total_tokens` (int): Общее количество использованных токенов.
- `prompt_tokens_details` (TokenDetails): Детализация токенов, использованных в запросе.
- `completion_tokens_details` (TokenDetails): Детализация токенов, использованных в ответе.

**Методы**:
- `model_construct(prompt_tokens=0, completion_tokens=0, total_tokens=0, prompt_tokens_details=None, completion_tokens_details=None, **kwargs)`: Создает экземпляр класса с параметрами по умолчанию.

### `ToolFunctionModel`
**Описание**: Модель для хранения информации о функции инструмента.

**Атрибуты**:
- `name` (str): Имя функции инструмента.
- `arguments` (str): Аргументы функции инструмента.

### `ToolCallModel`
**Описание**: Модель для хранения информации о вызове инструмента.

**Атрибуты**:
- `id` (str): Идентификатор вызова инструмента.
- `type` (str): Тип вызова инструмента.
- `function` (ToolFunctionModel): Информация о функции инструмента.

**Методы**:
- `model_construct(function=None, **kwargs)`: Создает экземпляр класса с параметрами по умолчанию.

### `ChatCompletionChunk`
**Описание**: Модель для представления частичного ответа чат-завершения.

**Атрибуты**:
- `id` (str): Идентификатор чат-завершения.
- `object` (str): Тип объекта.
- `created` (int): Время создания.
- `model` (str): Используемая модель.
- `provider` (Optional[str])`: Поставщик модели.
- `choices` (List[ChatCompletionDeltaChoice]): Список вариантов дельты чат-завершения.
- `usage` (UsageModel): Информация об использовании токенов.

**Методы**:
- `model_construct(content: str, finish_reason: str, completion_id: str = None, created: int = None, usage: UsageModel = None)`: Создает экземпляр класса с параметрами по умолчанию.

### `ChatCompletionMessage`
**Описание**: Модель для представления сообщения чат-завершения.

**Атрибуты**:
- `role` (str): Роль сообщения (например, "assistant").
- `content` (str): Содержимое сообщения.
- `tool_calls` (list[ToolCallModel]): Список вызовов инструментов.

**Методы**:
- `model_construct(content: str, tool_calls: list = None)`: Создает экземпляр класса с параметрами по умолчанию.
- `save(self, filepath: str, allowd_types = None)`: Сохраняет содержимое сообщения в файл.

### `ChatCompletionChoice`
**Описание**: Модель для представления варианта ответа чат-завершения.

**Атрибуты**:
- `index` (int): Индекс варианта.
- `message` (ChatCompletionMessage): Сообщение чат-завершения.
- `finish_reason` (str): Причина завершения.

**Методы**:
- `model_construct(message: ChatCompletionMessage, finish_reason: str)`: Создает экземпляр класса с параметрами по умолчанию.

### `ChatCompletion`
**Описание**: Модель для представления ответа чат-завершения.

**Атрибуты**:
- `id` (str): Идентификатор чат-завершения.
- `object` (str): Тип объекта.
- `created` (int): Время создания.
- `model` (str): Используемая модель.
- `provider` (Optional[str])`: Поставщик модели.
- `choices` (list[ChatCompletionChoice]): Список вариантов ответа чат-завершения.
- `usage` (UsageModel): Информация об использовании токенов.
- `conversation` (dict): Информация о контексте диалога.

**Методы**:
- `model_construct(content: str, finish_reason: str, completion_id: str = None, created: int = None, tool_calls: list[ToolCallModel] = None, usage: UsageModel = None, conversation: dict = None)`: Создает экземпляр класса с параметрами по умолчанию.

### `ChatCompletionDelta`
**Описание**: Модель для представления дельты чат-завершения.

**Атрибуты**:
- `role` (str): Роль дельты (например, "assistant").
- `content` (str): Содержимое дельты.

**Методы**:
- `model_construct(content: Optional[str])`: Создает экземпляр класса с параметрами по умолчанию.

### `ChatCompletionDeltaChoice`
**Описание**: Модель для представления варианта дельты чат-завершения.

**Атрибуты**:
- `index` (int): Индекс варианта.
- `delta` (ChatCompletionDelta): Дельта чат-завершения.
- `finish_reason` (Optional[str])`: Причина завершения.

**Методы**:
- `model_construct(delta: ChatCompletionDelta, finish_reason: Optional[str])`: Создает экземпляр класса с параметрами по умолчанию.

### `Image`
**Описание**: Модель для представления изображения.

**Атрибуты**:
- `url` (Optional[str])`: URL изображения.
- `b64_json` (Optional[str])`: Изображение в формате base64.
- `revised_prompt` (Optional[str])`: Уточненный запрос.

**Методы**:
- `model_construct(url: str = None, b64_json: str = None, revised_prompt: str = None)`: Создает экземпляр класса с параметрами по умолчанию.

### `ImagesResponse`
**Описание**: Модель для представления ответа на запрос изображений.

**Атрибуты**:
- `data` (List[Image]): Список изображений.
- `model` (str): Используемая модель.
- `provider` (str): Поставщик модели.
- `created` (int): Время создания.

**Методы**:
- `model_construct(data: List[Image], created: int = None, model: str = None, provider: str = None)`: Создает экземпляр класса с параметрами по умолчанию.

## Функции

### `filter_none`
Функция `filter_none` импортируется из `g4f.client.helper`.

### `filter_markdown`
Функция `filter_markdown` импортируется из `g4f.client.helper`.

### `extract_data_uri`
Функция `extract_data_uri` импортируется из `g4f.image`.

### `images_dir`
Переменная `images_dir` импортируется из `g4f.image.copy_images`.

### `model_construct`
**Назначение**: Создание экземпляра класса модели с использованием переданных аргументов и фильтрацией `None` значений.

**Как работает функция**:

1.  **Вызов родительского метода `model_construct`**:
    - Вызывается метод `model_construct` родительского класса (если он существует).

2.  **Обработка аргументов**:
    - Аргументы, переданные в функцию, используются для создания экземпляра класса модели.
    - Функция фильтрует значения `None`, чтобы исключить их из атрибутов модели.

3.  **Создание и возврат экземпляра модели**:
    - Возвращается созданный экземпляр класса модели.

**Примеры**:

```python
usage_model = UsageModel.model_construct(prompt_tokens=10, completion_tokens=5)
print(usage_model.prompt_tokens)
print(usage_model.completion_tokens)
print(usage_model.total_tokens)

chat_completion = ChatCompletion.model_construct(content="Привет!", finish_reason="stop")
print(chat_completion.choices[0].message.content)
print(chat_completion.choices[0].finish_reason)
```