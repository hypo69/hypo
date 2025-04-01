## Анализ кода модуля `minibot.py`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Четкая структура кода, разделение на классы и функции.
    - Использование логирования для отслеживания действий пользователей и ошибок.
    - Обработка различных типов сообщений (текст, голосовые, документы).
    - Использование `dotenv` для управления конфигурацией.
- **Минусы**:
    - Не хватает подробной документации для всех функций и классов.
    - Некоторые участки кода могут быть улучшены с точки зрения читаемости и эффективности.
    - Жестко заданные пути к файлам (например, `user_flowchart.png`).
    - Не все переменные аннотированы типами.

**Рекомендации по улучшению:**

1. **Добавить документацию**:
   - Добавить docstrings к классам `BotHandler` и `Config`, а также ко всем методам в классе `BotHandler`. Описать назначение каждого метода, аргументы и возвращаемые значения.
   - Описать модуль в целом.
2. **Улучшить обработку ошибок**:
   - В блоках `try...except` добавить более конкретную обработку исключений, чтобы понимать, какие именно ошибки происходят.
   - Логировать ошибки с уровнем `error` и передавать `exc_info=True` для получения полной трассировки.
3. **Пересмотреть структуру проекта**:
   - Вынести конфигурацию в отдельный файл или класс, чтобы отделить параметры бота от основной логики.
   - Использовать `j_loads` для загрузки конфигурации из JSON-файла.
4. **Улучшить читаемость кода**:
   - Добавить пробелы вокруг операторов присваивания и других операторов.
   - Использовать более понятные имена переменных.
5. **Аннотировать типы**:
   - Добавить аннотации типов для всех переменных и параметров функций, где это возможно.
6. **Избавиться от дублирования кода**:
   - Создать вспомогательную функцию для отправки сообщений, чтобы избежать повторения `bot.send_message(message.chat.id, ...)`.
7. **Безопасность**:
   - Хранить секретные ключи и токены в безопасном месте, например, в переменных окружения, и не помещать их непосредственно в код.
8. **Конфигурация путей**:
    - Использовать переменные окружения или конфигурационные файлы для хранения путей к файлам, чтобы упростить развертывание и настройку.
    - Использовать `Path` для работы с путями.
9. **Удалить неиспользуемые импорты**:
   - Удалить неиспользуемые импорты, такие как `header`.
   
**Оптимизированный код:**

