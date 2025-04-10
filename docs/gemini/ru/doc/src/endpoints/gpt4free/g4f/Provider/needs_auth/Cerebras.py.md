# Модуль Cerebras

## Обзор

Модуль `Cerebras.py` предоставляет класс `Cerebras`, который является наследником класса `OpenaiAPI`. Он предназначен для взаимодействия с сервисом Cerebras Inference, предоставляющим доступ к различным моделям, включая Llama и Deepseek. Модуль обеспечивает аутентификацию и создание асинхронных генераторов для обработки сообщений с использованием API Cerebras.

## Подробнее

Модуль содержит информацию о доступных моделях, URL-адресах для доступа к API, а также методы для аутентификации и создания асинхронных генераторов. Он использует `aiohttp` для асинхронных запросов, а также функции из других модулей проекта, таких как `raise_for_status` для обработки ошибок и `get_cookies` для получения cookies.

## Классы

### `Cerebras`

**Описание**: Класс для взаимодействия с сервисом Cerebras Inference.

**Наследует**:
- `OpenaiAPI`: Наследует функциональность для работы с OpenAI-подобными API.

**Атрибуты**:
- `label` (str): Метка провайдера "Cerebras Inference".
- `url` (str): URL для доступа к сервису Cerebras Inference.
- `login_url` (str): URL для логина в Cerebras Cloud.
- `api_base` (str): Базовый URL для API Cerebras.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию ("llama3.1-70b").
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь с псевдонимами моделей.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для обработки сообщений.

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        api_key: str = None,
        cookies: Cookies = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для взаимодействия с API Cerebras.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для обработки.
            api_key (str, optional): API ключ. Если не указан, пытается получить его из cookies. По умолчанию `None`.
            cookies (Cookies, optional): Cookies для аутентификации. Если `api_key` не указан, используются cookies для получения ключа. По умолчанию `None`.
            **kwargs: Дополнительные аргументы, передаваемые в базовый класс.

        Returns:
            AsyncResult: Асинхронный генератор чанков данных.

        Как работает функция:
        1.  Проверяет наличие `api_key`. Если он не предоставлен, пытается получить его из cookies.
        2.  Если `api_key` отсутствует, функция пытается получить cookies из домена ".cerebras.ai".
        3.  Используя полученные cookies, отправляется запрос к "https://inference.cerebras.ai/api/auth/session" для получения данных сессии, из которых извлекается `api_key`.
        4.  Вызывает метод `create_async_generator` базового класса `OpenaiAPI` с полученным или предоставленным `api_key` и другими параметрами.
        5.  Передает полученные чанки данных от базового класса.

        Внутренние функции:
        - Отсутствуют.

        """
        ...
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Cerebras.

**Параметры**:
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для обработки.
- `api_key` (str, optional): API ключ. Если не указан, пытается получить его из cookies. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. Если `api_key` не указан, используются cookies для получения ключа. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, передаваемые в базовый класс.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор чанков данных.

**Вызывает исключения**:
- Отсутствуют.

**Как работает функция**:

1.  **Проверка API-ключа**: Если `api_key` не предоставлен явно, функция пытается получить его из cookies. Если cookies также не предоставлены, они извлекаются из домена `.cerebras.ai`.
2.  **Получение API-ключа из сессии**: Если `api_key` не был предоставлен, отправляется GET-запрос к `https://inference.cerebras.ai/api/auth/session` для получения данных сессии. Из полученных данных извлекается `api_key`.
3.  **Создание асинхронного генератора**: Вызывается метод `create_async_generator` родительского класса (`OpenaiAPI`) с переданными параметрами, включая полученный `api_key`.
4.  **Генерация чанков**: Функция итерирует по чанкам, возвращаемым родительским классом, и передает их вызывающей стороне.

```
    Проверка API-ключа
    │
    ├── Нет API-ключа: Попытка получения cookies
    │   │
    │   └── Получение cookies из домена ".cerebras.ai"
    │       │
    │       └── Запрос к API для получения API-ключа из сессии
    │
    └── Есть API-ключ: Пропуск шага получения API-ключа
    │
    Создание асинхронного генератора в родительском классе (OpenaiAPI)
    │
    Итерация по чанкам, возвращаемым родительским классом
    │
    Передача чанков вызывающей стороне
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с указанием API-ключа
async for chunk in Cerebras.create_async_generator(model="llama3.1-70b", messages=[{"role": "user", "content": "Hello"}], api_key="YOUR_API_KEY"):
    print(chunk)

# Пример 2: Создание асинхронного генератора без API-ключа (с использованием cookies)
async for chunk in Cerebras.create_async_generator(model="llama3.1-70b", messages=[{"role": "user", "content": "Hello"}], cookies={"session_id": "YOUR_SESSION_ID"}):
    print(chunk)

# Пример 3: Создание асинхронного генератора без API-ключа и cookies (автоматическое получение cookies)
async for chunk in Cerebras.create_async_generator(model="llama3.1-70b", messages=[{"role": "user", "content": "Hello"}]):
    print(chunk)