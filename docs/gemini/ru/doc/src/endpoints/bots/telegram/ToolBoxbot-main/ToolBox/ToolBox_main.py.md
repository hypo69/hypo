# Модуль обработки логики Telegram-бота ToolBox
=================================================

Модуль содержит обработчики для различных команд и запросов, поступающих от Telegram-бота.
Он включает в себя обработку команд `/start`, `/profile`, `/stat`, обработку платных подписок,
генерацию текста и изображений, а также взаимодействие с базой данных пользователей.

## Обзор

Этот модуль является основным обработчиком логики Telegram-бота. Он обрабатывает команды,
запросы и взаимодействия пользователей, используя базу данных для хранения информации о пользователях
и их подписках. Он также интегрирован с внешними инструментами для генерации текста и изображений.

## Подробнее

Модуль предоставляет следующие возможности:

- Обработка команды `/start`: инициализация или обновление данных пользователя в базе данных.
- Обработка команды `/profile`: отображение информации о текущей подписке пользователя.
- Обработка команды `/stat`: отображение статистики по использованию бота (доступно только для администраторов).
- Обработка платных подписок: обработка успешных платежей и активация подписок для пользователей.
- Генерация текста: обработка текстовых запросов пользователей и генерация ответов с использованием внешних инструментов.
- Генерация изображений: обработка запросов на генерацию изображений с использованием внешних инструментов.
- Обработка callback-запросов: обработка нажатий на кнопки в интерфейсе бота.
- Проверка времени окончания подписки: автоматическая проверка и обновление статуса подписки пользователей.

## Классы

В данном модуле классы отсутствуют

## Функции

### `process_pre_checkout_query`

```python
def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery) -> None:
    """
    Обрабатывает предварительный запрос перед оплатой.

    Args:
        pre_checkout_query (types.PreCheckoutQuery): Объект запроса перед оплатой.

    Returns:
        None

    Как работает функция:
    1. Функция принимает объект `pre_checkout_query` типа `types.PreCheckoutQuery`, который содержит информацию о запросе перед оплатой.
    2. Вызывает метод `bot.answer_pre_checkout_query` для ответа на запрос. В качестве аргументов передаются `pre_checkout_query.id` - ID запроса, и `ok=True`, что означает подтверждение возможности проведения оплаты.

    ASCII flowchart:
    PreCheckoutQuery
    ↓
    AnswerPreCheckoutQuery (ok=True)
    """
```

### `successful_payment`

```python
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message) -> None:
    """
    Обрабатывает успешный платеж пользователя.

    Args:
        message (types.Message): Объект сообщения с информацией об успешном платеже.

    Returns:
        None

    Как работает функция:
    1. Функция принимает объект `message` типа `types.Message`, который содержит информацию об успешном платеже.
    2. Извлекает `user_id` из `message.chat.id` и преобразует его в строку.
    3. Проверяет `message.successful_payment.invoice_payload` для определения типа оплаченного тарифа.
       - Если `invoice_payload` равен `'basic_invoice_payload'`, устанавливает для пользователя тариф `basic` в `True`.
       - Если `invoice_payload` равен `'pro_invoice_payload'`, устанавливает для пользователя тарифы `pro` и `basic` в `True`.
    4. Начисляет токены пользователю:
       - Устанавливает `incoming_tokens` равным `1.7 * 10**5`.
       - Устанавливает `outgoing_tokens` равным `5 * 10**5`.
    5. Устанавливает дату окончания подписки `datetime_sub` на месяц вперед от текущей даты.
    6. Обновляет данные пользователя в базе данных с помощью `base.insert_or_update_data`.
    7. Отправляет пользователю сообщение об успешной активации подписки.
    8. Вызывает функцию `tb.restart(message)` для перезапуска обработки сообщений.

    ASCII flowchart:
    Message (successful_payment)
    ↓
    Extract User ID
    ↓
    Check Invoice Payload (basic/pro)
    ↓
    Set Tariff (basic/pro)
    ↓
    Enroll Tokens
    ↓
    Set Datetime Subscription
    ↓
    Update Database
    ↓
    Send Confirmation Message
    ↓
    Restart

    Примеры:
    Пример вызова функции при получении сообщения об успешной оплате тарифа basic:
    >>> message = create_mock_message(chat_id=123456789, invoice_payload='basic_invoice_payload')
    >>> successful_payment(message)

    Пример вызова функции при получении сообщения об успешной оплате тарифа pro:
    >>> message = create_mock_message(chat_id=987654321, invoice_payload='pro_invoice_payload')
    >>> successful_payment(message)
    """
```

