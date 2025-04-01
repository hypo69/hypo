# Модуль интеграционных тестов для gpt4free
## Обзор

Модуль `integration.py` предназначен для интеграционного тестирования провайдеров `Copilot` и `DDG` с использованием библиотеки `g4f`. Он включает в себя как синхронные, так и асинхронные тесты для проверки корректности взаимодействия с провайдерами при запросах к `ChatCompletion`.

## Подробнее

Этот модуль выполняет интеграционные тесты, чтобы убедиться, что провайдеры `Copilot` и `DDG` правильно интегрированы с библиотекой `g4f`. В частности, проверяется, что ответы от этих провайдеров соответствуют ожидаемому формату `json_object` и содержат ключ `"success"`.
Модуль использует `unittest` для организации тестов и включает как синхронные, так и асинхронные тесты для полного охвата функциональности.

## Классы

### `TestProviderIntegration`

**Описание**: Класс для синхронных интеграционных тестов провайдеров.

**Наследует**:
- `unittest.TestCase`: Базовый класс для создания тестов в `unittest`.

**Методы**:

- `test_bing(self)`: Тест для провайдера `Copilot`.
- `test_openai(self)`: Тест для провайдера `DDG`.

### `TestChatCompletionAsync`

**Описание**: Класс для асинхронных интеграционных тестов провайдеров.

**Наследует**:
- `unittest.IsolatedAsyncioTestCase`: Базовый класс для создания асинхронных тестов в `unittest`.

**Методы**:

- `test_bing(self)`: Асинхронный тест для провайдера `Copilot`.
- `test_openai(self)`: Асинхронный тест для провайдера `DDG`.

## Функции

### `TestProviderIntegration.test_bing`

```python
    def test_bing(self):
        client = Client(provider=Copilot)
        response = client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))
```

**Назначение**: Проверяет интеграцию с провайдером `Copilot`. Функция создает синхронный клиент с провайдером `Copilot`, отправляет запрос и проверяет, что ответ является экземпляром `ChatCompletion` и содержит ключ `"success"` в JSON.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TestProviderIntegration`.

**Возвращает**: None

**Вызывает исключения**: None

**Как работает функция**:
1. **Создание клиента**: Создается экземпляр класса `Client` с указанием провайдера `Copilot`.
2. **Отправка запроса**: Отправляется запрос к `chat.completions.create` с предопределенными сообщениями `DEFAULT_MESSAGES`, пустой строкой и указанием формата ответа `json_object`.
3. **Проверка типа ответа**: Проверяется, что полученный ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Извлекается содержимое ответа, декодируется из JSON и проверяется наличие ключа `"success"`.

```
Создание клиента (client)
↓
Отправка запроса (response)
↓
Проверка типа ответа (assertIsInstance)
↓
Проверка содержимого ответа (assertIn)
```

**Примеры**:
```python
import unittest
from g4f.client import Client
from g4f.Provider import Copilot
from g4f.client import ChatCompletion

DEFAULT_MESSAGES = [{"role": "system", "content": 'Response in json, Example: {"success": false}'},
                    {"role": "user", "content": "Say success true in json"}]

class TestProviderIntegration(unittest.TestCase):
    def test_bing(self):
        client = Client(provider=Copilot)
        response = client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))

if __name__ == '__main__':
    unittest.main()
```

### `TestProviderIntegration.test_openai`

```python
    def test_openai(self):
        client = Client(provider=DDG)
        response = client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))
```

**Назначение**: Проверяет интеграцию с провайдером `DDG`. Функция создает синхронный клиент с провайдером `DDG`, отправляет запрос и проверяет, что ответ является экземпляром `ChatCompletion` и содержит ключ `"success"` в JSON.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TestProviderIntegration`.

**Возвращает**: None

**Вызывает исключения**: None

**Как работает функция**:
1. **Создание клиента**: Создается экземпляр класса `Client` с указанием провайдера `DDG`.
2. **Отправка запроса**: Отправляется запрос к `chat.completions.create` с предопределенными сообщениями `DEFAULT_MESSAGES`, пустой строкой и указанием формата ответа `json_object`.
3. **Проверка типа ответа**: Проверяется, что полученный ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Извлекается содержимое ответа, декодируется из JSON и проверяется наличие ключа `"success"`.

