# Анализ кода модуля `ToolBox_main.py`

**Качество кода: 7/10**
   -  Плюсы
        - Код достаточно структурирован и разделен на логические блоки.
        - Используются асинхронные функции и многопоточность для обработки задач.
        - Присутствует базовая обработка ошибок через `try-except` (хотя есть возможность улучшить).
        - Код использует `telebot` для работы с Telegram ботом.
        - Есть работа с базой данных.
        - Используется `dotenv` для загрузки переменных окружения.
   -  Минусы
        -  Много глобальных переменных, что усложняет отслеживание состояния.
        -  Сложная логика обработки сообщений и коллбэков, что делает код менее читаемым.
        -  Обработка ошибок не всегда логируется, что может затруднить отладку.
        -  Использование `match-case` (Python 3.10+) может быть улучшено добавлением `default` ветки.
        -  Не все функции документированы.
        -  Код не использует `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        -  Отсутствует описание модуля в начале файла.
        -  Много `magic strings`, которые можно вынести в константы.

**Рекомендации по улучшению**
1. **Документирование**: Добавить docstring к модулю, ко всем функциям и методам с использованием формата RST.
2. **Логирование**: Заменить `print` на `logger.error` для записи ошибок.
3. **Обработка ошибок**: Улучшить обработку ошибок, используя `logger.error` вместо общих `try-except`.
4. **Глобальные переменные**: Минимизировать использование глобальных переменных, передавая необходимые данные через аргументы функций.
5. **Импорты**: Добавить отсутствующие импорты `from src.logger import logger`
6. **Форматирование**: Использовать одинарные кавычки (`'`) для строк, где это требуется, и двойные (`"`) только для вывода.
7. **Константы**: Вынести `magic strings` в константы для улучшения читаемости и поддержки.
8. **`match-case`**: Добавить `default` ветку в `match-case`.
9. **База данных**: Пересмотреть логику работы с базой данных, возможно, стоит вынести ее в отдельный класс.
10. **Комментарии**: Добавить более подробные комментарии к сложному коду.
11. **Удалить Thread**: Заменить `Thread` на `asyncio.create_task` и `await`.
12. **Обработка JSON**: Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения данных (в текущем коде не требуется, но рекомендуется к использованию при работе с JSON).
13. **Удалить lambda**: Заменить lambda на обычные функции.
14. **Удалить вложенный try except**: Удалить вложенные `try except`  в цикле `for i in range(len(db[user_id]['text'])):`

**Оптимизированный код**

