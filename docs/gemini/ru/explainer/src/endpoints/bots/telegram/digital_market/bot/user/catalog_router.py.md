## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    - **Переменные**: Их типы и использование.
    - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

```mermaid
flowchart TD
    Start[Начало] --> CatalogCallback[Обработка callback_query "catalog"];
    CatalogCallback -- "Запрос категорий" --> FindAllCategories[CategoryDao.find_all]
    FindAllCategories -- "Получены категории" --> CatalogKeyboard[Генерация клавиатуры catalog_kb]
    CatalogKeyboard --> SendCatalogMessage[Отправка сообщения с категориями]
    SendCatalogMessage --> CategoryCallback[Обработка callback_query "category_*"]
    CategoryCallback -- "Извлечение category_id" --> FindProducts[ProductDao.find_all]
    FindProducts -- "Получены продукты" --> CheckProducts[Проверка наличия продуктов]
    CheckProducts -- "Продукты есть" --> LoopProducts[Цикл по продуктам]
    LoopProducts -- "Для каждого продукта" --> ProductText[Формирование текста продукта]
    ProductText --> ProductKeyboard[Генерация клавиатуры product_kb]
    ProductKeyboard --> SendProductMessage[Отправка сообщения с продуктом]
    SendProductMessage -- "Конец цикла" --> CheckProducts
    CheckProducts -- "Нет продуктов" --> AnswerNoProducts[Ответ о отсутствии продуктов]
    AnswerNoProducts --> End[Конец]
    CategoryCallback -- "Неудачный запрос" --> AnswerNoProducts
    SendCatalogMessage -- "Неудачный запрос" --> AnswerNoProducts
    LoopProducts -- "Конец цикла" --> ProductCallback[Обработка callback_query "buy_*"]
    ProductCallback -- "Разделение данных" --> CheckPaymentType[Проверка типа оплаты]
    CheckPaymentType -- "yukassa" --> SendYukassaInvoice[Вызов send_yukassa_invoice]
    CheckPaymentType -- "stars" --> SendStarsInvoice[Вызов send_stars_invoice]
    CheckPaymentType -- "robocassa" --> SendRobocassaInvoice[Вызов send_robocassa_invoice]
    SendYukassaInvoice --> SendInvoiceYookassa[Отправка инвойса через bot.send_invoice (Юкасса)]
    SendInvoiceYookassa --> DeleteMessage[Удаление сообщения]
     SendStarsInvoice --> SendInvoiceStars[Отправка инвойса через bot.send_invoice (Звезды)]
    SendInvoiceStars --> DeleteMessage
    SendRobocassaInvoice --> GeneratePaymentLink[Генерация ссылки на оплату Robokassa]
    GeneratePaymentLink --> SendRobocassaMessage[Отправка сообщения с ссылкой Robokassa]
    SendRobocassaMessage --> DeleteMessage
    DeleteMessage --> PreCheckoutQuery[Обработка pre_checkout_query]
    PreCheckoutQuery --> AnswerPreCheckoutQuery[bot.answer_pre_checkout_query]
    AnswerPreCheckoutQuery --> SuccessfulPayment[Обработка successful_payment]
    SuccessfulPayment -- "Разделение payload" --> CheckStarsPayment[Проверка типа оплаты (звезды)]
    CheckStarsPayment -- "Звезды" --> StarsPayment[Обработка оплаты звездами]
    CheckStarsPayment -- "Не звезды" --> RubPayment[Обработка оплаты рублями]
    StarsPayment --> PaymentDataStars[Формирование данных об оплате (звезды)]
    RubPayment --> PaymentDataRub[Формирование данных об оплате (рубли)]
    PaymentDataStars --> SuccessLogic[Вызов successful_payment_logic]
     PaymentDataRub --> SuccessLogic
     SuccessLogic --> End
    
```

**Примеры:**

1.  **Начало**: Пользователь нажимает кнопку "Каталог".
2.  **Обработка callback\_query "catalog"**: Выполняется функция `page_catalog`.
3.  **CategoryDao.find\_all**: Запрос к базе данных на получение списка категорий.
    *   Пример: `[Category(id=1, name="Электроника"), Category(id=2, name="Книги")]`
