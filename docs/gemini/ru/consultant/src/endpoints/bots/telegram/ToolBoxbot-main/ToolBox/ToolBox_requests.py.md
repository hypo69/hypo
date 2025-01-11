# Анализ кода модуля ToolBox_requests

**Качество кода: 6/10**

*   **Плюсы:**
    *   Используются лямбда-функции для создания однотипных действий.
    *   Код разбит на методы, что улучшает читаемость.
    *   Используются классы для разделения функциональности.
*   **Минусы:**
    *   Отсутствует описание модуля.
    *   Не все функции документированы.
    *   Не все импорты расположены в начале файла.
    *   Используются множественные лямбды, что усложняет восприятие кода.
    *   Слишком длинные строки кода.
    *   Использование `while True` с `try-except` для обработки ошибок, что может привести к бесконечному циклу.
    *   Используется `time.sleep` что плохо влияет на производительность.
    *   Не используется `from src.logger.logger import logger` для логирования ошибок.
    *   Много дублирующегося кода, например, при отправке сообщений с разными текстами, но с одинаковой структурой.
    *   Сложная логика `TextCommands` и `SomeTextsCommand`, что делает код трудно читаемым.
    *   Несогласованность в наименовании переменных (например, `avalib` вместо `available`).

**Рекомендации по улучшению:**

1.  **Документирование:**
    *   Добавить docstring для модуля, классов и методов в формате RST.
    *   Включить описания аргументов и возвращаемых значений функций.
2.  **Импорты:**
    *   Перенести все импорты в начало файла.
3.  **Рефакторинг:**
    *   Заменить лямбда-функции на обычные для лучшей читаемости и возможности документирования.
    *   Упростить и разбить на более мелкие функции методы `TextCommands` и `SomeTextsCommand`.
    *   Избавиться от `while True` с `try-except`, заменить обработкой ошибок с помощью `logger.error`.
    *   Использовать `asyncio.sleep` вместо `time.sleep`
    *   Избегать использования множественных `nonlocal` переменных.
    *   Упростить отправку сообщений, возможно, через отдельную функцию.
    *   Переработать метод `__FLUX_schnell` для исключения бесконечного цикла.
    *   Использовать константы для магических значений (например, `num_inference_steps`).
    *   Переименовать переменные в соответствии со стандартами (например, `avalib` на `available`).
4.  **Логирование:**
    *   Использовать `from src.logger.logger import logger` для логирования ошибок.
5.  **Улучшения:**
    *   Разделить функции отправки сообщений и обработки данных.
    *   В `TextCommands` и `SomeTextsCommand` использовать асинхронные функции и `asyncio.sleep`.

