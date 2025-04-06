# Модуль DuckDuckGo.py

## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с чат-ботом DuckDuckGo, используя библиотеку `duckduckgo_search`. Он позволяет генерировать ответы чат-бота на основе предоставленных сообщений, поддерживая стриминг, системные сообщения и историю сообщений.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими доступа к возможностям чат-бота DuckDuckGo.
Он включает в себя обработку зависимостей, аутентификацию через `nodriver` (если доступно) и асинхронную генерацию ответов. Модуль также предоставляет псевдонимы для моделей, чтобы упростить их использование.

## Классы

### `DuckDuckGo`

**Описание**: Класс `DuckDuckGo` предоставляет асинхронный интерфейс для взаимодействия с чат-ботом DuckDuckGo. Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую структуру для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Duck.ai (duckduckgo_search)"`.
- `url` (str): URL чат-бота DuckDuckGo, `"https://duckduckgo.com/aichat"`.
- `api_base` (str): Базовый URL API DuckDuckGo, `"https://duckduckgo.com/duckchat/v1/"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, `False`.
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга, `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений, `True`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений, `True`.
- `default_model` (str): Модель, используемая по умолчанию, `"gpt-4o-mini"`.
- `models` (list): Список поддерживаемых моделей, `[default_model, "meta-llama/Llama-3.3-70B-Instruct-Turbo", "claude-3-haiku-20240307", "o3-mini", "mistralai/Mistral-Small-24B-Instruct-2501"]`.
- `ddgs` (DDGS): Инстанс класса `DDGS` из библиотеки `duckduckgo_search`.
- `model_aliases` (dict): Словарь псевдонимов моделей, например `{"gpt-4": "gpt-4o-mini", ...}`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от чат-бота DuckDuckGo.
- `nodriver_auth`: Выполняет аутентификацию с использованием `nodriver` для получения необходимых токенов.

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
    """
    Создает асинхронный генератор для получения ответов от чат-бота DuckDuckGo.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для передачи в чат-бот.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа от чат-бота. По умолчанию `60`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от чат-бота.

    Raises:
        ImportError: Если не установлена библиотека `duckduckgo_search`.
        DuckDuckGoSearchException: Если во время запроса к DuckDuckGo произошла ошибка.
        RatelimitException: Если превышен лимит запросов.
        ConversationLimitException: Если превышен лимит на количество сообщений в разговоре.

    Как работает функция:
    1. Проверяет, установлена ли библиотека `duckduckgo_search`. Если нет, вызывает исключение `ImportError`.
    2. Если `cls.ddgs` не инициализирован, создает экземпляр `DDGS` с заданными параметрами прокси и таймаута, а также выполняет аутентификацию через `nodriver_auth`, если доступен `nodriver`.
    3. Получает псевдоним модели с помощью `cls.get_model(model)`.
    4. Использует `cls.ddgs.chat_yield` для получения асинхронного генератора ответов от чат-бота, передавая последнее сообщение пользователя, модель и таймаут.
    5. Передает каждый чанк ответа через `yield`.

    ASCII flowchart:

    Проверка duckduckgo_search -> Создание DDGS (если не существует) -> nodriver_auth (если has_nodriver) -> Получение псевдонима модели -> chat_yield -> Выдача чанков

    Примеры:
        Пример 1: Создание генератора с использованием модели по умолчанию
        >>> model = "gpt-4o-mini"
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> generator = DuckDuckGo.create_async_generator(model=model, messages=messages)

        Пример 2: Создание генератора с использованием прокси и таймаута
        >>> model = "gpt-4o-mini"
        >>> messages = [{"role": "user", "content": "Hello"}]
        >>> proxy = "http://proxy.example.com"
        >>> timeout = 30
        >>> generator = DuckDuckGo.create_async_generator(model=model, messages=messages, proxy=proxy, timeout=timeout)
    """
    if not has_requirements:
        raise ImportError("duckduckgo_search is not installed. Install it with `pip install duckduckgo-search`.")
    if cls.ddgs is None:
        cls.ddgs = DDGS(proxy=proxy, timeout=timeout)
        if has_nodriver:
            await cls.nodriver_auth(proxy=proxy)
    model = cls.get_model(model)
    for chunk in cls.ddgs.chat_yield(get_last_user_message(messages), model, timeout):
        yield chunk
```

### `nodriver_auth`

```python
@classmethod
async def nodriver_auth(cls, proxy: str = None):
    """
    Выполняет аутентификацию с использованием `nodriver` для получения необходимых токенов.

    Args:
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.

    Как работает функция:
    1. Получает экземпляр браузера и функцию для его остановки с помощью `get_nodriver`.
    2. Определяет функцию `on_request`, которая будет вызываться при каждом запросе. Эта функция проверяет, содержит ли URL запроса `cls.api_base`. Если да, она извлекает значения `X-Vqd-4`, `X-Vqd-Hash-1` и `F-Fe-Version` из заголовков запроса и сохраняет их в атрибуты `cls.ddgs._chat_vqd`, `cls.ddgs._chat_vqd_hash` и `cls.ddgs._chat_xfe` соответственно.
    3. Активирует перехват сетевых запросов с помощью `page.send(nodriver.cdp.network.enable())`.
    4. Добавляет обработчик `on_request` для события `nodriver.cdp.network.RequestWillBeSent`.
    5. Открывает страницу `cls.url` в браузере.
    6. Ожидает, пока не будет установлено значение `cls.ddgs._chat_vqd`.
    7. Закрывает страницу и останавливает браузер.

    ASCII flowchart:

    get_nodriver -> Определение on_request -> Активация перехвата запросов -> Добавление обработчика on_request -> Открытие страницы cls.url -> Ожидание cls.ddgs._chat_vqd -> Закрытие страницы -> Остановка браузера
    """
    browser, stop_browser = await get_nodriver(proxy=proxy)
    try:
        page = browser.main_tab
        def on_request(event: nodriver.cdp.network.RequestWillBeSent, page=None):
            """
            Обработчик сетевых запросов для извлечения токенов аутентификации.

            Args:
                event (nodriver.cdp.network.RequestWillBeSent): Объект события, содержащий информацию о запросе.
                page: Страница браузера.
            """
            if cls.api_base in event.request.url:
                if "X-Vqd-4" in event.request.headers:
                    cls.ddgs._chat_vqd = event.request.headers["X-Vqd-4"]
                if "X-Vqd-Hash-1" in event.request.headers:
                    cls.ddgs._chat_vqd_hash = event.request.headers["X-Vqd-Hash-1"]
                if "F-Fe-Version" in event.request.headers:
                    cls.ddgs._chat_xfe = event.request.headers["F-Fe-Version" ]
        await page.send(nodriver.cdp.network.enable())
        page.add_handler(nodriver.cdp.network.RequestWillBeSent, on_request)
        page = await browser.get(cls.url)
        while True:
            if cls.ddgs._chat_vqd:
                break
            await asyncio.sleep(1)
        await page.close()
    finally:
        stop_browser()
```

## Функции
В данном модуле функции отсутствуют.