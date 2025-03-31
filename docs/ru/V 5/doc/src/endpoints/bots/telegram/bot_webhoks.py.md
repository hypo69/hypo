# Модуль `telegram_webhooks`

## Обзор

Модуль `telegram_webhooks` предоставляет реализацию Telegram-бота, интегрированного с сервером FastAPI через RPC. Он позволяет обрабатывать входящие сообщения и команды от пользователей Telegram, а также регистрировать маршруты для вебхуков через RPC.

## Подробней

Этот модуль является ключевым компонентом системы для интеграции Telegram-бота с бэкэнд-сервером, использующим FastAPI. Он обеспечивает возможность динамического добавления маршрутов для обработки различных типов сообщений и команд, а также поддерживает работу через вебхуки или polling.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для взаимодействия с Telegram ботом. Он инициализирует бота, регистрирует обработчики команд и сообщений, а также запускает бота в режиме webhook или polling.

**Как работает класс**:
1.  **Инициализация**: При инициализации класса создается экземпляр `Application` из библиотеки `telegram.ext`, устанавливается токен бота, задается маршрут для вебхука и загружается конфигурация из файла `telegram.json`.
2.  **Регистрация обработчиков**: В методе `_register_default_handlers` регистрируются обработчики для различных команд и типов сообщений, таких как `/start`, `/help`, `/sendpdf`, текстовые сообщения, голосовые сообщения и документы.
3.  **Запуск бота**: Метод `run` запускает бота в режиме webhook или polling. Если настроен webhook, он регистрирует маршрут через RPC и запускает приложение с использованием `run_webhook`. В противном случае запускается polling через `run_polling`.
4.  **Остановка бота**: Метод `stop` останавливает бота и удаляет вебхук.

**Методы**:

*   `__init__(self, token: str, route: str = 'telegram_webhook')`: Инициализирует экземпляр класса `TelegramBot`.
*   `run(self)`: Запускает бота и инициализирует RPC и webhook.
*   `_register_default_handlers(self)`: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.
*   `initialize_bot_webhook(self, route: str)`: Инициализирует webhook бота.
*   `_register_route_via_rpc(self, rpc_client: ServerProxy)`: Регистрирует маршрут webhook Telegram через RPC.
*   `stop(self)`: Останавливает бота и удаляет webhook.

**Параметры**:

*   `token` (str): Токен Telegram-бота.
*   `route` (str, optional): Маршрут вебхука для FastAPI. По умолчанию `/telegram_webhook`.

### `__init__`

```python
 def __init__(self, token: str, route: str = 'telegram_webhook'):
        """
        Initialize the TelegramBot instance.

        Args:
            token (str): Telegram bot token.
            route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
        """
        self.token: str = token
        self.port: int = 443
        self.route: str = route
        self.config: SimpleNamespace = j_loads_ns(__root__ / 'src/endpoints/bots/telegram/telegram.json')
        self.application: Application = Application.builder().token(self.token).build()
        self.handler: BotHandler = BotHandler()
        self._register_default_handlers()
```

**Описание**: Инициализирует экземпляр класса `TelegramBot`.

**Как работает функция**:

1.  Сохраняет токен бота, порт и маршрут вебхука в атрибутах экземпляра.
2.  Загружает конфигурацию из файла `telegram.json` с использованием `j_loads_ns` и сохраняет ее в атрибуте `config`.
3.  Создает экземпляр `Application` из библиотеки `telegram.ext` с использованием предоставленного токена.
4.  Создает экземпляр класса `BotHandler` и сохраняет его в атрибуте `handler`.
5.  Вызывает метод `_register_default_handlers` для регистрации обработчиков команд и сообщений.

**Параметры**:

*   `token` (str): Токен Telegram-бота.
*   `route` (str, optional): Маршрут вебхука для FastAPI. По умолчанию `/telegram_webhook`.

### `run`

```python
 def run(self):
        """Run the bot and initialize RPC and webhook."""
        try:
            # Initialize RPC client
            rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)

            # Start the server via RPC
            rpc_client.start_server(self.port, gs.host)

            # Register the route via RPC
            # Динамическое добавление маршрутов
            

            logger.success(f'Server running at http://{gs.host}:{self.port}/hello')
        except Exception as ex:
            logger.error(f"Ошибка FastApiServer: {ex}", exc_info=True)
            sys.exit()




        # Initialize the Telegram bot webhook
        webhook_url = self.initialize_bot_webhook(self.route)
        # 
        if webhook_url:
            self._register_route_via_rpc(rpc_client)
            try:
                self.application.run_webhook(listen='0.0.0.0',
                                                         webhook_url=webhook_url, 
                                                         port=self.port)
                
                logger.info(f"Application started: {self.application.bot_data}")
                ...

            except Exception as ex:
                logger.error(f"Ошибка установки вебхука")
                ...

            ...
        else:
            self.application.run_polling()
            ...
```

**Описание**: Запускает бота и инициализирует RPC и webhook.

**Как работает функция**:

1.  Инициализирует RPC-клиент для взаимодействия с сервером FastAPI.
2.  Запускает сервер через RPC, используя порт и хост, указанные в конфигурации.
3.  Инициализирует webhook для Telegram-бота с использованием метода `initialize_bot_webhook`.
4.  Если webhook успешно инициализирован, регистрирует маршрут через RPC с помощью метода `_register_route_via_rpc` и запускает приложение в режиме webhook.
5.  Если webhook не настроен, запускает приложение в режиме polling.
6.  Обрабатывает возможные исключения при инициализации RPC, установке webhook и запуске приложения, логируя ошибки.

### `_register_default_handlers`

```python
 def _register_default_handlers(self):
        """Register the default handlers using the BotHandler instance."""
        self.application.add_handler(CommandHandler('start', self.handler.start))
        self.application.add_handler(CommandHandler('help', self.handler.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.handler.send_pdf))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handler.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handler.handle_document))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handler.handle_log))
```

**Описание**: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.

**Как работает функция**:

1.  Добавляет обработчики команд для `/start`, `/help` и `/sendpdf`, используя `CommandHandler`.
2.  Добавляет обработчик для текстовых сообщений, не являющихся командами, с использованием `MessageHandler` и фильтра `filters.TEXT & ~filters.COMMAND`.
3.  Добавляет обработчики для голосовых сообщений и документов, используя `MessageHandler` и соответствующие фильтры.

### `_handle_message`

```python
 async def _handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle any text message."""
        await self.bot_handler.handle_message(update, context)
```

**Описание**: Обрабатывает любое текстовое сообщение.

**Как работает функция**:

1.  Вызывает метод `handle_message` экземпляра `bot_handler` для обработки текстового сообщения.

**Параметры**:

*   `update` (Update): Объект `Update` от Telegram.
*   `context` (CallbackContext): Контекст обратного вызова.

### `initialize_bot_webhook`

```python
 def initialize_bot_webhook(self, route: str):
        """Initialize the bot webhook."""
        route = route if route.startswith('/') else f'/{route}'
        host = gs.host

        if host in ('127.0.0.1', 'localhost'):
            from pyngrok import ngrok
            ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN", ""))
            http_tunnel = ngrok.connect(self.port)
            host = http_tunnel.public_url

        host = host if host.startswith('http') else f'https://{host}'
        webhook_url = f'{host}{route}'

        _dev = True
        if _dev:
            import requests
            response = requests.post(f'{webhook_url}')
            print(response.json, text_color='green', bg_color='gray')

        try:
            self.application.bot.set_webhook(url=webhook_url)
            logger.success(f'https://api.telegram.org/bot{self.token}/getWebhookInfo') 
            return webhook_url
        except Exception as ex:
            logger.error(f'Error setting webhook: ',ex, exc_info=True)
            return False
```

**Описание**: Инициализирует webhook бота.

**Как работает функция**:

1.  Формирует URL для вебхука на основе хоста и маршрута.
2.  Если хост указан как `127.0.0.1` или `localhost`, использует `ngrok` для создания публичного URL.
3.  Устанавливает webhook для бота с использованием `self.application.bot.set_webhook`.
4.  Обрабатывает возможные исключения при установке webhook, логируя ошибки.

**Параметры**:

*   `route` (str): Маршрут вебхука.

**Возвращает**:

*   `str | False`: URL вебхука в случае успеха, `False` в случае ошибки.

### `_register_route_via_rpc`

```python
 def _register_route_via_rpc(self, rpc_client: ServerProxy):
        """Register the Telegram webhook route via RPC."""
        try:
            # Регистрация маршрута через RPC
            route = self.route if self.route.startswith('/') else f'/{self.route}'
            rpc_client.add_new_route(
                route,
                'self.bot_handler.handle_message',
                ['POST']
            )

            logger.info(f"Route {self.route} registered via RPC.")
        except Exception as ex:
            logger.error(f"Failed to register route via RPC:",ex, exc_info=True)
            ...
```

**Описание**: Регистрирует маршрут webhook Telegram через RPC.

**Как работает функция**:

1.  Формирует маршрут для регистрации через RPC.
2.  Вызывает метод `add_new_route` RPC-клиента для регистрации маршрута, указав метод обработки `'self.bot_handler.handle_message'` и разрешенные HTTP-методы `['POST']`.
3.  Обрабатывает возможные исключения при регистрации маршрута, логируя ошибки.

**Параметры**:

*   `rpc_client` (ServerProxy): RPC-клиент для взаимодействия с сервером.

### `stop`

```python
 def stop(self):
        """Stop the bot and delete the webhook."""
        try:
            self.application.stop()
            self.application.bot.delete_webhook()
            logger.info("Bot stopped.")
        except Exception as ex:
            logger.error(f'Error deleting webhook:',ex, exc_info=True)
```

**Описание**: Останавливает бота и удаляет webhook.

**Как работает функция**:

1.  Останавливает приложение с помощью `self.application.stop()`.
2.  Удаляет webhook с использованием `self.application.bot.delete_webhook()`.
3.  Обрабатывает возможные исключения при остановке бота и удалении webhook, логируя ошибки.