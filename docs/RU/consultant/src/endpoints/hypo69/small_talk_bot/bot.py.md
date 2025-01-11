# Анализ кода модуля `bot.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код хорошо структурирован, используется класс `PsychologistTelgrambot` для управления ботом.
    *   Применяется асинхронность для обработки сообщений и команд, что обеспечивает отзывчивость бота.
    *   Используется `dataclass` для удобного создания экземпляров класса.
    *   Присутствует разделение на хендлеры для разных типов сообщений и команд.
    *   Реализовано логирование сообщений пользователя.
    *   Используется `GoogleGenerativeAI` для обработки текстовых запросов.
    *   Есть обработка загрузки документов.
*   **Минусы:**
    *   Не все функции и методы документированы в формате reStructuredText (RST).
    *   Некоторые переменные и методы требуют более описательных названий (например, `d`, `kt`).
    *   Использование `try-except` с `logger.debug` для обработки ошибок чтения вопросов не является оптимальным. Лучше использовать `logger.error` для ошибок.
    *   Присутствует дублирование кода в `handle_suppliers_response` и `handle_onetab_response` (похожие блоки try-except).
    *   Не хватает обработки ошибок при сохранении логов.
    *   Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    *   Не все импорты используются (например, `header`, `Path`).
    *   Не все константы вынесены в начало модуля (например, `mode`).

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Добавить docstring в формате RST для всех функций, методов и класса, используя Sphinx-совместимый синтаксис.
2.  **Именование:**
    *   Переименовать переменные `d` на `driver`, `kt` на `bot` для лучшей читаемости.
3.  **Обработка ошибок:**
    *   Использовать `logger.error` вместо `logger.debug` для критических ошибок, например, при чтении вопросов.
    *   Добавить обработку ошибок при сохранении логов.
4.  **Рефакторинг:**
    *   Вынести повторяющийся код в `handle_suppliers_response` и `handle_onetab_response` в отдельную функцию или метод.
5.  **Импорты:**
    *   Удалить неиспользуемые импорты.
6.  **Чтение файлов:**
    *   Использовать `j_loads` или `j_loads_ns` для чтения файлов.
7.  **Константы:**
    *   Вынести константу `mode = 'test'` в начало модуля.
8.  **Комментарии:**
    *   Добавить комментарии к важным блокам кода, используя формат RST.

**Оптимизированный код:**

```python
"""
Модуль для создания и управления Telegram-ботом психологом.
=========================================================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`, который представляет собой Telegram-бота,
предназначенного для предоставления психологической помощи. Бот использует Google Gemini для
генерации ответов на запросы пользователей, а также поддерживает обработку URL, документов и голоса.

Пример использования
--------------------

Пример создания и запуска бота:

.. code-block:: python

    bot = PsychologistTelgrambot()
    asyncio.run(bot.application.run_polling())
