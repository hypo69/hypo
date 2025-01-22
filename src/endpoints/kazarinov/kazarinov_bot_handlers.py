## \file /src/endpoints/kazarinov/bot_handlers.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
.. module:: src.endpoints.kazarinov.bot_handlers 
	:platform: Windows, Unix
	:synopsis: Обработка событий телеграм бота

Обработчик собтий телеграм-бота  `kazarinov_bot`
=========================================================================================

Модуль обрабатывает команды, переданные телеграм-боту, такие как работа с ссылками OneTab
и выполнение связанных сценариев.

Пример использования
--------------------

Пример использования класса `BotHandler`:

.. code-block:: python

    handler = BotHandler()
    handler.handle_url(update, context)
"""

import asyncio
import random
import requests
from pathlib import Path
from typing import Optional, Any
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import CallbackContext

import header
from src import gs
from src.logger.logger import logger
from src.webdriver.playwright import Playwrid
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.utils.url import is_url
from src.utils.printer import pprint as print



class BotHandler:
    """Исполнитель команд, полученных ботом."""

    mexiron: MexironBuilder

    def __init__(self):
        """Инициализация обработчика событий телеграм-бота."""
        self.mexiron = MexironBuilder()

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Обработка текстовых сообщений с маршрутизацией на основе URL."""
        q = update.message.text
        if q == '?':
            await update.message.reply_photo(
                gs.path.endpoints / 'kazarinov' / 'assets' / 'user_flowchart.png'
            )
            return

        if is_url(q):
            await self.handle_url(update, context)
            return

        if q in ('--next', '-next', '__next', '-n', '-q'):
            await self.handle_next_command(update)
            return

        answer = self.model.chat(q)
        await update.message.reply_text(answer)

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """Обработка URL, присланного пользователем."""
        response = update.message.text
        if response.startswith(('https://one-tab.com', 'http://one-tab.com',
                                'https://www.one-tab.com', 'http://www.one-tab.com')):
            price, mexiron_name, urls = self.fetch_target_urls_onetab(response)
            if not urls:
                await update.message.reply_text('Некорректные данные.')
                return

            if await self.mexiron.run_scenario(
                update=update,
                context=context,
                urls=urls if isinstance(urls, list) else [urls],
                price=price,
                mexiron_name=mexiron_name
            ):
                await update.message.reply_text('Готово!')
                return
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')

    async def handle_next_command(self, update: Update) -> None:
        """Обработка команды '--next' и её аналогов."""
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.error('Ошибка чтения вопросов: %s', ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    def fetch_target_urls_onetab(self, one_tab_url: str) -> list[str] | bool:
        """
        Извлечение целевых URL с указанного URL OneTab.

        Args:
            one_tab_url (str): URL страницы OneTab.

        Returns:
            list[str] | bool: Список целевых URL или False при ошибке.
        """
        try:
            response = requests.get(one_tab_url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Извлечение ссылок
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Извлечение данных из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            if not data:
                price = ''
                mexiron_name = gs.now
            else:
                # Разбивка данных на цену и имя
                parts = data.split(maxsplit=1)
                price = int(parts[0]) if parts[0].isdigit() else ''
                mexiron_name = parts[1] if len(parts) > 1 else gs.now

            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            logger.error('Ошибка при выполнении запроса: %s', ex)
            return



    async def help_command(self, update: Update, context: CallbackContext) -> None:
        """Handle the /help command."""
        self.update = update
        self.context = context
        await self.update.message.reply_text(
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )

    async def send_pdf(self, pdf_file: str | Path) -> None:
        """Handle the /sendpdf command to generate and send a PDF file."""
        try:
            # Отправка PDF-файла пользователю
            with open(pdf_file, 'rb') as pdf_file_obj:
                await self.update.message.reply_document(document=pdf_file_obj)

        except Exception as ex:
            logger.error('Ошибка при отправке PDF-файла: ', ex)
            await self.update.message.reply_text('Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')

    async def handle_voice(self, update: Update, context: CallbackContext) -> None:
        """Handle voice messages and transcribe the audio."""
        self.update = update
        self.context = context
        try:
            # Получаем файл голосового сообщения
            voice = self.update.message.voice
            file = await self.context.bot.get_file(voice.file_id)
            file_path = gs.path.temp / f'{voice.file_id}.ogg'
            
            # Сохраняем файл на локальной системе
            await file.download_to_drive(file_path)

            # Здесь можно добавить обработку файла (распознавание речи), например, с помощью Google Speech-to-Text
            transcribed_text = self.transcribe_voice(file_path)
            
            # Отправляем распознанный текст пользователю
            await self.update.message.reply_text(f'Распознанный текст: {transcribed_text}')
        
        except Exception as ex:
            logger.error('Ошибка при обработке голосового сообщения: ', ex)
            await self.update.message.reply_text('Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')

    async def transcribe_voice(self, file_path: Path) -> str:
        """Transcribe voice message using a speech recognition service."""
        # Пример заглушки, замените это на реальную логику распознавания речи
        return 'Распознавание голоса ещё не реализовано.'

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """Handle received documents.

        Args:
            update (Update): Update object containing the message data.
            context (CallbackContext): Context of the current conversation.

        Returns:
            str: Content of the text document.
        """
        self.update = update
        self.context = context
        file = await self.update.message.document.get_file()
        tmp_file_path = await file.download_to_drive()  # Save file locally
        await update.message.reply_text(f'Файл сохранене в {tmp_file_path}')
        return True 

    async def handle_message(self, update: Update, context: CallbackContext) -> str:
        """Handle any text message.

        Args:
            update (Update): Update object containing the message data.
            context (CallbackContext): Context of the current conversation.

        Returns:
            str: Text received from the user.
        """
        self.update = update
        self.context = context
        return self.update.message.text

    async def handle_log(self, update: Update, context: CallbackContext) -> None:
        """Handle log messages."""
        log_message = update.message.text
        logger.info(f"Received log message: {log_message}")
        await update.message.reply_text("Log received and processed.")