### `StartProcessing`

```python
@bot.message_handler(commands=['start'])
def StartProcessing(message: types.Message) -> None:
    """
    Обрабатывает команду /start.

    Args:
        message (types.Message): Объект сообщения, содержащий команду /start.

    Returns:
        None

    Как работает функция:
    1. Извлекает `user_id` из `message.chat.id` и преобразует его в строку.
    2. Проверяет, существует ли пользователь в базе данных `db`.
       - Если пользователь не существует (`not db.get(user_id, False)`), создает новую запись пользователя с использованием шаблона `DATA_PATTERN()`.
       - Если пользователь существует, обновляет запись пользователя, сохраняя текущие значения `basic`, `pro`, `incoming_tokens`, `outgoing_tokens`, `free_requests`, `datetime_sub`, `promocode` и `ref`.
    3. Обновляет или вставляет данные пользователя в базу данных с помощью `base.insert_or_update_data`.
    4. Вызывает функцию `tb.start_request(message)` для отправки начального запроса пользователю.

    ASCII flowchart:
    Message (/start)
    ↓
    Extract User ID
    ↓
    Check if User Exists in DB
    ├──> No: Create New User Data (DATA_PATTERN)
    └──> Yes: Update User Data
    ↓
    Update/Insert Data in DB
    ↓
    Send Start Request

    Примеры:
    Пример вызова функции при получении команды /start от нового пользователя:
    >>> message = create_mock_message(chat_id=123456789, text='/start')
    >>> StartProcessing(message)

    Пример вызова функции при получении команды /start от существующего пользователя:
    >>> message = create_mock_message(chat_id=987654321, text='/start')
    >>> StartProcessing(message)
    """
```

### `personal_account`

```python
@bot.message_handler(commands=['profile'])
def personal_account(message: types.Message) -> None:
    """
    Обрабатывает команду /profile и отображает информацию о подписке пользователя.

    Args:
        message (types.Message): Объект сообщения, содержащий команду /profile.

    Returns:
        None

    Как работает функция:
    1. Извлекает `user_id` из `message.chat.id` и преобразует его в строку.
    2. Проверяет статус подписки пользователя:
       - Если у пользователя активна подписка `BASIC` и не активна подписка `PRO` (`db[user_id]['basic'] and (not db[user_id]['pro'])`), отправляет сообщение с информацией о подписке `BASIC` (безлимитные текстовые генерации, отсутствие генерации изображений).
       - Если у пользователя активны обе подписки `BASIC` и `PRO` (`db[user_id]['basic'] and db[user_id]['pro']`), отправляет сообщение с информацией о подписке `PRO` (безлимитные текстовые и графические генерации).
       - Если у пользователя нет активных подписок, отправляет сообщение с информацией об отсутствии подписки и количестве доступных бесплатных текстовых генераций.

    ASCII flowchart:
    Message (/profile)
    ↓
    Extract User ID
    ↓
    Check Subscription Status
    ├──> BASIC only: Send BASIC subscription info
    ├──> BASIC and PRO: Send PRO subscription info
    └──> No subscription: Send info about free text generations

    Примеры:
    Пример вызова функции при получении команды /profile от пользователя с подпиской BASIC:
    >>> message = create_mock_message(chat_id=123456789, text='/profile')
    >>> personal_account(message)

    Пример вызова функции при получении команды /profile от пользователя с подпиской PRO:
    >>> message = create_mock_message(chat_id=987654321, text='/profile')
    >>> personal_account(message)

    Пример вызова функции при получении команды /profile от пользователя без подписки:
    >>> message = create_mock_message(chat_id=555555555, text='/profile')
    >>> personal_account(message)
    """
```

### `show_stat`

