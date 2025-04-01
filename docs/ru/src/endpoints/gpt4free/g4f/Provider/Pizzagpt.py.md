# Модуль Pizzagpt

## Обзор

Модуль `Pizzagpt` предоставляет асинхронный интерфейс для взаимодействия с API pizzagpt.it. Он позволяет генерировать ответы на основе предоставленных сообщений, используя модель `gpt-4o-mini`. Модуль включает поддержку прокси и обработку ошибок.

## Подробней

Модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется взаимодействие с сервисом pizzagpt.it для получения ответов на запросы.
Он использует `aiohttp` для асинхронных HTTP-запросов и предоставляет класс `Pizzagpt`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

## Классы

### `Pizzagpt`

**Описание**: Класс для взаимодействия с API pizzagpt.it.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса pizzagpt.it.
- `api_endpoint` (str): Endpoint API для запросов.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `models` (List[str]): Список поддерживаемых моделей.

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
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от API pizzagpt.it.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API.

        Raises:
            ValueError: Если обнаружено сообщение о злоупотреблении.
            Exception: При возникновении ошибок HTTP запроса.

        """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API pizzagpt.it и получения ответов на основе предоставленных сообщений.

**Параметры**:
- `model` (str): Модель, используемая для генерации ответа.
- `messages` (Messages): Список сообщений, отправляемых в API для получения ответа.
- `proxy` (str, optional): URL прокси-сервера для использования при отправке запроса. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `ValueError`: Если обнаружено сообщение о злоупотреблении ("Misuse detected. please get in touch").

**Как работает функция**:

1. **Подготовка заголовков**: Функция создает заголовки HTTP-запроса, включая `accept`, `accept-language`, `content-type`, `origin`, `referer`, `user-agent` и `x-secret`. Заголовки содержат информацию о клиенте и типе контента.
2. **Создание сессии**: Используется `aiohttp.ClientSession` для выполнения асинхронных HTTP-запросов.
3. **Форматирование запроса**: Форматирует сообщения с использованием `format_prompt` для подготовки данных для отправки в API.
4. **Отправка запроса**: Отправляет POST-запрос к API pizzagpt.it с использованием `session.post`. Запрос включает JSON-данные с вопросом (prompt) и использует прокси, если он указан.
5. **Обработка ответа**:
   - Проверяет статус ответа и вызывает исключение `response.raise_for_status()`, если произошла ошибка.
   - Извлекает JSON из ответа и получает содержимое ответа из поля `answer.content`.
6. **Генерация ответа**:
   - Если содержимое ответа существует, функция проверяет, не содержит ли оно сообщение о злоупотреблении. Если такое сообщение обнаружено, вызывается исключение `ValueError`.
   - Выдает содержимое ответа с использованием `yield content`.
   - Завершает генерацию, выдавая сигнал `FinishReason("stop")`.

```
Подготовка заголовков --> Создание сессии
   ↓
Форматирование запроса --> Отправка запроса
   ↓
Обработка ответа --> Проверка содержимого --> Генерация ответа
```

**Примеры**:

```python
# Пример 1: Базовый вызов функции
async for message in Pizzagpt.create_async_generator(model='gpt-4o-mini', messages=[{'role': 'user', 'content': 'Hello'}]):
    print(message)

# Пример 2: Использование прокси
async for message in Pizzagpt.create_async_generator(model='gpt-4o-mini', messages=[{'role': 'user', 'content': 'Как дела?'}], proxy='http://proxy.example.com'):
    print(message)

# Пример 3: Обработка ошибки ValueError
try:
    async for message in Pizzagpt.create_async_generator(model='gpt-4o-mini', messages=[{'role': 'user', 'content': 'злоупотребление'}], proxy='http://proxy.example.com'):
        print(message)
except ValueError as ex:
    print(f"Ошибка: {ex}")