4.  **Генерация клавиатуры catalog\_kb**: Создание кнопок с названиями категорий.
    *   Пример: Кнопки "Электроника", "Книги".
5.  **Отправка сообщения с категориями**: Пользователю отправляется сообщение с выбором категорий.
6.  **Обработка callback\_query "category\_\*"**: Пользователь выбирает категорию, например "Электроника" (`category_1`). Выполняется функция `page_catalog_products`.
7.  **ProductDao.find\_all**: Запрос в базу данных на получение списка товаров для выбранной категории.
    *   Пример: `[Product(id=1, name="Телефон", price=10000, description="...", category_id=1), Product(id=2, name="Ноутбук", price=50000, description="...", category_id=1)]`
8.  **Проверка наличия продуктов**: Если есть товары, то для каждого товара:
    *   Формируется текстовое описание продукта.
        *   Пример: "📦 **Название товара:** Телефон\n\n💰 **Цена:** 10000 руб.\n\n📝 **Описание:**\n*...\*\n\n━━━━━━━━━━━━━━━━━━"
    *   Создается клавиатура с кнопкой "Купить" для каждого товара.
        *   Пример: Кнопка "Купить" (`buy_yukassa_1_10000`, `buy_stars_1_10`, `buy_robocassa_1_10000`)
9.  **Отправка сообщения с товаром**: Сообщение с описанием и кнопкой "Купить" отправляется пользователю.
10. **Обработка callback\_query "buy\_\*"**: Пользователь нажимает кнопку "Купить" (например, `buy_yukassa_1_10000`). Выполняется функция `process_about`.
11. **Проверка типа оплаты**: Определяется тип оплаты ("yukassa", "stars", "robocassa") и вызывается соответствующая функция (например, `send_yukassa_invoice`).
12. **Отправка инвойса/сообщения об оплате**: В зависимости от типа оплаты, отправляется инвойс через `bot.send_invoice` или ссылка на оплату.
13. **Обработка pre\_checkout\_query**: Обработка предварительного запроса перед оплатой.
14. **Обработка successful\_payment**: Обработка успешной оплаты, получение данных об оплате.
15. **Формирование данных об оплате**: Извлекаются данные из payload и формируется словарь `payment_data`.
16. **Вызов successful\_payment\_logic**: Функция `successful_payment_logic` вызывается для завершения логики оплаты.

## <mermaid>

