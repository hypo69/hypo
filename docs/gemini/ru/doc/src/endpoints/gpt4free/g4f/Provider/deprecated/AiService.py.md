# Модуль AiService

## Обзор

Модуль `AiService` предоставляет класс `AiService`, который является провайдером для взаимодействия с AI-моделью через `aiservice.vercel.app`. Он поддерживает модель `gpt-35-turbo` и позволяет отправлять запросы к AI-сервису для генерации ответов на основе предоставленных сообщений.

## Подробней

Этот модуль используется для интеграции с AI-сервисом, предоставляемым `aiservice.vercel.app`, и позволяет использовать его возможности для генерации текста на основе заданных сообщений. Класс `AiService` наследуется от `AbstractProvider` и реализует метод `create_completion` для отправки запросов к AI-сервису.

## Классы

### `AiService`

**Описание**: Класс `AiService` является провайдером для взаимодействия с AI-моделью через `aiservice.vercel.app`.

**Наследует**:
- `AbstractProvider`: Абстрактный базовый класс для провайдеров.

**Атрибуты**:
- `url` (str): URL AI-сервиса (`https://aiservice.vercel.app/`).
- `working` (bool): Флаг, указывающий на работоспособность сервиса (по умолчанию `False`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-35_turbo` (по умолчанию `True`).

**Методы**:
- `create_completion`: Отправляет запрос к AI-сервису для генерации ответа на основе предоставленных сообщений.

## Функции

### `create_completion`

```python
@staticmethod
def create_completion(
    model: str,
    messages: Messages,
    stream: bool,
    **kwargs: Any,
) -> CreateResult:
    """
    Отправляет запрос к AI-сервису для генерации ответа на основе предоставленных сообщений.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для AI-модели.
        stream (bool): Флаг, указывающий на потоковую передачу данных.
        **kwargs (Any): Дополнительные аргументы.

    Returns:
        CreateResult: Результат генерации ответа от AI-модели.

    Raises:
        requests.exceptions.HTTPError: Если возникает HTTP ошибка при отправке запроса.

    """
```

**Назначение**: Отправляет запрос к AI-сервису для генерации ответа на основе предоставленных сообщений.

**Параметры**:
- `model` (str): Название модели, которую нужно использовать.
- `messages` (Messages): Список сообщений, используемых для контекста AI-модели.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `**kwargs` (Any): Дополнительные параметры, которые могут быть переданы.

**Возвращает**:
- `CreateResult`: Результат генерации ответа от AI-модели.

**Вызывает исключения**:
- `requests.exceptions.HTTPError`: Если возникает HTTP ошибка при отправке запроса.

**Как работает функция**:
1. Формирует текстовое представление сообщений, объединяя роль и содержание каждого сообщения в строку.
2. Задает заголовки HTTP-запроса, включая `accept`, `content-type`, `sec-fetch-dest`, `sec-fetch-mode`, `sec-fetch-site` и `Referer`.
3. Формирует словарь `data`, содержащий текстовое представление сообщений под ключом `"input"`.
4. Отправляет POST-запрос к URL `https://aiservice.vercel.app/api/chat/answer` с заданными заголовками и данными.
5. Обрабатывает ответ от сервера, проверяя статус код и извлекая данные из JSON-ответа.
6. Генерирует ответ, возвращая данные из JSON-ответа.

```
Начало
↓
Формирование текстового запроса (messages_to_text)
↓
Установка HTTP-заголовков (set_headers)
↓
Отправка POST-запроса (send_request)
↓
Обработка ответа (handle_response)
↓
Генерация результата (yield_result)
↓
Конец
```

**Примеры**:

```python
# Пример вызова функции create_completion
model = "gpt-3.5-turbo"
messages = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I am doing well, thank you!"}
]
stream = False
kwargs = {}

# Предполагается, что AiService уже инициализирован
# result = AiService.create_completion(model, messages, stream, **kwargs)
# for item in result:
#     print(item)