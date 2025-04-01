# Модуль `models.py`

## Обзор

Модуль `models.py` предназначен для управления моделями, используемыми в клиентской части проекта. Он предоставляет класс `ClientModels`, который позволяет получать, фильтровать и управлять списком доступных моделей, включая текстовые, визуальные и мультимедийные модели.

## Подробнее

Этот модуль обеспечивает абстракцию над различными типами моделей и провайдерами, позволяя клиентскому коду легко взаимодействовать с ними без необходимости знать детали реализации каждого провайдера. Он использует `ModelUtils` и `ProviderUtils` для конвертации и получения информации о моделях и провайдерах.

## Классы

### `ClientModels`

**Описание**: Класс `ClientModels` управляет списком доступных моделей, предоставляя методы для получения моделей различных типов от разных провайдеров.

**Принцип работы**:
Класс инициализируется с клиентским объектом и опциональными провайдерами для текстовых и мультимедийных моделей. Он предоставляет методы для получения списка всех моделей, визуальных моделей, а также мультимедийных моделей (изображений и видео) от указанных провайдеров.

**Атрибуты**:
- `client`: Клиентский объект, используемый для выполнения запросов к API.
- `provider` (Optional[`ProviderType`]): Провайдер текстовых моделей. По умолчанию `None`.
- `media_provider` (Optional[`ProviderType`]): Провайдер мультимедийных моделей. По умолчанию `None`.

**Методы**:

- `__init__(self, client, provider: ProviderType = None, media_provider: ProviderType = None)`
- `get(self, name, default=None) -> ProviderType`
- `get_all(self, api_key: str = None, **kwargs) -> list[str]`
- `get_vision(self, **kwargs) -> list[str]`
- `get_media(self, api_key: str = None, **kwargs) -> list[str]`
- `get_image(self, **kwargs) -> list[str]`
- `get_video(self, **kwargs) -> list[str]`

## Функции

### `__init__`

```python
def __init__(self, client, provider: ProviderType = None, media_provider: ProviderType = None):
    """
    Инициализирует экземпляр класса `ClientModels`.

    Args:
        client: Клиентский объект, используемый для выполнения запросов к API.
        provider (Optional[ProviderType], optional): Провайдер текстовых моделей. По умолчанию `None`.
        media_provider (Optional[ProviderType], optional): Провайдер мультимедийных моделей. По умолчанию `None`.
    """
```

**Назначение**: Инициализирует объект `ClientModels` с указанным клиентом и провайдерами.

**Параметры**:
- `client`: Клиентский объект, используемый для выполнения запросов к API.
- `provider` (Optional[`ProviderType`]): Провайдер текстовых моделей. По умолчанию `None`.
- `media_provider` (Optional[`ProviderType`]): Провайдер мультимедийных моделей. По умолчанию `None`.

**Как работает функция**:
1. Функция инициализирует атрибуты `self.client`, `self.provider` и `self.media_provider` значениями, переданными в качестве аргументов.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
provider = ProviderUtils.convert['g4f.provider.GptGo']
media_provider = None
client_models = ClientModels(client, provider, media_provider)
```

### `get`

```python
def get(self, name, default=None) -> ProviderType:
    """
    Получает провайдера по имени модели или провайдера.

    Args:
        name (str): Имя модели или провайдера.
        default: Значение по умолчанию, если провайдер не найден.

    Returns:
        ProviderType: Провайдер, соответствующий указанному имени, или значение по умолчанию.
    """
```

**Назначение**: Получает провайдера по имени модели или провайдера.

**Параметры**:
- `name` (str): Имя модели или провайдера.
- `default`: Значение по умолчанию, если провайдер не найден.

**Возвращает**:
- `ProviderType`: Провайдер, соответствующий указанному имени, или значение по умолчанию.

**Как работает функция**:
1. Функция проверяет, есть ли указанное имя в словаре `ModelUtils.convert`. Если да, возвращает `best_provider` для данной модели.
2. Если имя не найдено в `ModelUtils.convert`, функция проверяет, есть ли оно в словаре `ProviderUtils.convert`. Если да, возвращает соответствующего провайдера.
3. Если имя не найдено ни в одном из словарей, функция возвращает значение по умолчанию (`default`).

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  # 
provider_name = "g4f.provider.GptGo"
client_models = ClientModels(client)
provider = client_models.get(provider_name)
print(provider)
```

### `get_all`

```python
def get_all(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список всех моделей, поддерживаемых провайдером.

    Args:
        api_key (str, optional): API-ключ для провайдера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы для метода `get_models` провайдера.

    Returns:
        list[str]: Список идентификаторов моделей.
    """
```

**Назначение**: Получает список всех моделей, поддерживаемых провайдером.

**Параметры**:
- `api_key` (str, optional): API-ключ для провайдера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для метода `get_models` провайдера.

**Возвращает**:
- `list[str]`: Список идентификаторов моделей.