```python
## \file /src/endpoints/emil/minibot.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для реализации Telegram-бота для emil-design.com.
=========================================================

Этот модуль содержит классы и функции для обработки сообщений,
полученных от Telegram-бота, включая текстовые команды, URL,
голосовые сообщения и документы. Он также включает интеграцию
с Google Gemini для обработки текста и сценарии для выполнения
определенных задач.

Пример использования:
--------------------

Чтобы запустить бота, убедитесь, что у вас установлены все необходимые
зависимости и правильно настроены переменные окружения. Затем запустите
скрипт `bot.py`.
"""

import telebot
import os
import datetime
import random
from pathlib import Path
import asyncio

from dotenv import load_dotenv
load_dotenv()

from src.logger import logger
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.scenarios.scenario import fetch_target_urls_onetab, Scenario
from src.utils.url import is_url

##############################################################

ENDPOINT: str = 'emil'
USE_ENV: bool = True  # <- Определает откуда брать ключи. Если False - то из базы данных с паролями, иначе из .env

#############################################################

class BotHandler:
    """
    Обработчик команд, получаемых от Telegram-бота.

    Attributes:
        scenario (Scenario): Экземпляр класса Scenario для выполнения сценариев.
        model (GoogleGenerativeAI): Экземпляр класса GoogleGenerativeAI для взаимодействия с моделью Gemini.
        questions_list (list[str]): Список вопросов для обработки команды \'--next\'.
        base_dir (Path): Базовый путь к директории, где хранятся ресурсы.
    """

    base_dir: Path = gs.path.project_root / 'src' / 'endpoints' / 'kazarinov'

    def __init__(self) -> None:
        """
        Инициализация обработчика событий телеграм-бота.
        """
        self.scenario: Scenario = Scenario()
        self.model: GoogleGenerativeAI = GoogleGenerativeAI(os.getenv('GEMINI_API'))
        self.questions_list: list[str] = ['Я не понял?', 'Объясни пожалуйста']


    def handle_message(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> None:
        """
        Обрабатывает текстовые сообщения, поступающие от пользователя.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
        """
        text: str = message.text
        if text == '?':
            self._send_user_flowchart(bot, message.chat.id)
        elif is_url(text):
            self._handle_url(bot, message)
        elif text in ('--next', '-next', '__next', '-n', '-q'):
            self._handle_next_command(bot, message)
        else:
            try:
                answer: str = self.model.chat(text)
                bot.send_message(message.chat.id, answer)
            except Exception as ex:
                logger.error(f'Error during model interaction: {ex}', exc_info=True)
                bot.send_message(message.chat.id, 'Произошла ошибка при обработке сообщения.')


    def _send_user_flowchart(self, bot: telebot.TeleBot, chat_id: int) -> None:
        """
        Отправляет пользователю схему user_flowchart.png.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            chat_id (int): ID чата пользователя.
        """
        photo_path: Path = self.base_dir / 'assets' / 'user_flowchart.png'
        try:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)
        except FileNotFoundError:
            logger.error(f'File not found: {photo_path}', exc_info=True)
            bot.send_message(chat_id, 'Схема не найдена.')


    def _handle_url(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> None:
        """
        Обрабатывает URL, присланный пользователем.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
        """
        url: str = message.text
        if not url.startswith(('https://one-tab.com', 'https://www.one-tab.com')):
            bot.send_message(message.chat.id, 'Мне на вход нужен URL `https://one-tab.com` Проверь, что ты мне посылаешь')
            return

        # Parsing https//one-tab.com/XXXXXXXXX page
        try:
            price: float | int
            mexiron_name: str
            urls: list[str] = fetch_target_urls_onetab(url)
            bot.send_message(message.chat.id, f'Получил мехирон {mexiron_name} - {price} шек')
        except Exception as ex:
            logger.error(f'Error fetching URLs from OneTab: {ex}', exc_info=True)
            bot.send_message(message.chat.id, 'Произошла ошибка при получении данных из OneTab.')
            return

        if not urls:
            bot.send_message(message.chat.id, 'Некорректные данные. Не получил список URL комплектующих')
            return

        try:
            asyncio.run(
                self.scenario.run_scenario(
                    bot=bot,
                    chat_id=message.chat.id,
                    urls=list(urls),
                    price=price,
                    mexiron_name=mexiron_name
                ))

        except Exception as ex:
            logger.error(f'Error during scenario execution: {ex}', exc_info=True)
            bot.send_message(message.chat.id, f'Произошла ошибка при выполнении сценария. {ex.args}')


    def _handle_next_command(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> None:
        """
        Обрабатывает команду '--next' и ее аналоги.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
        """
        try:
            question: str = random.choice(self.questions_list)
            answer: str = self.model.ask(question)
            bot.send_message(message.chat.id, question)
            bot.send_message(message.chat.id, answer)
        except Exception as ex:
            logger.error(f'Ошибка чтения вопросов: {ex}', exc_info=True)
            bot.send_message(message.chat.id, 'Произошла ошибка при чтении вопросов.')


    def help_command(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> None:
        """
        Обрабатывает команду /help, отправляя список доступных команд.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
        """
        bot.send_message(
            message.chat.id,
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )


    def send_pdf(self, bot: telebot.TeleBot, message: 'telebot.types.Message', pdf_file: str) -> None:
        """
        Отправляет PDF-файл пользователю.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
            pdf_file (str): Путь к PDF-файлу.
        """
        try:
            with open(pdf_file, 'rb') as pdf_file_obj:
                bot.send_document(message.chat.id, document=pdf_file_obj)
        except Exception as ex:
            logger.error(f'Ошибка при отправке PDF-файла: {ex}', exc_info=True)
            bot.send_message(message.chat.id, 'Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')


    def handle_voice(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> None:
        """
        Обрабатывает голосовые сообщения, полученные от пользователя.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.
        """
        try:
            file_info: telebot.types.File = bot.get_file(message.voice.file_id)
            file: bytes = bot.download_file(file_info.file_path)
            file_path: Path = gs.path.temp / f'{message.voice.file_id}.ogg'
            with open(file_path, 'wb') as f:
                f.write(file)
            transcribed_text: str = self._transcribe_voice(file_path)
            bot.send_message(message.chat.id, f'Распознанный текст: {transcribed_text}')
        except Exception as ex:
            logger.error(f'Ошибка при обработке голосового сообщения: {ex}', exc_info=True)
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')


    def _transcribe_voice(self, file_path: str | Path) -> str:
        """
        Транскрибирует голосовое сообщение (заглушка).

        Args:
            file_path (str | Path): Путь к файлу голосового сообщения.

        Returns:
            str: Заглушка с сообщением о нереализованной функции.
        """
        return 'Распознавание голоса ещё не реализовано.'


    def handle_document(self, bot: telebot.TeleBot, message: 'telebot.types.Message') -> bool:
        """
        Обрабатывает документы, полученные от пользователя.

        Args:
            bot (telebot.TeleBot): Экземпляр Telegram-бота.
            message (telebot.types.Message): Объект сообщения от пользователя.

        Returns:
            bool: True, если документ успешно обработан, иначе False.
        """
        try:
            file_info: telebot.types.File = bot.get_file(message.document.file_id)
            file: bytes = bot.download_file(file_info.file_path)
            tmp_file_path: Path = gs.path.temp / message.document.file_name
            with open(tmp_file_path, 'wb') as f:
                f.write(file)
            bot.send_message(message.chat.id, f'Файл сохранен в {tmp_file_path}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при обработке документа: {ex}', exc_info=True)
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке документа. Попробуй ещё раз.')
            return False

# --- config.py -----------------
class Config:
    """
    Конфигурация бота.

    Attributes:
        BOT_TOKEN (str): Токен Telegram-бота.
        CHANNEL_ID (str): ID канала Telegram.
        PHOTO_DIR (Path): Путь к директории с фотографиями.
        COMMAND_INFO (str): Информация о боте.
        UNKNOWN_COMMAND_MESSAGE (str): Сообщение для неизвестной команды.
        START_MESSAGE (str): Сообщение при старте бота.
        HELP_MESSAGE (str): Сообщение со списком доступных команд.
    """
    BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN') if USE_ENV else gs.credentials.telegram.hypo69_emil_design_bot
    CHANNEL_ID: str = '@onela'
    PHOTO_DIR: Path = gs.path.project_root / 'endpoints' / 'kazarinov' / 'assets'
    COMMAND_INFO: str = 'This is a simple bot. Use /help to see commands.'
    UNKNOWN_COMMAND_MESSAGE: str = 'Unknown command. Use /help to see available commands.'
    START_MESSAGE: str = "Howdy, how are you doing?"
    HELP_MESSAGE: str = """
    Here are the available commands:
    /start - Starts the bot.
    /help - Shows this help message.
    /info - Shows information about the bot.
    /time - Shows the current time.
    /photo - Sends a random photo.
    """
# --- config.py end -----------------

# --- bot.py ---
config: Config = Config()
handler: BotHandler = BotHandler()
bot: telebot.TeleBot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает команду /start, отправляя стартовое сообщение.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)

@bot.message_handler(commands=['help'])
def command_help(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает команду /help, вызывая метод help_command обработчика.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)

@bot.message_handler(commands=['info'])
def command_info(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает команду /info, отправляя информацию о боте.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)

@bot.message_handler(commands=['time'])
def command_time(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает команду /time, отправляя текущее время.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send /time command")
    now: datetime.datetime = datetime.datetime.now()
    current_time: str = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")

@bot.message_handler(commands=['photo'])
def command_photo(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает команду /photo, отправляя случайное фото из директории.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send /photo command")
    try:
        photo_files: list[str] = os.listdir(config.PHOTO_DIR)
        if photo_files:
            random_photo: str = random.choice(photo_files)
            photo_path: str = os.path.join(config.PHOTO_DIR, random_photo)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "No photos in the folder.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Photo directory not found.")

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает голосовые сообщения, вызывая метод handle_voice обработчика.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document_message(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает сообщения с документами, вызывая метод handle_document обработчика.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)

@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает текстовые сообщения, не начинающиеся с '/', вызывая метод handle_message обработчика.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message)

@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message: 'telebot.types.Message') -> None:
    """
    Обрабатывает неизвестные команды, отправляя сообщение об этом пользователю.

    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.
    """
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)

bot.polling(none_stop=True)
# --- bot.py end ---