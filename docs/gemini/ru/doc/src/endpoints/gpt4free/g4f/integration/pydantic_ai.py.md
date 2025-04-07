# Модуль интеграции pydantic-ai с g4f
## Обзор

Модуль предоставляет интеграцию между библиотекой `pydantic-ai` и API `g4f` (gpt4free). Он позволяет использовать модели `g4f` в качестве AI-моделей в `pydantic-ai`. Модуль включает класс `AIModel`, который расширяет `OpenAIModel` из `pydantic-ai` и реализует логику взаимодействия с API `g4f`. Также модуль содержит функции для расширения функциональности `infer_model` из `pydantic-ai`, чтобы можно было использовать модели `g4f`.

## Подробней

Этот модуль позволяет использовать различные языковые модели, предоставляемые через `g4f`, в приложениях, использующих `pydantic-ai`. Это достигается путем создания класса `AIModel`, который адаптирует интерфейс `g4f` к требованиям `pydantic-ai`. Также модуль содержит функции `new_infer_model` и `patch_infer_model` для расширения функциональности `pydantic-ai` и обеспечения возможности использования моделей `g4f`.

## Классы

### `AIModel`

**Описание**: Класс `AIModel` представляет собой модель, которая использует API `g4f`. Он наследуется от `OpenAIModel` и предоставляет необходимые методы и атрибуты для взаимодействия с API `g4f`.

**Наследует**:
- `OpenAIModel`: Класс, предоставляющий базовую функциональность для моделей OpenAI в `pydantic-ai`.

**Атрибуты**:
- `client` (AsyncClient): Асинхронный клиент для взаимодействия с API `g4f`.
- `system_prompt_role` (OpenAISystemPromptRole | None): Роль, используемая для системного промпта.
- `_model_name` (str): Название используемой модели.
- `_provider` (str): Провайдер модели.
- `_system` (Optional[str]): Используемая система, по умолчанию 'openai'.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AIModel`.
- `name`: Возвращает название модели.

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
) -> None:
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
```

**Назначение**: Инициализирует объект `AIModel`.

**Параметры**:
- `model_name` (str): Название AI-модели для использования.
- `provider` (Optional[str]): Провайдер модели.
- `system_prompt_role` (Optional[OpenAISystemPromptRole]): Роль для системного промпта. По умолчанию `None`.
- `system` (Optional[str]): Используемая система, по умолчанию 'openai'.
- `**kwargs`: Дополнительные аргументы, передаваемые в `AsyncClient`.

**Как работает функция**:
1. Сохраняет имя модели `model_name` в атрибуте `_model_name`.
2. Сохраняет имя провайдера `provider` в атрибуте `_provider`.
3. Инициализирует асинхронный клиент `AsyncClient` с указанным провайдером и дополнительными аргументами.
4. Устанавливает роль системного промпта `system_prompt_role`.
5. Устанавливает используемую систему `system`.

```ascii
    model_name, provider, system_prompt_role, system, kwargs
    │
    │ Сохранение параметров
    ↓
    _model_name = model_name, _provider = provider, system_prompt_role = system_prompt_role
    │
    │ Инициализация AsyncClient
    ↓
    client = AsyncClient(provider=provider, **kwargs)
```

**Примеры**:

```python
from pydantic_ai.models.openai import OpenAISystemPromptRole

# Пример инициализации с указанием имени модели и провайдера
model = AIModel(model_name="gpt-3.5-turbo", provider="openai")

# Пример инициализации с указанием роли системного промпта
model = AIModel(model_name="gpt-4", provider="openai", system_prompt_role=OpenAISystemPromptRole.user)
```

#### `name`

```python
def name(self) -> str:
    """ """
```

**Назначение**: Возвращает название модели.

**Возвращает**:
- `str`: Название модели в формате `g4f:{provider}:{model_name}` или `g4f:{model_name}`, если провайдер не указан.

**Как работает функция**:
1. Проверяет, указан ли провайдер `self._provider`.
2. Если провайдер указан, формирует строку с названием модели в формате `g4f:{self._provider}:{self._model_name}`.
3. Если провайдер не указан, формирует строку с названием модели в формате `g4f:{self._model_name}`.
4. Возвращает сформированную строку.

