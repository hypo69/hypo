## \file /src/endpoints/hypo69/code_assistant/onela_bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.endpoints.hypo69.code_assistant.onela_bot
	:platform: Windows, Unix
	:synopsis: Модуль диалога с моделью ассистента программиста через чат телеграм. 
    """
MODE = 'dev'
import header
import asyncio
from pathlib import Path
from typing import List, Optional, Dict
from types import SimpleNamespace
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.bots.telegram import TelegramBot

class OnelaBot(TelegramBot):
	"""Взимодействие с моделью ассистента программиста"""

	model:GoogleGenerativeAI = GoogleGenerativeAI(api_key = gs.credentials.gemini.onela, generation_config = {"response_mime_type": "text/plain"})
	def __init__(self):
		""""""
		super().__init__(gs.credentials.telegram.onela_bot)

	async def handle_message(self, update: Update, context: CallbackContext) -> None:
		"""Handle text messages with URL-based routing."""
		q = update.message.text
		user_id = update.effective_user.id
		answer = self.model.chat(q)
		await update.message.reply_text(answer)

if __name__ == "__main__":
    bot = OnelaBot()
    asyncio.run(bot.application.run_polling())