```mermaid
flowchart TD
    Start([Начало])
    Start --> catalog_router_callback_catalog{catalog_router.callback_query(F.data == "catalog")}
    catalog_router_callback_catalog -- CallbackQuery, AsyncSession --> page_catalog[page_catalog(call: CallbackQuery, session_without_commit: AsyncSession)]
    page_catalog --> CategoryDao_find_all[CategoryDao.find_all(session=session_without_commit)]
    CategoryDao_find_all -- List[Category] --> catalog_kb_function[catalog_kb(catalog_data)]
    catalog_kb_function -- InlineKeyboardMarkup --> bot_send_message_catalog[bot.send_message(reply_markup=catalog_kb)]
    bot_send_message_catalog --> catalog_router_callback_category{catalog_router.callback_query(F.data.startswith("category_"))}
    catalog_router_callback_category -- CallbackQuery, AsyncSession --> page_catalog_products[page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession)]
    page_catalog_products --> ProductDao_find_all[ProductDao.find_all(session=session_without_commit, filters=ProductCategoryIDModel)]
    ProductDao_find_all -- List[Product] --> loop_products{for product in products_category}
    loop_products -- Product --> format_product_text[Формирование текста продукта]
    format_product_text -- str --> product_kb_function[product_kb(product.id, product.price, 1)]
    product_kb_function -- InlineKeyboardMarkup --> bot_send_message_product[bot.send_message(reply_markup=product_kb)]
    bot_send_message_product --> loop_products
    loop_products -- Конец цикла --> catalog_router_callback_buy{catalog_router.callback_query(F.data.startswith('buy_'))}
    catalog_router_callback_buy -- CallbackQuery, AsyncSession --> process_about[process_about(call: CallbackQuery, session_without_commit: AsyncSession)]
    process_about --> UserDAO_find_one_or_none[UserDAO.find_one_or_none(session=session_without_commit, filters=TelegramIDModel)]
    UserDAO_find_one_or_none -- User --> check_payment_type{if payment_type == "yukassa/stars/robocassa"}
    check_payment_type -- "yukassa" --> send_yukassa_invoice_func[send_yukassa_invoice(call, user_info, product_id, price)]
    check_payment_type -- "stars" --> send_stars_invoice_func[send_stars_invoice(call, user_info, product_id, stars_price)]
    check_payment_type -- "robocassa" --> send_robocassa_invoice_func[send_robocassa_invoice(call, user_info, product_id, price, session_without_commit)]
    send_yukassa_invoice_func --> bot_send_invoice_yukassa[bot.send_invoice(provider_token=settings.PROVIDER_TOKEN, reply_markup=get_product_buy_youkassa(price))]
    send_stars_invoice_func --> bot_send_invoice_stars[bot.send_invoice(currency='XTR', reply_markup=get_product_buy_stars(stars_price))]
    send_robocassa_invoice_func --> generate_payment_link_func[generate_payment_link(cost=float(price), number=pay_id, description=description, user_id=user_info.id, user_telegram_id=call.from_user.id, product_id=product_id)]
    generate_payment_link_func --> get_product_buy_robocassa_func[get_product_buy_robocassa(price, payment_link)]
     get_product_buy_robocassa_func --> bot_send_message_robocassa[bot.send_message(reply_markup=kb)]
    bot_send_invoice_yukassa --> catalog_router_pre_checkout_query{catalog_router.pre_checkout_query(lambda query: True)}
    bot_send_invoice_stars --> catalog_router_pre_checkout_query
    bot_send_message_robocassa --> catalog_router_pre_checkout_query
     catalog_router_pre_checkout_query -- PreCheckoutQuery --> pre_checkout_query_func[pre_checkout_query(pre_checkout_q: PreCheckoutQuery)]
    pre_checkout_query_func --> bot_answer_pre_checkout_query[bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)]
    bot_answer_pre_checkout_query --> catalog_router_successful_payment{catalog_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)}
    catalog_router_successful_payment -- Message, AsyncSession --> successful_payment_func[successful_payment(message: Message, session_with_commit: AsyncSession)]
     successful_payment_func --> payment_info_split[payment_info.invoice_payload.split('_')]
     payment_info_split --> check_stars_payment{if payment_type == 'stars'}
     check_stars_payment -- "stars" --> stars_payment[Обработка оплаты звездами]
     check_stars_payment -- "не звезды" --> rub_payment[Обработка оплаты рублями]
      stars_payment --> create_payment_data_stars[Создание словаря payment_data (звезды)]
       rub_payment --> create_payment_data_rub[Создание словаря payment_data (рубли)]
      create_payment_data_stars --> successful_payment_logic_call[successful_payment_logic(session=session_with_commit, payment_data=payment_data, currency=currency, user_tg_id=message.from_user.id, bot=bot)]
      create_payment_data_rub --> successful_payment_logic_call
    successful_payment_logic_call --> End([Конец])
```

**Анализ зависимостей `mermaid`:**

1.  `aiogram`:
    *   `Router`: Используется для создания роутера (`catalog_router`), который обрабатывает входящие запросы.
    *   `F`: Используется для фильтрации входящих запросов, например, `F.data == "catalog"`.
    *   `ContentType`: Используется для фильтрации сообщений по типу контента, например, `ContentType.SUCCESSFUL_PAYMENT`.
    *   `Message`: Тип данных для входящих сообщений от Telegram.
    *   `CallbackQuery`: Тип данных для входящих callback запросов от Telegram.
    *   `LabeledPrice`: Используется для создания цен для инвойсов.
    *   `PreCheckoutQuery`: Тип данных для предварительных запросов перед оплатой.
