# Модуль ToolBox_main

## Обзор

Модуль `ToolBox_main.py` является основным модулем для управления Telegram-ботом `ToolBox`. Он содержит функции для обработки команд пользователя, управления тарифами, генерации текста и изображений, а также взаимодействия с базой данных пользователей.

## Подробней

Этот модуль обеспечивает функциональность Telegram-бота, включая обработку команд `/start`, `/profile`, `/stat`, обработку платных подписок, генерацию контента на основе запросов пользователей и управление реферальной системой. Он интегрируется с классами `ToolBox` и `DataBase` для выполнения запросов к API и управления данными пользователей, соответственно.

## Классы

В данном модуле классы не определены.

## Функции

### `process_pre_checkout_query`

```python
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery) -> None:
    """Обрабатывает предварительный запрос перед совершением оплаты.

    Args:
        pre_checkout_query (types.PreCheckoutQuery): Объект запроса.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает предварительные запросы перед оплатой, отправляя подтверждение боту.
    2. Использует метод `bot.answer_pre_checkout_query` для ответа на запрос с положительным результатом (ok=True).

    """
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
```

### `successful_payment`

```python
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message) -> None:
    """Обрабатывает успешное завершение оплаты пользователем.

    Args:
        message (types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает информацию об успешной оплате от пользователя.
    2. Обновляет данные пользователя в базе данных в зависимости от приобретенного тарифного плана ("basic" или "pro").
    3. Начисляет токены пользователю в соответствии с тарифным планом.
    4. Устанавливает дату окончания подписки пользователя.
    5. Отправляет пользователю подтверждение об активации подписки.
    6. Перезапускает взаимодействие с пользователем через функцию `tb.restart`.

    """
    global db
    user_id = str(message.chat.id)
    # tariffs pay separation
    if message.successful_payment.invoice_payload == 'basic_invoice_payload':
        db[user_id]['basic'] = True
    elif message.successful_payment.invoice_payload == 'pro_invoice_payload':
        db[user_id]['pro'] = True
        db[user_id]['basic'] = True

    # Tokens enrollment
    db[user_id]['incoming_tokens'] = 1.7*10**5
    db[user_id]['outgoing_tokens'] = 5*10**5

    # Datetime tariff subscribe
    db[user_id]['datetime_sub'] = datetime.now().replace(microsecond=0)+relativedelta(months=1)
    base.insert_or_update_data(user_id, db[user_id])
    bot.send_message(user_id, "Спасибо за оплату! Ваша подписка активирована.")
    tb.restart(message)
```

### `StartProcessing`

```python
@bot.message_handler(commands=['start'])
def StartProcessing(message: types.Message) -> None:
    """Обрабатывает команду `/start`, инициализирует или обновляет данные пользователя.

    Args:
        message (types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает команду `/start`, которую отправляет пользователь.
    2. Инициализирует данные пользователя, используя `DATA_PATTERN`, если пользователь новый или обновляет существующие данные.
    3. Сохраняет или обновляет данные пользователя в базе данных.
    4. Вызывает функцию `tb.start_request` для начала взаимодействия с пользователем.

    """
    global db
    user_id = str(message.chat.id)
    db[user_id] = DATA_PATTERN() if not db.get(user_id, False) else DATA_PATTERN(basic=db[user_id]['basic'], pro=db[user_id]['pro'], incoming_tokens=db[user_id]['incoming_tokens'],
                                                                                outgoing_tokens=db[user_id]['outgoing_tokens'], free_requests=db[user_id]['free_requests'], datetime_sub=db[user_id]['datetime_sub'],
                                                                                promocode=db[user_id]['promocode'], ref=db[user_id]['ref']
                                                                                )
    base.insert_or_update_data(user_id, db[user_id])
    tb.start_request(message)
```

### `personal_account`

