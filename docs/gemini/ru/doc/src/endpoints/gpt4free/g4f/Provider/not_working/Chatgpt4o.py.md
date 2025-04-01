# Модуль для работы с провайдером Chatgpt4o
=================================================

Модуль содержит класс `Chatgpt4o`, который является асинхронным провайдером для взаимодействия с моделью gpt-4o-mini-2024-07-18.
Этот модуль предназначен для интеграции с API chatgpt4o.one.

## Обзор

Модуль `Chatgpt4o.py` предоставляет функциональность для взаимодействия с сервисом `chatgpt4o.one`. Он включает в себя асинхронный класс `Chatgpt4o`, который позволяет отправлять запросы к API и получать ответы. Модуль также содержит настройки по умолчанию для модели и URL, а также методы для обработки ответов и ошибок.

## Подробнее

Модуль предназначен для использования в асинхронных приложениях, где требуется взаимодействие с моделью `gpt-4o-mini-2024-07-18` через API `chatgpt4o.one`. Он автоматически получает `post_id` и `nonce`, необходимые для аутентификации запросов.

## Классы

### `Chatgpt4o`

**Описание**:
Асинхронный провайдер для взаимодействия с API `chatgpt4o.one`.

**Наследует**:
- `AsyncProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса `chatgpt4o.one`.
- `working` (bool): Указывает, работает ли провайдер.
- `_post_id` (Optional[str]): ID поста, необходимого для запросов.
- `_nonce` (Optional[str]): Nonce, необходимый для запросов.
- `default_model` (str): Модель по умолчанию (`gpt-4o-mini-2024-07-18`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Псевдонимы моделей.

**Методы**:
- `create_async`: Асинхронный метод для создания запроса к API и получения ответа.

## Функции

### `create_async`

```python
    @classmethod
    async def create_async(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 120,
        cookies: dict = None,
        **kwargs
    ) -> str:
        """ Асинхронно создает запрос к API chatgpt4o.one и возвращает ответ.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
            cookies (dict, optional): Cookie для отправки с запросом. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Returns:
            str: Ответ от API в формате JSON.

        Raises:
            RuntimeError: Если не найден `post_id` или `nonce`, или если ответ не содержит поле `data`.
        """
```

**Назначение**:
Асинхронно создает запрос к API `chatgpt4o.one` и возвращает ответ.

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию 120.
- `cookies` (dict, optional): Cookie для отправки с запросом. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `str`: Ответ от API в формате JSON.

**Вызывает исключения**:
- `RuntimeError`: Если не найден `post_id` или `nonce`, или если ответ не содержит поле `data`.

**Как работает функция**:

1. **Определение заголовков**: Определяются заголовки HTTP-запроса, включая User-Agent, Referer и другие необходимые параметры.
2. **Создание сессии**: Создается асинхронная сессия с использованием `StreamSession` для выполнения HTTP-запросов. Устанавливаются параметры прокси и таймаут.
3. **Получение `post_id` и `nonce`**: Если `post_id` или `nonce` не установлены, функция выполняет GET-запрос к главной странице `chatgpt4o.one`, чтобы извлечь эти значения из HTML-кода страницы.
4. **Формирование данных запроса**: Формируются данные для POST-запроса, включая `_wpnonce`, `post_id`, URL, действие (`action`) и сообщение (`message`).
5. **Отправка POST-запроса**: Выполняется POST-запрос к `chatgpt4o.one/wp-admin/admin-ajax.php` с сформированными данными.
6. **Обработка ответа**: Проверяется наличие поля `data` в JSON-ответе. Если поле отсутствует, выбрасывается исключение `RuntimeError`.
7. **Возврат результата**: Возвращается значение поля `data` из JSON-ответа.

```
A: Определение заголовков и создание сессии
|
B: Проверка наличия post_id и nonce
|
C: Получение post_id и nonce (если необходимо)
|
D: Формирование данных запроса
|
E: Отправка POST-запроса
|
F: Обработка и возврат ответа
```

**Примеры**:

Пример 1: Базовый вызов функции

```python
import asyncio
from typing import List, Dict

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]
    result = await Chatgpt4o.create_async(model=model, messages=messages)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

Пример 2: Вызов функции с прокси и cookies

```python
import asyncio
from typing import List, Dict

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Tell me a joke."}]
    proxy = "http://your-proxy-server:8080"
    cookies = {"session_id": "12345"}
    result = await Chatgpt4o.create_async(model=model, messages=messages, proxy=proxy, cookies=cookies)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())