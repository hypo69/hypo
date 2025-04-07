# Документация модуля `backend.py`

## Обзор

Модуль содержит юнит-тесты для backend API, используемого в графическом интерфейсе `g4f`. Он проверяет корректность работы API, включая получение информации о версии, моделях, провайдерах, а также функцию поиска.

## Подробнее

Этот модуль является частью системы тестирования и предназначен для автоматической проверки работоспособности API, предоставляющего данные для графического интерфейса. Расположение файла в структуре проекта указывает на то, что он отвечает за тестирование backend-части API для gpt4free.

## Классы

### `TestBackendApi`

**Описание**: Класс `TestBackendApi` содержит набор тестов для проверки функциональности `Backend_Api`.

**Наследует**: `unittest.TestCase`

**Атрибуты**:

-   `app` (MagicMock): Мок-объект приложения, используемый для имитации окружения.
-   `api` (Backend_Api): Экземпляр класса `Backend_Api`, который будет тестироваться.

**Методы**:

-   `setUp()`: Метод подготовки тестового окружения.
-   `test_version()`: Тест для проверки получения информации о версии.
-   `test_get_models()`: Тест для проверки получения списка моделей.
-   `test_get_providers()`: Тест для проверки получения списка провайдеров.
-   `test_search()`: Тест для проверки работы функции поиска.

## Функции

### `setUp`

```python
def setUp(self):
    """
    Метод подготовки тестового окружения перед каждым тестом.

    Args:
        self (TestBackendApi): Экземпляр класса `TestBackendApi`.

    Raises:
        unittest.SkipTest: Если не установлены необходимые зависимости (`gui is not installed`).

    Как работает функция:
    1. Проверяет, установлены ли необходимые зависимости для графического интерфейса.
    2. Если зависимости не установлены, пропускает все тесты в классе.
    3. Создает мок-объект приложения (`MagicMock`).
    4. Инициализирует экземпляр класса `Backend_Api` с мок-объектом приложения.
    """
```

**Как работает функция**:

1.  **Проверка зависимостей**: Функция проверяет, установлены ли необходимые зависимости для графического интерфейса (`gui`). Если `has_requirements` равно `False`, это означает, что зависимости не установлены, и тест будет пропущен.

2.  **Пропуск тестов**: Если зависимости не установлены, вызывается `self.skipTest("gui is not installed")`, что приводит к пропуску всех тестов в данном классе.

3.  **Создание мок-объекта**: Если зависимости установлены, создается мок-объект приложения с использованием `MagicMock`. Этот объект будет использоваться для имитации взаимодействия с приложением.

4.  **Инициализация Backend_Api**: Создается экземпляр класса `Backend_Api`, который принимает мок-объект приложения в качестве аргумента. Этот экземпляр будет тестироваться в последующих методах.

```
    Проверка зависимостей
    │
    ├─── Нет зависимостей? ─── Да ─── Пропуск тестов
    │   │
    │   └─── Нет ─── Создание мок-объекта
    │       │
    │       └─── Инициализация Backend_Api
    │
    Конец
```

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.api = MagicMock()

    def test_something(self):
        self.assertTrue(True)  # Пример теста
```

### `test_version`

```python
def test_version(self):
    """
    Тест для проверки получения информации о версии.

    Args:
        self (TestBackendApi): Экземпляр класса `TestBackendApi`.

    Returns:
        None

    Как работает функция:
    1. Вызывает метод `get_version()` класса `Backend_Api`.
    2. Проверяет, что в ответе присутствуют ключи "version" и "latest_version".
    """
```

**Как работает функция**:

1.  **Вызов метода `get_version()`**: Функция вызывает метод `get_version()` экземпляра класса `Backend_Api`. Предполагается, что этот метод возвращает словарь, содержащий информацию о версии.

2.  **Проверка ключей в ответе**: Функция проверяет, что в словаре, возвращенном методом `get_version()`, присутствуют ключи "version" и "latest_version". Это делается с помощью `self.assertIn("version", response)` и `self.assertIn("latest_version", response)`. Если ключи отсутствуют, тест завершится с ошибкой.

```
    Вызов get_version()
    │
    └─── Проверка наличия ключа "version" в ответе
    │
    └─── Проверка наличия ключа "latest_version" в ответе
    │
    Конец
```

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.api = MagicMock()
        self.api.get_version = MagicMock(return_value={"version": "1.0", "latest_version": "2.0"})

    def test_version(self):
        response = self.api.get_version()
        self.assertIn("version", response)
        self.assertIn("latest_version", response)
```

### `test_get_models`

