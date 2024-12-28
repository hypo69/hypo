
Код устанавливает и запускает aiohttp-сервер, который слушает входящие webhook-и от Telegram, обрабатывает их, вызывая нужные обработчики телеграм бота. Сама логика обработки сообщений теперь находится в классе `BotHandler` благодаря вызову `await self.bot_handler.handle_message(update, context)`.


**Структура кода:**

Файл `bot_web_hooks.py` определяет класс `TelegramBot` и функции для настройки и запуска aiohttp-приложения, обрабатывающего webhook-и Telegram.

**Класс `TelegramBot`:**

1.  **`__init__(self, token: str, bot_handler)`:**
    *   Инициализирует экземпляр телеграм-бота.
    *   Принимает токен бота и экземпляр `bot_handler` (который содержит логику обработки сообщений).
    *   Загружает конфигурацию (`_load_config`) из JSON-файла.
    *   Создает экземпляр `telegram.ext.Application` с использованием токена бота.
    *   Сохраняет переданный `bot_handler`.
    *   Регистрирует обработчики команд и сообщений (`register_handlers`).

2.  **`_load_config(self, config_path: str | Path)`:**
    *   Загружает конфигурацию из JSON-файла.
    *   Получает значения `host` и `port` из конфигурации. Если конфигурация не найдена, то устанавливаются дефолтные значения.

3.  **`register_handlers(self)`:**
    *   Регистрирует обработчики для разных типов сообщений:
        *   `/start`: `self.start`
        *   `/help`: `self.help_command`
        *   `/sendpdf`: `self.send_pdf`
        *   Текстовые сообщения (не команды): `self.handle_message`
        *   Голосовые сообщения: `self.handle_voice`
        *   Документы: `self.handle_document`
        *   Лог-сообщения: `self.handle_log`
4.  **Обработчики (`start`, `help_command`, `send_pdf`, `handle_voice`, `handle_document`, `handle_message`, `handle_log`)**:
    *   Каждый из этих методов обрабатывает соответствующий тип сообщений от пользователя.
    *   `handle_message` вызывает `bot_handler.handle_message`, передавая ему `update` и `context`, чтобы логика обработки сообщения была в `BotHandler`.
    *   Остальные обрабатывают команды и типы сообщений (документы, голос, лог).

**Функции aiohttp для обработки webhook:**

1.  **`update_webhook_handler(request: web.Request) -> web.Response`:**
    *   **Главная функция обработчика webhook-ов**.
    *   Принимает объект `web.Request` от aiohttp (представляет входящий HTTP POST-запрос).
    *   Извлекает данные JSON из тела запроса `data = await request.json()`.
    *   Получает экземпляр `bot` из приложения (`app = request.app`, `bot = app['bot']`)
    *   Обрабатывает запрос,  передавая данные в `bot.application.process_update` с использованием `Update.de_json`. Это преобразует JSON из запроса Telegram в объект `Update` и передает его в Telegram Bot API.
    *   Возвращает пустой `web.Response()` в случае успешной обработки или  `web.Response(status=500)` в случае ошибки.

2.  **`on_startup(app: web.Application)`:**
    *   Вызывается при запуске приложения aiohttp.
    *   Устанавливает webhook для бота с помощью `bot.application.bot.set_webhook` по адресу который задан в `gs.settings.get_webhook_url`.

3.  **`on_shutdown(app: web.Application)`:**
    *   Вызывается при остановке приложения aiohttp.
    *   Удаляет webhook для бота с помощью `bot.application.bot.delete_webhook`.

4.  **`setup_application(app: web.Application, application: Application)`:**
     *   `setup_application` используется для настройки приложения телеграм-бота, чтобы оно могло отвечать через webhook.
     *  Внутренняя функция `update_webhook_handler` получает данные из запроса и отправляет их на обработку в телеграм-бота.
     *  `app['webhook_handler']` - сохраняет функцию, как handler для дальнейшего использования
    
5. **`create_app(bot: TelegramBot) -> web.Application`:**
   *   Создает и настраивает aiohttp-приложение.
   *   `app['bot'] = bot`: Сохраняет экземпляр бота в приложении aiohttp для дальнейшего использования.
   *   `app.router.add_post('/webhook', update_webhook_handler)`: Регистрирует функцию `update_webhook_handler` как обработчик для POST-запросов на путь `/webhook`.
   *  `app.on_startup.append(on_startup)`: Добавляет функцию `on_startup` в список функций, которые будут выполняться при запуске приложения
   * `app.on_shutdown.append(on_shutdown)`: Добавляет функцию `on_shutdown` в список функций, которые будут выполняться при остановке приложения
   *  `setup_application(app, bot.application)`: Настраивает приложение, чтобы оно могло получать данные от телеграм, через webhook
   *   Возвращает сконфигурированное приложение aiohttp.

**Общий поток работы:**

1.  **Инициализация:**
    *   Экземпляр `TelegramBot` создается, передавая ему токен и `bot_handler`.
    *   Экземпляр `aiohttp.web.Application` создается с помощью `create_app()`, и в него передается `TelegramBot`.
    *   Сервер aiohttp запускается с помощью `web.run_app(app, host=bot.host, port=bot.port)`.

2.  **Webhook-запрос:**
    *   Telegram отправляет POST-запрос на `/webhook`.
    *   Aiohttp принимает этот запрос и направляет его в функцию `update_webhook_handler`.

3.  **Обработка запроса:**
    *   `update_webhook_handler` извлекает данные JSON из запроса.
    *   `update_webhook_handler` передает JSON данные в `bot.application.process_update`.
    *   `telegram.ext.Application` обрабатывает `Update`  и вызывает соответствующий обработчик (например `handle_message`)

4.  **Ответ:**
    *   `update_webhook_handler` возвращает пустой `web.Response`.
    *   Бот отвечает на сообщение пользователя, используя Telegram Bot API.