```python
"""
Модуль для обработки Telegram-бота с функциональностью текстовых и графических запросов.
=========================================================================================
Этот модуль содержит обработчики для команд и сообщений Telegram-бота,
а также логику для взаимодействия с базой данных и API.

Пример использования
--------------------

Пример запуска бота:

.. code-block:: python

    if __name__ == "__main__":
        Thread(target=bot.infinity_polling).start()
        asyncio.run(end_check_tariff_time())
"""
import asyncio
import base64
import string
import random
from telebot import types
from random import randint
from dotenv import load_dotenv
from datetime import datetime
#from threading import Thread # TODO: заменить на asyncio.create_task
from dateutil.relativedelta import relativedelta
from ToolBox_requests import ToolBox
from ToolBox_DataBase import DataBase
from src.logger import logger # TODO: добавить импорт logger

# Number of text types
N = 8
# User data initialization pattern
def data_pattern(text=None, sessions_messages=None, some=False, images="", free=False, basic=False, pro=False, incoming_tokens=0, outgoing_tokens=0, free_requests=10, datetime_sub=None, promocode=False, ref=''):
    """
    Создает шаблон данных пользователя.

    Args:
        text (list, optional): Список индексов текстовых запросов. По умолчанию [0]*N.
        sessions_messages (list, optional): Список сообщений сессии. По умолчанию [].
        some (bool, optional): Флаг выполнения множественных запросов. По умолчанию False.
        images (str, optional): Строка для хранения размера и seed изображения. По умолчанию "".
        free (bool, optional): Флаг бесплатного режима. По умолчанию False.
        basic (bool, optional): Флаг базовой подписки. По умолчанию False.
        pro (bool, optional): Флаг профессиональной подписки. По умолчанию False.
        incoming_tokens (int, optional): Количество входящих токенов. По умолчанию 0.
        outgoing_tokens (int, optional): Количество исходящих токенов. По умолчанию 0.
        free_requests (int, optional): Количество бесплатных запросов. По умолчанию 10.
        datetime_sub (datetime, optional): Дата окончания подписки. По умолчанию datetime.now() + 1 день.
        promocode (bool, optional): Флаг активации промокода. По умолчанию False.
        ref (str, optional): Реферальный код пользователя. По умолчанию "".

    Returns:
        dict: Словарь с данными пользователя.

    Example:
        >>> data_pattern()
        {'text': [0, 0, 0, 0, 0, 0, 0, 0], 'sessions_messages': [], 'some': False, 'images': '', 'free': False, 'basic': False, 'pro': False, 'incoming_tokens': 0, 'outgoing_tokens': 0, 'free_requests': 10, 'datetime_sub': datetime.datetime(...), 'promocode': False, 'ref': ''}
    """
    if text is None:
        text = [0] * N
    if sessions_messages is None:
        sessions_messages = []
    if datetime_sub is None:
        datetime_sub = datetime.now().replace(microsecond=0) + relativedelta(days=1)
    return {'text': text, "sessions_messages": sessions_messages, "some": some, 'images': images, 'free': free, 'basic': basic, 'pro': pro,
            'incoming_tokens': incoming_tokens, 'outgoing_tokens': outgoing_tokens,
            'free_requests': free_requests, 'datetime_sub': datetime_sub, 'promocode': promocode, 'ref': ref}

# Load environment variables
load_dotenv()
photo_array = []

# Objects initialized
tb = ToolBox(); bot = tb.bot
base = DataBase(db_name="UsersData.db", table_name="users_data_table",
                titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]", "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"}
                )

# Database initialization and connection
base.create(); db = base.load_data_from_db()

# Обработка запроса перед оплатой
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(pre_checkout_query):
    """
    Обрабатывает запрос перед оплатой.

    Args:
        pre_checkout_query (telebot.types.PreCheckoutQuery): Объект запроса перед оплатой.

    Returns:
        None
    """
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Обработка успешной оплаты
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    """
    Обрабатывает успешную оплату.

    Args:
        message (telebot.types.Message): Объект сообщения об успешной оплате.

    Returns:
        None
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

# Обработка команды start
@bot.message_handler(commands=['start'])
def start_processing(message):
    """
    Обрабатывает команду /start.

    Args:
        message (telebot.types.Message): Объект сообщения с командой /start.

    Returns:
        None
    """
    global db
    user_id = str(message.chat.id)
    db[user_id] = data_pattern() if not db.get(user_id, False) else data_pattern(basic=db[user_id]['basic'], pro=db[user_id]['pro'], incoming_tokens=db[user_id]['incoming_tokens'],
                                                                                outgoing_tokens=db[user_id]['outgoing_tokens'], free_requests=db[user_id]['free_requests'], datetime_sub=db[user_id]['datetime_sub'],
                                                                                promocode=db[user_id]['promocode'], ref=db[user_id]['ref']
                                                                                )
    base.insert_or_update_data(user_id, db[user_id])
    tb.start_request(message)

# Информация о тарифе
@bot.message_handler(commands=['profile'])
def personal_account(message):
    """
    Выводит информацию о текущем тарифе пользователя.

    Args:
        message (telebot.types.Message): Объект сообщения с командой /profile.

    Returns:
        None
    """
    global db
    user_id = str(message.chat.id)
    if db[user_id]['basic'] and (not db[user_id]['pro']):
        bot.send_message(chat_id=user_id, text="Подписка: BASIC\nТекстовые генерации: безлимит\nГенерация изображений: нет", parse_mode='html')
    elif db[user_id]['basic'] and db[user_id]['pro']:
        bot.send_message(chat_id=user_id, text="Подписка: PRO\nТекстовые генерации: безлимит\nГенерация изображений: безлимит", parse_mode='html')
    else:
        bot.send_message(chat_id=user_id, text=f"У вас нет подписки\nТекстовые генерации: 10 в день, осталось:{db[user_id]['free_requests']}\nГенерация изображений: нет", parse_mode='html')

# Показ статистики
@bot.message_handler(commands=['stat'])
def show_stat(message):
    """
    Выводит статистику бота для администраторов.

    Args:
        message (telebot.types.Message): Объект сообщения с командой /stat.

    Returns:
        None
    """
    global db
    user_id = str(message.chat.id)
    if user_id in ['2004851715', '206635551']:
        bot.send_message(chat_id=user_id, text=f"Всего пользователей: {len(db)}\nС промокодом: {len([1 for el in db.values() if el['promocode']])}")

# Генерация промокода
def generate_promo_code(length):
    """
    Генерирует случайный промокод заданной длины.

    Args:
        length (int): Длина промокода.

    Returns:
        str: Сгенерированный промокод.

    Example:
        >>> generate_promo_code(10)
        'aB1cD2eF3g'
    """
    characters = string.ascii_letters + string.digits
    promo_code = ''.join(random.choices(characters, k=length))
    return promo_code

# Обработка callback запросов
@bot.callback_query_handler(func=lambda call: True)
def calls_processing(call):
    """
    Обрабатывает все callback-запросы от кнопок.

    Args:
        call (telebot.types.CallbackQuery): Объект callback-запроса.

    Returns:
        None
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
        db[user_id] = data_pattern()
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
            case _:
                logger.error(f"Неизвестный callback data: {call.data}")

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
                #thr=Thread(target=tb.Image_Regen_And_Upscale, args=(call.message, prompt, size, int(seed), 30))
                #thr.start(); thr.join()
                asyncio.create_task(tb.Image_Regen_And_Upscale(call.message, prompt, size, int(seed), 30))
                tb.BeforeUpscale(call.message)
            case "regenerate":
                bot.delete_message(user_id, call.message.message_id)
                seed = randint(1, 1000000)
                #thr=Thread(target=tb.Image_Regen_And_Upscale, args=(call.message, prompt, size, seed))
                #thr.start()
                asyncio.create_task(tb.Image_Regen_And_Upscale(call.message, prompt, size, seed))
                db[user_id]["images"] = '|'.join(db[user_id]["images"].rsplit('|')[:2])+'|'+str(seed)
                base.insert_or_update_data(user_id, db[user_id])
                #thr.join()
                tb.ImageChange(call.message)
            case _:
                logger.error(f"Неизвестный callback data: {call.data}")

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
                         
                        if message.text.lower() == "free24" or message.text in [us['ref'] for us in db.values()] and db[user_id]['ref']!=message.text:
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
            case _:
                logger.error(f"Неизвестный callback data: {call.data}")
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
                db[user_id] = data_pattern(basic=db[user_id]['basic'], pro=db[user_id]['pro'], incoming_tokens=db[user_id]['incoming_tokens'],
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
            case _:
                logger.error(f"Неизвестный callback data: {call.data}")

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

# Pattern for tokens cancellation
def tokens_cancelletion_pattern(user_id: str, func, message, i: int = None) -> None:
    """
    Управляет списанием токенов или бесплатных запросов пользователя.

    Args:
        user_id (str): ID пользователя.
        func (function): Функция для обработки запроса.
        message (telebot.types.Message): Объект сообщения.
        i (int, optional): Индекс для текстовых запросов. Defaults to None.

    Returns:
        None
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


# Обработка сообщений и фото
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def tasks_processing(message):
    """
    Обрабатывает входящие текстовые сообщения и фотографии.

    Args:
        message (telebot.types.Message): Объект сообщения.

    Returns:
        None
    """
    global db
    user_id = str(message.chat.id)

    # Images processing
    if db[user_id]['images'] != "" and len(db[user_id]['images'].split('|')) == 1:
        size = [int(el) for el in db[user_id]['images'].split('x')]
        prompt = message.text
        seed = tb.ImageCommand(message, prompt, size)
        db[user_id]['images']+='|'+prompt+'|'+str(int(seed))
    
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
            #thr = Thread(target=tokens_cancelletion_pattern, args=(user_id, tb.FreeCommand, message))
            #thr.start(); thr.join()
            asyncio.create_task(tokens_cancelletion_pattern(user_id, tb.FreeCommand, message))
        else:
            #thr = Thread(target=tokens_cancelletion_pattern, args=(user_id, tb.FreeCommand, message))
            #thr.start(); thr.join()
            asyncio.create_task(tokens_cancelletion_pattern(user_id, tb.FreeCommand, message))
    # Text processing
    else:
        for i in range(len(db[user_id]['text'])):
            if db[user_id]['text'][i] and not db[user_id]['some']:
                #thr=Thread(target=tokens_cancelletion_pattern, args=(user_id, tb.TextCommands, message, i))
                #thr.start()
                asyncio.create_task(tokens_cancelletion_pattern(user_id, tb.TextCommands, message, i))
                db[user_id]['text'][i] = 0
                #thr.join()
            elif db[user_id]['text'][i] and db[user_id]['some']:
                #thr=Thread(target=tokens_cancelletion_pattern, args=(user_id, tb.SomeTextsCommand, message, i))
                #thr.start()
                asyncio.create_task(tokens_cancelletion_pattern(user_id, tb.SomeTextsCommand, message, i))
                db[user_id]['text'][i] = 0
                db[user_id]['some'] = False
                #thr.join()
    base.insert_or_update_data(user_id, db[user_id])

# Проверка окончания тарифа
async def end_check_tariff_time():
    """
    Асинхронно проверяет время окончания тарифа у пользователей.

    Returns:
        None
    """
    while True:
        global db
        for user_id, data in db.items():
            deltaf = data['datetime_sub'] - datetime.now().replace(microsecond=0)
            if int(deltaf.total_seconds()) <= 0 and (data['basic'] or data['pro'] or data['free_requests']<10):
                db[user_id] = data_pattern(text=data['text'], images=data['images'],
                                        free=data['free'], promocode=data['promocode'], ref=data['ref'])
                base.insert_or_update_data(user_id, db[user_id])
        await asyncio.sleep(10)

# Bot launch
if __name__ == "__main__":
    #Thread(target=bot.infinity_polling).start()
    asyncio.create_task(bot.infinity_polling())
    asyncio.run(end_check_tariff_time())
```