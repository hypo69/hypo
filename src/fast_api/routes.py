## \file /src/fast_api/routes.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.fast_api.routes
	:platform: Windows, Unix
	:synopsis: Манипулирование маршрутами в серевере

"""
import header
from src.endpoints.bots.telegram.bot_handlers import BotHandler
class Routes:

	def tegram_message_handler(self):
		""" """
		bot_nahdlers = BotHandler()
		telega_message_handler = bot_nahdlers.handle_message
