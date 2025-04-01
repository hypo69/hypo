# Модуль вебхуков Telegram

## Обзор

Модуль `src.endpoints.bots.telegram.webhooks` предоставляет функции для обработки вебхуков Telegram через сервер FastAPI. Он позволяет принимать и обрабатывать обновления от Telegram бота.

## Подробней

Этот модуль является частью системы взаимодействия с Telegram ботом через FastAPI. Он отвечает за прием и обработку входящих вебхуков от Telegram, используя библиотеку `python-telegram-bot`.

## Функции

### `telegram_webhook`

```python
def telegram_webhook(request: Request, application: Application):
    """
    Обрабатывает входящие HTTP-запросы, инициируя асинхронную обработку вебхука Telegram.

    Args:
        request (Request): Объект запроса FastAPI.
        application (Application): Объект приложения `telegram.ext.Application`.

    Returns:
        None

    Как работает функция:
    1. Функция принимает объект запроса `request` и объект приложения `application` в качестве параметров.
    2. Использует `asyncio.run`, чтобы запустить асинхронную функцию `telegram_webhook_async` в синхронном контексте.
       Это необходимо, поскольку FastAPI может работать в асинхронном режиме, а некоторые части кода могут требовать синхронного выполнения.
    3. Функция передаёт управление асинхронной функции `telegram_webhook_async` для дальнейшей обработки запроса.

    Внутри функции происходят следующие действия и преобразования:
    Запуск асинхронной функции в синхронном контексте.
    """
    ...
```

### `telegram_webhook_async`

```python
async def telegram_webhook_async(request: Request, application: Application):
    """
    Асинхронно обрабатывает входящие webhook запросы от Telegram.

    Args:
        request (Request): Объект запроса FastAPI.
        application (Application): Объект приложения `telegram.ext.Application`.

    Returns:
        Response: Объект ответа FastAPI с соответствующим кодом состояния.

    Raises:
        json.JSONDecodeError: Если не удается декодировать JSON из запроса.
        Exception: Если возникает любая другая ошибка при обработке вебхука.

    Как работает функция:
    1. Функция принимает объект запроса `request` и объект приложения `application` в качестве параметров.
    2. Извлекает JSON из тела запроса с использованием `await request.json()`.
    3. Использует асинхронный контекстный менеджер `async with application:` для управления ресурсами приложения `telegram.ext.Application`.
    4. Преобразует JSON в объект `Update` с использованием `Update.de_json(data, application.bot)` и передает его в приложение для обработки с использованием `await application.process_update(update)`.
    5. В случае успешной обработки возвращает `Response` с кодом состояния 200.
    6. Если происходит ошибка декодирования JSON, логирует ошибку с использованием `logger.error` и возвращает `Response` с кодом состояния 400 и сообщением об ошибке.
    7. Если происходит любая другая ошибка, логирует ошибку с использованием `logger.error` и возвращает `Response` с кодом состояния 500 и сообщением об ошибке.

    Внутри функции происходят следующие действия и преобразования:
    Получение JSON из тела запроса.
    |
    -- Преобразование JSON в объект `Update`.
    |
    Обработка обновления приложением.

    Примеры:
    Пример успешного вызова:
    ```python
    async def test_telegram_webhook_async_success():
        from unittest.mock import AsyncMock
        request_mock = AsyncMock()
        request_mock.json.return_value = {"message": {"text": "test"}}
        application_mock = AsyncMock()
        application_mock.__aenter__.return_value = application_mock
        application_mock.bot = AsyncMock()
        application_mock.process_update = AsyncMock()

        response = await telegram_webhook_async(request_mock, application_mock)

        assert response.status_code == 200
        application_mock.process_update.assert_called_once()
    ```

    Пример ошибки JSONDecodeError:
    ```python
    async def test_telegram_webhook_async_json_decode_error():
        from unittest.mock import AsyncMock
        request_mock = AsyncMock()
        request_mock.json.side_effect = json.JSONDecodeError("Invalid JSON", "doc", 0)
        application_mock = AsyncMock()

        response = await telegram_webhook_async(request_mock, application_mock)

        assert response.status_code == 400
        assert "Invalid JSON" in response.body.decode()
    ```

    Пример обработки исключения:
    ```python
     async def test_telegram_webhook_async_exception():
        from unittest.mock import AsyncMock

        request_mock = AsyncMock()
        request_mock.json.side_effect = Exception("Test Exception")
        application_mock = AsyncMock()
        application_mock.__aenter__.return_value = application_mock

        response = await telegram_webhook_async(request_mock, application_mock)

        assert response.status_code == 500
        assert "Test Exception" in response.body.decode()
    ```
    """
    ...