2.  `sqlalchemy.ext.asyncio`:
    *   `AsyncSession`: Используется для асинхронного взаимодействия с базой данных.
3.  `bot.app.utils`:
    *   `generate_payment_link`: Используется для генерации ссылок на оплату через Robokassa.
4.  `bot.config`:
    *   `bot`: Экземпляр бота aiogram.
    *   `settings`: Настройки проекта, включая `PROVIDER_TOKEN` для Юкассы.
5.  `bot.dao.dao`:
    *   `UserDAO`: DAO для работы с пользователями в базе данных.
    *   `CategoryDao`: DAO для работы с категориями товаров в базе данных.
    *   `ProductDao`: DAO для работы с товарами в базе данных.
    *    `PurchaseDao`: DAO для работы с покупками в базе данных.
6.  `bot.user.kbs`:
    *   `catalog_kb`: Функция для генерации клавиатуры с категориями.
    *   `product_kb`: Функция для генерации клавиатуры для товаров.
    *    `get_product_buy_youkassa`: Функция для генерации клавиатуры для покупки через Юкасса.
    *    `get_product_buy_stars`: Функция для генерации клавиатуры для покупки за звезды.
    *    `get_product_buy_robocassa`: Функция для генерации клавиатуры для покупки через Robokassa.
7.  `bot.user.schemas`:
    *   `TelegramIDModel`: Pydantic модель для фильтрации пользователей по telegram_id.
    *   `ProductCategoryIDModel`: Pydantic модель для фильтрации товаров по category_id.
    *    `PaymentData`: Pydantic модель для данных об оплате.
8. `bot.user.utils`:
    *  `successful_payment_logic`: Функция для обработки успешной оплаты.

## <объяснение>

**Импорты:**

*   `aiogram`: Библиотека для создания Telegram ботов.
    *   `Router`: Класс для создания роутеров, которые распределяют входящие обновления.
    *   `F`: Объект для фильтрации обновлений по разным условиям.
    *   `ContentType`: Перечисление типов контента сообщений (текст, фото, успешная оплата и т.д.).
    *   `Message`, `CallbackQuery`, `LabeledPrice`, `PreCheckoutQuery`: Типы данных для входящих сообщений, коллбеков, цен для инвойсов и предварительных запросов перед оплатой.
*   `sqlalchemy.ext.asyncio`: Библиотека для асинхронного взаимодействия с базой данных.
    *   `AsyncSession`: Класс для создания асинхронных сессий для работы с базой данных.
*   `bot.app.utils`:
    *   `generate_payment_link`: Функция для генерации ссылки на оплату через Robokassa.
*   `bot.config`:
    *   `bot`: Экземпляр бота, созданный с помощью aiogram.
    *   `settings`: Объект с настройками проекта, включая токен провайдера оплаты (Юкасса).
*   `bot.dao.dao`: Модуль с Data Access Objects (DAO) для взаимодействия с базой данных.
    *   `UserDAO`, `CategoryDao`, `ProductDao`, `PurchaseDao`: DAO для доступа к данным пользователей, категорий, товаров и покупок.
*   `bot.user.kbs`: Модуль с функциями для генерации клавиатур для разных этапов работы с каталогом.
    *   `catalog_kb`, `product_kb`: Функции для генерации клавиатур категорий и товаров.
    *   `get_product_buy_youkassa`, `get_product_buy_stars`, `get_product_buy_robocassa`: Функции для создания клавиатур для оплаты различными способами.
*   `bot.user.schemas`: Модуль с Pydantic моделями для валидации данных.
    *   `TelegramIDModel`, `ProductCategoryIDModel`, `PaymentData`: Модели для фильтрации пользователей по ID, фильтрации товаров по ID категории и валидации данных об оплате.
*   `bot.user.utils`:
    *   `successful_payment_logic`: Функция для обработки логики успешной оплаты.

**Классы:**

*   `catalog_router = Router()`: Создание роутера для обработки запросов, связанных с каталогом. Роутер используется для маршрутизации входящих обновлений от Telegram.

**Функции:**

