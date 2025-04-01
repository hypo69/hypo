# Модуль Cerebras

## Обзор

Модуль `Cerebras` предоставляет класс для взаимодействия с API Cerebras Inference для генерации текста. Он наследуется от класса `OpenaiAPI` и использует асинхронные запросы для получения результатов. Модуль поддерживает различные модели, предоставляемые Cerebras, и предоставляет методы для аутентификации и создания асинхронного генератора для получения ответов от API.

## Подробней

Этот модуль позволяет использовать модели Cerebras Inference для генерации текста. Он обеспечивает аутентификацию через API-ключ или cookies, а также предоставляет удобный интерфейс для отправки запросов и получения результатов в асинхронном режиме. Класс `Cerebras` поддерживает несколько моделей и предоставляет алиасы для удобства использования. Расположение файла в проекте указывает на то, что он является частью g4f (GPT4Free) и предназначен для работы с конкретным провайдером (Cerebras).

## Классы

### `Cerebras(OpenaiAPI)`

**Описание**: Класс для взаимодействия с API Cerebras Inference.

**Наследует**:
- `OpenaiAPI`: Предоставляет базовую функциональность для взаимодействия с API OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера "Cerebras Inference".
- `url` (str): URL главной страницы Cerebras Inference.
- `login_url` (str): URL страницы логина Cerebras Cloud.
- `api_base` (str): Базовый URL API Cerebras.
- `working` (bool): Указывает, что провайдер работает (True).
- `default_model` (str): Модель по умолчанию "llama3.1-70b".
- `models` (list[str]): Список поддерживаемых моделей.
- `model_aliases` (dict[str, str]): Алиасы моделей для удобства использования.

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от API.

## Функции

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
        """Создает асинхронный генератор для получения ответов от API Cerebras Inference.

        Args:
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки в API.
            api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
            cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
            **kwargs: Дополнительные аргументы, передаваемые в базовый класс.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий чанки ответов от API.

        Как работает функция:
         1. **Проверка наличия API-ключа**:
            - Функция сначала проверяет, был ли предоставлен API-ключ (`api_key`).
            - Если API-ключ не предоставлен, функция пытается получить его через cookies.

         2. **Получение API-ключа через cookies**:
            - Если `cookies` также не предоставлены, функция пытается получить их из домена ".cerebras.ai" с помощью `get_cookies(".cerebras.ai")`.
            - Открывается асинхронная сессия с использованием `ClientSession` и переданных cookies.
            - Выполняется GET-запрос к "https://inference.cerebras.ai/api/auth/session".
            - Функция `raise_for_status` проверяет, что ответ имеет статус 200 OK.
            - Извлекается JSON-ответ, который должен содержать API-ключ.
            - API-ключ извлекается из `data.get("user", {}).get("demoApiKey")`.

         3. **Создание асинхронного генератора**:
            - Независимо от того, как был получен `api_key`, функция вызывает метод `create_async_generator` родительского класса (`super().create_async_generator(...)`) для создания асинхронного генератора.
            - При вызове передаются следующие аргументы:
              - `model`: Модель, указанная при вызове функции.
              - `messages`: Сообщения для отправки в API.
              - `impersonate="chrome"`: Указывает, что запросы должны имитировать браузер Chrome.
              - `api_key`: API-ключ, полученный на предыдущих шагах.
              - `headers={"User-Agent": "ex/JS 1.5.0"}`: Заголовки, включающие User-Agent.
              - `**kwargs`: Дополнительные аргументы, переданные при вызове функции.

         4. **Генерация чанков ответов**:
            - Асинхронный генератор, созданный в родительском классе, возвращает чанки ответов от API.
            - Каждый чанк передается вызывающей стороне с помощью `yield chunk`.

        A -- Проверка API-ключа
        |
        B -- Получение API-ключа через Cookies
        |
        C -- Создание асинхронного генератора
        |
        D -- Генерация чанков ответов
        |
        E -- Выдача чанка ответа

        ASCII flowchart:

        Проверка API-ключа
        │
        ├── Нет API-ключа ── Получение API-ключа через Cookies
        │   │
        │   └── Получение Cookies, запрос к API, извлечение API-ключа
        │
        └── Есть API-ключ
        │
        Создание асинхронного генератора (с API-ключом, сообщениями и заголовками)
        │
        Генерация чанков ответов (из асинхронного генератора)
        │
        Выдача чанка ответа (yield)

        """
        if api_key is None:
            if cookies is None:
                cookies = get_cookies(".cerebras.ai")
            async with ClientSession(cookies=cookies) as session:
                async with session.get("https://inference.cerebras.ai/api/auth/session") as response:
                    await raise_for_status(response)
                    data = await response.json()
                    if data:
                        api_key = data.get("user", {}).get("demoApiKey")
        async for chunk in super().create_async_generator(
            model, messages,
            impersonate="chrome",
            api_key=api_key,
            headers={
                "User-Agent": "ex/JS 1.5.0",
            },
            **kwargs
        ):
            yield chunk
```

**Параметры**:
- `cls` (type[Cerebras]): Ссылка на класс `Cerebras`.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки в API.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, передаваемые в базовый класс.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий чанки ответов от API.

**Примеры**:

```python
# Пример использования create_async_generator
async def main():
    model = "llama3.1-70b"
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    api_key = "your_api_key"  # Замените на ваш фактический API-ключ

    async for chunk in Cerebras.create_async_generator(model=model, messages=messages, api_key=api_key):
        print(chunk, end="")

# Запуск примера
# asyncio.run(main())