# Модуль `Goabror`

## Обзор

Модуль предоставляет класс `Goabror`, который является асинхронным генератором для взаимодействия с API Goabror.uz. Он позволяет отправлять запросы к API и получать ответы в виде асинхронного генератора, обрабатывая как JSON, так и текстовые ответы.

## Подробнее

Этот модуль предназначен для интеграции с сервисом Goabror.uz, предоставляющим доступ к моделям, аналогичным GPT. Класс `Goabror` упрощает взаимодействие с API, автоматически форматируя запросы и обрабатывая ответы, что делает его удобным для использования в асинхронных приложениях.

## Классы

### `Goabror`

**Описание**: Класс `Goabror` реализует асинхронный генератор для взаимодействия с API Goabror.uz.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL главной страницы Goabror.uz.
- `api_endpoint` (str): URL API для отправки запросов.
- `working` (bool): Флаг, указывающий, что провайдер работает.
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4`).
- `models` (list[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для отправки запросов к API и получения ответов.

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
        """ Создает асинхронный генератор для отправки запросов к API Goabror.uz и получения ответов.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API.
        """
```

**Назначение**: Создает асинхронный генератор для отправки запросов к API Goabror.uz и получения ответов.

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Как работает функция**:

1.  **Определение заголовков**: Функция начинает с определения заголовков HTTP-запроса, включая `accept`, `accept-language` и `user-agent`.
2.  **Создание сессии**: Создается асинхронная сессия `ClientSession` с заданными заголовками для выполнения HTTP-запросов.
3.  **Формирование параметров запроса**: Функция форматирует параметры запроса, включая пользовательское сообщение и системный промпт, используя функции `format_prompt` и `get_system_prompt` соответственно.
4.  **Выполнение GET-запроса**: С использованием асинхронной сессии выполняется GET-запрос к API-endpoint с переданными параметрами и прокси (если указан).
5.  **Обработка ответа**: Полученный ответ проходит через проверку на ошибки с помощью `raise_for_status`, после чего извлекается текстовое содержимое ответа.
6.  **Анализ ответа**: Функция пытается интерпретировать текстовый ответ как JSON. Если это удается, и в JSON-ответе присутствует ключ `"data"`, то значение этого ключа передается в генератор. В противном случае, в генератор передается весь JSON-ответ. Если JSON-декодирование не удается, то в генератор передается исходный текстовый ответ.

**ASCII flowchart**:

```
    Начало
    ↓
    [Определение заголовков HTTP-запроса]
    ↓
    [Создание асинхронной сессии ClientSession]
    ↓
    [Формирование параметров запроса]
    ↓
    [Выполнение GET-запроса к API-endpoint]
    ↓
    [Проверка ответа на ошибки raise_for_status]
    ↓
    [Получение текстового содержимого ответа]
    ↓
    [Попытка интерпретации ответа как JSON]
    |   [Удачно: Извлечение данных из ключа "data" или передача всего JSON]
    |   [Неудачно: Передача исходного текстового ответа]
    ↓
    Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gpt-4"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, how are you?"}]

    generator: AsyncGenerator[str, None] = Goabror.create_async_generator(model=model, messages=messages)
    async for response in generator:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример использования create_async_generator с прокси
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gpt-4"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Translate to french: Hello, how are you?"}]
    proxy = "http://your_proxy:8080"  # Замените на ваш прокси

    generator: AsyncGenerator[str, None] = Goabror.create_async_generator(model=model, messages=messages, proxy=proxy)
    async for response in generator:
        print(response)

if __name__ == "__main__":
    asyncio.run(main())