# Модуль `models.py`

## Обзор

Модуль `models.py` содержит класс `ClientModels`, который предназначен для управления и получения списка доступных моделей от различных провайдеров, включая текстовые, визуальные и медиа-модели. Он обеспечивает централизованный доступ к моделям, используемым в проекте `hypotez`, и упрощает их получение и фильтрацию.

## Подробнее

Этот модуль играет важную роль в абстрагировании процесса получения моделей от конкретных провайдеров. Он позволяет клиенту (например, другому модулю или классу) запрашивать список моделей, не заботясь о том, какой провайдер используется и какие параметры необходимо передать.  Класс `ClientModels` инкапсулирует логику выбора провайдера и получения моделей, предоставляя унифицированный интерфейс для работы с ними.

## Классы

### `ClientModels`

**Описание**: Класс `ClientModels` управляет получением моделей от различных провайдеров.

**Принцип работы**:
1.  При инициализации класс принимает объект клиента (`client`), а также провайдера (`provider`) и медиа-провайдера (`media_provider`).
2.  Метод `get` возвращает провайдера для указанной модели по имени, используя словари `ModelUtils.convert` и `ProviderUtils.convert`.
3.  Методы `get_all`, `get_vision`, `get_media`, `get_image` и `get_video` используются для получения списков моделей различных типов от соответствующих провайдеров.

**Атрибуты**:

*   `client`: Объект клиента, используемый для получения ключа API.
*   `provider` (`ProviderType`): Провайдер текстовых моделей.
*   `media_provider` (`ProviderType`): Провайдер медиа-моделей.

**Методы**:

*   `get(name, default=None)`: Возвращает провайдера по имени модели.
*   `get_all(api_key=None, **kwargs)`: Возвращает список всех моделей от текстового провайдера.
*   `get_vision(**kwargs)`: Возвращает список vision моделей.
*   `get_media(api_key=None, **kwargs)`: Возвращает список всех моделей от медиа-провайдера.
*   `get_image(**kwargs)`: Возвращает список image моделей.
*   `get_video(**kwargs)`: Возвращает список video моделей.

## Функции

### `__init__`

```python
def __init__(self, client, provider: ProviderType = None, media_provider: ProviderType = None):
    """
    Инициализирует экземпляр класса `ClientModels`.

    Args:
        client: Объект клиента, используемый для получения ключа API.
        provider (ProviderType, optional): Провайдер текстовых моделей. По умолчанию `None`.
        media_provider (ProviderType, optional): Провайдер медиа-моделей. По умолчанию `None`.

    Returns:
        None

    Raises:
        None
    """
    ...
```

**Назначение**: Инициализирует объект `ClientModels` с клиентом и провайдерами.

**Параметры**:

*   `client`: Объект клиента, используемый для получения ключа API.
*   `provider` (`ProviderType`, optional): Провайдер текстовых моделей. По умолчанию `None`.
*   `media_provider` (`ProviderType`, optional): Провайдер медиа-моделей. По умолчанию `None`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Присваивает переданные аргументы `client`, `provider` и `media_provider` соответствующим атрибутам экземпляра класса.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

# Пример 1: Создание экземпляра ClientModels с клиентом и провайдером
client = MockClient(api_key="test_api_key")
provider = ProviderUtils.convert['Llama2']  # Например, провайдер Llama2
media_provider = ProviderUtils.convert['BingImageCreator'] # Например, провайдер BingImageCreator
client_models = ClientModels(client=client, provider=provider, media_provider=media_provider)

print(f"Client: {client_models.client.api_key}")
print(f"Provider: {client_models.provider}")
print(f"Media Provider: {client_models.media_provider}")

# Пример 2: Создание экземпляра ClientModels только с клиентом
client = MockClient()
client_models = ClientModels(client=client)

print(f"Client: {client_models.client.api_key}")
print(f"Provider: {client_models.provider}")
print(f"Media Provider: {client_models.media_provider}")
```

### `get`

```python
def get(self, name, default=None) -> ProviderType:
    """
    Получает провайдера по имени модели.

    Args:
        name: Имя модели.
        default: Значение по умолчанию, если модель не найдена.

    Returns:
        ProviderType: Провайдер для указанной модели или значение по умолчанию.
    """
    ...
