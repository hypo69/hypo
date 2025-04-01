# Документация для модуля `backend.py`

## Обзор

Модуль содержит тесты для backend API, используемого в графическом интерфейсе `g4f`. Он включает в себя проверку версий, моделей, провайдеров и поисковых функций.

## Подробней

Этот модуль предназначен для автоматического тестирования API, предоставляющего данные для графического интерфейса. Тесты охватывают различные аспекты API, включая получение версий, моделей, провайдеров и выполнение поисковых запросов. В случае отсутствия необходимых зависимостей, тесты пропускаются.

## Классы

### `TestBackendApi`

**Описание**: Класс `TestBackendApi` содержит набор тестов для проверки функциональности `Backend_Api`.

**Принцип работы**:
Класс `TestBackendApi` является подклассом `unittest.TestCase` и содержит методы для тестирования различных функций `Backend_Api`. В методе `setUp` выполняется настройка тестовой среды, включая создание экземпляра `Backend_Api` и проверку наличия необходимых зависимостей. Если зависимости отсутствуют, тест пропускается.

**Методы**:
- `setUp`: Настройка тестовой среды перед каждым тестом.
- `test_version`: Тестирование эндпоинта для получения информации о версии.
- `test_get_models`: Тестирование эндпоинта для получения списка моделей.
- `test_get_providers`: Тестирование эндпоинта для получения списка провайдеров.
- `test_search`: Тестирование функции поиска.

## Функции

### `setUp`

```python
def setUp(self):
    """
    Настраивает тестовую среду перед каждым тестом.

    Args:
        self: Экземпляр класса TestBackendApi.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если отсутствует модуль `g4f.gui.server.backend_api`.
    """
```

**Как работает функция**:

1. Проверяется наличие требований для запуска тестов графического интерфейса. Если модуль `g4f.gui.server.backend_api` не установлен, тест пропускается.
2. Создается mock-объект `MagicMock` для имитации приложения.
3. Инициализируется экземпляр класса `Backend_Api` с mock-объектом приложения.

**Примеры**:

```python
# Пример использования setUp
test_case = TestBackendApi()
test_case.setUp()
```

### `test_version`

```python
def test_version(self):
    """
    Тестирует эндпоинт для получения информации о версии.

    Args:
        self: Экземпляр класса TestBackendApi.

    Returns:
        None

    Raises:
        AssertionError: Если в ответе отсутствует ключ "version" или "latest_version".
    """
```

**Как работает функция**:

1. Вызывается метод `get_version` объекта `self.api`.
2. Проверяется наличие ключей `"version"` и `"latest_version"` в полученном ответе.

**Примеры**:

```python
# Пример использования test_version
test_case = TestBackendApi()
test_case.setUp()
test_case.test_version()
```

### `test_get_models`

```python
def test_get_models(self):
    """
    Тестирует эндпоинт для получения списка моделей.

    Args:
        self: Экземпляр класса TestBackendApi.

    Returns:
        None

    Raises:
        AssertionError: Если ответ не является списком или список пуст.
    """
```

**Как работает функция**:

1. Вызывается метод `get_models` объекта `self.api`.
2. Проверяется, что полученный ответ является списком (`list`).
3. Проверяется, что длина списка больше 0.

**Примеры**:

```python
# Пример использования test_get_models
test_case = TestBackendApi()
test_case.setUp()
test_case.test_get_models()
```

### `test_get_providers`

```python
def test_get_providers(self):
    """
    Тестирует эндпоинт для получения списка провайдеров.

    Args:
        self: Экземпляр класса TestBackendApi.

    Returns:
        None

    Raises:
        AssertionError: Если ответ не является списком или список пуст.
    """
```

**Как работает функция**:

1. Вызывается метод `get_providers` объекта `self.api`.
2. Проверяется, что полученный ответ является списком (`list`).
3. Проверяется, что длина списка больше 0.

**Примеры**:

```python
# Пример использования test_get_providers
test_case = TestBackendApi()
test_case.setUp()
test_case.test_get_providers()
```

### `test_search`

```python
def test_search(self):
    """
    Тестирует функцию поиска.

    Args:
        self: Экземпляр класса TestBackendApi.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если отсутствует модуль `duckduckgo_search` или `g4f.gui.server.internet.search`.
        AssertionError: Если длина результата поиска равна 0.
    """
```

**Как работает функция**:

1. Импортируется функция `search` из модуля `g4f.gui.server.internet`.
2. Выполняется поисковый запрос "Hello" с использованием `asyncio.run`.
3. Обрабатываются возможные исключения:
   - `DuckDuckGoSearchException`: Если возникает ошибка при поиске, тест пропускается.
   - `MissingRequirementsError`: Если поиск не установлен, тест пропускается.
4. Проверяется, что длина результата поиска больше 0.

**Примеры**:

```python
# Пример использования test_search
test_case = TestBackendApi()
test_case.setUp()
test_case.test_search()