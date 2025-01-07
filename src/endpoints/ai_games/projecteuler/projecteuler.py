from __future__ import annotations
from types import SimpleNamespace
## \file /src/endpoints/ai_games/projecteuler/projecteuler.py
# -*- coding: utf-8 -*-

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
from src.utils.file import get_filenames
from src.utils.printer import pprint

class ProjectEuler:
	"""
	алиса просит у модели предоствить ей текст задачи,
	борис просит у модели предоставить ему решение
	"""
	lang:str
	alice:GoogleGenerativeAI
	bob:GoogleGenerativeAI
	base_path:Path = gs.path.endpoints / 'ai_games' / 'projecteuler' 
	alice_instruction:str
	bob_instruction:str
	config: 'SimpleNamespace' = j_loads_ns(base_path / 'projecteuler.json')

	def __init__(self, lang:str = 'en'):
		""""""
		self.lang = lang
		alice_instruction:str = Path(self.base_path / 'assets' / 'instructions' / f'alice.{self.lang}.md').read_text(encoding='UTF-8')
		bob_instruction:str = Path(self.base_path / 'assets' / 'instructions' / f'bob.{self.lang}.md').read_text(encoding='UTF-8')		
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
		for i in range(135,900):
			q = self.alice_instruction.replace('<PROBLEM_NUMBER>', str(i))
			response = await self.alice.ask(q)
			self.save_problem(str(i), response)
			time.sleep(25)

	async def solve_probems(self):
		""""""
		...
		problems_to_solve_files_list:list = get_filenames(self.base_path /  {self.lang} / 'problems')
		for file_name in problems_to_solve_files_list:
			problem_number = int(file_name.split('_')[1].split('.')[0])
			q = self.bob_instruction.replace('<PROBLEM_TO_SOLVE>', Path(self.base_path / {self.lang} / 'problems' / file_name).read_text(encoding='UTF-8'))
			response  =  await self.bob.ask(q)
			self.save_problem_solve(problem_number,response)
			time.sleep(25)



	def save_problem(self, problem_number:str, problem_text:str):
		""""""
		...
		output_file:Path = self.base_path / {self.lang} / 'problems' / f'e_{problem_number}.md'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(problem_text,encoding='UTF-8')
		print(f'Saved problem No {problem_number}')

	def save_problem_solve(self, problem_number:str, solve_text:str):
		""""""
		...
		output_file:Path = self.base_path / {self.lang} / 'solves' / f'e_{problem_number}.md'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(solve_text,encoding='UTF-8')
		print(f'Saved sovle No {problem_number}')

if __name__ == '__main__':
	languges_list: list = ['ru','he','en']
	for lang in languges_list:
		euler = ProjectEuler(lang)
		asyncio.run( euler.collect_problems())
		asyncio.run( euler.solve_probems())