```

**Назначение**: Получает провайдера для указанной модели по имени.

**Параметры**:

*   `name`: Имя модели.
*   `default`: Значение по умолчанию, если модель не найдена.

**Возвращает**:

*   `ProviderType`: Провайдер для указанной модели или значение по умолчанию.

**Как работает функция**:

1.  Проверяет, есть ли модель с указанным именем в словаре `ModelUtils.convert`. Если есть, возвращает `best_provider` для этой модели.
2.  Если модель не найдена в `ModelUtils.convert`, проверяет, есть ли она в словаре `ProviderUtils.convert`. Если есть, возвращает соответствующего провайдера.
3.  Если модель не найдена ни в одном из словарей, возвращает значение `default`.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType
from ..models import ModelUtils

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

# Пример 1: Получение провайдера для существующей модели
client = MockClient(api_key="test_api_key")
client_models = ClientModels(client=client)
model_name = list(ModelUtils.convert.keys())[0]  # Берем первую модель из ModelUtils.convert для примера
provider = client_models.get(model_name)

print(f"Provider for '{model_name}': {provider}")

# Пример 2: Получение провайдера для несуществующей модели с указанием значения по умолчанию
client = MockClient()
client_models = ClientModels(client=client)
default_provider = ProviderUtils.convert['Bard']  # Например, провайдер Bard
provider = client_models.get("non_existent_model", default=default_provider)

print(f"Provider for 'non_existent_model': {provider}")

# Пример 3: Получение провайдера для существующего провайдера
client = MockClient()
client_models = ClientModels(client=client)
provider_name = list(ProviderUtils.convert.keys())[0]  # Берем первый провайдер из ProviderUtils.convert для примера
provider = client_models.get(provider_name)

print(f"Provider for '{provider_name}': {provider}")
```

### `get_all`

```python
def get_all(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список всех моделей от текстового провайдера.

    Args:
        api_key (str, optional): Ключ API. По умолчанию `None`.
        **kwargs: Дополнительные аргументы, передаваемые в `get_models` провайдера.

    Returns:
        list[str]: Список идентификаторов моделей.
    """
    ...
```

**Назначение**: Получает список всех моделей от текстового провайдера.

**Параметры**:

*   `api_key` (`str`, optional): Ключ API. По умолчанию `None`.
*   `**kwargs`: Дополнительные аргументы, передаваемые в `get_models` провайдера.

**Возвращает**:

*   `list[str]`: Список идентификаторов моделей.

**Как работает функция**:

1.  Проверяет, установлен ли атрибут `provider`. Если нет, возвращает пустой список.
2.  Если `api_key` не передан, использует `self.client.api_key`.
3.  Вызывает метод `get_models` провайдера, передавая `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4.  Возвращает список моделей, полученный от провайдера.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

class MockProvider:
    def __init__(self, name):
        self.name = name
        self.models = [f"{name}_model_1", f"{name}_model_2"]

    def get_models(self, **kwargs):
        # Пример использования api_key, если он передан
        api_key = kwargs.get("api_key")
        if api_key:
            print(f"Using API key: {api_key}")
        return self.models

    def __str__(self):
        return self.name

# Пример 1: Получение списка моделей с указанием API key
client = MockClient(api_key="test_api_key")
provider = MockProvider(name="TestProvider")  # Создаем экземпляр MockProvider
client_models = ClientModels(client=client, provider=provider)
models = client_models.get_all(api_key="custom_api_key")

print(f"Models: {models}")

# Пример 2: Получение списка моделей без указания API key (используется API key клиента)
client = MockClient(api_key="client_api_key")
provider = MockProvider(name="AnotherProvider")  # Создаем экземпляр MockProvider
client_models = ClientModels(client=client, provider=provider)
models = client_models.get_all()

print(f"Models: {models}")

# Пример 3: Получение списка моделей без провайдера
client = MockClient()
client_models = ClientModels(client=client)
models = client_models.get_all()

print(f"Models: {models}")
```

### `get_vision`

```python
def get_vision(self, **kwargs) -> list[str]:
    """
    Получает список vision моделей.

    Args:
        **kwargs: Дополнительные аргументы, передаваемые в `get_all` провайдера.

    Returns:
        list[str]: Список идентификаторов vision моделей.
    """
    ...
```

**Назначение**: Получает список vision моделей.

**Параметры**:

*   `**kwargs`: Дополнительные аргументы, передаваемые в `get_all` провайдера.

**Возвращает**:

*   `list[str]`: Список идентификаторов vision моделей.

**Как работает функция**:

1.  Если `self.provider` не установлен, возвращает список `model_id` для каждой модели, являющейся экземпляром `VisionModel`.
2.  Вызывает `self.get_all(**kwargs)` для обновления списка моделей у провайдера.
3.  Если у провайдера есть атрибут `vision_models`, возвращает его значение.
4.  Если атрибута `vision_models` нет, возвращает пустой список.