```python
@bot.message_handler(commands=['profile'])
def personal_account(message: types.Message) -> None:
    """Отображает информацию о тарифном плане пользователя.

    Args:
        message (types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает команду `/profile`, отправленную пользователем.
    2. Извлекает информацию о тарифном плане пользователя из базы данных.
    3. Отправляет пользователю сообщение с информацией о его тарифном плане ("BASIC", "PRO" или отсутствии подписки).
    """
    global db
    user_id = str(message.chat.id)
    if db[user_id]['basic'] and (not db[user_id]['pro']):
        bot.send_message(chat_id=user_id, text="Подписка: BASIC\nТекстовые генерации: безлимит\nГенерация изображений: нет", parse_mode='html')
    elif db[user_id]['basic'] and db[user_id]['pro']:
        bot.send_message(chat_id=user_id, text="Подписка: PRO\nТекстовые генерации: безлимит\nГенерация изображений: безлимит", parse_mode='html')
    else:
        bot.send_message(chat_id=user_id, text=f"У вас нет подписки\nТекстовые генерации: 10 в день, осталось:{db[user_id]['free_requests']}\nГенерация изображений: нет", parse_mode='html')
```

### `show_stat`

```python
@bot.message_handler(commands=['stat'])
def show_stat(message: types.Message) -> None:
    """Отображает статистику бота для администраторов.

    Args:
        message (types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает команду `/stat`, отправленную пользователем.
    2. Проверяет, является ли пользователь администратором (user_id in ['2004851715', '206635551']).
    3. Отправляет администратору сообщение со статистикой бота: общее количество пользователей и количество пользователей с промокодом.

    """
    global db
    user_id = str(message.chat.id)
    if user_id in ['2004851715', '206635551']:
        bot.send_message(chat_id=user_id, text=f"Всего пользователей: {len(db)}\nС промокодом: {len([1 for el in db.values() if el['promocode']])}")
```

### `generate_promo_code`

```python
def generate_promo_code(length: int) -> str:
    """Генерирует случайный промокод заданной длины.

    Args:
        length (int): Длина промокода.

    Returns:
        str: Сгенерированный промокод.

    Как работает функция:
    1. Функция генерирует промокод заданной длины.
    2. Использует символы из `string.ascii_letters` (буквы) и `string.digits` (цифры) для генерации.
    3. Возвращает сгенерированный промокод в виде строки.

    """
    characters = string.ascii_letters + string.digits
    promo_code = ''.join(random.choices(characters, k=length))
    return promo_code
```

### `CallsProcessing`

