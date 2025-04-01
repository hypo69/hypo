# Модуль для модульного тестирования провайдеров моделей
===========================================================

Модуль содержит класс `TestProviderHasModel`, который используется для модульного тестирования наличия моделей у различных провайдеров, определенных в `g4f`.

Пример использования
----------------------

```python
import unittest
from typing import Type
import asyncio

from g4f.models import __models__
from g4f.providers.base_provider import BaseProvider, ProviderModelMixin
from g4f.errors import MissingRequirementsError, MissingAuthError

class TestProviderHasModel(unittest.TestCase):
    cache: dict = {}

    def test_provider_has_model(self):
        for model, providers in __models__.values():
            for provider in providers:
                if issubclass(provider, ProviderModelMixin):
                    if model.name in provider.model_aliases:
                        model_name = provider.model_aliases[model.name]
                    else:
                        model_name = model.name
                    self.provider_has_model(provider, model_name)

    def provider_has_model(self, provider: Type[BaseProvider], model: str):
        if provider.__name__ not in self.cache:
            try:
                self.cache[provider.__name__] = provider.get_models()
            except (MissingRequirementsError, MissingAuthError):
                return
        if self.cache[provider.__name__]:
            self.assertIn(model, self.cache[provider.__name__], provider.__name__)

    def test_all_providers_working(self):
        for model, providers in __models__.values():
            for provider in providers:
                self.assertTrue(provider.working, f"{provider.__name__} in {model.name}")
```

## Обзор

Модуль предоставляет набор тестов для проверки совместимости моделей и провайдеров в библиотеке `g4f`. Он проверяет, что каждый провайдер, указанный в `__models__`, имеет соответствующие модели и что все провайдеры помечены как работающие.

## Подробнее

Модуль использует библиотеку `unittest` для определения тестовых случаев. Он итерируется по моделям и провайдерам, определенным в `g4f.models.__models__`, и проверяет, что каждый провайдер имеет доступ к соответствующим моделям. Также проверяется, что все провайдеры помечены как работающие.

## Классы

### `TestProviderHasModel`

**Описание**: Класс, содержащий модульные тесты для проверки наличия моделей у провайдеров.

**Наследует**: `unittest.TestCase`

**Атрибуты**:
- `cache` (dict): Статический кэш для хранения списка моделей, предоставляемых каждым провайдером.

**Методы**:
- `test_provider_has_model()`: Проверяет, что каждый провайдер имеет соответствующие модели.
- `provider_has_model(provider: Type[BaseProvider], model: str)`: Проверяет, что конкретный провайдер имеет указанную модель.
- `test_all_providers_working()`: Проверяет, что все провайдеры помечены как работающие.

## Функции

### `test_provider_has_model`

```python
def test_provider_has_model(self):
    """Проверяет, что каждый провайдер имеет соответствующие модели.
    Args:
        self: Экземпляр класса TestProviderHasModel.

    Returns:
        None

    Raises:
        AssertionError: Если провайдер не имеет ожидаемой модели.
    """
    ...
```

**Назначение**: Проверяет, что каждый провайдер, указанный в `__models__`, имеет соответствующие модели.

**Как работает функция**:
1. **Перебор моделей и провайдеров**: Итерируется по всем моделям и связанным с ними провайдерам из `__models__.values()`.
2. **Проверка на `ProviderModelMixin`**: Убеждается, что текущий провайдер является подклассом `ProviderModelMixin`.
3. **Определение имени модели**: Если у модели есть псевдоним (`model_aliases`) для данного провайдера, используется псевдоним. В противном случае используется стандартное имя модели.
4. **Вызов `provider_has_model`**: Вызывает метод `self.provider_has_model` для проверки наличия модели у текущего провайдера.

ASCII flowchart:

```
A[Перебор моделей и провайдеров]
|
B[Проверка на ProviderModelMixin]
|
C[Определение имени модели (псевдоним или стандартное имя)]
|
D[Вызов provider_has_model]
```

**Примеры**:

Примеры вызова не требуются, так как это метод модульного тестирования, вызываемый автоматически фреймворком `unittest`.

### `provider_has_model`

```python
def provider_has_model(self, provider: Type[BaseProvider], model: str):
    """Проверяет, что конкретный провайдер имеет указанную модель.

    Args:
        provider (Type[BaseProvider]): Класс провайдера для проверки.
        model (str): Имя модели для проверки.
    Returns:
        None
    Raises:
        AssertionError: Если провайдер не имеет указанной модели.
    """
    ...
```

**Назначение**: Проверяет, что конкретный провайдер имеет указанную модель.

**Параметры**:
- `provider` (Type[BaseProvider]): Класс провайдера для проверки.
- `model` (str): Имя модели для проверки.

**Как работает функция**:
1. **Проверка кэша**: Если имя провайдера отсутствует в кэше, пытается получить список моделей от провайдера, вызвав `provider.get_models()`.
2. **Обработка исключений**: Если при получении списка моделей возникают исключения `MissingRequirementsError` или `MissingAuthError`, функция завершается, чтобы избежать ошибок при тестировании провайдеров, требующих дополнительной настройки.
3. **Проверка наличия модели**: Проверяет, что указанная модель присутствует в списке моделей, возвращенном провайдером (или взятом из кэша). Если модель отсутствует, генерируется `AssertionError`.

ASCII flowchart:

```
A[Проверка кэша для провайдера]
|
B[Если нет в кэше: Пытаемся получить список моделей от провайдера]
|
C[Обработка MissingRequirementsError, MissingAuthError]
|
D[Проверка наличия модели в списке моделей]
```

**Примеры**:

Примеры вызова не требуются, так как это метод модульного тестирования, вызываемый автоматически фреймворком `unittest`.

### `test_all_providers_working`

```python
def test_all_providers_working(self):
    """Проверяет, что все провайдеры помечены как работающие.
    Args:
        self: Экземпляр класса TestProviderHasModel.

    Returns:
        None

    Raises:
        AssertionError: Если провайдер не помечен как работающий.
    """
    ...
```

**Назначение**: Проверяет, что все провайдеры, указанные в `__models__`, помечены как работающие.

**Как работает функция**:
1. **Перебор моделей и провайдеров**: Итерируется по всем моделям и связанным с ними провайдерам из `__models__.values()`.
2. **Проверка `provider.working`**: Убеждается, что атрибут `working` у текущего провайдера имеет значение `True`. Если это не так, генерируется `AssertionError`.

ASCII flowchart:

```
A[Перебор моделей и провайдеров]
|
B[Проверка provider.working]
```

**Примеры**:

Примеры вызова не требуются, так как это метод модульного тестирования, вызываемый автоматически фреймворком `unittest`.