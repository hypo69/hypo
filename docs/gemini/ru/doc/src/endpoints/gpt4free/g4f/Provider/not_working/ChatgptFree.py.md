# Модуль для работы с ChatgptFree API
=================================================

Модуль содержит класс `ChatgptFree`, который используется для взаимодействия с API ChatgptFree для генерации текста на основе предоставленных сообщений.

Пример использования
----------------------

```python
# Пример асинхронного вызова метода create_async_generator
async for message in ChatgptFree.create_async_generator(model="gpt-4o-mini-2024-07-18", messages=[{"role": "user", "content": "Hello"}]):
    print(message, end="")
```

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [ChatgptFree](#chatgptfree)
- [Функции](#функции)

## Обзор

Модуль `ChatgptFree` предоставляет асинхронный интерфейс для взаимодействия с API ChatgptFree. Он включает в себя функциональность для получения ответа от модели на основе предоставленных сообщений. Модуль использует `StreamSession` для асинхронных HTTP-запросов и предоставляет методы для обработки потоковых ответов.

## Подробней

Этот модуль позволяет взаимодействовать с API ChatgptFree, который предоставляет возможность генерации текста на основе модели `gpt-4o-mini-2024-07-18` или ее алиасов. Он автоматически получает необходимые `post_id` и `nonce` для аутентификации и отправляет запросы для генерации текста.

## Классы

### `ChatgptFree`

**Описание**: Класс `ChatgptFree` предоставляет асинхронный интерфейс для взаимодействия с API ChatgptFree.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих данные.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL API ChatgptFree.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `_post_id` (str | None): ID поста для аутентификации.
- `_nonce` (str | None): nonce для аутентификации.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini-2024-07-18`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь алиасов моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API ChatgptFree.

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
    Создает асинхронный генератор для получения ответов от API ChatgptFree.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): HTTP-прокси для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
        cookies (dict, optional): Куки для отправки в API. По умолчанию `None`.

    Returns:
        AsyncGenerator[str, None]: Асинхронный генератор, выдающий текстовые ответы от API.

    Raises:
        RuntimeError: Если не удается получить `post_id` или `nonce`.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для получения ответов от API ChatgptFree.

**Параметры**:
- `cls` (ChatgptFree): Ссылка на класс.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): HTTP-прокси для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
- `cookies` (dict, optional): Куки для отправки в API. По умолчанию `None`.

**Возвращает**:
- `AsyncGenerator[str, None]`: Асинхронный генератор, выдающий текстовые ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если не удается получить `post_id` или `nonce`.

**Как работает функция**:

1. **Инициализация**:
   - Функция `create_async_generator` принимает параметры, необходимые для взаимодействия с API ChatgptFree, такие как модель, сообщения, прокси, таймаут и куки.

2. **Получение `post_id` и `nonce`**:
   - Если `_nonce` не установлен, функция выполняет GET-запрос к главной странице (`cls.url`) для получения `post_id` и `nonce` из HTML-ответа.
   - Используются регулярные выражения для поиска `post_id` и `nonce` в HTML-коде.
   - Если `post_id` или `nonce` не найдены, вызывается исключение `RuntimeError`.

3. **Формирование данных запроса**:
   - Форматируются сообщения с использованием функции `format_prompt(messages)`.
   - Создается словарь `data`, содержащий параметры запроса, такие как `_wpnonce`, `post_id`, `url`, `action`, `message` и `bot_id`.

4. **Отправка POST-запроса и обработка ответа**:
   - Отправляется POST-запрос к API (`cls.url/wp-admin/admin-ajax.php`) с использованием `StreamSession`.
   - Обрабатывается потоковый ответ от API построчно.
   - Каждая строка декодируется из UTF-8 и очищается от пробельных символов.
   - Если строка начинается с `data: `, извлекаются данные JSON и из них извлекается содержимое (`content`) из `choices[0].delta.content`.
   - Если `content` существует, он передается в генератор с помощью `yield content`.
   - Обрабатываются ошибки декодирования JSON и пропускаются невалидные данные.

5. **Обработка завершающего буфера**:
   - После завершения потока проверяется, остался ли какой-либо текст в буфере (`buffer`).
   - Если буфер содержит данные, они пытаются быть декодированы как JSON.
   - Если декодирование успешно, и в JSON есть ключ `data`, его значение передается в генератор.
   - Если декодирование не удается, выводится сообщение об ошибке с содержимым буфера.

**ASCII Flowchart**:

```
A: Инициализация параметров (model, messages, proxy, timeout, cookies)
|
B: Проверка наличия nonce
|
+-- No --> C: Получение post_id и nonce с главной страницы
|         |
|         D: Извлечение post_id и nonce с помощью регулярных выражений
|         |
+---------/
|
E: Форматирование сообщений (prompt = format_prompt(messages))
|
F: Создание данных запроса (data)
|
G: Отправка POST-запроса к API
|
H: Обработка потокового ответа построчно
|
I: Проверка начала строки с "data: "
|
+-- Yes --> J: Извлечение JSON data
|         |
|         K: Извлечение content из data["choices"][0]["delta"]["content"]
|         |
|         L: Передача content в генератор (yield content)
|         |
+---------/
|
M: Обработка завершающего буфера (buffer)
|
N: Попытка декодирования буфера как JSON
|
O: Извлечение data из JSON и передача в генератор (yield data)
```

**Примеры**:

```python
# Пример асинхронного вызова метода create_async_generator
async def main():
    async for message in ChatgptFree.create_async_generator(model="gpt-4o-mini-2024-07-18", messages=[{"role": "user", "content": "Hello"}]):
        print(message, end="")

import asyncio
asyncio.run(main())
```

```python
# Пример использования прокси
async def main():
    async for message in ChatgptFree.create_async_generator(model="gpt-4o-mini-2024-07-18", messages=[{"role": "user", "content": "Hello"}], proxy="http://your_proxy:8080"):
        print(message, end="")

import asyncio
asyncio.run(main())