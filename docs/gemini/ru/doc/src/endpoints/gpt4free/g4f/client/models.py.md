# Модуль `models.py`

## Обзор

Модуль `models.py` предназначен для управления моделями, используемыми в клиентской части проекта `gpt4free`. Он предоставляет функциональность для получения, фильтрации и организации моделей, поддерживаемых различными провайдерами, включая модели для обработки текста, изображений и видео. Модуль содержит класс `ClientModels`, который агрегирует информацию о моделях и обеспечивает удобный интерфейс для доступа к ним.

## Подробнее

Модуль `models.py` играет важную роль в определении доступных моделей для использования в клиентской части проекта `gpt4free`. Он использует классы `ModelUtils`, `ImageModel`, `VisionModel`, `ProviderUtils` и `ProviderType` из других модулей для организации и фильтрации моделей. Класс `ClientModels` предоставляет методы для получения списка всех моделей, моделей для работы с изображениями и видео, а также для определения лучшего провайдера для конкретной модели.

## Классы

### `ClientModels`

**Описание**: Класс `ClientModels` управляет доступными моделями для различных провайдеров.

**Принцип работы**:
Класс инициализируется с клиентом и двумя провайдерами: `provider` для текстовых моделей и `media_provider` для моделей обработки медиа-контента (изображений и видео). Он предоставляет методы для получения моделей, поддерживаемых каждым провайдером, и фильтрации моделей на основе их типа (например, модели для работы с изображениями или видео).

**Аттрибуты**:
- `client`: Клиентский объект, используемый для выполнения запросов к провайдерам.
- `provider` (ProviderType): Провайдер для текстовых моделей.
- `media_provider` (ProviderType): Провайдер для моделей обработки медиа-контента.

**Методы**:
- `get(name, default)`: Возвращает провайдера для заданной модели или провайдера по умолчанию, если модель не найдена.
- `get_all(api_key, **kwargs)`: Возвращает список всех моделей, поддерживаемых провайдером.
- `get_vision(**kwargs)`: Возвращает список моделей, поддерживающих обработку изображений (vision models).
- `get_media(api_key, **kwargs)`: Возвращает список моделей для обработки медиа-контента, поддерживаемых медиа-провайдером.
- `get_image(**kwargs)`: Возвращает список моделей, поддерживающих работу с изображениями (image models).
- `get_video(**kwargs)`: Возвращает список моделей, поддерживающих работу с видео (video models).

## Функции

### `__init__`

```python
def __init__(self, client, provider: ProviderType = None, media_provider: ProviderType = None):
    """
    Инициализирует экземпляр класса `ClientModels`.

    Args:
        client: Клиентский объект, используемый для выполнения запросов к провайдерам.
        provider (ProviderType, optional): Провайдер для текстовых моделей. По умолчанию `None`.
        media_provider (ProviderType, optional): Провайдер для моделей обработки медиа-контента. По умолчанию `None`.
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `ClientModels` с указанием клиента и провайдеров.

**Параметры**:
- `client`: Клиентский объект, используемый для выполнения запросов к провайдерам.
- `provider` (ProviderType, optional): Провайдер для текстовых моделей. По умолчанию `None`.
- `media_provider` (ProviderType, optional): Провайдер для моделей обработки медиа-контента. По умолчанию `None`.

**Как работает функция**:
1. Функция принимает клиентский объект, провайдер для текстовых моделей и провайдер для моделей обработки медиа-контента.
2. Она присваивает переданные значения атрибутам `self.client`, `self.provider` и `self.media_provider` экземпляра класса.

```
ClientModels initialization
│
├── Assign client to self.client
│
├── Assign provider to self.provider
│
└── Assign media_provider to self.media_provider
```

**Примеры**:
```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

# Пример создания экземпляра класса ClientModels с указанием клиента и провайдеров
client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
provider = ProviderType() # <инструкция для модели gemini:Укажите текстового провайдера для инициализации класса ClientModels>
media_provider = ProviderType() # <инструкция для модели gemini:Укажите медиа-провайдера для инициализации класса ClientModels>
client_models = ClientModels(client, provider, media_provider)
```

### `get`

```python
def get(self, name, default=None) -> ProviderType:
    """
    Возвращает провайдера для заданной модели.

    Args:
        name: Имя модели.
        default: Значение по умолчанию, если модель не найдена.

    Returns:
        ProviderType: Провайдер для заданной модели или значение по умолчанию.
    """
    ...
