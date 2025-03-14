## \file /src/endpoints/math_challenges/scenarios/scenario.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
.. module:: src.endpoints.math_challenges.scenarios.scenario 
	:platform: Windows, Unix
	:synopsis: Сценарий для математических задач

"""
from typing import Optional

import os
from urllib import response
import header
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.logger import logger

##########################################################################################
ENDPOINT = 'math_challenges'
from src import USE_ENV
if USE_ENV:
    from dotenv import load_dotenv
    load_dotenv()

USE_ENV = False # <~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##########################################################################################

class Scenario:
	"""
	Класс для сценария математических задач.
	В этом классе задается вопрос модели машинного обучения.
	У модели есть несколько реэимов работы, которые можно настроить.
	функция get_question() возвращает вопрос, который задает модель.
	"""
	model: GoogleGenerativeAI

	def __init__(self, api_key:Optional[str] = None, task: Optional[str]=None):
		"""
		Инициализирует класс Scenario.
		Args:
			task: Строка с заданием.
		"""
		api_key:str = api_key if api_key else os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.teacher
		try:
			system_instruction:str = (gs.path.endpoints / ENDPOINT / 'instructions' / 'system_instruction.he.md').read_text(encoding='UTF-8')

			self.model = GoogleGenerativeAI(
			api_key=api_key,
			system_instruction=system_instruction,
			generation_config={'response_mime_type': 'text/plain'}
			)
		except Exception as ex:
			logger.error(f"Error loading model, or instructions or API key:", ex)
			...

	def ask_question(self, q:Optional[str] = None) -> str:
		"""
		Args:
			q (str): Вопрос.
		"""
		q:str = q if q else self.get_question()
		response = self.model.ask(q)


	def get_question(self) -> str:
		"""
		Решает задачу.
		Returns:
			Решение задачи.
		"""
		# Решение задачи
		return  (gs.path.endpoints / ENDPOINT / 'instructions' / 'challenges' / 'sequence_generation_guide.he.md').read_text(encoding='UTF-8')