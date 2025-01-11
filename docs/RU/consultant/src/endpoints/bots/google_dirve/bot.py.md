# Анализ кода модуля `bot.py`

**Качество кода**
6
-  Плюсы
    -   Используется асинхронность для обработки запросов, что повышает производительность.
    -   Разделение кода на функции делает его более читаемым и структурированным.
    -   Присутствует обработка различных типов ссылок (Dropbox, Mega, обычные URL).
    -   Есть механизм аутентификации через Google Drive API.
-  Минусы
    -   Многократное использование `print` для логирования, что затрудняет отладку и анализ.
    -   Используется `Exception` без конкретизации, что затрудняет понимание причин ошибок.
    -   Отсутствует подробная документация кода.
    -   Использование `os.remove(filename[-1])` выглядит как потенциальная ошибка, так как filename может быть строкой, а не списком.
    -   Дублирование кода (например, обработка `os.remove` в нескольких блоках `try-except`).
    -   Смешение логики загрузки и обработки файлов.
    -   Не стандартизированные имена переменных (FILENAME, SIZE, ID, FILELINK)

**Рекомендации по улучшению**
1.  Заменить все `print` на `logger` для более эффективного логирования.
2.  Уточнить типы исключений в блоках `try-except` для более точной обработки ошибок.
3.  Добавить документацию в формате RST для всех функций и классов.
4.  Исправить потенциальную ошибку `os.remove(filename[-1])`, убедившись, что `filename` всегда список.
5.  Устранить дублирование кода.
6.  Разделить логику загрузки и обработки файлов.
7.  Стандартизировать имена переменных согласно PEP 8 (например, `file_name`, `file_size`, `user_id`, `file_link`).
8.  Убрать лишние импорты.
9.  Использовать `j_loads_ns` для работы с JSON.
10. Добавить обработку ошибок при загрузке и сохранении токена.
11. Избегать избыточного использования `try-except`.
12. Добавить комментарии к коду для лучшего понимания его работы.
13. Добавить проверки на валидность URL.