```python
@bot.message_handler(commands=['stat'])
def show_stat(message: types.Message) -> None:
    """
    Отображает статистику использования бота (доступно только для администраторов).

    Args:
        message (types.Message): Объект сообщения, содержащий команду /stat.

    Returns:
        None

    Как работает функция:
    1. Извлекает `user_id` из `message.chat.id` и преобразует его в строку.
    2. Проверяет, является ли `user_id` администратором (входит ли в список `['2004851715', '206635551']`).
       - Если пользователь является администратором, отправляет сообщение со статистикой:
         - Общее количество пользователей: `len(db)`.
         - Количество пользователей с промокодом: `len([1 for el in db.values() if el['promocode']])`.

    ASCII flowchart:
    Message (/stat)
    ↓
    Extract User ID
    ↓
    Check if User is Admin
    └──> Yes: Send Statistics (Total Users, Users with Promocode)

    Примеры:
    Пример вызова функции при получении команды /stat от пользователя, являющегося администратором:
    >>> message = create_mock_message(chat_id=2004851715, text='/stat')
    >>> show_stat(message)

    Пример вызова функции при получении команды /stat от пользователя, не являющегося администратором:
    >>> message = create_mock_message(chat_id=123456789, text='/stat')
    >>> show_stat(message) # Ничего не произойдет, так как пользователь не администратор
    """
```

### `generate_promo_code`

```python
def generate_promo_code(length: int) -> str:
    """
    Генерирует случайный промокод заданной длины.

    Args:
        length (int): Длина промокода.

    Returns:
        str: Сгенерированный промокод.

    Как работает функция:
    1. Определяет набор символов `characters`, включающий латинские буквы в верхнем и нижнем регистре, а также цифры.
    2. Использует `random.choices` для случайного выбора символов из набора `characters` `length` раз.
    3. Объединяет выбранные символы в строку с помощью `''.join()`.
    4. Возвращает сгенерированный промокод.

    ASCII flowchart:
    Length
    ↓
    Define Characters Set
    ↓
    Randomly Choose Characters (length times)
    ↓
    Join Characters into String
    ↓
    Return Promo Code

    Примеры:
    Пример вызова функции для генерации промокода длиной 10 символов:
    >>> promo_code = generate_promo_code(10)
    >>> print(promo_code) # Например: "aB9cD3eF1g"
    """
```

### `CallsProcessing`

```python
@bot.callback_query_handler(func=lambda call: True)
def CallsProcessing(call: types.CallbackQuery) -> None:
    """
    Обрабатывает callback-запросы от нажатий на кнопки в Telegram-боте.

    Args:
        call (types.CallbackQuery): Объект callback-запроса.

    Returns:
        None

    Как работает функция:
    1. Извлекает `user_id` из `call.message.chat.id` и преобразует его в строку.
    2. Определяет список `text_buttons` с идентификаторами кнопок текстовых задач.
    3. Проверяет, существует ли пользователь в базе данных `db`. Если нет, создает новую запись пользователя с использованием `DATA_PATTERN`.
    4. Обрабатывает callback-запросы в зависимости от значения `call.data`:
       - Если `call.data` содержится в `tb.data`, вызывает соответствующие методы из `ToolBox` для обработки основных задач (текст, изображения, тарифы, бесплатный режим).
       - Если `call.data` соответствует выбору размера изображения (`"576x1024"`, `"1024x1024"`, `"1024x576"`), сохраняет размер изображения в базе данных и вызывает `tb.ImageArea`.
       - Если `call.data` соответствует запросу на upscale или регенерацию изображения (`"upscale"`, `"regenerate"`), выполняет соответствующие действия с использованием потоков.
       - Если `call.data` соответствует выбору тарифа (`"basic"`, `"pro"`, `"promo"`, `"ref"`), обрабатывает выбор тарифа, активацию промокода или отображение реферального кода.
       - Если `call.data` соответствует одной из кнопок текстовых задач (`text_buttons`), вызывает `tb.SomeTexts` или `tb.OneTextArea` в зависимости от типа задачи.
       - Если `call.data` соответствует кнопке выхода (`"exit"`, `"text_exit"`, `"tariff_exit"`), выполняет соответствующие действия для выхода из текущего режима.
       - Если `call.data` соответствует кнопке выбора одной текстовой области (`f"one_{ind}" for ind in range(N)`), вызывает `tb.OneTextArea` для выбора текстовой области.
       - Если `call.data` соответствует кнопке выбора нескольких текстовых областей (`f"some_{ind}" for ind in range(N)`), вызывает `tb.SomeTextsArea` для выбора нескольких текстовых областей.
    5. Обновляет данные пользователя в базе данных с помощью `base.insert_or_update_data`.

    ASCII flowchart (упрощенный):
    CallbackQuery
    ↓
    Extract User ID
    ↓
    Check if User Exists
    ↓
    Handle Callback Data
    ├──> Main Tasks (text, images, tariff, free)
    ├──> Image Size Selection
    ├──> Upscale/Regenerate Image
    ├──> Tariff Selection/Promo Code/Referral Code
    ├──> Text Tasks
    ├──> Exit
    └──> Text Area Selection (One/Some)
    ↓
    Update User Data in DB

    Примеры:
    Пример вызова функции при нажатии на кнопку "text":
    >>> call = create_mock_callback_query(chat_id=123456789, data='text')
    >>> CallsProcessing(call)

    Пример вызова функции при нажатии на кнопку "basic":
    >>> call = create_mock_callback_query(chat_id=987654321, data='basic')
    >>> CallsProcessing(call)

    Пример вызова функции при нажатии на кнопку "exit":
    >>> call = create_mock_callback_query(chat_id=555555555, data='exit')
    >>> CallsProcessing(call)
    """
```

