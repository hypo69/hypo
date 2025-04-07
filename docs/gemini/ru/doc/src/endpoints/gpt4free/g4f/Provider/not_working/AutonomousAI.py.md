# Модуль для работы с провайдером AutonomousAI
==================================================

Модуль содержит класс `AutonomousAI`, который используется для взаимодействия с сервисом AutonomousAI для генерации текста.
Поддерживает потоковую передачу данных, системные сообщения и историю сообщений.

## Обзор

Этот модуль предоставляет асинхронный интерфейс для взаимодействия с API AutonomousAI. Он поддерживает различные модели, включая `llama`, `qwen_coder`, `hermes`, `vision` и `summary`. Модуль позволяет отправлять сообщения и получать ответы в потоковом режиме, а также поддерживает установку системных сообщений и учет истории сообщений.

## Подробнее

Модуль `AutonomousAI` предназначен для интеграции с сервисом AutonomousAI, который предоставляет доступ к различным моделям генерации текста. Он использует асинхронные запросы для эффективного взаимодействия с API и поддерживает потоковую передачу данных для уменьшения времени ожидания ответа. Расположение модуля в структуре проекта указывает на его роль как одного из провайдеров для получения ответов от AI-моделей.

## Классы

### `AutonomousAI`

**Описание**: Класс для взаимодействия с API AutonomousAI.
**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL для API AutonomousAI.
- `api_endpoints` (dict): Словарь с конечными точками API для различных моделей.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию.
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь с псевдонимами моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    stream: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API AutonomousAI.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу данных. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Как работает функция:
    1. Определяется конечная точка API на основе выбранной модели.
    2. Формируются заголовки запроса.
    3. Создается сессия `aiohttp.ClientSession` с заданными заголовками.
    4. Список сообщений преобразуется в JSON-формат и кодируется в base64.
    5. Формируются данные запроса, включая закодированное сообщение, идентификатор потока, флаг потоковой передачи и идентификатор агента AI.
    6. Отправляется POST-запрос к API с использованием `session.post`.
    7. Обрабатывается ответ от API:
        - Читаются чанки данных из ответа.
        - Если чанк содержит `data: [DONE]`, он пропускается.
        - Из каждого чанка извлекаются данные JSON.
        - Извлекается содержимое сообщения (`delta["content"]`) и возвращается через генератор.
        - Если в чанке содержится информация о причине завершения (`finish_reason`), она также возвращается через генератор.
    8. В случае ошибки декодирования JSON, она игнорируется.
    """

    # Получение конечной точки API для заданной модели
    api_endpoint = cls.api_endpoints[model]

    # Определение заголовков запроса
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'country-code': 'US',
        'origin': 'https://www.autonomous.ai',
        'referer': 'https://www.autonomous.ai/',
        'time-zone': 'America/New_York',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    # Создание асинхронной сессии для выполнения запросов
    async with ClientSession(headers=headers) as session:
        # Преобразование сообщений в JSON и кодирование в base64
        message_json = json.dumps(messages)
        encoded_message = base64.b64encode(message_json.encode()).decode(errors="ignore")

        # Формирование данных для отправки в запросе
        data = {
            "messages": encoded_message,
            "threadId": model,
            "stream": stream,
            "aiAgent": model
        }

        # Отправка асинхронного POST-запроса
        async with session.post(api_endpoint, json=data, proxy=proxy) as response:
            # Проверка статуса ответа
            await raise_for_status(response)

            # Асинхронный перебор чанков данных в ответе
            async for chunk in response.content:
                if chunk:
                    chunk_str = chunk.decode()
                    if chunk_str == "data: [DONE]":
                        continue

                    try:
                        # Удаление префикса "data: " и парсинг JSON
                        chunk_data = json.loads(chunk_str.replace("data: ", ""))
                        if "choices" in chunk_data and chunk_data["choices"]:
                            delta = chunk_data["choices"][0].get("delta", {})
                            if "content" in delta and delta["content"]:
                                yield delta["content"]
                        if "finish_reason" in chunk_data and chunk_data["finish_reason"]:
                            yield FinishReason(chunk_data["finish_reason"])
                    except json.JSONDecodeError:
                        continue

**Как работает функция**:

```
    Начало
    │
    └──  Определение конечной точки API (api_endpoint)
    │
    └──  Формирование заголовков (headers)
    │
    └──  Создание асинхронной сессии (session)
    │
    └──  Преобразование сообщений в JSON и кодирование в base64 (encoded_message)
    │
    └──  Формирование данных запроса (data)
    │
    └──  Отправка POST-запроса (response)
    │
    └──  Обработка ответа:
    │    │
    │    ├──  Чтение чанков данных (chunk)
    │    │
    │    ├──  Проверка на "data: [DONE]"
    │    │
    │    ├──  Извлечение JSON из чанка (chunk_data)
    │    │
    │    ├──  Извлечение содержимого сообщения (delta["content"])
    │    │
    │    └──  Извлечение причины завершения (finish_reason)
    │
    └──  Завершение
```

**Примеры**:

```python
# Пример вызова функции
model = "llama"
messages = [{"role": "user", "content": "Hello, how are you?"}]
proxy = None
stream = True

async def main():
    async for response in AutonomousAI.create_async_generator(model, messages, proxy, stream):
        print(response, end="")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```