**Оптимизированный код**
```python
#!/usr/bin/env python3
"""
Модуль для телеграм бота, работающего с Google Drive.
=========================================================================================

Этот модуль реализует телеграм-бота, который позволяет пользователям загружать файлы по URL на Google Drive.
Он поддерживает загрузку с различных источников, таких как прямые ссылки, Dropbox и Mega.
Бот также предоставляет команды для аутентификации в Google Drive, отзыва токена и получения справки.

Пример использования
--------------------

Пример запуска бота:

.. code-block:: python

    # Запуск бота с использованием токена из переменной окружения или файла creds.py
    # export TG_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    # python bot.py
"""
import os
import sys
import re
from time import time
import subprocess
from pathlib import Path
# Импорты telegram
from telegram import ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram.ext.dispatcher import run_async
# Импорты google
from pydrive.auth import GoogleAuth
# Импорты для загрузки
from pySmartDL import SmartDL
# Импорты для работы с файлами и JSON
from src.utils.jjson import j_loads_ns
# Импорты из проекта
from src.logger.logger import logger
from hypotez.src.endpoints.bots.google_dirve.upload import upload
from hypotez.src.endpoints.bots.google_dirve.creds import Creds
from hypotez.src.endpoints.bots.google_dirve.plugins import TEXT
from hypotez.src.endpoints.bots.google_dirve.plugins.tok_rec import is_token
from hypotez.src.endpoints.bots.google_dirve.plugins.dpbox import DPBOX
from hypotez.src.endpoints.bots.google_dirve.plugins.wdl import wget_dl
from hypotez.src.endpoints.bots.google_dirve.mega import Mega


gauth = GoogleAuth()

######################################################################################
# Инициализация бота
bot_token = Creds.TG_TOKEN
updater = Updater(token=bot_token,  workers=8, use_context=True)
dp = updater.dispatcher
######################################################################################


@run_async
def help_command(update, context):
    """
    Отправляет пользователю справочное сообщение.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    try:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=TEXT.HELP, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(f'Ошибка при отправке справки: {e}')


@run_async
def auth_command(update, context):
    """
    Выполняет аутентификацию пользователя в Google Drive.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    user_id = str(update.message.from_user.id)
    try:
        gauth.LoadCredentialsFile(user_id)
    except Exception as e:
        logger.error(f"Файл с учетными данными отсутствует: {e}")

    if gauth.credentials is None:
        auth_url = gauth.GetAuthUrl()
        auth_message = TEXT.AUTH_URL.format(auth_url)
        context.bot.send_message(
            chat_id=update.message.chat_id, text=auth_message, parse_mode=ParseMode.HTML)
    elif gauth.access_token_expired:
        gauth.Refresh()  # Обновление токена
    else:
        gauth.Authorize()  # Авторизация с сохраненными данными
        context.bot.send_message(
            chat_id=update.message.chat_id, text=TEXT.ALREADY_AUTH)


@run_async
def token_command(update, context):
    """
    Обрабатывает токен, отправленный пользователем, для завершения аутентификации.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    message = update.message.text
    user_id = str(update.message.from_user.id)

    if is_token(message):
        token = message.split()[-1]
        try:
            gauth.Auth(token)
            gauth.SaveCredentialsFile(user_id)
            context.bot.send_message(
                chat_id=update.message.chat_id, text=TEXT.AUTH_SUCC)
        except Exception as e:
            logger.error(f"Ошибка аутентификации: {e}")
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text=TEXT.AUTH_ERROR)


@run_async
def start_command(update, context):
    """
    Отправляет приветственное сообщение пользователю.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    first_name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=TEXT.START.format(first_name), parse_mode=ParseMode.HTML)


@run_async
def revoke_token_command(update, context):
    """
    Отзывает токен пользователя, удаляя файл с учетными данными.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    user_id = str(update.message.chat_id)
    try:
        os.remove(user_id)
        context.bot.send_message(
            chat_id=update.message.chat_id, text=TEXT.REVOKE_TOK)
    except Exception as e:
        logger.error(f"Ошибка при отзыве токена: {e}")
        context.bot.send_message(
            chat_id=update.message.chat_id, text=TEXT.REVOKE_FAIL)


@run_async
def upload_command(update, context):
    """
    Обрабатывает URL, отправленный пользователем, загружает файл и отправляет ссылку на Google Drive.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    url = update.message.text
    url = url.split()[-1]
    sent_message = context.bot.send_message(
        chat_id=update.message.chat_id, text=TEXT.PROCESSING)

    user_id = str(update.message.chat_id)
    
    if not os.path.isfile(user_id):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=TEXT.NOT_AUTH)
        return
    
    download_status = False
    file_name = None

    if "openload" in url or "oload" in url:
        sent_message.edit_text("Openload больше не доступен")
        return
    
    elif 'dropbox.com' in url:
            
        url = DPBOX(url)
        file_name = url.split("/")[-1]
        logger.info(f"Начало загрузки Dropbox: {file_name}")
        sent_message.edit_text(TEXT.DP_DOWNLOAD)
        file_name = wget_dl(str(url))
        logger.info(f"Загрузка Dropbox завершена: {file_name}")
        sent_message.edit_text(TEXT.DOWN_COMPLETE)
        download_status = True

    elif 'mega.nz' in url:
        try:
            logger.info("Начало загрузки Mega")
            sent_message.edit_text(TEXT.DOWN_MEGA)
            mega = Mega.from_credentials(TEXT.MEGA_EMAIL, TEXT.MEGA_PASSWORD)
            file_name = mega.download_from_url(url)
            logger.info(f"Загрузка Mega завершена: {file_name}")
            sent_message.edit_text(TEXT.DOWN_COMPLETE)
            download_status = True
        except Exception as e:
            logger.error(f"Ошибка загрузки Mega: {e}")
            sent_message.edit_text("Ошибка загрузки Mega !!")
    
    else:
        try:
            file_name = url.split("/")[-1]
            logger.info(f"Начало загрузки: {file_name}")
            sent_message.edit_text(TEXT.DOWNLOAD)
            file_name = wget_dl(str(url))
            logger.info(f"Загрузка завершена: {file_name}")
            sent_message.edit_text(TEXT.DOWN_COMPLETE)
            download_status = True

        except Exception as e:
            if TEXT.DOWN_TWO:
                try:
                    sent_message.edit_text(
                        f"Ошибка загрузчика 1: {e} \\n\\n Загрузчик 2: Начало загрузки...")
                    downloader = SmartDL(url)
                    downloader.start()
                    file_name = downloader.get_dest()
                    download_status = True
                except Exception as ex:
                    logger.error(f"Ошибка загрузки через SmartDL: {ex}")
                    sent_message.edit_text(f"Ошибка загрузки: {ex}")
                    download_status = False
            else:
                logger.error(f"Ошибка загрузки: {e}")
                sent_message.edit_text(f"Ошибка загрузки: {e}")
                download_status = False
    
    if file_name and "error" in file_name:
        sent_message.edit_text("Ошибка загрузки !!")
        try:
            os.remove(file_name)
        except Exception as e:
            logger.error(f"Ошибка при удалении файла после загрузки: {e}")
        return

    if download_status:
        sent_message.edit_text(TEXT.UPLOADING)
        try:
            file_size = os.path.getsize(file_name) / 1048576
            file_size = round(file_size)
            file_name_for_message = file_name.split("/")[-1]
            try:
                file_link = upload(file_name, update,
                                  context, TEXT.drive_folder_name)
            except Exception as e:
                logger.error(f"Ошибка загрузки на Google Drive: {e}")
                sent_message.edit_text(f"Ошибка загрузки: {e}")
            else:
                sent_message.edit_text(TEXT.DOWNLOAD_URL.format(
                    file_name_for_message, file_size, file_link), parse_mode=ParseMode.HTML)
            try:
                os.remove(file_name)
            except Exception as e:
                logger.error(f"Ошибка при удалении файла после загрузки на Google Drive: {e}")
        except Exception as e:
             logger.error(f"Ошибка при загрузке файла: {e}")
             sent_message.edit_text(f"Ошибка загрузки: {e}")
             try:
                os.remove(file_name)
             except Exception as ex:
                logger.error(f"Ошибка при удалении файла после ошибки: {ex}")
    else:
        sent_message.edit_text("Произошла ошибка при загрузке.")



def status_command(update, context):
    """
    Отправляет сообщение о статусе бота.

    Args:
        update (:obj:`telegram.Update`): Обновление от Telegram API.
        context (:obj:`telegram.ext.CallbackContext`): Контекст обратного вызова.
    """
    context.bot.send_message(
        chat_id=update.message.chat_id, text=TEXT.UPDATE, parse_mode=ParseMode.HTML)


# Регистрация обработчиков команд
update_status = CommandHandler('update', status_command)
dp.add_handler(update_status)

start_handler = CommandHandler('start', start_command)
dp.add_handler(start_handler)

downloader_handler = MessageHandler(Filters.regex(r'http'), upload_command)
dp.add_handler(downloader_handler)

help_handler = CommandHandler('help', help_command)
dp.add_handler(help_handler)

auth_handler = CommandHandler('auth', auth_command)
dp.add_handler(auth_handler)

token_handler = MessageHandler(Filters.text, token_command)
dp.add_handler(token_handler)

revoke_handler = CommandHandler('revoke', revoke_token_command)
dp.add_handler(revoke_handler)


updater.start_polling()
updater.idle()
```