*   `page_catalog(call: CallbackQuery, session_without_commit: AsyncSession)`:
    *   Аргументы: `call` (CallbackQuery), `session_without_commit` (AsyncSession).
    *   Назначение: Обрабатывает запрос на показ каталога.
    *   Пример: Пользователь нажимает кнопку "Каталог".
    *   Возвращает: `None`.
    1.  Отвечает на колбек `call.answer("Загрузка каталога...")`.
    2.  Удаляет предыдущее сообщение с кнопкой "Каталог" через  `call.message.delete()`.
    3.  Получает список всех категорий с помощью `CategoryDao.find_all(session=session_without_commit)`.
    4.  Отправляет сообщение с клавиатурой выбора категорий `call.message.answer(...)` с использованием функции `catalog_kb()`.
*   `page_catalog_products(call: CallbackQuery, session_without_commit: AsyncSession)`:
    *   Аргументы: `call` (CallbackQuery), `session_without_commit` (AsyncSession).
    *   Назначение: Обрабатывает выбор категории и отображает список товаров в ней.
    *   Пример: Пользователь выбирает категорию "Электроника".
    *   Возвращает: `None`.
    1.  Извлекает `category_id` из данных коллбека `call.data`.
    2.  Получает список товаров по выбранной категории с помощью `ProductDao.find_all(...)`.
    3.  Если товары есть, то для каждого товара:
        *   Формирует текст описания товара.
        *   Отправляет сообщение с описанием товара и кнопкой "Купить" `call.message.answer(...)` используя `product_kb()`.
    4.  Если нет товаров, сообщает, что в данной категории нет товаров `call.answer("В данной категории нет товаров.")`.
*   `process_about(call: CallbackQuery, session_without_commit: AsyncSession)`:
    *   Аргументы: `call` (CallbackQuery), `session_without_commit` (AsyncSession).
    *   Назначение: Обрабатывает запрос на покупку товара.
    *   Пример: Пользователь нажимает кнопку "Купить" (например, `buy_yukassa_1_10000`).
    *   Возвращает: `None`.
    1.  Получает информацию о пользователе из базы данных через `UserDAO.find_one_or_none(...)`.
    2.  Разделяет данные из коллбека `call.data` на тип оплаты, ID товара и цену.
    3.  В зависимости от типа оплаты (`yukassa`, `stars`, `robocassa`), вызывает соответствующую функцию (`send_yukassa_invoice`, `send_stars_invoice`, `send_robocassa_invoice`).
    4.  Удаляет предыдущее сообщение `call.message.delete()`.
*   `send_yukassa_invoice(call, user_info, product_id, price)`:
    *   Аргументы: `call` (CallbackQuery), `user_info` (User), `product_id` (int), `price` (int).
    *   Назначение: Отправляет инвойс для оплаты через Юкассу.
    *   Пример: После выбора варианта оплаты Юкасса.
    *   Возвращает: `None`.
    1.  Отправляет инвойс через `bot.send_invoice(...)` с необходимыми параметрами (ID чата, заголовок, описание, payload, токен провайдера, валюта, цены) и клавиатурой `get_product_buy_youkassa()`.
*   `send_robocassa_invoice(call, user_info, product_id, price, session: AsyncSession)`:
    *   Аргументы: `call` (CallbackQuery), `user_info` (User), `product_id` (int), `price` (int), `session` (AsyncSession).
    *   Назначение: Генерирует ссылку на оплату через Robokassa и отправляет пользователю.
    *   Пример: После выбора варианта оплаты Robokassa.
    *   Возвращает: `None`.
    1.  Получает следующий ID покупки через `PurchaseDao.get_next_id(session=session)`.
    2.  Формирует описание платежа.
    3.  Генерирует ссылку на оплату через `generate_payment_link(...)`.
    4.  Создает клавиатуру с кнопкой для перехода к оплате, используя `get_product_buy_robocassa(...)`.
    5.  Отправляет сообщение с ссылкой и клавиатурой `call.message.answer(...)`.
