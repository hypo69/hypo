from __future__ import annotations
from types import SimpleNamespace
## \file hypotez/src/endpoints/ai_games/projecteuler/projecteuler.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.ai_games.projecteuler 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import time
from pathlib import Path

import header
from src import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.jjson import j_loads_ns

class ProjectEuler:
	"""
	алиса просит у модели предоствить ей текст задачи,
	борис просит у модели предоставить ему решение
	"""
	alice:GoogleGenerativeAI
	bob:GoogleGenerativeAI
	base_path:Path = gs.path.endpoints / 'ai_games' / 'projecteuler' 
	alice_instruction:str = Path(base_path / 'assets' / 'instructions' / 'alice.md').read_text(encoding='UTF-8')
	bob_instruction:str = Path(base_path / 'assets' / 'instructions' / 'alice.md').read_text(encoding='UTF-8')
	config: 'SimpleNamespace' = j_loads_ns(base_path / 'projecteuler.json')

	def __init__(self):
		""""""
		
		self.bob = GoogleGenerativeAI(
                model_name=self.config.model_name,
                api_key=gs.credentials.gemini.onela
            )

		self.alice = GoogleGenerativeAI(
                model_name=self.config.model_name,
                api_key=gs.credentials.gemini.onela
            )

	async def collect_problems(self):
		""""""
		...
		for i in range(1,900):
			q = self.alice_instruction.replace('<PROBLEM_NUMBER>', str(i))
			response = await self.alice.ask(q)
			self.save_code(str(i), response)
			print(response)
			time.sleep(25)


	def save_code(self, problem_number:str, problem_text:str):
		""""""
		...
		output_file:Path = self.base_path / 'problems' / f'e_{problem_number}.md'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(problem_text,encoding='UTF-8')
		print(f'Saved problem No {problem_number}')

if __name__ == '__main__':
	euler = ProjectEuler()
	asyncio.run( euler.collect_problems())