**Примеры**:

```python
from ..models import ModelUtils, VisionModel
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

class MockProvider:
    def __init__(self, name):
        self.name = name
        self.vision_models = [f"{name}_vision_model_1", f"{name}_vision_model_2"]

    def get_models(self, **kwargs):
        return []  # В данном примере не используется

    def __str__(self):
        return self.name

# Пример 1: Получение vision моделей с установленным провайдером
client = MockClient()
provider = MockProvider(name="TestProvider")  # Создаем экземпляр MockProvider
client_models = ClientModels(client=client, provider=provider)
vision_models = client_models.get_vision()

print(f"Vision Models: {vision_models}")

# Пример 2: Получение vision моделей без установленного провайдера
client = MockClient()
client_models = ClientModels(client=client)

# Добавим VisionModel в ModelUtils.convert для демонстрации
class DummyVisionModel(VisionModel):
    pass

model_id = "dummy_vision_model"
ModelUtils.convert[model_id] = DummyVisionModel()

vision_models = client_models.get_vision()

print(f"Vision Models: {vision_models}")

# Пример 3: Получение vision моделей с провайдером без vision_models
class MockProviderWithoutVisionModels:
    def __init__(self, name):
        self.name = name

    def get_models(self, **kwargs):
        return []

client = MockClient()
provider = MockProviderWithoutVisionModels(name="AnotherProvider")
client_models = ClientModels(client=client, provider=provider)
vision_models = client_models.get_vision()

print(f"Vision Models: {vision_models}")
```

### `get_media`

```python
def get_media(self, api_key: str = None, **kwargs) -> list[str]:
    """
    Получает список всех моделей от медиа-провайдера.

    Args:
        api_key (str, optional): Ключ API. По умолчанию `None`.
        **kwargs: Дополнительные аргументы, передаваемые в `get_models` провайдера.

    Returns:
        list[str]: Список идентификаторов моделей.
    """
    ...
```

**Назначение**: Получает список всех моделей от медиа-провайдера.

**Параметры**:

*   `api_key` (`str`, optional): Ключ API. По умолчанию `None`.
*   `**kwargs`: Дополнительные аргументы, передаваемые в `get_models` провайдера.

**Возвращает**:

*   `list[str]`: Список идентификаторов моделей.

**Как работает функция**:

1.  Проверяет, установлен ли атрибут `media_provider`. Если нет, возвращает пустой список.
2.  Если `api_key` не передан, использует `self.client.api_key`.
3.  Вызывает метод `get_models` медиа-провайдера, передавая `api_key` (если он есть) и дополнительные аргументы `kwargs`.
4.  Возвращает список моделей, полученный от медиа-провайдера.

**Примеры**:

```python
class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

class MockMediaProvider:
    def __init__(self, name):
        self.name = name
        self.models = [f"{name}_media_model_1", f"{name}_media_model_2"]

    def get_models(self, **kwargs):
        # Пример использования api_key, если он передан
        api_key = kwargs.get("api_key")
        if api_key:
            print(f"Using API key: {api_key}")
        return self.models

    def __str__(self):
        return self.name

# Пример 1: Получение списка медиа-моделей с указанием API key
client = MockClient(api_key="test_api_key")
media_provider = MockMediaProvider(name="TestMediaProvider")  # Создаем экземпляр MockMediaProvider
client_models = ClientModels(client=client, media_provider=media_provider)
models = client_models.get_media(api_key="custom_api_key")

print(f"Media Models: {models}")

# Пример 2: Получение списка медиа-моделей без указания API key (используется API key клиента)
client = MockClient(api_key="client_api_key")
media_provider = MockMediaProvider(name="AnotherMediaProvider")  # Создаем экземпляр MockMediaProvider
client_models = ClientModels(client=client, media_provider=media_provider)
models = client_models.get_media()

print(f"Media Models: {models}")

# Пример 3: Получение списка медиа-моделей без медиа-провайдера
client = MockClient()
client_models = ClientModels(client=client)
models = client_models.get_media()

print(f"Media Models: {models}")
```

### `get_image`

```python
def get_image(self, **kwargs) -> list[str]:
    """
    Получает список image моделей.

    Args:
        **kwargs: Дополнительные аргументы, передаваемые в `get_media` провайдера.

    Returns:
        list[str]: Список идентификаторов image моделей.
    """
    ...
```

**Назначение**: Получает список image моделей.

