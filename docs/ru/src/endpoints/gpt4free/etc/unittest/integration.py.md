# Модуль интеграционного тестирования провайдеров gpt4free
## Обзор

Модуль содержит интеграционные тесты для проверки работоспособности различных провайдеров, используемых в библиотеке `gpt4free`. Он проверяет взаимодействие с провайдерами Copilot и DDG (DuckDuckGo) как в синхронном, так и в асинхронном режимах.

## Подробней

Этот модуль предназначен для автоматической проверки интеграции с различными поставщиками услуг, используемыми в проекте `gpt4free`. Он использует библиотеку `unittest` для создания и запуска тестов, которые проверяют, что ответы от провайдеров соответствуют ожидаемому формату и содержат ожидаемые данные. Тесты охватывают как синхронные, так и асинхронные вызовы к API провайдеров.

## Классы

### `TestProviderIntegration`

**Описание**: Класс, содержащий интеграционные тесты для синхронных вызовов к провайдерам.

**Наследует**:
- `unittest.TestCase`: Предоставляет методы для написания тестовых случаев.

**Методы**:
- `test_bing()`: Проверяет интеграцию с провайдером Copilot.
- `test_openai()`: Проверяет интеграцию с провайдером DDG (DuckDuckGo).

### `TestChatCompletionAsync`

**Описание**: Класс, содержащий интеграционные тесты для асинхронных вызовов к провайдерам.

**Наследует**:
- `unittest.IsolatedAsyncioTestCase`: Предоставляет методы для написания асинхронных тестовых случаев.

**Методы**:
- `test_bing()`: Асинхронно проверяет интеграцию с провайдером Copilot.
- `test_openai()`: Асинхронно проверяет интеграцию с провайдером DDG (DuckDuckGo).

## Функции

### `test_bing` (в классе `TestProviderIntegration`)

```python
    def test_bing(self):
        """Проверяет интеграцию с провайдером Copilot."""
```

**Назначение**: Проверяет, что интеграция с провайдером Copilot работает корректно при синхронном вызове.

**Как работает функция**:

1. **Создание клиента**: Создается экземпляр класса `Client` с указанием провайдера `Copilot`.
2. **Вызов API**: Вызывается метод `client.chat.completions.create` с предопределенными сообщениями (`DEFAULT_MESSAGES`), пустой строкой и указанием формата ответа (`response_format={"type": "json_object"}`).
3. **Проверка типа ответа**: Проверяется, что ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Проверяется, что в JSON-ответе содержится ключ `"success"`.

```
Создание клиента
     ↓
Вызов API → Получение ответа
     ↓
Проверка типа ответа
     ↓
Проверка содержимого ответа
```

**Примеры**:
```python
# Пример использования test_bing
test_case = TestProviderIntegration()
test_case.test_bing()
```

### `test_openai` (в классе `TestProviderIntegration`)

```python
    def test_openai(self):
        """Проверяет интеграцию с провайдером DDG (DuckDuckGo)."""
```

**Назначение**: Проверяет, что интеграция с провайдером DDG работает корректно при синхронном вызове.

**Как работает функция**:

1. **Создание клиента**: Создается экземпляр класса `Client` с указанием провайдера `DDG`.
2. **Вызов API**: Вызывается метод `client.chat.completions.create` с предопределенными сообщениями (`DEFAULT_MESSAGES`), пустой строкой и указанием формата ответа (`response_format={"type": "json_object"}`).
3. **Проверка типа ответа**: Проверяется, что ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Проверяется, что в JSON-ответе содержится ключ `"success"`.

```
Создание клиента
     ↓
Вызов API → Получение ответа
     ↓
Проверка типа ответа
     ↓
Проверка содержимого ответа
```

**Примеры**:
```python
# Пример использования test_openai
test_case = TestProviderIntegration()
test_case.test_openai()
```

### `test_bing` (в классе `TestChatCompletionAsync`)

```python
    async def test_bing(self):
        """Асинхронно проверяет интеграцию с провайдером Copilot."""
```

**Назначение**: Проверяет, что интеграция с провайдером Copilot работает корректно при асинхронном вызове.

**Как работает функция**:

1. **Создание клиента**: Создается экземпляр класса `AsyncClient` с указанием провайдера `Copilot`.
2. **Вызов API**: Вызывается метод `client.chat.completions.create` с предопределенными сообщениями (`DEFAULT_MESSAGES`), пустой строкой и указанием формата ответа (`response_format={"type": "json_object"}`).
3. **Проверка типа ответа**: Проверяется, что ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Проверяется, что в JSON-ответе содержится ключ `"success"`.

```
Создание клиента
     ↓
Вызов API → Получение ответа
     ↓
Проверка типа ответа
     ↓
Проверка содержимого ответа
```

**Примеры**:
```python
# Пример использования test_bing
import asyncio
test_case = TestChatCompletionAsync()
asyncio.run(test_case.test_bing())
```

### `test_openai` (в классе `TestChatCompletionAsync`)

```python
    async def test_openai(self):
        """Асинхронно проверяет интеграцию с провайдером DDG (DuckDuckGo)."""
```

**Назначение**: Проверяет, что интеграция с провайдером DDG работает корректно при асинхронном вызове.

**Как работает функция**:

1. **Создание клиента**: Создается экземпляр класса `AsyncClient` с указанием провайдера `DDG`.
2. **Вызов API**: Вызывается метод `client.chat.completions.create` с предопределенными сообщениями (`DEFAULT_MESSAGES`), пустой строкой и указанием формата ответа (`response_format={"type": "json_object"}`).
3. **Проверка типа ответа**: Проверяется, что ответ является экземпляром класса `ChatCompletion`.
4. **Проверка содержимого ответа**: Проверяется, что в JSON-ответе содержится ключ `"success"`.

```
Создание клиента
     ↓
Вызов API → Получение ответа
     ↓
Проверка типа ответа
     ↓
Проверка содержимого ответа
```

**Примеры**:
```python
# Пример использования test_openai
import asyncio
test_case = TestChatCompletionAsync()
asyncio.run(test_case.test_openai())
```

### `__main__`

```python
if __name__ == '__main__':
    unittest.main()
```

**Назначение**: Обеспечивает запуск тестов при непосредственном выполнении скрипта.

**Как работает**:
- Если скрипт запускается напрямую (а не импортируется как модуль), то выполняется функция `unittest.main()`, которая автоматически обнаруживает и запускает все тесты, определенные в модуле.