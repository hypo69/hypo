## \file /src/endpoints/ai_games/101_basic_games/101_basic_games.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.ai_games.101_basic_games 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import time
from pathlib import Path
import header
from src import gs

from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai import OpenAIModel
from src.endpoints.hypo69.code_assistant import CodeAssistant

from src.utils.jjson import j_loads, j_loads_ns
from src.utils.file import get_filenames
from src.utils.printer import pprint

class Games101Basic():
	"""	"""
	lang:str
	bob:GoogleGenerativeAI
	alice:GoogleGenerativeAI
	base:str = '101_basic_computer_games'
	base_path:Path = gs.path.endpoints / 'ai_games' / base

	def __init__(self, lanf:str = 'en'):
		""""""
		config  = j_loads_ns(self.base_path / '101_basic_computer_games.json')
		self.lang = lang
		#system_instruction = Path(self.base_path / 'assets' / 'instructions' / 'raw.md').read_text(encoding='UTF-8')
		system_instruction = Path(self.base_path / 'assets' / 'instructions' / 'fts.txt').read_text(encoding='UTF-8')
		
		self.bob = GoogleGenerativeAI(
                model_name=config.model_name,
                api_key=gs.credentials.gemini.onela,
                system_instruction = system_instruction,
            )

		code_assistant = CodeAssistant()


	@property
	def games_list(self):
		"""
		Генерация списка имен игр из файлов в каталоге 'rules'.
		Извлекает имя игры из каждого файла, приводя его к верхнему регистру и заменяя подчеркивания на пробелы.
		"""
		rules_files = get_filenames(self.base_path / self.lang / 'rules')
		games:list = []
		for file_name in rules_files:
			if file_name == ('README.MD' or 'TOC.MD'):
				continue
			game_name = file_name.split('_', 1)[1].split('.')[0]  # Разделяем по подчеркиванию и точке
			games.append( game_name.upper().replace('_', ' ') ) # Преобразуем в верхний регистр и заменяем подчеркивания на пробелы
		return games
	
	async def generate_python_code(self):
		""""""
		for game in self.games_list:
			command_instruction:str = Path(self.base_path / 'assets' / 'instructions' / f'{self.base}_write_code.{self.lang}.md').read_text(encoding='UTF-8')
			q = command_instruction.replace('<GAME>',f'<{game}>')
			print(game)
			response = await self.bob.ask(q)
			if response.startswith(('```', '```python')) and response.endswith(('```', '```\n')):
				# Удаление начальных ```
				response = response.lstrip('`')
				# Удаление начальных 'python' после кавычек
				if response.startswith('python'):
					response = response[len('python'):].lstrip()
				# Удаление закрывающих ```
				response = response.rstrip('`').rstrip()
			self.save_code(game , response)
			time.sleep(20)

	def save_code(self, game:str, code:str):
		""""""
		...
		output_file:Path = self.base_path / self.lang / game / f'{game.lower().replace(' ','_')}.py'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(code,encoding='UTF-8')
		print('saved')

	async def generate_repository_toc(self):
		""""""
		...

		command_instruction = Path(self.base_path / 'assets' / 'instructions' / f'{self.base}_create_toc.{self.lang}.md').read_text(encoding='UTF-8')
		q = command_instruction + str(self.games_list) 
		response = await self.bob.ask(q)
		
		output_file:Path = self.base_path / self.lang  / 'TOC.MD'
		output_file.parent.mkdir(parents=True, exist_ok=True)
		output_file.write_text(response,encoding='UTF-8')

	async def translate_games()




if __name__ == '__main__':

	langs_list:list = ['ru','he']
	executed_langs_list:list = ['en']
	for lang in langs_list:
		print(f'Start: {lang}')
		g101 = Games101Basic(lang)
		asyncio.run( g101.generate_repository_toc())
		#asyncio.run( g101.generate_python_code())