```python
@bot.callback_query_handler(func=lambda call: True)
def CallsProcessing(call: types.CallbackQuery) -> None:
    """Обрабатывает callback-запросы от нажатия кнопок в боте.

    Args:
        call (types.CallbackQuery): Объект callback-запроса.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает callback-запросы от нажатия кнопок в боте.
    2. Определяет действие, которое необходимо выполнить, в зависимости от данных, переданных в callback-запросе (`call.data`).
    3. Выполняет соответствующие действия, такие как обработка выбора типа текста, размера изображения, тарифного плана или промокода.
    4. Обновляет данные пользователя в базе данных.
    5. Вызывает другие функции для выполнения конкретных задач, таких как `tb.Text_types`, `tb.ImageSize`, `tb.TariffArea` и другие.
    """
    global db
    user_id = str(call.message.chat.id)

    text_buttons = [
        "comm-text", "smm-text", "brainst-text",
        "advertising-text", "headlines-text", 
        "seo-text", "news", "editing"
    ]
    # User data create
    if not db.get(user_id):
        db[user_id] = DATA_PATTERN()
        base.insert_or_update_data(user_id, db[user_id])

    # Main tasks buttons
    if call.data in tb.data:
        match call.data:
            # Text button
            case "text":
                tb.Text_types(call.message)
            # Image button
            case "images":
                if db[user_id]["pro"]:
                    tb.ImageSize(call.message)
                else:
                    bot.send_message(chat_id=user_id, text="Обновите ваш тариф до PRO")
                    tb.restart(call.message)
            # Free mode button
            case "free":
                db[user_id]['free'] = True
                base.insert_or_update_data(user_id, db[user_id])
                bot.delete_message(user_id, message_id=call.message.message_id)
                tb.FreeArea(call.message)
            # Tariff button
            case "tariff":
                tb.TariffArea(call.message)
    
    # Image size buttons
    elif call.data in ["576x1024", "1024x1024", "1024x576"]:
        db[user_id]['images'] = call.data
        base.insert_or_update_data(user_id, db[user_id])
        tb.ImageArea(call.message)

    elif call.data in ["upscale", "regenerate"]:
        size, prompt, seed = db[user_id]["images"].split('|')
        size = [int(el) for el in size.split('x')]
        match call.data:
            case "upscale":
                bot.delete_message(user_id, call.message.message_id)
                thr=Thread(target=tb.Image_Regen_And_Upscale, args=(call.message, prompt, size, int(seed), 30))
                thr.start(); thr.join()
                tb.BeforeUpscale(call.message)
            case "regenerate":
                bot.delete_message(user_id, call.message.message_id)
                seed = randint(1, 1000000)
                thr=Thread(target=tb.Image_Regen_And_Upscale, args=(call.message, prompt, size, seed))
                thr.start()
                db[user_id]["images"] = '|'.join(db[user_id]["images"].rsplit('|')[:2])+'|'+str(seed)
                base.insert_or_update_data(user_id, db[user_id])
                thr.join()
                tb.ImageChange(call.message)

    # Tariffs buttons
    elif call.data in ["basic", "pro", "promo", "ref"]:
        match call.data:
            # basic
            case "basic":
                if not db[user_id]['basic']:
                    tb.Basic_tariff(call.message)
                else:
                    bot.send_message(chat_id=user_id, text="Вы уже подключили тариф BASIC.")
                    tb.restart(call.message)
            # pro
            case "pro":
                if not db[user_id]['pro']:
                    tb.Pro_tariff(call.message)
                else:
                    bot.send_message(chat_id=user_id, text="Вы уже подключили тариф PRO.")
                    tb.restart(call.message)
            # promo
            case "promo":
                if (not db[user_id]['pro']) and (not db[user_id]['promocode']):
                    msg = bot.send_message(chat_id=user_id, text="Введите ваш промокод")
                    def get_promo_code(message: types.Message) -> None:
                        """Обрабатывает введенный пользователем промокод.

                        Args:
                            message (types.Message): Объект сообщения от Telegram.

                        Returns:
                            None
                        
                        Как работает внутренняя функция:
                            1. Проверяет введенный пользователем промокод.
                            2. Если промокод верен ("free24" или реферальный код), активирует PRO-подписку для пользователя.
                            3. Начисляет токены пользователю.
                            4. Устанавливает дату окончания подписки.
                            5. Обновляет данные пользователя в базе данных.
                            6. Отправляет пользователю подтверждение об активации подписки.
                            7. Перезапускает взаимодействие с пользователем через функцию `tb.restart`.
                            8. Если промокод не верен, отправляет пользователю сообщение об ошибке.

                        """
                        if message.text.lower() == "free24" or message.text == [us['ref'] for us in db.values()] and db[user_id]['ref']!=message.text:
                            db[user_id]['pro'] = True
                            db[user_id]['basic'] = True
                            db[user_id]['incoming_tokens'] = 1.7*10**5
                            db[user_id]['outgoing_tokens'] = 5*10**5
                            db[user_id]['datetime_sub'] = datetime.now().replace(microsecond=0)+relativedelta(months=1)
                            db[user_id]['promocode'] = True
                            base.insert_or_update_data(user_id, db[user_id])
                            bot.send_message(chat_id=user_id, text="Ваша подписка активирвана. Приятного использования ☺️", parse_mode='html')
                        else:
                            bot.send_message(chat_id=user_id, text="Неверный промокод.")
                        tb.restart(message)
                    bot.register_next_step_handler(msg, get_promo_code)
                else:
                    bot.send_message(chat_id=user_id, text="Вы уже подключили тариф PRO или уже активировали промокод")
                    tb.restart(call.message)
            
            case "ref":
                if db[user_id]['ref'] == '':
                    referal = generate_promo_code(10)
                    db[user_id]['ref'] = referal
                else:
                    referal = db[user_id]['ref']
                bot.send_message(chat_id=user_id, text=f"Ваш реферальный код: {referal}", parse_mode='html')
                tb.restart(call.message)
                base.insert_or_update_data(user_id, db[user_id])
    # Texts buttons
    elif call.data in text_buttons:
        avalib = [0, 1, 3, 5, 6]
        index = text_buttons.index(call.data)
        if index in avalib:
            tb.SomeTexts(call.message, avalib.index(index))
        else:
            db[user_id]['text'][index] = 1
            base.insert_or_update_data(user_id, db[user_id])
            tb.OneTextArea(call.message, index)

    # All exit buttons
    elif call.data in ["exit", "text_exit", "tariff_exit"]:
        match call.data:
            # Cancel to main menu button
            case "exit":
                db[user_id] = DATA_PATTERN(basic=db[user_id]['basic'], pro=db[user_id]['pro'], incoming_tokens=db[user_id]['incoming_tokens'],
                                        outgoing_tokens=db[user_id]['outgoing_tokens'], free_requests=db[user_id]['free_requests'],
                                        datetime_sub=db[user_id]['datetime_sub'], promocode=db[user_id]['promocode'], ref=db[user_id]['ref'])
                base.insert_or_update_data(user_id, db[user_id])
                tb.restart_markup(call.message)
            # Cancel from text field input
            case "text_exit":
                db[user_id]['text'] = [0]*N
                db[user_id]['some'] = False
                base.insert_or_update_data(user_id, db[user_id])
                tb.Text_types(call.message)
            # Cancel from tariff area selection
            case "tariff_exit":
                bot.delete_message(user_id, call.message.message_id)
                tb.TariffExit(call.message)

    # One text area buttons
    elif call.data in [f"one_{ind}" for ind in range(N)]:
        index = [0, 1, 3, 5, 6][int(call.data[-1])]
        db[user_id]['text'][index] = 1
        base.insert_or_update_data(user_id, db[user_id])
        tb.OneTextArea(call.message, index)

    # Some texts area buttons
    elif call.data in [f"some_{ind}" for ind in range(N)]:
        index = [0, 1, 3, 5, 6][int(call.data[-1])]
        db[user_id]['text'][index] = 1
        db[user_id]['some'] = True
        base.insert_or_update_data(user_id, db[user_id])
        tb.SomeTextsArea(call.message, int(call.data[-1]))
```

