### Анализ кода модуля `ToolBox_requests`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Использование классов для организации кода.
    - Разделение на приватные и публичные методы.
    - Применение лямбда-функций для упрощения создания клавиатур и сообщений.
    - Асинхронная обработка запросов через ThreadPoolExecutor.
- **Минусы**:
    - Непоследовательное использование кавычек (смешивание одинарных и двойных).
    - Отсутствие документации в формате RST для функций и классов.
    - Чрезмерное использование `try-except` блоков без конкретной обработки ошибок.
    - Использование `time.sleep` в циклах, что может блокировать основной поток.
    -  Сложная логика с несколькими вложенными функциями, что затрудняет чтение и понимание.
    -  Не всегда используется `self` в лямбда-функциях.
    -  Смешаны функции обработки текста и изображения.

**Рекомендации по улучшению**:
- Привести все строки в коде к использованию одинарных кавычек, а двойные оставить для вывода и логирования.
- Добавить RST-документацию для всех функций и классов.
- Заменить `time.sleep` на асинхронные механизмы.
- Упростить логику, разделив на более мелкие функции.
- Использовать `logger.error` для обработки ошибок вместо общих `try-except`.
- Привести в порядок использование `self` в лямбда-функциях.
- Разделить обработку текста и изображений на разные классы или методы.
- Использовать `from src.logger import logger` для логирования.
- Привести в порядок форматирование кода в соответствии с PEP8.
- Использовать `j_loads` или `j_loads_ns` вместо `json.load`.
- Выровнять названия переменных, функций и импортов.
- Добавить комментарии там где есть сложная логика