**Как работает функция**:
1. Функция проверяет, установлен ли атрибут `self.provider`. Если нет, возвращает пустой список.
2. Если `api_key` не передан, он берется из атрибута `self.client.api_key`.
3. Функция вызывает метод `get_models` провайдера, передавая `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4. Возвращает список идентификаторов моделей, полученных от провайдера.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
provider = ProviderUtils.convert['g4f.provider.GptGo']
client_models = ClientModels(client, provider)
models = client_models.get_all()
print(models)
```

### `get_vision`

```python
def get_vision(self, **kwargs) -> list[str]:
    """
    Получает список vision-моделей.

    Args:
        **kwargs: Дополнительные аргументы для метода `get_all`.

    Returns:
        list[str]: Список идентификаторов vision-моделей.
    """
```

**Назначение**: Получает список vision-моделей.

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_all`.

**Возвращает**:
- `list[str]`: Список идентификаторов vision-моделей.

**Как работает функция**:
1. Функция проверяет, установлен ли атрибут `self.provider`.
2. Если `self.provider` не установлен, возвращается список `model_id` для всех моделей, являющихся экземплярами класса `VisionModel`.
3. Если `self.provider` установлен, вызывается функция `self.get_all(**kwargs)`, после чего проверяется наличие атрибута `vision_models` у `self.provider`.
4. Если атрибут `vision_models` присутствует, возвращается его значение. В противном случае возвращается пустой список.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
provider = ProviderUtils.convert['g4f.provider.GptGo']
client_models = ClientModels(client, provider)
vision_models = client_models.get_vision()
print(vision_models)
```

### `get_media`

```python
def get_media(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список media-моделей, поддерживаемых медиа-провайдером.

    Args:
        api_key (str, optional): API-ключ для медиа-провайдера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы для метода `get_models` медиа-провайдера.

    Returns:
        list[str]: Список идентификаторов медиа-моделей.
    """
```

**Назначение**: Получает список media-моделей, поддерживаемых медиа-провайдером.

**Параметры**:
- `api_key` (str, optional): API-ключ для медиа-провайдера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы для метода `get_models` медиа-провайдера.

**Возвращает**:
- `list[str]`: Список идентификаторов медиа-моделей.

**Как работает функция**:
1. Функция проверяет, установлен ли атрибут `self.media_provider`. Если нет, возвращает пустой список.
2. Если `api_key` не передан, он берется из атрибута `self.client.api_key`.
3. Функция вызывает метод `get_models` медиа-провайдера, передавая `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4. Возвращает список идентификаторов моделей, полученных от медиа-провайдера.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
media_provider = ProviderUtils.convert['g4f.provider.GptGo']
client_models = ClientModels(client, media_provider=media_provider)
media_models = client_models.get_media()
print(media_models)
```

### `get_image`

```python
def get_image(self, **kwargs) -> list[str]:
    """
    Получает список image-моделей.

    Args:
        **kwargs: Дополнительные аргументы для метода `get_media`.

    Returns:
        list[str]: Список идентификаторов image-моделей.
    """
```

**Назначение**: Получает список image-моделей.

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_media`.

**Возвращает**:
- `list[str]`: Список идентификаторов image-моделей.

**Как работает функция**:
1. Функция проверяет, установлен ли атрибут `self.media_provider`.
2. Если `self.media_provider` не установлен, возвращается список `model_id` для всех моделей, являющихся экземплярами класса `ImageModel`.
3. Если `self.media_provider` установлен, вызывается функция `self.get_media(**kwargs)`, после чего проверяется наличие атрибута `image_models` у `self.media_provider`.
4. Если атрибут `image_models` присутствует, возвращается его значение. В противном случае возвращается пустой список.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
media_provider = ProviderUtils.convert['g4f.provider.GptGo']
client_models = ClientModels(client, media_provider=media_provider)
image_models = client_models.get_image()
print(image_models)
```

### `get_video`

```python
def get_video(self, **kwargs) -> list[str]:
    """
    Получает список video-моделей.

    Args:
        **kwargs: Дополнительные аргументы для метода `get_media`.

    Returns:
        list[str]: Список идентификаторов video-моделей.
    """
```

**Назначение**: Получает список video-моделей.

**Параметры**:
- `**kwargs`: Дополнительные аргументы для метода `get_media`.

**Возвращает**:
- `list[str]`: Список идентификаторов video-моделей.

**Как работает функция**:
1. Функция проверяет, установлен ли атрибут `self.media_provider`.
2. Если `self.media_provider` не установлен, возвращается пустой список.
3. Если `self.media_provider` установлен, вызывается функция `self.get_media(**kwargs)`, после чего проверяется наличие атрибута `video_models` у `self.media_provider`.
4. Если атрибут `video_models` присутствует, возвращается его значение. В противном случае возвращается пустой список.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils, ImageModel, VisionModel
client = None  #  
media_provider = ProviderUtils.convert['g4f.provider.GptGo']
client_models = ClientModels(client, media_provider=media_provider)
video_models = client_models.get_video()
print(video_models)