### `TokensCancelletionPattern`

```python
def TokensCancelletionPattern(user_id: str, func: callable, message: types.Message, i: Optional[int] = None) -> None:
    """Определяет шаблон списания токенов или запросов для пользователя.

    Args:
        user_id (str): ID пользователя.
        func (callable): Функция для выполнения (например, `tb.TextCommands` или `tb.SomeTextsCommand`).
        message (types.Message): Объект сообщения от Telegram.
        i (Optional[int], optional): Индекс для некоторых функций. Defaults to None.

    Returns:
        None

    Как работает функция:
    1. Функция определяет, как списывать токены или бесплатные запросы у пользователя в зависимости от его тарифного плана и доступных ресурсов.
    2. Проверяет, есть ли у пользователя доступные входящие и исходящие токены или бесплатные запросы.
    3. Вызывает переданную функцию (`func`) для обработки сообщения пользователя и получения информации о количестве использованных токенов.
    4. Обновляет количество токенов или бесплатных запросов в базе данных.
    5. Если у пользователя закончились токены или бесплатные запросы, отправляет ему сообщение о необходимости продления тарифного плана.

    """
    global db
    in_tokens = db[user_id]['incoming_tokens']
    out_tokens = db[user_id]['outgoing_tokens']
    free_requests = db[user_id]['free_requests']

    if in_tokens > 0 and out_tokens > 0 or free_requests > 0:
        if i is None:
            incoming_tokens, outgoing_tokens, db[user_id]['sessions_messages'] = func(message, db[user_id]['sessions_messages']); cnt = 1
        else:
            incoming_tokens, outgoing_tokens, cnt = func(message, i) if func == tb.TextCommands else func(message, i, {"incoming_tokens": in_tokens,
                                                                                                                        "outgoing_tokens": out_tokens,
                                                                                                                        "free_requests": free_requests})
        if in_tokens > 0 and out_tokens > 0:
            db[user_id]['incoming_tokens'] -= incoming_tokens
            db[user_id]['outgoing_tokens'] -= outgoing_tokens

        elif free_requests > 0:
            db[user_id]['free_requests'] -= cnt

    elif db[user_id]['free_requests'] == 0:
        tb.FreeTariffEnd(message)

    else:
        tb.TarrifEnd(message)
        db[user_id]['incoming_tokens'] = 0 if in_tokens <= 0 else in_tokens
        db[user_id]['outgoing_tokens'] = 0 if out_tokens <= 0 else out_tokens
        tb.restart(message)
```

### `TasksProcessing`