"""
import asyncio
import random
from pathlib import Path
from typing import Any, Optional
from dataclasses import dataclass, field
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

from src import gs
from src.bots.telegram import TelegramBot
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import read_text_file, recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

MODE = 'test' # Режим работы бота: test или prod

@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Представляет Telegram-бота с пользовательским поведением для психолога.

    :ivar token: Токен для доступа к Telegram API.
    :vartype token: str
    :ivar driver: Экземпляр веб-драйвера для выполнения действий в браузере.
    :vartype driver: Driver
    :ivar model: Экземпляр модели Google Generative AI для генерации ответов.
    :vartype model: GoogleGenerativeAI
    :ivar system_instruction: Системная инструкция для модели.
    :vartype system_instruction: str
    :ivar questions_list: Список вопросов для бота.
    :vartype questions_list: list
    :ivar timestamp: Временная метка создания экземпляра бота.
    :vartype timestamp: str
    """
    token: str = field(init=False)
    driver: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        """Инициализирует бота, загружает настройки и регистрирует обработчики."""
        # mode = 'test' # Режим работы бота: test или prod
        # self.token = gs.credentials.telegram.hypo69_test_bot if mode == 'test' else gs.credentials.telegram.hypo69_psychologist_bot
        # # Код устанавливает токен бота из конфигурации
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        # Код инициализирует веб-драйвер Chrome
        self.driver = Driver(Chrome)

        # Код считывает системную инструкцию из файла
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        # Код считывает список вопросов из файлов
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        # Код инициализирует модель Google Gemini
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        
        # Код регистрирует обработчики
        self.register_handlers()

    def register_handlers(self):
        """Регистрирует обработчики команд и сообщений."""
        # Код добавляет обработчики для команд и сообщений
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает команду /start.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Контекст вызова обработчика.
        :type context: telegram.ext.CallbackContext
        """
        # Код отправляет приветственное сообщение
        await update.message.reply_text('Hi! I am a smart assistant psychologist.')
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает текстовые сообщения, включая URL-маршрутизацию.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Контекст вызова обработчика.
        :type context: telegram.ext.CallbackContext
        """
        # Код извлекает текст сообщения и ID пользователя
        response = update.message.text
        user_id = update.effective_user.id

        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        # Код сохраняет сообщение пользователя в лог-файл
        try:
            save_text_file(f"User {user_id}: {response}\n", log_path)
        except Exception as ex:
            logger.error(f'Ошибка сохранения лога для пользователя {user_id}', exc_info=ex)
            await update.message.reply_text('Произошла ошибка при сохранении лога.')
            return

        # Код отправляет запрос в модель и возвращает ответ
        answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
        await update.message.reply_text(answer)

    def get_handler_for_url(self, response: str):
        """
        Определяет обработчик для URL.

        :param response: Текст сообщения пользователя.
        :type response: str
        :return: Функция-обработчик или None.
        :rtype: Callable | None
        """
        # Код сопоставляет URL с обработчиками
        url_handlers = {
            "suppliers": (
                (
                    'https://morlevi.co.il',
                    'https://www.morlevi.co.il',
                    'https://grandadvance.co.il',
                    'https://www.grandadvance.co.il',
                    'https://ksp.co.il',
                    'https://www.ksp.co.il',
                    'https://ivory.co.il',
                    'https://www.ivory.co.il'
                ),
                self.handle_suppliers_response
            ),
            "onetab": (('https://www.one-tab.com',), self.handle_onetab_response),
        }
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                return handler_func
        return None

    async def _run_scenario(self, update: Update, scenario_func, *args, **kwargs):
        """
         Выполняет сценарий и обрабатывает ответ.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param scenario_func: Функция сценария для выполнения
        :type scenario_func: Callable
        :param args: Позиционные аргументы для функции сценария
        :type args: tuple
        :param kwargs: Ключевые аргументы для функции сценария
        :type kwargs: dict
        """
        try:
            # Код исполняет сценарий и обрабатывает результат
            if await scenario_func(*args, **kwargs):
                await update.message.reply_text('Готово!')
            else:
                await update.message.reply_text('Хуёвенько. Попробуй еще раз')
        except Exception as ex:
            logger.error('Ошибка выполнения сценария', exc_info=ex)
            await update.message.reply_text('Произошла ошибка при выполнении сценария.')


    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса поставщиков.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param response: Текст сообщения пользователя.
        :type response: str
        """
        # Код вызывает метод выполнения сценария для поставщиков
        await self._run_scenario(update, self.mexiron.run_scenario, response, update)

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса OneTab.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param response: Текст сообщения пользователя.
        :type response: str
        """
        #TODO:  добавить цены и имя мексирона в метод и в аргументы. А пока возьму заглушки.
        price = 100
        mexiron_name = 'test_mexiron'
        urls = [response]
        # Код вызывает метод выполнения сценария для OneTab
        await self._run_scenario(update, self.mexiron.run_scenario, price=price, mexiron_name=mexiron_name, urls=urls)
        # await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls)
        #     await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
        # else:
        #     await update.message.reply_text('Хуёвенько. Попробуй ещё раз')

    async def handle_next_command(self, update: Update) -> None:
        """
        Обрабатывает команды '--next' и связанные с ними.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        """
        try:
            # Код выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
            # Код получает ответ от модели
            answer = self.model.ask(question)
            # Код отправляет вопрос и ответ
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.error("Ошибка чтения вопросов", exc_info=ex)
            # Код отправляет сообщение об ошибке
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает загрузку документов.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Контекст вызова обработчика.
        :type context: telegram.ext.CallbackContext
        """
        # Код вызывает метод обработки документа от родительского класса
        file_content = await super().handle_document(update, context)
        # Код отправляет подтверждение о получении документа
        await update.message.reply_text(f'Received your document. Content: {file_content}')

if __name__ == "__main__":
    # Код создает и запускает бота
    bot = PsychologistTelgrambot()
    asyncio.run(bot.application.run_polling())
```