```
Создание клиента (client)
↓
Отправка запроса (response)
↓
Проверка типа ответа (assertIsInstance)
↓
Проверка содержимого ответа (assertIn)
```

**Примеры**:
```python
import unittest
from g4f.client import Client
from g4f.Provider import DDG
from g4f.client import ChatCompletion

DEFAULT_MESSAGES = [{"role": "system", "content": 'Response in json, Example: {"success": false}'},
                    {"role": "user", "content": "Say success true in json"}]

class TestProviderIntegration(unittest.TestCase):
    def test_openai(self):
        client = Client(provider=DDG)
        response = client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))

if __name__ == '__main__':
    unittest.main()
```

### `TestChatCompletionAsync.test_bing`

```python
    async def test_bing(self):
        client = AsyncClient(provider=Copilot)
        response = await client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))
```

**Назначение**: Асинхронно проверяет интеграцию с провайдером `Copilot`. Функция создает асинхронный клиент с провайдером `Copilot`, отправляет запрос и проверяет, что ответ является экземпляром `ChatCompletion` и содержит ключ `"success"` в JSON.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TestChatCompletionAsync`.

**Возвращает**: None

**Вызывает исключения**: None

**Как работает функция**:
1. **Создание клиента**: Создается экземпляр класса `AsyncClient` с указанием провайдера `Copilot`.
2. **Отправка запроса**: Отправляется асинхронный запрос к `chat.completions.create` с предопределенными сообщениями `DEFAULT_MESSAGES`, пустой строкой и указанием формата ответа `json_object`.
3. **Проверка типа ответа**: Проверяется, что полученный ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Извлекается содержимое ответа, декодируется из JSON и проверяется наличие ключа `"success"`.

```
Создание клиента (client)
↓
Отправка запроса (response)
↓
Проверка типа ответа (assertIsInstance)
↓
Проверка содержимого ответа (assertIn)
```

**Примеры**:
```python
import unittest
from g4f.client import AsyncClient
from g4f.Provider import Copilot
from g4f.client import ChatCompletion

DEFAULT_MESSAGES = [{"role": "system", "content": 'Response in json, Example: {"success": false}'},
                    {"role": "user", "content": "Say success true in json"}]

class TestChatCompletionAsync(unittest.IsolatedAsyncioTestCase):
    async def test_bing(self):
        client = AsyncClient(provider=Copilot)
        response = await client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))

if __name__ == '__main__':
    unittest.main()
```

### `TestChatCompletionAsync.test_openai`

```python
    async def test_openai(self):
        client = AsyncClient(provider=DDG)
        response = await client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))
```

**Назначение**: Асинхронно проверяет интеграцию с провайдером `DDG`. Функция создает асинхронный клиент с провайдером `DDG`, отправляет запрос и проверяет, что ответ является экземпляром `ChatCompletion` и содержит ключ `"success"` в JSON.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TestChatCompletionAsync`.

**Возвращает**: None

**Вызывает исключения**: None

**Как работает функция**:
1. **Создание клиента**: Создается экземпляр класса `AsyncClient` с указанием провайдера `DDG`.
2. **Отправка запроса**: Отправляется асинхронный запрос к `chat.completions.create` с предопределенными сообщениями `DEFAULT_MESSAGES`, пустой строкой и указанием формата ответа `json_object`.
3. **Проверка типа ответа**: Проверяется, что полученный ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Извлекается содержимое ответа, декодируется из JSON и проверяется наличие ключа `"success"`.

```
Создание клиента (client)
↓
Отправка запроса (response)
↓
Проверка типа ответа (assertIsInstance)
↓
Проверка содержимого ответа (assertIn)
```

**Примеры**:
```python
import unittest
from g4f.client import AsyncClient
from g4f.Provider import DDG
from g4f.client import ChatCompletion

DEFAULT_MESSAGES = [{"role": "system", "content": 'Response in json, Example: {"success": false}'},
                    {"role": "user", "content": "Say success true in json"}]

class TestChatCompletionAsync(unittest.IsolatedAsyncioTestCase):
    async def test_openai(self):
        client = AsyncClient(provider=DDG)
        response = await client.chat.completions.create(DEFAULT_MESSAGES, "", response_format={"type": "json_object"})
        self.assertIsInstance(response, ChatCompletion)
        self.assertIn("success", json.loads(response.choices[0].message.content))

if __name__ == '__main__':
    unittest.main()