```python
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def TasksProcessing(message: types.Message) -> None:
    """Обрабатывает входящие текстовые сообщения и фотографии от пользователей.

    Args:
        message (types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Как работает функция:
    1. Функция обрабатывает входящие сообщения от пользователей, определяет их тип (текст или фотография) и выполняет соответствующие действия.
    2. Если пользователь отправил изображение и у него активен режим генерации изображений, функция обрабатывает запрос на генерацию изображения.
    3. Если пользователь находится в бесплатном режиме (`db[user_id]['free']`), функция обрабатывает сообщение как запрос в бесплатном режиме.
    4. Если пользователь отправил текстовое сообщение и выбрал один из типов текста для генерации, функция обрабатывает запрос на генерацию текста.
    5. Использует `TokensCancelletionPattern` для списания токенов или бесплатных запросов.
    """
    global db
    user_id = str(message.chat.id)

    # Images processing
    if db[user_id]['images'] != "" and len(db[user_id]['images'].split('|')) == 1:
        size = [int(el) for el in db[user_id]['images'].split('x')]
        prompt = message.text
        seed = tb.ImageCommand(message, prompt, size)
        db[user_id]['images']+="|"+prompt+"|"+str(int(seed))
    
    # Main menu exit button
    elif db[user_id]['free'] and message.text == 'В меню':
        db[user_id]['sessions_messages'] = []
        db[user_id]['free'] = False
        bot.send_message(chat_id=user_id, text='Сессия завершена', reply_markup=types.ReplyKeyboardRemove(), parse_mode='html')
        tb.restart(message)

    # Free mode processing
    elif db[user_id]['free']:
        if message.content_type == 'photo':
            photo = base64.b64encode(bot.download_file(bot.get_file(message.photo[-1].file_id).file_path)).decode()
            if message.caption is not None:
                db[user_id]['sessions_messages'].append({"content": [{"type": "text", "text": message.caption}, {"type": "image_url", "image_url": f"data:image/jpeg;base64,{photo}"}], "role": "user"})
            else:
                db[user_id]['sessions_messages'].append({"content": [{"type": "image_url", "image_url": f"data:image/jpeg;base64,{photo}"}], "role": "user"})
            thr = Thread(target=TokensCancelletionPattern, args=(user_id, tb.FreeCommand, message))
            thr.start(); thr.join()
        else:
            thr = Thread(target=TokensCancelletionPattern, args=(user_id, tb.FreeCommand, message))
            thr.start(); thr.join()
    # Text processing
    else:
        for i in range(len(db[user_id]['text'])):
            if db[user_id]['text'][i] and not db[user_id]['some']:
                thr=Thread(target=TokensCancelletionPattern, args=(user_id, tb.TextCommands, message, i))
                thr.start()
                db[user_id]['text'][i] = 0
                thr.join()
            elif db[user_id]['text'][i] and db[user_id]['some']:
                thr=Thread(target=TokensCancelletionPattern, args=(user_id, tb.SomeTextsCommand, message, i))
                thr.start()
                db[user_id]['text'][i] = 0
                db[user_id]['some'] = False
                thr.join()
    base.insert_or_update_data(user_id, db[user_id])
```

### `end_check_tariff_time`

```python
async def end_check_tariff_time() -> None:
    """Проверяет время окончания действия тарифа у пользователей и обновляет их статус.

    Returns:
        None

    Как работает функция:
    1. Функция является асинхронной и выполняется в бесконечном цикле.
    2. Проверяет время окончания действия тарифа у каждого пользователя в базе данных.
    3. Если время окончания тарифа истекло, сбрасывает тариф пользователя и обновляет его данные в базе данных.
    4. Засыпает на 10 секунд перед следующей проверкой.
    """
    while True:
        global db
        for user_id, data in db.items():
            deltaf = data['datetime_sub'] - datetime.now().replace(microsecond=0)
            if int(deltaf.total_seconds()) <= 0 and (data['basic'] or data['pro'] or data['free_requests']<10):
                db[user_id] = DATA_PATTERN(text=data['text'], images=data['images'],
                                        free=data['free'], promocode=data['promocode'], ref=data['ref'])
                base.insert_or_update_data(user_id, db[user_id])
        await asyncio.sleep(10)
```

## Запуск бота

```python
if __name__ == "__main__":
    Thread(target=bot.infinity_polling).start()
    asyncio.run(end_check_tariff_time())
```

**Как работает**:

1.  Запускает бота в режиме непрерывного опроса (`bot.infinity_polling`) в отдельном потоке.
2.  Запускает асинхронную функцию `end_check_tariff_time` для проверки и обновления статуса тарифов пользователей.