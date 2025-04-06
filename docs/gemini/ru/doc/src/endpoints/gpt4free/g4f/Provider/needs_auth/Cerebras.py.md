# Модуль Cerebras

## Обзор

Модуль `Cerebras` предназначен для взаимодействия с API Cerebras Inference, предоставляя асинхронный генератор для обработки сообщений с использованием различных моделей, таких как `llama3.1-70b`, `llama3.1-8b` и `deepseek-r1-distill-llama-70b`. Он наследуется от класса `OpenaiAPI` и использует `aiohttp` для выполнения асинхронных HTTP-запросов. Этот модуль предназначен для использования в проектах, требующих доступа к моделям Cerebras Inference.

## Подробней

Модуль `Cerebras` предоставляет возможность использования моделей Cerebras Inference API. Он автоматически получает `api_key` из cookies, если он не передан явно. Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими доступа к моделям Cerebras Inference.

## Классы

### `Cerebras`

**Описание**: Класс `Cerebras` предназначен для взаимодействия с API Cerebras Inference.

**Наследует**:

- `OpenaiAPI`: Этот класс наследует функциональность от `OpenaiAPI`, предоставляя базовые методы для работы с API.

**Атрибуты**:

- `label` (str): Метка для идентификации провайдера, значение: "Cerebras Inference".
- `url` (str): URL для доступа к Cerebras Inference, значение: "https://inference.cerebras.ai/".
- `login_url` (str): URL для логина, значение: "https://cloud.cerebras.ai".
- `api_base` (str): Базовый URL для API Cerebras, значение: "https://api.cerebras.ai/v1".
- `working` (bool): Указывает, работает ли провайдер, значение: `True`.
- `default_model` (str): Модель по умолчанию, значение: "llama3.1-70b".
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:

- `create_async_generator()`: Создает асинхронный генератор для обработки сообщений с использованием Cerebras Inference API.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    cookies: Cookies = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для обработки сообщений с использованием Cerebras Inference API.

    Args:
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для обработки.
        api_key (str, optional): API ключ для доступа к Cerebras Inference API. Defaults to None.
        cookies (Cookies, optional): Cookies для аутентификации. Defaults to None.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор чанков ответа.
    """
```

**Назначение**:

Функция `create_async_generator` создает и возвращает асинхронный генератор, который используется для обработки сообщений с помощью моделей Cerebras Inference API. Она получает API-ключ либо из cookies, либо напрямую, если он передан. Затем она вызывает метод `create_async_generator` из родительского класса (`OpenaiAPI`) для фактической генерации чанков ответа.

**Параметры**:

- `cls` (class): Ссылка на класс `Cerebras`.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для обработки.
- `api_key` (str, optional): API ключ для доступа к Cerebras Inference API. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, которые будут переданы в метод `create_async_generator` родительского класса.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, выдающий чанки ответа от API.

**Как работает функция**:

1. **Проверка наличия API-ключа**: Функция проверяет, передан ли `api_key` напрямую.
2. **Получение API-ключа из cookies**: Если `api_key` не передан, функция пытается получить его из cookies домена `.cerebras.ai`.
3. **Создание сессии**: Создается асинхронная сессия `ClientSession` с использованием cookies.
4. **Получение API-ключа из сессии**: Если `api_key` не был передан напрямую, выполняется запрос к "https://inference.cerebras.ai/api/auth/session" для получения `api_key` из JSON-ответа.
5. **Вызов родительского метода**: Функция вызывает метод `create_async_generator` из родительского класса (`OpenaiAPI`) с полученным или переданным `api_key` и другими параметрами.
6. **Генерация чанков**: Асинхронный генератор возвращает чанки ответа, полученные от API.

```
Проверка API-ключа  --> Получение API-ключа из cookies --> Создание асинхронной сессии --> Получение API-ключа из сессии (если необходимо) --> Вызов родительского метода create_async_generator --> Генерация чанков
```

**Примеры**:

```python
# Пример использования функции create_async_generator
model = "llama3.1-70b"
messages = [{"role": "user", "content": "Hello, how are you?"}]
api_key = "YOUR_API_KEY"

async def main():
    async for chunk in Cerebras.create_async_generator(model=model, messages=messages, api_key=api_key):
        print(chunk)

# Запуск примера
# asyncio.run(main())