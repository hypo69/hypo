# hypotez/src/endpoints/bots/telegram/ToolBoxbot-main/ToolBox/ToolBox_main.py

## Обзор

Этот файл содержит основной код для Telegram-бота ToolBox. Он включает в себя обработку команд, колбэков, текстовых сообщений и изображений, а также логику для управления тарифами, промокодами и реферальными ссылками. Бот использует базу данных для хранения информации о пользователях и их подписках.

## Подробнее

Файл содержит инициализацию бота, подключение к базе данных, обработку различных типов сообщений и запросов от пользователей, а также асинхронную задачу для проверки времени окончания действия тарифов.

## Содержание

- [DATA_PATTERN](#data_pattern)
- [process_pre_checkout_query](#process_pre_checkout_query)
- [successful_payment](#successful_payment)
- [StartProcessing](#startprocessing)
- [personal_account](#personal_account)
- [show_stat](#show_stat)
- [generate_promo_code](#generate_promo_code)
- [CallsProcessing](#callsprocessing)
- [TokensCancelletionPattern](#tokenscancelletionpattern)
- [TasksProcessing](#tasksprocessing)
- [end_check_tariff_time](#end_check_tariff_time)

## DATA_PATTERN

```python
DATA_PATTERN = lambda text=[0]*N, sessions_messages=[], some=False, images="", free=False, basic=False, pro=False, incoming_tokens=0, outgoing_tokens=0, free_requests=10, datetime_sub=datetime.now().replace(microsecond=0)+relativedelta(days=1), promocode=False, ref='': {'text':text, "sessions_messages": sessions_messages, "some":some, 'images':images, 'free': free, 'basic': basic, 'pro': pro, 
                                                                                                                                                                                    'incoming_tokens': incoming_tokens, 'outgoing_tokens': outgoing_tokens,
                                                                                                                                                                                    'free_requests': free_requests, 'datetime_sub': datetime_sub, 'promocode': promocode, 'ref': ref}
```

**Назначение**: Функция `DATA_PATTERN` - это lambda-функция, которая создает словарь с данными пользователя по умолчанию.

**Как работает функция**:

Функция создает словарь, содержащий информацию о пользователе, такую как его текстовые данные, сообщения сессий, изображения, статус подписки (free, basic, pro), количество входящих и исходящих токенов, количество бесплатных запросов, дату окончания подписки, наличие промокода и реферальную ссылку.

**Параметры**:

- `text` (list, optional): Список, представляющий различные типы текста. По умолчанию `[0]*N`.
- `sessions_messages` (list, optional): Список сообщений сессии. По умолчанию `[]`.
- `some` (bool, optional): Булево значение. По умолчанию `False`.
- `images` (str, optional): Строка, представляющая изображения. По умолчанию `""`.
- `free` (bool, optional): Статус бесплатной подписки. По умолчанию `False`.
- `basic` (bool, optional): Статус базовой подписки. По умолчанию `False`.
- `pro` (bool, optional): Статус профессиональной подписки. По умолчанию `False`.
- `incoming_tokens` (int, optional): Количество входящих токенов. По умолчанию `0`.
- `outgoing_tokens` (int, optional): Количество исходящих токенов. По умолчанию `0`.
- `free_requests` (int, optional): Количество бесплатных запросов. По умолчанию `10`.
- `datetime_sub` (datetime, optional): Дата окончания подписки. По умолчанию `datetime.now().replace(microsecond=0)+relativedelta(days=1)`.
- `promocode` (bool, optional): Наличие промокода. По умолчанию `False`.
- `ref` (str, optional): Реферальная ссылка. По умолчанию `""`.

**Возвращает**:

- `dict`: Словарь с данными пользователя.

**Примеры**:

```python
>>> data = DATA_PATTERN()
>>> print(data)
{'text': [0, 0, 0, 0, 0, 0, 0, 0], 'sessions_messages': [], 'some': False, 'images': '', 'free': False, 'basic': False, 'pro': False, 'incoming_tokens': 0, 'outgoing_tokens': 0, 'free_requests': 10, 'datetime_sub': datetime.datetime(...), 'promocode': False, 'ref': ''}
```

## Функции

### `process_pre_checkout_query`

```python
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query):
    """
    Args:
        pre_checkout_query:

    Returns:

    """
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
```

**Назначение**: Обрабатывает предварительные запросы перед оплатой.

**Как работает функция**:
Функция `process_pre_checkout_query` обрабатывает предварительные запросы перед совершением платежа. Она отвечает на запрос `pre_checkout_query` утвердительно, подтверждая готовность к проведению платежа.

**Параметры**:

- `pre_checkout_query`: Объект запроса от Telegram API, содержащий информацию о предварительном запросе перед оплатой.

**Возвращает**:

- `None`: Функция ничего не возвращает, она отправляет ответ на запрос через `bot.answer_pre_checkout_query`.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# process_pre_checkout_query(pre_checkout_query)
```

### `successful_payment`

```python
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    """
    Args:
        message:

    Returns:

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

**Назначение**: Обрабатывает успешные платежи.

**Как работает функция**:
Функция `successful_payment` обрабатывает уведомления об успешной оплате от пользователя. Она определяет, какой тариф был оплачен (basic или pro), и соответственно обновляет данные пользователя в базе данных, включая установку флагов `basic` и `pro`, начисление токенов и установку даты окончания подписки. После этого пользователю отправляется сообщение с благодарностью и подтверждением активации подписки.

**Параметры**:

- `message`: Объект сообщения от Telegram API, содержащий информацию об успешном платеже.

**Возвращает**:

- `None`: Функция ничего не возвращает, она обновляет данные в базе данных и отправляет сообщение пользователю.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# successful_payment(message)
```

### `StartProcessing`

```python
@bot.message_handler(commands=['start'])
def StartProcessing(message):
    """
    Args:
        message:

    Returns:

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

**Назначение**: Обрабатывает команду `/start`.

**Как работает функция**:
Функция `StartProcessing` обрабатывает команду `/start`, которую отправляет пользователь. Она проверяет, есть ли данные о пользователе в базе данных. Если данных нет, создается новый профиль пользователя с данными по умолчанию, используя `DATA_PATTERN`. Если данные есть, они обновляются с сохранением информации о подписке, токенах, бесплатных запросах, дате окончания подписки, промокоде и реферальной ссылке. После этого вызывается метод `start_request` объекта `tb` для отправки начального запроса пользователю.

**Параметры**:

- `message`: Объект сообщения от Telegram API, содержащий информацию о команде `/start`.

**Возвращает**:

- `None`: Функция ничего не возвращает, она обновляет данные в базе данных и вызывает метод `start_request`.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# StartProcessing(message)
```

### `personal_account`

```python
@bot.message_handler(commands=['profile'])
def personal_account(message):
    """
    Args:
        message:

    Returns:

    """
    global db
    user_id = str(message.chat.id)
    if db[user_id]['basic'] and (not db[user_id]['pro']):
        bot.send_message(chat_id=user_id, text="Подписка: BASIC\\nТекстовые генерации: безлимит\\nГенерация изображений: нет", parse_mode='html')
    elif db[user_id]['basic'] and db[user_id]['pro']:
        bot.send_message(chat_id=user_id, text="Подписка: PRO\\nТекстовые генерации: безлимит\\nГенерация изображений: безлимит", parse_mode='html')
    else:
        bot.send_message(chat_id=user_id, text=f"У вас нет подписки\\nТекстовые генерации: 10 в день, осталось:{db[user_id]['free_requests']}\\nГенерация изображений: нет", parse_mode='html')
```

**Назначение**: Обрабатывает команду `/profile`.

**Как работает функция**:
Функция `personal_account` обрабатывает команду `/profile`, отправленную пользователем. Она извлекает информацию о подписке пользователя из базы данных и отправляет соответствующее сообщение с информацией о текущей подписке, лимитах на генерацию текста и изображений. Если у пользователя нет активной подписки, сообщается о наличии 10 бесплатных текстовых генераций в день и остатке доступных запросов.

**Параметры**:

- `message`: Объект сообщения от Telegram API, содержащий информацию о команде `/profile`.

**Возвращает**:

- `None`: Функция ничего не возвращает, она отправляет сообщение пользователю с информацией о его профиле.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# personal_account(message)
```

### `show_stat`

```python
@bot.message_handler(commands=['stat'])
def show_stat(message):
    """
    Args:
        message:

    Returns:

    """
    global db
    user_id = str(message.chat.id)
    if user_id in ['2004851715', '206635551']:
        bot.send_message(chat_id=user_id, text=f"Всего пользователей: {len(db)}\\nС промокодом: {len([1 for el in db.values() if el['promocode']])}")
```

**Назначение**: Обрабатывает команду `/stat` для отображения статистики.

**Как работает функция**:
Функция `show_stat` обрабатывает команду `/stat`, отправленную пользователем. Она проверяет, является ли пользователь одним из администраторов (имеет ли его ID в списке `['2004851715', '206635551']`). Если пользователь является администратором, ему отправляется сообщение со статистикой: общее количество пользователей в базе данных и количество пользователей, использовавших промокод.

**Параметры**:

- `message`: Объект сообщения от Telegram API, содержащий информацию о команде `/stat`.

**Возвращает**:

- `None`: Функция ничего не возвращает, она отправляет сообщение пользователю со статистикой, если он является администратором.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# show_stat(message)
```

### `generate_promo_code`

```python
def generate_promo_code(length):
    """
    Args:
        length:

    Returns:

    """
    characters = string.ascii_letters + string.digits
    promo_code = ''.join(random.choices(characters, k=length))
    return promo_code
```

**Назначение**: Генерирует промокод заданной длины.

**Как работает функция**:
Функция `generate_promo_code` генерирует случайный промокод заданной длины. Она использует символы из `string.ascii_letters` (буквы ASCII в нижнем и верхнем регистре) и `string.digits` (цифры) для создания промокода. `random.choices` выбирает `k` случайных символов из заданной последовательности, а `''.join()` объединяет их в строку.

**Параметры**:

- `length` (int): Длина генерируемого промокода.

**Возвращает**:

- `str`: Сгенерированный промокод.

**Примеры**:

```python
>>> generate_promo_code(10)
'a1B2c3D4e5'
```

### `CallsProcessing`

```python
@bot.callback_query_handler(func=lambda call: True)
def CallsProcessing(call):
    """
    Args:
        call:

    Returns:

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
                if db[user_id]["pro"]:\
                    tb.ImageSize(call.message)
                else:\
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
                    def get_promo_code(message):
                        """
                        Args:
                            message:

                        Returns:

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

**Назначение**: Обрабатывает callback-запросы от кнопок в Telegram-боте.

**Как работает функция**:
Функция `CallsProcessing` обрабатывает callback-запросы, поступающие от нажатий на кнопки в интерфейсе Telegram-бота. Она определяет, какая кнопка была нажата, и выполняет соответствующие действия. Основные этапы работы функции:
1.  **Определение ID пользователя**: Извлекается ID пользователя из объекта `call.message.chat.id`.
2.  **Инициализация данных пользователя**: Если в базе данных отсутствует информация о пользователе, создается запись с использованием шаблона `DATA_PATTERN`.
3.  **Обработка основных кнопок задач**:
    *   `text`: Вызывается метод `tb.Text_types` для отображения типов текста.
    *   `images`: Проверяется, есть ли у пользователя подписка PRO. Если есть, вызывается метод `tb.ImageSize` для отображения размеров изображений. Иначе отправляется сообщение о необходимости обновления тарифа до PRO.
    *   `free`: Устанавливается флаг `free` в `True`, данные пользователя обновляются, удаляется предыдущее сообщение и вызывается метод `tb.FreeArea` для отображения бесплатной зоны.
    *   `tariff`: Вызывается метод `tb.TariffArea` для отображения информации о тарифах.
4.  **Обработка кнопок выбора размера изображения**:
    *   При нажатии на кнопки с размерами (`"576x1024"`, `"1024x1024"`, `"1024x576"`), размер сохраняется в базе данных и вызывается метод `tb.ImageArea` для отображения области генерации изображений.
5.  **Обработка кнопок управления изображением (`upscale`, `regenerate`)**:
    *   Извлекаются параметры изображения (размер, промпт, seed) из базы данных.
    *   `upscale`: Удаляется предыдущее сообщение, запускается поток для увеличения изображения, и вызывается метод `tb.BeforeUpscale`.
    *   `regenerate`: Удаляется предыдущее сообщение, генерируется новое случайное значение seed, запускается поток для повторной генерации изображения, сохраняются новые параметры в базе данных и вызывается метод `tb.ImageChange`.
6.  **Обработка кнопок выбора тарифа (`basic`, `pro`, `promo`, `ref`)**:
    *   `basic`: Если у пользователя нет подписки BASIC, вызывается метод `tb.Basic_tariff`. Иначе отправляется сообщение о том, что подписка уже подключена.
    *   `pro`: Если у пользователя нет подписки PRO, вызывается метод `tb.Pro_tariff`. Иначе отправляется сообщение о том, что подписка уже подключена.
    *   `promo`: Если у пользователя нет подписки PRO и не активирован промокод, запрашивается ввод промокода. Функция `get_promo_code` проверяет введенный промокод и, если он верен, активирует подписку PRO, начисляет токены и устанавливает дату окончания подписки.
        *   **Внутренняя функция `get_promo_code`**:
            *   **Назначение**: Проверяет введенный промокод и, если он верен, активирует подписку PRO.
            *   **Как работает функция**:
                Функция `get_promo_code` обрабатывает введенный пользователем промокод. Она проверяет, соответствует ли введенный промокод значению `"free24"` или реферальному коду других пользователей. Если промокод верен, активируется подписка PRO, начисляются токены, устанавливается дата окончания подписки, и пользователю отправляется сообщение об успешной активации. В противном случае отправляется сообщение о неверном промокоде.
            *   **Параметры**:
                *   `message` (types.Message): Объект сообщения от Telegram API, содержащий введенный пользователем промокод.
            *   **Возвращает**:
                *   `None`: Функция ничего не возвращает, она обновляет данные в базе данных и отправляет сообщение пользователю.
    *   `ref`: Если у пользователя нет реферального кода, он генерируется. Отправляется сообщение с реферальным кодом.
7.  **Обработка кнопок выбора текста (`text_buttons`)**:
    *   Определяется индекс нажатой кнопки.
    *   Если индекс входит в список `avalib`, вызывается метод `tb.SomeTexts`.
    *   Иначе устанавливается значение `1` в соответствующей позиции списка `db[user_id]['text']` и вызывается метод `tb.OneTextArea`.
8.  **Обработка кнопок выхода (`exit`, `text_exit`, `tariff_exit`)**:
    *   `exit`: Сбрасываются все текущие настройки, восстанавливаются данные пользователя и вызывается метод `tb.restart_markup`.
    *   `text_exit`: Сбрасываются настройки текста, устанавливается `db[user_id]['some'] = False` и вызывается метод `tb.Text_types`.
    *   `tariff_exit`: Удаляется сообщение и вызывается метод `tb.TariffExit`.
9.  **Обработка кнопок выбора одной текстовой области (`one_{ind}`)**:
    *   Определяется индекс выбранной области, устанавливается значение `1` в соответствующей позиции списка `db[user_id]['text']` и вызывается метод `tb.OneTextArea`.
10. **Обработка кнопок выбора нескольких текстовых областей (`some_{ind}`)**:

    *   Определяется индекс выбранной области, устанавливается значение `1` в соответствующей позиции списка `db[user_id]['text']`, устанавливается `db[user_id]['some'] = True` и вызывается метод `tb.SomeTextsArea`.

**Параметры**:

- `call`: Объект `types.CallbackQuery`, содержащий информацию о callback-запросе.

**Возвращает**:

- `None`: Функция ничего не возвращает, она выполняет действия в зависимости от нажатой кнопки.

**Примеры**:

```python
# Пример использования (не вызывается напрямую, обрабатывается декоратором)
# CallsProcessing(call)
```

### `TokensCancelletionPattern`

```python
def TokensCancelletionPattern(user_id: str, func, message, i: int = None) -> None:
    """
    Args:
        user_id (str):
        func:
        message:
        i (int, optional):  (Default value = None)

    Returns:

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

**Назначение**: Управляет использованием токенов и бесплатных запросов для пользователя.

**Как работает функция**:
Функция `TokensCancelletionPattern` управляет процессом списания токенов и бесплатных запросов для каждого пользователя при выполнении определенных действий (например, генерация текста). Она проверяет, достаточно ли у пользователя токенов или бесплатных запросов, вызывает соответствующую функцию для выполнения задачи и списывает использованные токены или запросы.

**Основные этапы работы функции**:

1.  **Извлечение данных пользователя**:
    *   Получение количества входящих и исходящих токенов (`in_tokens`, `out_tokens`) и количества бесплатных запросов (`free_requests`) из базы данных для указанного `user_id`.

2.  **Проверка наличия ресурсов**:
    *   Проверяется, есть ли у пользователя достаточно токенов (входящих и исходящих) или бесплатных запросов.

3.  **Выполнение задачи и списание ресурсов**:

    *   Если `i` равно `None`:
        *   Вызывается функция `func` с аргументами `message` и `db[user_id]['sessions_messages']`.
        *   Результаты выполнения функции (количество входящих и исходящих токенов, обновленные сообщения сессии) присваиваются переменным `incoming_tokens`, `outgoing_tokens` и `db[user_id]['sessions_messages']` соответственно.
        *   Устанавливается `cnt = 1`.
    *   Если `i` не равно `None`:
        *   Вызывается функция `func` с аргументами `message` и `i`, если `func` равна `tb.TextCommands`, иначе вызывается `func` с аргументами `message`, `i` и словарем, содержащим информацию о токенах и бесплатных запросах.
        *   Результаты выполнения функции (количество входящих и исходящих токенов, количество использованных запросов) присваиваются переменным `incoming_tokens`, `outgoing_tokens` и `cnt` соответственно.
    *   Если у пользователя есть токены (и `in_tokens > 0` и `out_tokens > 0`):
        *   Списываются использованные токены из баланса пользователя.
    *   Если у пользователя есть бесплатные запросы (`free_requests > 0`):
        *   Списываются использованные бесплатные запросы из баланса пользователя.

4.  **Обработка ситуаций, когда ресурсы закончились**:

    *   Если бесплатные запросы закончились (`db[user_id]['free_requests'] == 0`):
        *   Вызывается функция `tb.FreeTariffEnd` для отображения сообщения об окончании бесплатных запросов.
    *   Иначе (если токены закончились):
        *   Вызывается функция `tb.TarrifEnd` для отображения сообщения об окончании тарифа.
        *   Устанавли