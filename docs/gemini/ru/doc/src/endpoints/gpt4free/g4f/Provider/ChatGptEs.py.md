# Модуль `ChatGptEs`

## Обзор

Модуль `ChatGptEs` предоставляет асинхронный генератор для взаимодействия с сервисом ChatGptEs. Он использует библиотеку `curl_cffi` для обхода защиты Cloudflare и отправки запросов к API. Модуль поддерживает потоковую передачу данных и предоставляет методы для формирования запросов и обработки ответов.

## Подробней

Модуль предназначен для интеграции с другими частями проекта `hypotez` для обеспечения взаимодействия с ChatGptEs. Он обеспечивает асинхронное взаимодействие с API, что позволяет избежать блокировки основного потока выполнения. Для работы модуля требуется установленная библиотека `curl_cffi`.

## Классы

### `ChatGptEs`

**Описание**: Класс `ChatGptEs` является поставщиком асинхронного генератора для взаимодействия с ChatGptEs.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса ChatGptEs (`https://chatgpt.es`).
- `api_endpoint` (str): URL API сервиса ChatGptEs (`https://chatgpt.es/wp-admin/admin-ajax.php`).
- `working` (bool): Указывает, работает ли провайдер (значение `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (значение `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (значение `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (значение `False`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o`).
- `models` (List[str]): Список поддерживаемых моделей (`['gpt-4', 'gpt-4o', 'gpt-4o-mini']`).
- `SYSTEM_PROMPT` (str): Системное сообщение, используемое для форматирования запроса.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с ChatGptEs.

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
    """Создает асинхронный генератор для взаимодействия с ChatGptEs.

    Args:
        cls (ChatGptEs): Ссылка на класс.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для получения ответов от ChatGptEs.

    Raises:
        MissingRequirementsError: Если не установлена библиотека `curl_cffi`.
        ValueError: Если получен неожиданный формат ответа или произошла ошибка при запросе.
    """
    ...
```

**Назначение**: Создает асинхронный генератор для взаимодействия с ChatGptEs.

**Параметры**:
- `cls` (ChatGptEs): Ссылка на класс.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от ChatGptEs.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлена библиотека `curl_cffi`.
- `ValueError`: Если получен неожиданный формат ответа или произошла ошибка при запросе.

**Как работает функция**:
1. **Проверка зависимостей**: Проверяет, установлена ли библиотека `curl_cffi`. Если нет, вызывает исключение `MissingRequirementsError`.
2. **Формирование запроса**: Форматирует запрос на основе переданных сообщений и системного промпта.
3. **Создание сессии**: Создает сессию `curl_cffi` для выполнения запросов с автоматическим обходом Cloudflare.
4. **Настройка заголовков**: Устанавливает необходимые заголовки для запроса, такие как `user-agent`, `referer`, `origin` и `content-type`.
5. **Настройка прокси**: Если передан прокси-сервер, устанавливает его для сессии.
6. **Получение `nonce` и `post_id`**: Выполняет первый GET-запрос к `cls.url` для получения значений `nonce` и `post_id` из HTML-кода страницы.
7. **Извлечение `nonce`**: Использует регулярные выражения для извлечения значения `nonce` из HTML-кода. Если `nonce` не найден, используется значение по умолчанию.
8. **Извлечение `post_id`**: Использует регулярные выражения для извлечения значения `post_id` из HTML-кода. Если `post_id` не найден, используется значение по умолчанию ("106").
9. **Генерация `client_id`**: Генерирует случайный `client_id`.
10. **Подготовка данных**: Формирует словарь `data` с параметрами запроса, включая `_wpnonce`, `post_id`, `url`, `action`, `message`, `bot_id`, `chatbot_identity`, `wpaicg_chat_client_id` и `wpaicg_chat_history`.
11. **Выполнение POST-запроса**: Выполняет POST-запрос к `cls.api_endpoint` с переданными данными.
12. **Обработка ответа**: Проверяет статус код ответа. Если статус код не равен 200, вызывает исключение `ValueError`.
13. **Извлечение результата**: Извлекает данные из JSON-ответа и возвращает их в виде генератора. Если в ответе содержится сообщение об ошибке (например, "Du musst das Kästchen anklicken!"), вызывает исключение `ValueError`.

```
Логическая схема работы функции:

A: Проверка зависимостей (curl_cffi)
|
B: Формирование запроса
|
C: Создание сессии curl_cffi и настройка заголовков
|
D: Настройка прокси (если указан)
|
E: Получение nonce и post_id из HTML
|
F: Подготовка данных для POST-запроса
|
G: Выполнение POST-запроса к API
|
H: Обработка ответа и извлечение данных
|
I: Возврат данных в виде генератора или исключения
```

**Примеры**:

```python
# Пример вызова функции create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gpt-4o"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]
    proxy = None

    try:
        generator: AsyncGenerator[str, None] = await ChatGptEs.create_async_generator(model, messages, proxy)
        async for message in generator:
            print(f"Response: {message}")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

В данном примере демонстрируется вызов функции `create_async_generator` с указанием модели, списка сообщений и прокси-сервера (в данном случае `None`). Результат выводится в консоль.
```python
# Пример вызова с прокси
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gpt-4o"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Привет, как дела?"}]
    proxy = "http://your_proxy:8080"

    try:
        generator: AsyncGenerator[str, None] = await ChatGptEs.create_async_generator(model, messages, proxy)
        async for message in generator:
            print(f"Response: {message}")
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

В данном примере демонстрируется вызов функции `create_async_generator` с использованием прокси-сервера.

### `get_model`

```python
    @classmethod
    def get_model(cls, model: str | None = None) -> str:
        """
        Получает имя модели. Если `model` не указан, возвращается `default_model`.

        Args:
            model (str | None, optional): Имя модели. По умолчанию `None`.

        Returns:
            str: Имя модели.
        """
        return model if model in cls.models else cls.default_model
```

**Назначение**: Получает имя модели. Если `model` не указан, возвращается `default_model`.

**Параметры**:
- `model` (str | None, optional): Имя модели. По умолчанию `None`.

**Возвращает**:
- `str`: Имя модели.

**Как работает функция**:

1. Проверяет, входит ли переданный параметр `model` в список допустимых моделей `cls.models`.
2. Если `model` входит в список, функция возвращает значение `model`.
3. Если `model` не входит в список или имеет значение `None`, функция возвращает значение `cls.default_model`.

```
Логическая схема работы функции:
A: Проверка наличия model в списке допустимых моделей
|
B: Возврат model (если model в списке) или default_model (если model не в списке)
```

**Примеры**:
```python
# Пример 1: Использование допустимой модели
model_name = ChatGptEs.get_model("gpt-4")
print(model_name)  # Вывод: gpt-4
```

```python
# Пример 2: Использование недопустимой модели
model_name = ChatGptEs.get_model("gpt-5")
print(model_name)  # Вывод: gpt-4o
```

```python
# Пример 3: Использование модели по умолчанию
model_name = ChatGptEs.get_model()
print(model_name) # Вывод: gpt-4o
```