# Анализ кода модуля `bot.py`

**Качество кода**
8
- Плюсы
    - Код использует асинхронность для обработки сообщений в Telegram, что обеспечивает хорошую производительность.
    - Присутствует разделение на классы, что способствует лучшей организации кода.
    - Используются dataclasses для определения структуры данных бота.
    - Применяется `recursively_read_text_files` для загрузки данных, что удобно.
    -  Логика обработки различных типов сообщений (текст, голос, документы) разделена.
- Минусы
    -  Отсутствует подробная документация в формате reStructuredText для всех функций и классов.
    -  Не везде используется `logger.error` для обработки исключений, вместо этого иногда используется `print` или `logger.debug` для ошибок.
    -  Есть дублирование кода в `handle_suppliers_response` и `handle_onetab_response`.
    -  Использование `...` в коде как точки остановки.
    -  Не все переменные имеют аннотацию типов.
    -  Не всегда используются f-строки для форматирования строк.

**Рекомендации по улучшению**

1. **Документация**: Добавить reStructuredText (RST) docstrings для всех классов, методов и функций.
2. **Логирование**: Заменить `print` на `logger.error` для обработки исключений. Использовать более информативные сообщения в логах.
3. **Рефакторинг**: Вынести общую логику `handle_suppliers_response` и `handle_onetab_response` в отдельную функцию.
4. **Импорты**: Добавить все необходимые импорты, которые могут отсутствовать.
5. **Удалить `...`**: Убрать все `...` из кода.
6. **Типизация**: Добавить аннотации типов для всех переменных.
7.  **Форматирование строк**: Использовать f-строки для форматирования строк, где это возможно.
8. **Константы**: Вынести повторяющиеся строки и значения в константы.
9. **Переменные**: Добавить аннотации типов для переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для реализации Telegram-бота психолога.
==================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`,
который наследуется от :class:`TelegramBot` и реализует
специфическое поведение бота-психолога.

"""
import asyncio
from pathlib import Path
from typing import Optional, List, Tuple, Callable, Dict, Any
from dataclasses import dataclass, field
import random

from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

from src import gs
from src.bots.telegram import TelegramBot
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import read_text_file, recursively_read_text_files, save_text_file
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.url import is_url

MODE: str = 'dev' # Режим работы бота ('dev' или 'test')
SUPPLIERS_URLS: Tuple[str, ...] = (
    'https://morlevi.co.il', 'https://www.morlevi.co.il',
    'https://grandadvance.co.il', 'https://www.grandadvance.co.il',
    'https://ksp.co.il', 'https://www.ksp.co.il',
    'https://ivory.co.il', 'https://www.ivory.co.il'
)
ONETAB_URLS: Tuple[str, ...] = ('https://www.one-tab.com',)
GREETING_MESSAGE: str = 'Hi! I am a smart assistant psychologist.'
ERROR_READING_QUESTIONS: str = 'Произошла ошибка при чтении вопросов.'
READY_MESSAGE: str = 'Готово!'
TRY_AGAIN_MESSAGE: str = 'Хуёвенько. Попробуй еще раз'
WHATSAPP_MESSAGE: str = 'Готово!\\nСсылку я вышлю на WhatsApp'

@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Класс, реализующий Telegram-бота психолога.

    Наследуется от :class:`TelegramBot` и добавляет
    специфическую функциональность для обработки сообщений
    и взаимодействия с пользователем.

    :ivar token: Токен для доступа к Telegram API.
    :vartype token: str
    :ivar d: Драйвер веб-браузера.
    :vartype d: Driver
    :ivar model: Модель Google Gemini для генерации ответов.
    :vartype model: GoogleGenerativeAI
    :ivar system_instruction: Инструкция для модели Gemini.
    :vartype system_instruction: str
    :ivar questions_list: Список вопросов для бота.
    :vartype questions_list: list
    :ivar timestamp: Временная метка создания экземпляра бота.
    :vartype timestamp: str
    """
    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: List[str] = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self) -> None:
        """
        Инициализирует бота, настраивает токен, драйвер, модель ИИ и загружает необходимые данные.
        """
        mode: str = 'test'
        #self.token = gs.credentials.telegram.hypo69_test_bot if mode == 'test' else gs.credentials.telegram.hypo69_psychologist_bot
        #  Получение токена для телеграм бота из настроек
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)
        #  Инициализация драйвера для работы с браузером
        self.d = Driver(Chrome)
        #  Чтение системной инструкции для модели ИИ из файла
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        #  Чтение списка вопросов из файлов
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )
        #  Инициализация модели Google Gemini
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        #  Регистрация обработчиков
        self.register_handlers()

    def register_handlers(self) -> None:
        """
        Регистрирует обработчики команд и сообщений для бота.
        """
        #  Регистрация обработчика команды start
        self.application.add_handler(CommandHandler('start', self.start))
        #  Регистрация обработчика команды help
        self.application.add_handler(CommandHandler('help', self.help_command))
        #  Регистрация обработчика текстовых сообщений
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        #  Регистрация обработчика голосовых сообщений
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        #  Регистрация обработчика документов
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
         Обрабатывает команду /start, отправляет приветственное сообщение.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Объект CallbackContext от Telegram.
        :type context: telegram.ext.CallbackContext
        """
        #  Отправка приветственного сообщения
        await update.message.reply_text(GREETING_MESSAGE)
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает текстовые сообщения, включая URL-адреса.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Объект CallbackContext от Telegram.
        :type context: telegram.ext.CallbackContext
        """
        #  Получение текста сообщения от пользователя
        response: str = update.message.text
        user_id: int = update.effective_user.id
        #  Формирование пути к файлу логов
        log_path: Path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        #  Сохранение сообщения пользователя в лог
        save_text_file(f"User {user_id}: {response}\n", Path(log_path))
        #  Получение ответа от модели ИИ
        answer: str = self.model.ask(q=response, history_file=f'{user_id}.txt')
        #  Отправка ответа пользователю
        return await update.message.reply_text(answer)

    def get_handler_for_url(self, response: str) -> Optional[Callable]:
        """
        Определяет обработчик для URL-адреса, если такой существует.

        :param response: URL-адрес для проверки.
        :type response: str
        :return: Функция-обработчик или None, если не найдено.
        :rtype: Optional[Callable]
        """
        url_handlers: Dict[str, Tuple[Tuple[str, ...], Callable]] = {
            "suppliers": (SUPPLIERS_URLS, self.handle_suppliers_response),
            "onetab": (ONETAB_URLS, self.handle_onetab_response),
        }
        #  Проверка наличия обработчика для URL
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                return handler_func
        return None

    async def _run_mexiron_scenario(self, update: Update, response: str, price: Optional[float] = None, mexiron_name: Optional[str] = None, urls: Optional[List[str]] = None) -> None:
        """
        Выполняет сценарий Mexiron и отправляет ответ пользователю.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param response: Текст сообщения от пользователя.
        :type response: str
        :param price: Цена товара.
        :type price: Optional[float]
        :param mexiron_name: Название сценария Mexiron.
        :type mexiron_name: Optional[str]
        :param urls: Список URL-адресов.
        :type urls: Optional[List[str]]
        """
        try:
            if await self.mexiron.run_scenario(response, update, price=price, mexiron_name=mexiron_name, urls=urls):
               await update.message.reply_text(READY_MESSAGE)
            else:
                await update.message.reply_text(TRY_AGAIN_MESSAGE)
        except Exception as ex:
            logger.error(f'Ошибка выполнения сценария Mexiron: {ex}', exc_info=True)
            await update.message.reply_text(TRY_AGAIN_MESSAGE)

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает ответы, содержащие URL-адреса поставщиков.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param response: URL-адрес от пользователя.
        :type response: str
        """
        await self._run_mexiron_scenario(update, response)

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает ответы, содержащие URL-адреса OneTab.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param response: URL-адрес от пользователя.
        :type response: str
        """
        await self._run_mexiron_scenario(update, response, mexiron_name='onetab', urls=[response])
        await update.message.reply_text(WHATSAPP_MESSAGE)

    async def handle_next_command(self, update: Update) -> None:
        """
        Обрабатывает команду '--next', выбирая случайный вопрос и отправляя его с ответом.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        """
        try:
            question: str = random.choice(self.questions_list)
            answer: str = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.error(f"Ошибка чтения вопросов: {ex}", exc_info=True)
            await update.message.reply_text(ERROR_READING_QUESTIONS)

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает загруженные документы, отправляет содержимое пользователю.

        :param update: Объект Update от Telegram.
        :type update: telegram.Update
        :param context: Объект CallbackContext от Telegram.
        :type context: telegram.ext.CallbackContext
        """
        #  Получение содержимого файла
        file_content: str = await super().handle_document(update, context)
        #  Отправка содержимого файла пользователю
        await update.message.reply_text(f'Received your document. Content: {file_content}')


if __name__ == "__main__":
    #  Создание экземпляра бота
    kt = PsychologistTelgrambot()
    #  Запуск бота
    asyncio.run(kt.application.run_polling())
```