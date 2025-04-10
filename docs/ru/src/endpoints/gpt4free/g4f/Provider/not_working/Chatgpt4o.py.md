# Модуль для работы с асинхронным провайдером Chatgpt4o
========================================================

Модуль содержит класс `Chatgpt4o`, который является асинхронным провайдером для взаимодействия с моделью `gpt-4o-mini-2024-07-18`.

## Обзор

Этот модуль предназначен для асинхронного взаимодействия с сервисом `chatgpt4o.one`. Он предоставляет функциональность для отправки сообщений и получения ответов от языковой модели `gpt-4o-mini-2024-07-18`.

## Подробней

Модуль использует `StreamSession` для выполнения асинхронных HTTP-запросов и включает в себя методы для получения идентификатора поста и nonce, необходимых для аутентификации.

## Классы

### `Chatgpt4o`

**Описание**: Класс `Chatgpt4o` является асинхронным провайдером, предназначенным для взаимодействия с моделью `gpt-4o-mini-2024-07-18` через сервис `chatgpt4o.one`.

**Наследует**:
- `AsyncProvider`: Обеспечивает базовую структуру для асинхронных провайдеров.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса `chatgpt4o.one`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `False`).
- `_post_id` (str): Идентификатор поста, необходимый для запросов.
- `_nonce` (str): Nonce, необходимый для запросов.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini-2024-07-18`).
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Псевдонимы моделей.

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
        """ Асинхронно создает запрос к chatgpt4o.one и возвращает ответ.
        Args:
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Время ожидания ответа в секундах. По умолчанию 120.
            cookies (dict, optional): Куки для отправки с запросом. По умолчанию `None`.

        Returns:
            str: Ответ от сервера.

        Raises:
            RuntimeError: Если не найден `post_id` или `nonce`, или если отсутствует поле `data` в ответе.
        """
```

**Назначение**: Метод `create_async` выполняет асинхронный запрос к сервису `chatgpt4o.one` и возвращает ответ от языковой модели.

**Параметры**:
- `cls` (Chatgpt4o): Ссылка на класс.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания ответа в секундах. По умолчанию 120.
- `cookies` (dict, optional): Куки для отправки с запросом. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `str`: Ответ от сервера.

**Вызывает исключения**:
- `RuntimeError`: Если не найден `post_id` или `nonce`, или если отсутствует поле `data` в ответе.

**Как работает функция**:

1.  **Определение заголовков**: Определяются заголовки HTTP-запроса, включая `user-agent`, `referer` и другие необходимые параметры.
2.  **Создание сессии**: Создается асинхронная сессия с использованием `StreamSession` с заданными заголовками, куками, прокси и временем ожидания.
3.  **Получение `post_id` и `nonce`**: Если `_post_id` или `_nonce` не определены, функция отправляет GET-запрос на главную страницу сервиса, извлекает `post_id` и `nonce` из HTML-ответа с использованием регулярных выражений.
4.  **Форматирование запроса**: Форматирует список сообщений в строку запроса.
5.  **Отправка POST-запроса**: Отправляет POST-запрос на конечную точку `wp-admin/admin-ajax.php` с данными, включающими `_wpnonce`, `post_id`, `url`, `action`, `message` и `bot_id`.
6.  **Обработка ответа**: Обрабатывает JSON-ответ, проверяет наличие поля `data` и возвращает его значение.

```ascii
    +-----------------------+
    |    Определение        |
    |      заголовков       |
    +-----------------------+
             ↓
    +-----------------------+
    |   Создание            |
    |     асинхронной       |
    |        сессии         |
    +-----------------------+
             ↓
    +-----------------------+
    |   Получение           |
    |    post_id и nonce    |
    | (если необходимо)     |
    +-----------------------+
             ↓
    +-----------------------+
    |  Форматирование       |
    |      запроса          |
    +-----------------------+
             ↓
    +-----------------------+
    |  Отправка             |
    |   POST-запроса        |
    +-----------------------+
             ↓
    +-----------------------+
    |  Обработка            |
    |      ответа           |
    +-----------------------+
```

**Примеры**:

```python
# Пример вызова функции create_async
import asyncio
from typing import List, Dict, Optional

from g4f.Provider.not_working.Chatgpt4o import Chatgpt4o

async def main():
    model = "gpt-4o-mini-2024-07-18"
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "Привет!"}
    ]
    proxy: Optional[str] = None
    timeout: int = 120
    cookies: Optional[Dict[str, str]] = None

    try:
        response = await Chatgpt4o.create_async(
            model=model, messages=messages, proxy=proxy, timeout=timeout, cookies=cookies
        )
        print(f"Ответ: {response}")
    except Exception as ex:
        print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())