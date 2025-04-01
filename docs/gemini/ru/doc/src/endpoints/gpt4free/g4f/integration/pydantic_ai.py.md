# Документация модуля pydantic_ai.py

## Обзор

Модуль `pydantic_ai.py` предназначен для интеграции с API G4F (GPT4Free) и расширения функциональности `pydantic-ai`. Он предоставляет класс `AIModel`, который наследуется от `OpenAIModel` и позволяет использовать модели G4F для задач, связанных с искусственным интеллектом. Модуль также включает функции для определения и "патчинга" моделей, чтобы они могли работать с G4F API.

## Подробней

Этот модуль позволяет использовать различные AI-модели через API G4F, интегрируя их с библиотекой `pydantic-ai`. Это дает возможность определять модели, указывать провайдера и настраивать параметры для работы с AI-сервисами.
В файле определены инструменты, позволяющие расширить функциональность `pydantic-ai` для работы с моделями G4F, предоставляя удобный интерфейс для взаимодействия с ними.

## Классы

### `AIModel`

**Описание**: Класс `AIModel` представляет собой модель, использующую API G4F. Он наследуется от `OpenAIModel` и предназначен для работы с моделями OpenAI через G4F.

**Принцип работы**:
Класс инициализируется с именем модели, провайдером (необязательно) и другими параметрами. Он использует `AsyncClient` для выполнения запросов к API G4F.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `AIModel`.
- `name`: Возвращает имя модели, которое включает префикс "g4f", имя провайдера (если указан) и имя самой модели.

#### `__init__`

```python
def __init__(
    self,
    model_name: str,
    provider: str | None = None,
    *,
    system_prompt_role: OpenAISystemPromptRole | None = None,
    system: str | None = 'openai',
    **kwargs
):
    """Initialize an AI model.

    Args:
        model_name: The name of the AI model to use. List of model names available
            [here](https://github.com/openai/openai-python/blob/v1.54.3/src/openai/types/chat_model.py#L7)
            (Unfortunately, despite being ask to do so, OpenAI do not provide `.inv` files for their API).
        system_prompt_role: The role to use for the system prompt message. If not provided, defaults to `'system'`.
            In the future, this may be inferred from the model name.
        system: The model provider used, defaults to `openai`. This is for observability purposes, you must
            customize the `base_url` and `api_key` to use a different provider.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `AIModel`.

**Параметры**:
- `model_name` (str): Имя используемой AI-модели. Список доступных имен моделей можно найти [здесь](https://github.com/openai/openai-python/blob/v1.54.3/src/openai/types/chat_model.py#L7).
- `provider` (Optional[str], optional): Провайдер модели. По умолчанию `None`.
- `system_prompt_role` (Optional[OpenAISystemPromptRole], optional): Роль для системного запроса. Если не указана, по умолчанию используется `'system'`.
- `system` (Optional[str], optional): Провайдер модели. По умолчанию `'openai'`. Используется для целей наблюдаемости. Необходимо настроить `base_url` и `api_key` для использования другого провайдера.
- `**kwargs`: Дополнительные аргументы, передаваемые в `AsyncClient`.

**Как работает функция**:

1. Функция инициализирует модель AI с заданным именем и провайдером.
2. Создается экземпляр `AsyncClient` для взаимодействия с API G4F.
3. Устанавливается роль для системного запроса.
4. Настраивается система (провайдер) для целей наблюдаемости.

**Примеры**:
```python
model = AIModel(model_name='gpt-3.5-turbo', provider='openai')
```

#### `name`

```python
def name(self) -> str:
    """ """
    ...
```

**Описание**: Возвращает имя модели.

**Возвращает**:
- `str`: Имя модели в формате `g4f:<provider>:<model_name>` или `g4f:<model_name>`, если провайдер не указан.

**Как работает функция**:

1. Проверяет, указан ли провайдер.
2. Формирует имя модели в зависимости от наличия провайдера.

**Примеры**:
```python
model = AIModel(model_name='gpt-3.5-turbo', provider='openai')
print(model.name())  # Вывод: g4f:openai:gpt-3.5-turbo

model = AIModel(model_name='gpt-3.5-turbo')
print(model.name())  # Вывод: g4f:gpt-3.5-turbo
```

## Функции

### `new_infer_model`

```python
def new_infer_model(model: Model | KnownModelName, api_key: str = None) -> Model:
    """ """
    ...
```

**Описание**: Определяет модель на основе переданных аргументов. Если модель начинается с "g4f:", создается экземпляр `AIModel`.

**Параметры**:
- `model` (Model | KnownModelName): Модель или имя известной модели.
- `api_key` (str, optional): API-ключ. По умолчанию `None`.

**Возвращает**:
- `Model`: Экземпляр класса `AIModel` или результат функции `infer_model`.

**Как работает функция**:

1. Проверяет, является ли входной аргумент `model` экземпляром класса `Model`. Если да, возвращает его без изменений.
2. Проверяет, начинается ли имя модели с префикса "g4f:". Если да, обрезает префикс и создает экземпляр `AIModel` с соответствующими параметрами.
3. Если имя модели содержит разделитель ":", разделяет его на провайдера и имя модели.
4. Если имя модели не начинается с "g4f:", вызывает функцию `infer_model` для определения модели.

**Примеры**:
```python
model = new_infer_model(model='g4f:gpt-3.5-turbo', api_key='test_key')
print(model.name())  # Вывод: g4f:gpt-3.5-turbo

model = new_infer_model(model='g4f:openai:gpt-3.5-turbo', api_key='test_key')
print(model.name())  # Вывод: g4f:openai:gpt-3.5-turbo
```

### `patch_infer_model`

```python
def patch_infer_model(api_key: str | None = None):
    """ """
    ...
```

**Описание**: Заменяет функции `infer_model` и класс `AIModel` в модуле `pydantic_ai.models` на новые, чтобы использовать G4F API.

**Параметры**:
- `api_key` (Optional[str], optional): API-ключ. По умолчанию `None`.

**Как работает функция**:

1. Импортирует модуль `pydantic_ai.models`.
2. Заменяет функцию `pydantic_ai.models.infer_model` на `new_infer_model` с использованием `partial`, передавая `api_key`.
3. Заменяет класс `pydantic_ai.models.AIModel` на `AIModel` из текущего модуля.