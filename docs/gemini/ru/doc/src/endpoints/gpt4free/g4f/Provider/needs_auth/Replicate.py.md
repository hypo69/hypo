# Модуль Replicate

## Обзор

Модуль `Replicate` предназначен для взаимодействия с платформой Replicate, предоставляющей доступ к различным моделям машинного обучения. Он позволяет генерировать текст на основе предоставленных сообщений, используя API Replicate. Модуль поддерживает как асинхронный потоковый режим генерации, так и работу через прокси.

## Подробней

Этот модуль является частью проекта `hypotez` и обеспечивает интеграцию с платформой Replicate для выполнения задач, связанных с генерацией текста на основе моделей машинного обучения. Он использует асинхронные запросы для эффективного взаимодействия с API Replicate, поддерживая потоковую передачу данных для уменьшения задержек и улучшения производительности.

## Классы

### `Replicate`

**Описание**: Класс `Replicate` является асинхронным генераторным провайдером и миксином для моделей. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет ему асинхронно генерировать данные и управлять моделями.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями, такие как получение модели по умолчанию.

**Атрибуты**:
- `url` (str): URL главной страницы Replicate.
- `login_url` (str): URL страницы для получения API-токенов Replicate.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для работы с провайдером.
- `default_model` (str): Модель, используемая по умолчанию, если не указана другая.
- `models` (list[str]): Список поддерживаемых моделей.

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        api_key: str = None,
        proxy: str = None,
        timeout: int = 180,
        system_prompt: str = None,
        max_tokens: int = None,
        temperature: float = None,
        top_p: float = None,
        top_k: float = None,
        stop: list = None,
        extra_data: dict = {},\
        headers: dict = {\
            "accept": "application/json",\
        },\
        **kwargs\
    ) -> AsyncResult:
        ...
```

**Назначение**: Создает асинхронный генератор для получения ответов от API Replicate.

**Параметры**:
- `cls` (Replicate): Ссылка на класс `Replicate`.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки в модель.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Адрес прокси-сервера. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания ответа от сервера в секундах. По умолчанию `180`.
- `system_prompt` (str, optional): Системное сообщение для модели. По умолчанию `None`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
- `temperature` (float, optional): Температура для управления случайностью генерации. По умолчанию `None`.
- `top_p` (float, optional): Top-p вероятность для выбора токенов. По умолчанию `None`.
- `top_k` (float, optional): Top-k количество токенов для выбора. По умолчанию `None`.
- `stop` (list[str], optional): Список стоп-слов, при появлении которых генерация прекращается. По умолчанию `None`.
- `extra_data` (dict, optional): Дополнительные параметры для отправки в запросе. По умолчанию `{}`.
- `headers` (dict, optional): Дополнительные HTTP-заголовки для запроса. По умолчанию `{"accept": "application/json"}`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст от модели.

**Вызывает исключения**:
- `MissingAuthError`: Если `needs_auth` установлено в `True`, а `api_key` не предоставлен.
- `ResponseError`: Если получен некорректный ответ от API.

**Как работает функция**:

1. **Подготовка параметров**:
   - Извлекается модель с использованием `cls.get_model(model)`.
   - Проверяется наличие API-ключа, если требуется аутентификация. Если ключ отсутствует, вызывается исключение `MissingAuthError`.

2. **Формирование заголовков и URL**:
   - Формируются заголовки запроса, включая API-ключ, если он предоставлен.
   - Определяется базовый URL для API в зависимости от наличия API-ключа.

3. **Создание асинхронной сессии**:
   - Создается асинхронная сессия с использованием `StreamSession` для выполнения HTTP-запросов с поддержкой прокси и таймаутов.

4. **Формирование данных запроса**:
   - Формируются данные для отправки в запросе, включая:
     - `stream`: Устанавливается в `True` для потоковой передачи данных.
     - `input`: Параметры для модели, такие как `prompt` (сформированный из сообщений), `system_prompt`, `max_new_tokens`, `temperature`, `top_p`, `top_k` и `stop_sequences`.

5. **Отправка запроса и обработка ответа**:
   - Отправляется POST-запрос к API Replicate с сформированными данными.
   - Проверяется статус ответа и вызывается исключение `ResponseError` в случае ошибки.
   - Извлекается `id` из JSON-ответа. Если `id` отсутствует, вызывается исключение `ResponseError`.

6. **Получение потока данных**:
   - Отправляется GET-запрос к URL потока (`result["urls"]["stream"]`) для получения потока данных от API.
   - Итерируется по строкам ответа, обрабатывая события `event`:
     - Если `event` равен `b"done"`, генерация завершается.
     - Если `event` равен `b"output"`, извлекается текст из строки данных (`line[6:].decode()`) и передается в генератор (`yield new_text`).

```text
Подготовка параметров
     │
     │api_key?
     ├── Да ── Формирование заголовков и URL
     │    │
     │    └── Создание асинхронной сессии
     │    │
     │    └── Формирование данных запроса
     │    │
     │    └── Отправка запроса и обработка ответа
     │    │
     │    └── Получение потока данных
     │    │
     └── Нет ── Вызов исключения MissingAuthError
```

**Примеры**:

```python
# Пример использования с API-ключом
api_key = "YOUR_API_KEY"
messages = [{"role": "user", "content": "Напиши стихотворение о весне."}]
async for chunk in Replicate.create_async_generator(model="meta/meta-llama-3-70b-instruct", messages=messages, api_key=api_key):
    print(chunk, end="")

# Пример использования с прокси
api_key = "YOUR_API_KEY"
messages = [{"role": "user", "content": "Расскажи о космосе."}]
async for chunk in Replicate.create_async_generator(model="meta/meta-llama-3-70b-instruct", messages=messages, api_key=api_key, proxy="http://your.proxy:8080"):
    print(chunk, end="")

# Пример использования с дополнительными параметрами
api_key = "YOUR_API_KEY"
messages = [{"role": "user", "content": "Переведи на английский: Привет, мир!"}]
extra_data = {"language": "english"}
async for chunk in Replicate.create_async_generator(model="meta/meta-llama-3-70b-instruct", messages=messages, api_key=api_key, extra_data=extra_data):
    print(chunk, end="")