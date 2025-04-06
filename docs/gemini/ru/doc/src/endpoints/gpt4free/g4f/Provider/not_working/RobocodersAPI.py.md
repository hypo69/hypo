# Модуль для работы с RobocodersAPI

## Обзор

Модуль `RobocodersAPI` предоставляет асинхронный интерфейс для взаимодействия с API Robocoders AI. Он позволяет генерировать ответы от AI-агентов, таких как `GeneralCodingAgent`, `RepoAgent` и `FrontEndAgent`. Модуль поддерживает сохранение истории сообщений, использует кэширование токенов доступа и идентификаторов сессий для оптимизации работы.

## Подробнее

Этот модуль предназначен для интеграции с AI-сервисами Robocoders, предоставляя удобный способ отправки запросов и получения ответов в асинхронном режиме. Он включает в себя механизмы обработки ошибок, автоматического обновления токенов и управления сессиями.

## Классы

### `RobocodersAPI`

**Описание**: Класс `RobocodersAPI` реализует асинхронный провайдер для взаимодействия с API Robocoders AI.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("API Robocoders AI").
- `url` (str): URL документации API ("https://api.robocoders.ai/docs").
- `api_endpoint` (str): URL конечной точки API для чата ("https://api.robocoders.ai/chat").
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`'GeneralCodingAgent'`).
- `agent` (List[str]): Список доступных агентов (`[default_model, "RepoAgent", "FrontEndAgent"]`).
- `models` (List[str]): Список поддерживаемых моделей (совпадает со списком агентов).
- `CACHE_DIR` (Path): Директория для хранения кэша (`Path(get_cookies_dir())`).
- `CACHE_FILE` (Path): Путь к файлу кэша (`CACHE_DIR / "robocoders.json"`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API.
- `_get_or_create_access_and_session`: Получает или создает токен доступа и идентификатор сессии.
- `_fetch_and_cache_access_token`: Получает и кэширует токен доступа.
- `_create_and_cache_session`: Создает и кэширует идентификатор сессии.
- `_save_cached_data`: Сохраняет данные в кэш.
- `_update_cached_data`: Обновляет данные в кэше.
- `_clear_cached_data`: Очищает кэш.
- `_get_cached_data`: Получает данные из кэша.

## Функции

### `create_async_generator`

```python
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от API Robocoders AI.

        Args:
            model (str): Модель, используемая для генерации ответа.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API.

        Raises:
            Exception: Если не удалось инициализировать взаимодействие с API, произошла ошибка аутентификации,
                       ошибка валидации входных данных, серверная ошибка или неожиданная ошибка.

        Внутренние функции:
            Отсутствуют.
        """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Robocoders AI.

**Параметры**:
- `model` (str): Модель, используемая для генерации ответа (например, `'GeneralCodingAgent'`).
- `messages` (Messages): Список сообщений, отправляемых в API.
- `proxy` (str, optional): URL прокси-сервера (по умолчанию `None`).
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `Exception`: В случае ошибок при инициализации API, аутентификации, валидации, серверных ошибках и других непредвиденных ситуациях.

**Как работает функция**:

1.  **Инициализация сессии**: Функция создает асинхронную клиентскую сессию `aiohttp` с установленным таймаутом.
2.  **Получение или создание токена и ID сессии**: Использует метод `_get_or_create_access_and_session` для получения существующих или создания новых токена доступа и ID сессии.
3.  **Формирование заголовков**: Создает заголовки запроса, включая токен доступа.
4.  **Формирование данных запроса**: Подготавливает данные для отправки в API, включая ID сессии, промпт и модель агента.
5.  **Отправка запроса и обработка ответа**: Отправляет POST-запрос к API и обрабатывает ответ. В случае ошибок (401, 422, 500+) выбрасывает исключения.
6.  **Генерация ответов**: Асинхронно читает ответ, декодирует его из JSON и извлекает сообщения из полей `'args.content'` или `'message'`.  Возвращает сообщения через `yield`.
7.  **Обработка лимитов ресурсов**: Проверяет, достигнут ли лимит ресурсов, и автоматически продолжает диалог, отправляя запрос с `prompt="continue"`.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Создание асинхронной сессии
    │
    │   Получение/создание токена и ID сессии
    │
    │   Формирование заголовков и данных запроса
    │
    │   Отправка POST-запроса к API
    │
    │   Обработка ответа
    │   │
    │   └─── Ошибка (401, 422, 500+) -> Выброс исключения
    │   │
    │   Успех
    │   │
    │   Асинхронное чтение ответа
    │   │
    │   Декодирование JSON и извлечение сообщений
    │   │
    │   Проверка лимита ресурсов
    │   │
    │   └─── Достигнут -> Отправка запроса "continue"
    │   │
    │   Выдача сообщений через yield
    │
    Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "GeneralCodingAgent"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Напиши функцию на Python, которая складывает два числа."}]
    
    async def print_response(generator: AsyncGenerator[str, None]):
        async for message in generator:
            print(message, end="")

    try:
        generator = await RobocodersAPI.create_async_generator(model=model, messages=messages)
        await print_response(generator)
    except Exception as ex:
        print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_get_or_create_access_and_session`

```python
    @staticmethod
    async def _get_or_create_access_and_session(session: aiohttp.ClientSession):
        """
        Получает существующие или создает новые токен доступа и идентификатор сессии.

        Args:
            session (aiohttp.ClientSession): Асинхронная клиентская сессия.

        Returns:
            Tuple[str, str]: Токен доступа и идентификатор сессии.

        Raises:
            Exception: Если не удалось получить токен доступа или создать сессию.
        """
```

**Назначение**: Получает существующие из кэша или создает новые токен доступа и идентификатор сессии для взаимодействия с API Robocoders AI.

**Параметры**:
- `session` (aiohttp.ClientSession): Асинхронная клиентская сессия.

**Возвращает**:
- `Tuple[str, str]`: Кортеж, содержащий токен доступа и идентификатор сессии.

**Вызывает исключения**:
- `Exception`: Если не удается получить токен доступа или создать сессию.

**Как работает функция**:

1.  **Создание директории кэша**: Проверяет и создает директорию для кэша, если она не существует.
2.  **Загрузка данных из кэша**: Пытается загрузить данные из файла кэша. Если файл существует, загружает токен доступа и ID сессии.
3.  **Валидация данных**: Проверяет, существуют ли токен и ID сессии. Если они существуют, возвращает их.
4.  **Создание новых токена и ID сессии**: Если данные невалидны или отсутствуют в кэше, вызывает `_fetch_and_cache_access_token` и `_create_and_cache_session` для получения новых токена и ID сессии.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Создание директории кэша
    │
    │   Загрузка данных из кэша
    │
    │   Валидация данных (токен и ID сессии)
    │
    └─── Существуют -> Возврат токена и ID сессии
    │
    └─── Не существуют
        │
        │   Получение и кэширование токена
        │
        │   Создание и кэширование ID сессии
        │
        │   Возврат токена и ID сессии
    │
    Конец
```

**Примеры**:

```python
# Пример использования _get_or_create_access_and_session
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            access_token, session_id = await RobocodersAPI._get_or_create_access_and_session(session)
            print(f"Токен доступа: {access_token}")
            print(f"ID сессии: {session_id}")
        except Exception as ex:
            print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_fetch_and_cache_access_token`

```python
    @staticmethod
    async def _fetch_and_cache_access_token(session: aiohttp.ClientSession) -> str:
        """
        Получает токен доступа с API Robocoders AI и кэширует его.

        Args:
            session (aiohttp.ClientSession): Асинхронная клиентская сессия.

        Returns:
            str: Токен доступа.

        Raises:
            MissingRequirementsError: Если не установлен пакет "beautifulsoup4".
        """
```

**Назначение**: Получает токен доступа с API Robocoders AI, используя `BeautifulSoup` для парсинга HTML, и кэширует его.

**Параметры**:
- `session` (aiohttp.ClientSession): Асинхронная клиентская сессия.

**Возвращает**:
- `str`: Токен доступа.

**Вызывает исключения**:
- `MissingRequirementsError`: Если библиотека `beautifulsoup4` не установлена.

**Как работает функция**:

1.  **Проверка наличия BeautifulSoup**: Проверяет, установлен ли пакет `beautifulsoup4`. Если нет, вызывает исключение `MissingRequirementsError`.
2.  **Формирование запроса**: Подготавливает URL и заголовки для запроса к API аутентификации.
3.  **Отправка запроса и парсинг ответа**: Отправляет GET-запрос и получает HTML-ответ. Использует `BeautifulSoup` для поиска элемента `<pre>` с `id='token'` и извлекает текст токена.
4.  **Кэширование токена**: Сохраняет токен в кэш с помощью `_save_cached_data`.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Проверка наличия BeautifulSoup
    │
    └─── Отсутствует -> Выброс исключения MissingRequirementsError
    │
    └─── Присутствует
        │
        │   Формирование запроса
        │
        │   Отправка GET-запроса
        │
        │   Парсинг HTML с помощью BeautifulSoup
        │
        │   Извлечение токена
        │
        │   Кэширование токена
        │
        │   Возврат токена
    │
    Конец
```

**Примеры**:

```python
# Пример использования _fetch_and_cache_access_token
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            access_token = await RobocodersAPI._fetch_and_cache_access_token(session)
            print(f"Токен доступа: {access_token}")
        except Exception as ex:
            print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_create_and_cache_session`

```python
    @staticmethod
    async def _create_and_cache_session(session: aiohttp.ClientSession, access_token: str) -> str:
        """
        Создает идентификатор сессии, используя токен доступа, и кэширует его.

        Args:
            session (aiohttp.ClientSession): Асинхронная клиентская сессия.
            access_token (str): Токен доступа.

        Returns:
            str: Идентификатор сессии.

        Raises:
            Exception: Если произошла ошибка аутентификации или валидации входных данных.
        """
```

**Назначение**: Создает идентификатор сессии, используя полученный токен доступа, и кэширует его.

**Параметры**:
- `session` (aiohttp.ClientSession): Асинхронная клиентская сессия.
- `access_token` (str): Токен доступа.

**Возвращает**:
- `str`: Идентификатор сессии.

**Вызывает исключения**:
- `Exception`: В случае ошибки аутентификации (401) или ошибки валидации входных данных (422).

**Как работает функция**:

1.  **Формирование запроса**: Подготавливает URL и заголовки для создания сессии, включая токен доступа.
2.  **Отправка запроса и обработка ответа**: Отправляет GET-запрос и получает JSON-ответ. Извлекает идентификатор сессии из поля `'sid'`.
3.  **Кэширование ID сессии**: Обновляет кэш с помощью `_update_cached_data`, сохраняя ID сессии.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Формирование запроса
    │
    │   Отправка GET-запроса
    │
    │   Обработка ответа
    │   │
    │   └─── Ошибка (401, 422) -> Выброс исключения
    │   │
    │   Успех
    │   │
    │   Извлечение ID сессии
    │
    │   Кэширование ID сессии
    │
    │   Возврат ID сессии
    │
    Конец
```

**Примеры**:

```python
# Пример использования _create_and_cache_session
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            # Для примера требуется предварительно получить access_token
            access_token = "example_access_token"  
            session_id = await RobocodersAPI._create_and_cache_session(session, access_token)
            print(f"ID сессии: {session_id}")
        except Exception as ex:
            print(f"Ошибка: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `_save_cached_data`

```python
    @staticmethod
    def _save_cached_data(new_data: dict):
        """Save new data to cache file"""
```

**Назначение**: Сохраняет новые данные в файл кэша.

**Параметры**:
- `new_data` (dict): Словарь с данными для сохранения.

**Возвращает**:
- `None`

**Как работает функция**:

1.  **Создание директории кэша**: Проверяет и создает директорию для кэша, если она не существует.
2.  **Создание файла кэша**: Создает файл кэша, если он не существует.
3.  **Сохранение данных**: Записывает данные в файл кэша в формате JSON.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Создание директории кэша
    │
    │   Создание файла кэша
    │
    │   Запись данных в файл кэша
    │
    Конец
```

**Примеры**:

```python
# Пример использования _save_cached_data
new_data = {"access_token": "example_token"}
RobocodersAPI._save_cached_data(new_data)
```

### `_update_cached_data`

```python
    @staticmethod
    def _update_cached_data(updated_data: dict):
        """Update existing cache data with new values"""
```

**Назначение**: Обновляет существующие данные в файле кэша новыми значениями.

**Параметры**:
- `updated_data` (dict): Словарь с данными для обновления.

**Возвращает**:
- `None`

**Как работает функция**:

1.  **Загрузка существующих данных**: Пытается загрузить существующие данные из файла кэша. Если файл поврежден, начинает с пустого словаря.
2.  **Обновление данных**: Обновляет загруженные данные новыми значениями.
3.  **Сохранение обновленных данных**: Записывает обновленные данные в файл кэша в формате JSON.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Загрузка существующих данных из кэша
    │
    │   Обновление данных
    │
    │   Запись обновленных данных в файл кэша
    │
    Конец
```

**Примеры**:

```python
# Пример использования _update_cached_data
updated_data = {"sid": "example_session_id"}
RobocodersAPI._update_cached_data(updated_data)
```

### `_clear_cached_data`

```python
    @staticmethod
    def _clear_cached_data():
        """Remove cache file"""
```

**Назначение**: Удаляет файл кэша.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Как работает функция**:

1.  **Проверка наличия файла кэша**: Проверяет, существует ли файл кэша.
2.  **Удаление файла**: Удаляет файл кэша, если он существует.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Проверка наличия файла кэша
    │
    └─── Существует -> Удаление файла
    │
    Конец
```

**Примеры**:

```python
# Пример использования _clear_cached_data
RobocodersAPI._clear_cached_data()
```

### `_get_cached_data`

```python
    @staticmethod
    def _get_cached_data() -> dict:
        """Get all cached data"""
```

**Назначение**: Получает все данные из файла кэша.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `dict`: Словарь с данными из кэша.

**Как работает функция**:

1.  **Проверка наличия файла кэша**: Проверяет, существует ли файл кэша.
2.  **Загрузка данных**: Пытается загрузить данные из файла кэша. Если файл поврежден, возвращает пустой словарь.

**ASCII схема работы функции**:

```
    Начало
    │
    │   Проверка наличия файла кэша
    │
    └─── Существует -> Загрузка данных из файла
    │
    └─── Отсутствует -> Возврат пустого словаря
    │
    Конец
```

**Примеры**:

```python
# Пример использования _get_cached_data
cached_data = RobocodersAPI._get_cached_data()
print(cached_data)