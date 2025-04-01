# Модуль интеграции Pydantic AI с G4F
## Обзор

Модуль `pydantic_ai.py` предназначен для интеграции библиотеки `pydantic-ai` с API `g4f` (gpt4free). Он предоставляет класс `AIModel`, который расширяет возможности моделей OpenAI, позволяя использовать их через API `g4f`. Кроме того, модуль содержит функции для определения и патчинга моделей, чтобы они могли работать с `g4f`.

## Подробней

Этот модуль позволяет использовать модели OpenAI через API `g4f`, что может быть полезно для обхода ограничений OpenAI API или для использования альтернативных провайдеров моделей. Класс `AIModel` предоставляет интерфейс, совместимый с `pydantic-ai`, что упрощает интеграцию с существующим кодом, использующим `pydantic-ai`. Функции `new_infer_model` и `patch_infer_model` позволяют изменять поведение `pydantic-ai` для использования моделей `g4f`.

## Классы

### `AIModel`
**Описание**: Класс `AIModel` представляет собой модель, использующую API `g4f`. Он наследуется от `OpenAIModel` и предоставляет функциональность для взаимодействия с моделями через API `g4f`.

**Наследует**:
- `OpenAIModel`: Предоставляет базовую функциональность для работы с моделями OpenAI.

**Атрибуты**:
- `client` (`AsyncClient`): Асинхронный клиент для взаимодействия с API `g4f`.
- `system_prompt_role` (`OpenAISystemPromptRole | None`): Роль для системного промпта.
- `_model_name` (`str`): Название модели.
- `_provider` (`str`): Провайдер модели.
- `_system` (`Optional[str]`): Используемая система, по умолчанию 'openai'.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AIModel`.
- `name`: Возвращает имя модели.

### `__init__`

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

**Назначение**: Инициализирует объект `AIModel`.

**Параметры**:
- `model_name` (`str`): Имя используемой AI-модели.
- `provider` (`Optional[str]`, optional): Провайдер модели. По умолчанию `None`.
- `system_prompt_role` (`Optional[OpenAISystemPromptRole]`, optional): Роль для системного промпта. По умолчанию `None`.
- `system` (`Optional[str]`, optional): Используемая система, по умолчанию 'openai'.
- `**kwargs`: Дополнительные аргументы, передаваемые в `AsyncClient`.

**Как работает функция**:
1. Сохраняет имя модели `model_name` в атрибуте `_model_name`.
2. Сохраняет провайдера модели `provider` в атрибуте `_provider`.
3. Создает экземпляр `AsyncClient` с указанным провайдером и дополнительными аргументами и сохраняет его в атрибуте `client`.
4. Сохраняет роль системного промпта `system_prompt_role` в соответствующем атрибуте.
5. Сохраняет название системы в атрибуте `_system`.

```
    Сохранение имени модели --> Сохранение провайдера --> Создание AsyncClient --> Сохранение роли промпта --> Сохранение системы
```

**Примеры**:
```python
model = AIModel(model_name='gpt-3.5-turbo', provider='openai')
model = AIModel(model_name='gpt-4', provider='azure', system_prompt_role=OpenAISystemPromptRole.USER)
```

### `name`

```python
def name(self) -> str:
    """ """
    ...
```

**Назначение**: Возвращает имя модели в формате `g4f:{provider}:{model_name}` или `g4f:{model_name}`, если провайдер не указан.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:
1. Проверяет, указан ли провайдер модели (`self._provider`).
2. Если провайдер указан, возвращает имя в формате `g4f:{self._provider}:{self._model_name}`.
3. Если провайдер не указан, возвращает имя в формате `g4f:{self._model_name}`.

```
Проверка провайдера --> Формирование имени модели
```

**Примеры**:
```python
model = AIModel(model_name='gpt-3.5-turbo', provider='openai')
print(model.name())  # Вывод: g4f:openai:gpt-3.5-turbo

model = AIModel(model_name='gpt-4')
print(model.name())  # Вывод: g4f:gpt-4
```

## Функции

### `new_infer_model`

```python
def new_infer_model(model: Model | KnownModelName, api_key: str = None) -> Model:
    """ """
    ...
```

**Назначение**: Определяет модель на основе входных данных. Если модель начинается с "g4f:", создает экземпляр `AIModel`.

**Параметры**:
- `model` (`Model | KnownModelName`): Модель или имя известной модели.
- `api_key` (`Optional[str]`, optional): API-ключ. По умолчанию `None`.

**Возвращает**:
- `Model`: Экземпляр модели.

**Как работает функция**:
1. Проверяет, является ли `model` экземпляром класса `Model`. Если да, возвращает `model` без изменений.
2. Проверяет, начинается ли `model` со строки "g4f:".
3. Если `model` начинается с "g4f:", обрезает эту строку.
4. Проверяет, содержит ли `model` символ ":".
5. Если `model` содержит ":", разделяет строку на `provider` и `model`.
6. Создает и возвращает экземпляр `AIModel` с указанными `model` и `provider`.
7. Если `model` не содержит ":", создает и возвращает экземпляр `AIModel` только с указанным `model`.
8. Если `model` не начинается с "g4f:", вызывает функцию `infer_model` из `pydantic_ai.models` и возвращает результат.

```
Проверка типа Model --> Проверка префикса "g4f:" --> Разделение на провайдера и модель (если есть) --> Создание AIModel --> Вызов infer_model (если префикс отсутствует)
```

**Примеры**:
```python
model = new_infer_model(model='g4f:openai:gpt-3.5-turbo')
print(model)  # Вывод: AIModel(client=<...>, system_prompt_role=None, _model_name='gpt-3.5-turbo', _provider='openai', _system='openai')

model = new_infer_model(model='gpt-3.5-turbo')
print(model)  # Вывод: Instance of OpenAI chat model gpt-3.5-turbo
```

### `patch_infer_model`

```python
def patch_infer_model(api_key: str | None = None):
    """ """
    ...
```

**Назначение**: Заменяет функцию `infer_model` в модуле `pydantic_ai.models` на `new_infer_model` и устанавливает `AIModel` в `pydantic_ai.models.AIModel`.

**Параметры**:
- `api_key` (`Optional[str]`, optional): API-ключ. По умолчанию `None`.

**Как работает функция**:
1. Импортирует модуль `pydantic_ai.models`.
2. Заменяет функцию `pydantic_ai.models.infer_model` на `new_infer_model` с помощью `partial`, передавая `api_key`.
3. Устанавливает `pydantic_ai.models.AIModel` в класс `AIModel`.

```
Импорт модуля pydantic_ai.models --> Замена infer_model --> Установка AIModel
```

**Примеры**:
```python
patch_infer_model(api_key='test_api_key')