*   `send_stars_invoice(call, user_info, product_id, stars_price)`:
    *   Аргументы: `call` (CallbackQuery), `user_info` (User), `product_id` (int), `stars_price` (int).
    *   Назначение: Отправляет инвойс для оплаты "звездами".
    *   Пример: После выбора варианта оплаты "звездами".
    *   Возвращает: `None`.
    1.  Отправляет инвойс через `bot.send_invoice(...)` с необходимыми параметрами и клавиатурой `get_product_buy_stars()`.
*   `pre_checkout_query(pre_checkout_q: PreCheckoutQuery)`:
    *   Аргументы: `pre_checkout_q` (PreCheckoutQuery).
    *   Назначение: Обрабатывает предварительные запросы перед оплатой, подтверждает возможность оплаты.
    *   Возвращает: `None`.
    1.  Отвечает на предварительный запрос `bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)`.
*   `successful_payment(message: Message, session_with_commit: AsyncSession)`:
    *   Аргументы: `message` (Message), `session_with_commit` (AsyncSession).
    *   Назначение: Обрабатывает успешную оплату.
    *   Возвращает: `None`.
    1.  Получает данные об оплате из `message.successful_payment`.
    2.  Извлекает тип оплаты, ID пользователя и ID товара из `invoice_payload`.
    3.  Определяет валюту и цену в зависимости от типа оплаты.
    4.  Формирует словарь `payment_data` с данными об оплате.
    5.  Вызывает функцию `successful_payment_logic(...)` для дальнейшей обработки.

**Переменные:**

*   `catalog_router`: Экземпляр роутера для обработки запросов каталога.
*   `catalog_data`: Список категорий, полученный из базы данных.
*   `products_category`: Список товаров, полученных из базы данных.
*   `product`: Объект товара в цикле `for product in products_category`.
*   `product_text`: Текст описания товара.
*    `payment_type`, `product_id`, `price`: Разделенные данные из `call.data` в функции `process_about`.
*   `user_info`: Информация о пользователе, полученная из базы данных.
*   `pay_id`: ID покупки, полученный из базы данных.
*   `payment_data`: Словарь с данными об оплате.
*    `currency`: Валюта платежа (₽ или ⭐).

**Потенциальные ошибки и области для улучшения:**

1.  **Обработка ошибок:**
    *   В коде есть блок `try-except` в функции `page_catalog`, но он пустой, что не позволяет отслеживать ошибки.
    *   Необходимо добавить более детальную обработку ошибок, чтобы предотвратить сбои и сообщать пользователю об ошибках.
2.  **Валидация данных:**
    *   При получении `category_id` и `product_id` из строки не проверяется их корректность, что может привести к ошибкам при работе с базой данных.
    *   Необходимо добавить валидацию данных, чтобы убедиться, что все ID являются целыми числами, что обеспечит стабильность работы системы.
3.  **Логика обработки ошибок:**
    *   В случае, если у пользователя нет информации в базе данных `user_info` будет `None`, что может вызвать ошибку в дальнейших функциях, стоит добавить проверки, чтобы не было проблем.
4.  **Общая оптимизация:**
    *   Можно оптимизировать код, разделив некоторые функции на более мелкие и специализированные, что улучшит читаемость и поддержку кода.
    *   Использование более структурированных сообщений, таких как форматированные сообщения и шаблоны.

**Цепочка взаимосвязей:**

1.  **Пользователь Telegram** нажимает кнопку "Каталог" или "Купить".
2.  **Telegram API** отправляет `callback_query` в бота.
3.  **`catalog_router`** обрабатывает запрос, вызывает соответствующую функцию.
4.  **`CategoryDao` / `ProductDao` / `UserDAO`** взаимодействуют с базой данных через `AsyncSession`.
5.  **`catalog_kb` / `product_kb`** формируют клавиатуры для отображения пользователю.
6.  **`bot`** отправляет сообщения и инвойсы через Telegram API.
7.  **`generate_payment_link`** генерирует ссылки на оплату для Robokassa.
8.  **`successful_payment_logic`** обрабатывает успешные оплаты и обновляет данные в базе данных.
9.  **Telegram API** получает ответ от бота и отображает его пользователю.