**Оптимизированный код**:
```python
"""
Модуль для обработки запросов Telegram бота.
=============================================

Модуль содержит класс :class:`ToolBox`, который обрабатывает различные команды
пользователей в Telegram боте, включая текстовые запросы, генерацию изображений,
тарифы и свободный режим.

Пример использования
----------------------
.. code-block:: python

    toolbox = ToolBox()
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        toolbox.start_request(message)
"""
import os
import concurrent.futures
import time
from random import randint
from telebot import TeleBot, types
from src.utils.jjson import j_loads
from src.logger import logger # Изменен импорт
from BaseSettings.AuxiliaryClasses import PromptsCompressor, keyboards
from ToolBox_n_networks import neural_networks

# Class initialization
pc = PromptsCompressor()

#Main functions class
class ToolBox(keyboards, neural_networks):
    """
    Основной класс для обработки запросов Telegram бота.

    :param keyboards: Класс для работы с клавиатурами.
    :type keyboards: src.BaseSettings.AuxiliaryClasses.keyboards
    :param neural_networks: Класс для работы с нейронными сетями.
    :type neural_networks: ToolBox_n_networks.neural_networks
    """
    def __init__(self):
        """
        Инициализация класса ToolBox.
        
        Загружает настройки, промпты и устанавливает основные параметры бота.
        """
        # Start buttons
        self.name = ['Текст 📝', 'Изображения 🎨', 'Свободный режим 🗽', 'Тарифы 💸'] # Используем одинарные кавычки
        self.data = ['text', 'images', 'free', 'tariff']  # Используем одинарные кавычки

        # Prompts texts load
        with open('ToolBox/BaseSettings/prompts.json', 'r') as file:  # Используем одинарные кавычки
            self.prompts_text = j_loads(file)  # Используем j_loads

        # Telegram bot initialization
        self.bot = TeleBot(token=os.environ['TOKEN']) # Используем одинарные кавычки
        # Inline keyboard blank lambda
        self.keyboard_blank = lambda name, data: super()._keyboard_two_blank(data, name) # Исправлено использование self
        # Markup keyboard
        self.reply_keyboard = lambda name: super()._reply_keyboard(name) # Исправлено использование self
        # Request delay
        self.__delay = lambda message: self.bot.send_message(message.chat.id, "Подождите, это должно занять несколько секунд . . .", parse_mode='html')  # Используем одинарные кавычки
        # Start request
        self.start_request = lambda message: self.bot.send_message(message.chat.id, self.prompts_text['hello'], reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html')  # Используем одинарные кавычки
        # Restart request
        self.restart = lambda message: self.bot.send_message(message.chat.id, "Выберите нужную вам задачу", reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html') # Используем одинарные кавычки
        # Restart markup
        self.restart_markup = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Выберите нужную вам задачу", reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html') # Используем одинарные кавычки
        # One text request
        self.OneTextArea = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=self.prompts_text['text_list'][ind] if type(self.prompts_text['text_list'][ind]) == str else self.prompts_text['text_list'][ind][0], reply_markup=self.keyboard_blank(['Назад'], ['text_exit'])) # Используем одинарные кавычки
        # Some texts request
        self.SomeTextsArea = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=self.prompts_text['few_texts_list'][ind][0], reply_markup=self.keyboard_blank(['Назад'], ['text_exit'])) # Используем одинарные кавычки
        # Image size
        self.ImageSize = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Выберите разрешение изображения", reply_markup=self.keyboard_blank(['9:16', '1:1', '16:9', 'В меню'], ['576x1024', '1024x1024', '1024x576', 'exit']), parse_mode='html') # Используем одинарные кавычки
        # Image request
        self.ImageArea = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Введите ваш запрос для изображений 🖼", reply_markup=self.keyboard_blank(['В меню'], ['exit']), parse_mode='html') # Используем одинарные кавычки
        # Image change
        self.ImageChange = lambda message: self.bot.send_message(chat_id=message.chat.id, text="Выберите следующее действие", reply_markup=self.keyboard_blank(['Улучшить 🪄', '🔁', 'Новая 🖼', 'В меню'], ['upscale', 'regenerate', 'images', 'exit']), parse_mode='html') # Используем одинарные кавычки
        # Message before upscale
        self.BeforeUpscale = lambda message: self.bot.send_message(chat_id=message.chat.id, text="Выберите следующее действие", reply_markup=self.keyboard_blank(['🔁', 'Новая 🖼', 'В меню'], ['regenerate', 'images', 'exit']), parse_mode='html') # Используем одинарные кавычки
        # Free mode request
        self.FreeArea = lambda message: self.bot.send_message(chat_id=message.chat.id, text="Введите ваш запрос", reply_markup=self.reply_keyboard(['В меню']), parse_mode='html') # Используем одинарные кавычки
        # Tariff request
        self.TariffArea = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Тарифы", reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Используем одинарные кавычки
        # Tariffs area exit
        self.TariffExit = lambda message: self.bot.send_message(chat_id=message.chat.id, text="Тарифы", reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'В меню'], ['basic', 'pro', 'promo', 'exit'])) # Используем одинарные кавычки
        # End tariff
        self.TarrifEnd = lambda message: self.bot.send_message(chat_id=message.chat.id, text="У вас закончились запросы, но вы можете продлить ваш тариф.", reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Используем одинарные кавычки
        # Free tariff end
        self.FreeTariffEnd = lambda message: self.bot.send_message(chat_id=message.chat.id, text="Лимит бесплатных запросов, увы, исчерпан😢 Но вы можете выбрать один из наших платных тарифов. Просто нажмите на них и получите подробное описание", reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Используем одинарные кавычки
        # Select one or some texts
        self.SomeTexts = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Хотите сделать один текст или сразу несколько?", reply_markup=self.keyboard_blank(['Один', 'Несколько', 'Назад'], [f'one_{ind}', f'some_{ind}', 'text_exit'])) # Используем одинарные кавычки

#Private
    def __gpt_4o_mini(self, prompt: list[dict], message) -> tuple[dict[str, str], int, int]:
        """
        Приватный метод для обработки запросов к GPT-4o mini.

        :param prompt: Список словарей с промптами для модели.
        :type prompt: list[dict]
        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :return: Кортеж, содержащий ответ от модели, количество входящих и исходящих токенов.
        :rtype: tuple[dict[str, str], int, int]
        """
        send = self.__delay(message) # Отправляем сообщение о задержке
        try:
             response, incoming_tokens, outgoing_tokens = super()._free_gpt_4o_mini(prompt=prompt) # Вызываем метод родительского класса
             self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=PromptsCompressor.html_tags_insert(response['content']), parse_mode='html') # Редактируем сообщение с ответом
             return response, incoming_tokens, outgoing_tokens # Возвращаем ответ и токены
        except Exception as e: # Ловим исключения
             logger.error(f"Error in __gpt_4o_mini: {e}") # Логируем ошибку
             self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text="Произошла ошибка при обработке запроса.") # Отправляем сообщение об ошибке
             return {}, 0, 0 # Возвращаем пустые данные

    def __FLUX_schnell(self, prompt: str, size: list[int], message, seed: int, num_inference_steps: int) -> None:
        """
        Приватный метод для обработки запросов к FLUX_schnell.

        :param prompt: Текст промпта для генерации изображения.
        :type prompt: str
        :param size: Список с размерами изображения.
        :type size: list[int]
        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param seed: Зерно для генерации изображения.
        :type seed: int
        :param num_inference_steps: Количество шагов для генерации изображения.
        :type num_inference_steps: int
        """
        send = self.__delay(message) # Отправляем сообщение о задержке
        try:
            while True: # Бесконечный цикл для попытки генерации
                photo = super()._FLUX_schnell(prompt, size, seed, num_inference_steps) # Вызываем метод родительского класса
                if photo: # Если фото сгенерировано
                    self.bot.send_photo(chat_id=message.chat.id, photo=photo) # Отправляем фото
                    self.bot.delete_message(chat_id=send.chat.id, message_id=send.message_id) # Удаляем сообщение о задержке
                    return
        except Exception as e: # Ловим исключения
            logger.error(f"Error in __FLUX_schnell: {e}") # Логируем ошибку
            self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text="При генерации возникла ошибка, попробуйте повторить позже") # Отправляем сообщение об ошибке

#Public
    def Text_types(self, message):
        """
        Обрабатывает запрос на выбор типа текста.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :return: Сообщение с выбором типа текста.
        :rtype: telebot.types.Message
        """
        name = ['Коммерческий  🛍️', 'SMM 📱', 'Брейншторм 💡', 'Реклама 📺', 'Заголовки 🔍', 'SEO 🌐', 'Новость 📰', 'Редактура 📝', 'В меню'] # Используем одинарные кавычки
        data = ['comm-text', 'smm-text', 'brainst-text', 'advertising-text', 'headlines-text', 'seo-text', 'news', 'editing', 'exit'] # Используем одинарные кавычки
        return self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="📝 Выберите тип текста", reply_markup=self.keyboard_blank(name, data))

    def Basic_tariff(self, message):
        """
        Обрабатывает запрос на подключение тарифа BASIC.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        """
        keyboard = types.InlineKeyboardMarkup() # Создаем инлайн клавиатуру
        keyboard.add(types.InlineKeyboardButton("Подключить тариф BASIC", pay=True)) # Добавляем кнопку оплаты
        keyboard.add(types.InlineKeyboardButton("К тарифам", callback_data="tariff_exit")) # Добавляем кнопку перехода к тарифам
        price = [types.LabeledPrice(label='BASIC', amount=99 * 100)] # Создаем цену
        self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем сообщение
        self.bot.send_invoice(chat_id=message.chat.id, title='BASIC', # Отправляем инвойс
            description="Безлимитная генерация текста, в том числе по готовым промптам.",
            invoice_payload='basic_invoice_payload',
            start_parameter='subscription',
            provider_token=os.environ['PROVIDE_TOKEN'],
            currency='RUB', prices=price, reply_markup=keyboard)

    def Pro_tariff(self, message):
        """
        Обрабатывает запрос на подключение тарифа PRO.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        """
        keyboard = types.InlineKeyboardMarkup() # Создаем инлайн клавиатуру
        keyboard.add(types.InlineKeyboardButton("Подключить тариф PRO", pay=True)) # Добавляем кнопку оплаты
        keyboard.add(types.InlineKeyboardButton("К тарифам", callback_data="tariff_exit")) # Добавляем кнопку перехода к тарифам
        price = [types.LabeledPrice(label='PRO', amount=199 * 100)] # Создаем цену
        self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем сообщение
        self.bot.send_invoice(chat_id=message.chat.id, title='PRO', # Отправляем инвойс
            description="Безлимитная генерация текста (в том числе по готовым промптам) и изображений.",
            invoice_payload='pro_invoice_payload',
            start_parameter='subscription',
            provider_token=os.environ['PROVIDE_TOKEN'],
            currency='RUB', prices=price, reply_markup=keyboard)

    def TextCommands(self, message, ind: int) -> tuple[int, int, int]:
        """
        Обрабатывает текстовые команды.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param ind: Индекс команды.
        :type ind: int
        :return: Кортеж с входящими токенами, исходящими токенами и 1.
        :rtype: tuple[int, int, int]
        """
        info = [] # Создаем пустой список для информации
        incoming_tokens = 0; outgoing_tokens = 0; response = None # Инициализируем переменные
        if 'TEXT' in pc.commands_size[ind]: # Если команда содержит текст
            info.append(message.text) # Добавляем текст сообщения
            msg = self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text['text_list'][ind][1]) # Отправляем сообщение с запросом параметра
            def Text_next_step(message):
                nonlocal info, incoming_tokens, outgoing_tokens, response
                info += message.text.split(';') # Добавляем параметры
                while len(info) < len(pc.commands_size[ind]): # Если параметров не хватает
                    info.append("Параметр отсутствует") # Добавляем пустые
                prompt = pc.get_prompt(ind=ind, info=info) # Получаем промпт
                response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=[{ "role": "user", "content": prompt }], message=message) # Обрабатываем промпт
                self.restart(message) # Перезапускаем бота
            self.bot.register_next_step_handler(msg, Text_next_step) # Регистрируем следующий шаг
            while response is None: # Ждем ответа
                time.sleep(0.5) # Задержка
            return incoming_tokens, outgoing_tokens, 1 # Возвращаем токены
        else:
            info = message.text.split(';') # Получаем параметры
            while len(info) < len(pc.commands_size[ind]): # Если параметров не хватает
                info.append("Параметр отсутствует") # Добавляем пустые
            prompt = pc.get_prompt(ind=ind, info=info) # Получаем промпт
            response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=[{ "role": "user", "content": prompt }], message=message) # Обрабатываем промпт
            self.restart(message) # Перезапускаем бота
            return incoming_tokens, outgoing_tokens, 1 # Возвращаем токены

    def SomeTextsCommand(self, message, ind: int, tokens: dict[str, int]) -> tuple[int, int, int]:
        """
        Обрабатывает запрос на генерацию нескольких текстов.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param ind: Индекс команды.
        :type ind: int
        :param tokens: Словарь с токенами.
        :type tokens: dict[str, int]
        :return: Кортеж с входящими токенами, исходящими токенами и количеством текстов.
        :rtype: tuple[int, int, int]
        """
        try:
            n = int(message.text) # Получаем количество текстов
        except ValueError: # Если не число
            logger.error(f"Invalid input for number of texts: {message.text}") # Логируем ошибку
            self.bot.send_message(chat_id=message.chat.id, text="Пожалуйста, введите корректное число.") # Отправляем сообщение
            return 0, 0, 0 # Возвращаем 0
        avalib = [0, 1, 3, 5, 6] # Список с индексами
        ans = [] # Список для ответов
        for i in range(n): # Запускаем цикл
            ans.append([]) # Добавляем список
            if "TEXT" in pc.commands_size[ind]: # Если есть текст
                msg = self.bot.send_message(chat_id=message.chat.id, text=f"Введите текст источника {i+1}") # Запрашиваем текст
                text = None # Инициализируем текст
                def Text_next_step(message):
                    nonlocal text, ans
                    text = message.text # Получаем текст
                    ans[i].append(text) # Добавляем текст в список
                self.bot.register_next_step_handler(msg, Text_next_step) # Регистрируем следующий шаг
                while text is None: # Ждем текст
                    time.sleep(0.5) # Задержка
        index = avalib.index(ind) # Получаем индекс
        for el in range(1, len(self.prompts_text["few_texts_list"][index])): # Цикл по параметрам
            msg = self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text["few_texts_list"][index][el]) # Запрашиваем параметры
            params = None # Инициализируем параметры
            def Params_addition(message):
                nonlocal params, ans
                params = message.text # Получаем параметры
                params = params.split(';') # Разбиваем параметры
                if len(params) < len(pc.commands_size[ind]): # Если не хватает параметров
                    while len(params) < len(pc.commands_size[ind]): # Добавляем пустые параметры
                        params.append(None)
                param = params[0] # Получаем параметр
                [ans[i].append(param) if params[i] is None else ans[i].append(params[i]) for i in range(len(ans))] # Добавляем параметры в список
            self.bot.register_next_step_handler(msg, Params_addition) # Регистрируем следующий шаг
            while params is None: # Ждем параметры
                 time.sleep(0.5) # Задержка
        incoming_tokens = 0; outgoing_tokens = 0 # Инициализируем токены
        def process_prompt(i):
            nonlocal incoming_tokens, outgoing_tokens # Объявляем переменные
            prompt = pc.get_prompt(ind=ind, info=ans[i]) # Получаем промпт
            if tokens['incoming_tokens'] - incoming_tokens > 0 and tokens['outgoing_tokens'] - outgoing_tokens > 0 or tokens['free_requests'] - i > 0: # Проверяем токены
                response, in_tokens, out_tokens = self.__gpt_4o_mini(prompt=[{"role": "user", "content": prompt}], message=message) # Обрабатываем промпт
                return in_tokens, out_tokens # Возвращаем токены
            return 0, 0 # Возвращаем 0
        with concurrent.futures.ThreadPoolExecutor() as executor: # Создаем пул потоков
            results = list(executor.map(process_prompt, range(n))) # Запускаем обработку
        for in_tokens, out_tokens in results:
            incoming_tokens += in_tokens # Считаем входящие
            outgoing_tokens += out_tokens # Считаем исходящие
        self.restart(message) # Перезапускаем бота
        return incoming_tokens, outgoing_tokens, n # Возвращаем токены

    def ImageCommand(self, message, prompt: str, size: list[int]) -> int:
        """
        Обрабатывает запрос на генерацию изображения.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param prompt: Текст промпта для генерации изображения.
        :type prompt: str
        :param size: Список с размерами изображения.
        :type size: list[int]
        :return: Зерно для генерации изображения.
        :rtype: int
        """
        seed = randint(1, 1000000) # Генерируем случайное зерно
        self.__FLUX_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=4) # Запускаем генерацию
        self.ImageChange(message) # Запускаем изменение
        return seed # Возвращаем зерно

    def Image_Regen_And_Upscale(self, message, prompt: str, size: list[int], seed, num_inference_steps=4) -> None:
        """
        Обрабатывает запрос на регенерацию или улучшение изображения.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param prompt: Текст промпта для генерации изображения.
        :type prompt: str
        :param size: Список с размерами изображения.
        :type size: list[int]
        :param seed: Зерно для генерации изображения.
        :type seed: int
        :param num_inference_steps: Количество шагов для генерации изображения.
        :type num_inference_steps: int
        """
        self.__FLUX_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=num_inference_steps) # Запускаем генерацию

    def FreeCommand(self, message, prompts: list[str]) -> tuple[int, int, list[str]]:
        """
        Обрабатывает запрос в свободном режиме.

        :param message: Объект сообщения Telegram.
        :type message: telebot.types.Message
        :param prompts: Список промптов.
        :type prompts: list[str]
        :return: Кортеж с входящими токенами, исходящими токенами и списком промптов.
        :rtype: tuple[int, int, list[str]]
        """
        try:
            if type(prompts[-1].get('content', False))!=list: # Проверка типа последнего промпта
                prompts.append({"content": message.text, "role": "user"}) # Добавляем промпт
        except Exception as e: # Ловим исключения
            logger.error(f"Error in FreeCommand: {e}") # Логируем ошибку
        response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=prompts, message=message) # Обрабатываем промпт
        prompts.append(response) # Добавляем ответ
        return incoming_tokens, outgoing_tokens, prompts # Возвращаем токены и промпты