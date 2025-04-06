# Модуль `ChatgptFree`

## Обзор

Модуль `ChatgptFree` предоставляет асинхронный генератор для взаимодействия с моделью `gpt-4o-mini-2024-07-18` через сервис `chatgptfree.ai`. Он использует `StreamSession` для асинхронной потоковой передачи данных и включает в себя логику для получения `post_id` и `nonce`, необходимых для аутентификации запросов.

## Подробней

Этот модуль является частью набора провайдеров для проекта `hypotez`, предназначенных для интеграции с различными AI-сервисами. Он позволяет отправлять запросы к `chatgptfree.ai` и получать ответы в виде асинхронного генератора, что удобно для обработки больших объемов текстовых данных.

## Классы

### `ChatgptFree`

**Описание**: Класс `ChatgptFree` является асинхронным генератором провайдера и миксином модели провайдера. Он предоставляет методы для взаимодействия с сервисом `chatgptfree.ai`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL сервиса `chatgptfree.ai`.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `_post_id` (Optional[str]): ID поста, необходимый для запросов.
- `_nonce` (Optional[str]): Nonce, необходимый для аутентификации запросов.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini-2024-07-18`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь с псевдонимами моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от `chatgptfree.ai`.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    cookies: dict = None,
    **kwargs
) -> AsyncGenerator[str, None]:
    """
    Создает асинхронный генератор для получения ответов от `chatgptfree.ai`.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
        cookies (dict, optional): Cookie для отправки. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncGenerator[str, None]: Асинхронный генератор, выдающий ответы от `chatgptfree.ai`.

    Raises:
        RuntimeError: Если не удается найти `post_id` или `nonce`.
        Exception: Если возникает ошибка при выполнении HTTP-запроса.
    """
```

**Назначение**: Создает асинхронный генератор, который взаимодействует с сервисом `chatgptfree.ai` для получения ответов на основе предоставленных сообщений.

**Параметры**:
- `cls` (ChatgptFree): Ссылка на класс `ChatgptFree`.
- `model` (str): Название модели, которую нужно использовать для генерации ответа.
- `messages (Messages)`: Список сообщений, которые будут отправлены в запросе.
- `proxy` (str, optional): URL прокси-сервера, который будет использоваться для выполнения запроса. По умолчанию `None`.
- `timeout` (int, optional): Максимальное время ожидания ответа от сервера в секундах. По умолчанию `120`.
- `cookies` (dict, optional): Cookie, которые будут отправлены в запросе. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в функцию.

**Возвращает**:
- `AsyncGenerator[str, None]`: Асинхронный генератор, который выдает текстовые фрагменты ответа от `chatgptfree.ai`.

**Вызывает исключения**:
- `RuntimeError`: Вызывается, если не удается извлечь `post_id` или `nonce` из HTML-ответа.
- `Exception`: Вызывается в случае ошибок при выполнении HTTP-запросов или при обработке данных.

**Как работает функция**:
1. **Настройка заголовков**: Функция задает необходимые HTTP-заголовки для запроса, включая `authority`, `accept`, `user-agent` и другие.
2. **Инициализация сессии**: Используется `StreamSession` для асинхронного управления HTTP-сессией с возможностью использования прокси и таймаута.
3. **Получение `post_id` и `nonce`**: Если `_post_id` или `_nonce` не установлены, функция выполняет GET-запрос к главной странице `chatgptfree.ai` и извлекает значения `post_id` и `nonce` из HTML-кода страницы с использованием регулярных выражений.
4. **Форматирование запроса**: Подготавливает данные для POST-запроса, включая `_wpnonce`, `post_id`, `url`, `action`, `message` (сформированное из входных сообщений) и `bot_id`.
5. **Отправка POST-запроса**: Отправляет асинхронный POST-запрос к `chatgptfree.ai/wp-admin/admin-ajax.php` с данными запроса.
6. **Обработка потока ответов**: Функция читает ответ построчно, декодирует каждую строку и извлекает содержимое из JSON-данных, если строка начинается с `data: `. Если строка содержит `[DONE]`, генерация завершается.
7. **Обработка буфера**: Если после завершения потока остается непустой буфер, функция пытается декодировать его как JSON и извлечь данные из поля `data`.
8. **Генерация результатов**: Функция использует `yield content` для выдачи фрагментов ответа в виде асинхронного генератора.

**Внутренние функции**:
- Нет внутренних функций.

```
Настройка заголовков    ->  GET запрос для извлечения post_id и nonce
     |                       (если _nonce не установлен)
     ↓                       |
Инициализация сессии     ->  Извлечение post_id и nonce из HTML
     |                       |   (с использованием регулярных выражений)
     ↓                       |
Форматирование запроса    ->  Обработка ошибок извлечения
     |                       |   (если не найдены post_id и nonce)
     ↓                       |
Отправка POST-запроса     ->  Формирование данных для POST запроса
     |                       |   (включая nonce, post_id, url, action, message, bot_id)
     ↓                       |
Обработка потока ответов ->  Отправка POST запроса к admin-ajax.php
     |                       |   (с использованием StreamSession)
     ↓                       |
Обработка буфера        ->  Чтение ответа построчно
     |                       |   (декодирование и обработка JSON)
     ↓                       |
Генерация результатов     ->  Извлечение содержимого из JSON (если строка начинается с 'data: ')
                             |   (и выдача фрагментов ответа через yield)
                             |
                             ->  Обработка завершающего буфера (если есть)
```

**Примеры**:

```python
# Пример использования асинхронного генератора
import asyncio

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages = [{"role": "user", "content": "Tell me a joke."}]
    async for message in ChatgptFree.create_async_generator(model=model, messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример использования с прокси
import asyncio

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages = [{"role": "user", "content": "Tell me a joke."}]
    proxy = "http://your_proxy:8080"
    async for message in ChatgptFree.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример использования с таймаутом и cookie
import asyncio

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages = [{"role": "user", "content": "Tell me a joke."}]
    timeout = 60
    cookies = {"cookie_name": "cookie_value"}
    async for message in ChatgptFree.create_async_generator(model=model, messages=messages, timeout=timeout, cookies=cookies):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())