```python
def test_get_models(self):
    """
    Тест для проверки получения списка моделей.

    Args:
        self (TestBackendApi): Экземпляр класса `TestBackendApi`.

    Returns:
        None

    Как работает функция:
    1. Вызывает метод `get_models()` класса `Backend_Api`.
    2. Проверяет, что ответ является списком.
    3. Проверяет, что длина списка больше 0.
    """
```

**Как работает функция**:

1.  **Вызов метода `get_models()`**: Функция вызывает метод `get_models()` экземпляра класса `Backend_Api`. Предполагается, что этот метод возвращает список моделей.

2.  **Проверка типа ответа**: Функция проверяет, что возвращенный объект является списком с помощью `self.assertIsInstance(response, list)`.

3.  **Проверка длины списка**: Функция проверяет, что длина списка больше 0 с помощью `self.assertTrue(len(response) > 0)`. Это гарантирует, что список моделей не пуст.

```
    Вызов get_models()
    │
    └─── Проверка, является ли ответ списком
    │
    └─── Проверка, что длина списка больше 0
    │
    Конец
```

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.api = MagicMock()
        self.api.get_models = MagicMock(return_value=["model1", "model2"])

    def test_get_models(self):
        response = self.api.get_models()
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)
```

### `test_get_providers`

```python
def test_get_providers(self):
    """
    Тест для проверки получения списка провайдеров.

    Args:
        self (TestBackendApi): Экземпляр класса `TestBackendApi`.

    Returns:
        None

    Как работает функция:
    1. Вызывает метод `get_providers()` класса `Backend_Api`.
    2. Проверяет, что ответ является списком.
    3. Проверяет, что длина списка больше 0.
    """
```

**Как работает функция**:

1.  **Вызов метода `get_providers()`**: Функция вызывает метод `get_providers()` экземпляра класса `Backend_Api`. Предполагается, что этот метод возвращает список провайдеров.

2.  **Проверка типа ответа**: Функция проверяет, что возвращенный объект является списком с помощью `self.assertIsInstance(response, list)`.

3.  **Проверка длины списка**: Функция проверяет, что длина списка больше 0 с помощью `self.assertTrue(len(response) > 0)`. Это гарантирует, что список провайдеров не пуст.

```
    Вызов get_providers()
    │
    └─── Проверка, является ли ответ списком
    │
    └─── Проверка, что длина списка больше 0
    │
    Конец
```

**Примеры**:

```python
import unittest
from unittest.mock import MagicMock

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.api = MagicMock()
        self.api.get_providers = MagicMock(return_value=["provider1", "provider2"])

    def test_get_providers(self):
        response = self.api.get_providers()
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)
```

### `test_search`

```python
def test_search(self):
    """
    Тест для проверки работы функции поиска.

    Args:
        self (TestBackendApi): Экземпляр класса `TestBackendApi`.

    Returns:
        None

    Raises:
        unittest.SkipTest: Если `DuckDuckGoSearchException` или `MissingRequirementsError`.

    Как работает функция:
    1. Импортирует функцию `search` из модуля `g4f.gui.server.internet`.
    2. Вызывает функцию `search` с поисковым запросом "Hello" и запускает её в асинхронном режиме.
    3. Проверяет, что длина результата поиска больше 0.
    """
```

**Как работает функция**:

1.  **Импорт функции поиска**: Импортируется функция `search` из модуля `g4f.gui.server.internet`.

2.  **Вызов функции поиска**: Функция `search` вызывается с поисковым запросом "Hello". Вызов оборачивается в `asyncio.run()`, чтобы выполнить асинхронную операцию.

3.  **Обработка исключений**:
    *   Если возникает исключение `DuckDuckGoSearchException`, тест пропускается с соответствующим сообщением.
    *   Если возникает исключение `MissingRequirementsError`, тест пропускается с сообщением о том, что поиск не установлен.

4.  **Проверка результата поиска**: Функция проверяет, что длина результата поиска (который, как предполагается, является строкой или списком) больше 0.

```
    Импорт функции поиска
    │
    └─── Вызов функции поиска в асинхронном режиме
    │
    ├─── DuckDuckGoSearchException ─── Пропуск теста
    │   │
    │   ├─── MissingRequirementsError ─── Пропуск теста
    │   │
    │   └─── Проверка, что длина результата поиска больше 0
    │
    Конец
```

**Примеры**:

```python
import unittest
import asyncio
from unittest.mock import MagicMock

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.api = MagicMock()

    async def mock_search(query: str) -> str:
        return "Result"
    
    def test_search(self):
        asyncio.run(self.mock_search("Hello"))
        self.assertTrue(len("Result") > 0)