### `TokensCancelletionPattern`

```python
def TokensCancelletionPattern(user_id: str, func: callable, message: types.Message, i: Optional[int] = None) -> None:
    """
    Управляет списанием токенов или бесплатных запросов пользователя при выполнении задачи.

    Args:
        user_id (str): ID пользователя.
        func (callable): Функция для выполнения задачи (например, `tb.TextCommands`, `tb.FreeCommand`).
        message (types.Message): Объект сообщения пользователя.
        i (Optional[int], optional): Индекс задачи (если применимо). По умолчанию `None`.

    Returns:
        None

    Как работает функция:
    1. Получает информацию о токенах и бесплатных запросах пользователя из базы данных `db`.
    2. Проверяет, достаточно ли у пользователя токенов (`in_tokens > 0 and out_tokens > 0`) или бесплатных запросов (`free_requests > 0`).
    3. Если токенов или запросов достаточно:
       - Вызывает функцию `func` для выполнения задачи.
       - Если `i` не указан, вызывает `func` с аргументами `message` и `db[user_id]['sessions_messages']` и получает `incoming_tokens`, `outgoing_tokens` и обновленный список `sessions_messages`.
       - Если `i` указан, вызывает `func` с аргументами `message` и `i` (или с дополнительным аргументом `{"incoming_tokens": in_tokens, "outgoing_tokens": out_tokens, "free_requests": free_requests}` для `tb.TextCommands`) и получает `incoming_tokens`, `outgoing_tokens` и `cnt`.
       - Списывает токены или бесплатные запросы в зависимости от доступности.
    4. Если бесплатных запросов нет (`db[user_id]['free_requests'] == 0`), вызывает `tb.FreeTariffEnd(message)` для уведомления пользователя об окончании бесплатных запросов.
    5. Если токенов нет, вызывает `tb.TarrifEnd(message)` для уведомления пользователя об окончании тарифа и устанавливает `incoming_tokens` и `outgoing_tokens` в 0 (если они были положительными).
    6. Перезапускает обработку сообщений с помощью `tb.restart(message)`.

    ASCII flowchart:
    User ID, Function, Message, Index (optional)
    ↓
    Get User Tokens and Free Requests
    ↓
    Check if Tokens/Requests are Sufficient
    ├──> Yes:
    │   │
    │   Call Function
    │   │
    │   Deduct Tokens/Requests
    │
    ├──> No Free Requests:
    │   │
    │   Notify Free Tariff End
    │
    └──> No Tokens:
        │
        Notify Tariff End
        │
        Reset Tokens
        │
        Restart

    Примеры:
    Пример вызова функции для обработки текстовой команды:
    >>> TokensCancelletionPattern(user_id='123456789', func=tb.TextCommands, message=message, i=0)

    Пример вызова функции для обработки бесплатной команды:
    >>> TokensCancelletionPattern(user_id='987654321', func=tb.FreeCommand, message=message)
    """
```

