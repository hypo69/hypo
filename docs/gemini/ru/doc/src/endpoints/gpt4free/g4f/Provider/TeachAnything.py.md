# Модуль TeachAnything

## Обзор

Модуль `TeachAnything` предоставляет асинхронный генератор для взаимодействия с API `teach-anything.com`. Он позволяет получать ответы от AI-моделей Gemini 1.5 Pro и Gemini 1.5 Flash. Модуль использует `aiohttp` для асинхронных HTTP-запросов и предоставляет методы для форматирования запросов и обработки ответов.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с AI-моделями через API `teach-anything.com`. Он обеспечивает асинхронное взаимодействие, что позволяет эффективно обрабатывать запросы и ответы, не блокируя основной поток выполнения. Модуль также предоставляет механизм для обработки ошибок декодирования и логирования.

## Классы

### `TeachAnything`

**Описание**: Класс `TeachAnything` является провайдером асинхронного генератора, который взаимодействует с API `teach-anything.com`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL API `teach-anything.com`.
- `api_endpoint` (str): Endpoint API для генерации ответов.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `default_model` (str): Модель по умолчанию (`gemini-1.5-pro`).
- `models` (List[str])`: Список поддерживаемых моделей (`gemini-1.5-pro`, `gemini-1.5-flash`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API.
- `_get_headers`: Возвращает словарь с заголовками HTTP-запроса.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str | None = None,
    **kwargs: Any
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от API.

    Args:
        cls (TeachAnything): Класс TeachAnything.
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для отправки в API.
        proxy (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs (Any): Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа от API.

    Raises:
        aiohttp.ClientError: Если возникает ошибка при выполнении HTTP-запроса.
        Exception: Если возникает ошибка при декодировании ответа.
    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с API `teach-anything.com`.

**Параметры**:
- `cls` (TeachAnything): Класс `TeachAnything`.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs` (Any): Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа от API.

**Вызывает исключения**:
- `aiohttp.ClientError`: Если возникает ошибка при выполнении HTTP-запроса.
- `Exception`: Если возникает ошибка при декодировании ответа.

**Как работает функция**:

1. **Подготовка**:
   - Функция получает параметры, такие как используемая модель, список сообщений и URL прокси-сервера (если указан).
   - Формируются заголовки HTTP-запроса с помощью метода `_get_headers`.
   - Определяется модель с помощью `cls.get_model(model)`.

2. **Выполнение HTTP-запроса**:
   - Создается асинхронная сессия `aiohttp.ClientSession` с заданными заголовками.
   - Форматируется запрос с помощью функции `format_prompt(messages)`.
   - Отправляется POST-запрос на API endpoint (`cls.url + cls.api_endpoint`) с использованием `session.post`.

3. **Обработка ответа**:
   - Ответ от API обрабатывается по частям (chunks) с использованием `response.content.iter_any()`.
   - Каждый чанк добавляется в буфер (`buffer`).
   - Буфер декодируется в кодировке UTF-8. Если декодирование успешно, результат передается через `yield` и буфер очищается.
   - Если декодирование вызывает ошибку `UnicodeDecodeError`, ожидается поступление дополнительных данных в буфер.

4. **Обработка остаточных данных**:
   - После завершения итерации по чанкам проверяется, остались ли данные в буфере.
   - Если данные остались, они декодируются и передаются через `yield`.
   - В случае ошибки декодирования остаточных данных, она выводится в консоль.

```
    Подготовка запроса
    │
    ├───► Создание сессии aiohttp
    │
    ├───► Форматирование запроса
    │
    └───► Отправка POST-запроса
        │
        │   Обработка ответа по частям
        │   │
        │   ├───► Декодирование чанка
        │   │   │
        │   │   ├───► Успешно: Передача результата через yield
        │   │   │
        │   │   └───► Ошибка: Ожидание дополнительных данных
        │   │
        │   └───► Обработка остаточных данных в буфере
        │
        └───► Завершение
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict

from g4f.Provider.TeachAnything import TeachAnything
from g4f.typing import Messages

async def main():
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, world!"}]
    async for message in TeachAnything.create_async_generator(model="gemini-1.5-pro", messages=messages):
        print(message, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_get_headers`

```python
@staticmethod
def _get_headers() -> Dict[str, str]:
    """
    Возвращает словарь с заголовками HTTP-запроса.

    Returns:
        Dict[str, str]: Словарь с заголовками HTTP-запроса.
    """
```

**Назначение**: Получение заголовков для HTTP-запроса.

**Возвращает**:
- `Dict[str, str]`: Словарь с заголовками HTTP-запроса.

**Как работает функция**:

1. **Определение заголовков**:
   - Функция определяет набор HTTP-заголовков, необходимых для взаимодействия с API `teach-anything.com`.
   - Заголовки включают `accept`, `accept-language`, `content-type`, `user-agent` и другие.

2. **Возврат заголовков**:
   - Функция возвращает словарь, содержащий определенные заголовки.

```
    Определение заголовков
    │
    └───► Возврат словаря с заголовками
```

**Примеры**:

```python
# Пример использования _get_headers
from g4f.Provider.TeachAnything import TeachAnything

headers = TeachAnything._get_headers()
print(headers)
```