```

**Назначение**: Возвращает провайдера для заданной модели или значение по умолчанию, если модель не найдена.

**Параметры**:
- `name`: Имя модели.
- `default`: Значение по умолчанию, если модель не найдена.

**Возвращает**:
- `ProviderType`: Провайдер для заданной модели или значение по умолчанию.

**Как работает функция**:
1. Функция проверяет, есть ли модель с указанным именем в словаре `ModelUtils.convert`.
2. Если модель найдена, функция возвращает лучшего провайдера для этой модели.
3. Если модель не найдена в `ModelUtils.convert`, функция проверяет, есть ли модель в словаре `ProviderUtils.convert`.
4. Если модель найдена в `ProviderUtils.convert`, функция возвращает соответствующего провайдера.
5. Если модель не найдена ни в одном из словарей, функция возвращает значение по умолчанию.

```
Get provider
│
├── Check if model name in ModelUtils.convert
│   └── Return ModelUtils.convert[name].best_provider if found
│
├── Check if model name in ProviderUtils.convert
│   └── Return ProviderUtils.convert[name] if found
│
└── Return default value
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo']  # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client)
# Пример получения провайдера для модели "gpt-3.5-turbo"
provider = client_models.get("gpt-3.5-turbo")
print(provider)

# Пример получения провайдера для несуществующей модели с указанием значения по умолчанию
default_provider = client_models.get("non-existent-model", "default_provider")
print(default_provider)
```

### `get_all`

```python
def get_all(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Возвращает список всех моделей, поддерживаемых провайдером.

    Args:
        api_key (str, optional): API-ключ для провайдера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы для метода `get_models` провайдера.

    Returns:
        list[str]: Список всех моделей, поддерживаемых провайдером.
    """
    ...
```

**Назначение**: Возвращает список всех моделей, поддерживаемых провайдером.

**Параметры**:
- `api_key` (str, optional): API-ключ для провайдера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для метода `get_models` провайдера.

**Возвращает**:
- `list[str]`: Список всех моделей, поддерживаемых провайдером.

**Как работает функция**:
1. Функция проверяет, установлен ли провайдер. Если провайдер не установлен, возвращается пустой список.
2. Если `api_key` не передан, используется `api_key` клиента.
3. Функция вызывает метод `get_models` провайдера, передавая ему `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4. Возвращается список моделей, полученный от провайдера.

```
Get all models
│
├── Check if provider is None
│   └── Return empty list if provider is None
│
├── Check if api_key is None
│   └── Use client.api_key if api_key is None
│
└── Call provider.get_models with api_key and kwargs
    └── Return list of models
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client, ProviderUtils.convert['g4f.provider.GptGo'])
# Пример получения списка всех моделей без API-ключа
all_models = client_models.get_all()
print(all_models)

# Пример получения списка всех моделей с API-ключом
all_models_with_api_key = client_models.get_all(api_key="your_api_key") # <инструкция для модели gemini:Замените 'your_api_key' на фактический API ключ>
print(all_models_with_api_key)
```

### `get_vision`

```python
def get_vision(self, **kwargs) -> list[str]:
    """
    Возвращает список моделей, поддерживающих обработку изображений (vision models).

    Args:
        **kwargs: Дополнительные аргументы для метода `get_all` провайдера.

    Returns:
        list[str]: Список моделей, поддерживающих обработку изображений.
    """
    ...
```

**Назначение**: Возвращает список моделей, поддерживающих обработку изображений (vision models).

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_all` провайдера.

**Возвращает**:
- `list[str]`: Список моделей, поддерживающих обработку изображений.

**Как работает функция**:
1. Функция проверяет, установлен ли провайдер. Если провайдер не установлен, возвращается список `model_id` для каждой модели из `ModelUtils.convert.items()`, если модель является экземпляром класса `VisionModel`.
2. Если провайдер установлен, вызывается метод `get_all` для получения списка всех моделей.
3. Функция проверяет, есть ли у провайдера атрибут `vision_models`.
4. Если атрибут `vision_models` существует, функция возвращает значение этого атрибута.
5. Если атрибут `vision_models` не существует, функция возвращает пустой список.

```
Get vision models
│
├── Check if provider is None
│   └── Return list of VisionModel from ModelUtils.convert if provider is None
│
├── Call get_all with kwargs
│
├── Check if provider has attribute vision_models
│   └── Return provider.vision_models if attribute exists
│
└── Return empty list
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client, ProviderUtils.convert['g4f.provider.GptGo'])
# Пример получения списка vision моделей
vision_models = client_models.get_vision()
print(vision_models)
```

### `get_media`

```python
def get_media(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Возвращает список моделей для обработки медиа-контента, поддерживаемых медиа-провайдером.

    Args:
        api_key (str, optional): API-ключ для медиа-провайдера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы для метода `get_models` медиа-провайдера.

    Returns:
        list[str]: Список моделей для обработки медиа-контента, поддерживаемых медиа-провайдером.
    """
    ...
```

**Назначение**: Возвращает список моделей для обработки медиа-контента, поддерживаемых медиа-провайдером.

**Параметры**:
- `api_key` (str, optional): API-ключ для медиа-провайдера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для метода `get_models` медиа-провайдера.

**Возвращает**:
- `list[str]`: Список моделей для обработки медиа-контента, поддерживаемых медиа-провайдером.

**Как работает функция**:
1. Функция проверяет, установлен ли медиа-провайдер. Если медиа-провайдер не установлен, возвращается пустой список.
2. Если `api_key` не передан, используется `api_key` клиента.
3. Функция вызывает метод `get_models` медиа-провайдера, передавая ему `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4. Возвращается список моделей, полученный от медиа-провайдера.

```
Get media models
│
├── Check if media_provider is None
│   └── Return empty list if media_provider is None
│
├── Check if api_key is None
│   └── Use client.api_key if api_key is None
│
└── Call media_provider.get_models with api_key and kwargs
    └── Return list of media models
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client, media_provider=ProviderUtils.convert['g4f.provider.GptGo']) # <инструкция для модели gemini:Укажите медиа-провайдера для инициализации класса ClientModels>

# Пример получения списка media моделей без API-ключа
media_models = client_models.get_media()
print(media_models)

# Пример получения списка media моделей с API-ключом
media_models_with_api_key = client_models.get_media(api_key="your_api_key") # <инструкция для модели gemini:Замените 'your_api_key' на фактический API ключ>
print(media_models_with_api_key)
```

### `get_image`

```python
def get_image(self, **kwargs) -> list[str]:
    """
    Возвращает список моделей, поддерживающих работу с изображениями (image models).

    Args:
        **kwargs: Дополнительные аргументы для метода `get_media`.

    Returns:
        list[str]: Список моделей, поддерживающих работу с изображениями.
    """
    ...
```

**Назначение**: Возвращает список моделей, поддерживающих работу с изображениями (image models).

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_media`.

**Возвращает**:
- `list[str]`: Список моделей, поддерживающих работу с изображениями.

**Как работает функция**:
1. Функция проверяет, установлен ли медиа-провайдер. Если медиа-провайдер не установлен, возвращается список `model_id` для каждой модели из `ModelUtils.convert.items()`, если модель является экземпляром класса `ImageModel`.
2. Если медиа-провайдер установлен, вызывается метод `get_media` для получения списка моделей для обработки медиа-контента.
3. Функция проверяет, есть ли у медиа-провайдера атрибут `image_models`.
4. Если атрибут `image_models` существует, функция возвращает значение этого атрибута.
5. Если атрибут `image_models` не существует, функция возвращает пустой список.

```
Get image models
│
├── Check if media_provider is None
│   └── Return list of ImageModel from ModelUtils.convert if media_provider is None
│
├── Call get_media with kwargs
│
├── Check if media_provider has attribute image_models
│   └── Return media_provider.image_models if attribute exists
│
└── Return empty list
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client, media_provider=ProviderUtils.convert['g4f.provider.GptGo']) # <инструкция для модели gemini:Укажите медиа-провайдера для инициализации класса ClientModels>