```ascii
    self._provider, self._model_name
    │
    │ Проверка наличия провайдера
    ↓
    if self._provider:
        result = f'g4f:{self._provider}:{self._model_name}'
    else:
        result = f'g4f:{self._model_name}'
    │
    │ Возврат названия модели
    ↓
    return result
```

**Примеры**:

```python
# Пример получения названия модели с указанным провайдером
model = AIModel(model_name="gpt-3.5-turbo", provider="openai")
model_name = model.name()
print(model_name)  # Вывод: g4f:openai:gpt-3.5-turbo

# Пример получения названия модели без указания провайдера
model = AIModel(model_name="gpt-4")
model_name = model.name()
print(model_name)  # Вывод: g4f:gpt-4
```

## Функции

### `new_infer_model`

```python
def new_infer_model(model: Model | KnownModelName, api_key: str = None) -> Model:
    """ """
```

**Назначение**: Функция для определения типа модели. Если модель начинается с "g4f:", пытается создать экземпляр `AIModel`. В противном случае использует стандартную функцию `infer_model` из `pydantic-ai`.

**Параметры**:
- `model` (Model | KnownModelName): Модель или название известной модели.
- `api_key` (Optional[str]): Ключ API.

**Возвращает**:
- `Model`: Экземпляр класса `Model` или `AIModel`.

**Как работает функция**:
1. Проверяет, является ли входной параметр `model` экземпляром класса `Model`. Если да, возвращает его.
2. Проверяет, начинается ли название модели с префикса "g4f:".
3. Если название модели начинается с "g4f:", обрезает этот префикс.
4. Если в названии модели есть символ ":", разделяет название на провайдера и имя модели.
5. Создает экземпляр класса `AIModel` с указанным именем модели и провайдером (если он есть).
6. Если название модели не начинается с "g4f:", вызывает стандартную функцию `infer_model` из `pydantic-ai`.

```ascii
    model, api_key
    │
    │ Проверка типа модели
    ↓
    if isinstance(model, Model):
        return model
    │
    │ Проверка префикса "g4f:"
    ↓
    if model.startswith("g4f:"):
        model = model[4:]
        if ":" in model:
            provider, model = model.split(":", 1)
            return AIModel(model, provider=provider, api_key=api_key)
        return AIModel(model)
    │
    │ Использование стандартной infer_model
    ↓
    return infer_model(model)
```

**Примеры**:

```python
from pydantic_ai.models import Model, KnownModelName

# Пример использования с названием модели g4f
model = new_infer_model("g4f:gpt-3.5-turbo")
print(type(model))  # Вывод: <class '__main__.AIModel'>

# Пример использования с названием модели g4f и провайдером
model = new_infer_model("g4f:openai:gpt-4")
print(type(model))  # Вывод: <class '__main__.AIModel'>

# Пример использования со стандартной моделью
model = new_infer_model("gpt-3.5-turbo")
print(type(model))  # Вывод: <class 'pydantic_ai.models.openai.OpenAIModel'>
```

### `patch_infer_model`

```python
def patch_infer_model(api_key: str | None = None):
    """ """
```

**Назначение**: Функция для замены стандартной функции `infer_model` в модуле `pydantic_ai.models` на функцию `new_infer_model`. Это позволяет использовать модели `g4f` по умолчанию при вызове `infer_model`.

**Параметры**:
- `api_key` (Optional[str]): Ключ API.

**Как работает функция**:
1. Импортирует модуль `pydantic_ai.models`.
2. Заменяет функцию `pydantic_ai.models.infer_model` на `new_infer_model` с помощью `partial`, передавая `api_key`.
3. Заменяет класс `pydantic_ai.models.AIModel` на `AIModel` из текущего модуля.

```ascii
    api_key
    │
    │ Импорт модуля pydantic_ai.models
    ↓
    import pydantic_ai.models
    │
    │ Замена infer_model
    ↓
    pydantic_ai.models.infer_model = partial(new_infer_model, api_key=api_key)
    │
    │ Замена AIModel
    ↓
    pydantic_ai.models.AIModel = AIModel
```

**Примеры**:

```python
# Пример использования
patch_infer_model()

from pydantic_ai.models import infer_model

# Теперь infer_model будет использовать new_infer_model
model = infer_model("g4f:gpt-3.5-turbo")
print(type(model))  # Вывод: <class '__main__.AIModel'>

model = infer_model("gpt-3.5-turbo")
#Внимание! тут может быть ошибка, надо проверить
print(type(model))