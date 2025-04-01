# Модуль DuckDuckGo

## Обзор

Модуль `DuckDuckGo.py` предоставляет асинхронный интерфейс для взаимодействия с сервисом DuckDuckGo AI Chat через библиотеку `duckduckgo_search`. Он позволяет получать ответы от различных моделей, таких как `gpt-4o-mini`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`, `claude-3-haiku-20240307`, `o3-mini` и `mistralai/Mistral-Small-24B-Instruct-2501`, используя асинхронные генераторы. Модуль также включает поддержку прокси и аутентификацию через `nodriver` для обхода ограничений.

## Подробнее

Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется взаимодействие с AI-моделями через DuckDuckGo AI Chat. Он предоставляет удобный интерфейс для получения ответов в асинхронном режиме, что позволяет эффективно использовать ресурсы и обрабатывать запросы параллельно.

Модуль использует библиотеку `duckduckgo_search` для взаимодействия с DuckDuckGo AI Chat. Если библиотека не установлена, модуль выдаст ошибку `ImportError`. Для аутентификации и получения необходимых параметров используется `nodriver`.

## Классы

### `DuckDuckGo`

**Описание**: Класс `DuckDuckGo` является асинхронным провайдером для взаимодействия с DuckDuckGo AI Chat.

**Принцип работы**:
Класс наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он инициализирует `DDGS` (DuckDuckGo Search) клиент с поддержкой прокси и таймаута. Также предоставляет метод `create_async_generator` для создания асинхронного генератора, который возвращает ответы от DuckDuckGo AI Chat.

**Атрибуты класса**:
- `label` (str): Метка провайдера "Duck.ai (duckduckgo_search)".
- `url` (str): URL для DuckDuckGo AI Chat "https://duckduckgo.com/aichat".
- `api_base` (str): Базовый URL для API DuckDuckGo "https://duckduckgo.com/duckchat/v1/".
- `working` (bool): Указывает, работает ли провайдер (по умолчанию `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (по умолчанию `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (по умолчанию `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (по умолчанию `True`).
- `default_model` (str): Модель по умолчанию "gpt-4o-mini".
- `models` (List[str]): Список поддерживаемых моделей.
- `ddgs` (DDGS): Инстанс класса `DDGS` для выполнения поисковых запросов.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от DuckDuckGo AI Chat.
- `nodriver_auth`: Выполняет аутентификацию через `nodriver` для получения необходимых параметров.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 60,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения ответов от DuckDuckGo AI Chat.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `60`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от DuckDuckGo AI Chat.

        Raises:
            ImportError: Если не установлен пакет `duckduckgo_search`.
        Как работает функция:
        1. Проверяется, установлен ли пакет `duckduckgo_search`. Если нет, вызывается исключение `ImportError`.
        2. Если `ddgs` не инициализирован, он инициализируется с использованием прокси и таймаута.
        3. Вызывается функция `cls.nodriver_auth(proxy=proxy)`, чтобы получить параметры аутентификации.
        4. Модель приводится к нужному виду с помощью `cls.get_model(model)`.
        5. Создается асинхронный генератор с помощью `cls.ddgs.chat_yield()`, который возвращает ответы от DuckDuckGo AI Chat.
        6. Генератор возвращает чанки данных.

        Внутри функции происходят следующие действия и преобразования:
        A: Проверка наличия `duckduckgo_search`.
        |
        B: Инициализация `DDGS`, если он еще не инициализирован.
        |
        C: Аутентификация через `nodriver`.
        |
        D: Получение модели.
        |
        E: Запуск асинхронного генератора `cls.ddgs.chat_yield()`.

        """
```
**Параметры**:

- `model` (str): Модель для использования в чате.
- `messages` (Messages): Список сообщений, отправленных пользователем.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию `60`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий ответы от DuckDuckGo AI Chat.

**Вызывает исключения**:

- `ImportError`: Если не установлен пакет `duckduckgo_search`.

**Примеры**:

```python
# Пример использования функции create_async_generator
model = "gpt-4o-mini"
messages = [{"role": "user", "content": "Hello, how are you?"}]
proxy = "http://your_proxy:8080"
timeout = 60

async def main():
    async for chunk in DuckDuckGo.create_async_generator(model=model, messages=messages, proxy=proxy, timeout=timeout):
        print(chunk)

# asyncio.run(main())  # Закомментировано, так как пример требует асинхронного контекста
```

### `nodriver_auth`

```python
    @classmethod
    async def nodriver_auth(cls, proxy: str = None):
        """Выполняет аутентификацию через `nodriver` для получения необходимых параметров.

        Args:
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.

        Raises:
            Exception: Если возникает ошибка при аутентификации.

        Как работает функция:

        1.  Запускается браузер с помощью `get_nodriver(proxy=proxy)`.
        2.  Определяется функция `on_request`, которая будет вызываться при каждом запросе.
            Эта функция проверяет, содержит ли URL запроса `cls.api_base`.
            Если да, то из заголовков запроса извлекаются значения `X-Vqd-4`, `X-Vqd-Hash-1` и `F-Fe-Version` и сохраняются в атрибуты `cls.ddgs._chat_vqd`, `cls.ddgs._chat_vqd_hash` и `cls.ddgs._chat_xfe` соответственно.
        3.  Включается перехват запросов в браузере с помощью `page.send(nodriver.cdp.network.enable())`.
        4.  Добавляется обработчик `on_request` для перехвата запросов с помощью `page.add_handler(nodriver.cdp.network.RequestWillBeSent, on_request)`.
        5.  Открывается страница `cls.url` в браузере с помощью `browser.get(cls.url)`.
        6.  В цикле проверяется, получено ли значение `cls.ddgs._chat_vqd`. Если да, цикл завершается.
        7.  Закрывается вкладка с помощью `page.close()`.
        8.  Останавливается браузер с помощью `stop_browser()`.

        Внутри функции происходят следующие действия и преобразования:
        A: Запуск браузера с помощью `get_nodriver`.
        |
        B: Определение функции `on_request` для перехвата запросов.
        |
        C: Включение перехвата запросов в браузере.
        |
        D: Добавление обработчика `on_request` для перехвата запросов.
        |
        E: Открытие страницы `cls.url` в браузере.
        |
        F: Ожидание получения значения `cls.ddgs._chat_vqd`.
        |
        G: Закрытие вкладки и остановка браузера.
        """
```

**Параметры**:

- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.

**Вызывает исключения**:

- `Exception`: Если возникает ошибка при аутентификации.

**Примеры**:

```python
# Пример использования функции nodriver_auth
proxy = "http://your_proxy:8080"

async def main():
    await DuckDuckGo.nodriver_auth(proxy=proxy)
    print(DuckDuckGo.ddgs._chat_vqd)

# asyncio.run(main())  # Закомментировано, так как пример требует асинхронного контекста
```