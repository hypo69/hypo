# Модуль `ChatAnywhere`

## Обзор

Модуль `ChatAnywhere` предоставляет асинхронный интерфейс для взаимодействия с сервисом ChatAnywhere (`https://chatanywhere.cn`). Этот модуль предназначен для генерации текста на основе предоставленных сообщений с использованием модели GPT-3.5 Turbo. Он поддерживает проксирование запросов, настройку времени ожидания и температуры генерации.

## Подробней

Модуль использует асинхронные запросы (`aiohttp`) для взаимодействия с API ChatAnywhere. Он формирует заголовки и полезную нагрузку запроса, отправляет запрос и возвращает асинхронный генератор, который выдает чанки ответа.

## Классы

### `ChatAnywhere`

**Описание**: Класс `ChatAnywhere` является провайдером асинхронной генерации текста.

**Принцип работы**:
1.  Устанавливает URL (`https://chatanywhere.cn`) целевого сервиса.
2.  Поддерживает модель `gpt-3.5-turbo`.
3.  Поддерживает сохранение истории сообщений.
4.  Имеет флаг `working`, который показывает, что провайдер в данный момент работает (`False`).

**Методы**:

*   `create_async_generator`: Создает асинхронный генератор для получения ответов от ChatAnywhere.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    temperature: float = 0.5,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для получения ответов от ChatAnywhere.

    Args:
        model (str): Идентификатор модели для использования.
        messages (Messages): Список сообщений для отправки в запросе.
        proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
        timeout (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию `120`.
        temperature (float, optional): Температура генерации текста. По умолчанию `0.5`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий чанки текста.

    Raises:
        aiohttp.ClientResponseError: Если возникает HTTP ошибка при запросе.

    Как работает функция:
        1.  Функция `create_async_generator` создает асинхронный генератор для получения ответов от ChatAnywhere.
        2.  Определяет заголовки (`headers`) для HTTP-запроса, включая `User-Agent`, `Accept`, `Content-Type`, `Referer` и другие.
        3.  Создает асинхронную сессию (`ClientSession`) с заданными заголовками и таймаутом.
        4.  Формирует данные (`data`) для отправки в теле запроса, включая список сообщений, идентификатор, заголовок, параметры (`temperature`), используемые модели.
        5.  Отправляет асинхронный POST-запрос к API ChatAnywhere (`{cls.url}/v1/chat/gpt/`) с использованием созданной сессии, передавая данные в формате JSON и прокси-сервер (если указан).
        6.  Обрабатывает ответ от сервера и проверяет статус код ответа на наличие ошибок.
        7.  Итерируется по содержимому ответа чанками (`chunk`) и декодирует каждый чанк в строку, а затем выдает его через `yield`.

    Внутри функции происходят следующие действия и преобразования:

    A - Формирование заголовков запроса:
    |
    B - Создание асинхронной сессии:
    |
    C - Формирование данных запроса:
    |
    D - Отправка POST-запроса и получение ответа:
    |
    E - Обработка ответа и выдача чанков.

    Примеры:
        Пример 1: Использование без прокси
        ```python
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        async for chunk in ChatAnywhere.create_async_generator(model="gpt-3.5-turbo", messages=messages):
            print(chunk, end="")
        ```

        Пример 2: Использование с прокси
        ```python
        messages = [{"role": "user", "content": "Привет, как дела?"}]
        async for chunk in ChatAnywhere.create_async_generator(model="gpt-3.5-turbo", messages=messages, proxy="http://your_proxy:8080"):
            print(chunk, end="")
        ```

        Пример 3: Использование с указанием температуры
        ```python
        messages = [{"role": "user", "content": "Tell me a story."}]
        async for chunk in ChatAnywhere.create_async_generator(model="gpt-3.5-turbo", messages=messages, temperature=0.7):
            print(chunk, end="")
        ```
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Referer": f"{cls.url}/",
        "Origin": cls.url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Authorization": "",
        "Connection": "keep-alive",
        "TE": "trailers"
    }
    async with ClientSession(headers=headers, timeout=ClientTimeout(timeout)) as session:
        data = {
            "list": messages,
            "id": "s1_qYuOLXjI3rEpc7WHfQ",
            "title": messages[-1]["content"],
            "prompt": "",
            "temperature": temperature,
            "models": "61490748",
            "continuous": True
        }
        async with session.post(f"{cls.url}/v1/chat/gpt/", json=data, proxy=proxy) as response:
            response.raise_for_status()
            async for chunk in response.content.iter_any():
                if chunk:
                    yield chunk.decode()