**Параметры**:

*   `**kwargs`: Дополнительные аргументы, передаваемые в `get_media` провайдера.

**Возвращает**:

*   `list[str]`: Список идентификаторов image моделей.

**Как работает функция**:

1.  Если `self.media_provider` не установлен, возвращает список `model_id` для каждой модели, являющейся экземпляром `ImageModel`.
2.  Вызывает `self.get_media(**kwargs)` для обновления списка моделей у медиа-провайдера.
3.  Если у медиа-провайдера есть атрибут `image_models`, возвращает его значение.
4.  Если атрибута `image_models` нет, возвращает пустой список.

**Примеры**:

```python
from ..models import ModelUtils, ImageModel
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

class MockMediaProvider:
    def __init__(self, name):
        self.name = name
        self.image_models = [f"{name}_image_model_1", f"{name}_image_model_2"]

    def get_models(self, **kwargs):
        return []  # В данном примере не используется

    def __str__(self):
        return self.name

# Пример 1: Получение image моделей с установленным медиа-провайдером
client = MockClient()
media_provider = MockMediaProvider(name="TestMediaProvider")  # Создаем экземпляр MockMediaProvider
client_models = ClientModels(client=client, media_provider=media_provider)
image_models = client_models.get_image()

print(f"Image Models: {image_models}")

# Пример 2: Получение image моделей без установленного медиа-провайдера
client = MockClient()
client_models = ClientModels(client=client)

# Добавим ImageModel в ModelUtils.convert для демонстрации
class DummyImageModel(ImageModel):
    pass

model_id = "dummy_image_model"
ModelUtils.convert[model_id] = DummyImageModel()

image_models = client_models.get_image()

print(f"Image Models: {image_models}")

# Пример 3: Получение image моделей с медиа-провайдером без image_models
class MockMediaProviderWithoutImageModels:
    def __init__(self, name):
        self.name = name

    def get_models(self, **kwargs):
        return []

client = MockClient()
media_provider = MockMediaProviderWithoutImageModels(name="AnotherMediaProvider")
client_models = ClientModels(client=client, media_provider=media_provider)
image_models = client_models.get_image()

print(f"Image Models: {image_models}")
```

### `get_video`

```python
def get_video(self, **kwargs) -> list[str]:
    """
    Получает список video моделей.

    Args:
        **kwargs: Дополнительные аргументы, передаваемые в `get_media` провайдера.

    Returns:
        list[str]: Список идентификаторов video моделей.
    """
    ...
```

**Назначение**: Получает список video моделей.

**Параметры**:

*   `**kwargs`: Дополнительные аргументы, передаваемые в `get_media` провайдера.

**Возвращает**:

*   `list[str]`: Список идентификаторов video моделей.

**Как работает функция**:

1.  Если `self.media_provider` не установлен, возвращает пустой список.
2.  Вызывает `self.get_media(**kwargs)` для обновления списка моделей у медиа-провайдера.
3.  Если у медиа-провайдера есть атрибут `video_models`, возвращает его значение.
4.  Если атрибута `video_models` нет, возвращает пустой список.

**Примеры**:

```python
from ..Provider import ProviderUtils
from ..providers.types import ProviderType

class MockClient:
    def __init__(self, api_key=None):
        self.api_key = api_key

class MockMediaProvider:
    def __init__(self, name):
        self.name = name
        self.video_models = [f"{name}_video_model_1", f"{name}_video_model_2"]

    def get_models(self, **kwargs):
        return []  # В данном примере не используется

    def __str__(self):
        return self.name

# Пример 1: Получение video моделей с установленным медиа-провайдером
client = MockClient()
media_provider = MockMediaProvider(name="TestMediaProvider")  # Создаем экземпляр MockMediaProvider
client_models = ClientModels(client=client, media_provider=media_provider)
video_models = client_models.get_video()

print(f"Video Models: {video_models}")

# Пример 2: Получение video моделей без установленного медиа-провайдера
client = MockClient()
client_models = ClientModels(client=client)
video_models = client_models.get_video()

print(f"Video Models: {video_models}")

# Пример 3: Получение video моделей с медиа-провайдером без video_models
class MockMediaProviderWithoutVideoModels:
    def __init__(self, name):
        self.name = name

    def get_models(self, **kwargs):
        return []

client = MockClient()
media_provider = MockMediaProviderWithoutVideoModels(name="AnotherMediaProvider")
client_models = ClientModels(client=client, media_provider=media_provider)
video_models = client_models.get_video()

print(f"Video Models: {video_models}")