# Пример получения списка image моделей
image_models = client_models.get_image()
print(image_models)
```

### `get_video`

```python
def get_video(self, **kwargs) -> list[str]:
    """
    Возвращает список моделей, поддерживающих работу с видео (video models).

    Args:
        **kwargs: Дополнительные аргументы для метода `get_media`.

    Returns:
        list[str]: Список моделей, поддерживающих работу с видео.
    """
    ...
```

**Назначение**: Возвращает список моделей, поддерживающих работу с видео (video models).

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_media`.

**Возвращает**:
- `list[str]`: Список моделей, поддерживающих работу с видео.

**Как работает функция**:
1. Функция проверяет, установлен ли медиа-провайдер. Если медиа-провайдер не установлен, возвращается пустой список.
2. Если медиа-провайдер установлен, вызывается метод `get_media` для получения списка моделей для обработки медиа-контента.
3. Функция проверяет, есть ли у медиа-провайдера атрибут `video_models`.
4. Если атрибут `video_models` существует, функция возвращает значение этого атрибута.
5. Если атрибут `video_models` не существует, функция возвращает пустой список.

```
Get video models
│
├── Check if media_provider is None
│   └── Return empty list if media_provider is None
│
├── Call get_media with kwargs
│
├── Check if media_provider has attribute video_models
│   └── Return media_provider.video_models if attribute exists
│
└── Return empty list
```

**Примеры**:
```python
from ..Provider import ProviderUtils

client = ProviderUtils.convert['g4f.provider.GptGo'] # <инструкция для модели gemini:Укажите клиента для инициализации класса ClientModels>
client_models = ClientModels(client, media_provider=ProviderUtils.convert['g4f.provider.GptGo']) # <инструкция для модели gemini:Укажите медиа-провайдера для инициализации класса ClientModels>

# Пример получения списка video моделей
video_models = client_models.get_video()
print(video_models)