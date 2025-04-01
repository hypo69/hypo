# Модуль Aichat

## Обзор

Модуль `Aichat` предоставляет асинхронный интерфейс для взаимодействия с сервисом `chat-gpt.org`. Он позволяет отправлять запросы к модели GPT-3.5 Turbo и получать ответы. Этот модуль является частью коллекции провайдеров для работы с различными AI-моделями. Модуль предназначен для использования в асинхронных приложениях, где требуется неблокирующий ввод-вывод.

## Подробнее

Модуль использует библиотеку `requests` для выполнения асинхронных HTTP-запросов. Для аутентификации используются cookies, полученные с сайта `chat-gpt.org`. Модуль поддерживает установку прокси-сервера для выполнения запросов.
Расположение файла в проекте: `hypotez/src/endpoints/gpt4free/g4f/Provider/deprecated/Aichat.py` указывает на то, что это один из устаревших провайдеров, возможно, с ограниченной поддержкой или функциональностью.

## Классы

### `Aichat`

**Описание**:
Класс `Aichat` предоставляет асинхронный интерфейс для взаимодействия с сервисом `chat-gpt.org`. Он позволяет отправлять запросы к модели GPT-3.5 Turbo и получать ответы.

**Принцип работы**:
Класс использует асинхронные запросы для обмена данными с сервером `chat-gpt.org`. Он форматирует сообщения, устанавливает необходимые заголовки и обрабатывает ответы, возвращая результат или вызывая исключение в случае ошибки.

**Параметры**:
- `url` (str): URL-адрес сервиса `chat-gpt.org`.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель GPT-3.5 Turbo.

**Методы**:
- `create_async`: Асинхронный метод для отправки запроса к модели и получения ответа.

## Функции

### `create_async`

```python
    @staticmethod
    async def create_async(
        model: str,
        messages: Messages,
        proxy: str = None, **kwargs) -> str:
        """
        Отправляет асинхронный запрос к модели GPT-3.5 Turbo и возвращает ответ.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            **kwargs: Дополнительные аргументы, такие как cookies и параметры запроса.

        Returns:
            str: Ответ от модели.

        Raises:
            RuntimeError: Если не удалось получить cookies.
            Exception: Если получен ошибочный ответ от сервера.

        Как работает функция:
        1. Функция пытается получить cookies с сайта `chat-gpt.org`, если они не переданы в аргументе `kwargs`. Если cookies получить не удается, выбрасывается исключение `RuntimeError`.
        2. Формируются заголовки запроса, включая User-Agent, Accept и Content-Type.
        3. Создается асинхронная сессия с использованием `StreamSession`, устанавливаются заголовки, cookies, timeout и прокси (если указан).
        4. Формируется JSON-тело запроса, включающее отформатированные сообщения, температуру, параметры presence_penalty, top_p и frequency_penalty.
        5. Отправляется POST-запрос к API `chat-gpt.org` с использованием асинхронной сессии.
        6. Обрабатывается ответ от сервера, проверяется статус код и извлекается результат.
        7. Если в ответе отсутствует поле `response` или оно пустое, выбрасывается исключение `Exception`.
        8. Возвращается текстовое сообщение из ответа.

        Внутри функции происходят следующие действия и преобразования:
        A. Получение cookies: Проверяется наличие cookies в аргументах `kwargs`, в противном случае делается попытка получить их с сайта `chat-gpt.org`.
        |
        B. Формирование заголовков: Создается словарь с необходимыми HTTP-заголовками для запроса.
        |
        C. Создание асинхронной сессии: Инициализируется `StreamSession` с заданными заголовками, cookies, таймаутом и прокси.
        |
        D. Формирование JSON-тела запроса: Создается словарь с данными, отправляемыми в теле POST-запроса.
        |
        E. Отправка POST-запроса: Выполняется асинхронный POST-запрос к API `chat-gpt.org`.
        |
        F. Обработка ответа: Анализируется ответ от сервера на наличие ошибок и извлекается текстовое сообщение.

        Примеры:
            1.  Вызов функции с минимальным набором параметров:
            ```python
            await Aichat.create_async(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}])
            ```

            2.  Вызов функции с указанием прокси-сервера:
            ```python
            await Aichat.create_async(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], proxy="http://proxy.example.com")
            ```

            3.  Вызов функции с передачей cookies и изменением температуры:
            ```python
            await Aichat.create_async(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], cookies={"cookie_name": "cookie_value"}, temperature=0.7)
            ```
        """

        cookies = get_cookies('chat-gpt.org') if not kwargs.get('cookies') else kwargs.get('cookies')
        if not cookies:
            raise RuntimeError(
                "g4f.provider.Aichat requires cookies, [refresh https://chat-gpt.org on chrome]"
            )

        headers = {
            'authority': 'chat-gpt.org',
            'accept': '*/*',
            'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
            'content-type': 'application/json',
            'origin': 'https://chat-gpt.org',
            'referer': 'https://chat-gpt.org/chat',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

        async with StreamSession(headers=headers,
                                    cookies=cookies,
                                    timeout=6,
                                    proxies={"https": proxy} if proxy else None,
                                    impersonate="chrome110", verify=False) as session:

            json_data = {
                "message": format_prompt(messages),
                "temperature": kwargs.get('temperature', 0.5),
                "presence_penalty": 0,
                "top_p": kwargs.get('top_p', 1),
                "frequency_penalty": 0,
            }

            async with session.post("https://chat-gpt.org/api/text",
                                    json=json_data) as response:

                response.raise_for_status()
                result = await response.json()

                if not result['response']:
                    raise Exception(f"Error Response: {result}")

                return result["message"]