## \file ../src/suppliers/kazarinov/bot.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Kazarinov's specific bot with customized behavior. """

import asyncio
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
import random

import header
from src import gs
from src.bots.telegram_bot import TelegramBot
from src.webdriver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.suppliers.kazarinov.parser_onetab import fetch_target_urls_onetab
from src.suppliers.kazarinov.scenarios.scenario_pricelist import Mexiron
from src.suppliers.kazarinov import gemini_chat
from src.utils.file import read_text_file, recursive_read_text_files
from src.utils.string.url import is_url

class KazarinovTelegram(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    token = gs.credentials.telegram.bot.kazarinov
    d:Driver
    mexiron: Mexiron
    model_chat:GoogleGenerativeAI
    model_adviser:GoogleGenerativeAI
    system_instruction:str
    questions_list:list = recursive_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'q', ['*.*'], as_list = True )
    timestamp:str

    def __init__(self):
        """Initialize the Kazarinov bot."""
        super().__init__(self.token)
        self.d = Driver(Chrome)
        self.mexiron = Mexiron(self.d)
        self.timestamp = gs.now
        # Register command handlers
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))

        # Register message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

        self.base_path = gs.path.data / 'kazarinov' / 'mexironim' / self.timestamp
        
        self.system_instruction: str = read_text_file(gs.path.data / 'kazarinov' / 'prompts' /  'system_instruction.txt')
        self.correct_answers: str = read_text_file(gs.path.data / 'kazarinov' / 'prompts' /  'correct_anwers.txt')
        self.advise_instructions: str = read_text_file(gs.path.data / 'kazarinov' / 'prompts' /  'model_adviser.txt')
        api_key = gs.credentials.gemini.kazarinov
        self.model = GoogleGenerativeAI(api_key = api_key, system_instruction = self.system_instruction, generation_config = {"response_mime_type": "text/plain"})
        self.model.ask(self.correct_answers)
        self.model.ask(self.system_instruction)
        # self.model_adviser = GoogleGenerativeAI(api_key = api_key, system_instruction = self.advise_instructions, generation_config = {"response_mime_type": "text/plain"})
        # self.model_adviser.ask(self.correct_answers)
        # self.model_adviser.ask(self.system_instruction)

        


    async def start(self, update: Update, context: CallbackContext) -> None:
        """Override the /start command with custom behavior."""
        await update.message.reply_text('Hello! This is Kazarinov’s custom bot.')
        # Optionally, call the parent method if needed
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> bool:
        """Override the message handler with custom logic."""
        ...
        response = update.message.text
        if response.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
            if await self.mexiron.run_scenario(response): #< - одна ссылка на морлеви надо вытащить максимум данных со страницы
                return  await update.message.reply_text('Готово!')
            return  await update.message.reply_text('Хуёвенько')

        if response.startswith('https://www.one-tab.com'): # <- пока обрабатываются ссылки только на морлеви
            price, mexiron_name, urls = fetch_target_urls_onetab(response)
            if not all([price, mexiron_name, urls]):      # <- проверка, что все три значения False
                error_message = (
                'Ошибка на сервере OneTab. Такое редко, но бывает. '
                'Отдохни, попей кофе и попробуй еще раз через часок, другой.'
                )
                return  await update.message.reply_text(error_message)


            if await self.mexiron.run_scenario(price = price, mexiron_name = mexiron_name, urls = urls):
                return  await update.message.reply_text('Готово!\nСсылку я вышлю на whatsapp')
            return  await update.message.reply_text('Хуёвенько. Попробуй еще раз')

        if response.startswith(('--next','-next','__next')) or response=='-n' or response=='-q':
                q = random.choice( self.questions_list)
                await update.message.reply_text(q)
                a =  self.model.ask(q)
                return await update.message.reply_text(a)
        else:
            if not is_url(response):
                return await update.message.reply_text(self.model.ask(response))

        

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """Override document handler with additional logging."""
        file_content = await super().handle_document(update, context)
        await update.message.reply_text(f'Received your document. Content: {file_content}')
        return file_content

if __name__ == "__main__":
    kt = KazarinovTelegram()
    # Start the bot (add necessary logic to run the event loop if needed)
    asyncio.run(kt.application.run_polling())
