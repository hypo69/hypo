# Модуль `ChatGLM`

## Обзор

Модуль `ChatGLM` предоставляет асинхронную интеграцию с сервисом ChatGLM для генерации текста. Он включает в себя функциональность для отправки запросов к API ChatGLM и получения ответов в виде асинхронного генератора. Модуль поддерживает стриминг ответов, что позволяет получать текст по частям в режиме реального времени.

## Подробней

Этот модуль позволяет взаимодействовать с API ChatGLM (<https://chatglm.cn>) для генерации текста на основе предоставленных сообщений. Он использует асинхронные запросы (`aiohttp`) для обеспечения неблокирующего взаимодействия с API. Модуль также обрабатывает ответы в формате `text/event-stream`, извлекая текстовое содержимое и возвращая его в виде генератора.

## Классы

### `ChatGLM`

**Описание**: Класс `ChatGLM` является асинхронным провайдером, который реализует взаимодействие с API ChatGLM. Он предоставляет методы для создания асинхронных генераторов, отправляющих запросы и получающих ответы от API ChatGLM.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, возвращающих генераторы.
- `ProviderModelMixin`: Добавляет поддержку выбора модели.

**Атрибуты**:
- `url` (str): URL сервиса ChatGLM (`https://chatglm.cn`).
- `api_endpoint` (str): URL API endpoint для взаимодействия (`https://chatglm.cn/chatglm/mainchat-api/guest/stream`).
- `working` (bool): Флаг, указывающий, что провайдер работает (`True`).
- `supports_stream` (bool): Флаг, указывающий, что провайдер поддерживает стриминг (`True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (`False`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (`False`).
- `default_model` (str): Модель, используемая по умолчанию (`glm-4`).
- `models` (list): Список поддерживаемых моделей (`[default_model]`).

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API ChatGLM.

    Args:
        model (str): Имя модели, которую следует использовать.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текстовые фрагменты из API.

    Raises:
        Exception: В случае ошибок при взаимодействии с API.
    """
```

**Назначение**: Создает асинхронный генератор, который отправляет сообщения в API ChatGLM и возвращает ответы в виде текстовых фрагментов.

**Параметры**:
- `cls`: Ссылка на класс `ChatGLM`.
- `model` (str): Имя модели, которую следует использовать.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текстовые фрагменты из API.

**Как работает функция**:
1. Генерирует уникальный `device_id` для идентификации устройства.
2. Определяет заголовки HTTP-запроса, включая `Content-Type`, `User-Agent` и `X-Device-Id`.
3. Создает асинхронную сессию `ClientSession` с заданными заголовками.
4. Формирует JSON-данные для отправки в API, включая `assistant_id`, `conversation_id`, `meta_data` и `messages`.
5. Отправляет POST-запрос к `api_endpoint` с использованием асинхронной сессии и прокси (если указан).
6. Обрабатывает ответ от API, декодируя чанки данных и извлекая текстовое содержимое из JSON.
7. Генерирует текстовые фрагменты, возвращая их через `yield`.
8. Если статус ответа равен `'finish'`, генерирует `FinishReason("stop")`.

**Внутренние функции**: Нет.

**ASCII flowchart**:

```
A [Генерация device_id]
    ↓
B [Определение headers]
    ↓
C [Создание ClientSession]
    ↓
D [Формирование JSON data]
    ↓
E [Отправка POST запроса]
    ↓
F [Обработка ответа]
    ↓
G [Извлечение текста]
    ↓
H [Генерация текста или FinishReason]
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Привет, как дела?"}]
async def main():
    async for text in ChatGLM.create_async_generator(model="glm-4", messages=messages):
        print(text)
```
```python
# Использование с прокси
messages = [{"role": "user", "content": "Привет, как дела?"}]
async def main():
    async for text in ChatGLM.create_async_generator(model="glm-4", messages=messages, proxy="http://proxy.example.com"):
        print(text)