**Оптимизированный код:**
```python
"""
Модуль для обработки запросов от пользователей Telegram бота.
===========================================================

Этот модуль содержит класс :class:`ToolBox`, который обрабатывает различные запросы
от пользователей Telegram бота, включая генерацию текста и изображений с
использованием нейронных сетей.

Пример использования
--------------------

Пример использования класса `ToolBox`:

.. code-block:: python

    toolbox = ToolBox()
    toolbox.bot.polling(none_stop=True)
"""
import asyncio
import os
import json
import concurrent.futures
from random import randint
import base64
from pathlib import Path
from typing import Any, List, Dict, Tuple
from telebot import TeleBot, types
from src.logger.logger import logger  # Correct import
from BaseSettings.AuxiliaryClasses import PromptsCompressor, keyboards
from ToolBox_n_networks import neural_networks
from src.utils.jjson import j_loads  # Используем j_loads

# Инициализация класса
pc = PromptsCompressor()


# Основной класс для обработки запросов
class ToolBox(keyboards, neural_networks):
    """
    Класс для обработки запросов от пользователей Telegram бота.

    Attributes:
        name (List[str]): Список имен кнопок для главного меню.
        data (List[str]): Список данных кнопок для главного меню.
        prompts_text (Dict[str, Any]): Словарь с текстами подсказок.
        bot (TeleBot): Экземпляр бота TeleBot.
        keyboard_blank (Callable): Лямбда-функция для создания инлайн-клавиатуры.
        reply_keyboard (Callable): Лямбда-функция для создания обычной клавиатуры.
        __delay (Callable): Лямбда-функция для отправки сообщения ожидания.
        start_request (Callable): Лямбда-функция для отправки стартового сообщения.
        restart (Callable): Лямбда-функция для отправки сообщения о перезапуске.
        restart_markup (Callable): Лямбда-функция для редактирования сообщения о перезапуске.
        OneTextArea (Callable): Лямбда-функция для отображения текста запроса.
        SomeTextsArea (Callable): Лямбда-функция для отображения нескольких текстов запроса.
        ImageSize (Callable): Лямбда-функция для выбора размера изображения.
        ImageArea (Callable): Лямбда-функция для запроса ввода изображения.
        ImageChange (Callable): Лямбда-функция для отображения действий с изображением.
        BeforeUpscale (Callable): Лямбда-функция для отображения действий перед улучшением.
        FreeArea (Callable): Лямбда-функция для запроса свободного режима.
        TariffArea (Callable): Лямбда-функция для запроса выбора тарифа.
        TariffExit (Callable): Лямбда-функция для выхода из меню тарифов.
        TarrifEnd (Callable): Лямбда-функция для уведомления об окончании тарифа.
        FreeTariffEnd (Callable): Лямбда-функция для уведомления об окончании бесплатных запросов.
        SomeTexts (Callable): Лямбда-функция для выбора количества текстов.
    """

    def __init__(self):
        # Start buttons
        self.name = ['Текст 📝', 'Изображения 🎨', 'Свободный режим 🗽', 'Тарифы 💸']
        self.data = ['text', 'images', 'free', 'tariff']

        # Prompts texts load
        try:
            with open('ToolBox/BaseSettings/prompts.json', 'r') as file:  # Используем 'r' для чтения
                self.prompts_text = j_loads(file) # Используем j_loads
        except Exception as ex:
             logger.error('Ошибка загрузки файла prompts.json', ex)
             self.prompts_text = {}

        # Telegram bot initialization
        self.bot = TeleBot(token=os.environ['TOKEN'])
        # Inline keyboard blank lambda
        self.keyboard_blank = lambda name, data: super()._keyboard_two_blank(data, name)  # Убрал self из лямбды
        # Markup keyboard
        self.reply_keyboard = lambda name: super()._reply_keyboard(name) # Убрал self из лямбды
        # Request delay
        self.__delay = lambda message: self.bot.send_message(message.chat.id, 'Подождите, это должно занять несколько секунд . . .', parse_mode='html') # Убрал self из лямбды
        # Start request
        self.start_request = lambda message: self.bot.send_message(message.chat.id, self.prompts_text['hello'], reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html') # Убрал self из лямбды
        # Restart request
        self.restart = lambda message: self.bot.send_message(message.chat.id, 'Выберите нужную вам задачу', reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html') # Убрал self из лямбды
        # Restart murkup
        self.restart_markup = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Выберите нужную вам задачу', reply_markup=self.keyboard_blank(self.name, self.data), parse_mode='html') # Убрал self из лямбды
        # One text request
        self.OneTextArea = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=self.prompts_text['text_list'][ind] if isinstance(self.prompts_text['text_list'][ind], str) else self.prompts_text['text_list'][ind][0], reply_markup=self.keyboard_blank(['Назад'], ['text_exit'])) # Убрал self из лямбды
        # Some texts request
        self.SomeTextsArea = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=self.prompts_text['few_texts_list'][ind][0], reply_markup=self.keyboard_blank(['Назад'], ['text_exit'])) # Убрал self из лямбды
        # Image size
        self.ImageSize = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Выберите разрешение изображения', reply_markup=self.keyboard_blank(['9:16', '1:1', '16:9', 'В меню'], ['576x1024', '1024x1024', '1024x576', 'exit']), parse_mode='html') # Убрал self из лямбды
        # Image request
        self.ImageArea = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Введите ваш запрос для изображений 🖼', reply_markup=self.keyboard_blank(['В меню'], ['exit']), parse_mode='html') # Убрал self из лямбды
        # Image change
        self.ImageChange = lambda message: self.bot.send_message(chat_id=message.chat.id, text='Выберите следующее действие', reply_markup=self.keyboard_blank(['Улучшить 🪄', '🔁', 'Новая 🖼', 'В меню'], ['upscale', 'regenerate', 'images', 'exit']), parse_mode='html') # Убрал self из лямбды
        # Message before upscale
        self.BeforeUpscale = lambda message: self.bot.send_message(chat_id=message.chat.id, text='Выберите следующее действие', reply_markup=self.keyboard_blank(['🔁', 'Новая 🖼', 'В меню'], ['regenerate', 'images', 'exit']), parse_mode='html') # Убрал self из лямбды
        # Free mode request
        self.FreeArea = lambda message: self.bot.send_message(chat_id=message.chat.id, text='Введите ваш запрос', reply_markup=self.reply_keyboard(['В меню']), parse_mode='html') # Убрал self из лямбды
        # Tariff request
        self.TariffArea = lambda message: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Тарифы', reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Убрал self из лямбды
        # Tariffs area exit
        self.TariffExit = lambda message: self.bot.send_message(chat_id=message.chat.id, text='Тарифы', reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'В меню'], ['basic', 'pro', 'promo', 'exit'])) # Убрал self из лямбды
        # End tariff
        self.TarrifEnd = lambda message: self.bot.send_message(chat_id=message.chat.id, text='У вас закончились запросы, но вы можете продлить ваш тариф.', reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Убрал self из лямбды
        # Free tariff end
        self.FreeTariffEnd = lambda message: self.bot.send_message(chat_id=message.chat.id, text='Лимит бесплатных запросов, увы, исчерпан😢 Но вы можете выбрать один из наших платных тарифов. Просто нажмите на них и получите подробное описание', reply_markup=self.keyboard_blank(['BASIC', 'PRO', 'Промокод', 'Реферальная программа', 'В меню'], ['basic', 'pro', 'promo', 'ref', 'exit'])) # Убрал self из лямбды
        # Select one or some texts
        self.SomeTexts = lambda message, ind: self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Хотите сделать один текст или сразу несколько?', reply_markup=self.keyboard_blank(['Один', 'Несколько', 'Назад'], [f'one_{ind}', f'some_{ind}', 'text_exit'])) # Убрал self из лямбды

    # Private methods
    async def _send_message_with_delay(self, message: types.Message, text: str, parse_mode: str = 'html', reply_markup: types.InlineKeyboardMarkup = None) -> types.Message:
        """Отправляет сообщение с задержкой и возможностью разметки.

        Args:
            message (types.Message): Объект сообщения Telegram.
            text (str): Текст сообщения.
            parse_mode (str, optional): Режим разметки. Defaults to 'html'.
             reply_markup (types.InlineKeyboardMarkup, optional): Inline клавиатура. Defaults to None

        Returns:
            types.Message: Отправленное сообщение.
        """
        send = self.__delay(message)
        await asyncio.sleep(1) # Задержка перед отправкой сообщения
        if reply_markup:
            await self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=text, parse_mode=parse_mode, reply_markup=reply_markup)
        else:
            await self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=text, parse_mode=parse_mode)
        return send

    async def _gpt_4o_mini(self, prompt: List[Dict[str, str]], message: types.Message) -> Tuple[Dict[str, str], int, int]:
        """
        Выполняет запрос к GPT-4o mini.

        Args:
            prompt (List[Dict[str, str]]): Список словарей с запросами.
            message (types.Message): Объект сообщения Telegram.

        Returns:
            Tuple[Dict[str, str], int, int]: Кортеж, содержащий ответ, количество входящих и исходящих токенов.
        """
        send = await self._send_message_with_delay(message, "Идет обработка запроса...")
        response, incoming_tokens, outgoing_tokens = super()._free_gpt_4o_mini(prompt=prompt)
        await self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=PromptsCompressor.html_tags_insert(response['content']), parse_mode='html')
        return response, incoming_tokens, outgoing_tokens

    async def _flux_schnell(self, prompt: str, size: List[int], message: types.Message, seed: int, num_inference_steps: int) -> None:
        """
        Выполняет запрос к FLUX schnell для генерации изображения.

        Args:
            prompt (str): Текст запроса.
            size (List[int]): Размеры изображения.
            message (types.Message): Объект сообщения Telegram.
            seed (int): Зерно для генерации.
            num_inference_steps (int): Количество шагов для генерации.
        """
        send = await self._send_message_with_delay(message, "Генерируем изображение...")
        photo = None
        for _ in range(3): # Попробуем сделать 3 попытки
            try:
                photo = super()._FLUX_schnell(prompt, size, seed, num_inference_steps)
                break
            except Exception as ex:
                logger.error('Ошибка генерации изображения', ex)
                await asyncio.sleep(1) # Небольшая задержка перед повторной попыткой
        if photo:
            await self.bot.send_photo(chat_id=message.chat.id, photo=photo)
            await self.bot.delete_message(chat_id=send.chat.id, message_id=send.message_id)
        else:
            await self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text="При генерации возникла ошибка, попробуйте повторить позже")


    # Public methods
    def text_types(self, message: types.Message) -> types.Message:
        """
        Отправляет сообщение с типами текста.

        Args:
            message (types.Message): Объект сообщения Telegram.

        Returns:
            types.Message: Сообщение с типами текста.
        """
        names = ['Коммерческий  🛍️', 'SMM 📱', 'Брейншторм 💡', 'Реклама 📺', 'Заголовки 🔍', 'SEO 🌐', 'Новость 📰', 'Редактура 📝', 'В меню']
        data = ['comm-text', 'smm-text', 'brainst-text', 'advertising-text', 'headlines-text', 'seo-text', 'news', 'editing', 'exit']
        return self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='📝 Выберите тип текста', reply_markup=self.keyboard_blank(names, data))

    def basic_tariff(self, message: types.Message) -> None:
        """
        Отправляет счет для оплаты базового тарифа.

        Args:
            message (types.Message): Объект сообщения Telegram.
        """
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Подключить тариф BASIC', pay=True))
        keyboard.add(types.InlineKeyboardButton('К тарифам', callback_data='tariff_exit'))
        price = [types.LabeledPrice(label='BASIC', amount=99 * 100)]
        self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        self.bot.send_invoice(chat_id=message.chat.id, title='BASIC',
                            description='Безлимитная генерация текста, в том числе по готовым промптам.',
                            invoice_payload='basic_invoice_payload',
                            start_parameter='subscription',
                            provider_token=os.environ['PROVIDE_TOKEN'],
                            currency='RUB', prices=price, reply_markup=keyboard)

    def pro_tariff(self, message: types.Message) -> None:
        """
         Отправляет счет для оплаты профессионального тарифа.

        Args:
            message (types.Message): Объект сообщения Telegram.
        """
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Подключить тариф PRO', pay=True))
        keyboard.add(types.InlineKeyboardButton('К тарифам', callback_data='tariff_exit'))
        price = [types.LabeledPrice(label='PRO', amount=199 * 100)]
        self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        self.bot.send_invoice(chat_id=message.chat.id, title='PRO',
                            description='Безлимитная генерация текста (в том числе по готовым промптам) и изображений.',
                            invoice_payload='pro_invoice_payload',
                            start_parameter='subscription',
                            provider_token=os.environ['PROVIDE_TOKEN'],
                            currency='RUB', prices=price, reply_markup=keyboard)

    async def text_commands(self, message: types.Message, ind: int) -> Tuple[int, int, int]:
        """
        Обрабатывает текстовые команды.

        Args:
            message (types.Message): Объект сообщения Telegram.
            ind (int): Индекс команды.

        Returns:
            Tuple[int, int, int]: Кортеж, содержащий количество входящих токенов, исходящих токенов и количество запросов.
        """
        info = []
        incoming_tokens = 0
        outgoing_tokens = 0
        response = None
        if 'TEXT' in pc.commands_size[ind]:
            info.append(message.text)
            msg = await self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text['text_list'][ind][1])

            async def text_next_step(message: types.Message):
                nonlocal info, incoming_tokens, outgoing_tokens, response
                info += message.text.split(';')
                while len(info) < len(pc.commands_size[ind]):
                    info.append('Параметр отсутствует')
                prompt = pc.get_prompt(ind=ind, info=info)
                response, incoming_tokens, outgoing_tokens = await self._gpt_4o_mini(prompt=[{'role': 'user', 'content': prompt}], message=message)
                self.restart(message)

            self.bot.register_next_step_handler(msg, text_next_step)
            while response is None:
                await asyncio.sleep(0.1)
            return incoming_tokens, outgoing_tokens, 1
        else:
            info = message.text.split(';')
            while len(info) < len(pc.commands_size[ind]):
                info.append('Параметр отсутствует')
            prompt = pc.get_prompt(ind=ind, info=info)
            response, incoming_tokens, outgoing_tokens = await self._gpt_4o_mini(prompt=[{'role': 'user', 'content': prompt}], message=message)
            self.restart(message)
            return incoming_tokens, outgoing_tokens, 1


    async def some_texts_command(self, message: types.Message, ind: int, tokens: Dict[str, int]) -> Tuple[int, int, int]:
        """
         Обрабатывает несколько текстовых команд.

        Args:
            message (types.Message): Объект сообщения Telegram.
            ind (int): Индекс команды.
            tokens (Dict[str, int]): Словарь с токенами.

        Returns:
            Tuple[int, int, int]: Кортеж, содержащий количество входящих токенов, исходящих токенов и количество запросов.
        """
        n = int(message.text)
        available = [0, 1, 3, 5, 6]  # Исправил опечатку
        answers = []

        for i in range(n):
            answers.append([])
            if 'TEXT' in pc.commands_size[ind]:
                msg = await self.bot.send_message(chat_id=message.chat.id, text=f'Введите текст источника {i + 1}')
                text = None

                async def text_next_step(message: types.Message):
                    nonlocal text, answers
                    text = message.text
                    answers[i].append(text)

                self.bot.register_next_step_handler(msg, text_next_step)
                while text is None:
                    await asyncio.sleep(0.1)

        index = available.index(ind)
        for el in range(1, len(self.prompts_text['few_texts_list'][index])):
            msg = await self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text['few_texts_list'][index][el])
            params = None

            async def params_addition(message: types.Message):
                nonlocal params, answers
                params = message.text
                params = params.split(';')
                if len(params) < len(pc.commands_size[ind]):
                    while len(params) < len(pc.commands_size[ind]):
                        params.append(None)
                param = params[0]
                for j in range(len(answers)): # Используем for j in range
                    if params[j] is None:
                        answers[j].append(param)
                    else:
                         answers[j].append(params[j])


            self.bot.register_next_step_handler(msg, params_addition)
            while params is None:
                await asyncio.sleep(0.1)

        incoming_tokens = 0
        outgoing_tokens = 0
        async def process_prompt(i: int) -> Tuple[int, int]:
            nonlocal incoming_tokens, outgoing_tokens
            prompt = pc.get_prompt(ind=ind, info=answers[i])
            if tokens['incoming_tokens'] - incoming_tokens > 0 and tokens['outgoing_tokens'] - outgoing_tokens > 0 or tokens['free_requests'] - i > 0:
                response, in_tokens, out_tokens = await self._gpt_4o_mini(prompt=[{'role': 'user', 'content': prompt}], message=message)
                return in_tokens, out_tokens
            return 0, 0

        with concurrent.futures.ThreadPoolExecutor() as executor:
           results = list(executor.map(process_prompt, range(n)))

        for in_tokens, out_tokens in results:
            incoming_tokens += in_tokens
            outgoing_tokens += out_tokens

        self.restart(message)
        return incoming_tokens, outgoing_tokens, n


    async def image_command(self, message: types.Message, prompt: str, size: List[int]) -> int:
        """
        Обрабатывает команды для генерации изображений.

        Args:
            message (types.Message): Объект сообщения Telegram.
            prompt (str): Текст запроса.
            size (List[int]): Размеры изображения.

        Returns:
            int: Зерно для генерации.
        """
        seed = randint(1, 1000000)
        await self._flux_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=4)
        self.ImageChange(message)
        return seed

    async def image_regen_and_upscale(self, message: types.Message, prompt: str, size: List[int], seed: int, num_inference_steps: int = 4) -> None:
        """
        Обрабатывает команды для регенерации и улучшения изображений.

        Args:
            message (types.Message): Объект сообщения Telegram.
            prompt (str): Текст запроса.
            size (List[int]): Размеры изображения.
            seed (int): Зерно для генерации.
            num_inference_steps (int, optional): Количество шагов для генерации. Defaults to 4.
        """
        await self._flux_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=num_inference_steps)

    async def free_command(self, message: types.Message, prompts: List[Dict[str, Any]]) -> Tuple[int, int, List[Dict[str, Any]]]:
        """
        Обрабатывает команды свободного режима.

        Args:
            message (types.Message): Объект сообщения Telegram.
            prompts (List[Dict[str, Any]]): Список предыдущих запросов и ответов.

        Returns:
            Tuple[int, int, List[Dict[str, Any]]]: Кортеж, содержащий количество входящих токенов, исходящих токенов и обновленный список запросов и ответов.
        """
        try:
            if not isinstance(prompts[-1].get('content', False), list):
                prompts.append({'content': message.text, 'role': 'user'})
        except (IndexError, TypeError):
            pass
        response, incoming_tokens, outgoing_tokens = await self._gpt_4o_mini(prompt=prompts, message=message)
        prompts.append(response)
        return incoming_tokens, outgoing_tokens, prompts