### `TasksProcessing`

```python
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def TasksProcessing(message: types.Message) -> None:
    """
    Обрабатывает входящие текстовые сообщения и фотографии от пользователя.

    Args:
        message (types.Message): Объект входящего сообщения.

    Returns:
        None

    Как работает функция:
    1. Извлекает `user_id` из `message.chat.id`.
    2. Проверяет, запрошена ли генерация изображения (`db[user_id]['images'] != ""`).
       - Если да и `db[user_id]['images']` содержит только размер изображения, то извлекает размер, текст запроса и генерирует seed для изображения.
         Сохраняет параметры генерации изображения в `db[user_id]['images']`.
    3. Проверяет, находится ли пользователь в "свободном режиме" (`db[user_id]['free']`).
       - Если да и текст сообщения - "В меню", то завершает сессию, очищает историю и возвращает пользователя в главное меню.
    4. Если пользователь в "свободном режиме", то обрабатывает текст или фотографию:
       - Если получена фотография, кодирует её в base64 и добавляет в историю сессии.
       - Вызывает `TokensCancelletionPattern` для обработки запроса в "свободном режиме".
    5. Если пользователь не в "свободном режиме", то обрабатывает сообщение как текстовый запрос:
       - Перебирает все активные текстовые задачи (`db[user_id]['text'][i]`).
       - Вызывает `TokensCancelletionPattern` для каждой активной задачи.
       - Сбрасывает флаг задачи (`db[user_id]['text'][i] = 0`).
    6. Обновляет данные пользователя в базе данных.

    ASCII flowchart:
    Message (text/photo)
    │
    ├──> Image Generation Requested?
    │   │
    │   Yes: Extract size, prompt, generate seed, save params
    │
    ├──> Free Mode Active?
    │   │
    │   Yes: "В меню"? -> End session, clear history, return to main menu
    │   │
    │   Yes: Photo? -> Encode to base64, add to history
    │   │
    │   Yes: Call TokensCancelletionPattern for FreeCommand
    │
    └──> Text Processing:
        │
        Iterate over active text tasks
        │
        Call TokensCancelletionPattern for each task
        │
        Reset task flag
    ↓
    Update user data in DB

    Примеры:
    Обработка текстового запроса в обычном режиме:
    >>> message = create_mock_message(chat_id=123, text="Some text")
    >>> db["123"] = {"text": [1, 0, 0, 0, 0, 0, 0, 0], "some": False, 'images': ""}
    >>> TasksProcessing(message)

    Обработка фото в свободном режиме:
    >>> message = create_mock_message(chat_id=456, content_type='photo', caption="Photo caption")
    >>> TasksProcessing(message)
    """
```

### `end_check_tariff_time`

```python
async def end_check_tariff_time() -> None:
    """
    Проверяет время окончания действия тарифа у пользователей и обновляет их статус.

    Returns:
        None

    Как работает функция:
    1. Запускает бесконечный цикл.
    2. Для каждого пользователя в базе данных (`db.items()`):
       - Вычисляет разницу между временем окончания подписки (`data['datetime_sub']`) и текущим временем.
       - Если время окончания подписки уже прошло и у пользователя есть активные подписки (`basic`, `pro`) или осталось менее 10 бесплатных запросов, то:
         - Обнуляет параметры тарифа пользователя, сохраняя только `text`, `images`, `free`, `promocode` и `ref`.
         - Обновляет данные пользователя в базе данных.
    3. Приостанавливает выполнение на 10 секунд.

    ASCII flowchart:
    Loop
    │
    ├──> For each user in DB:
    │   │
    │   Calculate time difference
    │   │
    │   Check if tariff expired and user has active subscription or few free requests
    │   │
    │   Yes: Reset tariff parameters, save data to DB
    │
    └──> Sleep 10 seconds

    Примеры:
    (async function, примеры вызова не требуются)
    """
```

## Запуск бота

```python
if __name__ == "__main__":
    Thread(target=bot.infinity_polling).start()
    asyncio.run(end_check_tariff_time())
```

**Описание**:
- Запускает бота в режиме непрерывного опроса (`bot.infinity_polling`) в отдельном потоке.
- Запускает асинхронную задачу `end_check_tariff_time` для проверки времени окончания действия тарифа.